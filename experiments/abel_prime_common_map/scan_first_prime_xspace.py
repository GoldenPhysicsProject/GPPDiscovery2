"""Actual first-prime Weil form: independent REAL-SPACE sine Galerkin scan.

Numerical diagnostics only (not interval-certified, not RH).
Uses an exact analytic sine-translation overlap formula and analytic
archimedean tail, rather than Fourier-frequency truncation.
Requires numpy, scipy, mpmath. Recompute at 150/300/600 Gauss nodes.
"""
import numpy as np
from scipy.special import roots_legendre
from scipy.linalg import null_space
import mpmath as mp

L = .72
N = 48
ell = np.log(2.)
v = ell / np.sqrt(2.)
a = np.arange(1, N+1, dtype=float)*np.pi/L
idx = np.arange(1,N+1)
AI, AJ = a[:,None], a[None,:]
sign = (-1.)**(idx[:,None]+idx[None,:])
eye = np.eye(N, dtype=bool)
den = AI - AJ
den[eye] = 1

def autocorr_sine(t):
    """Symmetrized mixed autocorrelation, 0 <= t <= L."""
    if t >= L:
        return np.zeros((N,N))
    si = np.sin(a*t)
    raw = ((sign*si[None,:]-si[:,None])/den
           +(sign*si[None,:]+si[:,None])/(AI+AJ))/L
    raw[eye] = ((L-t)/L)*np.cos(a*t)+np.sin(a*t)/(a*L)
    return (raw+raw.T)/2

def arch_weight(t):
    return np.exp(-t/2)/(-np.expm1(-2*t))

def scan(nquad):
    t, wt = roots_legendre(nquad)
    t = L*(t+1)/2
    wt = L*wt/2
    E = np.zeros((N,N))
    identity = np.eye(N)
    for ti, wi in zip(t,wt):
        E += 2*wi*arch_weight(ti)*(identity-autocorr_sine(ti))
    mp.mp.dps = 40
    z = mp.exp(-mp.mpf(str(L))/2)
    tail = float(mp.log((1+z)/(1-z)) + 2*mp.atan(z))
    E += tail*identity
    Cinf = -float(mp.euler)-np.log(np.pi)-np.pi/2-3*ell
    # Exact pointwise n=2 prime overlap, symmetrized in test indices.
    prime = 2*v*autocorr_sine(ell)
    x, wx = roots_legendre(400)
    x, wx = x*L/2, wx*L/2
    F = np.sqrt(2/L)*np.sin((x[:,None]+L/2)*a[None,:])
    C = np.einsum('x,x,xi->i',wx,np.cosh(x/2),F)
    S = np.einsum('x,x,xi->i',wx,np.sinh(x/2),F)
    W = E + Cinf*identity + 2*np.outer(C,C)-2*np.outer(S,S)-prime
    moments=np.stack([np.einsum('x,x,xi->i',wx,x**j,F) for j in range(6)])
    return W,E,moments

if __name__ == "__main__":
    for nquad in (150,300,600):
        W,E,moments=scan(nquad)
        print("quadrature",nquad, "first Ritz W eigenvalues",
              np.linalg.eigvalsh(W)[:3], "first Ritz E eigenvalues",
              np.linalg.eigvalsh(E)[:4])
        for m in range(6):
            Z=null_space(moments[:m,:]) if m else np.eye(N)
            print("  moment count",m, "smallest W Ritz",
                  np.linalg.eigvalsh(Z.T@W@Z)[0])
        # This is not an infinite-tail certificate. A stable finite
        # Galerkin eigenvalue is NOT a theorem of full positivity.
