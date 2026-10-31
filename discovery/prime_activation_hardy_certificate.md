# The first two prime atoms are form-dominated by completed Archimedean kinetic energy

2026-10-31, Codex / GPPDiscovery2. **Unconditional analytic theorem** with
one outward-rounded Arb scalar inequality. This is a genuinely
prime-inclusive, all-test-function estimate on the **corrected** semilocal
Weil quadratic form. It is not completed Weil positivity and not RH.

## Theorem

For every `0<L<=57/50=1.14` and every complex `L²` test function `f`
supported in `[0,L]` with finite logarithmic kinetic energy, let

    q_f(y) = 2 Re integral_R conj(f(x)) f(x+y) dx,
    E_L[f] = integral_0^infinity (q_f(0)-q_f(y))/(2 sinh y) dy,
    S_L[f] = sum_(p^r <= exp L) log(p)/sqrt(p^r) q_f(r log p).

Then **all prime-power atoms actually present** are absorbed by positive
Archimedean kinetic energy:

    |S_L[f]| <= K(L) E_L[f] <= K(57/50) E_L[f]
    K(57/50) < 0.974098 < 1.

In particular,

    E_L[f] - S_L[f] >= (1-K(57/50)) E_L[f]
                    >= 0.025902 E_L[f] >= 0.

For L in `(log 3,57/50]`, the only atoms are p=2 and p=3; below log3
there is only p=2 or no atom. The exact Arb value is

    K(57/50) = 0.97409707495124296475951365019470365...
    1-K(57/50) = 0.02590292504875703524048634980529634...

This gives **noncircular** sign-safe prime/Arch cancellation for the
first two prime atoms, across the entire continuum of modes N, despite
the failure of absolute operator norm and Gershgorin on larger windows.

## Proof: boundary Hardy charge for an activated arithmetic atom

Fix any shift `0<a<L`, set `epsilon=L-a>0`, and denote the two support
end strips by

    A = [0,epsilon],   B = [L-epsilon,L] = [a,L],
    M_epsilon[f] = integral_A |f|² + integral_B |f|².

The signed autocorrelation at shift a has overlap only between these
two strips, so Cauchy-Schwarz and 2uv<=u²+v² show

    |q_f(a)| <= M_epsilon[f].                           (1)

For every `y>=epsilon`, in the full translated-difference integral

    q_f(0)-q_f(y) = integral_R |f(t+y)-f(t)|² dt,

the region `t in [-y,epsilon-y]` (outside the left support) contributes
`integral_A |f|²`; independently, `t in [a,L]` (rightmost strip with
`t+y >= L`) contributes `integral_B |f|²`. The regions are disjoint.
Thus **pointwise for all y>=epsilon**:

    q_f(0)-q_f(y) >= M_epsilon[f].                    (2)

Integrate (2) against the exact positive kinetic measure:

    E_L[f] >= (M_epsilon[f]/2) integral_epsilon^infinity csch y dy
           = (M_epsilon[f]/2) log coth(epsilon/2).

Combining with (1) gives the exact, uniform first-prime activation
estimate

    |q_f(a)| <= [2/log coth((L-a)/2)] E_L[f].         (3)

In particular the prime term becomes **infinitesimally form-small** as
its shift enters the support (`L downarrow a`): its relative constant
is O(1/log(2/(L-a))). This is stronger than the discontinuous crude
operator-norm estimate `|q_f(a)|<=2||f||²`, and even stronger than the
pointwise finite-nilpotent bound when epsilon is tiny.

For all prime powers `n=p^r` with `log n<L` put

    w_n = log p/sqrt(n),
    kappa_n(L) = 2 w_n / log coth((L-log n)/2),
    K(L) = sum_(p^r < exp L) kappa_(p^r)(L).

By (3), triangle inequality and positivity of E,

    |S_L[f]| <= K(L) E_L[f].                         (4)

Each `kappa_n` is strictly increasing for L>log n and tends to 0 at its
activation point. Hence K is nondecreasing across all prime-power
thresholds. Since `log 3 < 57/50 < log 4`, only the exact p=2 and p=3
terms need verification at the rational endpoint. FLINT/Arb 256-bit
interval arithmetic certifies:

    kappa_2(57/50) = 0.6469830502271198218124305469...
    kappa_3(57/50) = 0.3271140247241231429470831033...
    K(57/50) < 1.

The computation can be reproduced with
`discovery/prime_activation_hardy_certificate.py` on the Discovery2
workbench; run it alongside the short-support Arb certificate in CI.

## Meaning for the remaining RH positivity obstruction

In the corrected completed decomposition

    Q_L[f] = (E_L[f]-S_L[f]) + P_L[f]
             - (log(4pi)+EulerGamma)||f||² - A_L[f],

the **entire signed arithmetic source** is now paid for by a provably
positive Archimedean term on `0<L<=1.14`. This does **not** control
the negative subtraction/contact term nor the indefinite rank-two pole
in this larger window. The previous stronger completed Q>0 theorem
is proved only on `0<L<=5/32`. There is no claim of Weil positivity at
L=1.14 and no RH claim.

The next precise task is a pole-aware kinetic inequality on `[0,1.14]`
that keeps the pole's positive rank-one channel instead of replacing
the whole pole with its very small negative eigenvalue. This may allow
noncircular sewing across the first prime events; the current crude
global lower bound B_40 already fails before those events.
