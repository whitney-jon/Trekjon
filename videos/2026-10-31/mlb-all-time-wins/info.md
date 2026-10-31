# Which MLB team has won the most games?

Style: **Standard** (`goals_race_vertical.py`, baseball theme) with record mode: each bar shows all-time wins, with losses (L) in a small line underneath. Team logos on the bars. Event cards sit in the centred position above the year.

## Description
In 2005 the Giants became the first team in baseball history to win 10,000 games. Today they've won 11,685. Which MLB team has won the most games?

This race tracks every franchise's all-time regular-season wins from 1980 to the end of the 2026 season, with each team's history back to 1876 carried into the first frame. The Giants lead all the way, with the Cubs chasing. Behind them, the Braves pass the Pirates in 1995, the Dodgers and Yankees climb the table, and the Pirates fall from third to sixth.

Key Highlights:
Giants First: The Giants were the first franchise to 10,000 wins (2005) and have led all the way.
Yankee Efficiency: The Yankees have only 8,284 losses, the fewest in the top 10 by more than 1,000.
The Phillies: Philadelphia has more losses (11,465) than any team in sports history.
Late Starters: The Yankees began in 1903, decades after the NL teams, but have climbed to fifth.

Data includes: San Francisco Giants, Chicago Cubs, Atlanta Braves, Los Angeles Dodgers, New York Yankees, Pittsburgh Pirates, St. Louis Cardinals, Cincinnati Reds, Philadelphia Phillies, Boston Red Sox, and other historical top-ten franchises.

Data Source: MLB Stats API standings, 1876–2026 (National League and American League); 1892 National League standings from StatsCrew

#MLB #Baseball #Giants #Cubs #Yankees #Dodgers #Braves #GraphRace

## Music (pick from the YouTube/Facebook in-app audio library so it's licensed)
1. "Centerfield" – John Fogerty
2. "Take Me Out to the Ball Game" (instrumental)
3. "Seven Nation Army" – The White Stripes

## How it works
- National League and American League regular-season games only (no postseason). American Association, Union, Players' and Federal League seasons are not counted, so totals can be a little lower than Baseball-Reference's franchise totals for the Dodgers, Pirates, Reds and Cardinals.
- Franchises are counted as one team through moves and renames, e.g. the Giants include New York, the Braves include Boston and Milwaukee, the Dodgers include Brooklyn and Cleveland includes the Indians.
- Ties (games that counted but ended level) are not shown: they were very rare and stopped counting in the standings long ago.
- 1981 and 1994 were strike-shortened and 2020 was a 60-game season, so the bars slow down in those years. 2026 is the full season just finished.
- The 1892 season was missing from the API (it was a split season), so it was added from the full-season 1892 NL standings.

## Events
- 1995 | Braves pass the Pirates for No. 3.
- 2005 | Giants become the first team to 10,000 wins.

## QA
- Checked against reported milestones: Giants' 10,000th win in 2005; Phillies' 10,000th loss in July 2007 (9,954 losses at the end of 2006); Cubs' 11,000th win in 2020; Phillies' 10,000th win in August 2022, the 9th franchise to get there.
- Leader in every season: San Francisco Giants.
