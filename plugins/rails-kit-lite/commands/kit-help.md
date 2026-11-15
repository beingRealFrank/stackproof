---
description: List the Stackproof Rails kit's skills, subagents and guard rules
---
# Stackproof Ruby on Rails kit (lite)

**Skills** (run as `/rails-kit-lite:<skill>`)
- `init`: detect the app's real setup and write or extend CLAUDE.md under a `## Stackproof` heading.
- `migration`: reversible migrations, safe indexes, backfills; never hand-edit `db/schema.rb`.

**Subagents**: `rails-reviewer`.

**Guard hook** blocks: force-push, `--no-verify`, `rm -rf` on root or home, `curl | sh`, `git reset --hard origin/...`, `rails db:drop/reset/schema:load` outside `RAILS_ENV=test`, production-environment runs, `credentials:edit/show`, and edits to `db/schema.rb`, `db/structure.sql`, committed migrations, `config/master.key`, encrypted credentials and `vendor/`.

**Switch the guard off for one session:** `STACKPROOF_GUARD=off claude`

The full kit adds 4 more skills, 2 more subagents and the format hook: https://beingrealfrank.github.io/stackproof/kits/rails.html
