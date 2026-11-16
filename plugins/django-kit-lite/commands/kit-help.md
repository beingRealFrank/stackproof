---
description: List the Stackproof Django kit's skills, subagents and guard rules
---
# Stackproof Django kit (lite)

**Skills** (run as `/django-kit-lite:<skill>`)
- `init`: detect the project's real setup and write or extend CLAUDE.md under a `## Stackproof` heading.
- `migration`: `makemigrations`, `--check --dry-run`, reversible `RunPython`, data migrations; never edit committed migrations.

**Subagents**: `django-reviewer`.

**Guard hook** blocks: force-push, `--no-verify`, `rm -rf` on root or home, `curl | sh`, `git reset --hard origin/...`, `manage.py flush`, `migrate <app> zero`, `DROP DATABASE/TABLE`, production-settings runs, and edits to committed migrations, `.env` files, `local_settings.py`, SQLite files, `staticfiles/` and virtualenv directories.

**Switch the guard off for one session:** `STACKPROOF_GUARD=off claude`

The full kit adds 4 more skills, 2 more subagents and the format hook: https://beingrealfrank.github.io/stackproof/kits/django.html
