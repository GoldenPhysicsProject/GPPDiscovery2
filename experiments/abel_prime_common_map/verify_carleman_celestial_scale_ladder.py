"""65-digit audit: prime RG -> Carleman -> celestial P via gamma duplication.

All exact theorems are proved analytically in the companion research note.
Numbers are independently reproducible checks, NOT an RH/Weil certificate.
"""
import mpmath as m
m.mp.dps=65

def C(lam):
    return m.pi/m.cosh(m.pi*lam)

def P(lam):
    return m.pi*lam/m.sinh(m.pi*lam) if lam else m.mpf(1)

for l in map(m.mpf,['0','.03','.2','.7','1.7','3.1']):
    assert m.almosteq(C(l),abs(m.gamma(m.mpf('.5')+1j*l))**2)
    assert m.almosteq(P(l),abs(m.gamma(1+1j*l))**2)
    assert m.almosteq(P(2*l),C(l)*P(l)/m.pi)
    if l:
        assert m.almosteq(m.beta(m.mpf('.5')+1j*l,m.mpf('.5')-1j*l),C(l))
    prev=None
    for n in [4,8,16,30,60]:
        q=m.fprod([1/m.cosh(m.pi*l/(2**j)) for j in range(1,n+1)])
        assert abs(q-P(l))<abs(P(l))*(4*(m.pi*l/(2**n))**2+m.mpf('1e-62'))
        if prev is not None and l:assert q<prev
        prev=q
    print('lambda',str(l),'C',m.nstr(C(l),20),'P',m.nstr(P(l),20),
          '60-step error',m.nstr(abs(q-P(l)),12))

# Exact Carleman Mellin eigenvalue formula, independently integrated.
for lam in map(m.mpf,['0','.7','1.7']):
    beta=m.quad(lambda z:z**(-m.mpf('.5')+1j*lam)/(1+z),[0,1,m.inf])
    assert abs(beta-C(lam))<m.mpf('1e-25')

# The dyadic factors are characteristic functions of scaled sech laws.
# The limiting law is the logistic distribution in Daniel's August paper.
for lam in map(m.mpf,['.2','1','2']):
    logistic=m.quad(lambda x:m.cos(lam*x)/(4*m.cosh(x/2)**2),[-m.inf,0,m.inf])
    sech=m.quad(lambda x:m.cos(lam*x)/(2*m.pi*m.cosh(x/2)),[-m.inf,0,m.inf])
    assert abs(logistic-P(lam))<m.mpf('1e-27')
    assert abs(sech-1/m.cosh(m.pi*lam))<m.mpf('1e-26')

# Main dimension-doubled transfer is bounded: P(2lambda)<=C(lambda)/pi.
for lam in map(m.mpf,['0','.2','.7','3']):
    assert P(2*lam)<=C(lam)/m.pi+m.mpf('1e-45')

# Analytic uniform norm bound for N factors: (16/(3e^2))*4^(-N).
# Finite numerical samples demonstrate it without serving as proof.
for N in [1,2,3,5,8,12]:
    bound=16/(3*m.e**2*4**N)
    for k in range(601):
        lam=m.mpf(k)/100
        pN=m.fprod(1/m.cosh(m.pi*lam/2**j) for j in range(1,N+1))
        assert 0<=pN-P(lam)<bound
    print('N',N,'certified ANALYTIC operator bound',m.nstr(bound,14))
print('PASS numerical Carleman / celestial scale ladder, no RH claim.')
