# Stackproof Django kit (lite)

A free starter for Claude Code in Django projects. It contains an `init` skill that writes a CLAUDE.md with commands checked against your repository, a `migration` skill for reversible migrations that never edit committed ones, a `django-reviewer` subagent, and a guard hook that protects committed migrations, `.env` files, `local_settings.py` and your database.

Install:

```
/plugin marketplace add beingRealFrank/stackproof
/plugin install django-kit-lite@stackproof
```

Then run `/django-kit-lite:init` in your project. The hooks need Python 3.8+, make no network calls and collect nothing. Turn the guard off for one session with `STACKPROOF_GUARD=off claude`. MIT licensed.
