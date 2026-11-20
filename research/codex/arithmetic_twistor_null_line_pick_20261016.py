#!/usr/bin/env python3
"""Arithmetic twistor line, shadow quotient, and Pick falsifier.

Exact geometric equalities use SymPy. Numerical log-derivative/Pick tests
use mpmath and NumPy, and are NOT an RH proof or interval certificates.
See private GPP-bridge:
work/codex/2026-10-16_arithmetic_twistor_null_line_shadow_quotient_signed_pick_kernel.md
"""
import sympy as S
import mpmath as mp
import numpy as np

def exact_twistor_check():
    w = S.symbols("w", complex=True)
    sx, sz = S.Matrix([[0, 1], [1, 0]]), S.diag(1, -1)
    pi = S.Matrix([1, w])
    omega = sz * pi / 2
    H = S.simplify((S.conjugate(omega).T * pi +
                    S.conjugate(pi).T * omega)[0])
    Jpi, Jomega = sx * S.conjugate(pi), -sx * S.conjugate(omega)
    HJ = S.simplify((S.conjugate(Jomega).T * Jpi +
                     S.conjugate(Jpi).T * Jomega)[0])
    assert S.simplify(H - (1 - w*S.conjugate(w))) == 0
    assert S.simplify(HJ + H) == 0
    assert S.simplify(Jomega - sz*Jpi/2) == S.zeros(2, 1)
    z = (1+w)/(2*(1-w))
    u = z*z
    assert S.simplify(z.subs(w,1/w) + z) == 0
    assert S.simplify(u.subs(w,1/w) - u) == 0
    T,X,Y,Z = S.symbols("T X Y Z",real=True)
    x = S.Matrix([[T+Z,X-S.I*Y],[X+S.I*Y,T-Z]])
    xr = sx*S.conjugate(x)*sx
    assert S.simplify(xr-S.Matrix([[T-Z,X-S.I*Y],
                                   [X+S.I*Y,T+Z]])) == S.zeros(2)
    xc = -S.I*sz/2
    assert S.simplify(sx*S.conjugate(xc)*sx-xc) == S.zeros(2)
    print("PASS exact: SU(2,2) norm, anti-isometry, incidence, reflection, shadow quotient")

def xi(s):
    return s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)/2

def m(u, theta=0):
    z=mp.sqrt(u)
    if theta==0:
        s=mp.mpf("0.5")+z
        return mp.diff(xi,s)/(2*z*xi(s))
    a=mp.mpf("0.5")+z-theta
    b=mp.mpf("0.5")+z+theta
    return (mp.diff(xi,a)/xi(a)+mp.diff(xi,b)/xi(b))/(2*z)

def check_pick():
    mp.mp.dps=65
    samples=[mp.mpc(1,1),mp.mpc(2,3),mp.mpc(4,2)]
    K=np.array([[complex((mp.conj(m(v))-m(u))/(u-mp.conj(v)))
                 for v in samples] for u in samples])
    assert np.max(np.abs(K-K.conj().T))<1e-12
    print("Zeta finite-sample Pick eigenvalues (NUMERICAL ONLY):",np.linalg.eigvalsh(K))
    theta=mp.mpf("0.2")
    gamma=mp.im(mp.zetazero(1))
    u0=(theta+1j*gamma)**2
    u=u0-mp.mpc(0,"0.001")
    print("Shifted fake: upper-plane Im(u) =", mp.nstr(mp.im(u),16))
    print("Im m_fake(u) =", mp.nstr(mp.im(m(u,theta)),25))
    print("Im m_zeta(u) =", mp.nstr(mp.im(m(u)),25))
    assert mp.im(u)>0 and mp.im(m(u,theta))>100 and mp.im(m(u))<0
    print("PASS: shifted-xi fake violates anti-Herglotz, as analytic pole argument predicts")

if __name__=="__main__":
    exact_twistor_check()
    check_pick()
