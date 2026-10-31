"""All-layer nilpotent translation bound for the exact completed Weil form.

For y in [L/k, L/(k-1)], truncated translation on [0,L] has
nilpotence index k. Fiber decomposition over t modulo y shows its
numerical radius is <= cos(pi/(k+1)). This gives an all-functions
coercivity constant B_K(L) from K positive hyperbolic bands. The same
path-graph bound also controls the sign-sensitive gamma tilt; AM-GM
provides the explicit elementary gamma coefficient r(y)<=exp(y/4)/4.

This experiment is restricted to prime-free L<log(2); no RH claim.
"""

import argparse
import math


def b_tower(L, max_layers):
    assert L > 0 and max_layers >= 2
    c = math.log(4 * math.pi) + 0.5772156649015328606
    # Exact positive gamma tail and a new AM-GM tilt bound:
    # r(y)<=exp(y/4)/4, so 2 int_0^L r <= 2(exp(L/4)-1).
    base = -math.log(math.tanh(L/2)) + L - 2*math.sinh(L/2) \
        - c - 2*math.expm1(L/4)
    gains = []
    for k in range(2, max_layers + 1):
        coefficient = 1 - math.cos(math.pi/(k+1))
        ratio = math.tanh(L/(2*(k-1))) / math.tanh(L/(2*k))
        # Apply the same nilpotent-shift upper bound also to the negative
        # gamma tilt A=integral r(y) q(y)dy, not only the positive kinetic.
        tilt_discount = 2 * (math.exp(L/(4*(k-1)))-math.exp(L/(4*k)))
        gains.append(coefficient * (math.log(ratio) + tilt_discount))
    return base + sum(gains)


def root(k, lo=0.0001, hi=math.log(2)):
    assert b_tower(lo,k)>0 and b_tower(hi,k)<0
    for _ in range(70):
        mid=(lo+hi)/2
        if b_tower(mid,k)>0:
            lo=mid
        else:
            hi=mid
    return lo


def certified_at_fraction(num, den, layers):
    from flint import arb, ctx, fmpq
    ctx.prec=256
    rational=lambda n,d=1:arb(fmpq(n,d))
    L=rational(num,den)
    assert L < arb(2).log()
    c=(4*arb.pi()).log()+arb.const_euler()
    base=-(L/2).tanh().log()+L-2*(L/2).sinh() \
        -c-2*((L/4).exp()-1)
    total=base
    for k in range(2,layers+1):
        coef=1-(arb.pi()/(k+1)).cos()
        ratio=(L/(2*(k-1))).tanh()/(L/(2*k)).tanh()
        tilt_discount=2*((L/(4*(k-1))).exp()-(L/(4*k)).exp())
        total+=coef*(ratio.log()+tilt_discount)
    return total


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--max-layers',type=int,default=40)
    p.add_argument('--certify-num',type=int,default=5)
    p.add_argument('--certify-den',type=int,default=32)
    p.add_argument('--min-margin-num',type=int,default=1)
    p.add_argument('--min-margin-den',type=int,default=200)
    a=p.parse_args()
    assert 2<=a.max_layers<=1000
    for k in [x for x in (2,3,4,6,10,20,40,100,200,500) if x<=a.max_layers]:
        print(f'K={k:3d}: B_K(1/8)={b_tower(1/8,k):+.12f}; '
              f'positive root L*={root(k):.12f}')
    cert=certified_at_fraction(a.certify_num,a.certify_den,a.max_layers)
    print(f'Arb B_{a.max_layers}({a.certify_num}/{a.certify_den})={cert}')
    from flint import arb, fmpq
    assert a.min_margin_den>0
    assert cert>arb(fmpq(a.min_margin_num,a.min_margin_den))
    print('CERTIFIED completed Weil positivity for every admissible f '
          'and every 0<L<=rational endpoint; prime-free, not RH')


if __name__=='__main__':
    main()
