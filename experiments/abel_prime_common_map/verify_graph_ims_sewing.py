"""Exact rational finite-graph IMS identity for gamma/prime jump channels.

Not a zeta Weil full-positivity certificate; algebraic test only.
"""
from fractions import Fraction as Q
f=[Q(3,7),-Q(4,5),Q(9,11),Q(2,3)]
chi=[(Q(1),Q(0)),(Q(3,5),Q(4,5)),(Q(3,5),Q(4,5)),(Q(0),Q(1))]
assert all(a*a+b*b==1 for a,b in chi)
edges=[(0,1,Q(3,2)),(1,2,Q(7,5)),(2,3,Q(11,7)),(0,3,Q(2,9))]
E=lambda u:sum(w*(u[i]-u[j])**2 for i,j,w in edges)
pieces=[[f[i]*chi[i][k] for i in range(4)] for k in (0,1)]
d=sum(E(u) for u in pieces)-E(f)
R=sum(w*f[i]*f[j]*sum((chi[i][k]-chi[j][k])**2 for k in (0,1))
      for i,j,w in edges)
assert d==R
P=lambda u:sum(-2*w*u[i]*u[j] for i,j,w in edges)
assert sum(P(u) for u in pieces)-P(f)==R
print("PASS exact rational gamma / prime IMS graph algebra; cost",R)
print("Mock graph only; NO RH/ARP/Weil full positivity certificate")
