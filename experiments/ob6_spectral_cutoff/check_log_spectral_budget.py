"""Paper-level numerical diagnostics for the logarithmic Weil kinetic barrier.
No RH assumption, no zeros, no numerical interval certification.
Theorems in research note use exact Hilbert space estimates, not these floating checks.
"""
import mpmath as mp
mp.mp.dps=35
L=mp.mpf('0.72'); N=11
primes=[2,3,5,7,11]
CINF=mp.digamma(mp.mpf(1)/4)-mp.log(mp.pi)
THETA=sum(mp.log(p) for p in primes)
KAPPA=CINF+L-2*mp.sinh(L/2)
m=THETA+KAPPA
D=abs(CINF)+4*mp.sinh(L/2)
T=sum(mp.log(p)*(1+p**(-mp.mpf('.5')))/(1-p**(-mp.mpf('.5'))) for p in primes)
assert m>0
print('L',L,'N',N,'coercivity_m',mp.nstr(m,20),'tN0',mp.nstr(T,20),'D_L',mp.nstr(D,20))
for eps in [mp.mpf('.2'),mp.mpf('.1'),mp.mpf('.01')]:
    need=T*(1+D/m)/(eps**2)
    # asymptotic a(R) = log(R/2)-digamma(1/4)+o(1)
    logRapprox=need+mp.log(2)+mp.digamma(mp.mpf('0.25'))
    print('eps',eps,'required a(R) >=',mp.nstr(need,16),'asymptotic log R >=',mp.nstr(logRapprox,16))

def a(k):
    return mp.re(mp.digamma(mp.mpf(1)/4+1j*k/2))-mp.digamma(mp.mpf(1)/4)

# Exactly normalized Dirichlet sine autocorrelation on [0,L].
def auto(t,k):
    return (1-t/L)*mp.cos(k*t)+mp.sin(k*t)/(k*L) if t<L else mp.mpf(0)

def energy_by_autocorr(n):
    k=n*mp.pi/L
    w=lambda t: mp.exp(-t/2)/(1-mp.exp(-2*t))
    fun=lambda t: w(t)*(1-auto(t,k))
    nodes=[L*j/(10*n) for j in range(10*n+1)]
    inte=mp.fsum(mp.quad(fun,[u,v]) for u,v in zip(nodes[:-1],nodes[1:]))
    u=mp.exp(-L/2)
    tail=mp.atanh(u)+mp.atan(u)
    return 2*(inte+tail)

for n in [1,2,4,8,16,32]:
    k=n*mp.pi/L
    if n<=8:
        en=energy_by_autocorr(n)
        print('sine n',n,'E',mp.nstr(en,19),'a(k)',mp.nstr(a(k),19),'difference',mp.nstr(en-a(k),12))
    else:
        print('sine n',n,'a(k)',mp.nstr(a(k),18),'log n',mp.nstr(mp.log(n),16))
print('PASS diagnostics; exact theorems do not rely on numeric quadrature')
