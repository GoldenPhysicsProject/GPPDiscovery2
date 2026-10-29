"""Outward Arb one-sided lower spectral margin for corrected completed Weil Q.

A strict LDL certificate of Q - delta*diag(Q) > 0 gives a nonzero
normalized lower gap 1+lambda_min(T) > delta. This is finite N,L only.
"""
import os
from flint import arb, fmpq, ctx
from arb_semilocal_weil_matrix import entry
from arb_multiwindow_certificates import certify_positive_definite
ctx.prec = int(os.environ.get("GPP_ARB_PREC_BITS", "160"))

lam=arb(5)/2
modes=list(range(-20,21))
Q=[[entry(i,j,lam,6)[0] for j in modes] for i in modes]
assert all(Q[i][i] > 0 for i in range(len(Q)))
pivots=certify_positive_definite(Q)
print("CERTIFIED positive corrected completed Weil 41-mode matrix, pivots:",len(pivots))
for exponent in [4,8,12,16,20,24,28,32,36,40,44,48,52,56,64,72]:
    delta=arb(fmpq(1,10**exponent))
    shifted=[[Q[i][j] - (delta*Q[i][i] if i==j else arb(0))
              for j in range(len(Q))] for i in range(len(Q))]
    try:
        certify_positive_definite(shifted)
    except AssertionError:
        continue
    print(f"CERTIFIED normalized one-sided gap > 10^(-{exponent})")
    break
else:
    raise AssertionError("No strict one-sided 41-mode margin certified")
print("Finite window certificate only; no claim uniform in N,L or RH")
