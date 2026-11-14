---
description: List the Stackproof Drupal 11 lite kit's skills, subagent and guard rules
---
# Stackproof Drupal 11 kit (lite)

**Skills** (run as `/drupal11-kit-lite:<skill>`)
- `init`: detect the project's real setup and write or extend CLAUDE.md under a `## Stackproof` heading.
- `module-scaffold`: a Drupal 11 module with `.info.yml`, services, attribute plugins and OOP hooks.

**Subagent**: `drupal-reviewer` (standards, access checks, cache metadata, XSS, config schema).

**Guard hook** blocks: force-push, `--no-verify`, `rm -rf` on root or home, `curl | sh`, `git reset --hard origin/...`, `drush sql:drop` and `site:install`, drush production aliases, `drush cim -y`, an unscoped `composer update`, and edits to Drupal core, `vendor/`, contrib code, `settings.php` and uploaded files.

**Switch the guard off for one session:** `STACKPROOF_GUARD=off claude`

The full kit adds 4 more skills, 2 more subagents and the format hook: https://beingrealfrank.github.io/stackproof/kits/drupal11.html
