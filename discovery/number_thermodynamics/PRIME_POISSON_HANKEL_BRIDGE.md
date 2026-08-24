# Prime Poisson kernel / Hankel-moment bridge

Codex/GPT discovery track, 2026-08-24.

## Exact identity on the absolute-convergence half-plane

Let a>1 and t be real. From the Euler product,

  -zeta'/zeta(a+it)
  = sum_p log(p) sum_{k>=1} p^{-ka} exp(-i k t log p).

Taking real parts gives

  Re[-zeta'/zeta(a+it)]
  = sum_p log(p) sum_{k>=1} p^{-ka} cos(k t log p).

For 0<r<1, the Poisson kernel is

  K_r(theta)=(1-r^2)/(1-2 r cos(theta)+r^2)
            =1+2 sum_{k>=1} r^k cos(k theta).

Therefore, with r_p(a)=p^{-a},

  Re[-zeta'/zeta(a+it)]
  = (1/2) sum_p log(p) [K_{r_p(a)}(t log p)-1].

This identity is absolutely convergent for a>1. It canonically identifies the convergent-axis logarithmic zeta response with a positive-prime sum of the same local Poisson kernels already used in the finite-prime Weil/positive-type construction.

At t=0,

  -zeta'/zeta(a)
  = (1/2) sum_p log(p) [K_{p^{-a}}(0)-1]
  = sum_p log(p) sum_{k>=1} p^{-ka}.

## Radial derivatives are the Hankel moments

Differentiating termwise for a>=1+epsilon gives, for every integer r>=0,

  (-1)^r d^r/da^r [-zeta'/zeta(a)]
  = sum_p (log p)^(r+1) sum_{k>=1} k^r p^{-ka}
  = sum_{n>=2} Lambda(n) (log n)^r n^{-a}.

Equivalently these are the radial derivatives, at theta=0, of the prime Poisson-kernel family:

  (-1)^r d^r/da^r [-zeta'/zeta(a)]
  = (1/2) sum_p log(p) (-1)^r d^r/da^r [K_{p^{-a}}(0)-1].

Thus the previously identified Hankel moment matrices are not an unrelated positivity gadget. They are the radial-moment Gram matrices of the same local positive-type kernels whose angular variable encodes the finite-prime explicit-formula oscillations.

## Two-variable positive kernel viewpoint

Define

  Phi(a,t) := Re[-zeta'/zeta(a+it)]
            = (1/2) sum_p log(p) [K_{p^{-a}}(t log p)-1],  a>1.

For each fixed a>1, every local summand is positive type as a function of t because its Fourier coefficients are nonnegative:

  K_{p^{-a}}(t log p)-1
  = 2 sum_{k>=1} p^{-ka} cos(k t log p).

Hence Phi(a,.) is a positive sum of positive-type kernels (where convergence is absolute). Along t=0, its alternating a-derivatives are strictly positive and form the Stieltjes/Hamburger-type moment sequence used by the Hankel construction.

This supplies a canonical two-variable bridge:

  angular variable t  <-> explicit-formula / prime-frequency oscillation,
  radial variable a    <-> thermodynamic damping / cumulant-Hankel moments.

The critical-line local kernel used elsewhere corresponds formally to the radial value a=1/2 at each individual prime, whereas the global prime sum is only absolutely convergent here for a>1. Moving the *global* identity from a>1 toward a=1/2 therefore remains a genuine analytic-continuation/explicit-formula problem; local positivity alone does not justify that passage.

## Consequence for the RH program

This bridge is useful because it ties two already-positive constructions together before invoking zeros. It does NOT prove Weil positivity or RH. The missing global theorem remains an unconditional completed explicit-formula identity on an adequate test class, including the Archimedean term and the correct regularization/continuation of the prime contribution.

## Formalization target

1. Formalize the finite-prime identity
   Re[-zeta_p'/zeta_p(a+it)] = (log p)/2 * (K_{p^{-a}}(t log p)-1).
2. Sum over finite prime sets and prove positive-type preservation.
3. On a>1, identify the limit with the existing GlobalVonMangoldtBridge.
4. Differentiate at t=0 to connect the prime Poisson radial derivatives with the Hankel moments.

No critical-strip positivity is claimed.
