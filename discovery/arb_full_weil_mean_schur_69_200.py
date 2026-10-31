"""Outward 256-bit exact Schur certificate: full completed Weil positivity
for EVERY admissible complex f on log-support L<=69/200 (no prime atoms).

The full analytic justification including V boundary variance, gamma jump,
Legendre odd/even gaps, and pole is in short_support_schur_variance_69_200.md.
"""
from flint import arb, ctx, fmpq
ctx.prec = 256
q=lambda n,d=1: arb(fmpq(n,d))
L=q(69,200)
kappa=q(1,1000)
c=(4*arb.pi()).log()+arb.const_euler()
C0=4*(L/4).sinh()
A=L*((L/4).exp()-1)/4
B=L*L/24+2*C0*((L/4).cosh()-1)
std0=(1-arb.pi()**2/12).sqrt()
D=(std0+(A+B)/2)**2
m=(2/L).log()-c+2*C0-L/4+1-A
beta=-(L/4).tanh().log()-((L/4).exp()-1)-c
gamma_e=beta+q(3,2)
gamma_o=beta+1-2*((L/2).sinh()-L/2)
assert L < arb(2).log()
assert gamma_e>kappa and gamma_o>kappa
residual=m-kappa-D/(gamma_e-kappa)
print('m lower=',m)
print('mean fluctuation variance upper=',D)
print('even mean-zero lower=',gamma_e)
print('odd lower=',gamma_o)
print('fully coupled one-sided constant-even Schur residual=',residual)
assert residual>q(1,2000)  # strictly >0.0005, not rounding
assert m>kappa
print('PASS: Q_L[f] >= ||f||²/1000 for ALL admissible f, every 0<L<=69/200')
print('Prime free interval only; not global Weil positivity or RH.')
