# Who has scored the most T20 international runs?

**Style:** Notebook (Hand-made Moss & Peach) — `handmade_notebook_style.py`, `NB_PRESET=moss`, `--theme cricket` (no cricket icon file in icons/, so the script's drawn cricket ball is used), country flags, `--palette`, `--engage --seconds 43.97` → 1,319 frames (44.0 s; re-cut on 5 Nov 2026 at the user's request because the 30 s version moved too fast, everything else unchanged), 20 time points (~2.2 s each).

## Title
Who has scored the most T20 international runs?

## Description
At the end of 2006, in the format's second year, South Africa's Graeme Smith led the T20 international run chart with just 188. So who has scored the most T20 international runs?

This race tracks men's T20I career runs year by year from 2006 to the end of 2025 (2005 games included). The lead changes hands again and again: Misbah-ul-Haq, Brendon McCullum's long reign, Martin Guptill, then India's Virat Kohli and Rohit Sharma, before Pakistan's Babar Azam moved to the top in 2025.

Europe has its own star in the race: Ireland's Paul Stirling climbs into the top five with 3,798 runs, alongside England's Jos Buttler on 3,869 — and the UAE's Muhammad Waseem breaks into the top ten as an associate-nation batter.

Key Highlights:
McCullum's Reign: Brendon McCullum led from 2009 to 2017 and became the first to 2,000 T20I runs on 29 March 2014.
Kohli Breaks 4,000: Virat Kohli became the first to 4,000 T20I runs on 10 November 2022 against England in Adelaide.
World Cup Farewell: Rohit Sharma and Virat Kohli finished their T20I careers in 2024 on 4,231 and 4,188 runs.
Babar Takes Over: Babar Azam ended 2025 as the all-time leader with 4,429 runs.

Data includes: Babar Azam, Rohit Sharma, Virat Kohli, Jos Buttler, Paul Stirling, Martin Guptill, Mohammad Rizwan, David Warner, Muhammad Waseem, and other historical top-ten contenders.

Data Source: ESPNcricinfo Statsguru T20I batting records (career totals to 31 Dec of each year, 2006–2025); Wikipedia "List of Twenty20 International records" (dated revisions 2014–2025).

#Cricket #T20I #T20Cricket #CricketStats #BabarAzam #ViratKohli #RohitSharma #PaulStirling

## Music (pick from the YouTube/Facebook in-app audio library so it's licensed and won't be muted or claimed)
1. "Jai Ho" – A. R. Rahman
2. "Don't Stop Me Now" – Queen
3. "Shut Up and Dance" – Walk the Moon

## Data notes / reading of the brief
- Men's T20 internationals, all nations (associate players included as ESPNcricinfo counts them, e.g. UAE's Muhammad Waseem and Malaysia's Virandeep Singh). Career totals at 31 December of each year; 2005 matches are included in the first (2006) row. 2026 (incl. the 2026 T20 World Cup) is excluded.
- World XI / ICC appearances count, as ESPNcricinfo includes them (Shoaib Malik, Shahid Afridi, David Miller) — flags show the player's own nation. Ross Taylor's 2025 runs were for Samoa, so his (ghost-row) flag switches to Samoa in 2025.
- Flags: `flags/my.png` (Malaysia, for Virandeep Singh, 10th at the end of 2025 in the faint ghost row) was not in the repo; it was drawn from the national flag design for this video and added. Replace it with your own upload if you prefer.

## QA
- Final row (end of 2025) checked against two sources: ESPNcricinfo Statsguru (to 31 Dec 2025) and Wikipedia's 31 Dec 2025 revision of "List of Twenty20 International records": Babar 4,429, Rohit 4,231, Kohli 4,188, Buttler 3,869, Stirling 3,798 (both); Guptill 3,531 and Warner 3,277 (Wikipedia player career stats); Rizwan 3,414 (Wikipedia average table, Dec 2025); Waseem 3,184 (Statsguru; Wikipedia Dec 2025 tables give the same 91 innings, 2,098 balls and 187 sixes but not the run total).
- Intermediate spot checks against dated Wikipedia revisions: Dec 2014 top 5 (McCullum 2,105, Jayawardene 1,493, Dilshan 1,466, Warner 1,444, Duminy 1,399), Dec 2018 (Guptill 2,271, Rohit 2,237, Malik 2,190, Kohli 2,167, McCullum 2,140), Dec 2021 (Guptill 3,299, Kohli 3,227, Rohit 3,197, Babar 2,620, Finch 2,608), Dec 2022 (Kohli 4,008, Rohit 3,853, Guptill 3,531, Babar 3,355, Stirling 3,181) — all match the CSV exactly.
- Events:
  - 2014: McCullum first to 2,000 T20I runs — 65 v Netherlands, Chattogram, 29 Mar 2014 (ESPNcricinfo Statsguru innings list; Wikipedia records table).
  - 2022: Kohli first to 4,000 T20I runs — 50 v England, Adelaide, 10 Nov 2022 (ESPNcricinfo Statsguru innings list; Wikipedia "fastest to 4,000" record, 10 November 2022).
- Lead changes on screen: Smith → Misbah (2008) → McCullum (2009) → Guptill (2018) → Rohit/Kohli (2019–20) → Guptill (2021) → Kohli (2022) → Rohit (2024) → Babar (2025).
- Checks: `--check-flags` (all present incl. new my.png); safe-zone check passed; preview stills and 7 frames from the MP4 reviewed; final frame matches the CSV; event cards dark text on peach, readable.
