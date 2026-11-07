# Which NHL team has won the most games since 2000?

Style: **Hand-made Notebook – Rink** (new preset `NB_PRESET=rink`: navy header, cool ice-white paper, navy ink, goal-line red accent), rendered with `handmade_notebook_style.py --seconds 45 --season-labels --record losses.csv --record-ties ties.csv --logo-bare`. Header icon: `icons/hockey.png`, re-inked white. Record mode as in the all-time version: big number = wins, small line underneath = L (incl. OT/SO losses) · T. A follow-up to the 31 Oct all-time wins video, made because fans asked for the expansion era.

## Description
On 1 January 2000 every NHL team starts on zero. Which team has won the most games since?

This race counts every team's regular-season wins since 1 January 2000, starting with the second half of 1999/00. Detroit lead for 18 straight seasons, San Jose take over in 2019/20 and Washington in 2021/22. Then Boston go top in 2022/23 and become the first team to 1,000 wins since 2000.

For the European fan: Nicklas Lidström and Henrik Zetterberg's Red Wings set the early pace, and Alex Ovechkin's Washington Capitals finish third on 1,072 wins.

Key Highlights:
Detroit's Reign: The Red Wings are No. 1 every season from 2001/02 to 2018/19.
Shark Attack: San Jose top the table in 2019/20 and 2020/21, before Washington's brief spell at No. 1.
Bruins on Top: Boston lead since 2022/23, reach 1,000 wins first in 2023/24 and finish on 1,085.
New Teams: Vegas (2017/18), Seattle (2021/22) and Utah (2024/25) join the race, and Atlanta's Thrashers become the Winnipeg Jets in 2011.

Data includes: Boston Bruins, Dallas Stars, Washington Capitals, Colorado Avalanche, St. Louis Blues, Pittsburgh Penguins, Tampa Bay Lightning, Detroit Red Wings, New York Rangers, Nashville Predators, and other top-ten contenders.

Data Source: StatsCrew NHL season standings (1999/00–2025/26), with the 2023/24 season from ChampsOrChumps and the 31 Dec 1999 standings from Hockey-Reference

#NHL #Hockey #Bruins #RedWings #Sharks #Stars #NHLStats #GraphRace

## Music (pick from the YouTube/Facebook in-app audio library so it's licensed and won't be claimed or muted)
1. "Song 2" – Blur
2. "Kernkraft 400" – Zombie Nation
3. "Thunderstruck" – AC/DC

## How it counts
- NHL regular-season games from 1 January 2000 (your rule: "since 2000" = from 1 Jan 2000). The first step is the Jan–Apr 2000 part of 1999/00: full-season 1999/00 records (StatsCrew) minus the standings through 31 Dec 1999 (Hockey-Reference). Every team's two halves add up to 82 games. Losses (L) include overtime and shootout losses; ties (T) ended after 2003/04.
- 2004/05 was cancelled by the lockout, so the bars stand still for one season. 2012/13 (48 games), 2019/20 (paused, about 70 games) and 2020/21 (56 games) were shortened.
- Franchises: the Atlanta Thrashers and Winnipeg Jets are one franchise (name switches in 2011/12); Phoenix/Arizona Coyotes stop after 2023/24; the Utah Hockey Club / Utah Mammoth is counted as a new team from 2024/25, as the NHL lists it.
- Check: each team's W + L + T matches its games played in every season.

## Events
- 2012/13 | A lockout cuts the season to 48 games.
- 2019/20 | Sharks end Detroit's 18-year run at No. 1 (838 v 830).

## Final (wins · L · T)
Bruins 1,085 · 887 · 50 · Stars 1,077 · 889 · 54 · Capitals 1,072 · 907 · 45 · Avalanche 1,071 · 900 · 51 · Blues 1,046 · 929 · 49 · Penguins 1,044 · 943 · 36 · Lightning 1,038 · 942 · 45 · Red Wings 1,037 · 940 · 46 · Rangers 1,024 · 968 · 32 · Predators 1,013 · 960 · 48.

## QA
- Season records spot-checked against known records: 2005/06 Red Wings 58–16–8, 2009/10 Capitals 54–15–13, 2018/19 Lightning 62–16–4, 2022/23 Bruins 65–12–5, 2023/24 Rangers 55–23–4, 2024/25 Jets 56–22–4.
- Logos: Sharks, Senators, Canucks, Sabres, Predators and Wild had no logo in `logos/nhl/` at first render.
