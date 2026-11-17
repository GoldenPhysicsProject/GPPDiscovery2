"""Exact rational subcertificate for the six-moment first-prime Weil bound.

Verifies only arithmetic; separate Weil identities, Fourier-Plancherel,
Legendre moment inequalities, and transcendental comparisons need Lean audit.
"""
from fractions import Fraction as Q
from math import factorial

L, R, m = Q(18,25), Q(25,2), 6
z=L*R/2
assert z==Q(9,2)
odd=1
for k in range(1,2*m+2,2):
    odd*=k
assert odd==135135
ratio=z*z/(2*m+3)**2
assert ratio==Q(9,100)
# 1/pi < 1/3, first geometric Legendre tail:
delta=L*R/3*(z**(2*m)/odd**2)/(1-ratio)
assert delta<Q(1,80)
# Positive 100-term partial sum of archimedean multiplier.
a100=sum((Q(16*R*R,(4*k+1)*((4*k+1)**2+4*R*R)) for k in range(100)),Q(0))
assert a100>Q(121,20)
H256=sum((Q(1,k) for k in range(1,257)),Q(0))
assert H256-8*Q(6931,10000)<Q(29,50)
x=Q(23,20)
assert sum((x**j/factorial(j) for j in range(6)),Q(0))>Q(22,7)
u=L/2
assert u**3/(3*(1-u*u))<Q(9,500)
assert Q(7,5)**2<2
M=(Q(29,50)+Q(23,20)+Q(11,7)+Q(52,25)+Q(9,500)+Q(1,2))
assert M==Q(5162,875)<Q(59,10)
margin=Q(121,20)*(1-Q(1,80))-Q(59,10)
assert margin==Q(119,1600)>0
print("PASS six-moment exact rational certificate")
print("L",L,"R",R,"a100",float(a100),">6.05")
print("low-frequency fraction <",float(delta),"<1/80")
print("negative bound <=",float(M),"<5.9")
print("positive lower margin >",margin,float(margin))
