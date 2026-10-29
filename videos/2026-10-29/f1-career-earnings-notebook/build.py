import sys
sys.path.insert(0,'/home/claude/work/f1money')
from load import load, START, END
# Spotrac logo id -> (slug, face/edge)
TM = {'ferrari':('ferrari','#DC0000/#FFEB00'),'mclaren':('mclaren','#FF8000/#47C7FC'),'mercedes':('mercedes','#00A19C/#C8CCCE'),
 'redbull1':('red-bull','#1E2A78/#FFC906'),'redbull2':('toro-rosso','#0032A0/#C8102E'),'rb':('rb','#6692FF/#FFFFFF'),
 'renault3':('renault','#FFD800/#0055A5'),'renault2':('renault','#FFD800/#000000'),'renault1':('renault','#FFD800/#000000'),
 'williams1':('williams','#00A0DE/#041E42'),'honda':('honda','#FFFFFF/#CC0000'),'brawn':('brawn','#E8FF2A/#FFFFFF'),
 'toyota':('toyota','#FFFFFF/#E10A17'),'teamlotus':('lotus','#0B6E3B/#FFE600'),'lotus':('lotus','#B8975A/#000000'),
 'sauber':('sauber','#00519A/#FFFFFF'),'sauber1':('sauber','#00519A/#FFFFFF'),'bmw':('bmw-sauber','#FFFFFF/#0066B1'),
 'alfa':('alfa-romeo','#981E32/#FFFFFF'),'kick_sauber':('sauber','#52E252/#000000'),'aston_martin_logo':('aston-martin','#00665E/#CEDC00'),
 'alpine-f1':('alpine','#0093CC/#FF87BC'),'forceindia':('force-india','#FFFFFF/#FF7F00'),'racingpoint1':('racing-point','#F596C8/#0A2240'),
 'alphatauri':('alphatauri','#2B4562/#FFFFFF'),'haas':('haas','#B6BABD/#DA291C'),'cad_2026':('cadillac','#C0C0C0/#000000')}
S,T=load(); YEARS=list(range(START,END+1))
cum={n:[sum(v for y,v in S[n].items() if y<=Y) for Y in YEARS] for n in S}
rank=[sorted(S,key=lambda n:-cum[n][i]) for i in range(len(YEARS))]
keep=set()
for r in rank: keep|=set(r[:12])
def team(n,Y):
    ys=[y for y in T[n] if y<=Y]; return T[n][max(ys)] if ys else T[n][min(T[n])]
first={n:min(i for i in range(len(YEARS)) if n in rank[i][:12]) for n in keep}
names=sorted(keep,key=lambda n:(first[n],-cum[n][first[n]]))
out=['# topic: formula 1 f1 driver career salary earnings money','# question: Which F1 driver has|earned the most?','# format: $|m||1']
out+=['# event: '+e for e in sys.argv[1:]]
for n in names:
    segs,lsegs,lc,ll=[],[],None,None
    for Y in YEARS:
        sl,col=TM[team(n,Y)]
        if col!=lc: segs.append(f'{Y}:{col}'); lc=col
        if sl!=ll: lsegs.append(f'{Y}:{sl}'); ll=sl
    out.append(f'# color: {n} | '+' | '.join(segs)); out.append(f'# logo: {n} | '+' | '.join(lsegs))
out.append('Year,'+','.join(names))
for i,Y in enumerate(YEARS): out.append(f'{Y},'+','.join(f'{cum[n][i]:.3f}' for n in names))
open('/home/claude/work/f1money/f1-career-earnings.csv','w').write('\n'.join(out)+'\n')
print(len(names),'drivers')
