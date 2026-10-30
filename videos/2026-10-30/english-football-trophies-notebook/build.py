import sys
sys.path.insert(0, '/home/claude/work/trophies')
from data import WINS, TOTAL
from collections import Counter
COL = {'Liverpool':'#C8102E/#F6EB61','Manchester United':'#DA291C/#FBE122','Arsenal':'#EF0107/#FFFFFF','Manchester City':'#6CABDD/#1C2C5B',
 'Chelsea':'#034694/#DBA111','Tottenham Hotspur':'#132257/#FFFFFF','Aston Villa':'#670E36/#95BFE5','Everton':'#003399/#FFFFFF',
 'Newcastle United':'#241F20/#FFFFFF','Nottingham Forest':'#DD0000/#FFFFFF','Wolverhampton Wanderers':'#FDB913/#231F20',
 'Blackburn Rovers':'#009EE0/#FFFFFF','Sunderland':'#EB172B/#FFFFFF','Sheffield Wednesday':'#4466AA/#FFFFFF','Leeds United':'#FFFFFF/#1D428A',
 'West Bromwich Albion':'#122F67/#FFFFFF'}
post = Counter(c for y, c, t in WINS); pre = {c: TOTAL[c] - post[c] for c in TOTAL}
YEARS = list(range(1991, 2027))
cum = {c: [pre[c] + sum(1 for y, cc, t in WINS if cc == c and y <= Y) for Y in YEARS] for c in pre}
rank = [sorted(cum, key=lambda c: (-cum[c][i], c)) for i in range(len(YEARS))]
keep = set()
for r in rank: keep |= set(r[:11])
first = {c: min(i for i in range(len(YEARS)) if c in rank[i][:11]) for c in keep}
names = sorted(keep, key=lambda c: (first[c], -cum[c][first[c]]))
out = ['# topic: english football trophies premier league fa cup', '# question: Which club has won the|most trophies in England?']
out += ['# event: ' + e for e in sys.argv[1:]]
for c in names:
    out.append(f'# color: {c} | 1991:{COL[c]}')
    tr = {}
    for y, cc, t in WINS:
        if cc == c: tr.setdefault(y, []).append(t)
    if tr: out.append(f'# trophy: {c} | ' + ' | '.join(f'{y}:{"".join(sorted(v))}' for y, v in sorted(tr.items())))
out.append('Year,' + ','.join(names))
for i, Y in enumerate(YEARS): out.append(f'{Y},' + ','.join(str(cum[c][i]) for c in names))
open('/home/claude/work/trophies/english-trophies.csv', 'w').write('\n'.join(out) + '\n')
print(len(names), names)
