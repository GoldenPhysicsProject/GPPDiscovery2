"""Outward-rounded enclosures for two grid witnesses, using mpmath.iv."""
from mpmath import iv
from fractions import Fraction
from math import factorial
iv.dps=40
I=iv.mpc(0,1)
def scalar(f):
    return iv.mpf(f.numerator)/f.denominator
# B2 through B12
ber=[Fraction(1,6),Fraction(-1,30),Fraction(1,42),Fraction(-1,30),
     Fraction(5,66),Fraction(-691,2730)]
def discbox(r):
    t=iv.mpf([-1,1])*r
    return iv.mpc(t,t)
def L(s,ch):
    q=len(ch)
    N=200*q
    v=d=0
    for j in range(1,N+1):
        c=ch[j%q]
        if c:
            l=iv.log(j)
            term=c*iv.exp(-s*l)
            v+=term
            d-=l*term
    for a in range(1,q+1):
        c=ch[a%q]
        if not c: continue
        x=iv.mpf(N+a)
        l=iv.log(x)
        u=x/q/(s-1)+iv.mpf('.5')
        du=-x/q/(s-1)**2
        p,dp=1,0
        for j in range(11):
            dp=dp*(s+j)+p
            p=p*(s+j)
            if j%2==0:
                coef=scalar(ber[j//2])/factorial(j+2)*(q/x)**(j+1)
                u+=coef*p
                du+=coef*dp
        fac=c*iv.exp(-s*l)
        v+=fac*u
        d+=fac*(du-l*u)
        # On |w-s|<=1/4, Re w>=0 and |w+j|<=100 for j=0,...,11
        # at all four witness points. |B12(periodic)|<1.
        # Integral remainder <= 100^12 q^11 x^(-11)/(11*12!).
        r=iv.mpf(100)**12*(q/x)**11/(11*factorial(12))
        v+=discbox(r)
        d+=discbox(4*r)
    return v,d
B=[0,1,0,-1]
R=[0,1,-1,-1,1]
T=[B[j%4]*R[j%5] for j in range(20)]
def psi(w):
    W=w+100
    # Compare sum 1/(W+j) with integral on each unit interval.
    # Sum-integral discrepancy <= integral_0^inf |W+x|^-2 dx.
    return iv.log(W)-sum(1/(w+j) for j in range(100))+discbox(1/W.real)
def h(t,y,name):
    s=iv.mpf('.5')+y-I*t
    if name=='DH':
        k=(iv.sqrt(10-2*iv.sqrt(5))-2)/(iv.sqrt(5)-1)
        v,d=L(s,[0,1,k,-k,-1])
        g=(iv.log(5/iv.pi)+psi((s+1)/2))/2
    else:
        a,da=L(s,[1])
        b,db=L(s,B)
        r,dr=L(s,R)
        e,de=L(s,T)
        v=a*e+b*r
        d=da*e+a*de+db*r+b*dr
        g=iv.log(iv.sqrt(5)/iv.pi)+psi(s)+1/s+1/(s-1)
    return I*(g+d/v)
def main():
    for name,t,y,m,n in [('DH','85.6','.2',2,3),('Epstein','52.7','.05',4,3)]:
        t,y=iv.mpf(t),iv.mpf(y)
        a,b=h(t,y,name),h(t+iv.mpf('.1'),y,name)
        cross=((a-iv.mpc(b.real,-b.imag))/(-iv.mpf('.1')+2*I*y)).real
        Q=(m*m*a.imag/y+2*m*n*cross+n*n*b.imag/y)/(m*m+n*n)
        print(name,Q)
        assert Q.b<0

if __name__=='__main__': main()
