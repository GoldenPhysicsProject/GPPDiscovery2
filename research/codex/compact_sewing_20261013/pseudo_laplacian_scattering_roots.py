"""Eisenstein constant-term pseudo-Laplacian secular roots, not zeta zeros."""
import numpy as np,mpmath as m
from scipy.optimize import brentq
m.mp.dps=30
def scattering(t):
 w=m.mpc('.5',t)
 return complex(m.sqrt(m.pi)*m.gamma(w-.5)/m.gamma(w)*m.zeta(2*w-1)/m.zeta(2*w))
def ratio(t,T):return scattering(t)*np.exp(-2j*t*np.log(T))
def roots(T,tmax=30,step=.05):
 grid=np.arange(.02,tmax,step)
 angles=np.unwrap(np.angle([ratio(t,T) for t in grid]))
 hits=[]
 for i in range(len(grid)-1):
  a,b=angles[i:i+2]
  if int(np.floor((a-np.pi)/(2*np.pi)))!=int(np.floor((b-np.pi)/(2*np.pi))):
   t=brentq(lambda x:np.imag(ratio(x,T)),grid[i],grid[i+1],xtol=1e-12)
   if np.real(ratio(t,T))<-.999999:hits.append(t)
 return hits
if __name__=='__main__':
 for T in [2,3,5]:
  rr=roots(T)[:5]
  print(T,rr,[.25+t*t for t in rr])
  assert all(abs(1+ratio(t,T))<1e-8 for t in rr)
