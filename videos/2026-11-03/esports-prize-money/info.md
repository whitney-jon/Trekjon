# Which game has paid out the most prize money?

Style: **F1 Dark Notebook skin** (`pl_notebook_style.py`, `NB_PRESET=f1dark`, `--theme money`, `--seconds 20`). The dark-mode trial is applied to a non-F1 topic, with the money icon in the header. 16 years in 20.1 s. Bars use each game's brand colour. **No game logos yet**: they weren't in the repo when this was rendered. It can be re-rendered with logos in a few minutes once they're in `logos/esports/`.

## Description
In 2010 the richest game in esports was Counter-Strike, with $15 million paid out in prize money over its lifetime. Fifteen years later, one game has paid out more than $380 million. Which game has paid out the most prize money?

This race adds up every dollar of tournament prize money by game, from 2010 to 2025. Counter-Strike leads at the start, StarCraft takes over in 2013, and Dota 2's International prize pools send it to No. 1 in 2014, where it has stayed. Fortnite arrives in 2018, and its $30 million World Cup in 2019 puts it level with Counter-Strike in the fight for No. 2.

Key Highlights:
Dota 2's Crowdfunded Fortune: The International's huge prize pools made Dota 2 No. 1 from 2014, on $382 million by the end of 2025.
Counter-Strike's Comeback: The longest-running series (1.6, Source, CS:GO and CS2) is back clear in second on $230 million.
The Fortnite Explosion: $0 to $100 million in two years, after the 2019 World Cup.
Mobile Rising: Arena of Valor (Honor of Kings) and PUBG Mobile have both climbed into the top six.

Data includes: Dota 2, Counter-Strike, Fortnite, League of Legends, Arena of Valor, PUBG Mobile, Call of Duty, PUBG, StarCraft, Rocket League and other games that reached the top ten.

Data Source: Esports Earnings (esportsearnings.com), yearly "Top Games" tables 1998–2025, summed by game.

#Esports #Gaming #Dota2 #CounterStrike #Fortnite #LeagueOfLegends #PrizeMoney #GraphRace

## Music (pick from the YouTube/Facebook in-app audio library so it's licensed)
1. "Legends Never Die" – Against The Current
2. "Blinding Lights" – The Weeknd
3. "Turbo Killer" – Carpenter Brut

## How it works
- Cumulative tournament prize money in US dollars, as recorded by Esports Earnings. Totals before 2010 are carried into the first frame.
- Series are grouped. **Counter-Strike** = 1.6 + Condition Zero + Source + CS:GO + CS2. **StarCraft** = Brood War + StarCraft II + Remastered. **Call of Duty** = all main titles and Warzone (not CoD Mobile or CoD Online). **Halo** = all Halo titles. **Overwatch** = 1 + 2. **EA FC (FIFA)** = all FIFA and EA Sports FC titles. **Quake** = all Quake titles. **WarCraft III** includes Reforged.
- Kept separate: PUBG (PC) and PUBG Mobile; League of Legends (Wild Rift is not included); Arena of Valor as Esports Earnings lists it.
- Each year counts the top 40 games in Esports Earnings' table for that year. Games outside the top 40 in a year are not counted that year, so small totals can be slightly low; the top ten is unaffected.
- It stops at the end of 2025. Esports Earnings' 2026 figures are still incomplete (Dota 2 and League of Legends barely appear yet).

## Events
- 2014 | Dota 2 takes No. 1 ($24.9m v StarCraft's $22.8m; The International 2014 had a record $10.9m prize pool).
- 2019 | Fortnite World Cup pays out $30m (the first Fortnite World Cup, July 2019, $30 million total prize pool).

## QA
- Yearly totals read directly from Esports Earnings' tables in the browser. Spot checks: 2017 Dota 2 $38.1m (TI7 year), 2019 Fortnite $80.8m (World Cup year), 2021 Dota 2 $48.0m (TI10, $40m pool).
- Earlier bot-blocked copies of the 2017, 2019 and 2021 pages showed only partial totals and were not used.
- Leaders by year-end: Counter-Strike 2010–2012, StarCraft 2013, Dota 2 2014–2025.
