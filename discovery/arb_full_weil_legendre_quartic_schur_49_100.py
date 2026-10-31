"""256-bit outward Arb certificate of an INFINITE-dimensional exact Schur
sufficient theorem for the corrected COMPLETED Weil form, L<=49/100.

Analytic proof: discovery/full_weil_legendre_quartic_schur_49_100.md.
This is a PRIME-FREE restricted-support theorem; NOT RH.
"""
from flint import arb, ctx, fmpq
ctx.prec=256
q=lambda n,d=1:arb(fmpq(n,d))
zero=q(0)
L=q(49,100)
eta=q(1,100000)
margin=q(1,1000)
assert L<arb(2).log() and L<1
cst=(4*arb.pi()).log()+arb.const_euler()
z=L/2
Hpp=z.cosh()/z.sinh()**2
H4=z.cosh()*(z.cosh()**2+5)/z.sinh()**4
K2=L*L*Hpp/2
K4=L**4*H4/24
beta=-(L/4).tanh().log()-((L/4).exp()-1)-cst
def harm(n):
    return sum((q(1,j) for j in range(1,n+1)),zero)
def a(n):
    assert n>=1
    return q(n)/(q(2*n-1)*q(2*n+1)).sqrt()
D=12
M=[[zero for _ in range(D)] for _ in range(D)]
for n in range(D-1):
    M[n][n+1]=M[n+1][n]=a(n+1)/2
def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),zero)
             for j in range(len(B[0]))] for i in range(len(A))]
T2=matmul(M,M)
T4=matmul(T2,T2)
def block(T,rows,cols):
    return [[T[i][j] for j in cols] for i in rows]
def exact_ldl(A,name):
    A=[row[:] for row in A]
    pivots=[]
    for i in range(len(A)):
        d=A[i][i]
        print(name,'pivot',i,'=',d)
        assert d>0, (name,i,d)
        pivots.append(d)
        for j in range(i+1,len(A)):
            for k in range(i+1,len(A)):
                A[j][k]-=A[j][i]*A[i][k]/d
    return pivots

# Mirror-even low modes 0,2,4, infinite n>=6.
c0=4*(L/4).sinh()/L.sqrt()
c2=(5*L).sqrt()*(4*(L/4).sinh()/L-48*(L/4).cosh()/L**2
                 +192*(L/4).sinh()/L**3)
Uc=L*((L/4)**4*(L/4).cosh()/24)**2
p=2*(1/eta-1)*Uc
I=[0,2,4];J=[6,8]
cv=[c0,c2,zero]
low=[[ (beta+harm(i)-(p if i==4 else zero) if i==j else zero)
       +K2*T2[i][j]+K4*T4[i][j]+2*(1-eta)*cv[u]*cv[v]
       for v,j in enumerate(I)] for u,i in enumerate(I)]
cross=[[K2*T2[i][j]+K4*T4[i][j] for j in J] for i in I]
high=beta+harm(6)-p
assert high>margin
schur=[[ low[i][j]-(margin if i==j else zero)
        -sum((cross[i][k]*cross[j][k] for k in range(len(J))),zero)/(high-margin)
        for j in range(len(I))] for i in range(len(I))]
print('Even high tail lower=',high,'cosh tail penalty=',p)
pe=exact_ldl(schur,'even')

# Mirror-odd low modes 1,3, infinite n>=5, exact negative sinh pole.
s2=(L/2).sinh()-L/2
I=[1,3];J=[5,7]
low=[[ (beta+harm(i)-2*s2 if i==j else zero)
       +K2*T2[i][j]+K4*T4[i][j]
       for j in I] for i in I]
cross=[[K2*T2[i][j]+K4*T4[i][j] for j in J] for i in I]
highodd=beta+harm(5)-2*s2
assert highodd>margin
schurodd=[[low[i][j]-(margin if i==j else zero)
           -sum((cross[i][k]*cross[j][k] for k in range(len(J))),zero)/(highodd-margin)
           for j in range(len(I))] for i in range(len(I))]
print('Odd high tail lower=',highodd)
po=exact_ldl(schurodd,'odd')
assert pe[1]>q(1,25) and po[0]>q(1,5)
print('CERTIFIED Q[f]>=1/1000 ||f||² for ALL complex admissible tests')
print('on any log-support interval length L<=49/100, complete pole+gamma included.')
print('The prime-power comb is empty here; no RH proof.')
