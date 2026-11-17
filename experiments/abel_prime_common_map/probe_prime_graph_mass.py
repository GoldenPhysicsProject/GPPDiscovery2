"""All-prime graph mass and possible superadditivity: NUMERICAL PROBE ONLY.

No certified global prime inequality, RH proof, or all-width positive Schur test.
Exact analytic graph/parity results are in companion research note.
"""
import math,bisect
N=4_000_000
sieve=bytearray(b'\x01')*(N+1)
sieve[0]=sieve[1]=0
for p in range(2,math.isqrt(N)+1):
    if sieve[p]:
        sieve[p*p::p]=b'\x00'*((N-p*p)//p+1)
weights=[0.]*(N+1)
events=[]
for p in range(2,N+1):
    if sieve[p]:
        ellp=math.log(p)
        q=p
        while q<=N:
            v=ellp/math.sqrt(q)
            weights[q]=v
            events.append((math.log(q),v))
            q*=p
prefix=weights[:]
for n in range(1,N+1):prefix[n]+=prefix[n-1]
events.sort()
logs=[el for el,v in events]
partial=[0.]
for el,v in events:partial.append(partial[-1]+v)
def V(t):
    return partial[bisect.bisect_right(logs,t)] if t>=0 else 0.
for L in (0.72,1.2,1.6,2,3.5,5,8,10,12,15):
    assert math.exp(L)<N
    i=bisect.bisect_left(logs,L)
    endpoints=[0.,L]
    for el in logs[:i]:endpoints.extend((el,L-el))
    endpoints=sorted(set(endpoints))
    # Midpoints of open cells give the ESSENTIAL sup, not accidental
    # isolated simultaneous double-jumps at prime thresholds.
    M=max(V((a+b)/2)+V(L-(a+b)/2)
          for a,b in zip(endpoints,endpoints[1:]) if b>a)
    Vs=V(L)
    Pneg=2*math.sinh(L/2)-L
    B_old=5.3721834192256656+2*Vs+2*L*math.exp(L/2)
    B_new=5.3721834192256656+M+Pneg
    assert M<=Vs+V(L/2)+1e-8
    print('L %.2f V %.9f M %.9f pole_neg %.9f oldB %.4f newB %.4f'
          %(L,Vs,M,Pneg,B_old,B_new))
    if abs(M-Vs)>1e-8:
        print('WEIGHTED-SUPERADDITIVITY CONJECTURE COUNTEREXAMPLE',L,M-Vs)
worst=(float('inf'),0,0)
for n in range(2,2001):
    for m in range(2,2001):
        d=prefix[n*m]-prefix[n]-prefix[m]
        if d<worst[0]:worst=(d,n,m)
assert worst[0]>0
print('NUMERICAL n,m<=2000 superadditivity PASS; min gap',worst)
print('M(L)=V(L) is an observation at sampled L only, NOT proved.')
