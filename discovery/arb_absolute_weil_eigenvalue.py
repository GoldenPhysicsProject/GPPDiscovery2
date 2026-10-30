"""Corrected exact Weil Q absolute eigenvalue vs normalized Schur gap.

All reported positivity LOWER bounds are outward Arb LDL certificates of
Q-epsilon I. Upper bounds use exact rational trial vectors in interval
Rayleigh quotients. Float eigensolves select trial vectors only.
"""
import os, math
import numpy as np
from flint import arb, fmpq, ctx
from arb_semilocal_weil_matrix import entry
from arb_multiwindow_certificates import certify_positive_definite
ctx.prec=int(os.environ.get("GPP_ARB_PREC_BITS","512"))
lam=arb(5)/2
cutoff=6
maxN=int(os.environ.get("GPP_ABS_N","20"))
modes=list(range(-maxN,maxN+1))
Q=[[entry(i,j,lam,cutoff)[0] for j in modes] for i in modes]
for N in sorted({0,1,2,3,5,8,12,16,20,maxN}&set(range(maxN+1))):
    inds=list(range(maxN-N,maxN+N+1))
    M=[[Q[i][j] for j in inds] for i in inds]
    certify_positive_definite(M)
    A=np.array([[float(x.mid()) for x in row] for row in M])
    vals,vecs=np.linalg.eigh(A)
    estimate=float(vals[0])
    lower=None
    for power in range(1,81):
        delta=arb(fmpq(1,10**power))
        shift=[[M[i][j]-(delta if i==j else arb(0)) for j in range(len(M))] for i in range(len(M))]
        try:
            certify_positive_definite(shift)
            lower=power
            break
        except AssertionError:
            continue
    assert lower is not None
    v=[arb(fmpq(int(round(x*10**12)),10**12)) for x in vecs[:,0]]
    norm=sum((x*x for x in v),arb(0))
    ray=sum((v[i]*M[i][j]*v[j] for i in range(len(v)) for j in range(len(v))),arb(0))/norm
    assert ray>0
    print(f'N={N:2d} dim={2*N+1:2d} absolute LDL lower > 1e-{lower} '
          f'upper via rational Rayleigh {ray} float trial eig {estimate:.12g}', flush=True)
print('Scope: genuine corrected finite matrices only; NOT all-N or RH.')
