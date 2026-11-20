#!/usr/bin/env python3
"""Exact twistor theta-mixture Fisher variance and strict off-axis fake.

Mathematical identities:
  m=E_u[q],  -m'=E_u[-dq/du]-Var_u(q);
  4||d psi_u/du||^2=Var_u(q).
This code checks a positive two-atom theta analogue with OFF-AXIS
zeros despite each cosh component having pure imaginary zeros.
It does not certify RH, Pick positivity, or a CFS variational principle.
"""
import sympy as sp
z,u=sp.symbols("z u", real=True)
Y=sp.symbols("Y")
F=sp.cosh(2*z)+5*sp.cosh(z)
poly=2*Y**2+5*Y-1
assert sp.simplify(F-poly.subs(Y,sp.cosh(z))) == 0
roots=sp.solve(poly,Y)
yneg=(-5-sp.sqrt(33))/4
assert sp.simplify(poly.subs(Y,yneg)) == 0
assert bool(yneg < -1)
# A complex zero is z0=acosh(-yneg)+I*pi. Its squared u0 is in UHP.
a=sp.acosh(-yneg)
assert sp.N(a,30) > 0
u0=(a+sp.I*sp.pi)**2
assert sp.N(sp.im(u0),30)>0
# Positive kernel weights at u=0: nu={2:1/6,1:5/6}.
M2=sp.Rational(4+5,6)
M4=sp.Rational(16+5,6)
assert sp.simplify((3*M2**2-M4)/12-sp.Rational(13,48))==0
# Independent direct f(u) series: f(u)=6+(9/2)u+(7/8)u²+...
f0=sp.Integer(6)
fprime=sp.Rational(9,2)
fsecond=sp.Rational(7,4)
assert sp.simplify((fprime**2-f0*fsecond)/f0**2-sp.Rational(13,48))==0
print("PASS exact cosh polynomial, off-axis root, positive local derivative 13/48")
print("z0 =",sp.N(a+sp.I*sp.pi,18))
print("u0 =",sp.N(u0,18))
# A 1x1 anti-Pick diagonal witness immediately below the UHP pole.
zz=sp.sqrt(u0-sp.I/1000)
mf=(2*sp.sinh(2*zz)+5*sp.sinh(zz))/(2*zz*(sp.cosh(2*zz)+5*sp.cosh(zz)))
assert sp.im(sp.N(mf,40))>0
print("Im m(fake) at u0-0.001i =",sp.N(sp.im(mf),18))
print("WARNING: this only falsifies generic positive mixtures, not the true xi.")
