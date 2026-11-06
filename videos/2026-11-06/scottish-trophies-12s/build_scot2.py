import sys
sys.path.insert(0, '/home/claude/work/scot')
from data import WINS
from lower import T2, T3, T4
from collections import Counter
LC_CAL = {2017: 2016, 2018: 2017, 2019: 2018, 2020: 2019, 2022: 2021, 2024: 2023, 2025: 2024, 2026: 2025}
wins = [((LC_CAL.get(y, y) if t == 'C' else y), {'Greenock Morton': 'Morton'}.get(c, c), t) for y, c, t in WINS]
for s in (T2, T3, T4):
    for it in s.split('|'):
        y, cs = it.split(' ', 1)
        for c in cs.split(';'):
            wins.append((int(y), c.strip(), 'S'))     # S = lower-league title (tiers 2-4)
# Aberdeen's 1983 Super Cup and every European trophy use the Europe icon
YEARS = list(range(2000, 2023, 2)) + [2023, 2024, 2025, 2026]
clubs = sorted({c for _, c, _ in wins})
cum = {c: [sum(1 for y, cc, t in wins if cc == c and y <= Y) for Y in YEARS] for c in clubs}
keep = set()
for i in range(len(YEARS)):
    s = sorted(clubs, key=lambda c: -cum[c][i]); cut = cum[s[10]][i]
    keep |= {c for c in clubs if cum[c][i] >= cut}
names = sorted(keep, key=lambda c: (-cum[c][0], -cum[c][-1], c))
if __name__ == '__main__':
    LABEL = {'Heart of Midlothian': 'Hearts'}
    out = ['# topic: scottish football trophies', '# question: Which club has won the|most trophies in Scotland?']
    out += ['# event: ' + e for e in sys.argv[2:]]
    for c in names:
        tr = {}
        for y, cc, t in wins:
            if cc == c and y > 2000:
                tr.setdefault(y, []).append(t)
        if tr:
            out.append(f'# trophy: {LABEL.get(c, c)} | ' + ' | '.join(f'{y}:{"".join(sorted(v, key="LFCSE".index))}' for y, v in sorted(tr.items())))
    out.append('Year,' + ','.join(LABEL.get(c, c) for c in names))
    for i, Y in enumerate(YEARS):
        out.append(f'{Y},' + ','.join(str(cum[c][i]) for c in names))
    open(sys.argv[1], 'w').write('\n'.join(out) + '\n')
    for i, Y in enumerate(YEARS):
        print(Y, sorted(((cum[c][i], c) for c in names), reverse=True)[:12])
    print(sorted(((cum[c][-1], c) for c in clubs), reverse=True)[:22])
