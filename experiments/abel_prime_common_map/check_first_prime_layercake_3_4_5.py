"""Exact rational layer-cake certificates for the first-prime Weil form.

Checks arithmetic only; source Weil/Fourier/Legendre analytic identifications
still require formal proof. All asserted bounds use exact fractions, no floats.
"""
from fractions import Fraction as Q

L=Q(18,25)

def odd_double_factorial(n):
    x=1
    for k in range(1,2*n+2,2):x*=k
    return x

def band_upper(R,m):
    z=Q(R)*L/2
    s=Q(0)
    for n in range(m,12):
        A=z*z/Q(2*(2*n+3))
        B=z**4/Q(8*(2*n+3)*(2*n+5))
        assert A < 1
        F=(1-2*A*Q(2*n+1,2*n+3)
           +(A*A+2*B)*Q(2*n+1,2*n+5)
           -2*A*B*Q(2*n+1,2*n+7)
           +B*B*Q(2*n+1,2*n+9))
        assert 0<F<=1
        s+=z**(2*n)*F/Q(odd_double_factorial(n)**2)
    n=12
    ratio=z*z/Q((2*n+3)**2)
    assert ratio<1
    s+=z**(2*n)/Q(odd_double_factorial(n)**2)/(1-ratio)
    return L*Q(R)/3*s

def symbol100(R):
    R=Q(R)
    return sum((Q(16*R*R,(4*k+1)*((4*k+1)**2+4*R*R))
                for k in range(100)),Q(0))

def layer_cake(radii,m):
    prev=Q(0);result=Q(0)
    for r in radii:
        d=band_upper(r,m)
        assert 0<=d<1
        a=symbol100(r)
        assert a>prev
        result+=(a-prev)*(1-d)
        prev=a
    return result

claims=[
  (3,[Q(j,2) for j in range(1,24)]+[Q(47,4)],
   Q(59,10),Q(1,50),Q(1,295)),
  (4,[Q(j) for j in range(1,14)],
   Q(121,20),Q(17,100),Q(17,605)),
  (5,[Q(2),Q(4),Q(6),Q(8),Q(10),Q(12),Q(13),Q(14)],
   Q(123,20),Q(27,100),Q(9,205))
]
Mupper=Q(147,25)
for m,radii,E0,margin,eta in claims:
    A=layer_cake(radii,m)
    assert A>E0
    assert E0-Mupper==margin
    assert (E0-Mupper)/E0==eta
    print("moments",m,"thresholds",len(radii),
          "rational lower E~",format(float(A),".12f"),
          "E>",E0, "W>=",margin,"||f||^2",
          "energy coercivity >=",eta)
print("PASS exact rational spectral layer-cake arithmetic; analytic proof open")
