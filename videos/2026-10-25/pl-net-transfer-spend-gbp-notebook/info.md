# Which club has the highest Premier League net spend?

Style test: **Premier League Notebook** (hand-drawn skin in PL colours), for comparison on Facebook against the standard Premier League videos. Same data as the 24 Oct euro version, converted to pounds.

## Description
When the Premier League began in 1992, Blackburn Rovers were the big spenders, and a £5m net outlay was enough to top the table. More than three decades and billions of pounds later, which club has the highest net transfer spend in Premier League history?

This race tracks every club's cumulative net transfer spend (money spent on transfers minus money received) in its Premier League seasons, from 1992/93 to the 2026 summer window. Blackburn, Liverpool, Newcastle and Leeds take turns at the top in the 1990s, then Chelsea go clear after Roman Abramovich's 2003 takeover. Manchester City take over in 2015/16, Chelsea's record £489m net spend in 2022/23 puts them back in front, and City lead again from 2025/26 to finish on £1.83bn, ahead of Manchester United and Chelsea.

For European fans: City (£1.83bn), United (£1.74bn) and Chelsea (£1.49bn) lead the way, with Arsenal, Spurs and Liverpool all between £1.14bn and £1.2bn.

Key Highlights:
The Abramovich Effect: Chelsea's net spend went from £67m to £295m in their first two seasons under Roman Abramovich (2003/04 and 2004/05).
City's Climb: Manchester City were ninth in 2007/08; after the 2008 Abu Dhabi takeover they reached the top by 2015/16.
The Record Season: Chelsea's £489m net spend in 2022/23 is the most by any club in a single Premier League season.
2026 Finish: City's £162m net summer took them to £1.83bn, £87m clear of United.

Data includes: Manchester City, Manchester United, Chelsea, Arsenal, Tottenham Hotspur, Liverpool, Newcastle United, West Ham United, Aston Villa, Fulham, and other historical top-ten contenders.

Data Source: Transfermarkt, Premier League transfer income and expenditures by season (1992/93–2026/27), converted to pounds at each season's average exchange rate (US Federal Reserve rates via FRED)

#PremierLeague #ManCity #ManUtd #Chelsea #TransferWindow #NetSpend #EuropeanFootball #GraphRace

## Music (pick from the YouTube/Facebook in-app audio library so it's licensed)
1. "Money" – Pink Floyd
2. "Price Tag" – Jessie J
3. "Can't Hold Us" – Macklemore & Ryan Lewis

## Posting note
Man City's financial charges are topical, but the reported verdict has not yet led to final sanctions. Keep the caption about the data (who has spent the most) and avoid saying City broke rules or will be punished.

## Style
Rendered with `pl_notebook_style.py` (same arguments as `goals_race_vertical.py`): cream lined paper with lavender rules and a PL magenta margin, the PL magenta-to-purple header painted like marker with a hand-cut edge and a hand-drawn double PL green rule, club-colour highlighter bars with crests and wobbly PL-purple ink outlines that redraw like stop-motion pencil, sketched name pills, and a magenta hand-drawn underline under the season.

## How it works
- Net spend = transfer fees paid minus fees received, as recorded by Transfermarkt (in euros), loans included. Only Premier League seasons count.
- Pounds: each season's net spend is converted at that season's average pound-per-euro rate (July–June; the 2026/27 summer window uses June–August 2026), then added up. Rates are monthly Federal Reserve averages from FRED (US dollars per euro, per ECU before 1999, and per pound), e.g. 0.78 in 1992/93, 0.69 in 2003/04, 0.87 in 2022/23, 0.86 in summer 2026. August 2024 (0.851) matches x-rates.com (0.852).
- Converting season by season keeps old fees close to what was paid in pounds at the time. Because the rate moves, the order can differ slightly from the euro version: in pounds City stay ahead of United in 2025/26 (in euros United briefly led).
- Each step is one season (summer and January windows); 2026/27 is the 2026 summer window only.
- Birmingham City and Stoke City (10th briefly around 2010–14) have no crest in our logo folder, so they show colour only.

## Events
- 2003 | Roman Abramovich buys Chelsea (July 2003).
- 2008 | Abu Dhabi group buys Manchester City (September 2008).

## QA
- Same 35 Transfermarkt season tables as the euro version (euro season sums match Transfermarkt's own 1992–2026 totals exactly for the six clubs never relegated).
- Independent £ check against Transfer League's 2003–2019 net spend table: City £1,062m v £1,073m (−1%), United £689m v £688m (0%), Spurs £184m v £179m (+2%). Other clubs differ by 9–30% because the two sites use different fee databases and Transfer League's table runs to around 2019.
- Leaders by season (in pounds): Blackburn 1992–96, Liverpool 1996/97, Newcastle 1997–99, Liverpool 1999–2001, Leeds 2001/02, United 2002/03, Chelsea 2003–15, City 2015–22, Chelsea 2022–25, City 2025–27.
