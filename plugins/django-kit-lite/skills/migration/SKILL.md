---
name: migration
description: Use when adding or changing a Django migration: new models or fields, indexes, constraints, data migrations with RunPython, squashing, or fixing a failed or mistaken migration.
---

# Django migrations

## Detect first

```bash
ls manage.py; grep -n -i -E '^django[=<>~\[ ]' requirements*.txt 2>/dev/null | head -2
grep -n -E "ENGINE" */settings*.py */settings/*.py 2>/dev/null | head -3
ls */migrations | tail -8
git status --short | grep migrations | head
./manage.py showmigrations 2>&1 | tail -8
```

Note the **database engine** (PostgreSQL, MySQL or SQLite), how the project names migrations, and whether the newest migrations are committed (`git ls-files <app>/migrations`). Follow the repo's existing style.

## Rules

1. **Change the model first, then generate.** `./manage.py makemigrations <app> -n short_name` writes the next file in `<app>/migrations/`. Read the generated file before moving on.
2. **Never edit a committed migration.** Check with `git ls-files <app>/migrations/<file>`: if tracked, it may have run elsewhere. Fix it with a new migration. The guard hook blocks this too. A migration you just generated and have not committed can be regenerated freely.
3. **Prove nothing is missing.** `./manage.py makemigrations --check --dry-run` exits non-zero when model changes have no migration; run it before finishing.
4. **Make it reversible.** Schema operations reverse automatically. A `migrations.RunPython(forward)` needs a reverse function as its second argument, or `migrations.RunPython.noop` when undoing is safe to skip. `migrations.RunSQL` needs `reverse_sql`.
5. **Data migrations** are their own migration file. Use `apps.get_model("app", "Model")` inside the function, never import the real model, and keep the schema change in a separate earlier migration.
6. **New required column on a big table.** Add it with `null=True` or a default, backfill in a data migration, then tighten it in a later migration. Check what SQL runs: `./manage.py sqlmigrate <app> <number>`.
7. **Indexes and constraints** go in the model's `Meta` (`indexes`, `constraints`) so `makemigrations` generates them; do not hand-write `RunSQL` for what the ORM can express.
8. **Squashing** is optional and only for old, fully-applied migrations: `./manage.py squashmigrations <app> <start> <end>`; keep the originals until every deployment has migrated past them.

## Run and verify

```bash
./manage.py migrate
./manage.py showmigrations <app> | tail -3
./manage.py migrate <app> <previous_number>    # proves the migration reverses
./manage.py migrate
./manage.py makemigrations --check --dry-run
```

Never run `migrate <app> zero` or `flush`. Run the related tests (`tests` skill). The model change and its migration are one commit.

Sources: https://docs.djangoproject.com/en/6.0/topics/migrations/, https://docs.djangoproject.com/en/6.0/ref/migration-operations/
