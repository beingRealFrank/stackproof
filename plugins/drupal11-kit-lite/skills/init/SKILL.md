---
name: init
description: Use when the user asks to set up, onboard or initialise Claude Code for a Drupal site, module, theme or distribution, or to create, extend or update its CLAUDE.md or AGENTS.md (how to install, run, test and lint the project).
---

# Initialise a Drupal project for Claude Code

## Detect first

Read the real setup before writing anything. Run these and keep the output:

```bash
ls -a | head -40
test -f composer.json && grep -n -E '"(drupal/core|drupal/core-recommended|drush/drush|drupal/core-dev|phpunit/phpunit|drupal/coder|mglaman/phpstan-drupal|palantirnet/drupal-rector|drupal/upgrade_status)"|"type"|"name"' composer.json
test -f composer.lock && grep -n -A1 -E '"name": "(drupal/core|drush/drush)"' composer.lock | head -8
ls -d web docroot .ddev .lando.yml phpunit.xml phpunit.xml.dist phpcs.xml phpcs.xml.dist .phpcs.xml phpstan.neon phpstan.neon.dist 2>/dev/null
ls *.info.yml 2>/dev/null
test -f composer.json && grep -n -A12 '"scripts"' composer.json | head -20
ls CLAUDE.md AGENTS.md 2>/dev/null
```

Work out:

- **Project kind.** `"type": "drupal-module"` or a root `*.info.yml` means a single module or theme (no docroot, no `web/core`). `"type": "project"` with `web/` or `docroot/` means a site.
- **Docroot** (`web`, `docroot`, or none), **core constraint** (the `drupal/core` or `drupal/core-recommended` line), **Drush** (`vendor/bin/drush` exists?), **runner** (`ddev` if `.ddev/` exists, else host).
- **Test setup.** `phpunit.xml(.dist)` in the project root or `<docroot>/core/phpunit.xml.dist`. A module repo has no `web/core/`, so say that tests need a full Drupal codebase around it.
- **Lint**: which of `phpcs.xml*`, `phpstan.neon*` exist, and any `composer.json` `scripts` entries.

If `CLAUDE.md` or `AGENTS.md` exists, read it fully. **Never delete or rewrite its existing lines.** Follow the project's existing conventions over this kit's defaults.

## Write CLAUDE.md

1. Read `references/CLAUDE.template.md` in this skill's directory.
2. Fill every placeholder from what you detected. Only include a command if you saw its file or script in this repository (`composer.json` scripts, `.ddev/`, `vendor/bin/...`, a CI workflow under `.github/` or `.gitlab-ci.yml`). Delete the lines you cannot confirm instead of guessing.
3. If no `CLAUDE.md` exists, create it from the template.
4. If one exists, **append** a `## Stackproof` section (the template's five parts become `###` subsections). If an earlier `## Stackproof` section exists, replace only that section. Leave everything else byte for byte.
5. If only `AGENTS.md` exists, do the same to `CLAUDE.md` and add a line `See AGENTS.md for project rules.` at the top of the new section; do not edit `AGENTS.md`.

## Required sections

The result must contain the template's five parts: Project facts, Commands, Conventions, a **Never** section (the protected paths and blocked commands in plain words) and the Stackproof line. A CLAUDE.md without a Never section is incomplete. Every command you write must be backed by something a reader can check: a file or script in this repository, or an official docs page whose URL you put next to the command in the form `(source: <file or URL>)`. Do not write a command that has neither. When the repository itself cannot run the command (a module repo has no `web/core`), write one line saying what is missing and where the command runs, instead of a command that would fail here. Do not write the words "unconfirmed" or "assumed" in the file.

## Report

If the guard hook is installed (the kit's `hooks/` directory is loaded), list what it blocks: Drupal core, `vendor/`, contrib modules, themes and profiles, `settings.php`, uploaded files, `drush sql:drop`, `site:install`, `cim -y`, an unscoped `composer update`, and force pushes. Then print a summary: facts found, commands written, commands dropped because unconfirmed, and the file(s) changed.

Sources: https://www.drupal.org/docs/develop/standards/coding-standards, https://www.drush.org/13.x/commands/config_import/
