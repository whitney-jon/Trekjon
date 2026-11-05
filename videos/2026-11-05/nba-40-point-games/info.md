# Who has the most 40-point games since 1990?

**Style:** Notebook (Hand-made Slate & Tangerine, dark) — `handmade_notebook_style.py`, `NB_PRESET=slate`, `--theme basketball` (no NBA icon file in icons/, so the script's drawn basketball is used), team logos from `logos/nba` (no flags), `--engage --seconds 30 --season-labels` (900 frames, 30.0 s), 20 time points (~1.5 s each).

## Title
Who has the most 40-point games since 1990?

(The brief's working title was "Who has the most 40-point games in NBA history?". The race counts from 1989-90, not all-time — Wilt Chamberlain and pre-1990 Jordan games aren't in it — so the title and on-screen question say "since 1990" to stay accurate.)

## Description
In 1989-90 Michael Jordan scored 40 or more points 22 times, and nobody else had more than 11. So who has the most 40-point games since 1990?

This race counts NBA regular-season 40-point games from the 1989-90 season to 2025-26, with everyone starting on zero. Jordan led for two decades, Kobe Bryant's 27-game 2005-06 season set up his takeover in 2009-10, and James Harden's scoring seasons with Houston lifted him past Jordan into second in July 2020.

European fans will spot Slovenia's Luka Dončić, the fastest riser of the 2020s with 62, and Greece's Giannis Antetokounmpo, who sits just outside the top 9 on 56.

Key Highlights:
Jordan's Era: Michael Jordan had 96 40-point games from 1989-90 on, 88 of them for Chicago.
Kobe's Season: Kobe Bryant had 27 40-point games in 2005-06, including his 81 against Toronto on 22 Jan 2006.
Harden Climbs: James Harden passed Jordan's 96 with 49 points against Dallas on 31 Jul 2020.
New Wave: Luka Dončić had 16 40-point games in 2025-26 and finished the season on 62.

Data includes: Kobe Bryant, James Harden, Michael Jordan, Allen Iverson, LeBron James, Stephen Curry, Kevin Durant, Luka Dončić, Damian Lillard, Giannis Antetokounmpo, and other historical top-ten contenders.

Data Source: LandOfBasketball.com season-by-season 40-point game lists (1989-90 to 2025-26); StatMuse regular-season 40-point games (1989-90 to 2025-26).

#NBA #Basketball #40PointGames #NBAStats #KobeBryant #JamesHarden #MichaelJordan #LukaDoncic

## Music (pick from the YouTube/Facebook in-app audio library so it's licensed and won't be muted or claimed)
1. "Jump Around" – House of Pain
2. "Can't Stop" – Red Hot Chili Peppers
3. "Power" – Kanye West

## Data notes / reading of the brief
- Regular season only, 1989-90 to 2025-26 (2026-27, in progress, excluded). Everyone starts on 0 (`--season-labels`; zero row labelled 1990).
- Time points: every second season (1990, 1992 … 2026, labels are the season's end year). Each value is the real cumulative count at the end of that season; 37 single seasons would be far too fast for 30 s.
- Logo and bar colour: the team where each player had most of his 40-point games since 1989-90 (e.g. Shaquille O'Neal = Lakers 26 v Magic 21, LeBron = Cavaliers 51, Durant = Thunder 45, Dončić = Mavericks 42, Vince Carter = Nets 17 v Raptors 14 — the Nets use the current Brooklyn logo; Carmelo Anthony is 17–17 Nuggets/Knicks, shown as Nuggets).
- Missing logos in `logos/nba/` (those bars show no badge): `jazz.png` (Karl Malone), `magic.png` (Tracy McGrady), `suns.png` (Tom Chambers), `hornets.png` (Glen Rice). Karl Malone and McGrady are visible for long stretches.

## QA
- Final row (end of 2025-26) checked against two sources: LandOfBasketball season lists (summed) and StatMuse "most 40 point games from 1989-90 to 2025-26 regular season": Kobe 122, Harden 107, Jordan 96, LeBron 79, Iverson 79, Curry 75, Durant 74, Dončić 62, Lillard 60, Giannis 56, Westbrook 50, Shaq 49, Embiid 49 — exact match.
- Intermediate spot checks: StatMuse single-season lists for 1989-90 to 1996-97 match LandOfBasketball exactly (e.g. 1989-90 Jordan 22, Ewing 11, Malone 11, Bird 7, Chambers 7; 1996-97 Jordan 8, Rice 7, Sprewell 6, Iverson 5); StatMuse 1989-90 to 2005-06 leader Jordan 96 = CSV 2006; every LandOfBasketball season list sums to its own season total.
- Events:
  - 2006: Kobe has 27 40-point games in 2005-06, incl. 81 v Toronto on 22 Jan 2006 (LandOfBasketball 2005-06 40-point game list, game log dated 2006-01-22, 81 pts, W 122-104 v Raptors).
  - 2020: Harden passes Jordan for 2nd — his 97th since 1989-90: 49 pts, W 153-149 OT at Dallas, 31 Jul 2020 (LandOfBasketball 2019-20 game list: 77 before the season, 20th of 2019-20).
- Lead change on screen: Jordan → Kobe (2010).
- Checks: safe-zone check passed; preview stills and 7 frames from the MP4 reviewed; final frame numbers match the CSV; event card text dark on tangerine, readable.
