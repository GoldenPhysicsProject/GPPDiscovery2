#!/usr/bin/env python3
"""
Numerical falsification harness for the exact semilocal-Loewner identity.

Uses an arbitrary finite signed compactly supported measure Psi on [0,L].
No zeta zeros and no RH assumptions enter.  It compares:
  (1) Q_mn = Psi[q_mn]
with
  (2) the confluent Loewner matrix of
      f_L(x)=(2/L) Psi[-sin(x y)+sin(Lx)cos(x y)].
"""
import numpy as np

rng=np.random.default_rng(20260927)
L=5.7
N=8
# arbitrary signed distribution sampled as atoms
y=np.sort(rng.uniform(0,L,47))
w=rng.normal(size=len(y))

def Psi(vals):
    return np.dot(w,vals)

def S(x):
    return Psi(np.sin(x*y))
def C(x):
    return Psi(np.cos(x*y))
def Sp(x):
    return Psi(y*np.cos(x*y))
def Cp(x):
    return Psi(-y*np.sin(x*y))

def f(x):
    return (2/L)*(-S(x)+np.sin(L*x)*C(x))
def fp(x):
    return (2/L)*(-Sp(x)+L*np.cos(L*x)*C(x)+np.sin(L*x)*Cp(x))

ns=np.arange(-N,N+1)
xs=2*np.pi*ns/L
M=len(ns)

Q=np.empty((M,M))
for i,m in enumerate(ns):
    for j,n in enumerate(ns):
        if m==n:
            Q[i,j]=Psi(2*(1-y/L)*np.cos(xs[i]*y))
        else:
            q=(np.sin(xs[i]*y)-np.sin(xs[j]*y))/(np.pi*(n-m))
            Q[i,j]=Psi(q)

Lo=np.empty_like(Q)
for i in range(M):
    for j in range(M):
        if i==j:
            Lo[i,j]=fp(xs[i])
        else:
            Lo[i,j]=(f(xs[i])-f(xs[j]))/(xs[i]-xs[j])

err=np.max(np.abs(Q-Lo))
rel=np.linalg.norm(Q-Lo)/max(np.linalg.norm(Q),1e-300)
print(f"max_abs_error={err:.3e}")
print(f"fro_relative_error={rel:.3e}")
assert err < 2e-11
print("PASS: semilocal Weil matrix equals confluent Loewner matrix.")

# shifted/quasiperiodic lattice check
theta=0.317
xst=2*np.pi*(ns+theta)/L

def ftheta(x):
    return (2/L)*(-S(x)+np.sin(L*x-2*np.pi*theta)*C(x))
def fthetap(x):
    phase=L*x-2*np.pi*theta
    return (2/L)*(-Sp(x)+L*np.cos(phase)*C(x)+np.sin(phase)*Cp(x))

Qt=np.empty((M,M))
for i,m in enumerate(ns):
    for j,n in enumerate(ns):
        if m==n:
            Qt[i,j]=Psi(2*(1-y/L)*np.cos(xst[i]*y))
        else:
            q=(np.sin(xst[i]*y)-np.sin(xst[j]*y))/(np.pi*(n-m))
            Qt[i,j]=Psi(q)
Lot=np.empty_like(Qt)
for i in range(M):
    for j in range(M):
        if i==j:
            Lot[i,j]=fthetap(xst[i])
        else:
            Lot[i,j]=(ftheta(xst[i])-ftheta(xst[j]))/(xst[i]-xst[j])
errt=np.max(np.abs(Qt-Lot))
print(f"twisted_max_abs_error={errt:.3e}")
assert errt < 2e-11
print("PASS: quasiperiodic shifted-lattice Loewner identity.")
