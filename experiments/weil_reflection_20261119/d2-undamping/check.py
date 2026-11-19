"""Arithmetic check and full L2 tail bound for undamping at a=2."""
from math import ceil, cosh, exp, expm1, log, pi, sin, sqrt
from scipy.integrate import quad
from scipy.special import digamma

RATES=(0.5,1.5,2.5)

def prime_powers(width):
    limit=ceil(exp(width))
    prime=[True]*(limit+1)
    for p in range(2,limit+1):
        if not prime[p]:
            continue
        for m in range(2*p,limit+1,p):
            prime[m]=False
        n=p
        while log(n)<width:
            yield log(n), log(p)/sqrt(n)
            n*=p

def run(L,j,r,theta):
    """f=(g+T_r g)/sqrt(2) for normalized j-th Dirichlet sine g on [0,L]."""
    width=L+r
    k=j*pi/L
    def overlap(t):
        from math import cos
        x=abs(t)
        if x>=L: return 0.
        return (1-x/L)*cos(k*x)+sin(k*x)/(k*L)
    def C(t):
        return overlap(t)+(overlap(t-r)+overlap(t+r))/2
    def factor(t):
        return 1. if theta is None else 2*cosh(theta*t)
    knots=sorted({z for z in [r,L,abs(L-r)] if 0<z<width})
    def integrate(function):
        return quad(function,0,width,points=knots,epsabs=1e-11,epsrel=1e-11)[0]
    shifts=list(prime_powers(width))
    offsets=(0.,) if theta is None else (-theta,theta)
    def arithmetic(a):
        # Shift the entire gamma factor and poles for the fake.
        c=sum(digamma((.5+b)/2)-log(pi) for b in offsets)
        def w(t):
            return sum(exp(-(.5+b)*t) for b in offsets)/(-expm1(-2*t))
        v=(c+2*quad(w,width,float('inf'),epsabs=1e-12)[0])*C(0)
        v+=2*integrate(lambda t:w(t)*(C(0)-exp(-a*t)*C(t)))
        v+=4*integrate(lambda t:sum(cosh((.5+b)*t) for b in offsets)*exp(-a*t)*C(t))
        return v-2*sum(coef*factor(h)*exp(-a*h)*C(h) for h,coef in shifts)
    smooth=2*integrate(lambda h:factor(h)*(exp(h/2)-exp(-1.5*h)-exp(-2.5*h))*C(h))
    atoms=-2*sum(coef*factor(h)*(-expm1(-2*h))*C(h) for h,coef in shifts)
    q0,q2=arithmetic(0),arithmetic(2)
    assert abs(q0-q2-smooth-atoms)<2e-10
    return q0,q2,smooth,atoms

if __name__=='__main__':
    for L,j,r in [(.72,1,0),(3,20,log(7))]:
        for theta in (None,.25):
            print(L,j,r,theta,'Q0 Q2 smooth atoms',run(L,j,r,theta))
    L=.72
    c=log(2)/sqrt(2)*(1-2**-2)
    print('first prime essential norm on L2',c)
    for m in (25,100):
        exact=sum(2*b/(b*b+((m+1)*pi/L)**2) for b in RATES)
        print(m,'exact diagonal tail norm',exact,'upper bound',9*(L/((m+1)*pi))**2)

def check_boundary_kernel():
    """K_b=2b(-d²+b²)_D^{-1}+H_b exactly, with rank(H_b)<=2."""
    from math import sinh
    L=.72
    for b in RATES:
        for x in [0.,.13,L/2,.69,L]:
            for y in [0.,.03,.47,L]:
                green=2*sinh(b*min(x,y))*sinh(b*(L-max(x,y)))/sinh(b*L)
                boundary=(sinh(b*(L-x))*exp(-b*y)+sinh(b*x)*exp(-b*(L-y)))/sinh(b*L)
                assert abs(green+boundary-exp(-b*abs(x-y)))<2e-15

if __name__=='__main__':
    check_boundary_kernel()
