"""RIGOROUS all-function first-four-prime Hardy-Schur certificate through L=83/50.

All decisive checks are exact rational comparisons. Arb 256-bit interval balls
verify the only transcendental inputs (logarithms, square roots, boundary
potential). The floating iteration ONLY finds a rational witness; no float
quantity enters the final proof check. Positive step profile h on 256 rational
cells satisfies A_prime h < (99/100) V h, uniformly pointwise a.e.

Consequently E_L[f]-S_L[f] >= (1/250)||f||² for ALL complex supported
f at L=83/50, and every shorter support by zero extension. True atoms
2,3,4,5 are included. NOT completed Weil positivity or RH.
"""
from fractions import Fraction as F
from math import floor, ceil, sqrt, log, tanh

from flint import arb, ctx, fmpq

ctx.prec = 256
L = F(83, 50)
M = 512
dx = L / M
rho = F(99, 100)
WITNESS_DENOM = 10**6


def ar(q):
    return arb(fmpq(q.numerator, q.denominator))


def dec(s):
    return F(s)


shifts = {
    2: (dec('0.693147180559'), dec('0.693147180561')),
    3: (dec('1.098612288667'), dec('1.098612288670')),
    4: (dec('1.386294361119'), dec('1.386294361121')),
    5: (dec('1.609437912433'), dec('1.609437912435')),
}
primes = {2: 2, 3: 3, 4: 2, 5: 5}
Larb = ar(L)
assert arb(5).log() < Larb < arb(6).log()
for n, (lo, hi) in shifts.items():
    assert ar(lo) < arb(n).log() < ar(hi)

weights = {}
for n, p in primes.items():
    # Candidate rational upper bound. Exact interval comparison below proves it.
    floating = log(p)/sqrt(n)
    upper = F(ceil((floating + 1e-8)*10**8), 10**8)
    assert ar(upper) > arb(p).log()/arb(n).sqrt()
    weights[n] = upper


def H_arb(z):
    assert z > 0
    return -(z/2).tanh().log()


def H_float(z):
    return -log(tanh(z/2))


Vlower = []
for i in range(M):
    left = i*dx
    right = (i+1)*dx
    # H''>0, V=(H(x)+H(L-x))/2 is symmetric/convex.
    # Thus min on a cell is at its point closest to L/2.
    x = min(max(L/2, left), right)
    candidate = (H_float(float(x))+H_float(float(L-x)))/2
    lower = F(floor((candidate-1e-7)*10**7), 10**7)
    assert lower > 0
    v_exact_ball = (H_arb(ar(x))+H_arb(ar(L-x)))/2
    assert ar(lower) < v_exact_ball, (i, lower, v_exact_ball)
    Vlower.append(lower)


def range_of_possible_cells(lo, hi):
    # Rational enclosure for x +/- log(n); exact floor arithmetic.
    if lo >= L or hi <= 0:
        return ()
    i0 = max(0, lo // dx)
    i1 = min(M-1, hi // dx)
    if i1 < i0:
        return ()
    assert i1-i0 <= 2, 'Unexpected wide shifted enclosure'
    return tuple(range(i0, i1+1))


edges = []
for i in range(M):
    left, right = i*dx, (i+1)*dx
    row = []
    for n,(amin,amax) in shifts.items():
        # Both shift directions: interval enclosures from verified log brackets.
        for lo,hi in ((left+amin, right+amax),
                      (left-amax, right-amin)):
            indices = range_of_possible_cells(lo, hi)
            if indices:
                row.append((weights[n],indices))
    edges.append(row)


def edge_upper_float(h):
    return [sum(float(w)*max(h[j] for j in idx) for w,idx in row)
            for row in edges]


# Discovery phase only. This is NOT the certificate.
h = [1.0] * M
for it in range(350):
    Ah = edge_upper_float(h)
    h = [1.0 + Ah[i]/float(Vlower[i]) for i in range(M)]
assert max(h)<1e10
# Freeze an explicit RATIONAL step function as our final proof witness.
h_rat = [F(round(z*WITNESS_DENOM), WITNESS_DENOM) for z in h]
assert all(z > 0 for z in h_rat)

# Entire analytic interval [0,L] is covered by the exact 256-cell partition.
# Every possible translated target cell was INCLUDED above using certified
# rational log brackets. The following checks are purely exact rational.
minimum_slack = None
worst_index = None
for i,row in enumerate(edges):
    rhs = rho * Vlower[i] * h_rat[i]
    lhs = sum((w*max(h_rat[j] for j in js) for w,js in row),F(0))
    slack = rhs-lhs
    if minimum_slack is None or slack < minimum_slack:
        minimum_slack, worst_index = slack,i
    assert slack > 0, ('Schur certificate failed',i,lhs,rhs)

# Uniform coercive scalar: (1-rho)*min V >= H(L/2)/100 > 1/250.
vfloor = H_arb(Larb/2)
assert vfloor > arb(fmpq(4,5))
assert (arb(1)-ar(rho))*vfloor > arb(fmpq(1,125))
print(f'CERTIFIED: rational support endpoint L={L}, mesh cells={M}, '
      f'prime-power atoms {list(primes)}, rational witness digits=6')
print(f'Exact rational min cell slack: {minimum_slack} at i={worst_index}')
print(f'Arb H(L/2): {vfloor}')
print('ALL f with support within [0,83/50]: E[f]-S[f] > '
      '(1/250)||f||² for f!=0; zero f equality.')
print('Smaller supports follow by zero extension, not an unproved '
      'scale monotonicity of a discontinuous comparison profile.')
print('This DOES NOT prove positivity of completed Q nor RH.')
