# Who has scored the most rugby test tries?

**Style:** Notebook (Hand-made Sand & Bottle Green) — `handmade_notebook_style.py`, `NB_PRESET=sand`, `--theme rugby` (no rugby icon file in icons/, so the script's drawn rugby ball is used), country flags, `--palette` (8 of 20 rows are New Zealand), `--engage --seconds 30.27` → 899 frames (29.97 s; this data's pacing jumps from 899 to 903 frames, so exactly 900 wasn't reachable), 19 time points (~1.6 s each).

## Title
Who has scored the most rugby test tries?

## Description
At the end of 2007 Australia's David Campese still held the try record among the big rugby nations with 64, ahead of England's Rory Underwood and the All Blacks' Doug Howlett. So who has scored the most rugby test tries?

This race tracks men's test tries for players from the ten tier-one nations, year by year from 2007 to the end of 2025 (career totals carried in, British & Irish Lions tests included as each player's test record does). Shane Williams' surge took Wales to second place, Bryan Habana chased down Campese in 2016, and George North became the latest to break into the top five.

European rugby is at the heart of it: Wales' Shane Williams (60) and George North (49), England's Rory Underwood (50) and Ireland's Brian O'Driscoll (47) all sit in the final top ten alongside the Southern Hemisphere wings.

Key Highlights:
Campese's Long Reign: David Campese's 64 tries stood as the tier-one record for 20 years after he retired in 1996.
Shane Williams Signs Off: Williams scored in his final test against Australia on 3 December 2011 to finish on 60.
Habana Takes the Record: Bryan Habana's 65th try came against Argentina in Salta on 27 August 2016, and he finished on 67.
North Climbs: George North finished his Wales career in 2024 on 49 tries, level with Doug Howlett.

Data includes: Bryan Habana, David Campese, Shane Williams, Rory Underwood, George North, Doug Howlett, Brian O'Driscoll, Julian Savea, Joe Rokocoko, Christian Cullen, and other historical top-ten contenders.

Data Source: Wikipedia "List of leading rugby union test try scorers" and per-player international try lists (to 2025); French Wikipedia player test-match statistics tables.

#Rugby #RugbyUnion #TestRugby #RugbyStats #SixNations #BryanHabana #ShaneWilliams #AllBlacks

## Music (pick from the YouTube/Facebook in-app audio library so it's licensed and won't be muted or claimed)
1. "Seven Nation Army" – The White Stripes
2. "Swing Low, Sweet Chariot" – Ladysmith Black Mambazo (2007 RWC version)
3. "World in Union" – Kiri Te Kanawa

## Data notes / reading of the brief
- Men's test tries for players from the tier-one nations (England, Scotland, Wales, Ireland, France, Italy, South Africa, New Zealand, Australia, Argentina). Japan's Daisuke Ohata (69) and Hirotoki Onozawa (55) and Georgia's Akaki Tabutsadze (52) are left out under that rule.
- British & Irish Lions test tries are included in the player's total (as in the Wikipedia list and the players' official records): Shane Williams 58+2, Underwood 49+1, North 47+2, O'Driscoll 46+1, Gareth Thomas 40+1. The flag is the player's own nation (Lions tries shown under it).
- Calendar years; the first row (2007) carries every total from the start of each career. 2026 (in progress) is excluded, so Will Jordan (56 in Oct 2026) and Beauden Barrett show their end-of-2025 totals (45 each) and sit just outside the top ten.
- Will Jordan's 2021/2022 split differs between English (15/4) and French (10/9) Wikipedia; it only affects his ghost row below the list (17 v 12 in 2021); his end-of-2025 total (45) agrees in both.

## QA
- Final row (end of 2025) checked against two sources: English Wikipedia list/per-player try lists and French Wikipedia player statistics: Habana 67 (year-by-year identical in both), Campese 64 (English list + his numbered try list), Shane Williams 60 (58 Wales + 2 Lions, both), Underwood 50 (49 + 1 Lions), North 49 (47 + 2 Lions; French per-year table), Howlett 49, O'Driscoll 47 (46 + 1), Savea 46 (per-year identical), Rokocoko 46 (French per-year table), Cullen 46 (per-year identical), Jordan 45 and Barrett 45 at end of 2025 (both sources).
- Intermediate spot checks: Habana's year-by-year tries match exactly between the two sources (e.g. 13 in 2007, 7 in 2015); Savea and Cullen year-by-year match exactly; Rokocoko 17 tries in 2003 (French Wikipedia record note) = CSV; North's Wales tries per year sum to 47 and Lions 2 in 2013; Shane Williams passed Ieuan Evans' 33 on 20 Sep 2007 (French Wikipedia) — consistent with CSV (33 at end of 2006 → 40 at end of 2007).
- Events:
  - 2011: Shane Williams scores in his last test: 60 — try No. 60, Wales v Australia, Millennium Stadium, 3 Dec 2011 (Wikipedia "List of international rugby union tries by Shane Williams").
  - 2016: Habana passes Campese's record of 64 — try No. 65, Argentina v South Africa, Salta, 27 Aug 2016 (Wikipedia "List of international rugby union tries by Bryan Habana").
- Lead change on screen: Campese → Habana (2016).
- Checks: `--check-flags` (au, fr, gb-eng, gb-wls, ie, nz, za all present); safe-zone check passed; preview stills and 7 frames from the MP4 reviewed; final frame matches the CSV; event cards white text on brick red, readable.
