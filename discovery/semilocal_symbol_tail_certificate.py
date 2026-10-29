"""Arb certificate that the completed Weil Fourier symbol is positive at high frequency.

For the exact semilocal form of v34 and f supported in [0,L], Plancherel gives

  Psi#(q_f) = integral_R h_L(xi) |fhat(xi)|^2 dxi,
  h_L(xi) = m(xi) + 2 integral_0^L k(y) cos(xi*y) dy
            - (log(4*pi) + Euler) - 2 sum_powers w_p cos(xi*log(p^r)),
  m(xi) = Re digamma(1/2 + i*xi/2) - digamma(1/2),
  k(y) = 2*cosh(y/2) - t^2/((t+1)*(t^2+1)), t=exp(y/2).

Elementary integration by parts and the bounds 0 <= r <= 1/3,
|r'| <= 1/6 imply
  |2 integral_0^L k(y) cos(xi*y)dy|
     <= (8*cosh(L/2) - 10/3 + L/3)/|xi|.

The multiplier m is increasing on xi>=0. Hence an Arb-positive lower
margin at radius R certifies h_L(xi)>0 for every real |xi|>=R.
This does NOT certify positivity on time-limited functions: their Fourier
transforms cannot be confined to a finite frequency interval, and the
remaining band requires a rigorous low/high spectral sewing theorem.
"""

import argparse
from flint import acb, arb, ctx

from arb_semilocal_weil_matrix import prime_powers

ctx.prec = 192


def certify_tail(lambda_num: int, lambda_den: int, radius: int):
    assert lambda_den > 0 and lambda_num > lambda_den and radius > 0
    lam = arb(lambda_num) / arb(lambda_den)
    L = 2 * lam.log()
    cutoff = (lambda_num * lambda_num) // (lambda_den * lambda_den)
    weights = sum((arb(p).log() / arb(power).sqrt()
                   for p, power in prime_powers(cutoff)), arb(0))
    half = arb(1) / 2
    m_radius = acb(half, arb(radius) / 2).digamma().real - half.digamma()
    contact = (4 * arb.pi()).log() + arb.const_euler()
    variation = 8 * (L / 2).cosh() - arb(10) / 3 + L / 3
    margin = m_radius - contact - 2 * weights - variation / radius
    print(f'lambda={lambda_num}/{lambda_den}, L={L}')
    print(f'exact prime-power cutoff={cutoff}, sum weights={weights}')
    print(f'R={radius}; m(R)={m_radius}; contact={contact}; '
          f'oscillatory variation constant={variation}')
    print(f'CERTIFIED lower bound on h_L(|xi|>=R): {margin}')
    assert margin > 0, 'Cannot certify positive tail at this radius'
    print('Certificate scope: all REAL |xi|>=R for exact semilocal symbol; '
          'not all functions and not RH')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--lambda-num', type=int, default=5)
    p.add_argument('--lambda-den', type=int, default=2)
    p.add_argument('--radius', type=int, default=512)
    args = p.parse_args()
    certify_tail(args.lambda_num, args.lambda_den, args.radius)


if __name__ == '__main__':
    main()
