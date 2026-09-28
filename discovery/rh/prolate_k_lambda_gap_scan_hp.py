#!/usr/bin/env python3
"""High-precision literal CCM prolate k_lambda vacuum-gap diagnostic.

Key improvements over the first prototype:
1. prolate eigenvectors are computed with mpmath eigsy in an orthonormal
   Legendre-Galerkin basis;
2. Fourier coefficients of k_lambda=E(h_lambda) are computed by an exact
   finite Mellin/Dirichlet-polynomial formula, with no y-quadrature and no
   double-precision conversion.

For h(x)=sum_q d_q x^q supported on [-lambda,lambda], A=log(lambda),
omega=2*pi*k/(2A), and c=lambda^2 an integer,

 I(omega) = int_{-A}^A k_lambda(e^y)e^{-i omega y}dy
          = sum_q d_q/a_q [
                lambda^(a_q) S_c(omega)
              - lambda^(-a_q) P_q(c)
            ],

 a_q=q+1/2-i omega,
 S_c(omega)=sum_{n<=c} n^(-1/2+i omega),
 P_q(c)=sum_{n<=c} n^q.

The even CCM Fourier coefficient is (-1)^k Re I / sqrt(2A).

No Riemann-zero data are used.
"""

from __future__ import annotations

import argparse, json, time
import mpmath as mp
import connes_cvs as cc


def sector_matrix(Q, parity: str):
    dim = Q.rows
    N = (dim - 1) // 2
    invsqrt2 = 1 / mp.sqrt(2)
    if parity == "even":
        V = mp.matrix(dim, N + 1)
        V[N, 0] = 1
        for k in range(1, N + 1):
            V[N + k, k] = invsqrt2
            V[N - k, k] = invsqrt2
    else:
        V = mp.matrix(dim, N)
        for k in range(1, N + 1):
            V[N + k, k - 1] = invsqrt2
            V[N - k, k - 1] = -invsqrt2
    return V, V.T * Q * V


def acoef(l):
    l=mp.mpf(l)
    return (l+1)/mp.sqrt((2*l+1)*(2*l+3))


def bcoef(l):
    if l == 0:
        return mp.mpf("0")
    l=mp.mpf(l)
    return l/mp.sqrt((2*l-1)*(2*l+1))


def legendre_polys(lmax):
    """Standard P_l coefficients in ascending powers, mpmath."""
    P=[[mp.mpf(1)]]
    if lmax == 0:
        return P
    P.append([mp.mpf(0),mp.mpf(1)])
    for l in range(1,lmax):
        # P_{l+1}=((2l+1)xP_l-lP_{l-1})/(l+1)
        a=[mp.mpf(0)]*(len(P[l])+1)
        for j,c in enumerate(P[l]):
            a[j+1] += (2*l+1)*c/(l+1)
        for j,c in enumerate(P[l-1]):
            a[j] -= l*c/(l+1)
        P.append(a)
    return P


def prolate_power_coeffs(c_int:int,lmax:int):
    """Return power coefficients d_q of normalized zero-integral h_lambda."""
    if lmax % 2:
        lmax += 1
    lam=mp.sqrt(c_int)
    gamma=2*mp.pi*lam*lam
    ls=list(range(0,lmax+1,2))
    m=len(ls)
    T=mp.matrix(m)
    for i,l in enumerate(ls):
        T[i,i]=mp.mpf(l*(l+1))+gamma**2*(acoef(l)**2+bcoef(l)**2)
        if i+1<m:
            off=gamma**2*acoef(l)*acoef(l+1)
            T[i,i+1]=off
            T[i+1,i]=off
    evals,evecs=mp.eigsy(T)
    v0=evecs[:,0]
    v4=evecs[:,2]

    # orientation from value at z=0
    P=legendre_polys(lmax)
    def val0(v):
        s=mp.mpf("0")
        for i,l in enumerate(ls):
            s += v[i]*mp.sqrt((2*l+1)/2)*P[l][0]
        return s
    if val0(v0)<0:
        v0=-v0
    if val0(v4)<0:
        v4=-v4

    comb=v4[0]*v0-v0[0]*v4
    comb/=mp.sqrt(sum(comb[i]**2 for i in range(m)))

    d=[mp.mpf("0")]*(lmax+1)
    for i,l in enumerate(ls):
        scale=comb[i]*mp.sqrt((2*l+1)/2)/mp.sqrt(lam)
        for q,pq in enumerate(P[l]):
            if pq:
                d[q]+=scale*pq/(lam**q)

    integ=sum(d[q]*(lam**(q+1)-(-lam)**(q+1))/(q+1) for q in range(len(d)))
    return d,evals,integ


