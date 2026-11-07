import sys
sys.path.insert(0, '/home/claude/work/mgr2')
from mdata import M
COL = {'ac-milan':'#C8102E','ajax':'#D2122E','arsenal':'#EF0107','aston-villa':'#670E36','athletic-bilbao':'#EE2523',
 'atletico-madrid':'#CB3524','austria-wien':'#6A2C91','barcelona':'#A50044','basel':'#E2001A','bayern-munich':'#DC052D',
 'benfica':'#E83030','besiktas':'#1A1A1A','bordeaux':'#1B2A49','borussia-dortmund':'#FDE100','braga':'#E30613',
 'celtic':'#018749','chelsea':'#034694','club-brugge':'#1E64C8','cska-moscow':'#B5121B','dynamo-kyiv':'#0055A4',
 'fenerbahce':'#12205C','fiorentina':'#5B2D8E','galatasaray':'#A90432','inter-milan':'#0068A8','juventus':'#1A1A1A',
 'lazio':'#87D8F7','leicester-city':'#003090','liverpool':'#C8102E','lokomotiv-moscow':'#00843D','lyon':'#1F3C88',
 'manchester-city':'#6CABDD','manchester-united':'#DA291C','napoli':'#12A0D7','olympiacos':'#E2231A','paris-saint-germain':'#004170',
 'psv-eindhoven':'#ED1C24','rangers':'#1B458F','real-madrid':'#FFFFFF','red-bull-salzburg':'#ED1C24','roma':'#8E1F2F',
 'schalke-04':'#004D9D','sevilla':'#D81E05','shakhtar-donetsk':'#F26522','sporting-cp':'#008057','valencia':'#FFFFFF',
 'villarreal':'#FFE667','wolfsburg':'#65B32E','zenit':'#0096D6','porto':'#00428C','anderlecht':'#5A2D82','nantes':'#FCD405','deportivo':'#1B5EAA','monaco':'#E2001A','aek-athens':'#FFD200','fc-tirol':'#00843D'}
ICON = {'L':'L','C':'F','CL':'E','EL':'U','ECL':'U','USC':'P','W':'I'}
YEARS = list(range(1999, 2028))   # 1999 = zero row; 2000 = trophies won Jan-Jun 2000 (end of 1999/00)
cum = {n: [sum(len(c.split()) for y, _, c in v if y <= Y) for Y in YEARS] for n, v in M.items()}
total = {n: cum[n][-1] for n in M}
# keep everyone who is ever in the top 11 (9 rows + 2 ghost rows), ties included
keep = set()
for i in range(len(YEARS)):
    vals = sorted({cum[n][i] for n in M}, reverse=True)
    s = sorted(M, key=lambda n: -cum[n][i])
    cut = cum[s[10]][i]
    keep |= {n for n in M if cum[n][i] >= max(cut, 1)}
names = sorted(keep, key=lambda n: (-cum[n][1], -total[n]))   # order by 2000-01 results (no spoiler), then total
out = ['# topic: football managers trophies', '# question: Which manager has won the|most trophies since 2000?']
out += ['# event: ' + e for e in sys.argv[2:]]
for Y in YEARS:
    out.append(f'# label: {Y} | {Y-1 if Y > 1999 else 1999}/{str(Y)[2:] if Y > 1999 else "00"}')
for n in names:
    v = sorted(M[n])
    tl = [(1999, v[0][1])] + [(y, c) for y, c, _ in v]
    seq = []
    for y, c in tl:
        if not seq or seq[-1][1] != c:
            seq.append((y, c))
    out.append(f'# logo: {n} | ' + ' | '.join(f'{y}:{c}' for y, c in seq))
    out.append(f'# color: {n} | ' + ' | '.join(f'{y}:{COL[c]}' for y, c in seq))
    out.append(f'# trophy: {n} | ' + ' | '.join(f'{y}:' + ''.join(ICON[t] for t in cs.split()) for y, _, cs in v))
out.append('Year,' + ','.join(names))
for i, Y in enumerate(YEARS):
    out.append(f'{Y},' + ','.join(str(cum[n][i]) for n in names))
open(sys.argv[1], 'w').write('\n'.join(out) + '\n')
print(len(names), names)
