"""Numerical audit of the prime-only reflection kernel and critical obstruction.

Research note: research/prime_plancherel_OS_wall_2026_11_16.md
Analytic proofs are in the note. This is NOT an RH or Weil-positivity certificate.
"""
import mpmath as mp
mp.mp.dps=65
CINF=-mp.euler-mp.log(mp.pi)-mp.pi/2-3*mp.log(2)
def h(s):
    return -mp.diff(mp.zeta,s)/mp.zeta(s)
assert mp.almosteq(h(mp.mpf('0.5')),CINF/2)
assert h(mp.mpf('0.5'))<0

def mangoldt(n):
    for p in range(2,int(n**0.5)+2):
        if n%p==0:
            k=n
            while k%p==0: k//=p
            return mp.log(p) if k==1 else mp.mpf('0')
    return mp.log(n)

sigma=mp.mpf('1.4')
ts=[mp.mpf(0),mp.mpf('0.1'),mp.mpf('0.3')]
N=80
K=mp.matrix([[mp.fsum(mangoldt(n)*mp.power(n,-sigma-ti-tj)
                       for n in range(2,N+1)) for tj in ts] for ti in ts])
for cs in ([1,0,0],[1,-2,1],[mp.mpf('0.7'),mp.mpf('1.5'),-1]):
    c=mp.matrix(cs)
    quadratic=(c.T*K*c)[0]
    squares=mp.fsum(mangoldt(n)*mp.power(n,-sigma)*
        abs(mp.fsum(c[j]*mp.power(n,-ts[j]) for j in range(3)))**2
        for n in range(2,N+1))
    assert mp.almosteq(quadratic,squares) and quadratic>=0

eps=mp.mpf('.01')
Khalf=mp.matrix([[h(mp.mpf('.5')+ti+tj)
    for tj in (mp.mpf(0),eps)] for ti in (mp.mpf(0),eps)])
assert Khalf[0,0]<0 and Khalf[1,1]<0
neutral=Khalf+mp.matrix([[(-h(mp.mpf('.5')))]*2]*2)
assert mp.almosteq(neutral[0,0],0)
assert mp.det(neutral)<0 and abs(neutral[0,1])>mp.mpf('.01')
assert h(mp.mpf('.5'))+2<0

print("PASS: finite prime Hankel kernel is an explicit sum of nonnegative squares")
print("Cinf/2 =",mp.nstr(CINF/2,35))
print("-zeta'/zeta(1/2) =",mp.nstr(h(mp.mpf('.5')),35))
print("Khalf =",[[mp.nstr(Khalf[i,j],15) for j in range(2)] for i in range(2)])
print("neutral-constant 2x2 determinant =",mp.nstr(mp.det(neutral),25))
print("pole-only-subtracted half density =",mp.nstr(h(mp.mpf('.5'))+2,25))
print("No RH, OS-completion or Weil full positivity claim.")


# The canonical COMPLETED logarithmic derivative is also not an OS kernel:
# the functional equation gives its origin diagonal = 0, but an off-diagonal
# entry is nonzero, contradicting positive semidefiniteness.
xi=lambda s: mp.mpf('.5')*s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)
hxi=lambda s: -mp.diff(xi,s)/xi(s)
assert abs(hxi(mp.mpf('.5')))<mp.mpf('1e-50')
hxi01=hxi(mp.mpf('.5')+eps)
assert abs(hxi01)>mp.mpf('1e-7')
assert -hxi01*hxi01 < 0
print("completed xi log-derivative off-diagonal =",mp.nstr(hxi01,25))
print("completed xi 2x2 determinant =",mp.nstr(-hxi01*hxi01,25))
