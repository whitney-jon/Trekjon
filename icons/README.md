# Header icons

One transparent PNG per sport theme, shown in the video header next to the title. The render script loads `icons/<theme>.png` (via `--icons-dir icons`) and falls back to its built-in drawn icon when a file is missing.

| File | Used for |
|---|---|
| `f1.png` | Formula 1 (included: chequered flag) |
| `hockey.png` | NHL / ice hockey (included: crossed sticks and puck) |
| `tennis.png` | Tennis |
| `basketball.png` | NBA / basketball |
| `football.png` | Football / soccer |
| `worldcup.png` | World Cup / trophies |
| `olympics.png` | Olympics / medals |
| `money.png` | Earnings / money |

Guidelines: square, transparent background, at least 512×512 px, centred with a little padding. It is drawn at 128×128 px in the video. No league, team or brand logos.

- `motogp.png` — official MotoGP wordmark (white, transparent). Wide logos (wider than 2.2:1) are shown stacked: logo centred above the title.
