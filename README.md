# Stackproof

Claude Code kits for Drupal 11, Next.js + Supabase, Rails and Django, each tested against a real open-source repository.

## Free lite install

```
/plugin marketplace add beingRealFrank/stackproof
/plugin install drupal11-kit-lite@stackproof
/plugin install nextjs-supabase-kit-lite@stackproof
/plugin install rails-kit-lite@stackproof
/plugin install django-kit-lite@stackproof
```

## Lite versus full kit

| | Lite (free, MIT) | Full kit |
|---|---|---|
| `init` skill (writes CLAUDE.md) | yes | yes |
| First workflow skill | yes | yes |
| More workflow skills | no | 4 more |
| Reviewer subagent | yes | yes, plus 2 more |
| Guard hook | yes | yes |
| Format hook | no | yes |

Full kits: https://beingrealfrank.github.io/stackproof/

## Verification

| Kit | Fixture | Commit | Cases | Suite | Without kit |
|---|---|---|---|---|---|
| Drupal 11 | localgov_directories | af3551c | 5/6 | 0.86 | 0.65 |
| Next.js + Supabase | makerkit-lite | 9ff430d | 6/6 | 1.00 | 0.74 |
| Ruby on Rails | lobsters | 28bc8d6 | 6/6 | 0.92 | 0.78 |
| Django | healthchecks | cb5c976 | 6/6 | 1.00 | 0.74 |

## Contributing

Issues are welcome.

Claude and Claude Code are trademarks of Anthropic. Stackproof is an independent project by Frank Gilroy and is not affiliated with Anthropic.

MIT license.
