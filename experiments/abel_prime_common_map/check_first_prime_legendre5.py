"""Exact rational subcertificate of the first-prime five-moment Weil index bound.

Checks arithmetic only. The source Weil identities, Legendre Fourier method,
cosine Taylor bounds and transcendental inequalities require analytic/Lean
formalization. This script does not prove global positivity or RH.
"""
from fractions import Fraction as Q
from math import factorial

L, R, m = Q(18, 25), Q(47, 4), 5
z = L*R/2
assert z == Q(423, 100)

def odd_factorial(n):
    p = 1
    for j in range(1, 2*n+2, 2):
        p *= j
    return p

def integrated_cos_upper(n):
    A = z*z / (2*(2*n+3))
    B = z**4 / (8*(2*n+3)*(2*n+5))
    assert A < 1
    # (2n+1) integral_0^1 u^(2n) (1-Au²+Bu⁴)² du
    F = (1 - 2*A*Q(2*n+1, 2*n+3)
         + (A*A + 2*B)*Q(2*n+1, 2*n+5)
         - 2*A*B*Q(2*n+1, 2*n+7)
         + B*B*Q(2*n+1, 2*n+9))
    assert 0 < F <= 1
    return F

finite = sum((
    z**(2*n) / odd_factorial(n)**2 * integrated_cos_upper(n)
    for n in range(m, 12)
), Q(0))
n = 12
ratio = z*z / (2*n+3)**2
assert ratio < 1
tail = z**(2*n) / odd_factorial(n)**2 / (1-ratio)
# Use 1/pi < 1/3.
delta_upper = L*R/3 * (finite + tail)
assert delta_upper < Q(9, 500)

a100 = sum((
    Q(16*R*R, (4*k+1)*((4*k+1)**2 + 4*R*R))
    for k in range(100)
), Q(0))
assert a100 > Q(1199, 200)

# gamma < H1024-10 log2, log2>693147/1e6.
H1024 = sum((Q(1,k) for k in range(1,1025)), Q(0))
assert H1024-10*Q(693147,1000000) < Q(578,1000)

# pi<3.1416 uses an independent sharp pi bound, NOT 22/7 alone.
pi_upper = Q(31416,10000)
assert pi_upper < Q(22,7)
x = Q(11448,10000)
assert sum((x**k/factorial(k) for k in range(8)), Q(0)) > pi_upper
assert pi_upper/2 == Q(15708,10000)

# 2(sinh(9/25)-9/25) ≤ x³/3 + x⁵/[60(1-x²)].
u = L/2
assert u**3/3 + u**5/(60*(1-u*u)) < Q(158,10000)
assert Q(14142,10000)**2 < 2
assert Q(693148,1000000)/Q(14142,10000) < Q(4902,10000)

Mmajor = (Q(578,1000)+Q(11448,10000)+Q(15708,10000)
          +Q(207945,100000)+Q(158,10000)+Q(4902,10000))
assert Mmajor == Q(117581,20000) < Q(147,25)

margin = Q(1199,200)*(1-Q(9,500))-Q(147,25)
assert margin == Q(709,100000)>0
assert Q(1199,200)*(1-Q(9,500)) == Q(588709,100000)

print("PASS: five-moment first-prime rational subcertificate")
print("L=",L,"R=",R,"z=",z)
print("100-term lower multiplier",float(a100),">5.995")
print("upper Fourier band leakage",float(delta_upper),"<0.018")
print("negative perturbation majorant",float(Mmajor),"<5.88")
print("strict L2 Weil margin >",margin)
print("analytic proof and Lean compilation remain independent obligations")
