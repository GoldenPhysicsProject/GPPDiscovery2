"""Arb certifies boundary-Hardy Schur domination of first 3 prime-power atoms.

For E[f]=integral_0^infinity ||f(.+y)-f||²/(2 sinh y)dy and
S[f]=sum_{p**r<exp(L)} (log p)/sqrt(p**r)*q_f(log(p**r)),
one has E[f]-S[f]>= (1/125)||f||² for EVERY admissible f supported
on [0,L] with 0<L<=38/25. A stronger 3/100 margin holds through
L=3/2. This is a prime-inclusive all-functions
form inequality, NOT completed Weil positivity or RH.

Proof: E >= integral_0^L V_L(x)|f(x)|² dx,
V_L(x)=(H(x)+H(L-x))/2, H(x)=log coth(x/2).
|S| <= integral_0^L d_L(x)|f(x)|² dx where d is the weighted
degree of the p^r shift graph. For a fixed endpoint, check V-d at four
right endpoints in [0,L/2]; symmetry and V decreasing there prove
the pointwise inequality. Scaling x=tL extends it to all smaller L.
"""

from flint import arb, ctx, fmpq


def certify(L_num, L_den, margin_num, margin_den, bits=256):
    ctx.prec = bits
    L = arb(fmpq(L_num, L_den))
    a2, a3, a4, a5 = [arb(p).log() for p in (2, 3, 4, 5)]
    assert a4 < L < a5
    x4, x3, x2, middle = L-a4, L-a3, L-a2, L/2
    assert 0 < x4 < x3 < a2 < middle < x2
    w2 = a2 / arb(2).sqrt()
    w3 = a3 / arb(3).sqrt()
    w4 = a2 / 2  # p=2, r=2, i.e. n=4

    def H(z):
        assert z > 0
        return - (z/2).tanh().log()

    def V(z):
        return (H(z) + H(L-z))/2

    candidate_intervals = [
        ("[0,L-log4]", x4, w2+w3+w4),
        ("[L-log4,L-log3]", x3, w2+w3),
        ("[L-log3,log2]", a2, w2),
        ("[log2,L/2]", middle, 2*w2),
    ]
    margin = arb(fmpq(margin_num,margin_den))
    print(f'Endpoint L={L_num}/{L_den}; margin {margin_num}/{margin_den}')
    for label, end, degree in candidate_intervals:
        gap = V(end)-degree
        print(f'{label}: V(right)-degree = {gap}')
        assert gap > margin, f'Endpoint failed: {label}, {gap}'
    print(f'CERTIFIED: for every 0<L<={L_num}/{L_den}, E_L[f]-S_L[f]'
          f' >= ({margin_num}/{margin_den})||f||² for ALL admissible complex f.')
    print('Prime powers included: 2, 3, 4. Remaining pole/contact/tilt'
          ' not controlled. This is not RH.')


if __name__ == '__main__':
    certify(3,2,3,100)
    certify(38,25,1,125)
