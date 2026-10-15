#!/usr/bin/env python3
"""Interval lower certificate for primitive chi_4's first prime-active window.

Golden Physics Project / Daniel Toupin; Codex/GPT, October 15 2026.
Ground-state comparison is exact. mpmath.iv supplies elementary function
intervals; independent Arb replication/Lean check still requested.
No global GRH/RH claim. This is NOT a Ritz upper-bound experiment.
"""
from mpmath import iv

iv.dps = 55
h = iv.ln(3)/2
k = iv.mpf(19)/10
N = 15
cells = 100
a = [iv.mpf(3)/2 + 2*j for j in range(N)]
s = [aj*iv.cos(k*h)-k*iv.sin(k*h) for aj in a]
assert s[0].b < 0
assert all(v.a > 0 for v in s[1:])
assert iv.cos(k*h).a > 0

# Exact first N positive rational diagonal contributions.
diagonal = sum((2*k*k/(aj*(aj*aj+k*k)) for aj in a), iv.mpf(0))

def boundary(j, x):
    aj=a[j]
    # exp(-aj*h)cosh(aj*x) written without overflow
    return ((iv.exp(-aj*(h-x))+iv.exp(-aj*(h+x)))*s[j] /
            ((aj*aj+k*k)*iv.cos(k*x)))

enclosures = []
for i in range(cells):
    L = h*i/cells
    U = h*(i+1)/cells
    # b_0 decreases; b_j with j>=1 increases on 0<=x<=h.
    # The omitted j>=15 full contributions are nonnegative.
    bound = diagonal+boundary(0,U) + sum(
        (boundary(j,L) for j in range(1,N)),iv.mpf(0))
    enclosures.append(bound)

index = min(range(cells),key=lambda j:float(enclosures[j].a))
worst = enclosures[index]
target = iv.ln(2*iv.pi)+iv.euler-iv.pi/2
assert all(v.a>iv.mpf('0.87') for v in enclosures)
assert worst.a > target.b + iv.mpf('0.025')
print('h=(log3)/2:',h)
print('k:',k)
print('worst cell:',index)
print('ground-state lower enclosure:',worst)
print('c1-log4:',target)
print('safe result: Q_chi4(g) > 0.025 * ||g||^2, |supp g|<=(log3)/2')
print('STATUS: interval-assisted finite-window proof, independent Arb audit requested')
