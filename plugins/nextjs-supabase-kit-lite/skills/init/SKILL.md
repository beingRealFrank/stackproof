---
name: init
description: Use when the user asks to set up, onboard or initialise Claude Code for a Next.js and Supabase project, or to create, extend or update its CLAUDE.md or AGENTS.md (how to install, run, test and lint the project).
---

# Initialise a Next.js + Supabase project for Claude Code

## Detect first

Read the real setup before writing anything:

```bash
ls -a | head -40
cat package.json | head -60
ls pnpm-workspace.yaml pnpm-lock.yaml yarn.lock package-lock.json bun.lockb turbo.json 2>/dev/null
ls -d apps/* packages/* 2>/dev/null | head -20
find . -name config.toml -path '*supabase*' -not -path '*/node_modules/*' | head
find . -type d -path '*supabase/migrations' -not -path '*/node_modules/*' | head
find . \( -name 'proxy.ts' -o -name 'middleware.ts' \) -not -path '*/node_modules/*' | head
find . -name 'database.types.ts' -not -path '*/node_modules/*' | head
ls .prettierrc* .oxfmtrc* .oxlintrc.json eslint.config.* biome.json vitest.config.* playwright.config.* 2>/dev/null
ls CLAUDE.md AGENTS.md apps/*/CLAUDE.md apps/*/AGENTS.md 2>/dev/null
```

Work out: **package manager** (the lockfile that exists), **monorepo or not** (`pnpm-workspace.yaml`, `turbo.json`, `apps/`), **Next.js version** and whether the request hook file is `proxy.ts` (Next 16) or `middleware.ts`, where **`supabase/`** lives (it may be under `apps/web/`), the **types file** path(s), the **test runner** (Vitest, Jest, Playwright) and the **lint/format** tool the repo actually uses (the scripts in `package.json`, not a guess).

If `CLAUDE.md` or `AGENTS.md` exists (also under `apps/*`), read it fully. **Never delete or rewrite its existing lines.** Follow the project's conventions over this kit's defaults.

## Write CLAUDE.md

1. Read `references/CLAUDE.template.md` in this skill's directory.
2. Fill every placeholder from what you detected. Each command must be a `package.json` script, a `Makefile` target or a Supabase CLI command whose config you saw in the repo. Write scripts as the repo defines them (`pnpm --filter web supabase:typegen`, not a command you made up).
3. No `CLAUDE.md`: create it from the template. One exists: **append** a `## Stackproof` section (the template's five parts become `###` subsections); if an earlier `## Stackproof` section exists, replace only that section. Leave everything else byte for byte. If only `AGENTS.md` exists, put the section in `CLAUDE.md` with a first line `See AGENTS.md for project rules.` and leave `AGENTS.md` alone.

## Required sections

The result must contain Project facts, Commands, Conventions, a **Never** section (protected paths and blocked commands in plain words) and the Stackproof line. A CLAUDE.md without a Never section is incomplete. Back every command with `(source: <file or URL>)`; if you cannot, leave it out. Do not write "unconfirmed" or "assumed" in the file.

## Report

If the guard hook is loaded, list what it blocks: committed Supabase migrations, `.env*` files, generated `database.types.ts`, `node_modules`, `.next`, `supabase db push`, `db reset --linked`, `vercel --prod`, printing the service-role key, a `NEXT_PUBLIC_` variable holding a secret, and force pushes. Then summarise facts found, commands written, commands dropped, and files changed.

Sources: https://supabase.com/docs/guides/local-development/overview, https://nextjs.org/docs/app/api-reference/file-conventions/proxy
