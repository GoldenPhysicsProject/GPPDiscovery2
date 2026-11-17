"""Independent numerical bridge between source Weil interval tests and
Suzuki (2025) screw functions g0 and g∞. Analytic identities in research note.
No RH proof, no claimed new result for the published scalar criterion.
"""
import math
import numpy as np
import mpmath as mp
from arith_graph_common import mangoldt_sieve, box_weil
mp.mp.dps=40

def suzuki_ginfty(L):
    t=mp.mpf(str(L))
    z=mp.exp(-t/2)
    a=mp.mpf(1)/4
    return -t/2*(mp.digamma(a)-mp.log(mp.pi))-(mp.zeta(2,a)-z*mp.lerchphi(z**4,2,a))/4

if __name__=="__main__":
    Ls=[.72,1.,2.,3.5,6.,10.,12.]
    lam=mangoldt_sieve(math.ceil(math.exp(max(Ls)))+2)
    for L in Ls:
        nmax=int(math.exp(L))
        n=np.arange(2,nmax+1,dtype=np.float64)
        weight=lam[2:nmax+1]/np.sqrt(n)
        ell=np.log(n)
        active=ell<L
        V=float(np.sum(weight[active]))
        g0=float(np.sum(weight[active]*(L-ell[active]))
                  -4*(math.exp(L/2)+math.exp(-L/2)-2))
        H=-g0
        D=4*math.sinh(L/2)-V
        W=box_weil(L,lam)
        ginf=float(suzuki_ginfty(L))
        W_screw=-2*(g0+ginf)/L
        assert abs(W-W_screw)<1e-9
        print("L",L,"Wbox",W,"-2gζ/L",W_screw,"H=-g0",H,"D=H'",D)
    print("PASS Suzuki exact-normalization bridge numerically, no proof of sign.")
