"""Finite-T prime Dirichlet mean square and density-bound audit (NUMERICAL).

Exact analytic identities in research/prime_phase_recurrence_mean_square_2026_11_16.md
No RH or full Weil sign claim.
"""
import math
def prime_powers_under(x):
    N=math.ceil(x)
    sieve=bytearray(b'\1')*(N+1)
    sieve[0]=sieve[1]=0
    for p in range(2,math.isqrt(N)+1):
        if sieve[p]:sieve[p*p::p]=b'\0'*((N-p*p)//p+1)
    data=[]
    for p in range(2,N+1):
        if sieve[p]:
            q=p
            while q<x:
                data.append((math.log(q),math.log(p)/math.sqrt(q)))
                q*=p
    return data
def sinc(z):return math.sin(z)/z if abs(z)>1e-12 else 1.
def finite_mean(data,T):
    return sum(v*w*(sinc(T*(x-y))+sinc(T*(x+y)))
               for x,v in data for y,w in data)/2
def finite_error_bound(data,T):
    return (sum(v*w/abs(x-y) for i,(x,v) in enumerate(data)
                for j,(y,w) in enumerate(data) if i!=j)
           +sum(v*w/(x+y) for x,v in data for y,w in data))/(2*T)
for L in [3.5,5.0]:
    data=prime_powers_under(math.exp(L))
    V=sum(v for _,v in data)
    S2=sum(v*v for _,v in data)
    print('L',L,'prime-power events',len(data),'V',V,'S2/2',S2/2)
    for T in [10,100,1000,10000]:
        observed=finite_mean(data,T)
        bound=finite_error_bound(data,T)
        assert observed>=-1e-9 and abs(observed-S2/2)<=bound+1e-9
        print('T',T,'mean_square',round(observed,9),
              'difference',round(observed-S2/2,9),'bound',round(bound,9))
    eta=.5
    density_upper=S2/(2*eta**2*V**2)
    assert density_upper<1
    print('asymptotic upper density for Re F >= V/2:',density_upper)
print('PASS finite-T trigonometric identity sanity; no RH theorem.')
