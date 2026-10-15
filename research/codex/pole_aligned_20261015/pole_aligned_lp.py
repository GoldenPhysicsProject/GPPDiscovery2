"""UNTRUSTED floating LP: exact on-window *polar-aligned* completion.

Daniel Toupin / Golden Physics Project, Codex 2026-10-15.
This is an experiment, not interval certification or RH.
Run: python pole_aligned_lp.py 0.5
Or:  python pole_aligned_lp.py 0.4
"""
import json
import sys
import numpy as np
from scipy.special import digamma
from scipy.optimize import linprog

h = float(sys.argv[1]) if len(sys.argv) > 1 else .5
L = 2 * h
z = np.linspace(L, 7, 17)
dz = np.diff(z)
K = 221
u = L + np.arange(K) / 20
y0 = np.cosh(h)
kap = np.log(2) / np.sqrt(2)

def build(x):
    x = np.asarray(x)
    xx = np.maximum(x*x, 1e-25)
    safe = np.maximum(x, 1e-12)
    co = np.cos(x[:, None] * z[None, :])
    ph = np.empty((len(x), 16))
    pos = x > 1e-7
    ph[:, 0] = np.where(pos,
        (co[:, 0]-co[:, 1])/(dz[0]*xx) - np.sin(L*x)/safe, dz[0]/2)
    for j in range(1, 16):
        ph[:, j] = np.where(pos,
            ((co[:,j]-co[:,j-1])/dz[j-1] +
             (co[:,j]-co[:,j+1])/dz[j])/xx, (dz[j-1]+dz[j])/2)
    # Exact half-line cosine transform of cosh(t/2), t in [0,2h].
    pole = (.5*np.sinh(h)*np.cos(L*x) +
            x*np.cosh(h)*np.sin(L*x)) / (.25+x*x)
    base = (digamma(.25+.5j*x).real - np.log(np.pi)
            - 2*kap*np.cos(x*np.log(2))
            + 4*(pole+y0*ph[:,0]))
    # m=base+4 sum(y_j*ph_j) - sum(a_k*cos(u_k*x)).
    mat = np.column_stack((4*ph[:,1:], -np.cos(x[:,None]*u),
                           -np.ones((len(x),1))))
    return base, mat

x = np.unique(np.concatenate((np.arange(0,451,.45),
    np.arange(0,30,.12), np.arange(125.5,126.6,.05))))
result = None
for it in range(5):
    base, matrix = build(x)
    cost = np.zeros(matrix.shape[1])
    cost[-1] = -1
    result = linprog(cost, A_ub=-matrix, b_ub=base,
        bounds=[(-30,30)]*15 + [(-5,5)]*K + [(-100,10)],
        method="highs", options={"time_limit":80})
    if not result.success:
        print(it, "LP infeasible/failed", result.message, flush=True)
        break
    xf = np.arange(0,453,.035)
    bf,mf = build(xf)
    value = bf + mf[:,:-1] @ result.x[:-1]
    loc = int(np.argmin(value))
    print("iter",it,"LP margin",result.x[-1],"fine min",
          value[loc],"freq",xf[loc],flush=True)
    worst = np.argsort(value)[:100]
    extra = xf[worst[value[worst] < result.x[-1]-1e-6]]
    x = np.unique(np.concatenate([x,extra]))
    if not len(extra):
        break
if result is not None and result.success:
    out = {"status":"UNTRUSTED FLOAT LP; NOT a certificate",
        "h":h,"L":L,"K":K,"knots":z.tolist(),
        "y0":float(y0),"y_ext":result.x[:15].tolist(),
        "a_cos":result.x[15:-1].tolist(),
        "coarse_margin":float(result.x[-1]),
        "fine_min":float(value.min()),
        "fine_min_frequency":float(xf[np.argmin(value)]),
        "sample_count":int(len(x))}
    with open("pole_aligned_h%s_float.json"%str(h).replace(".","p"),"w") as f:
        json.dump(out,f,indent=2)
