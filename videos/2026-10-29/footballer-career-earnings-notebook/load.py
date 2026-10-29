FX={2017:1.2691,2018:1.3474,2019:1.2946,2020:1.2600,2021:1.3477,2022:1.3309,2023:1.2049,2024:1.2597,2025:1.2948,2026:1.3424}
YEARS=list(range(2017,2027))
def load():
    F={}; src={}
    for l in open('/home/claude/work/footymoney/forbes.txt'):
        if l.startswith('#') or not l.strip(): continue
        y,n,v,s=l.strip().split('|'); F.setdefault(n,{})[int(y)]=float(v); src[(n,int(y))]=s
    S={}; club={}
    for l in open('/home/claude/work/footymoney/ss.txt'):
        n,rest=l.strip().split('=',1)
        for t in rest.split(';'):
            y,v,c=t.split('~'); y=int(y)
            S.setdefault(n,{})[y]=int(v)*FX[y]/1e6; club.setdefault(n,{})[y]=c
    V={}
    for n in set(F)|set(S):
        V[n]={}
        for y in YEARS:
            if y in F.get(n,{}): V[n][y]=F[n][y]
            elif y in S.get(n,{}): V[n][y]=S[n][y]; src[(n,y)]='SS'
            else: V[n][y]=0; src[(n,y)]='--'
    return V,src,club
