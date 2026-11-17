"""Exact finite-shift cutoff-flow arithmetic; mpmath true Weil-box checks.
Research only: no RH assumption, no zero inputs. External certification not claimed."""
from fractions import Fraction as F
import mpmath as mp

def toy(c):
    r=F(1,2); a=sum(x*x for x in c)
    corr=lambda k: sum(c[j]*c[j+k] for j in range(len(c)-k))
    local=F(a)+2*sum((r**k)*corr(k) for k in range(1,len(c)))
    base=F(4)
    q=base-local
    results=[]
    for mass in [0,1,10,100,1000]:
        B=base+mass*a; C=local+mass*a
        ratio=F(C,B)
        results.append((mass,ratio))
        assert F(B-C)==q
        assert 1-ratio==F(q,B)
    for (s,R),(t,S) in zip(results[:-1],results[1:]):
        Bs=base+s*a; Bt=base+t*a
        assert S-R == F((t-s)*a*q,Bs*Bt)
    return {'coefficients':c,'L2':a,'local_Csq':local,'Q':q,'cutoff_ratios':results}

for c in [(1,1,1),(1,-1,1)]:
    print('TOY', toy(c))

mp.mp.dps=45
L=mp.mpf('1.0')
Cinf=mp.digamma(mp.mpf(1)/4)-mp.log(mp.pi)
a=[2*k+mp.mpf('.5') for k in range(10000)]
E=2*sum((-mp.expm1(-ak*L))/ak**2 for ak in a)
# Absolute positive tail of terms after k=9999 is less than 1/(2*(2*9999+.5)) < .000025; numeric sample only.
pole=16*(mp.cosh(L/2)-1)
v2=mp.log(2)/mp.sqrt(2)
Q=E+Cinf*L+pole-2*v2*(L-mp.log(2))
print('BOX t=1 Q via 10000 gamma modes',mp.nstr(Q,35),'gamma-tail <',mp.nstr(1/(2*9999+.5),10))
for N in [2,3,5,11,101,1009]:
    primes=[k for k in range(2,N+1) if all(k%d for d in range(2,int(k**.5)+1))]
    theta=sum(mp.log(p) for p in primes)
    B=E+Cinf*L+pole+theta*L
    C=B-Q
    print('N',N,'theta',mp.nstr(theta,14),'B',mp.nstr(B,14),'ratio',mp.nstr(C/B,18),'theta*(1-ratio)',mp.nstr(theta*(1-C/B),16))

# Translation-invariant, sign-indefinite example with ALL box indicators positive.
for length in [F(1,10),F(1),F(2),F(100)]:
    boxform=length+2*max(F(0),length-1)
    assert boxform>0
    print("ALL-BOX TOY: L=",length,"Q(box)=",boxform)
for k in [2,3,5]:
    vals=[(-1)**j for j in range(k)]
    q=sum(v*v for v in vals)+2*sum(vals[j]*vals[j+1] for j in range(k-1))
    assert q==2-k
    print("ALTERNATING BUMP CHAIN K=",k,"Q / ||h||^2=",q)
