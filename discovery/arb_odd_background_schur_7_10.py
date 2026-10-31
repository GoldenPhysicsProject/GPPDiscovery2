"""256-bit Arb proof gate: prime-omitted completed Weil Q0[f] >= 1/100 ||f||² on MIRROR-ODD tests
for EVERY admissible complex f on any logarithmic support on the fixed logarithmic support L=7/10.

This tests exact gamma surplus J_gamma >= J0 + (11*L/50) Var,\n20th-order Hardy curvature plus Legendre Jacobi
finite-band low/high Schur. Derivation in the adjacent mathematical note.
Not RH: L=0.7 > log2, and the actual prime source is DELIBERATELY omitted. This proves no positivity of the true prime-inclusive completed Weil form.
"""
from flint import arb,ctx,fmpq
from math import factorial
ctx.prec=256
q=lambda n,d=1:arb(fmpq(n,d))
Z=q(0)
L=q(7,10);R=10
eta=q(1,100000);kap=q(1,100)
assert L > arb(2).log()
beta=-(L/4).tanh().log()-((L/4).exp()-1)-(4*arb.pi()).log()-arb.const_euler()

def odd_power_polynomial(m):
    # Sum_(j>=0) (2j+1)^m x^j = P_m(x)/(1-x)^(m+1).
    # P_(m+1) = [1+(2m+1)x]P_m+2x(1-x)P'_m.
    P=[1]
    for j in range(m):
        O=[0]*(len(P)+1)
        for k,v in enumerate(P):
            O[k]+=v
            O[k+1]+=(2*j+1)*v
            if k:
                O[k]+=2*k*v
                O[k+1]-=2*k*v
        while len(O)>1 and O[-1]==0:O.pop()
        P=O
    return P

def even_H_derivative(r):
    z=L/2
    x=(-2*z).exp()
    p=odd_power_polynomial(2*r-1)
    v=sum((q(coeff)*x**i for i,coeff in enumerate(p)),Z)
    return 2*(-z).exp()*v/(1-x)**(2*r)

def a(n):
    assert n>=1
    return q(n)/(q(2*n-1)*q(2*n+1)).sqrt()

D=4*R+3
M=[[Z for j in range(D)] for i in range(D)]
for n in range(D-1):
    M[n][n+1]=M[n+1][n]=a(n+1)/2

def product(X,Y):
    return [[sum((X[i][k]*Y[k][j] for k in range(len(Y))),Z)
            for j in range(len(Y[0]))] for i in range(len(X))]

T2=product(M,M)
potential=[[Z for j in range(D)] for i in range(D)]
current=[[q(1) if i==j else Z for j in range(D)] for i in range(D)]
for r in range(1,R+1):
    current=product(current,T2)
    K=(L**(2*r))*even_H_derivative(r)/q(factorial(2*r))
    assert K>0
    print('Hardy curvature degree',2*r,'coefficient positive:',K)
    for i in range(D):
        for j in range(D):
            potential[i][j]+=K*current[i][j]

def harmonic(n):
    return sum((q(1,j) for j in range(1,n+1)),Z)

def certify_ldl(A,name):
    A=[row[:] for row in A]
    piv=[]
    for i in range(len(A)):
        d=A[i][i]
        assert d>0,(name,i,d)
        piv.append(d)
        for j in range(i+1,len(A)):
            for k in range(i+1,len(A)):
                A[j][k]-=A[j][i]*A[i][k]/d
    print(name,'strict Arb LDL pivots count:',len(piv))
    print(name,'smallest pivot midpoint diagnostic:',min(float(x.mid()) for x in piv))
    return piv

def schur(M,C,h):
    assert h>kap
    return [[M[i][j]-(kap if i==j else Z)
             -sum((C[i][k]*C[j][k] for k in range(len(C[0]))),Z)/(h-kap)
             for j in range(len(M))] for i in range(len(M))]

# True positive cosh pole, with a rigorous residual bound after e0,e2.
c0=4*(L/4).sinh()/L.sqrt()
c2=(5*L).sqrt()*(4*(L/4).sinh()/L-48*(L/4).cosh()/L**2
                 +192*(L/4).sinh()/L**3)
Uc=L*((L/4)**4*(L/4).cosh()/24)**2
pen=2*(1/eta-1)*Uc
even=[2*i for i in range(R+1)]
even_high=[2*i for i in range(R+1,2*R+1)]
cvec=[c0 if i==0 else c2 if i==2 else Z for i in even]
E=[[ (beta+harmonic(i)+(11*L/50 if i>=1 else Z)-(pen if i>=4 else Z) if i==j else Z)
      +potential[i][j]+2*(1-eta)*cvec[u]*cvec[v]
     for v,j in enumerate(even)] for u,i in enumerate(even)]
Ce=[[potential[i][j] for j in even_high] for i in even]
he=beta+harmonic(2*R+2)+11*L/50-pen
print('Mirror-even background Schur not claimed; it is not positive in this coarse model.')

# True negative sinh pole, bounded below globally, odd parity decouples.
s2=(L/2).sinh()-L/2
odd=[2*i+1 for i in range(R)]
odd_high=[2*i+1 for i in range(R,2*R)]
O=[[ (beta+harmonic(i)+11*L/50-2*s2 if i==j else Z)+potential[i][j]
     for j in odd] for i in odd]
Co=[[potential[i][j] for j in odd_high] for i in odd]
ho=beta+harmonic(2*R+1)+11*L/50-2*s2
odp=certify_ldl(schur(O,Co,ho),'odd')
print('CERTIFIED: MIRROR-ODD PRIME-OMITTED completed Q0[f] >= 1/100 ||f||²')
print('for ALL reflection-odd complex f on the FIXED interval L=7/10.')
print('Entire odd infinite tail controlled. Actual p2 arithmetic source is NOT included; no RH.')
