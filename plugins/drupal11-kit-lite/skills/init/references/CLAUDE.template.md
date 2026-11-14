## Project facts
- Framework: Drupal {core version from composer.lock or the drupal/core constraint}; PHP {version from composer.json "php" or CI}.
- Kind: {site | module | theme | distribution}; docroot: {web | docroot | none (module repo)}.
- Package manager: Composer. Runner: {ddev (prefix commands with `ddev `) | host}.
- Custom code: {web/modules/custom, web/themes/custom, or the repo root for a module}.

## Commands
- Install dependencies: {composer install}
- Rebuild caches: {drush cache:rebuild}
- Database updates: {drush updatedb}
- Config status / export / import: {drush config:status} / {drush config:export} / {drush config:import --diff first}
- Run one test: {vendor/bin/phpunit -c <docroot>/core path/to/Test.php}
- Run all tests of a module: {vendor/bin/phpunit -c <docroot>/core <path to module>}
- Lint/format: {vendor/bin/phpcs / vendor/bin/phpcbf with the project's phpcs.xml}

## Conventions
- {Coding standard in use: Drupal / DrupalPractice from phpcs.xml, or none found.}
- {Plugins: attributes (#[Block]) or annotations (@Block); hooks: OOP (#[Hook]) or procedural, as the repo already does.}
- {Config lives in: config/sync or config/install; config split in use: yes/no.}
- {Tests live in: tests/src/{Unit,Kernel,Functional,FunctionalJavascript}.}

## Never
- Never edit Drupal core, `vendor/`, or contrib modules, themes and profiles: patch through Composer or write a custom module.
- Never edit `settings.php` or uploaded files under `sites/*/files`.
- Never run `drush sql:drop`, `site:install`, `config:import -y` without showing the diff first, or an unscoped `composer update`.
- Never commit secrets.

## Stackproof
Written by the Stackproof Drupal 11 kit {version}.
