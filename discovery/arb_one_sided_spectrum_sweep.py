"""Rigorous lower/upper brackets for 1+lambda_min(T) on actual Weil matrices.

Builds the canonical completed prime-Archimedean matrix from the v34 source.
For each centered Fourier truncation, normalizes by its positive scalar
diagonal and certifies a rational *lower* spectral margin using interval LDL:
    (I + T) - delta I > 0.
A rational approximation to a numerical minimal eigenvector is evaluated
in Arb to certify a separate rational *upper* Rayleigh bound. Thus every
reported bracket is rigorous for that finite matrix. Nothing is uniform in
mode count or support length and no RH conclusion follows.
"""

import argparse
import math
import numpy as np
from flint import arb, fmpq, ctx

from arb_multiwindow_certificates import certify_positive_definite
from arb_semilocal_weil_matrix import entry

ctx.prec = 160
DEN = 10**6


def q(p, d=DEN):
    return arb(fmpq(p, d))


def inner(M, v):
    return sum((v[i]*M[i][j]*v[j]
                for i in range(len(v)) for j in range(len(v))), arb(0))


def bounds(Q):
    k = len(Q)
    assert all(Q[i][i] > 0 for i in range(k))
    H = [[(arb(1) if i==j else
           Q[i][j]/(Q[i][i]*Q[j][j]).sqrt())
          for j in range(k)] for i in range(k)]
    approx = np.array([[float(z.mid()) for z in row] for row in H])
    eigenvalues, eigenvectors = np.linalg.eigh(approx)
    est = float(eigenvalues[0])
    assert est > 0, 'Diagnostic found a nonpositive tentative gap'

    # Numerical eigenvalues only choose the rational delta candidate; LDL
    # on the ball matrix H-delta I establishes the actual lower bound.
    margin_int = max(0, int(math.floor(est*DEN))-2)
    while margin_int >= 0:
        shifted = [[H[i][j] - (q(margin_int) if i==j else arb(0))
                    for j in range(k)] for i in range(k)]
        try:
            certify_positive_definite(shifted)
            break
        except AssertionError:
            margin_int -= 1
    else:
        raise AssertionError('Could not certify even unshifted I+T positive')

    vec = [arb(fmpq(int(round(t*10**8)),10**8)) for t in eigenvectors[:,0]]
    norm2 = sum((u*u for u in vec),arb(0))
    assert norm2 > 0
    rayleigh = inner(H,vec)/norm2
    upper_int = int(math.ceil(float(rayleigh.mid())*DEN))+2
    while not rayleigh < q(upper_int):
        upper_int += 1
    assert 0 <= margin_int < upper_int
    return margin_int,upper_int,est


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--lambda-num',type=int,default=5)
    p.add_argument('--lambda-den',type=int,default=2)
    p.add_argument('--max-n',type=int,default=20)
    p.add_argument('--require-positive',action='store_true')
    args=p.parse_args()
    assert args.lambda_den > 0 and 0<=args.max_n<=64
    lam=arb(args.lambda_num)/args.lambda_den
    assert lam>1
    cutoff=(args.lambda_num**2)//(args.lambda_den**2)
    modes=list(range(-args.max_n,args.max_n+1))
    Q=[[entry(i,j,lam,cutoff)[0] for j in modes] for i in modes]
    ns=sorted({0,1,2,3,5,8,12,16,20,25,32,48,args.max_n} & set(range(args.max_n+1)))
    print(f'lambda={args.lambda_num}/{args.lambda_den}, L=2log(lambda), full modes={len(modes)}')
    for n in ns:
        idx=list(range(args.max_n-n,args.max_n+n+1))
        sub=[[Q[i][j] for j in idx] for i in idx]
        if args.require_positive:
            certify_positive_definite(sub)
        low,high,estimate=bounds(sub)
        print(f'N={n:2d}, dim={2*n+1:2d}, '
              f'CERTIFIED {low}/{DEN} < 1+lambda_min(T) < {high}/{DEN}; '
              f'numeric estimate={estimate:.9g}')


if __name__=='__main__':
    main()
