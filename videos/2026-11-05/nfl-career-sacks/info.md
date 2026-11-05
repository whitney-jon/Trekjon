# Who has the most sacks in NFL history?

**Style:** Notebook (Hand-made Legal Pad) — `handmade_notebook_style.py`, `NB_PRESET=legalpad`, `--theme nfl` (no NFL icon file in icons/, so the script's drawn football icon is used), team logos from `logos/nfl` (no flags), `--engage --seconds 29.97` (900 frames, 30.0 s), 19 time points (~1.6 s each).

## Title
Who has the most sacks in NFL history?

## Description
At the end of 1989 Lawrence Taylor led the NFL's official sack count with 104, ahead of Dexter Manley and a young Reggie White. So who has the most sacks in NFL history?

This race tracks official NFL regular-season sacks (an official stat since 1982) from 1989 to the end of the 2025 season. Reggie White took over from Taylor in 1993, Bruce Smith passed White's record of 198 in December 2003, and Julius Peppers climbed to fourth with his 2017 Carolina return.

There are no European players in this top ten: it is an all-American list built by pass rushers from the Bills, Eagles, Rams, Panthers and Vikings.

Key Highlights:
The LT Era: Lawrence Taylor led the official count through the early 1990s and finished on 132.5.
Minister of Defense: Reggie White took the lead in 1993 and finished with 198.
The Record: Bruce Smith passed White on 7 December 2003 and retired with 200.
Peppers' Climb: Julius Peppers passed Chris Doleman for fourth in October 2017 and finished on 159.5.

Data includes: Bruce Smith, Reggie White, Kevin Greene, Julius Peppers, Chris Doleman, Michael Strahan, Jason Taylor, Terrell Suggs, Von Miller, DeMarcus Ware, and other historical top-ten contenders.

Data Source: Pro-Football-Reference player pages and career sack leaders (official sacks, 1982–2025); Wikipedia "List of NFL career sacks leaders"; StatMuse cumulative checks.

#NFL #Sacks #AmericanFootball #NFLStats #NFLHistory #BruceSmith #ReggieWhite #Football

## Music (pick from the YouTube/Facebook in-app audio library so it's licensed and won't be muted or claimed)
1. "Remember the Name" – Fort Minor
2. "Centuries" – Fall Out Boy
3. "Can't Hold Us" – Macklemore & Ryan Lewis

## Data notes / reading of the brief
- Official sacks only (1982 on); pre-1982 sacks shown on PFR (e.g. Lawrence Taylor's 9.5 and Rickey Jackson's 8.0 in 1981) are not counted. Regular season only; 2026 (in progress) excluded.
- Time points: every second season (1989, 1991 … 2025). Each value is the real cumulative total at the end of that season, all-time from 1982; nothing is interpolated. Two-season steps were used because one point per season (44 seasons) would be far too fast for 30 s, and 2002–2025 alone is almost frozen at the top.
- Labels show one decimal (half sacks) and only ever show real end-of-season values (`# snap-labels`).
- Logo and bar colour: the team where each player made most of his sacks (e.g. Kevin Greene = Rams, Reggie White = Eagles, Peppers = Panthers, Jared Allen = Vikings, Von Miller = Broncos, Al Baker = Cardinals).
- Missing logo: `logos/nfl/houston-oilers-logo.png` (Sean Jones and William Fuller made most of their sacks for the Houston Oilers); their bars show no badge (`--logo-gaps`). Sean Jones is visible around 1995.

## QA
- Final row (2025) checked against two sources: PFR career leaders (official, filtered to 1982+) and Wikipedia's list: Smith 200, White 198, Greene 160, Peppers 159.5, Doleman 150.5, Strahan 141.5, J. Taylor 139.5, Suggs 139, Miller 138.5, Ware 138.5, Dent 137.5, Randle 137.5. Every player's season sum equals his official career total.
- Intermediate spot checks: StatMuse cumulative top 12 for 1982–89, 1982–92 and 1982–95 match the CSV exactly (e.g. 1989: Taylor 104, Manley 91, White/Dent 81; 1995: White 157, Taylor 132.5, Jackson 128); Peppers 142.5 on 4 Dec 2016 passing Strahan (NBC Sports/PFT; CSV 2015 = 136 + 7.5 in 2016); Peppers' 151st on 29 Oct 2017 (ESPN); Von Miller 137.5 on 25 Dec 2025 (Yardbarker; CSV 2025 = 138.5).
- Events:
  - 2003: Bruce Smith breaks Reggie White's record — sack No. 199 on Jesse Palmer, Washington 20–7 NY Giants, 7 Dec 2003 (commanders.com "Flashback: Smith's sack one for the record books"; ESPN 25 Feb 2004).
  - 2017: Peppers passes Doleman for 4th all-time — strip-sack of Jameis Winston, Panthers 17–3 Buccaneers, 29 Oct 2017 (ESPN).
- Lead changes on screen: Taylor → White (1993) → Smith (2003).
- Checks: safe-zone check passed; preview stills and 7 frames from the MP4 reviewed; final frame numbers match the CSV; event cards white text on red, readable.
