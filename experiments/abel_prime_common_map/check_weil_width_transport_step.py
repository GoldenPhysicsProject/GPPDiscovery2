"""Exact rational subcertificate of the first scale-transport Weil step.

Checks finite rational inequalities only. Fourier multiplier bounds,
GPPVerify Weil identities, analytic K(1/8)>4 and exp/log/atan estimates
require independent formal verification. No RH claim.
"""
from fractions import Fraction as Q

L0=Q(1,8)
L1=Q(1251,10000)
assert L1-L0==Q(1,10000)
assert L1/L0==Q(1251,1250)
assert L1<Q(1,4)

# exp(16/5) < 31 follows from exp(t) <= (1-t/32)^(-32)
assert Q(10,9)**32<31
assert Q(16,5)+Q(15,16)>4

# Weak source K operator majorant at width 1/8.
Cinf_mag_upper=Q(2,3)+Q(6,5)+Q(8,5)+Q(21,10)
assert Cinf_mag_upper+Q(1,3)<6

base_eps=Q(1,121)
omega=(Q(12,1250)+Q(18,7*10000))/4
rho=Q(12,1250)/4
assert omega==Q(69,28000)
assert rho==Q(3,1250)
assert omega<base_eps
new_eps=(base_eps-omega)/(1+rho)
assert new_eps==Q(98255,16980656)
assert new_eps>Q(1,175)

print("PASS exact rational width-transport subcertificate")
print("L0 =",L0,"L1 =",L1)
print("base epsilon =",base_eps,"omega <",omega,"rho <",rho)
print("new epsilon >",new_eps,">",Q(1,175))
print("Analytic and Lean verification remain open.")
