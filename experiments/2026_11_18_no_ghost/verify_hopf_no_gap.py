#!/usr/bin/env python3
"""Independent algebraic Hopf/WWIF geometry checks; no RH claim."""
import numpy as np
rng=np.random.default_rng(20261118)
def mul(a,b):
 x,y,z,w=a;X,Y,Z,W=b
 return np.array([x*X-y*Y-z*Z-w*W,x*Y+y*X+z*W-w*Z,x*Z-y*W+z*X+w*Y,x*W+y*Z-z*Y+w*X])
def conj(a): return np.array([a[0],-a[1],-a[2],-a[3]])
def hopf(u,v): return np.r_[2*mul(u,conj(v)),np.dot(u,u)-np.dot(v,v)]
err=0.0
for i in range(500):
 x=rng.normal(size=8); x/=np.linalg.norm(x);u,v=x[:4],x[4:]
 q=rng.normal(size=4);q/=np.linalg.norm(q)
 h=hopf(u,v)
 a=rng.normal(size=4); a/=np.linalg.norm(a)
 b=rng.normal(size=4); b/=np.linalg.norm(b)
 he=hopf(a/np.sqrt(2),b/np.sqrt(2))
 err=max(err,abs(np.linalg.norm(h)-1),np.linalg.norm(hopf(mul(u,q),mul(v,q))-h),np.linalg.norm(hopf(-u,-v)-h),abs(he[4]),abs(np.linalg.norm(he[:4])-1))
def eps(a,b,c):
 if len({a,b,c})<3:return 0
 return 1 if (a,b,c) in [(0,1,2),(1,2,0),(2,0,1)] else -1
C=np.array([[sum(eps(a,i,j)*eps(b,i,j) for i in range(3) for j in range(3)) for b in range(3)] for a in range(3)])
assert np.array_equal(C,2*np.eye(3))
assert err<5e-15
print('PASS: Hopf S7->S4, Sp(1) fiber, 1/2+1/2 equator S3, T^2 Ric; max residual',err)
print('Analytic identity: chi=pi/2+i t/l sends round S4 to ds2=-dt2+l2*cosh2(t/l)*dOmega3^2.')
print('Weil no-L2-gap statement proved analytically in adjacent research note (not inferred numerically).')
