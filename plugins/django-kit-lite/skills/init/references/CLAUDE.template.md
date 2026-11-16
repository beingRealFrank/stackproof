## Project facts
- Django {version}, Python {version}; settings module: {module}; database: {sqlite3 | postgresql | mysql}.
- Tests: {manage.py test | pytest-django}; linter/formatter: {ruff | black | flake8}; mypy in CI: {yes | no}.
- Layout: {apps and where templates, static files and management commands live}.

## Commands
- Setup: {pip install -r requirements.txt | uv sync}
- Migrate: `./manage.py migrate`; new migration: `./manage.py makemigrations`; check for missing ones: `./manage.py makemigrations --check --dry-run`
- Run the app: {./manage.py runserver}
- Test one module: {./manage.py test app.tests.test_x | pytest path/to/test_x.py}
- Test all: {./manage.py test | pytest}
- Lint / format: {ruff format . | black .}
- Type check: {mypy --strict app}

## Conventions
- {Style rules from the linter config and existing code.}
- {Where business logic lives (models, managers, services) and how views are written.}
- {Fixtures or factories; how tests are organised.}

## Never
- Never edit a committed migration: add a new one with `makemigrations`.
- Never read or edit `.env` files or `local_settings.py`; never commit secrets.
- Never run `manage.py flush`, `migrate <app> zero`, or SQL that drops data; never run against production settings.
- Never edit local database files, `staticfiles/` or the virtualenv.

## Stackproof
Written by the Stackproof Django kit {version}.
