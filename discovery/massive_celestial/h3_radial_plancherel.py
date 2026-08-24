#!/usr/bin/env python3
"""
Radial H^3 spherical transform normalization from ordinary sine inversion.

With
    phi_lam(r) = sin(lam*r)/(lam*sinh r),
    F(lam) = 4*pi * int_0^inf f(r) phi_lam(r) sinh(r)^2 dr,
put u(r)=sinh(r) f(r). Then
    F(lam) = (4*pi/lam) * int_0^inf u(r) sin(lam*r) dr.
Ordinary half-line sine inversion yields
    f(r) = (1/(2*pi^2)) * int_0^inf lam^2 F(lam) phi_lam(r) dlam.
Thus the positive-lambda radial H^3 Plancherel density is
    lam^2/(2*pi^2) dlam.
If both spectral signs are retained, this is equivalently
    lam^2/(4*pi^2) dlam on R.

Closed test:
    f(r)=r*exp(-r)/sinh(r), u(r)=r exp(-r)
    int u(r) sin(lam r) dr = 2 lam/(1+lam^2)^2
    F(lam)=8*pi/(1+lam^2)^2.
The inverse uses
    int_0^inf lam sin(lam r)/(1+lam^2)^2 dlam = pi*r*exp(-r)/4.
The numerical test below uses oscillatory quadrature and agrees to working precision.
"""
import mpmath as mp

mp.mp.dps = 50


def phi(lam, r):
    if lam == 0:
        return r/mp.sinh(r)
    return mp.sin(lam*r)/(lam*mp.sinh(r))


def f_exact(r):
    return r*mp.e**(-r)/mp.sinh(r)


def F_exact(lam):
    return 8*mp.pi/(1+lam*lam)**2


for r in [mp.mpf('0.4'), mp.mpf('1.1'), mp.mpf('2.3')]:
    integrand = lambda lam: (lam**2/(2*mp.pi**2))*F_exact(lam)*phi(lam, r)
    inv = mp.quadosc(integrand, [0, mp.inf], zeros=lambda n: n*mp.pi/r)
    err = abs(inv-f_exact(r))
    assert err < mp.mpf('1e-40')

print('PASS: radial H3 inversion density = lambda^2/(2*pi^2) on lambda>0')
print('PASS: explicit f(r)=r*e^-r/sinh(r) reconstructed to >40 digits')
