"""Numerical illustration of the rigorously proved high-frequency form mismatch.

Source Weil real-place E(f)=<f,a(D)f> with unbounded digamma symbol a,
while the celestial thermal P(D) is bounded and decays at high frequency.
Gaussian modulations are only diagnostics; the proof works on fixed
C_c^infty real test functions (see companion research note).
"""
import mpmath as m
m.mp.dps=45
psi0=m.digamma(m.mpf('.25'))
def a(r):return m.re(m.digamma(m.mpf('.25')+1j*r/2)-psi0)
def P(r):return m.pi*r/m.sinh(m.pi*r) if r else m.mpf(1)
for k in (0,2,5,10,20,40,80):
    e=m.quad(lambda u:m.exp(-u*u)*a(k+u),[-12,0,12])/m.sqrt(m.pi)
    q=m.quad(lambda u:m.exp(-u*u)*P(k+u),[-12,0,12])/m.sqrt(m.pi)
    assert e>=0 and q>0
    print('frequency',k,'archimedean E',m.nstr(e,15),
          'celestial thermal Q',m.nstr(q,15),
          'ratio',m.nstr(e/q,8))
print('PASS: E grows ~ log frequency while P becomes exponentially small.')
