#!/usr/bin/env python3
"""High precision checks for semilocal kinetic/pole identities, see adjacent .md."""
import mpmath as mp
mp.mp.dps=45
L=2*mp.log(mp.mpf(5)/2)
t=mp.exp(-L/2)
I=mp.quad(lambda y:(mp.exp(y/2)-1)/(2*mp.sinh(y)),[0,L])
Ic=mp.log(2/(1+t))-mp.log(2/(1+t*t))/2+mp.pi/4-mp.atan(t)
assert abs(I-Ic)<mp.mpf('1e-35')
assert L-2*mp.sinh(L/2)<0
print('PASS gamma tilt closed formula and negative pole eigenvalue')
