"""Exact rational first-prime reflection sewing acceptance test.

This is a falsifier for proposals claiming TERM-BY-TERM positive prime OS
pairings, not a no-go for the correct completed prime+gamma+pole Weil form.
All identities/decisive signs use fractions, never floats.

For global parity sigma=±1 and local endpoint parity tau=±1,
g=(1,tau) on the first strip and right boundary = sigma * reverse(g).
On this two-cell toy space, a second strip has independent amplitudes
for the full operator test. Normalize w2=log 2/sqrt2 >0 SYMBOLICALLY:
source/w2 = -2 Re<u,v>, boundary tax/w2 = -(|u|²+|v|²),
edge energy/w2 = |u-v|².
The exact algebra is edge - tax = source; the spectrum of the source
operator -w2 [[0,I],[I,0]] is ±w2. For any positive rank-one/TFD
local candidate K, equality K=source on the WHOLE Hilbert space is
impossible. The smallest uniform diagonal compensation to turn source
into a PSD Gram is exactly w2, and source+w2*I is a positive square.
The original source IS NOT that square: one must subtract contact w2 I.
"""
from fractions import Fraction as F


def sq_norm(v):
    return sum(x*x for x in v)


def overlap(a,b):
    return sum(x*y for x,y in zip(a,b))


def assert_complex_scalar_identity():
    # Generic Gaussian integers as exact coordinate pairs (Re, Im).
    # Python complex abs() is floating and MUST NOT certify equality.
    samples=((1,0),(1,1),(0,1),(-2,3),(0,-1))
    for u in samples:
        for v in samples:
            d=(u[0]-v[0])**2+(u[1]-v[1])**2
            m=u[0]**2+u[1]**2+v[0]**2+v[1]**2
            src=-2*(u[0]*v[0]+u[1]*v[1])
            assert d-m==src


def exact_reflection_channels():
    print('global sigma  local tau  -S2/(2w||g||²)  D/w  M/w')
    for sigma in (F(1),F(-1)):
        for tau in (F(1),F(-1)):
            g=(F(1),tau)
            Rg=(g[1],g[0])
            h=tuple(sigma*x for x in Rg)
            D=sq_norm(tuple(x-y for x,y in zip(g,h)))
            M=sq_norm(g)+sq_norm(h)
            source=D-M
            assert source==-2*overlap(g,h)
            assert source==-2*sigma*tau*sq_norm(g)
            print(str(sigma), str(tau), str(source/(2*sq_norm(g))),
                  str(D), str(M))
            assert source/(2*sq_norm(g))==-sigma*tau


def exact_local_PSD_obstruction():
    # Two-complex-sheets. Normalize the true prime coefficient w2=1
    # because positivity only depends on w2>0.
    sym=(F(1),F(1))
    anti=(F(1),F(-1))
    source=lambda x: -2*x[0]*x[1]
    assert source(sym)==-2
    assert source(anti)==2
    for d in (F(0),F(1,2),F(9,10)):
        # Candidate positive diagonal compensation d*I is impossible
        # since on symmetric vector it leaves negative quadratic energy.
        assert source(sym)+d*sq_norm(sym)<0
    # Exact minimum diagonal correction.
    for x in (sym,anti,(F(1),F(0)),(F(2,3),F(-5,7))):
        assert source(x)+sq_norm(x)==(x[0]-x[1])**2>=0
    # For a scalar uniform diagonal c, c>=1 is necessary and
    # sufficient for cI - swap to be PSD (eigenvalues c±1).
    assert source(sym)+F(1)*sq_norm(sym)==0
    assert source(anti)+F(1)*sq_norm(anti)>0
    print('Exact local obstruction: normalized source has +/-1 spectrum; '
          'minimum diagonal completion is c=1, and cI-source edge')
    # Ftheta local Toeplitz falsifier without transcendentals:
    # put q=p^theta>1, m1=q+q^-1. Negative determinant:
    # 4-(q+1/q)^2=-(q-1/q)^2.
    for q in (F(2),F(3,2),F(17,13)):
        m1=q+1/q
        det=4-m1*m1
        assert det==-(q-1/q)**2
        assert det<0
    print('Exact rational shifted Satake falsifier: negative 2x2 Toeplitz '
          'det for every tested q>1; algebra proves it for ALL q != 1')


if __name__=='__main__':
    assert_complex_scalar_identity()
    exact_reflection_channels()
    exact_local_PSD_obstruction()
    print('First-prime reflection/TFD acceptance tests PASS. '
          'No global Weil positivity claim; RH remains OPEN.')
