#!/usr/bin/env python3
"""
Exact radial H^3 reduction for the equal-mass celestial cut.

For the H^3 zonal spherical function
    phi_lam(eta) = sin(lam*eta)/(lam*sinh eta),
verify symbolically that
    phi'' + 2*coth(eta)*phi' + (1+lam^2)*phi = 0.

Equivalently, under u(eta)=sinh(eta) f(eta), the radial Laplacian
    Delta_rad f = f'' + 2*coth(eta) f'
conjugates to
    sinh(eta) * (Delta_rad + 1) f = u''.
Thus the radial spectral equation (Delta_rad + 1 + lam^2)f=0
is exactly the ordinary half-line Helmholtz equation u''+lam^2 u=0.

This is the practical harmonic-analysis reduction needed for the massive
D-dimensional unitarity/rational-amplitude track. It does NOT claim that
the full non-radial H^3 transform or its celestial sewing kernel has been
completed.
"""
import sympy as sp

eta, lam = sp.symbols('eta lam', positive=True, real=True)
phi = sp.sin(lam*eta)/(lam*sp.sinh(eta))
radial_eq = sp.simplify(sp.diff(phi, eta, 2) + 2*sp.coth(eta)*sp.diff(phi, eta) + (1+lam**2)*phi)
assert radial_eq == 0

u = sp.Function('u')(eta)
f = u/sp.sinh(eta)
conjugation = sp.simplify(sp.sinh(eta)*(sp.diff(f, eta, 2) + 2*sp.coth(eta)*sp.diff(f, eta) + f) - sp.diff(u, eta, 2))
assert conjugation == 0

u_lam = sp.sin(lam*eta)/lam
helmholtz = sp.simplify(sp.diff(u_lam, eta, 2) + lam**2*u_lam)
assert helmholtz == 0

print('PASS: H3 zonal spherical function solves radial eigenvalue equation')
print('PASS: sinh(eta) conjugates (Delta_rad + 1) to d^2/deta^2')
print('PASS: massive radial H3 spectral problem reduces to ordinary sine/Helmholtz transform')
