"""Exact displacement-rank-two assembly of the corrected semilocal Weil form.

For distinct Fourier modes, Q[m,n]=(g[m]-g[n])/(pi*(n-m)).
The diagonal entries are retained from the independent full Weil evaluator.
All integrations are evaluated by complex-ball quadrature in python-flint.
This is a finite-window identity, not a positivity theorem or RH proof.
"""

import argparse
from flint import arb, ctx

import arb_semilocal_weil_matrix as full
from arb_multiwindow_certificates import certify_positive_definite

from arb_semilocal_weil_matrix import I, entry, prime_powers

ctx.prec = 512


def scalar_g(m, lam, bound):
    """Certified g_m from the regularized sine transform and prime atoms."""
    if m == 0:
        return arb(0)
    L = 2 * lam.log()
    omega = 2 * arb.pi() * m / L

    def integrand(z):
        # sin(omega*z)/sinh(z), expressed via entire sincs at z=0.
        sin_over_z = omega * (omega * z).sinc()
        sinh_over_z = (I * z).sinc()
        return ((z / 2).exp() + (-z / 2).exp()) * (omega * z).sin() \
            - (z / 2).exp() * sin_over_z / (2 * sinh_over_z)

    result = full.real_integral(integrand, L)
    for p, k in prime_powers(bound):
        result -= arb(p).log() / arb(k).sqrt() * (
            omega * arb(k).log()).sin()
    return result


def assemble(n, lam, bound):
    assert n >= 0
    modes = list(range(-n, n+1))
    # The kernel is real and invariant under simultaneous sign reversal:
    # g[-m]=-g[m] and Q[-m,-m]=Q[m,m].
    g = {0: arb(0)}
    diag = {0: entry(0, 0, lam, bound)[0]}
    for m in range(1, n + 1):
        g[m] = scalar_g(m, lam, bound)
        g[-m] = -g[m]
        diag[m] = entry(m, m, lam, bound)[0]
        diag[-m] = diag[m]
    Q = [[diag[m] if m == k else (g[m] - g[k]) / (arb.pi() * (k-m))
          for k in modes] for m in modes]
    return modes, Q, g


def parity_blocks(Q, n):
    """Orthogonal reflection splitting: even (n+1) and odd (n) blocks."""
    def q(m, k):
        return Q[m+n][k+n]
    if n == 0:
        return [[q(0, 0)]], []
    root2 = arb(2).sqrt()
    E = [[arb(0) for _ in range(n+1)] for _ in range(n+1)]
    O = [[arb(0) for _ in range(n)] for _ in range(n)]
    E[0][0] = q(0, 0)
    for m in range(1, n+1):
        E[0][m] = root2 * q(0, m)
        E[m][0] = E[0][m]
        for k in range(1, n+1):
            E[m][k] = q(m, k) + q(m, -k)
            O[m-1][k-1] = q(m, k) - q(m, -k)
    return E, O


def verify(n, lam, bound, check, use_blocks):
    modes, Q, g = assemble(n, lam, bound)
    if check == 'full':
        pairs = [(m, k) for m in modes for k in modes if m <= k]
    elif check == 'sample':
        pairs = sorted({(m, k) for m in modes for k in modes
                        if m <= k and (m == k or (m * 23 + k * 19) % 29 == 0)})
    else:
        pairs = []
    for m, k in pairs:
        direct, _ = entry(m, k, lam, bound)
        fast = Q[m+n][k+n]
        assert (direct-fast).contains(0), (m, k, direct, fast)
        assert (arb.pi() * (k-m) * fast - (g[m]-g[k])).contains(0), (m, k)
    print(f'PASS: {len(pairs)} independent Arb entry enclosures; '
          f'commutator rank <=2 follows symbolically, N={n}')
    if use_blocks:
        E, O = parity_blocks(Q, n)
        even_pivots = certify_positive_definite(E)
        odd_pivots = certify_positive_definite(O) if O else []
        print(f'CERTIFIED parity decomposition: {len(even_pivots)} even '
              f'and {len(odd_pivots)} odd strictly positive Arb LDL pivots; '
              f'even final={even_pivots[-1]}')
    else:
        pivots = certify_positive_definite(Q)
        print(f'CERTIFIED {len(pivots)} positive pivots; central={pivots[n]}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=3)
    ap.add_argument('--lambda-num', type=int, default=5)
    ap.add_argument('--lambda-den', type=int, default=2)
    ap.add_argument('--check', choices=('full', 'sample', 'none'), default='full')
    ap.add_argument('--parity-blocks', action='store_true')
    ap.add_argument('--bits', type=int, default=512)
    ap.add_argument('--tol-digits', type=int, default=85)
    args = ap.parse_args()
    assert args.lambda_num > args.lambda_den > 0
    assert 128 <= args.bits <= 8192
    assert 10 <= args.tol_digits <= 300
    ctx.prec = args.bits
    full.ARB_TOL = 10.0 ** (-args.tol_digits)
    exact_bound = args.lambda_num**2 // args.lambda_den**2
    verify(args.n, arb(args.lambda_num) / args.lambda_den,
           exact_bound, args.check, args.parity_blocks)
