#!/usr/bin/env python3
"""Exact-formula numerical diagnostic for the pole-only Weil cross-face operator.
This does NOT compute the completed Weil form, nor establish RH."""
import mpmath as mp

mp.mp.dps = 70

def odd_gram(a, b, h):
    x, y = a+b, a-b
    return mp.sinh(x*h)/x - (h if abs(y)<mp.mpf('1e-40')
                              else mp.sinh(y*h)/y)

def pole_zeta(h):
    return -2*odd_gram(mp.mpf('0.5'),mp.mpf('0.5'),h)

def pole_shifted(theta, h):
    ap, am = mp.mpf('0.5')+theta,mp.mpf('0.5')-theta
    a = odd_gram(ap, ap, h)
    b = odd_gram(am, am, h)
    c = odd_gram(ap, am, h)
    det = a*b-c*c
    assert det > 0, 'nonpositive shifted odd Gram determinant'
    plus = (a+b+mp.sqrt((a-b)**2+4*c*c))/2
    minus = det/plus
    return -2*plus, -2*minus, det

def main():
    theta=mp.mpf(1)/4
    for h in map(mp.mpf,['0.34657359027997265','0.76','2','4','8','16']):
        m1,m2,det=pole_shifted(theta,h)
        print('h=',mp.nstr(h,8),'zeta=',mp.nstr(pole_zeta(h),18),
              'shifted=',mp.nstr(m1,18),mp.nstr(m2,18))
        assert m1<m2<0
        if h>=16:
            a1=-(mp.mpf(2)/3)*mp.exp(mp.mpf('1.5')*h)
            a2=-mp.mpf('0.5')*mp.exp(h/2)
            assert abs(m1/a1-1)<mp.mpf('.001')
            assert abs(m2/a2-1)<mp.mpf('.03')
if __name__ == '__main__':
    main()
