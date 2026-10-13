"""Finite-window Riemann-Weil diagnostic. Finite Ritz values are NOT proofs."""
import numpy as np
from scipy.signal import fftconvolve
from scipy.linalg import eigh,null_space
from sympy import primerange
from math import log,exp,pi,sqrt
gamma=.5772156649015329

def trial(h,theta=0.,M=19,N=2201):
 x=np.linspace(-h,h,N);dx=x[1]-x[0];z=x/h
 w=np.zeros(N);good=np.abs(z)<1
 w[good]=np.exp(-.7*z[good]**2/(1-z[good]**2))
 nodes=np.linspace(-.9*h,.9*h,M);d=2.35*h/(M-1)
 B=np.array([np.exp(-.5*((x-c)/d)**2)*w for c in nodes])
 G=B@B.T*dx
 exps=[-.5,.5] if theta==0 else [-.5-theta,-.5+theta,.5-theta,.5+theta]
 C=np.array([B@np.exp(a*x)*dx for a in exps])
 Z=null_space(C)
 s,V=eigh(Z.T@G@Z);mask=s>s[-1]*1e-10
 T=Z@V[:,mask]@np.diag(1/np.sqrt(s[mask]))
 u=np.arange(N)*dx
 terms=[]
 for p in primerange(2,int(exp(2*h))+2):
  n=p
  while log(n)<2*h-1e-12:
   terms.append((log(n),log(p)/sqrt(n)));n*=p
 W=np.zeros((M,M))
 for i in range(M):
  for j in range(i,M):
   f=fftconvolve(B[i],B[j][::-1],mode='full')*dx
   plus=f[N-1:];minus=f[N-1::-1];F0=G[i,j]
   v=np.empty(N);v[0]=F0/2
   v[1:]=(np.exp(-u[1:]/2)*np.cosh(theta*u[1:])*(plus[1:]+minus[1:])-2*np.exp(-u[1:])*F0)/(-np.expm1(-2*u[1:]))
   value=-(log(4*pi)+gamma+log(np.tanh(h)))*F0-np.trapezoid(v,u)
   for t,kappa in terms:
    k=int(t/dx);b=t/dx-k
    value-=kappa*np.cosh(theta*t)*((1-b)*(plus[k]+minus[k])+b*(plus[k+1]+minus[k+1]))
   W[i,j]=W[j,i]=value*(1 if theta==0 else 2)
 return float(eigh(T.T@W@T,eigvals_only=True)[0])

if __name__=='__main__':
 for h in (.5*log(2),.68,.72,.76):
  print(h,exp(h),'zeta',trial(h),'Fquarter',trial(h,.25))
