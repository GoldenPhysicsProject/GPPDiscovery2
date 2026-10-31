"""Proof-carrying infinite-tail Arb Schur certificate for the completed Weil form.

Target: L=1/2=.5, all complex functions, no prime atoms.
Analytic operator comparison, see adjacent .md:
 Q >= D+W+2(1-eta)|c2><c2|, D_n=H_n+beta-alpha,
 where W=k2(z/2)^2+k4(z/2)^4 is nonnegative multiplication,
 and Jgamma >= J0+(L/6)||f-mean(f)||² because w(y)>=1/(2y)+1/6.
 z=2x/L-1, P_n the normalized shifted Legendre eigenbasis of J_gamma>=J0.
 c2(x)=1+(x-L/2)^2/8 is a quadratic approximation to cosh pole
 with uniform positive remainder e<=cosh(L/4)(L/4)^4/24; alpha includes
 pole remainder penalty and entire negative sinh pole norm.
 Multiplication z is exactly a Jacobi tridiagonal operator,
 J_(n,n+1)=(n+1)/sqrt((2n+1)(2n+3)).
 W therefore has bandwidth 4. Split low n=0..N-1 and high n>=N:
 C_high>=d I, d=H_N+beta-alpha. Cross B has ONLY four high columns
 n=N..N+3; it is assembled exactly by Jacobi matrix powers.
 A sufficient all-mode bound Q>=delta I is:
 d>delta and A_low-delta I-B B^T/(d-delta)>0.
 The last finite matrix is rigorously LDL-certified by FLINT Arb.
 NO Galerkin extrapolation: all omitted modes are covered by the
 analytic high-tail inequality and exact finite-rank cross bound.
"""
from flint import arb,ctx,fmpq
ctx.prec=256
q=lambda a,b=1:arb(fmpq(a,b))
L=q(1,2)
N=12
eta=q(1,1000)
delta=q(1,10000)
c=(4*arb.pi()).log()+arb.const_euler()
a=L/2
beta=-(L/4).tanh().log()-((L/4).exp()-1)-c
h2=a.cosh()/a.sinh()**2
h4=(a.cosh()**2+5)*a.cosh()/a.sinh()**4
k2=L**2*h2/2
k4=L**4*h4/24
eps=(L/4).cosh()*(L/4)**4/24
s2=(L/2).sinh()-L/2
alpha=2*s2+2*(1/eta-1)*L*eps**2
assert 0<L<arb(2).log() and L<1
assert eps>0 and s2>0 and alpha>0

M=N+6
zero=arb(0)
J=[[zero for j in range(M)] for i in range(M)]
for n in range(M-1):
    j=arb(n+1)/(arb((2*n+1)*(2*n+3))).sqrt()
    J[n][n+1]=j
    J[n+1][n]=j

def mm(A,B):
    t=len(A); k=len(B); m=len(B[0])
    return [[sum((A[i][h]*B[h][j] for h in range(k)),arb(0))
             for j in range(m)] for i in range(t)]

J2=mm(J,J)
J4=mm(J2,J2)
W=[[k2*J2[i][j]/4+k4*J4[i][j]/16 for j in range(M)] for i in range(M)]
H=[arb(0)]
for n in range(1,M):
    H.append(H[-1]+q(1,n))
cvec=[arb(0)]*M
cvec[0]=L.sqrt()*(1+L**2/96)
cvec[2]=L.sqrt()*L**2/(48*arb(5).sqrt())

A=[[W[i][j]+(H[i]+(L/6 if i>0 else arb(0))+beta-alpha if i==j else arb(0))+
     2*(1-eta)*cvec[i]*cvec[j]
     for j in range(N)] for i in range(N)]
B=[[W[i][N+j] for j in range(4)] for i in range(N)]
d=H[N]+L/6+beta-alpha
assert d>delta
S=[[A[i][j]-(delta if i==j else arb(0))-
    sum((B[i][k]*B[j][k] for k in range(4)),arb(0))/(d-delta)
    for j in range(N)] for i in range(N)]

# Interval LDL pivots: a strictly positive ball at every pivot suffices.
pivots=[]
T=[row.copy() for row in S]
for k in range(N):
    pivot=T[k][k]
    assert pivot>0, ('Schur LDL pivot nonpositive/ambiguous',k,pivot)
    pivots.append(pivot)
    for i in range(k+1,N):
        for j in range(k+1,N):
            T[i][j] -= T[i][k]*T[k][j]/pivot
print('COMPLETE Weil full all-mode positivity certificate, L=1/2 prime-free')
print('beta=',beta,' k2=',k2,'k4=',k4)
print('cosh-tail pointwise bound=',eps,'alpha=',alpha)
print('high-tail lower d=',d,'target delta=',delta,'d-delta=',d-delta)
print('low Schur 12x12 interval LDL pivot min lower certificate')
for i,pivot in enumerate(pivots):
    print('pivot',i,pivot)
print('CERTIFIED: for every complex finite-energy test function with '
      'support <=1/2, full corrected Q[f]>=1/10000||f||²; '
      'no primes; RH/global positivity remains OPEN.')
