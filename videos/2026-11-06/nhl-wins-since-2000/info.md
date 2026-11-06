# Which NHL team has won the most games since 2000?

Style: **Hand-made Notebook – Rink** (new preset `NB_PRESET=rink`: navy header, cool ice-white paper, navy ink, goal-line red accent), rendered with `handmade_notebook_style.py --seconds 45 --season-labels --record losses.csv --record-ties ties.csv --logo-bare`. Header icon: `icons/hockey.png`, re-inked white. Record mode as in the all-time version: big number = wins, small line underneath = L (incl. OT/SO losses) · T. A follow-up to the 31 Oct all-time wins video, made because fans asked for the expansion era.

## Description
At the start of the 2000/01 season every NHL team starts on zero. Over the next 26 seasons, which team has won the most games?

This race counts every team's regular-season wins since 2000/01, the season the Wild and Blue Jackets joined. Detroit lead for 17 straight seasons, and San Jose take over in 2018/19. Boston go top in 2021/22, and in 2024/25 the Bruins and the Stars both pass 1,000 wins.

For the European fan: Nicklas Lidström and Henrik Zetterberg's Red Wings set the early pace, and Alex Ovechkin's Washington Capitals finish fourth on 1,041 wins.

Key Highlights:
Detroit's Reign: The Red Wings are No. 1 every season from 2001/02 to 2017/18.
Shark Attack: San Jose top the table from 2018/19 to 2020/21.
Bruins on Top: Boston lead since 2021/22 and finish on 1,074 wins.
New Teams: Vegas (2017/18), Seattle (2021/22) and Utah (2024/25) join the race, and Atlanta's Thrashers become the Winnipeg Jets in 2011.

Data includes: Boston Bruins, Dallas Stars, Colorado Avalanche, Washington Capitals, Tampa Bay Lightning, Pittsburgh Penguins, St. Louis Blues, Detroit Red Wings, New York Rangers, Nashville Predators, and other top-ten contenders.

Data Source: StatsCrew NHL season standings (2000/01–2025/26), with the 2023/24 season from ChampsOrChumps

#NHL #Hockey #Bruins #RedWings #Sharks #Stars #NHLStats #GraphRace

## Music (pick from the YouTube/Facebook in-app audio library so it's licensed and won't be claimed or muted)
1. "Song 2" – Blur
2. "Kernkraft 400" – Zombie Nation
3. "Thunderstruck" – AC/DC

## How it counts
- NHL regular-season games only, from 2000/01 (everyone starts at zero). Losses (L) include overtime and shootout losses; ties (T) ended after 2003/04.
- 2004/05 was cancelled by the lockout, so the bars stand still for one season. 2012/13 (48 games), 2019/20 (paused, about 70 games) and 2020/21 (56 games) were shortened.
- Franchises: the Atlanta Thrashers and Winnipeg Jets are one franchise (name switches in 2011/12); Phoenix/Arizona Coyotes stop after 2023/24; the Utah Hockey Club / Utah Mammoth is counted as a new team from 2024/25, as the NHL lists it.
- Check: each team's W + L + T matches its games played (e.g. Boston 1,074 + 864 + 40 = 1,978 = 22 × 82 + 48 + 70 + 56).

## Events
- 2012/13 | A lockout cuts the season to 48 games.
- 2018/19 | Sharks end Detroit's 17-year run at No. 1 (793 v 790).

## Final (wins · L · T)
Bruins 1,074 · 864 · 40 · Stars 1,053 · 875 · 49 · Avalanche 1,047 · 887 · 44 · Capitals 1,041 · 897 · 39 · Lightning 1,029 · 908 · 41 · Penguins 1,023 · 923 · 31 · Blues 1,017 · 920 · 42 · Red Wings 1,014 · 925 · 40 · Rangers 1,007 · 945 · 26 · Predators 998 · 933 · 46.

## QA
- Season records spot-checked against known records: 2005/06 Red Wings 58–16–8, 2009/10 Capitals 54–15–13, 2018/19 Lightning 62–16–4, 2022/23 Bruins 65–12–5, 2023/24 Rangers 55–23–4, 2024/25 Jets 56–22–4.
- Logos: Sharks, Senators, Canucks, Sabres, Predators and Wild had no logo in `logos/nhl/` at first render.
