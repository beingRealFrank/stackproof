#!/usr/bin/env python3
"""Stackproof guard hook (PreToolUse). Blocks risky shell commands and edits to protected paths.
Reads the hook event JSON on stdin and rules from ../hooks/rules.json. Exit 2 = block (reason on stderr), 0 = allow.
Standard library only. No network. Fails open on any internal error. Disable for one session: STACKPROOF_GUARD=off"""
import fnmatch, json, os, re, subprocess, sys

def tracked(proj, rel):
    try:
        return subprocess.run(['git', '-C', proj, 'ls-files', '--error-unmatch', rel], capture_output=True, timeout=5).returncode == 0
    except Exception:
        return False

def main():
    if os.environ.get('STACKPROOF_GUARD', '').lower() == 'off':
        return 0
    try:
        ev = json.load(sys.stdin)
        root = os.environ.get('CLAUDE_PLUGIN_ROOT') or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(root, 'hooks', 'rules.json')) as f:
            rules = json.load(f)
    except Exception:
        return 0
    tool = ev.get('tool_name', '')
    ti = ev.get('tool_input') or {}
    proj = os.environ.get('CLAUDE_PROJECT_DIR') or ev.get('cwd') or os.getcwd()
    if tool == 'Bash':
        cmd = ti.get('command', '') or ''
        for r in rules.get('bash_block', []):
            if re.search(r['re'], cmd) and not (r.get('unless') and re.search(r['unless'], cmd)):
                print('Stackproof guard blocked this command: ' + r['why'] + ' If the user explicitly wants it, ask them to run it themselves.', file=sys.stderr)
                return 2
        return 0
    if tool in ('Edit', 'Write', 'MultiEdit', 'NotebookEdit'):
        p = ti.get('file_path') or ti.get('notebook_path') or ''
        if not p:
            return 0
        ap = os.path.normpath(os.path.join(proj, p))
        rel = os.path.relpath(ap, proj)
        if rel.startswith('..'):
            return 0
        rel = rel.replace(os.sep, '/')
        for r in rules.get('path_block', []):
            if not any(fnmatch.fnmatch(rel, g) for g in r['globs']):
                continue
            if any(fnmatch.fnmatch(rel, g) for g in r.get('except', [])):
                continue
            if r.get('only_if_tracked') and not tracked(proj, rel):
                continue
            print('Stackproof guard blocked editing ' + rel + ': ' + r['why'], file=sys.stderr)
            return 2
        text = ' '.join(str(ti.get(k) or '') for k in ('content', 'new_string')) + ' '.join(str(e.get('new_string') or '') for e in (ti.get('edits') or []) if isinstance(e, dict))
        for r in rules.get('content_block', []):
            if any(fnmatch.fnmatch(rel, g) for g in r['globs']) and re.search(r['re'], text):
                print('Stackproof guard blocked this change to ' + rel + ': ' + r['why'], file=sys.stderr)
                return 2
    return 0

if __name__ == '__main__':
    sys.exit(main())
