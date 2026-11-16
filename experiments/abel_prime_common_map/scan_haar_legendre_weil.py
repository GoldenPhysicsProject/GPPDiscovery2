"""Haar/Peter-Weyl real-space Galerkin scan of the ACTUAL first-prime Weil form.

Uses a finite orthonormal Legendre basis on I_L, exact prime-2 shift of the
support and the archimedean real-space positive energy. No zeta zeros and no
assumed positivity. Numerical quadrature and finite Ritz spectra are NOT
a certificate of nonnegative Weil form on the whole test space.

Requires numpy, scipy.special, mpmath. Run:
python experiments/abel_prime_common_map/scan_haar_legendre_weil.py
"""
import numpy as np
import mpmath as mp
from scipy.special import eval_legendre, roots_legendre

L = 18 / 25
ELL = np.log(2.0)
V = ELL / np.sqrt(2.0)
CINF = -float(mp.euler) - np.log(np.pi) - np.pi/2 - 3*ELL

def matrices(n=30, nshift=250, nx=90):
    ks = np.arange(n)
    norms = np.sqrt((2*ks+1)/L)
    xnode, xweight = roots_legendre(nx)
    tnode, tweight = roots_legendre(nshift)
    tnode = L*(tnode+1)/2
    tweight = L*tweight/2

    def basis(x):
        return np.stack([norms[j]*eval_legendre(j,2*x/L) for j in range(n)], axis=-1)

    Id = np.eye(n)
    energy = np.zeros((n,n))
    for t, dt in zip(tnode,tweight):
        x = t/2 + (L-t)*xnode/2
        dx = (L-t)*xweight/2
        P, Q = basis(x),basis(x-t)
        corr = (P*dx[:,None]).T@Q
        corr = (corr+corr.T)/2
        weight = np.exp(-t/2)/(-np.expm1(-2*t))
        energy += 2*dt*weight*(Id-corr)
    mp.mp.dps=35
    z=mp.exp(-mp.mpf(str(L))/2)
    tail=float(mp.log((1+z)/(1-z))+2*mp.atan(z))
    energy += tail*Id

    x=L*xnode/2
    P=basis(x)
    C=np.sum(P*(L*xweight*np.cosh(x/2)/2)[:,None],axis=0)
    S=np.sum(P*(L*xweight*np.sinh(x/2)/2)[:,None],axis=0)

    # Exact support geometry: for shift ell, x in [-L/2+ell,L/2].
    x=ELL/2 + (L-ELL)*xnode/2
    dx=(L-ELL)*xweight/2
    P,Q=basis(x),basis(x-ELL)
    corr=(P*dx[:,None]).T@Q
    corr=(corr+corr.T)/2
    W=energy+CINF*Id+2*np.outer(C,C)-2*np.outer(S,S)-2*V*corr
    return (W+W.T)/2,energy,corr

if __name__ == "__main__":
    print("latitude shift alpha",2*ELL/L)
    print("Haar fraction of each coupled polar cap",1-ELL/L)
    for n,nt in [(16,200),(30,250),(50,350)]:
        W,E,prime=matrices(n,nt,110)
        ev=np.linalg.eigvalsh(W)
        even=np.linalg.eigvalsh(W[0::2,0::2])
        odd=np.linalg.eigvalsh(W[1::2,1::2])
        low=W[:5,:5]
        high=W[5:,5:]
        B=W[5:,:5]
        RitzSchur=low-B.T@np.linalg.solve(high,B)
        print("n",n,"min Ritz",ev[0],"even",even[0],"odd",odd[0],
              "min *truncated* Schur eigenvalue",
              np.linalg.eigvalsh(RitzSchur)[0])
        print("   prime corr normalized (0,0)/(1,1):",
              prime[0,0],prime[1,1])
    print("WARNING: finite Schur contains truncated high block only,")
    print("not certified full residual. This does not establish RH/ARP.")
