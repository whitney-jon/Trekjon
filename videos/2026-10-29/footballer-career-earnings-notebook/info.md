# Which footballer has earned the most?

Style: **Cream Notebook** (Notebook hand-drawn skin with a flat #F6F3EA cream header, #460619 burgundy title and ink, black-and-white ball icon), rendered with `pl_notebook_style.py`, `NB_PRESET=cream`, `--theme football`, `--icon football-ball.png`. Club logos replace flags and change as players move clubs. Event cards use the new centred position above the year (clear of the YouTube caption area).

## Description
In 2016-17, Cristiano Ronaldo and Lionel Messi were the only footballers earning more than $50 million a year on the pitch. Ten seasons later, Ronaldo alone has banked more than $1 billion in wages and bonuses. Which footballer has earned the most?

This race tracks career playing earnings (salary and bonuses, no endorsements) season by season from 2016-17 to 2025-26, with each bar in the colours and badge of the player's club. Ronaldo leads the first season, Messi takes No. 1 in 2018 and holds it for six seasons at Barcelona and PSG, and Neymar briefly climbs to No. 2. Then Ronaldo's move to Al Nassr changes everything: he retakes No. 1 in 2024 and finishes on $1.08 billion, ahead of Messi ($733m) and Neymar ($558m).

For UK fans: Gareth Bale, Wayne Rooney and Paul Pogba all feature in the early top 10, while Mohamed Salah ($244m) and Erling Haaland ($223m) are the Premier League's representatives in the final top 10.

Key Highlights:
Messi's Reign: Lionel Messi was football's top earner from 2018 to 2023.
The Saudi Effect: Ronaldo earned around $200m+ a season at Al Nassr, passing Messi in 2024.
The Billion-Dollar Man: Ronaldo's playing earnings passed $1 billion in 2025-26.
The Wildcards: Ezequiel Lavezzi and Hulk (China) and Andrés Iniesta (Japan) all reached the top 10.

Data includes: Cristiano Ronaldo, Lionel Messi, Neymar, Kylian Mbappé, Karim Benzema, Mohamed Salah, Sadio Mané, Robert Lewandowski, Erling Haaland, Kevin De Bruyne, and other historical top-ten contenders.

Data Source: Forbes World's Highest-Paid Soccer Players and Highest-Paid Athletes lists (on-field earnings: salary and bonuses); SalarySport wage histories (seasons a player was not on a Forbes list); US Federal Reserve exchange rates (FRED)

#Football #Soccer #CristianoRonaldo #Messi #Neymar #Mbappe #SportsMoney #GraphRace

## Music (pick from the YouTube/Facebook in-app audio library so it's licensed)
1. "Money" – Pink Floyd
2. "Started From the Bottom" – Drake
3. "Champions" – Kanye West et al. (if available in the library)

## How it works
- Values are on-field earnings only (salary and bonuses, before tax), added up season by season, 2016-17 to 2025-26 (2017 = 2016-17). Endorsements, image-rights deals and transfer fees are not included.
- Forbes first: where a player appears on a Forbes list, its on-field figure is used. 2017-2019: Forbes soccer top-20 lists (12 months to June); 2020-2026: Forbes Highest-Paid Athletes lists (12 months to May), with Forbes' autumn soccer lists for players outside the athletes top 50.
- Other seasons use SalarySport annual wages (base salary, so bonuses are missing), converted from pounds at each season's average rate from FRED (e.g. $1.27 in 2016-17, $1.20 in 2022-23, $1.34 in 2025-26).
- Estimates where neither source has the player: Oscar at Shanghai Port at the widely reported €400k a week (2017 SIPG half-season, 2021-2024, Jul-Dec 2024); Andrés Iniesta's 2016-17 and 2017-18 Barcelona wages from Capology (€15.43m); Iniesta 2021-22 at Forbes' 2020-21 rate ($30m).
- Bars follow the player's club at the end of each season; retired players keep their last club. Benzema moved to Al Hilal in February 2026.
- Bale's LAFC bar uses LAFC gold so the badge stays visible.

## Events
- 2018 | Messi takes No. 1 from Ronaldo ($137m v $119m).
- 2024 | Ronaldo's Saudi millions retake No. 1 ($620m v $603m).

## QA
- Top-five players' figures come from Forbes in every season except Neymar 2025-26 (Santos, SalarySport).
- Leaders by season: Ronaldo 2017, Messi 2018-2023, Ronaldo 2024-2026.
- Checks: Ronaldo 2018-19 SalarySport £51.5m (~$66m) v Forbes $65m; 2023-24 £156m (~$197m) v Forbes $200m.
- Known gap: Forbes left out some China-based players (Lavezzi, and Hulk in 2019), so their SalarySport wages are used.
