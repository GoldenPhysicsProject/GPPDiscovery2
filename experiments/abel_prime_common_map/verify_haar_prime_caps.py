"""Exact symbolic proof receipt for first-prime Haar polar-cap translations.

Polynomial identities only, using SymPy exact integration. The source Weil
identification and group-theoretic Haar statements require independent review.
"""
import sympy as s

h,u=s.symbols("h u",real=True)

def J(n,m):
    # Latitude shift alpha = 2-h in [-1,1]. Integrate the cap overlap.
    return s.factor(s.integrate(s.expand(
        s.legendre(n,1-u) * s.legendre(m,-1+h-u)),(u,0,h))/2)

checks={
 (0,0): h/2,
 (1,1): -h*(h*h-6*h+6)/12,
 (2,2): h*(3*h**4-30*h**3+100*h*h-120*h+40)/80,
 (0,2): h*(h-2)*(h-1)/4,
}
for (n,m),p in checks.items():
    assert s.simplify(J(n,m)-p)==0

# Exact Weyl parity identity on all first six class-one SO(3) reps.
for n in range(6):
    for m in range(6):
        assert s.simplify(J(m,n)-(-1)**(n+m)*J(n,m))==0
        if (n+m)%2:
            assert s.simplify(J(m,n)+J(n,m))==0
        else:
            assert s.simplify(J(m,n)-J(n,m))==0

# For 0<h<1, h²−6h+6 >= 1 (decreasing polynomial on [0,1]).
# Hence J11<0, whereas J00>0 for every first-prime-only width
# log2 < L < log3 < log4 = 2log2.
print("PASS exact prime cap polynomials, 36 parity relations")
print("J00 =",J(0,0))
print("J11 =",J(1,1))
print("J22 =",J(2,2))
print("Prime quadratic sign for low spin 0 is negative, for low spin 1 positive.")
print("No full Weil positivity inference.")
