# Strict KL orientation from the positive third cumulant

Codex/GPT discovery track, 2026-08-25.

On beta>1 the zeta Gibbs Fisher metric satisfies

g'(beta)=-kappa_3(beta)<0,

so g is strictly decreasing.

For beta<gamma, the exact triangular representations are

D(beta||gamma)=int_beta^gamma (gamma-x) g(x) dx,

D(gamma||beta)=int_beta^gamma (x-beta) g(x) dx.

Let

m=(beta+gamma)/2,
L=(gamma-beta)/2.

Pair points x=m-y and x=m+y. The difference becomes

D(beta||gamma)-D(gamma||beta)
 = 2 int_0^L y [g(m-y)-g(m+y)] dy.

For every y in (0,L), strict decrease of g gives

g(m-y)>g(m+y).

Hence the integrand is strictly positive away from y=0 and therefore

boxed:

D(beta||gamma) > D(gamma||beta),   1<beta<gamma.

Thus the information geometry has a definite thermodynamic orientation: moving from the lower-inverse-temperature distribution to the higher-inverse-temperature one costs more relative entropy than the reverse comparison.

Locally,

D(beta||beta+delta)-D(beta+delta||beta)
 = -(1/6) g'(beta) delta^3 + O(delta^4)
 = (1/6) kappa_3(beta) delta^3 + O(delta^4) > 0,

consistent with the exact inequality.

This asymmetry is controlled by the positive third cumulant of log n and is restricted entirely to the honest Gibbs domain beta>1.
