# Stackproof Next.js + Supabase kit (lite)

A free starter for Claude Code in Next.js App Router projects that use Supabase. It contains an `init` skill that writes a CLAUDE.md with commands checked against your repository, an `rls-policy` skill for row level security policies and pgTAP tests, a `nextjs-reviewer` subagent, and a guard hook that protects committed migrations, env files and generated types.

Install:

```
/plugin marketplace add beingRealFrank/stackproof
/plugin install nextjs-supabase-kit-lite@stackproof
```

Then run `/nextjs-supabase-kit-lite:init` in your project. The hooks need Python 3.8+, make no network calls and collect nothing. Turn the guard off for one session with `STACKPROOF_GUARD=off claude`. MIT licensed.
