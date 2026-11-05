# Who has scored the most T20 international runs?

**Style:** Notebook (Hand-made Moss & Peach) — `handmade_notebook_style.py`, `NB_PRESET=moss`, `--theme cricket` (no cricket icon file in icons/, so the script's drawn cricket ball is used), country flags, bars in each team's kit colour (India light blue, Pakistan green, Australia gold, England blue, New Zealand black, Ireland green, South Africa green, Sri Lanka blue, West Indies maroon, Afghanistan blue; UAE red and Malaysia navy from their national colours), `--engage --seconds 44` → 1,320 frames (44.0 s), 21 time points (~2.1 s each). Updated 5 Nov 2026 at the user's request: 44 s, kit colours, and a final 'Nov 2026' point.

## Title
Who has scored the most T20 international runs?

## Description
At the end of 2006, in the format's second year, South Africa's Graeme Smith led the T20 international run chart with just 188. So who has scored the most T20 international runs?

This race tracks men's T20I career runs year by year from 2006 to November 2026 (2005 games included). The lead changes hands again and again: Misbah-ul-Haq, Brendon McCullum's long reign, Martin Guptill, then India's Virat Kohli and Rohit Sharma, before Pakistan's Babar Azam moved to the top in 2025 — and England's Jos Buttler climbs to second in 2026.

Europe has its own stars in the race: England's Jos Buttler is second on 4,384 and Ireland's Paul Stirling fifth on 3,895, while Malaysia's Virandeep Singh (3,644) and the UAE's Muhammad Waseem (3,371) break into the top ten as associate-nation batters.

Key Highlights:
McCullum's Reign: Brendon McCullum led from 2009 to 2017 and became the first to 2,000 T20I runs on 29 March 2014.
Kohli Breaks 4,000: Virat Kohli became the first to 4,000 T20I runs on 10 November 2022 against England in Adelaide.
World Cup Farewell: Rohit Sharma and Virat Kohli finished their T20I careers in 2024 on 4,231 and 4,188 runs.
Babar Takes Over: Babar Azam became the all-time leader in 2025 and has 4,596 runs as of November 2026.

Data includes: Babar Azam, Jos Buttler, Rohit Sharma, Virat Kohli, Paul Stirling, Virandeep Singh, Martin Guptill, Mohammad Rizwan, Muhammad Waseem, and other historical top-ten contenders.

Data Source: ESPNcricinfo Statsguru T20I batting records (career totals to 31 Dec of each year, 2006–2025, and to 5 Nov 2026); Wikipedia "List of Twenty20 International records" (dated revisions 2014–2026).

#Cricket #T20I #T20Cricket #CricketStats #BabarAzam #ViratKohli #RohitSharma #PaulStirling

## Music (pick from the YouTube/Facebook in-app audio library so it's licensed and won't be muted or claimed)
1. "Jai Ho" – A. R. Rahman
2. "Don't Stop Me Now" – Queen
3. "Shut Up and Dance" – Walk the Moon

## Data notes / reading of the brief
- Men's T20 internationals, all nations (associate players included as ESPNcricinfo counts them, e.g. UAE's Muhammad Waseem and Malaysia's Virandeep Singh). Career totals at 31 December of each year; 2005 matches are included in the first (2006) row. The last row is 2026 to date (Statsguru to 5 Nov 2026, incl. the 2026 T20 World Cup), labelled 'Nov 2026'.
- World XI / ICC appearances count, as ESPNcricinfo includes them (Shoaib Malik, Shahid Afridi, David Miller) — flags show the player's own nation. Ross Taylor's 2025 runs were for Samoa, so his (ghost-row) flag switches to Samoa in 2025.
- Flags: `flags/my.png` (Malaysia, for Virandeep Singh, 10th at the end of 2025 in the faint ghost row) was not in the repo; it was drawn from the national flag design for this video and added. Replace it with your own upload if you prefer.

## QA
- Nov 2026 row checked against two sources: Statsguru to 5 Nov 2026 and Wikipedia's records list (as of 19 Sep 2026; no top-five player has added runs since): Babar 4,596, Buttler 4,384, Rohit 4,231, Kohli 4,188, Stirling 3,895 — exact match. Virandeep Singh 3,644 and Waseem 3,371 are from Statsguru only. Retired players are unchanged from 2025.
- End-of-2025 row checked against two sources: ESPNcricinfo Statsguru (to 31 Dec 2025) and Wikipedia's 31 Dec 2025 revision of "List of Twenty20 International records": Babar 4,429, Rohit 4,231, Kohli 4,188, Buttler 3,869, Stirling 3,798 (both); Guptill 3,531 and Warner 3,277 (Wikipedia player career stats); Rizwan 3,414 (Wikipedia average table, Dec 2025); Waseem 3,184 (Statsguru; Wikipedia Dec 2025 tables give the same 91 innings, 2,098 balls and 187 sixes but not the run total).
- Intermediate spot checks against dated Wikipedia revisions: Dec 2014 top 5 (McCullum 2,105, Jayawardene 1,493, Dilshan 1,466, Warner 1,444, Duminy 1,399), Dec 2018 (Guptill 2,271, Rohit 2,237, Malik 2,190, Kohli 2,167, McCullum 2,140), Dec 2021 (Guptill 3,299, Kohli 3,227, Rohit 3,197, Babar 2,620, Finch 2,608), Dec 2022 (Kohli 4,008, Rohit 3,853, Guptill 3,531, Babar 3,355, Stirling 3,181) — all match the CSV exactly.
- Events:
  - 2014: McCullum first to 2,000 T20I runs — 65 v Netherlands, Chattogram, 29 Mar 2014 (ESPNcricinfo Statsguru innings list; Wikipedia records table).
  - 2022: Kohli first to 4,000 T20I runs — 50 v England, Adelaide, 10 Nov 2022 (ESPNcricinfo Statsguru innings list; Wikipedia "fastest to 4,000" record, 10 November 2022).
- Lead changes on screen: Smith → Misbah (2008) → McCullum (2009) → Guptill (2018) → Rohit/Kohli (2019–20) → Guptill (2021) → Kohli (2022) → Rohit (2024) → Babar (2025).
- Checks: `--check-flags` (all present incl. new my.png); safe-zone check passed; preview stills and 7 frames from the MP4 reviewed; final frame matches the CSV; event cards dark text on peach, readable.
