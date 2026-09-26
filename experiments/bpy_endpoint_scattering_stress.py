#!/usr/bin/env python3
"""
BPY endpoint / scattering stress tests.

Tests:
  A. odd endpoint kernel K_0^- for Riemann Phi versus generic positive/log-concave controls;
  B. shifted scattering family S_a(z)=F(z-a)/F(z+a);
  C. naive Loewner-flow generator p_a(z)=K'(z-a)+K'(z+a).

Diagnostic only; no RH claim.
"""
import math
import numpy as np
from scipy.integrate import quad
import mpmath as mp

mp.mp.dps = 50

def phi(x):
    x = abs(float(x))
    if x > 4:
        return 0.0
    e2 = math.exp(2*x)
    s = 0.0
    for n in range(1, 30):
        expo = -math.pi*n*n*e2
        if expo < -745:
            break
        term = (
            4*math.pi**2*n**4*math.exp(4.5*x)
            - 6*math.pi*n**2*math.exp(2.5*x)
        )*math.exp(expo)
        s += term
        if n > 5 and abs(term) < 1e-18*max(1.0, abs(s)):
            break
    return s

def kminus(F, a, b, T=6.0):
    M, r = max(a,b), min(a,b)
    f1 = lambda t: 0.25*(a+b+2*t)*F(a+t)*F(b+t)
    f2 = lambda t: 0.25*(abs(a-b)+2*t)*F(M+t)*F(abs(r-t))
    return (
        quad(f1, 0, T, epsabs=1e-12, epsrel=1e-10, limit=300)[0]
        - quad(f2, 0, T, epsabs=1e-12, epsrel=1e-10, limit=300)[0]
    )

def xi(s):
    s = mp.mpc(s)
    return mp.mpf("0.5")*s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)

XI0 = xi(mp.mpf("0.5"))

def F(z):
    return xi(mp.mpf("0.5")+z)/XI0

def Kprime(z):
    return mp.diff(lambda zz: mp.log(F(zz)), z)

def S(a,z):
    return F(z-a)/F(z+a)

def generator(a,z):
    # -d_a log S_a
    return Kprime(z-a)+Kprime(z+a)

if __name__ == "__main__":
    pts = np.linspace(0.05, 1.0, 10)
    controls = {
        "Riemann Phi": phi,
        "Gaussian": lambda x: math.exp(-x*x),
        "quartic": lambda x: math.exp(-x**4),
        "pure exponential": lambda x: math.exp(-x),
        "superexponential": lambda x: math.exp(-math.exp(2*x)) if x < 4 else 0.0,
    }
    print("Odd endpoint kernel eigenvalue audit")
    for name, fun in controls.items():
        K = np.array([[kminus(fun,float(a),float(b)) for b in pts] for a in pts])
        ev = np.linalg.eigvalsh((K+K.T)/2)
        print(name, "min=", ev[0], "max=", ev[-1])

    print("\nShifted scattering family")
    for a in [0.05,0.1,0.2,0.3,0.45]:
        maxmod = 0.0
        argmax = None
        mingen = 1e100
        argmin = None
        for x in [0.01,0.03,0.1,0.3,0.7,1.5]:
            for y in np.linspace(0,30,61):
                z = mp.mpc(x,float(y))
                smod = float(abs(S(mp.mpf(a),z)))
                if smod > maxmod:
                    maxmod, argmax = smod, (x,float(y))
                gp = float(mp.re(generator(mp.mpf(a),z)))
                if gp < mingen:
                    mingen, argmin = gp, (x,float(y))
        print(
            f"a={a}: sampled max |S_a|={maxmod:.12g} at {argmax}; "
            f"min Re(-d_a log S_a)={mingen:.12g} at {argmin}"
        )
