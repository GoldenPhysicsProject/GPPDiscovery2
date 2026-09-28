#!/usr/bin/env python3
"""Finite Weil vacuum test against the explicit Riemann Phi profile.

Zero data are NOT used.  For each (c,N), build the truncated Weil matrix from
connes-cvs, project Riemann's explicit Phi kernel onto the same Fourier basis,
and measure:

  * Rayleigh excess above the even ground;
  * residual norm ||(Q-Rayleigh) v_Phi||;
  * even-sector gap;
  * direct overlap with the true even ground.

This is the quantitative object needed by
research/2026-09-28_quantitative_spectral_triple_closure_gap.md.

The candidate is the direct truncated Riemann Phi, not the more refined
prolate k_lambda, so failure would not kill the prolate route.
"""

from __future__ import annotations
import argparse, json, math, time
import mpmath as mp
import connes_cvs as cc


def riemann_phi_pos(y: mp.mpf, terms: int = 16) -> mp.mpf:
    """Standard positive-y Riemann Xi Fourier kernel; extend evenly."""
    y = abs(y)
    e2 = mp.e ** (2*y)
    e52 = mp.e ** (mp.mpf("2.5")*y)
    e92 = mp.e ** (mp.mpf("4.5")*y)
    s = mp.mpf("0")
    for n in range(1, terms + 1):
        n2 = mp.mpf(n*n)
        s += (2*mp.pi**2*n2**2*e92 - 3*mp.pi*n2*e52) * mp.e**(-mp.pi*n2*e2)
    return s


def sector_matrix(Q, parity: str):
    DIM = Q.rows
    N = (DIM - 1)//2
    invsqrt2 = 1/mp.sqrt(2)
    if parity == "even":
        V = mp.matrix(DIM, N+1)
        V[N,0] = 1
        for k in range(1,N+1):
            V[N+k,k] = invsqrt2
            V[N-k,k] = invsqrt2
    else:
        V = mp.matrix(DIM, N)
        for k in range(1,N+1):
            V[N+k,k-1] = invsqrt2
            V[N-k,k-1] = -invsqrt2
    return V, V.T*Q*V


def phi_fourier_vector(c: int, N: int, terms: int = 16):
    """Coefficients in U_k(x)=L^-1/2 exp(2 pi i k x/L), x in [0,L]."""
    L = mp.log(c)             # c=lambda^2, so L=2 log lambda
    A = L/2
    coeff = [mp.mpf("0")]*(2*N+1)
    for k in range(0,N+1):
        omega = 2*mp.pi*k/L
        integ = 2*mp.quad(lambda y: riemann_phi_pos(y,terms)*mp.cos(omega*y), [0,A])
        ak = ((-1)**k) * integ/mp.sqrt(L)
        coeff[N+k] = ak
        coeff[N-k] = ak
    v = mp.matrix(coeff)
    norm = mp.sqrt((v.T*v)[0])
    return v/norm


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--c",type=int,required=True)
    p.add_argument("--N",type=int,default=28)
    p.add_argument("--T",type=int,default=300)
    p.add_argument("--dps",type=int,default=70)
    p.add_argument("--terms",type=int,default=16)
    p.add_argument("--out",default="result.json")
    a=p.parse_args()
    mp.mp.dps=a.dps
    t0=time.time()

    Q=cc.build_galerkin_matrix(a.c,N=a.N,T=a.T,dps=a.dps)
    Ve,Qe=sector_matrix(Q,"even")
    eig, U=mp.eigsy(Qe)
    l1,l2=eig[0],eig[1]
    gap=l2-l1

    vp=phi_fourier_vector(a.c,a.N,a.terms)
    # Phi projection is even; move into orthonormal even coordinates.
    ve=Ve.T*vp
    ve=ve/mp.sqrt((ve.T*ve)[0])

    ray=(ve.T*Qe*ve)[0]
    resvec=Qe*ve-ray*ve
    res=mp.sqrt((resvec.T*resvec)[0])
    ground=U[:,0]
    ov=abs((ground.T*ve)[0])
    angle_def=1-ov**2

    # Davis-Kahan denominator using distance from trial Rayleigh to next even level.
    dist2=abs(l2-ray)
    dk = res/dist2 if dist2 != 0 else mp.inf
    rex=ray-l1
    ray_bound=rex/gap if gap != 0 else mp.inf

    rec=dict(
        c=a.c,N=a.N,T=a.T,dps=a.dps,terms=a.terms,L=float(mp.log(a.c)),
        lam1=mp.nstr(l1,30),lam2=mp.nstr(l2,30),gap=mp.nstr(gap,30),
        phi_rayleigh=mp.nstr(ray,30),
        rayleigh_excess=mp.nstr(rex,30),
        residual_norm=mp.nstr(res,30),
        overlap=mp.nstr(ov,30),
        one_minus_overlap_sq=mp.nstr(angle_def,30),
        rayleigh_excess_over_gap=mp.nstr(ray_bound,30),
        residual_over_dist2=mp.nstr(dk,30),
        seconds=round(time.time()-t0,1),
        uses_zero_data=False,
    )
    open(a.out,"w").write(json.dumps(rec))
    print(json.dumps(rec),flush=True)


if __name__=="__main__":
    main()
