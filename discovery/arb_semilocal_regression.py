"""Regression against the defining completed Weil distribution.

The old Arb diagonal gamma code multiplied (cos(w z)-1)/z by exp(z/2).
That was algebraically wrong and artificially increased positive diagonals.
This check MUST reject the historical erroneous script.
"""
from flint import arb, acb, ctx
from arb_semilocal_weil_matrix import entry, arch_integrand, I
ctx.prec = 160

lam = arb(5)/2
L = 2*lam.log()
for m,n,expected in [
    (0,0,"0.039182293233144781752199"),
    (0,1,"0.039602951775226656461759"),
    (1,1,"0.040475527993136503621513"),
    (2,2,"0.045615136024502264858371")]:
    Q=entry(m,n,lam,6)[0]
    assert abs(Q-arb(expected)) < arb("1e-19"), (m,n,Q)

for y in ["0.1", "0.37", "1.1"]:
    z=acb(arb(y))
    w=2*arb.pi()/L
    c=(w*z).cos()
    ez=(z/2).exp()
    direct=(ez*(1-z/L)*c-1)/((I*z).sinc()*z)
    regularized=arch_integrand(1,1,z,acb(L))
    assert abs((direct-regularized).real) < arb("1e-25"), (y,direct,regularized)

print("PASS: corrected gamma diagonal matches exact Weil formula")
print("PASS: completed Q(5/2): m=0,1,2 independent high precision values")
print("Scope: tiny finite regression; no all-mode or RH conclusion")
