"""Arb verification of exact mirror parity Loewner divided-difference structure.

The corrected exact semilocal Weil Q_mn has an integrable sine transform g(m).
For m != n Q_mn = (g(m)-g(n))/(pi*(n-m)), and g(-m)=-g(m).
Even and odd reflection blocks are rescaled Loewner divided differences
of H(t)=sqrt(t)*g(sqrt(t)) and J(t)=g(sqrt(t))/sqrt(t), plus a shared
diagonal d_m=Q_mm+g'(m)/pi. The diagonal d_m is NOT always positive.
"""
import os
from flint import acb,arb,ctx
from arb_semilocal_weil_matrix import entry, prime_powers, I

ctx.prec=int(os.environ.get("GPP_ARB_PREC_BITS","512"))
TOL=float(os.environ.get("GPP_ARB_TOL","1e-80"))
lam=arb(5)/2
L=2*lam.log()
LC=acb(L)
scale=2*arb.pi()/L
weights=[(arb(p).log()/arb(n).sqrt(),arb(n).log())
         for p,n in prime_powers(6)]

def ysmooth(z):
    # y*[2*cosh(y/2)-exp(y/2)/(2*sinh(y))], analytic at y=0
    ez=(z/2).exp()
    return z*(ez+(-z/2).exp())-ez/(2*(I*z).sinc())

def integrate(func):
    return acb.integral(lambda z, analytical: func(z),
                        acb(0),LC,rel_tol=TOL,abs_tol=TOL,
                        eval_limit=100000).real

def g(m):
    if m==0:return arb(0)
    w=scale*m
    val=integrate(lambda z:ysmooth(z)*w*(w*z).sinc())
    return val-sum((c*(w*a).sin() for c,a in weights),arb(0))

def gp(m):
    w=scale*m
    val=integrate(lambda z:ysmooth(z)*(w*z).cos())
    return scale*(val-sum((c*a*(w*a).cos() for c,a in weights),arb(0)))

for m,n in [(0,1),(1,2),(1,5),(2,8),(5,8),(-3,5),(-2,-4)]:
    assert m!=n
    actual=entry(m,n,lam,6)[0]
    predicted=(g(m)-g(n))/(arb.pi()*(n-m))
    assert abs(actual-predicted)<arb("1e-40"),(m,n,actual,predicted)
    print(f"PASS exact offdiag integrable-Loewner source at ({m},{n})")

for m,n in [(1,2),(2,8),(5,8)]:
    gm,gn=g(m),g(n)
    Qeven=entry(m,n,lam,6)[0]+entry(m,-n,lam,6)[0]
    Qodd=entry(m,n,lam,6)[0]-entry(m,-n,lam,6)[0]
    even_expr=2*(m*gm-n*gn)/(arb.pi()*(n*n-m*m))
    odd_expr=2*(n*gm-m*gn)/(arb.pi()*(n*n-m*m))
    assert abs(Qeven-even_expr)<arb("1e-40")
    assert abs(Qodd-odd_expr)<arb("1e-40")
    print(f"PASS mirror-even / odd Loewner formula at ({m},{n})")

for m in [0,1,4,5,8]:
    diagonal=entry(m,m,lam,6)[0]
    remainder=diagonal+gp(m)/arb.pi()
    if m in (5,8):assert remainder<0
    if m in (0,1,4):assert remainder>0
    print(f"CERTIFIED shared Loewner diagonal d_{m} = {remainder}")

print("No RH proof: the residual diagonal is SIGNED and operator monotonicity of the arithmetic Loewner symbols is unproved.")
