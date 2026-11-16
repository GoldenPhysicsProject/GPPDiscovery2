"""Finite negative-control diagnostics for normalized shifted prime coefficients.

a_theta(n) = Lambda(n) cosh(theta log n), with a_0 = Lambda.
Check first prime power at which 2sqrt(Psi_theta)-1-V_theta < 0.
This is numerical only; the proof of eventual failure uses the PNT.
This arithmetic deformation is NOT an entire completed L-function.
"""
import math

N=1_000_000
flags=bytearray(b'\x01')*(N+1)
flags[0]=flags[1]=0
for p in range(2,math.isqrt(N)+1):
    if flags[p]:
        flags[p*p::p]=b'\x00'*((N-p*p)//p+1)
events=[]
for p in range(2,N+1):
    if not flags[p]:
        continue
    q=p
    while q<=N:
        events.append((q,math.log(p)))
        q*=p
events.sort()

for theta in (0.0,0.01,0.05,0.1,0.25,0.4):
    psi=0.0
    V=0.0
    first=None
    for n,lp in events:
        a=lp*math.cosh(theta*math.log(n))
        psi+=a
        V+=a/math.sqrt(n)
        G=2*math.sqrt(psi)-1-V
        if G<0 and first is None:
            first=(n,G)
    if theta==0:
        assert first is None
    else:
        assert first is not None
    print("theta",theta,"first negative G at",first)
print("PASS numerical discrimination only; not a proof of global zeta positivity.")
