#!/usr/bin/env python3
"""Independent exact symbolic audit of Legendre q_f used by Arb certificates.

This test derives the autocorrelation by polynomial integration from e1,e3
rather than trusting the hardcoded degree-seven coefficients.
"""
import sympy as s
u,t=s.symbols('u t',real=True)
p1=lambda z:2*z-1
p3=lambda z:(5*(2*z-1)**3-3*(2*z-1))/2
f=lambda z:s.sqrt(3)*p1(z)-s.Rational(2,5)*s.sqrt(7)*p3(z)
q=s.expand(2*s.integrate(s.expand(f(u)*f(u+t)),(u,0,1-t)))
expected=(
    s.Rational(58,25)
    +(-s.Rational(206,25)+8*s.sqrt(21)/5)*t
    -8*s.sqrt(21)*t**2
    +(s.Rational(324,25)+48*s.sqrt(21)/5)*t**3
    -(s.Rational(336,25)+16*s.sqrt(21)/5)*t**5
    +s.Rational(32,5)*t**7
)
assert s.simplify(q-expected)==0
assert s.simplify(q.subs(t,0)-s.Rational(58,25))==0
assert s.simplify(q.subs(t,1))==0
norm=s.simplify(s.integrate(s.expand(f(u)**2),(u,0,1)))
assert norm==s.Rational(29,25)
print('PASS: exact 2-mode Legendre autocorrelation polynomial, norm, endpoint')
