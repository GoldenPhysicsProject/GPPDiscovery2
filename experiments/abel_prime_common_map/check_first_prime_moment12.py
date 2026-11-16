"""Exact rational checks for the first-prime 12-moment Weil negative-index bound.

This checks the arithmetic lemmas only; analytic Fourier and Weil identities
and elementary transcendental inequalities need separate proofs in Lean.
"""
from fractions import Fraction as Q
from math import factorial

L = Q(18, 25)
R = 11
m = 12

# Finite lower bound of the real-place Fourier multiplier at 11.
a_partial = sum(
    (Q(16*R*R, (4*k+1)*((4*k+1)**2 + 4*R*R))
     for k in range(100)), Q(0))
assert a_partial > Q(593, 100)

# Bandlimiting for twelve vanishing spatial moments.
# True delta has pi in the denominator; pi>3 suffices here.
delta_upper = L*R/3 * ((Q(R)*L/2)**m / factorial(m))**2
assert delta_upper < Q(1, 300)

# Bound the negative real-place scalar, sinh pole and the single prime.
# Inputs: gamma<29/50, log pi<23/20, pi/2<11/7,
# 3log2<52/25, 2(sinh(9/25)-9/25)<9/500, log2/sqrt2<1/2.
M_upper = Q(29,50)+Q(23,20)+Q(11,7)+Q(52,25)+Q(9,500)+Q(1,2)
assert M_upper == Q(5162,875) < Q(59,10)

x = L/2
sinh_remainder_bound = x**3/(3*(1-x*x))
assert sinh_remainder_bound == Q(243,13600) < Q(9,500)

# Derive gamma<29/50 using H256-log256 and log2>6931/10000.
H256 = sum((Q(1,j) for j in range(1,257)), Q(0))
assert H256-8*Q(6931,10000) < Q(29,50)

# Derive log(pi)<23/20 via pi<22/7 and exp Taylor lower bound.
z = Q(23,20)
exp_lower = sum((z**j/factorial(j) for j in range(6)), Q(0))
assert exp_lower > Q(22,7)

# Derive log2/sqrt2 < 1/2 via log2<7/10, sqrt2>7/5.
assert Q(7,5)**2 < 2

margin = Q(593,100)*(1-Q(1,300))-Q(59,10)
assert margin == Q(307,30000) > 0

print("PASS: 12-moment rational certificate")
print("100-term multiplier partial sum:", float(a_partial))
print("Fourier mass bound delta <", Q(1,300), "checked:", float(delta_upper))
print("Bounded-perturbation majorant:", M_upper)
print("Positive margin:", margin)
print("Analytic/Lean obligations: Weil source identity, Fourier multiplier,")
print("complex Taylor remainder, overlap lemma, transcendental inequalities.")
