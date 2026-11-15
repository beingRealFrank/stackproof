---
name: migration
description: Use when adding or changing a database migration in a Rails app: new tables, columns, indexes or constraints, backfilling data, or fixing a failed or mistaken migration.
---

# Rails migrations

## Detect first

```bash
grep -n "adapter" config/database.yml config/database.yml.sample 2>/dev/null | head -4
grep -n -E '^\s+(rails|pg|mysql2|trilogy|sqlite3|strong_migrations) \(' Gemfile.lock
ls db; ls db/migrate | tail -3; head -3 "db/migrate/$(ls db/migrate | tail -1)"
git status --short db | head; ls bin/rails
```

Note the **adapter** (PostgreSQL, MySQL or SQLite), the `ActiveRecord::Migration[x.y]` version the newest migration uses, and whether `db/schema.rb` or `db/structure.sql` is the schema format. Follow the repo's existing migration style.

## Rules

1. **New change, new file.** `bin/rails generate migration AddPinnedAtToStories pinned_at:datetime:index` writes `db/migrate/<timestamp>_add_pinned_at_to_stories.rb`. The name tells the generator what to build (`AddXToY`, `RemoveXFromY`, `CreateZs`).
2. **Never edit a committed migration.** Check `git ls-files db/migrate/<file>`: if tracked, it may have run elsewhere. Fix it with another migration. The guard hook blocks this too.
3. **Never hand-edit `db/schema.rb`.** It is rewritten by `bin/rails db:migrate`; commit the regenerated file with the migration.
4. **Make it reversible.** Use `change` with reversible commands, or write `up` and `down`. Inside `change`, wrap one-way SQL in `reversible do |dir| dir.up { … } dir.down { … } end`. A migration that raises `ActiveRecord::IrreversibleMigration` needs a good reason.
5. **Indexes.** Add an index for every new foreign key and for columns you filter or sort on. On **PostgreSQL only**, on a large live table use `disable_ddl_transaction!` and `add_index :t, :c, algorithm: :concurrently`. Do not use `algorithm: :concurrently` on MySQL or SQLite.
6. **Defaults and NOT NULL on big tables.** Adding a column with a default can rewrite or lock the table on some adapters and versions. Add it nullable first, backfill, then add the constraint in a later migration.
7. **Data backfills** go in a separate migration or a background job, not in the same migration as the schema change. In a migration, use a throwaway model class defined inside the migration, not the app's model.
8. Prefer `add_reference … foreign_key: true` for associations and match the existing key type.

## Run and verify

```bash
bin/rails db:migrate
bin/rails db:migrate:status | tail -5
bin/rails db:rollback          # one step back: proves the migration reverses
bin/rails db:migrate
git diff --stat db
```

The migration, the regenerated schema file and any model changes are one commit. Run the related tests (`tests` skill). Never run `db:reset`, `db:drop` or `db:schema:load` except with `RAILS_ENV=test`.

Sources: https://guides.rubyonrails.org/active_record_migrations.html
