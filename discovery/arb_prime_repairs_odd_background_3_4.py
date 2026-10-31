#!/usr/bin/env python3
"""Outward Arb certificate: prime-omitted completed Weil background is
INDEFINITE at L=3/4, while actual p=2 term repairs this specific test.

The explicit smooth polynomial f = e1 - (2/5)e3 uses normalized shifted
Legendre e1, e3 on [0,L] (zero outside). The boundary zero extension is
in the finite logarithmic form domain; smooth compactly supported cores
approximate it in that domain. Not a global RH proof.
"""
from flint import arb, acb, ctx, fmpq
ctx.prec=256
qrat=lambda a,b=1:arb(fmpq(a,b))
I=acb(0,1)
L=qrat(3,4)
a=arb(2).log()
rt=arb(21).sqrt()
norm=qrat(29,25)
c=[
    qrat(58,25),
    -qrat(206,25)+8*rt/5,
    -8*rt,
    qrat(324,25)+48*rt/5,
    qrat(0),
    -qrat(336,25)-16*rt/5,
    qrat(0),
    qrat(32,5),
]
assert c[0]==2*norm
TOL=1e-57
def qpoly(z):
    t=z/L
    s=acb(0)
    for v in c[::-1]:
        s=s*t+v
    return s

def kinetic_integrand(z):
    # q(0)-q(y) is divisible by y, so the singularity is REMOVED:
    # (q(0)-q(y))/(2 sinh y) =
    # -(sum_{k>=1} c_k (y/L)^(k-1))/(2 L sinh(y)/y)
    t=z/L
    s=acb(0)
    for v in c[:0:-1]:
        s=s*t+v
    return -s/(2*L*(I*z).sinc())

def tilt_integrand(z):
    # (e^(y/2)-1)/(2sinh(y)) = 1F1(1;2;y/2)/(4*sinh(y)/y)
    return qpoly(z)*(z/2).hypgeom_1f1(1,2)/(4*(I*z).sinc())

def integrate(f):
    val=acb.integral(lambda z,analytical:f(z),
                     acb(0),acb(L),rel_tol=TOL,abs_tol=TOL,
                     eval_limit=100000)
    return val.real
E=integrate(kinetic_integrand)-norm*(L/2).tanh().log()
P=integrate(lambda z:qpoly(z)*((z/2).exp()+(-z/2).exp()))
A=integrate(tilt_integrand)
c_infty=(4*arb.pi()).log()+arb.const_euler()
Q0=E+P-c_infty*norm-A
q_at_a=qpoly(acb(a)).real
S2=a/arb(2).sqrt()*q_at_a
Q=Q0-S2
print('L=3/4, f=e1-(2/5)e3, ||f||^2=29/25')
print('E gamma kinetic=',E)
print('P exact rank-two pole=',P)
print('A gamma tilt=',A)
print('Q0 prime-omitted COMPLETE Weil background=',Q0)
print('q_f(log2)=',q_at_a)
print('S2 actual first prime source=',S2)
print('Q=Q0-S2, actual first-prime completed form=',Q)
assert a<L and L<arb(3).log()
assert Q0 < -qrat(9,1000)
assert S2 < -qrat(67,1000)
assert Q > qrat(57,1000)
print('CERTIFIED: Q0[f]<-0.009 but Q[f]>0.057 on the SAME test.')
print('Scope: one explicit form-domain test, not an all-f sign or RH proof.')
