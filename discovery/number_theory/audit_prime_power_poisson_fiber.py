import math


def K(r, theta):
    return (1-r*r)/(1-2*r*math.cos(theta)+r*r)


def partial(p, a, t, M):
    lp=math.log(p)
    return 2*sum(lp*math.exp(-m*a*lp)*math.cos(m*t*lp) for m in range(1,M+1))

for p,a,t in [(2,1.4,.7),(3,1.2,2.1),(5,2.0,-1.3),(11,1.05,.4)]:
    r=p**(-a)
    th=t*math.log(p)
    target=math.log(p)*(K(r,th)-1)
    print(f'p={p} a={a} t={t} target={target:.17g}')
    for M in [4,8,16,32,64,128]:
        val=partial(p,a,t,M)
        print(M, val, abs(val-target))
    print()
