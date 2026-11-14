---
name: module-scaffold
description: Use when creating a new Drupal module, or adding a service, plugin (block, field formatter, etc.) or hook implementation to a Drupal 10.3+/11 module.
---

# Scaffold or extend a Drupal 11 module

## Detect first

```bash
ls *.info.yml web/modules/custom/*/*.info.yml docroot/modules/custom/*/*.info.yml 2>/dev/null | head
grep -n core_version_requirement $(ls *.info.yml web/modules/custom/*/*.info.yml 2>/dev/null | head -3)
grep -n '"drupal/core' composer.json
ls src src/Plugin src/Hook 2>/dev/null
grep -rln --include=*.php -e '#\[Hook(' -e '#\[Block(' -e '@Block(' . 2>/dev/null | head -5
```

Find the module's machine name (the `*.info.yml` file name), where custom modules live, and whether the repo already uses attributes or annotations, and OOP or procedural hooks. Follow the repo's conventions for naming, namespaces, dependency injection and tests. **New plugins use attributes, even when older plugins in the repo still use annotations** (Drupal 10.3+ and 11 discover both, so they coexist). Hooks follow the repo's style (see Hooks).

## New module

Create `<modules dir>/<machine_name>/` with:

```yaml
# <machine_name>.info.yml
name: 'Human name'
type: module
description: 'One sentence.'
package: Custom
core_version_requirement: ^11
```

Use `^10.3 || ^11` when the module must also run on Drupal 10 (plugin attributes need 10.3+; the OOP hook attribute needs 11.1+). Never write the old `core: 8.x` key. Add `dependencies:` as `drupal:node`, `drupal:views` (project:module form). Add `<machine_name>.services.yml` only when you add services.

## Plugins: attributes first

On Drupal 10.3+ and 11 plugins are discovered from PHP attributes. A block:

```php
<?php

declare(strict_types=1);

namespace Drupal\my_module\Plugin\Block;

use Drupal\Core\Block\Attribute\Block;
use Drupal\Core\Block\BlockBase;
use Drupal\Core\StringTranslation\TranslatableMarkup;

#[Block(
  id: 'my_module_example',
  admin_label: new TranslatableMarkup('Example'),
)]
class ExampleBlock extends BlockBase {

  public function build(): array {
    return ['#markup' => $this->t('Hello'), '#cache' => ['max-age' => 0]];
  }

}
```

File path: `src/Plugin/Block/ExampleBlock.php`. Set real cache metadata (`#cache` with `tags`, `contexts`, `max-age`) instead of leaving defaults when the output depends on data; use `max-age => 0` only when it truly cannot be cached. Inject services with `ContainerFactoryPluginInterface` and a `create()` method rather than calling `\Drupal::service()` in the class.

If `core_version_requirement` allows a release below 10.3 (for example `^10.2 || ^11`), attributes will not be discovered there. Raise it to `^10.3 || ^11` in the same change and say so plainly in your reply, with the reason. Use an annotation (`@Block(...)` in the docblock) only if the user tells you the module must keep supporting the lower release.

## Hooks: OOP when core allows

From Drupal 11.1, hook implementations are methods on classes in the `Drupal\<module>\Hook` namespace, marked with `#[Hook('hook_name')]`; the class is registered automatically.

```php
namespace Drupal\my_module\Hook;

use Drupal\Core\Hook\Attribute\Hook;

class MyModuleHooks {

  #[Hook('cron')]
  public function cron(): void {
  }

}
```

To also support 10.1 to 11.0, keep the procedural function in `<machine_name>.module` as a thin shim that calls the same class (register the class as a service in `services.yml`). If the module supports only 11.1+, use the OOP class alone. If the repo already uses procedural hooks and supports Drupal 10, stay procedural.

## Services

```yaml
services:
  my_module.helper:
    class: Drupal\my_module\Helper
    arguments: ['@entity_type.manager']
```

Constructor-inject dependencies; do not call `\Drupal::` inside service classes.

## Finish

1. `php -l` each new PHP file (or run it in the project's runner).
2. If the project has `phpcs.xml*`, run `vendor/bin/phpcs --standard=<its file> <module dir>` and fix findings.
3. Enable and rebuild caches with the project's runner: `drush pm:enable <machine_name>` then `drush cache:rebuild` (prefix `ddev` when `.ddev/` exists).
4. Add a test (use the `drupal-tests` skill).

Sources: https://www.drupal.org/node/3442349 (OOP hooks), https://www.drupal.org/docs/develop/creating-modules/understanding-hooks
