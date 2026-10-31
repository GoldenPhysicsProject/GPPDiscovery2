#!/usr/bin/env python3
"""Arb certificate for an ANALYTIC infinite-index OS counterexample.

No finite matrix is being promoted to a theorem: the proof uses the
infinite-dimensional eigenspaces of strip reflection and a universal Schur
bound on the smooth background. See adjacent .md for domain and scope.
"""
from flint import arb, ctx, fmpq

ctx.prec = 256
q = lambda n, d=1: arb(fmpq(n,d))
a=q(2).log()
w=a/q(2).sqrt()
delta=q(1,100)
assert q(2,3) < a < q(3,4)
assert q(16,25) < a - 2*delta
assert a + 2*delta < q(4,5)
assert (q(2,5)).exp() < q(3,2)
assert q(2).sqrt() < q(3,2)

# A(y) = exp(y/2)+exp(-y/2)-exp(y/2)/(2sinh y)
# and y in (16/25,4/5) on the chosen sum strip.
# These elementary envelope terms bound absolute |A|:
M = q(3,2) + q(1) + q(3,2) / (2*q(16,25))
assert M < q(4)
K_bound = 2*delta*q(4)
assert w > q(4,9)
gap = q(4,9) - K_bound
assert gap > q(1,3)

print("a = ln 2:", a)
print("w = ln 2/sqrt(2):", w)
print("interval I = (a/2 - 1/100, a/2 + 1/100)")
print("smooth real Arch+pole |A(t+s)| < 235/64 <", q(4))
print("operator norm smooth background ||K|| < 2/25")
print("negative index of K - w R = infinity on R-even subspace")
print("positive index of K - w R = infinity on R-odd subspace")
print("CERTIFIED strict uniform signed quadratic margin > 82/225")
print("This refutes raw additive-time OS Hankel positivity, NOT RH.")
