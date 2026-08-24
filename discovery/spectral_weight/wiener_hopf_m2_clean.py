#!/usr/bin/env python3
"""
Clean salvage: Wiener-Hopf factorization and the A2/Parseval proof of M2=1/90.

This file treats the statements purely as harmonic-analysis facts about
    P(lam)=pi*lam/sinh(pi*lam).
It makes no claim that the abstract convolution integral is an L-loop amplitude.

Fourier convention:
    Phat(k)=int_R exp(-ik lam) P(lam) dlam
           = pi/(2 cosh(k/2)^2).
Gamma reflection gives the exact Wiener-Hopf factors
    Phat_+(k)=(2*pi)^(-1/2) Gamma(1/2-ik/(2*pi))^2
    Phat_-(k)=(2*pi)^(-1/2) Gamma(1/2+ik/(2*pi))^2
with Phat=Phat_+ Phat_-.

For I_Q=int_{x>0,y>0} P(x)P(y)P(x-y) dxdy, evenness of P makes the six
A2 chambers cut by x=0,y=0,x=y equal. The positive quadrant contains two,
so I_Q=I_R2/3. Parseval/convolution gives
    I_R2=(1/(2*pi)) int_R Phat(k)^3 dk = 2*pi^2/15.
Hence M2=I_Q/(2*pi)^2=1/90.
"""
import mpmath as mp
mp.mp.dps=60

P=lambda l: mp.pi*l/mp.sinh(mp.pi*l) if l else mp.mpf(1)
Phat=lambda k: mp.pi/(2*mp.cosh(k/2)**2)
Wp=lambda k: mp.gamma(mp.mpf('0.5')-1j*k/(2*mp.pi))**2/mp.sqrt(2*mp.pi)
Wm=lambda k: mp.gamma(mp.mpf('0.5')+1j*k/(2*mp.pi))**2/mp.sqrt(2*mp.pi)

for k in [mp.mpf('0'),mp.mpf('.7'),mp.mpf('2.3'),mp.mpf('7.1')]:
    assert abs(Wp(k)*Wm(k)-Phat(k)) < mp.mpf('1e-50')

full=mp.quad(lambda k: Phat(k)**3,[-mp.inf,0,mp.inf])/(2*mp.pi)
assert abs(full-2*mp.pi**2/15) < mp.mpf('1e-50')
quadrant=full/3
M2=quadrant/(2*mp.pi)**2
assert abs(M2-mp.mpf(1)/90) < mp.mpf('1e-50')

print('PASS: exact Gamma Wiener-Hopf factorization of Phat')
print('PASS: full-plane A2 convolution = 2*pi^2/15')
print('PASS: chamber symmetry + Parseval gives M2 = 1/90')
