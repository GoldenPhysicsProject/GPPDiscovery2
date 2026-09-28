#!/usr/bin/env python3
"""Zero-free Shadow-Euler Pick-matrix diagnostic.

Tests the RH-equivalent Nevanlinna-Pick kernel on one shifted Shadow-Euler
sampling family:
  z_N = (kN/(k+N)-1/2)^2 + i eta,
  q(u) = -F'(u)/F(u),
  F(u) = xi(1/2+sqrt(u))/xi(1/2).

No Riemann-zero ordinates or root finding are used.
"""

import argparse, json
import mpmath as mp


def xi(s):
    return (
        mp.mpf("0.5") * s * (s-1)
        * mp.power(mp.pi, -s/2)
        * mp.gamma(s/2) * mp.zeta(s)
    )


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--k",type=int,default=2)
    ap.add_argument("--eta",default="0.5")
    ap.add_argument("--M",type=int,default=8)
    ap.add_argument("--dps",type=int,default=100)
    ap.add_argument("--out",default="pick.json")
    a=ap.parse_args()
    mp.mp.dps=a.dps
    eta=mp.mpf(a.eta)
    xi0=xi(mp.mpf("0.5"))

    def F(u):
        r=mp.sqrt(u)
        return xi(mp.mpf("0.5")+r)/xi0

    def q(u):
        return -mp.diff(lambda x: mp.log(F(x)),u)

    zs=[]
    for N in range(2,2+a.M):
        s=mp.mpf(a.k)*N/(a.k+N)
        u=(s-mp.mpf("0.5"))**2
        zs.append(u+1j*eta)

    P=mp.matrix(a.M)
    for i,z in enumerate(zs):
        for j,w in enumerate(zs):
            P[i,j]=(q(z)-mp.conj(q(w)))/(z-mp.conj(w))
    P=(P+P.H)/2
    ev=mp.eighe(P,eigvals_only=True)
    vals=[mp.re(ev[i]) for i in range(a.M)]

    rec={
        "k":a.k,"eta":str(eta),"M":a.M,"dps":a.dps,
        "min_eigenvalue":mp.nstr(min(vals),40),
        "max_eigenvalue":mp.nstr(max(vals),40),
        "eigenvalues":[mp.nstr(v,30) for v in vals],
        "uses_zero_data":False,
        "uses_root_finding":False,
    }
    open(a.out,"w").write(json.dumps(rec))
    print(json.dumps(rec))


if __name__=="__main__":
    main()
