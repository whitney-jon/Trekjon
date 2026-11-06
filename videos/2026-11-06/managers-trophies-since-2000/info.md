# Which manager has won the most trophies since 2000?

Style: **Hand-made Notebook – Claret & Gold** (new preset `NB_PRESET=claret`: claret header, warm ivory paper, near-black ink, old-gold accent), rendered with `handmade_notebook_style.py --seconds 45 --season-labels --stub-grey --logo-bare --trophy-icons`. Header icon: `icons/champions-league.png`, re-inked white. Trophy pops (re-inked claret): League (shield), Cup, Europe (Champions League and UEFA Super Cup), Europa (UEFA Cup/Europa League and Conference League), World (Club World Cup and Intercontinental Cup). Each bar shows the badge and colour of the club where that manager won his latest trophy.

## Description
At the start of the 2000/01 season every manager starts on zero. Over the next 26 years, which manager has won the most trophies?

This race counts the major trophies won by managers of clubs in Europe's main leagues since 2000/01: league titles, national cups, European trophies and world club titles. José Mourinho's Porto, Chelsea and Inter sides make him the early leader. Mircea Lucescu's Shakhtar Donetsk then take him to No. 1 in 2012/13. In 2017/18 Pep Guardiola goes top, and he finishes on 30, six clear of Carlo Ancelotti.

For the European fan: this isn't just the big five. Lucescu, who died in April 2026, won 17 of his 20 trophies with Ukrainian clubs. Neil Lennon (Celtic) and Sergei Semak (Zenit) sit on 9 alongside Benítez, Zidane, Flick and Valverde.

Key Highlights:
Pep on Top: 30 trophies with Barcelona, Bayern and Manchester City, including three Champions Leagues.
Lucescu's Shakhtar Era: Eight Ukrainian titles, six Ukrainian Cups and the 2009 UEFA Cup. He was No. 1 from 2012/13 to 2016/17.
Ancelotti's Europe: 24 trophies across Italy, England, France, Spain and Germany, including five Champions Leagues.
Luis Enrique's Surge: 10 trophies with PSG since 2023/24 take him to 18, past Mourinho's 17.

Data includes: Pep Guardiola, Carlo Ancelotti, Mircea Lucescu, Luis Enrique, José Mourinho, Massimiliano Allegri, Alex Ferguson, Roberto Mancini, Rafael Benítez, Zinedine Zidane, and other historical top-ten contenders.

Data Source: Wikipedia manager honours pages and season/final pages (2000/01 to 2026/27), checked against club and competition records (UEFA, Olympiacos managers list, Qarabağ/Shakhtar/Zenit season pages)

#Football #Managers #Guardiola #Ancelotti #Mourinho #Lucescu #ChampionsLeague #GraphRace

## Music (pick from the YouTube/Facebook in-app audio library so it's licensed and won't be claimed or muted)
1. "Live Is Life" – Opus
2. "Eye of the Tiger" – Survivor
3. "Heart of Courage" – Two Steps From Hell

## How it counts
- **Trophies counted (major only, as you chose):** league titles, national cups, UEFA Champions League, UEFA Cup/Europa League, Conference League, UEFA Super Cup, and Intercontinental Cup/FIFA Club World Cup. Not counted: league cups, national super cups (Community Shield, Supercopa etc.) and national-team trophies.
- **Leagues covered (main leagues + UEFA, as you chose):** England, Spain, Italy, Germany, France, Portugal, Netherlands, Belgium, Scotland, Turkey, Ukraine, Russia, Greece, Austria and Switzerland. Managers whose trophies came in other leagues aren't counted. For example, Qarabağ's Gurbanov has 17 in Azerbaijan.
- **Seasons:** a trophy counts in the season it belongs to, and August super cups open the new season. Calendar-year Russian leagues (to 2011) are placed in the season they finished in (e.g. Nov 2003 → 2003/04). 2026/27 so far = PSG's UEFA Super Cup (12 Aug 2026).
- **Final ties:** Benítez, Zidane, Flick, Valverde, Lennon and Semak are all on 9. Only one of them fits in row 9, and the order among tied managers stays as it was the season before.

### Final totals
Guardiola 30 · Ancelotti 24 · Lucescu 20 · Luis Enrique 18 · Mourinho 17 · Allegri 11 · Ferguson 10 · Mancini 10 · Benítez, Zidane, Flick, Valverde, Lennon, Semak 9 · Klopp, Wenger, Emery, Tuchel, Rodgers, Gross, Gazzaev 8.

### Itemised (season end year)
- Guardiola: Barça 09 L C CL, 10 USC W L, 11 L CL, 12 USC W C; Bayern 14 USC W L C, 15 L, 16 L C; Man City 18 L, 19 L C, 21 L, 22 L, 23 L C CL, 24 USC W L, 26 C.
- Ancelotti: Milan 03 CL C, 04 USC L, 07 CL, 08 USC W; Chelsea 10 L C; PSG 13 L; Real 14 C CL, 15 USC W; Bayern 17 L; Real 22 L CL, 23 USC W C, 24 L CL, 25 USC W.
- Lucescu: Galatasaray 01 USC, 02 L; Beşiktaş 03 L; Shakhtar 04 C, 05 L, 06 L, 08 L C, 09 UEFA Cup, 10 L, 11 L C, 12 L C, 13 L C, 14 L, 16 C; Dynamo Kyiv 21 L C.
- Luis Enrique: Barça 15 L C CL, 16 USC W L C, 17 C; PSG 24 L C, 25 L C CL, 26 USC W L CL, 27 USC.
- Mourinho: Porto 03 L C UEFA Cup, 04 L CL; Chelsea 05 L, 06 L, 07 C; Inter 09 L, 10 L C CL; Real 11 C, 12 L; Chelsea 15 L; Man Utd 17 EL; Roma 22 ECL.
- Full list for every manager: `mdata.py` in this folder.

## Events
- 2008/09 | Lucescu wins the UEFA Cup with Shakhtar (Shakhtar 2–1 Werder Bremen, Istanbul, 20 May 2009). Source: Wikipedia Mircea Lucescu honours; UEFA.
- 2017/18 | Guardiola takes No. 1 (19 v Lucescu's 18, after Man City's 2017/18 Premier League). Source: this data, from Wikipedia honours.

## QA (2025/26 and 2026/27 results checked online, since they are after the older sources)
- PSG won the 2026 Champions League final against Arsenal on penalties (Euronews, 30 May 2026), Ligue 1 2025/26 (5th in a row), the 2025 Intercontinental Cup against Flamengo (Dec 2025), and the 2026 UEFA Super Cup 2–1 against Aston Villa (12 Aug 2026, Salzburg). Lens won the 2026 Coupe de France.
- Barcelona (Flick) won La Liga 2025/26. Real Sociedad won the 2026 Copa del Rey. Inter (Chivu) won Serie A and the Coppa Italia 2026. Porto won the 2025/26 Primeira Liga, and Torreense won the Taça.
- Zenit (Semak) won the 2025/26 Russian Premier League. Spartak won the 2026 Russian Cup. Zenit won the 2024 Russian Cup (2–1 v Baltika).
- Lucescu: Wikipedia honours, plus the 2020 Ukrainian Super Cup (excluded, as a national super cup). Gazzaev: Wikipedia honours plus the 2007/08 Russian Cup (CSKA, 17 May 2008). Sollied: Wikipedia honours. Olympiacos managers: Wikipedia list of Olympiacos managers.
