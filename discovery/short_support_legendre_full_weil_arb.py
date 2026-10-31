"""Arb full completed Weil all-function bound L <= 303/1000 (prime-free).

New analytic input: shifted Legendre diagonalization of the log kernel
J0[f]=1/2 ∫_(x<z) |f(x)-f(z)|²/(z-x) dx dz, with eigenvalues
H_n on normalized P_n(2x/L-1). Therefore J0[f] >= ||f-mean f||².
For 0 < y <= L <= 1, true gamma jump weight
w(y)=e^(y/2)/(2sinh y) >= 1/(2y).
Thus in previously proved two-channel mean/variance argument
replace the coarse L*w(L) by the SHARP universal 1.

All other local-potential and cosh/sinh pole estimates identical to
discovery/short_support_mean_variance_weil.md. The only numerical gate
below is 256-bit outward Arb. The analytic Legendre proof is in
discovery/legendre_log_jump_weil.md.
"""
from flint import arb,ctx,fmpq
ctx.prec=256
q=lambda n,d=1:arb(fmpq(n,d))
L=q(303,1000)
eta=q(1,1000)
c=(4*arb.pi()).log()+arb.const_euler()
beta=-(L/4).tanh().log()-((L/4).exp()-1)-c
C0=4*(L/4).sinh()
cosh_var=L/2+(L/2).sinh()-C0*C0/L
sinh_norm=(L/2).sinh()-L/2
mean=beta+2*(1-eta)*C0*C0/L
fluct=beta+1-2*(1/eta-1)*cosh_var-2*sinh_norm
assert 0<L<arb(2).log() and L<1
assert cosh_var>0 and sinh_norm>0
assert mean>q(1,1000)
assert fluct>q(1,1000)
print('FULL completed Weil all admissible f, support <=303/1000; no primes')
print('beta=', beta)
print('mean-channel=',mean,' >1/1000')
print('mean-zero fluct-channel=',fluct,' >1/1000')
print('CERTIFIED Q[f] >= 1/1000 ||f||² by analytic log-Legendre'
      ' jump eigenvalue H_1=1, Young pole, and Arb endpoint scalars.')
print('This is prime-free only, not RH, analytic Legendre theorem'
      ' is not yet formalized in Lean.')
