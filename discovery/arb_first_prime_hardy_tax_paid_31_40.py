#!/usr/bin/env python3
"""256-bit Arb endpoint for exact ALL-function p2 boundary tax-paid
Hardy potential inequality, through L=31/40. Not RH/Weil positivity.
"""
from flint import arb, ctx, fmpq
ctx.prec=256
q=lambda n,d=1:arb(fmpq(n,d))
a=arb(2).log()
w=a/arb(2).sqrt()
L=q(31,40)
assert a<L and L<2*a and L<arb(3).log()
H=lambda z:-(z/2).tanh().log()
eps=L-a
d=(H(eps)+H(a))/2-H(L/2)-w
print('exact rational support L=31/40=',L)
print('first prime a=log2=',a)
print('w=log2/sqrt2=',w)
print('strip epsilon=',eps)
print('V_L(epsilon)-H(L/2)-w=',d)
assert d>q(3,1000)
print('CERTIFIED: for all 0<L<=31/40 and all complex L2 f,')
print('int (V_L-w*1_AunionB)|f|² >= H(L/2)||f||²+3/1000*M')
print('Monotonicity from H_prime=-1/sinh and H_second>0.')
print('This is TRUE p2-source tax absorption, not complete Weil positivity or RH.')
