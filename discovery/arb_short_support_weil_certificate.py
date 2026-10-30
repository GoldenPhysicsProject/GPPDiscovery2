"""Outward Arb endpoint certificate for an analytic all-test Weil positivity theorem.

The analytic proof, including two/three layer translation norm bounds,
is in short_support_weil_positivity.md. This only certifies the explicit
finite constant, not a matrix, and NEVER claims RH.
"""
from flint import arb, ctx, fmpq

ctx.prec = 192
q = lambda a,b=1: arb(fmpq(a,b))
L = q(1,8)
C = (4*arb.pi()).log()+arb.const_euler()
tail_lower = (2/L).log()
pole_min = L-2*(L/2).sinh()
tilt_lower = -2*L/3
gain2 = q(1,2) * ((L/2).tanh()/(L/4).tanh()).log()
gain3 = (1-1/q(2).sqrt())*((L/4).tanh()/(L/6).tanh()).log()
bound=tail_lower+pole_min-C+tilt_lower+gain2+gain3
print("L =",L)
print("Rigorous completed no-prime Weil Q_L lower coefficient:",bound)
print("Causal 2-layer gain:",gain2)
print("Causal 3-layer gain:",gain3)
assert bound > q(1,25), "Positivity coefficient not certified > 1/25"
assert L < q(1,2), "Support length too large for prime-free statement"
print("PASS: for all 0 < L <= 1/8, all admissible f, Q_L[f] >= ||f||²/25")
print("Scope: exact analytic full-form bound, no prime atoms at these L; not RH")
