# Club logos

Clean, consistently named copies of the club badges uploaded to the repo root, used by the render script (`--logos logos`). Each file is a transparent PNG (max 256 px), named by the club's slug: lowercase, `&` → `and`, everything else non-alphanumeric → `-` (e.g. `manchester-united.png`, `queens-park-rangers.png`). The script also understands short names such as Man Utd, Spurs, Wolves, QPR and PSG.

In the video the badge sits on a small disc at the end of the bar (white, or dark for very light badges such as Liverpool's).

Rules:
- The badge must belong to the exact club in the data. AFC Wimbledon (`afc-wimbledon.png`, founded 2002) is **not** Wimbledon FC, the Premier League club of 1992–2000, so it is never used for them.
- Missing badges: `wimbledon.png` (Wimbledon FC), `brighton-and-hove-albion.png` and `marseille.png`. The repo-root `Brighton.png` is actually the Wolves badge, and `Marseille.png` is actually Inter's current badge, so they were not copied.
- Root files that are not images (HTML pages saved with a .png name, e.g. `Blackburn_Rovers.png`, `Middlesbrough.png`, `Portsmouth.png`, `Watford.png`, `Stoke_City.png`) were skipped.
- To add a club: drop `<slug>.png` here, or add the badge anywhere in the repo and ask Claude to convert it.
