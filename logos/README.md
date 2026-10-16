# Club logos

Clean, consistently named copies of the club badges uploaded to the repo root, used by the render script (`--logos logos`). Each file is a transparent PNG (max 256 px), named by the club's slug: lowercase, `&` → `and`, everything else non-alphanumeric → `-` (e.g. `manchester-united.png`, `queens-park-rangers.png`). The script also understands short names such as Man Utd, Spurs, Wolves, QPR and PSG.

In the video the badge sits on a small disc at the end of the bar (white, or dark for very light badges such as Liverpool's).

Rules:
- The badge must belong to the exact club in the data. AFC Wimbledon (`afc-wimbledon.png`, founded 2002) is **not** Wimbledon FC, the Premier League club of 1992–2000, so it is never used for them.
- Missing badges: `wimbledon.png` (Wimbledon FC), `brighton-and-hove-albion.png` and `marseille.png`. The repo-root `Brighton.png` is actually the Wolves badge, and `Marseille.png` is actually Inter's current badge, so they were not copied.
- Root files that are not images (HTML pages saved with a .png name, e.g. `Blackburn_Rovers.png`, `Middlesbrough.png`, `Portsmouth.png`, `Watford.png`, `Stoke_City.png`) were skipped.
- To add a club: drop `<slug>.png` here, or add the badge anywhere in the repo and ask Claude to convert it.

## Sport folders and raw uploads
- `nba/` and `nhl/` hold cleaned team logos for NBA and NHL races (`--logos logos/nba`, `--logos logos/nhl`), so names like Kings, Rangers or Spurs never collide with football clubs.
- `_uploads/` keeps the original files as uploaded; the render script never reads it. Drop new uploads anywhere and Claude will clean and file them.
- F1 team logos and the European clubs added Oct 2026 (Benfica, Porto, Celtic, Hamburg, Feyenoord, Steaua Bucharest, Red Star Belgrade, Marseille, West Bromwich Albion) sit in this folder by slug.

## NBA era logos (added 16 Oct 2026)
`logos/nba/` also holds the logos of former identities that won titles, uploaded by the user: `minneapolis-lakers.png`, `philadelphia-warriors.png`, `rochester-royals.png`, `st-louis-hawks.png`, `syracuse-nationals.png`, `washington-bullets.png` and `baltimore-bullets.png` (the 1944–54 club, 1948 champions; folded in 1954). The old `baltimore-bullets.png` was the 1963–73 Bullets (today's Wizards) and is kept as `baltimore-bullets-1963-73.png`. Originals are in `_uploads/nba-era/`.
The render script finds a logo by the full name first, then without the city (`Los Angeles Lakers` → `lakers.png`), and switches logo when a column's name timeline switches (e.g. `Minneapolis Lakers|Lakers:1972`).
