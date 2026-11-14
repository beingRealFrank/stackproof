---
name: rls-policy
description: Use when creating or changing a Supabase table, view or storage bucket that the app reads from the client, or when writing, reviewing or testing row level security policies.
---

# Row level security for Supabase tables

## Detect first

```bash
find . -type d -path '*supabase/migrations' -not -path '*/node_modules/*' | head -3
grep -rn -i "enable row level security" --include=*.sql . 2>/dev/null | grep -v node_modules | head -5
grep -rn "auth.uid()" --include=*.sql . 2>/dev/null | grep -v node_modules | head -5
ls supabase/tests apps/*/supabase/tests 2>/dev/null | head
grep -n "schemas" supabase/config.toml apps/*/supabase/config.toml 2>/dev/null | head -3
```

Copy the style of the repo's existing policies (naming, which role clauses, helper functions such as an account-membership function). Follow the project's conventions over the defaults below.

## Rules

1. **Every table in an exposed schema (usually `public`) gets RLS in the same migration that creates it:** `alter table public.notes enable row level security;`. Without it, anyone with the anon key can read and write it.
2. **One policy per operation** (`select`, `insert`, `update`, `delete`), each `to authenticated` unless the data is truly public. `update` needs both `using` and `with check`; `insert` needs `with check`.
3. **Wrap the auth function in a select:** `(select auth.uid()) = user_id`. Supabase documents this form so Postgres evaluates it once per statement instead of per row.
4. **No `using (true)` on write policies**, and no `using (true)` on reads unless the table is meant to be public (say so in a comment).
5. **Index the columns the policy filters on** (for example `user_id`).
6. **The service-role key bypasses RLS.** Use it only in server-only code (see `server-auth`); never in a client component, never in `NEXT_PUBLIC_*`.
7. If the project has a helper (a security definer function that checks membership), use it instead of repeating a join in each policy.

## Template (own-rows table)

```sql
create table public.notes (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users (id) on delete cascade default auth.uid(),
  body text not null,
  created_at timestamptz not null default now()
);

create index notes_user_id_idx on public.notes (user_id);

alter table public.notes enable row level security;

create policy "notes_select_own" on public.notes for select to authenticated
  using ((select auth.uid()) = user_id);
create policy "notes_insert_own" on public.notes for insert to authenticated
  with check ((select auth.uid()) = user_id);
create policy "notes_update_own" on public.notes for update to authenticated
  using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);
create policy "notes_delete_own" on public.notes for delete to authenticated
  using ((select auth.uid()) = user_id);
```

Put it in a new migration (`migration` skill), never in an old one.

## Test with pgTAP

Create a test file with `supabase test new notes_rls`, which writes under `supabase/tests/`. Check that a user sees only their rows and an anonymous user sees none, then run `supabase test db` (the repo may wrap it in a script, such as `supabase:test`: check `package.json`). Run `supabase db lint` too if the repo uses it. The local database must be running (`supabase start`).

Report which tables changed, the policies added, and the test result. If you could not run the tests, say so.

Sources: https://supabase.com/docs/guides/database/postgres/row-level-security, https://supabase.com/docs/guides/local-development/testing/overview, https://supabase.com/docs/reference/cli/supabase-test-db
