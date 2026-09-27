#!/usr/bin/env python3
import mpmath as mp
mp.mp.dps=50

def Ainf(r):
    r=mp.mpf(r)
    return (1/(r+mp.mpf('0.5')) + 1/(r-mp.mpf('0.5'))
            - mp.log(mp.pi)/2
            + mp.digamma(r/2+mp.mpf('0.25'))/2)

def ladder(r):
    r=mp.mpf(r)
    A1=Ainf(1)
    escape=1/(r-mp.mpf('0.5'))-2
    tower=mp.nsum(lambda k:
        1/(r+2*k+mp.mpf('0.5'))
        - 1/(2*k+mp.mpf('1.5')),
        [1, mp.inf])
    return A1+escape-tower

tests=['1.1','1.5','2','3.7','10']
errs=[]
for r in tests:
    e=abs(Ainf(r)-ladder(r))
    errs.append(e)
    print(r, mp.nstr(e,20))
assert max(errs) < mp.mpf('1e-40')
print("PASS: Archimedean digamma impedance equals pole-minus-trivial-zero ladder.")
