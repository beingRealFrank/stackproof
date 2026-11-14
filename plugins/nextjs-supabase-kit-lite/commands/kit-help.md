---
description: List the Stackproof Next.js + Supabase lite kit's skills, subagent and guard rules
---
# Stackproof Next.js + Supabase kit (lite)

**Skills** (run as `/nextjs-supabase-kit-lite:<skill>`)
- `init`: detect the project's real setup and write or extend CLAUDE.md under a `## Stackproof` heading.
- `rls-policy`: enable RLS on new tables, write per-operation policies with `(select auth.uid())`, test with pgTAP.

**Subagent**: `nextjs-reviewer` (client/server boundary, leaked secrets, caching, `"use client"` sprawl).

**Guard hook** blocks: force-push, `--no-verify`, `rm -rf` on root or home, `curl | sh`, `git reset --hard origin/...`, `supabase db push`, `db reset --linked`, remote `migration repair/squash`, printing the service-role key, `vercel --prod`, edits to committed migrations, `.env*` files, generated `database.types.ts`, `node_modules` and `.next`, and `NEXT_PUBLIC_` variables that hold a secret.

**Switch the guard off for one session:** `STACKPROOF_GUARD=off claude`

The full kit adds 4 more skills, 2 more subagents and the format hook: https://beingrealfrank.github.io/stackproof/kits/nextjs-supabase.html
