## Project facts
- Framework: Next.js {version} (App Router); request hook file: {proxy.ts | middleware.ts}.
- Supabase: CLI project in {path to supabase/}; migrations in {path}/migrations; generated types at {path(s)}.
- Package manager: {pnpm | npm | yarn | bun}; layout: {single app | monorepo: apps/..., packages/...}.

## Commands
- Install: {pnpm install}
- Dev server: {script from package.json}
- Start local Supabase: {script or `supabase start`}
- New migration: `supabase migration new <name>`; reset local DB: {script or `supabase db reset`}
- Regenerate types: {typegen script}
- Test one file: {runner command with a path}; all tests: {script}
- Typecheck / lint / format: {scripts}

## Conventions
- {Server auth helper the repo uses (for example requireUser) and where it lives.}
- {Server Actions location and validation library (zod?).}
- {Lint/format tool in use.}

## Never
- Never edit a committed migration: add a new one.
- Never edit generated `database.types.ts`: regenerate it.
- Never read or edit `.env*` files; never print the service-role key; never put a secret in a `NEXT_PUBLIC_` variable.
- Never run `supabase db push`, `db reset --linked` or `vercel --prod` yourself.
- Never commit secrets.

## Stackproof
Written by the Stackproof Next.js + Supabase kit {version}.
