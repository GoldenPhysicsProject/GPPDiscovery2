"""Certified cover of the potentially negative frequency set of the Weil symbol.

The exact semilocal Fourier multiplier H_L is even and has a certified
positive tail. On each rational cell [x,x+h], x>0, use:
 * m(xi) >= m(x) (positive digamma odd-series monotonicity),
 * 2 int_0^L k(y) cos(xi*y)dy >= -B_L/x,
 * cos(xi*a) <= cos((x+h/2)*a) + (h/2)*a for a>0.
Everything on the right is Arb-enclosed. Cells that cannot be certified
above a positive target are added to a symmetric bad-frequency cover E.
For f with Fourier modes |m|>N, pointwise Cauchy-Schwarz yields
    int_E |fhat|^2 dxi/(2pi) <= 4*L*meas(E)/(pi^3*N) * ||f||^2
if N > R*L/pi, and thus Q_L is strictly positive on that entire
infinite-dimensional subspace when the printed bound is Arb-positive.

This is a sufficient but conservative cover; bad cells may be positive.
No certificate for the finite lower Fourier block or RH is implied.
"""

import argparse

from flint import acb, arb, ctx, fmpq
from arb_semilocal_weil_matrix import prime_powers

ctx.prec = 192


def rational(n, d=1):
    return arb(fmpq(n, d))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lambda-num', type=int, default=5)
    parser.add_argument('--lambda-den', type=int, default=2)
    parser.add_argument('--radius', type=int, default=1024)
    parser.add_argument('--inner', type=int, default=20)
    parser.add_argument('--step-den', type=int, default=10)
    parser.add_argument('--gap-num', type=int, default=1)
    parser.add_argument('--gap-den', type=int, default=2)
    parser.add_argument('--fourier-tail-n', type=int, default=1500)
    args = parser.parse_args()
    assert 0 < args.inner < args.radius
    assert args.step_den > 0 and args.gap_den > 0
    assert args.lambda_num > args.lambda_den > 0
    assert args.fourier_tail_n > 0

    lam = rational(args.lambda_num, args.lambda_den)
    L = 2*lam.log()
    cutoff = args.lambda_num**2 // args.lambda_den**2
    powers = prime_powers(cutoff)
    weights = [(arb(p).log()/arb(k).sqrt(), arb(k).log())
               for p,k in powers]
    total_w = sum((w for w,a in weights),arb(0))
    half = rational(1,2)
    psi_half = half.digamma()
    contact = (4*arb.pi()).log()+arb.const_euler()
    B = 8*(L/2).cosh()-rational(10,3)+L/3
    margin_tail = (acb(half,rational(args.radius,2)).digamma().real
                   -psi_half-contact-2*total_w-B/args.radius)
    target = rational(args.gap_num,args.gap_den)
    assert margin_tail > target, 'Far-frequency tail below desired target gap'

    assert (args.radius-args.inner)*args.step_den == int((args.radius-args.inner)*args.step_den)
    count = (args.radius-args.inner)*args.step_den
    unresolved = 0
    worst_certified_lower = None
    # Cell endpoints and midpoints use EXACT rational Arb scalars.
    h = rational(1,args.step_den)
    for cell in range(count):
        left = rational(args.inner*args.step_den+cell,args.step_den)
        middle = left+h/2
        m_left = acb(half,left/2).digamma().real-psi_half
        cosine_upper = sum((w*((a*middle).cos()+a*h/2)
                            for w,a in weights),arb(0))
        lower = m_left-contact-2*cosine_upper-B/left
        if not lower >= target:
            unresolved += 1
        elif worst_certified_lower is None or lower < worst_certified_lower:
            worst_certified_lower = lower

    # E includes the entire [0,inner] interval and all unresolved cells,
    # reflected across 0. Every other real frequency has H_L>=target.
    bad_measure = 2*(arb(args.inner)+rational(unresolved,args.step_den))
    assert rational(args.fourier_tail_n)>arb(args.radius)*L/arb.pi()
    leakage = 4*L*bad_measure/(arb.pi()**3*args.fourier_tail_n)
    worst_negative = 8*(L/2).sinh()+contact+2*total_w
    positive_margin = target - (target+worst_negative)*leakage

    print(f'lambda={args.lambda_num}/{args.lambda_den}, L={L}')
    print(f'far tail |xi| >= {args.radius}: margin={margin_tail} > {target}')
    print(f'certified rational cells: {count-unresolved}/{count}; '
          f'unresolved: {unresolved}')
    print(f'symmetric bad set measure <= {bad_measure}; '
          f'leakage into it <= {leakage}')
    print(f'CERTIFIED coercivity for all Fourier modes |m|>{args.fourier_tail_n}: '
          f'Q_L[f]/||f||^2 >= {positive_margin}')
    assert positive_margin > 0, 'Bad-frequency cover still too large'
    print('Scope: whole infinite high-mode subspace at fixed L, '
          'not low/high Schur positivity or RH')


if __name__ == '__main__':
    main()
