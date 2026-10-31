"""Certified first-prime activation control by the full archimedean kinetic form.

For a=log(p**r)<L and epsilon=L-a, the two end strips of width epsilon
control the autocorrelation q_f(a). Their L2 mass is charged by zero
extension into the entire positive logarithmic kinetic E[f]. Thus

    |q_f(a)| <= 2 E[f] / log(coth(epsilon/2)).

This is a genuine all-functions form estimate for the SIGNED prime atoms,
not a proof that the completed Weil quadratic form is positive. At
L=57/50, precisely the p=2 and p=3 atoms occur, and Arb proves their
combined relative bound is <1 (uniformly for all shorter supports).
"""

import argparse
import math


def kappa_float(L):
    atoms = [(2, 2), (3, 3), (2, 4), (5, 5), (2, 8), (3, 9)]
    ans = 0.0
    for p, n in atoms:
        eps = L - math.log(n)
        if eps > 0:
            log_coth = -math.log(math.tanh(eps / 2))
            ans += 2 * (math.log(p) / math.sqrt(n)) / log_coth
    return ans


def arb_certificate(num=57, den=50, bits=256):
    from flint import arb, ctx, fmpq
    ctx.prec = bits
    L = arb(fmpq(num, den))
    assert arb(3).log() < L < arb(4).log(), (
        "This specialized certificate assumes exactly p=2, p=3")
    kap = arb(0)
    terms = []
    for prime in (2, 3):
        a = arb(prime).log()
        eps = L - a
        log_coth = -(eps / 2).tanh().log()
        term = 2 * a / (arb(prime).sqrt() * log_coth)
        terms.append((prime, term))
        kap += term
    assert kap < arb(1), f"prime form bound not strictly below one: {kap}"
    return kap, 1-kap, terms


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', type=int, default=57)
    parser.add_argument('--den', type=int, default=50)
    args = parser.parse_args()
    assert args.den > 0 and args.num > 0
    for L in (math.log(2)+0.01, math.log(3)+0.001, 1.12, 1.14, 1.15):
        print(f'L={L:.10f}: exploratory prime/E ratio={kappa_float(L):.12f}')
    kap, margin, terms = arb_certificate(args.num, args.den)
    for prime, bound in terms:
        print(f'p={prime} certified contribution coefficient = {bound}')
    print(f'Arb K({args.num}/{args.den}) = {kap}')
    print(f'Arb 1-K({args.num}/{args.den}) = {margin}')
    print('CERTIFIED every supported complex f, for all 0<L<=endpoint:')
    print('E[f] - sum_p(log p)/sqrt(p) q_f(log p) >= (1-K(endpoint)) E[f] >= 0')
    print('Scope: primes p=2,3; independent of finite N; no completed Q>=0/RH claim.')


if __name__ == '__main__':
    main()
