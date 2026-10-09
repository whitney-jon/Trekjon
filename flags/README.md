# Country flags

Flag images for the bar-end chips. The render script loads `flags/<code>.png` (via `--flags flags`). Codes are lowercase. PNG, 3:2 or 4:3, about 128 px wide (shown at 68×40 px).

## Rules (also in the daily-run playbook)
1. **Accurate to the time period.** Use the nation the athlete or team represented at that time (East Germany, West Germany, Soviet Union, Yugoslavia...). If an athlete changed nation during the video, the CSV can switch flags on a given year, e.g. `Jaromir Jagr #CS|CZ:1993`.
2. **What the athlete represents themselves as**, per the governing body's records (e.g. Rory McIlroy = Northern Ireland on tour, not GB/UK).
3. **The nation as the sport recognises it.** Olympics: Great Britain (`gb`). Football, rugby, darts, snooker, Commonwealth Games: England, Scotland, Wales, Northern Ireland (never UK). Cricket: England. Rugby union Ireland: all-Ireland (`ie`).

## File names
| File | Nation |
|---|---|
| `<iso>.png` | Current nations by ISO 3166 alpha-2: `us.png`, `de.png`, `fr.png`, `ie.png`, `gb.png`... |
| `gb-eng.png` | England |
| `gb-sct.png` | Scotland |
| `gb-wls.png` | Wales |
| `gb-nir.png` | Northern Ireland |
| `su.png` | Soviet Union (to 1991) |
| `eun.png` | Unified Team (1992) |
| `dd.png` | East Germany (1949–1990) |
| `frg.png` | West Germany (1949–1990) |
| `eua.png` | United Team of Germany (Olympics 1956–1964) |
| `yu.png` | Yugoslavia (to 1992) |
| `fry.png` | FR Yugoslavia (1992–2003) |
| `scg.png` | Serbia and Montenegro (2003–2006) |
| `cs.png` | Czechoslovakia (to 1992) |
| `wi.png` | West Indies (cricket) |

A run checks every flag a video needs before rendering (`--check-flags`) and won't render with a missing flag; it reports which file to add instead.
