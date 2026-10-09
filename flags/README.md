# Country flags

Flag images for the bar-end chips. The render script looks for `flags/<code>.png` (via `--flags flags`), where `<code>` is the lowercase ISO 3166 alpha-2 code used in the CSV headers (e.g. `gb.png`, `de.png`, `br.png`). Special codes: `en` England, `wl` Wales, `su` USSR, `dd` East Germany.

Guidelines: PNG, 3:2 or 4:3, about 128 px wide (shown at 68×40 px). If a flag is missing, the video shows the two-letter country code in a dark chip instead.
