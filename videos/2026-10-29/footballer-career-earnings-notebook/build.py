import sys
sys.path.insert(0,'/home/claude/work/footymoney')
from load import load, YEARS
from clubs import TL, SLUG, COL, club_at
V,src,club=load()
cum={n:[sum(V[n][y] for y in YEARS if y<=Y) for Y in YEARS] for n in V}
rank=[sorted(V,key=lambda n:-cum[n][i]) for i in range(len(YEARS))]
keep=set()
for r in rank: keep|=set(r[:12])
miss=[n for n in keep if n not in TL]
if miss: print('NO CLUB TL',miss); sys.exit()
first={n:min(i for i in range(len(YEARS)) if n in rank[i][:12]) for n in keep}
names=sorted(keep,key=lambda n:(first[n],-cum[n][first[n]]))
out=['# topic: football soccer career salary earnings money','# question: Which footballer has|earned the most?','# format: $|m||1']
out+=['# event: '+e for e in sys.argv[1:]]
logos=set()
for n in names:
    segs,lsegs,lc,ll=[],[],None,None
    for Y in YEARS:
        c=club_at(n,Y); col=COL[c]; lg=SLUG[c]; logos.add(lg)
        if col!=lc: segs.append(f'{Y}:{col}'); lc=col
        if lg!=ll: lsegs.append(f'{Y}:{lg}'); ll=lg
    out.append(f'# color: {n} | '+' | '.join(segs))
    out.append(f'# logo: {n} | '+' | '.join(lsegs))
out.append('Year,'+','.join(names))
for i,Y in enumerate(YEARS): out.append(f'{Y},'+','.join(f'{cum[n][i]:.3f}' for n in names))
open('/home/claude/work/footymoney/footballer-career-earnings.csv','w').write('\n'.join(out)+'\n')
for i,Y in enumerate(YEARS):
    print(Y,' | '.join(f'{n.split()[-1]} {cum[n][i]:.1f} {club_at(n,Y)[:10]}' for n in rank[i][:10]))
print(len(names),'players; logos:',sorted(logos))
