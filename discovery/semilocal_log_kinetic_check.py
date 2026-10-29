#!/usr/bin/env python3
"""Independent 45 digit checks of the exact semilocal Weil decomposition."""
import mpmath as mp
mp.mp.dps=45
L=2*mp.log(mp.mpf(5)/2)
def q(m,n,y):
    if m==n:
        return 2*(1-y/L)*mp.cos(2*mp.pi*m*y/L)
    return (mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))/(mp.pi*(n-m))
def A(m,s):
    z=mp.mpf(s)/2+2j*mp.pi*m/L
    return (mp.exp(mp.mpf(s)*L/2)-1)/(mp.sqrt(L)*z)
for m,n in [(0,0),(0,1),(1,1),(-2,-1),(0,2)]:
    pole=mp.quad(lambda y:q(m,n,y)*(mp.exp(y/2)+mp.exp(-y/2)),[0,L])
    rank=A(m,1)*mp.conj(A(n,-1))+A(m,-1)*mp.conj(A(n,1))
    assert abs(pole-rank)<mp.mpf('1e-35')
assert L-2*mp.sinh(L/2)<0
for ell in [mp.mpf('.3'),L,mp.mpf(6),mp.mpf(15)]:
    t=mp.exp(-ell/2)
    direct=mp.quad(lambda y:(mp.exp(y/2)-1)/(2*mp.sinh(y)),[0,ell])
    closed=mp.log(2/(1+t))-mp.log(2/(1+t*t))/2+mp.pi/4-mp.atan(t)
    assert abs(direct-closed)<mp.mpf('1e-35')
for xi in [mp.mpf('.1'),mp.mpf(1),mp.mpf(10)]:
    integral=mp.quad(lambda y:(1-mp.cos(xi*y))/mp.sinh(y),[0,1,5,20,65])
    psi=mp.re(mp.digamma(mp.mpf('.5')+.5j*xi)-mp.digamma(mp.mpf('.5')))
    assert abs(integral-psi)<mp.mpf('1e-25')
q0=lambda y:2*(1-y/L)
E=mp.quad(lambda y:y/(L*mp.sinh(y)),[0,L])+2*mp.atanh(mp.exp(-L))
P=mp.quad(lambda y:q0(y)*(mp.exp(y/2)+mp.exp(-y/2)),[0,L])
T=mp.quad(lambda y:q0(y)*(mp.exp(y/2)-1)/(2*mp.sinh(y)),[0,L])
S=sum(mp.log(p)/mp.sqrt(n)*q0(mp.log(n)) for p,n in [(2,2),(3,3),(2,4),(5,5)])
c=mp.log(4*mp.pi)+mp.euler
Q=E+P-c-T-S
M=mp.quad(lambda y:mp.exp(-y/2)*q0(y),[0,L])
R=mp.quad(lambda y:mp.exp(y/2)*q0(y),[0,L])-S
assert abs(Q-(E+M-c-T+R))<mp.mpf('1e-35')
assert abs(Q-mp.mpf('0.039182293233144781752199'))<mp.mpf('4e-25')
print('PASS rank-two pole, gamma tilt, log digamma, PNT Ward and completed Q')
print('Q_(5/2,0)=',mp.nstr(Q,25))
