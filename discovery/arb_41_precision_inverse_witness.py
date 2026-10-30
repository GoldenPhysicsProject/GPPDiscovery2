"""Certify an extremely small TRUE absolute 41-mode Weil eigenvalue.

Use 110-digit mpmath *only to generate a candidate vector*. The published
upper Rayleigh bound is checked on exact rational components using outward
512-bit Arb arithmetic against the corrected completed Weil matrix.
The lower bound is a separate strict Arb LDL certificate of Q-eps I.
"""
import os
import re
import mpmath as mp
from flint import arb,fmpq,ctx
from arb_semilocal_weil_matrix import entry
from arb_multiwindow_certificates import certify_positive_definite

ctx.prec=int(os.environ.get("GPP_ARB_PREC_BITS","512"))
mp.mp.dps=110
N=int(os.environ.get("GPP_ABS_N","20"))
modes=list(range(-N,N+1))
lam=arb(5)/2
Q=[[entry(i,j,lam,6)[0] for j in modes] for i in modes]
for i in range(len(Q)):
    assert Q[i][i]>0
certify_positive_definite(Q)
eps=arb(fmpq(1,10**23))
certify_positive_definite([
    [Q[i][j] - (eps if i==j else arb(0)) for j in range(len(Q))]
    for i in range(len(Q))])
def arb_mid_decimal(z):
    # python-flint prints even an Arb midpoint as "[digits +/- display_radius]"
    # at high precision. Extract its leading decimal approximation for trial
    # vector discovery ONLY; final Rayleigh is always rigorous in Arb.
    found=re.search(r'[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?',str(z.mid()))
    assert found, z
    return mp.mpf(found.group(0))
A=mp.matrix([[arb_mid_decimal(z) for z in row] for row in Q])
Inv=A**-1
v=mp.matrix([mp.mpf((-1)**i)/(i+1) for i in range(len(Q))])
for step in range(20):
    w=Inv*v
    nv=mp.sqrt((w.T*w)[0])
    v=w/nv
numeric_ray=(v.T*A*v)[0]
scale=10**78
vr=[arb(fmpq(int(mp.nint(z*scale)),scale)) for z in v]
den=sum((z*z for z in vr),arb(0))
assert den>0
out=sum((vr[i]*Q[i][j]*vr[j] for i in range(len(vr)) for j in range(len(vr))),arb(0))/den
assert out > eps
assert out < arb('1e-14')
print(f'CERTIFIED corrected 41-mode λ_min(Q) > 1e-23')
print(f'CERTIFIED λ_min(Q) <= exact-rational Rayleigh = {out}')
print('110-digit inverse-iteration trial value:',mp.nstr(numeric_ray,50))
print('Scope: only λ=5/2,N=20 corrected finite matrix, not full Weil or RH')
