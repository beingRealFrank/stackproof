# Stackproof Drupal 11 kit (lite)

A free starter for Claude Code in Drupal 10.3+ and Drupal 11 projects. It contains an `init` skill that writes a CLAUDE.md with commands checked against your repository, a `module-scaffold` skill for modules, services, attribute plugins and OOP hooks, a `drupal-reviewer` subagent, and a guard hook that blocks destructive commands and edits to Drupal core, contrib code and settings.php.

Install:

```
/plugin marketplace add beingRealFrank/stackproof
/plugin install drupal11-kit-lite@stackproof
```

Then run `/drupal11-kit-lite:init` in your project. The hooks need Python 3.8+, make no network calls and collect nothing. Turn the guard off for one session with `STACKPROOF_GUARD=off claude`. MIT licensed.

Upgrading a site from Drupal 10? Liftpatch's free scanner gives a fixed price: https://beingrealfrank.github.io/liftpatch/#scan
