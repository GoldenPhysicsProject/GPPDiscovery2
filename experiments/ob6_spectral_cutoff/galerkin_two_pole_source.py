"""Uncertified source-only sine Galerkin for OB6 at L=0.72, prime=2 window.
Numerics guide the Schur pilot; finite matrices do NOT prove continuum positivity or RH.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh
L=.72
CINF=-5.3721834192256655822329574974497423
PRIMES=[2,3,5,7,11]
THETA=sum(math.log(p) for p in PRIMES)
T2=math.log(2)
w=lambda t: math.exp(-t/2)/(-math.expm1(-2*t))
U=math.exp(-L/2)
ARCH_TAIL=2*(math.atanh(U)+math.atan(U))

def gram(n,t):
    k=n*math.pi/L
    return (1-t/L)*math.cos(k*t)+math.sin(k*t)/(k*L)

def sym_shift(n,m,t):
    if n==m:return gram(n,t)
    if (n+m)%2:return 0.0
    k=n*math.pi/L; h=m*math.pi/L
    return 2*(k*math.sin(h*t)-h*math.sin(k*t))/(L*(k*k-h*h))

def pole_moment(n,kind):
    factor=math.sqrt(2/L); k=n*math.pi/L
    sh=lambda x: math.sinh((x-L/2)/2)
    ch=lambda x: math.cosh((x-L/2)/2)
    f=ch if kind=='c' else sh
    return quad(lambda x:factor*math.sin(k*x)*f(x),0,L,epsabs=1e-12)[0]

def energy(n,m):
    diag=(n==m)
    def integ(t):
        if t==0:return 0.
        a=sym_shift(n,m,t)
        return 2*w(t)*((1-a) if diag else -a)
    v=quad(integ,0,L,epsabs=3e-10,epsrel=2e-10,limit=200,points=[min(L,1e-3)],full_output=1)[0]
    return v+(ARCH_TAIL if diag else 0.0)

def build(M,return_matrices=False):
    E=np.empty((M,M));prime=np.empty((M,M))
    for i in range(M):
        for j in range(i,M):
            e=energy(i+1,j+1);E[i,j]=E[j,i]=e
            q=sym_shift(i+1,j+1,T2)
            prime[i,j]=prime[j,i]=q
    uc=np.array([pole_moment(i+1,'c') for i in range(M)])
    us=np.array([pole_moment(i+1,'s') for i in range(M)])
    P=2*(np.outer(uc,uc)-np.outer(us,us))
    G=E+(THETA+CINF)*np.eye(M)
    B=G+P
    V=THETA*np.eye(M)+2*math.log(2)/math.sqrt(2)*prime
    W=B-V
    assert np.allclose(W,E+CINF*np.eye(M)+P-2*math.log(2)/math.sqrt(2)*prime,atol=1e-12)
    assert np.linalg.eigvalsh(B)[0]>0
    Z=np.column_stack((uc,us));J=np.diag([2.,-2.])
    BW=np.linalg.inv(G)-np.linalg.inv(G)@Z@np.linalg.inv(np.linalg.inv(J)+Z.T@np.linalg.inv(G)@Z)@Z.T@np.linalg.inv(G)
    assert np.max(abs(BW-np.linalg.inv(B)))<2e-12
    lam=eigh(V,B,eigvals_only=True)
    if return_matrices:return B,V,W,E
    return lam[-1],np.linalg.eigvalsh(W)[0],np.linalg.eigvalsh(E)[0]

if __name__=='__main__':
    for M in [4,8,12,20,32,48,64,100]:
        mx,wmin,emin=build(M)
        print(f'M={M:3d} max normalized gram={mx:.14g} defect=1-lambda={1-mx:.8g} min W={wmin:.8g} min E={emin:.8g}')
    B,V,W,E=build(100,True)
    low=6; A=W[:low,:low]; H=W[low:,low:]; X=W[:low,low:]
    assert np.linalg.eigvalsh(H)[0]>0
    S=A-X@np.linalg.solve(H,X.T)
    print('100-mode 6-vs-94 Schur min eigen',np.linalg.eigvalsh(S)[0],
          'high block bottom',np.linalg.eigvalsh(H)[0])
    print('NO CERTIFICATE: finite compression gives a lower bound on the infinite top eigenvalue')
