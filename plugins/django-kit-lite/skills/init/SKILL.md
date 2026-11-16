---
name: init
description: Use when the user asks to set up, onboard or initialise Claude Code for a Django project, or to create, extend or update its CLAUDE.md or AGENTS.md (how to install, run, test and lint the project).
---

# Initialise a Django project for Claude Code

## Detect first

Read the real setup before writing anything:

```bash
ls -a | head -50
ls manage.py pyproject.toml setup.cfg tox.ini pytest.ini ruff.toml .ruff.toml mypy.ini Makefile Dockerfile docker-compose.y*ml uv.lock poetry.lock Pipfile requirements*.txt 2>/dev/null
grep -n -i -E '^(django|djangorestframework|pytest-django|pytest|ruff|black|flake8|mypy|django-stubs|celery|psycopg2?|mysqlclient)[=<>~\[ ]' requirements*.txt 2>/dev/null | head -20
grep -n -i -E 'django|pytest|ruff|black|mypy|requires-python' pyproject.toml 2>/dev/null | head -20
grep -rn "DJANGO_SETTINGS_MODULE" manage.py pytest.ini pyproject.toml tox.ini 2>/dev/null | head -4
grep -n -E "ENGINE|^DEBUG|SECRET_KEY" */settings*.py */settings/*.py 2>/dev/null | head -8
ls .github/workflows 2>/dev/null; ls CLAUDE.md AGENTS.md 2>/dev/null
python3 --version; ls -d venv .venv 2>/dev/null
```

Work out: **Django and Python versions** (from the requirements or lock file, not from memory), the **test runner** (`./manage.py test` unless pytest-django is configured), the **settings module** and how local settings or environment variables are supplied, the **database engine**, which **formatter or linter** the repo uses (`ruff`, `black`, `flake8`), whether **mypy** is run in CI, and how dependencies are installed (`pip -r`, `uv`, `poetry`). Read the CI workflow files and the `Makefile` for the commands the project itself runs, and the README for the run steps.

If `CLAUDE.md` or `AGENTS.md` exists, read it fully. **Never delete or rewrite its existing lines.** Follow the project's conventions over this kit's defaults. Also read `CONTRIBUTING.md` if present and obey any rules in it.

## Write CLAUDE.md

1. Read `references/CLAUDE.template.md` in this skill's directory.
2. Fill every placeholder from what you detected. Only write a command if you saw it in the README, the CI file, a Makefile target, `manage.py` or a config file in this repository. Delete lines you cannot confirm instead of guessing.
3. No `CLAUDE.md`: create it from the template. One exists: **append** a `## Stackproof` section (the template's five parts become `###` subsections); if an earlier `## Stackproof` section exists, replace only that section. Leave everything else byte for byte. If only `AGENTS.md` exists, put the section in `CLAUDE.md` with a first line `See AGENTS.md for project rules.` and do not edit `AGENTS.md`.

## Required sections

The result must contain Project facts, Commands, Conventions, a **Never** section (protected paths and blocked commands in plain words) and the Stackproof line. A CLAUDE.md without a Never section is incomplete. Back every command with `(source: <file>)` naming the README, CI file, Makefile or docs URL; if you cannot, leave it out. Do not write "unconfirmed" or "assumed" in the file.

## Report

If the guard hook is loaded, list what it blocks: committed migrations, `.env` files, `local_settings.py`, local SQLite files, `staticfiles/` and virtualenv directories, `manage.py flush`, `migrate <app> zero`, `DROP DATABASE/TABLE`, production-settings runs, and force pushes. Then summarise facts found, commands written, commands dropped, and files changed.

Sources: https://docs.djangoproject.com/en/6.0/ref/django-admin/, https://docs.djangoproject.com/en/6.0/topics/testing/overview/
