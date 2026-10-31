# Exact endpoint Hardy-Schur absorption of the first three prime-power atoms

2026-10-31, Codex / GPPDiscovery2. **Stronger than the earlier
`L<=57/50` relative-energy prime bound**: this is an unconditional
all-test-function **additive coercive estimate** for the entire
arithmetic source against the completed Archimedean kinetic.
It is not yet positivity of the full Weil form and does not prove RH.

## Theorem

For every `0<L<=38/25=1.52` and every admissible complex test function
`f` supported on `[0,L]`, define the exact kinetic and prime terms

    q(y) = 2 Re integral_R conj(f(x)) f(x+y) dx,
    E_L[f] = integral_0^infinity (q(0)-q(y))/(2 sinh(y)) dy,
    S_L[f] = sum_(p^r <= exp L) (log p)/sqrt(p^r) q(r log p).

Then

    E_L[f] - S_L[f] >= (1/125) ||f||².                 (T1)

At every `0<L<=3/2` the stronger estimate holds:

    E_L[f] - S_L[f] >= (3/100) ||f||².                (T2)

All genuine arithmetic atoms `p^r=2,3,4` below `exp(38/25)` are included.
The proof works for infinitely many modes and uses **no truncation**, no
global RH assumption, and no two-sided operator norm.

## Exact boundary Hardy weight

For any support `[0,L]` let `H(z)=log coth(z/2)` and

    V_L(x) = (H(x)+H(L-x))/2,          0<x<L.

For every shift y>0,

    q(0)-q(y) = integral_R |f(t+y)-f(t)|² dt.

The zero-extension regions outside the left support and beyond the
right support are disjoint and contribute at least

    integral_0^min(y,L) |f(x)|² dx
     + integral_max(0,L-y)^L |f(x)|² dx.

Integrating this pointwise bound against `dy/(2sinh y)` and using
`int_z^infinity csch(y)dy = H(z)` proves the **Hardy potential inequality**

    E_L[f] >= integral_0^L V_L(x)|f(x)|² dx.          (H)

This is an exact positive boundary payment from the **actual complete
infinite gamma tail**, not an imposed extra boundary condition.

## A pointwise prime graph degree

Let `a_n=log(n)`, `w_n=(log p)/sqrt(n)` for a prime power `n=p^r`
with `n<=exp L`. The term at a_n only couples `[0,L-a_n]` to
`[a_n,L]`:

    |q(a_n)| <= integral_0^L
          (1_{x<=L-a_n}+1_{x>=a_n}) |f(x)|² dx

by the simple exact SOS `2|ab|<=|a|²+|b|²`. Thus define

    d_L(x) = sum_(p^r<=exp L) w_(p^r)
             (1_{x<=L-a_(p^r)}+1_{x>=a_(p^r)}).

Then the **entire** signed prime sum obeys

    |S_L[f]| <= integral_0^L d_L(x)|f(x)|² dx.        (P)

Consequently the single pointwise condition

    V_L(x)-d_L(x) >= delta for all x in (0,L)       (C)

implies `E_L[f]-S_L[f]>=delta||f||²` for all complex f.

## Four exact scalar endpoint checks

Set endpoint `L0=38/25`, so `log4<L0<log5`, and put

    w2=log(2)/sqrt(2), w3=log(3)/sqrt(3), w4=log(2)/2.

By symmetry `V_L0(x)=V_L0(L0-x)` and
`d_L0(x)=d_L0(L0-x)`, it suffices to check `0<x<=L0/2`.
`H'(x)=-csch(x)`, so `V_L0` is strictly decreasing on this half.
The active prime graph degree is piecewise constant:

    x in [0,L0-log4]            : d = w2+w3+w4
    x in (L0-log4,L0-log3]     : d = w2+w3
    x in (L0-log3,log2)        : d = w2
    x in [log2,L0/2]           : d = 2*w2.

Therefore the minimum of `V_L0-d_L0` over each interval occurs at
its right endpoint. There are exactly **four scalar checks**, all
certified with outward-rounded FLINT/Arb 256-bit ball arithmetic:

| Right endpoint | Degree | Arb lower gap (displayed midpoint) |
|---|---|---|
| `L0-log4` | `w2+w3+w4` | `0.137801057051906975...` |
| `L0-log3` | `w2+w3` | `0.008157935828392378...` |
| `log2` from the left | `w2` | `0.528217625829850200...` |
| `L0/2` | `2*w2` | `0.033900500580736161...` |

The minimum certified margin is **strictly bigger than 1/125=0.008**.
With `L0=3/2`, the same four checks give respective margins
`0.21860908335`, `0.03179835658`, `0.53919793775`, and
`0.04596632769`, each **strictly above 3/100**.

The inequalities extend to every `0<L<L0`: for fixed `t=x/L`, the
Hardy weight `V_L(tL)` decreases with L, while each prime degree
indicator `1_{t<=1-a_n/L}+1_{t>=a_n/L}` is nondecreasing with L,
with new prime powers entering at nonnegative weight. Thus

    V_L(tL)-d_L(tL) >= V_L0(tL0)-d_L0(tL0) >= delta.

This completes the infinite-dimensional theorem for all support lengths.

**Reproducer:** `discovery/prime_arch_endpoint_schur.py`, run under
`python-flint==0.9.0` (same version as the Discovery2 CI workflow).

## Remaining obstacle, precisely

The exact corrected completed Weil form is

    Q_L[f]=(E_L[f]-S_L[f]) + P_L[f]
          -(log(4pi)+EulerGamma)||f||² - A_L[f].

The estimate just proved makes **the full signed arithmetic component
harmless relative to the positive gamma kinetic on L<=1.52**, even
after the first three true prime-power atoms have activated. However
`1/125` is less than the contact subtraction constant, so it does not
give `Q_L[f]>=0` at these larger L. Our previous full-Q positivity
theorem continues to cover only `0<L<=5/32`.

The next target is a pole/moment-aware stronger kinetic inequality,
perhaps a block Schur complement using the exact pole decomposition
`P_L=2|int f cosh((x-L/2)/2)dx|² -
2|int f sinh((x-L/2)/2)dx|²`, which keeps the large positive channel
coupled to the near-constant test modes. Do not upgrade the current
prime-absorption result to a global Weil positivity or RH assertion.
