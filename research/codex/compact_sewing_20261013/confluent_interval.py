"""Rigorous Arb ball checks for fixed rational completed-response witnesses.

Requires python-flint==0.9.0. This is interval certification by FLINT/Arb,
not Lean kernel certification. No zero data or finite Euler product is used.
"""
from pathlib import Path
import json
import flint
from flint import arb, arb_series, ctx

HERE=Path(__file__).resolve().parent
ctx.prec=512
ctx.cap=14

def xi(s):
    return s*(s-1)/2*((-arb.pi().log()/2)*s).exp()*(s/2).gamma()*s.zeta()

def response(theta=None):
    u=arb_series([1,1])
    s=(1+u).sqrt()+arb(1)/2
    g=xi(s) if theta is None else xi(s-theta)*xi(s+theta)
    return g.derivative()/g

def form(m, nums):
    n=len(nums)
    v=[arb(x)*(16**i)/10**12 for i,x in enumerate(nums)]
    return sum(((-1)**(i+j+1))*m[i+j+1]*v[i]*v[j]
               for i in range(n) for j in range(n))

cases=[(1,4,[-9682278,2628919585,-110388767086,1000000000000],
        (-4137,10**18),(-4136,10**18),(1142,10**18),(1143,10**18)),
       (1,10,[2982360,-469147113,13622444934,-24113302030,-1000000000000],
        (-9143,10**21),(-9142,10**21),(1311,10**20),(1312,10**20))]
star=response()
rows=[]
for tn,td,nums,lo,hi,slo,shi in cases:
    control=form(response(arb(tn)/td),nums)
    positive=form(star,nums)
    bounds=[arb(x)/d for x,d in (lo,hi,slo,shi)]
    # Arb comparisons assert strict ordering of disjoint interval enclosures.
    checks=[bounds[0]<control,control<bounds[1],bounds[2]<positive,positive<bounds[3]]
    assert all(checks), (control,positive,checks)
    row={'theta':[tn,td],'dimension':len(nums),'witness_numerators':nums,
         'denominator':10**12,'theta_enclosure':control.str(60),
         'zeta_enclosure':positive.str(60),'rational_bounds':[lo,hi,slo,shi],
         'strict_interval_comparisons_pass':checks}
    rows.append(row);print(json.dumps(row),flush=True)
result={'library':'python-flint','version':flint.__version__,'bits':ctx.prec,
        'series_order':ctx.cap,'status':'ARB_INTERVAL_CERTIFIED_NOT_LEAN', 'cases':rows}
(HERE/'confluent_interval.json').write_text(json.dumps(result,indent=2)+'\n')
