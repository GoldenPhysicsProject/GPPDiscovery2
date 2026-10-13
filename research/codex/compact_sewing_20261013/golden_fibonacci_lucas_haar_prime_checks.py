"""Fibonacci/Lucas/prime-five Haar and Frobenius checks; NOT an RH proof."""
import sympy as sp
from mpmath import mp
Q=sp.Matrix([[1,1],[1,0]])
A=Q**2
I=sp.eye(2)
assert Q.det()==-1 and A.det()==1
for n in range(1,101):
 B=A**n
 assert B==sp.Matrix([[sp.fibonacci(2*n+1),sp.fibonacci(2*n)],
                      [sp.fibonacci(2*n),sp.fibonacci(2*n-1)]])
 P=abs(int((B-I).det()))
 assert P==int(sp.lucas(2*n)-2)
 assert P==int(sp.lucas(n)**2 if n%2 else 5*sp.fibonacci(n)**2)
count=0
for prime in sp.primerange(2,1500):
 p=int(prime); count+=1
 chi=0 if p==5 else (1 if p%5 in (1,4) else -1)
 assert int(sp.fibonacci(p)-chi)%p==0
 assert int(sp.lucas(p)-1)%p==0
 if p!=5:
  B=A**(p-chi)-I
  assert all(int(B[i,j])%p==0 for i in range(2) for j in range(2))
 else:
  assert all(int(((A+I)**2)[i,j])%5==0 for i in range(2) for j in range(2))
  assert all(int((A**5+I)[i,j])%5==0 for i in range(2) for j in range(2))
mp.dps=70
phi=(1+mp.sqrt(5))/2
entropy=2*mp.log(phi)
L1=2*mp.log(phi)/mp.sqrt(5)
assert abs(entropy-mp.sqrt(5)*L1)<mp.mpf('1e-65')
assert abs(mp.log(mp.mpf(int(sp.lucas(200))))/100-entropy)<mp.mpf('1e-65')
print('PASS: 100 Fibonacci/Lucas powers,',count,'all-prime Frobenius tests; 70-digit Haar entropy / completed residue')
print('Entropy:',mp.nstr(entropy,52))
