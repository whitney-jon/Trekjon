FILL={('Lewis Hamilton',2014):(27.5,'mercedes'),('Jenson Button',2011):(12.0,'mclaren'),('Fernando Alonso',2006):(7.0,'renault3')}
START,END=2005,2026
def load():
    S={};T={}
    for l in open('/home/claude/work/f1money/spotrac.txt'):
        n,r=l.strip().split('=',1); S[n]={};T[n]={}
        for t in r.split(';'):
            y,v,tm=t.split('~'); y=int(y)
            if y>END: continue
            S[n][y]=int(v)/1e6; T[n][y]=tm
    for (n,y),(v,tm) in FILL.items(): S[n][y]=v; T[n][y]=tm
    return S,T
