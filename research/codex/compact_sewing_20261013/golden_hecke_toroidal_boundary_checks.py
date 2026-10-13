"""Golden Hecke closed-geodesic identity numerical control; exact proof in bridge."""
import numpy as np
import mpmath as mp
from scipy.special import gamma
from numpy.polynomial.legendre import leggauss
from sympy import Matrix, eye
phi=(1+np.sqrt(5))/2
L=4*np.log(phi)
def L5(s):
    return mp.power(5,-s)*(mp.zeta(s,mp.mpf(1)/5)-mp.zeta(s,mp.mpf(2)/5)-mp.zeta(s,mp.mpf(3)/5)+mp.zeta(s,mp.mpf(4)/5))
def LamK(s):
    return mp.power(5,mp.mpf(s)/2)*mp.power(mp.pi,-s)*mp.gamma(mp.mpf(s)/2)**2*mp.zeta(s)*L5(s)
def numeric_hecke(s,N=120):
    a=np.arange(-N,N+1)
    m,n=np.meshgrid(a,a,indexing='ij')
    mask=(m!=0)|(n!=0)
    m=m[mask].astype(float);n=n[mask].astype(float)
    aa=n+m*phi;bb=n+m*(1-phi)
    xs,ws=leggauss(52)
    total=0.
    for x,w in zip(xs,ws):
        t=L*(x+1)/2
        total+=L*w/2*np.sum((np.sqrt(5)/(aa**2*np.exp(t)+bb**2*np.exp(-t)))**s)
    return np.pi**(-s)*gamma(s)*total/2
P=(eye(2)+Matrix([[0,1],[1,0]]))/2
M=(eye(2)-Matrix([[0,1],[1,0]]))/2
assert P*P==P and M*M==M and P*M==Matrix.zeros(2)
for p in [2,3,5,7,11,19,29,31]:
    chi=0 if p==5 else (1 if p%5 in (1,4) else -1)
    if p==5: continue
    F=eye(2) if chi==1 else Matrix([[0,1],[1,0]])
    assert F*P==P and F*M==chi*M
mp.mp.dps=50
for s,tol in [(2.5,2e-6),(3.5,1e-9)]:
    got=numeric_hecke(s)
    target=float(LamK(s))
    print('s',s,'geodesic',got,'LambdaK',target,'relative error',got/target-1)
    assert abs(got/target-1)<tol
golden=(1+mp.sqrt(5))/2
L1=-sum(c*mp.digamma(mp.mpf(a)/5) for a,c in ((1,1),(2,-1),(3,-1),(4,1)))/5
assert abs(mp.sqrt(5)*L1-2*mp.log(golden))<mp.mpf('1e-45')
for t in [-3.2,-mp.log(golden),0,mp.log(golden),4]:
    z=lambda t: mp.mpf('.5')+mp.sqrt(5)/2*(mp.tanh(t)+1j/mp.cosh(t))
    assert abs(-1/z(t)-z(-t-2*mp.log(golden)))<mp.mpf('1e-43')
print('PASS: Hecke normalization, Galois Haar projectors, Weyl reflection, cusp residue')
