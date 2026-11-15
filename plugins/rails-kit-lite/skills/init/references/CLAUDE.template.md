## Project facts
- Rails {version}, Ruby {version}; database adapter: {sqlite3 | postgresql | mysql2 | trilogy}.
- Tests: {RSpec in spec/ | Minitest in test/}; linter: {standardrb | rubocop}; Brakeman: {yes | no}.
- Layout: {app/models, app/controllers, app/views, anything unusual such as engines or app/jobs}.

## Commands
- Setup: {bin/setup}
- Run the app: {bin/rails server | bin/dev}
- Test one file: {bundle exec rspec spec/models/x_spec.rb | bin/rails test test/models/x_test.rb}
- Test one example: {bundle exec rspec spec/models/x_spec.rb:LINE | bin/rails test test/models/x_test.rb:LINE}
- Test all: {bundle exec rspec | bin/rails test}
- Lint / format: {bundle exec standardrb --fix | bin/rubocop}
- Security scan: {bundle exec brakeman -q}
- Migrate: `bin/rails db:migrate`; status: `bin/rails db:migrate:status`

## Conventions
- {Style rules from the linter config and existing code.}
- {Where business logic lives (models, concerns, service objects) and how callbacks are used.}
- {Factories or fixtures; how tests are organised.}

## Never
- Never edit `db/schema.rb` or `db/structure.sql`: write a migration and run `bin/rails db:migrate`.
- Never edit a committed migration: add a new one.
- Never read or edit `config/master.key` or encrypted credentials.
- Never run `db:drop`, `db:reset` or `db:schema:load` outside `RAILS_ENV=test`; never run anything with `RAILS_ENV=production`.
- Never edit `vendor/`.
- Never commit secrets.

## Stackproof
Written by the Stackproof Rails kit {version}.
