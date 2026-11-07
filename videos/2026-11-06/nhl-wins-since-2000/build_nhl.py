import csv, sys, glob
FR = {'Mighty Ducks of Anaheim': 'Anaheim Ducks', 'Phoenix Coyotes': 'Arizona Coyotes', 'Atlanta Thrashers': 'Winnipeg Jets',
      'Utah Hockey Club': 'Utah Mammoth', 'Montréal Canadiens': 'Montreal Canadiens'}
YEARS = [1999] + list(range(2000, 2027))   # 1999 = zero row (31 Dec 1999); 2000 = Jan-Apr 2000 part of 1999/00
W, L, T = {}, {}, {}
for Y in range(2000, 2027):
    if Y == 2005:
        continue
    rows = list(csv.DictReader(open('raw/y2000_janapr.csv' if Y == 2000 else f'raw/y{Y-1}.csv')))
    for r in rows:
        t = FR.get(r['Team'], r['Team'])
        w = int(r['W'])
        if 'OTL' in r:
            l, ti = int(r['L']) + int(r['OTL']), 0
        elif Y == 2000:                                # Jan-Apr 2000: L already includes OT losses
            ti = int(r['T']); l = int(r['L'])
        else:                                          # 2000-01 to 2003-04: 82 games, L incl. OT losses = 82 - W - T
            ti = int(r['T']); l = 82 - w - ti
        W.setdefault(t, {})[Y] = w; L.setdefault(t, {})[Y] = l; T.setdefault(t, {})[Y] = ti
    assert len(rows) in (28, 30, 31, 32), (Y, len(rows))
teams = sorted(W)
cum = lambda D, t: [sum(v for y, v in D[t].items() if y <= Y) for Y in YEARS]
CW = {t: cum(W, t) for t in teams}; CL = {t: cum(L, t) for t in teams}; CT = {t: cum(T, t) for t in teams}
if __name__ == '__main__':
    for i, Y in enumerate(YEARS):
        s = sorted(teams, key=lambda t: -CW[t][i])
        print(Y, [(t.split()[-1], CW[t][i]) for t in s[:11]])

def write(prefix, ev):
    order = sorted(teams, key=lambda t: (-CW[t][1], t))      # first-season order, no spoiler
    hdr = ['Atlanta Thrashers|Winnipeg Jets:2012' if t == 'Winnipeg Jets' else t for t in order]
    head = ['# topic: nhl hockey wins since 2000', '# question: Which NHL team has won the|most games since 2000?']
    head += ['# event: ' + e for e in ev]
    head += [f'# label: {Y} | {(Y-1) if Y > 1999 else 1999}/{str(Y)[2:] if Y > 1999 else "00"}' for Y in YEARS]
    for name, D in (('wins', CW), ('losses', CL), ('ties', CT)):
        out = (head if name == 'wins' else []) + ['Year,' + ','.join(hdr)]
        out += [f'{Y},' + ','.join(str(D[t][i]) for t in order) for i, Y in enumerate(YEARS)]
        open(f'{prefix}-{name}.csv', 'w').write('\n'.join(out) + '\n')

if __name__ == '__main__' and len(sys.argv) > 1:
    write(sys.argv[1], sys.argv[2:])
    print({t: (CW[t][-1], CL[t][-1], CT[t][-1]) for t in sorted(teams, key=lambda t: -CW[t][-1])[:10]})
