"""Exact arithmetic checks: prime-five modular boundary (not an RH proof)."""
from fractions import Fraction
from sympy import Matrix, sqrt, simplify, eye
primes=[2,3,5,7,11,13,17,19,23,29,31,37]
assert [p for p in primes if Fraction(2*(p+1),p-1).denominator==1]==[2,3,5]
for p in primes:
    eigen=(sqrt(p)+1)/(sqrt(p)-1)
    assert simplify(eigen+1/eigen-Fraction(2*(p+1),p-1))==0
A=Matrix([[2,1],[1,1]])
S=Matrix([[0,-1],[1,0]])
phi=(1+sqrt(5))/2
assert A.det()==1 and A.trace()==3
assert simplify(phi**2+phi**-2)==3
assert S*S == -eye(2) and S*A*S.inv()==A.inv()
assert all(int(x)%5==0 for x in (A+eye(2))**2)
assert all(int(x-y)%5==0 for x,y in zip(A**5,-eye(2)))
def prod(x,y):
 a,b,c,d=x;e,f,g,h=y
 return ((a*e+b*g)%5,(a*f+b*h)%5,(c*e+d*g)%5,(c*f+d*h)%5)
gens=[tuple(int(z)%5 for z in A), tuple(int(z)%5 for z in S)]
seen={(1,0,0,1)}; queue=list(seen)
while queue:
 current=queue.pop()
 for g in gens:
  nxt=prod(current,g)
  if nxt not in seen:seen.add(nxt);queue.append(nxt)
assert len(seen)==20
print("PASS integral p={2,3,5}, shortest trace3, golden eigenvalue, mod5 Dic5 order20")
