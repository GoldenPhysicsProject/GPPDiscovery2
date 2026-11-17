"""Independent real-space checks of ALL-PRIME graph Dirichlet identity.

Numerical finite-window diagnostics, no RH or operator-positivity certificate.
"""
import math
import numpy as np
from scipy.special import roots_legendre
from arith_graph_common import mangoldt_sieve, w, K, CINF

nodes, weights=roots_legendre(210)

def quad_interval(fn,a,b):
    x=(b-a)*nodes/2+(a+b)/2
    return (b-a)/2*np.dot(weights,fn(x))

def f(x,L):
    return np.sqrt(2/L)*np.cos(np.pi*x/L)

def gamma_split(L):
    a,b=-L/2,L/2
    norm=quad_interval(lambda x:f(x,L)**2,a,b)
    C=quad_interval(lambda x:f(x,L)*np.cosh(x/2),a,b)
    S=quad_interval(lambda x:f(x,L)*np.sinh(x/2),a,b)
    pole=2*(C*C-S*S)
    ext=quad_interval(lambda x:(np.vectorize(K)(x-a)+np.vectorize(K)(b-x))/2*f(x,L)**2,a,b)
    def within(t):
        return quad_interval(lambda x:(f(x,L)-f(x-t,L))**2,a+t,b)
    def corr(t):
        return quad_interval(lambda x:f(x,L)*f(x-t,L),a+t,b)
    t=L*(nodes+1)/2
    dt=L*weights/2
    interior=sum(dt_i*w(float(t_i))*within(float(t_i)) for dt_i,t_i in zip(dt,t))
    energy=K(L)*norm+sum(dt_i*2*w(float(t_i))*(norm-corr(float(t_i)))
                        for dt_i,t_i in zip(dt,t))
    return norm,pole,ext,interior,energy

def prime_split(L,lam):
    a,b=-L/2,L/2
    original=degree=jump=0.0
    for n in range(2,math.ceil(math.exp(L))):
        if not lam[n]:continue
        ell=math.log(n)
        if ell>=L:continue
        v=lam[n]/math.sqrt(n)
        original-=2*v*quad_interval(lambda x:f(x,L)*f(x-ell,L),a+ell,b)
        jump+=v*quad_interval(lambda x:(f(x,L)-f(x-ell,L))**2,a+ell,b)
        degree+=v*quad_interval(lambda x:f(x,L)**2+f(x-ell,L)**2,a+ell,b)
    return original,degree,jump

if __name__=="__main__":
    widths=[0.72,1.2,2.0,3.5]
    lam=mangoldt_sieve(math.ceil(math.exp(max(widths)))+2)
    for L in widths:
        norm,pole,ext,internal,E=gamma_split(L)
        prime,degree,jump=prime_split(L,lam)
        orig=E+CINF*norm+pole+prime
        graph=internal+jump+(ext-degree+CINF*norm)+pole
        assert abs(E-ext-internal)<2e-7
        assert abs(prime-(jump-degree))<1e-10
        assert abs(orig-graph)<2e-7
        print("L",L,"W original",orig,"W all-prime graph",graph,
              "absolute difference",abs(orig-graph))
    print("PASS numerical all-prime graph decomposition, NOT a full positivity proof.")
