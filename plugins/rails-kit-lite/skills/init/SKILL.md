---
name: init
description: Use when the user asks to set up, onboard or initialise Claude Code for a Ruby on Rails app, or to create, extend or update its CLAUDE.md or AGENTS.md (how to install, run, test and lint the project).
---

# Initialise a Rails project for Claude Code

## Detect first

Read the real setup before writing anything:

```bash
ls -a | head -50
cat .ruby-version 2>/dev/null; grep -n -E '^\s+rails \(|^\s+(rspec-rails|minitest|brakeman|standard|rubocop-rails-omakase|bullet|factory_bot_rails|pg|mysql2|trilogy|sqlite3) \(' Gemfile.lock | head -20
grep -n -E "^gem ['\"](rails|rspec-rails|brakeman|standard|rubocop|bullet|pg|mysql2|trilogy|sqlite3)['\"]" Gemfile
ls bin; ls spec test .rspec .standard.yml .rubocop.yml Makefile Procfile.dev docker-compose.y*ml 2>/dev/null | head -30
grep -n "adapter" config/database.yml config/database.yml.sample 2>/dev/null | head -4
grep -rn "load_defaults" config/application.rb
ls .github/workflows 2>/dev/null; ls CLAUDE.md AGENTS.md 2>/dev/null
```

Work out: **Rails and Ruby versions**, the **test runner** (RSpec if `spec/` and `.rspec` exist, otherwise Minitest in `test/`), the **database adapter**, which **linter** the repo uses (`standardrb`, `rubocop`), whether **Brakeman** is in the Gemfile, and which `bin/` binstubs exist. Read CI workflow files and the `Makefile` for the commands the project itself runs.

If `CLAUDE.md` or `AGENTS.md` exists, read it fully. **Never delete or rewrite its existing lines.** Follow the project's conventions over this kit's defaults.

## Write CLAUDE.md

1. Read `references/CLAUDE.template.md` in this skill's directory.
2. Fill every placeholder from what you detected. Only write a command if you saw its binstub, Makefile target, CI step or gem in this repository. Delete lines you cannot confirm instead of guessing.
3. No `CLAUDE.md`: create it from the template. One exists: **append** a `## Stackproof` section (the template's five parts become `###` subsections); if an earlier `## Stackproof` section exists, replace only that section. Leave everything else byte for byte. If only `AGENTS.md` exists, put the section in `CLAUDE.md` with a first line `See AGENTS.md for project rules.` and do not edit `AGENTS.md`.

## Required sections

The result must contain Project facts, Commands, Conventions, a **Never** section (protected paths and blocked commands in plain words) and the Stackproof line. A CLAUDE.md without a Never section is incomplete. Back every command with `(source: <file>)` naming the binstub, Makefile, CI file or docs URL; if you cannot, leave it out. Do not write "unconfirmed" or "assumed" in the file.

## Report

If the guard hook is loaded, list what it blocks: `db/schema.rb` and `structure.sql`, committed migrations, `config/master.key` and encrypted credentials, `vendor/`, `rails db:drop/reset/schema:load` (outside `RAILS_ENV=test`), production environment runs, `credentials:edit/show`, and force pushes. Then summarise facts found, commands written, commands dropped, and files changed.

Sources: https://guides.rubyonrails.org/command_line.html, https://guides.rubyonrails.org/testing.html
