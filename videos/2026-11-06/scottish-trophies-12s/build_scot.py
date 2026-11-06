import sys
sys.path.insert(0, '/home/claude/work/scot')
from data import WINS
# League Cup finals played in the calendar year before the season ends (Nov/Dec finals), by season-end year
LC_CAL = {2017: 2016, 2018: 2017, 2019: 2018, 2020: 2019, 2022: 2021, 2024: 2023, 2025: 2024, 2026: 2025}
wins = [((LC_CAL.get(y, y) if t == 'C' else y), c, t) for y, c, t in WINS]
CLUBS = ['Celtic', 'Rangers', 'Aberdeen', 'Heart of Midlothian', 'Hibernian', "Queen's Park", 'Dundee',
         'Dundee United', 'Kilmarnock', 'St Mirren', 'Motherwell']
LABEL = {'Heart of Midlothian': 'Hearts'}
YEARS = list(range(2000, 2023, 2)) + [2023, 2024, 2025, 2026]
cum = {c: [sum(1 for y, cc, t in wins if cc == c and y <= Y) for Y in YEARS] for c in CLUBS}
COL = {'Rangers': '#1B458F', 'Aberdeen': '#C8102E', 'Hearts': '#7A1F35', 'Hibernian': '#00703C',
       'Dundee': '#1C2D5A', 'Dundee United': '#F47920', 'Motherwell': '#F5A800'}
out = ['# topic: scottish football trophies', '# question: Which club has won the|most trophies in Scotland?']
out += ['# event: ' + e for e in sys.argv[2:]]
out.append('Year,' + ','.join(LABEL.get(c, c) for c in CLUBS))
for i, Y in enumerate(YEARS):
    out.append(f'{Y},' + ','.join(str(cum[c][i]) for c in CLUBS))
open(sys.argv[1], 'w').write('\n'.join(out) + '\n')
for i, Y in enumerate(YEARS):
    print(Y, [cum[c][i] for c in CLUBS])
print({c: cum[c][-1] for c in CLUBS})
