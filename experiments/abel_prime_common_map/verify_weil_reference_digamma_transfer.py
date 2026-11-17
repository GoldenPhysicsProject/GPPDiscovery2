"""70-digit regression: gamma digamma recurrence and prime discrepancy transfer.
No RH, no zero-free claim; companion research note proves exact algebra.
"""
import mpmath as mp
mp.mp.dps=70
CINF=-mp.euler-mp.log(mp.pi)-mp.pi/2-3*mp.log(2)
def a_all(lam):
    return mp.re(mp.digamma(mp.mpf('0.25')+1j*lam/2)-mp.digamma(mp.mpf('0.25')))
def m_ref(lam):
    return mp.re(mp.digamma(mp.mpf('1.25')+1j*lam/2))-mp.log(mp.pi)
def m_gamma_yukawa(lam):
    return CINF+a_all(lam)+1/(lam*lam+mp.mpf('.25'))
for x in [0,mp.mpf('.01'),1,2,5,6,7,10,20,50,100]:
    assert abs(m_ref(x)-m_gamma_yukawa(x))<mp.mpf('1e-62')
    print('lambda',mp.nstr(x,9),'reference symbol',mp.nstr(m_ref(x),28))
r=mp.findroot(m_ref,(5,9))
assert abs(m_ref(r))<mp.mpf('1e-65')
assert m_ref(6)<0<m_ref(7)
print('single reference crossing',mp.nstr(r,50))
print('m_ref(0)',mp.nstr(m_ref(0),40))
# h(s)=-zeta'(s)/zeta(s) with its s=1 pole subtracted.
h=lambda s:-mp.zeta(s,derivative=1)/mp.zeta(s)
for exponent in [6,10,15,20]:
    eps=mp.power(10,-exponent)
    finite=h(1+eps)-1/eps
    print('epsilon 1e-',exponent,'subtract pole',mp.nstr(finite,30))
    assert abs(finite+mp.euler)<mp.mpf(10)*eps
print('renormalized Laplace transfer at s=1/2:',mp.nstr(-mp.euler,40))
print('PASS analytic gamma-shift/Laurent numerical audits; no RH result.')
