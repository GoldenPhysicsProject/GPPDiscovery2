"""Arb-certified scalar endpoints for exact Legendre logarithmic kinetic suppliers.

ANALYTIC theorem (see adjacent .md):
On [0,L], operator Af(x)=∫(f(x)-f(y))/|x-y|dy is diagonal on shifted
Legendre polynomials: A P_n = 2 H_n P_n. Its quadratic form J0=1/2<f,Af>
is >= ||f||² for reflection-odd f and >= 3/2||f||² for reflection-even
mean-zero f. For 0<y<=L<=1, completed gamma interior jump weight
exp(y/2)/(2sinh y) >= 1/(2y); hence J_gamma >= J0.

No primes for L<=43/100<log2. Full Q pole = +2|C|²-2|S|².
Odd f: C=0, |S|²<=||sinh((x-L/2)/2)||² ||f||².
Even mean-zero f: S=0 and positive C can be dropped.
Local potential V-Gamma-c >= beta(L) as in the earlier exact SOS.

All inequalities claimed for all smaller supports are obtained by
embedding into a FIXED ambient interval [0,43/100] and applying the
reflection/mean conditions relative to that ambient midpoint. This
does not say a function odd around its OWN smaller interval inherits
the ambient odd symmetry automatically unless centered consistently.
"""
from flint import arb, ctx, fmpq

ctx.prec = 256
q = lambda n,d=1: arb(fmpq(n,d))
L=q(43,100)
c=(4*arb.pi()).log()+arb.const_euler()
beta=-(L/4).tanh().log()-((L/4).exp()-1)-c
s_norm_sq=(L/2).sinh()-L/2
odd=beta+1-2*s_norm_sq
even_zero_mean=beta+q(3,2)
assert 0<L<arb(2).log()
assert s_norm_sq>0
assert odd>q(1,125)
assert even_zero_mean>q(1,2)
print('Arb certified L=43/100, prime free:')
print('beta =',beta)
print('odd full Q lower =',odd,' > 1/125')
print('reflection-even mean-zero full Q lower =',even_zero_mean,' > 1/2')
print('PROVED via Legendre harmonic-spectrum of 1/|x-y| '
      'and gamma-jump comparison, for the respective parity subspaces '
      'on a length-43/100 interval. Not full all-test Q, not RH.')
