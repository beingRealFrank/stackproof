# Stackproof Ruby on Rails kit (lite)

A free starter for Claude Code in Rails apps. It contains an `init` skill that writes a CLAUDE.md with commands checked against your repository, a `migration` skill for reversible migrations that never hand-edit `db/schema.rb`, a `rails-reviewer` subagent, and a guard hook that protects the schema file, committed migrations and credentials.

Install:

```
/plugin marketplace add beingRealFrank/stackproof
/plugin install rails-kit-lite@stackproof
```

Then run `/rails-kit-lite:init` in your project. The hooks need Python 3.8+, make no network calls and collect nothing. Turn the guard off for one session with `STACKPROOF_GUARD=off claude`. MIT licensed.