def exact_even_fourier_vector(c_int:int,N:int,lmax:int):
    lam=mp.sqrt(c_int)
    L=mp.log(c_int)
    d,peigs,hinteg=prolate_power_coeffs(c_int,lmax)

    # power sums used by every Fourier mode
    pows=[]
    for q in range(len(d)):
        if abs(d[q]) > mp.mpf(10)**(-mp.mp.dps+20):
            pows.append(sum(mp.mpf(n)**q for n in range(1,c_int+1)))
        else:
            pows.append(mp.mpf("0"))

    coeff=[mp.mpf("0")]*(2*N+1)
    raw_complex={}
    for k in range(0,N+1):
        omega=2*mp.pi*k/L
        S=sum(mp.power(n,-mp.mpf("0.5")+1j*omega) for n in range(1,c_int+1))
        I=0
        for q,dq in enumerate(d):
            if dq == 0:
                continue
            aq=mp.mpf(q)+mp.mpf("0.5")-1j*omega
            I += dq/aq * (mp.power(lam,aq)*S-mp.power(lam,-aq)*pows[q])
        ak=(-1 if k%2 else 1)*mp.re(I)/mp.sqrt(L)
        coeff[N+k]=ak
        coeff[N-k]=ak
        raw_complex[k]=I/mp.sqrt(L)

    v=mp.matrix(coeff)
    norm=mp.sqrt((v.T*v)[0])
    v/=norm

    # Fourier-basis odd leakage estimate from imaginary coefficients.
    even_energy=abs(mp.re(raw_complex[0]))**2
    odd_energy=mp.mpf("0")
    for k in range(1,N+1):
        even_energy += 2*abs(mp.re(raw_complex[k]))**2
        odd_energy += 2*abs(mp.im(raw_complex[k]))**2
    odd_frac=odd_energy/(even_energy+odd_energy) if even_energy+odd_energy else mp.nan

    diag={
        "lambda":mp.nstr(lam,40),
        "prolate_gamma":mp.nstr(2*mp.pi*lam*lam,40),
        "prolate_eig0":mp.nstr(peigs[0],50),
        "prolate_eig4":mp.nstr(peigs[2],50),
        "h_integral":mp.nstr(hinteg,50),
        "fourier_odd_fraction":mp.nstr(odd_frac,50),
    }
    return v,diag


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--c",type=int,required=True)
    ap.add_argument("--N",type=int,default=28)
    ap.add_argument("--T",type=int,default=300)
    ap.add_argument("--dps",type=int,default=100)
    ap.add_argument("--lmax",type=int,default=100)
    ap.add_argument("--out",default="result.json")
    a=ap.parse_args()
    mp.mp.dps=a.dps
    t0=time.time()

    Q=cc.build_galerkin_matrix(a.c,N=a.N,T=a.T,dps=a.dps)
    Ve,Qe=sector_matrix(Q,"even")
    eig,U=mp.eigsy(Qe)
    l1,l2=eig[0],eig[1]
    gap=l2-l1

    vp,diag=exact_even_fourier_vector(a.c,a.N,a.lmax)
    ve=Ve.T*vp
    ve/=mp.sqrt((ve.T*ve)[0])

    ray=(ve.T*Qe*ve)[0]
    resvec=Qe*ve-ray*ve
    res=mp.sqrt((resvec.T*resvec)[0])
    ground=U[:,0]
    ov=abs((ground.T*ve)[0])
    angle=1-ov**2
    rex=ray-l1
    dist2=abs(l2-ray)
    rec=dict(
        c=a.c,N=a.N,T=a.T,dps=a.dps,lmax=a.lmax,
        L=mp.nstr(mp.log(a.c),40),
        lam1=mp.nstr(l1,50),lam2=mp.nstr(l2,50),gap=mp.nstr(gap,50),
        prolate_rayleigh=mp.nstr(ray,50),
        rayleigh_excess=mp.nstr(rex,50),
        residual_norm=mp.nstr(res,50),
        overlap=mp.nstr(ov,50),
        one_minus_overlap_sq=mp.nstr(angle,50),
        rayleigh_excess_over_gap=mp.nstr(rex/gap,50),
        residual_over_dist2=mp.nstr(res/dist2,50),
        seconds=round(time.time()-t0,1),
        uses_zero_data=False,
        exact_mellin_projection=True,
        **diag
    )
    open(a.out,"w").write(json.dumps(rec))
    print(json.dumps(rec),flush=True)


if __name__=="__main__":
    main()
