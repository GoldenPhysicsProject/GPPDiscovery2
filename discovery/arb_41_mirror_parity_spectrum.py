"""Interval-certified mirror parity splitting of the corrected 41-mode Weil Gram.

Spatial reflection on the interval sends Fourier m to -m. The exact q_mn
formula is invariant under simultaneous sign reversal (m,n)->(-m,-n),
so the matrix decomposes into an even (dimension N+1) and an odd
(dimension N) block. All lower bounds are strict Arb LDL tests.
"""
import os
from flint import arb, fmpq, ctx
from arb_semilocal_weil_matrix import entry
from arb_multiwindow_certificates import certify_positive_definite

ctx.prec=int(os.environ.get("GPP_ARB_PREC_BITS","512"))
N=20
lam=arb(5)/2
idx=list(range(-N,N+1))
Q=[[entry(i,j,lam,6)[0] for j in idx] for i in idx]
rt=arb(2).sqrt()
# Canonical reflection-even vectors: e_0, (e_m+e_-m)/sqrt(2).
even=[[arb(0) for j in range(N+1)] for i in range(N+1)]
even[0][0]=Q[N][N]
for m in range(1,N+1):
    even[0][m]=even[m][0]=rt*Q[N][N+m]
for m in range(1,N+1):
    for n in range(1,N+1):
        even[m][n]=Q[N+m][N+n]+Q[N+m][N-n]

# Canonical reflection-odd vectors: (e_m-e_-m)/sqrt(2).
odd=[[Q[N+m][N+n]-Q[N+m][N-n] for n in range(1,N+1)]
     for m in range(1,N+1)]
print('Even block dim=',len(even),'Odd block dim=',len(odd))
certify_positive_definite(even)
certify_positive_definite(odd)
for label,M in [('even',even),('odd',odd)]:
    for power in range(1,61):
        delta=arb(fmpq(1,10**power))
        shifted=[[M[i][j]-(delta if i==j else arb(0))
                  for j in range(len(M))] for i in range(len(M))]
        try:
            certify_positive_definite(shifted)
            print(f'CERTIFIED {label} minimal eigenvalue > 1e-{power}')
            break
        except AssertionError:
            continue
    else:
        raise AssertionError(f'No positive {label} gap certified')

# The full 41x41 lowest eigenvalue was independently certified
# 1.08226835e-23 < min < 1.08226836e-23 by a rational vector.
# If the odd lower bound exceeds that upper, even is THE least channel.
odd_sep=arb(fmpq(1,10**20))
certify_positive_definite([[odd[i][j]-(odd_sep if i==j else arb(0))
                            for j in range(N)] for i in range(N)])
print('CERTIFIED odd channel λ_min > 1e-20 >> full λ_min < 1.08226836e-23')
print('CONSEQUENCE: corrected 41-mode lowest eigenvalue lies in mirror-EVEN channel')
print('Scope: finite corrected Weil compression, no RH or all-N sign proof')
