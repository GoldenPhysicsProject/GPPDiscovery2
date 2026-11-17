# An unconditional positive RG fixed point of the prime reflection kernel (2026-11-16)

**Status:** exact unconditional Euler-product theorem, with a 75-digit numerical audit. No RH, Weil positivity or celestial unification claim. The analytic ingredients are classical; the purpose here is the precise positive-renormalization bridge and the independent shifted-weight negative control.

Let h(s)=-zeta'(s)/zeta(s). For epsilon>0 define positive probability weights

    p_epsilon(n) = Lambda(n)*n^(-1-epsilon) / h(1+epsilon),  n>=2,

so Σ_n p_epsilon(n)=1 by the absolutely convergent Euler logarithmic derivative. Define X_epsilon=epsilon*log(n).

## Theorem: a nontrivial positive boundary-layer limit

For all t,u>=0, set

    K_epsilon(t,u)
       = E_p[exp(-(t+u)X_epsilon)]
       = h(1+epsilon*(1+t+u)) / h(1+epsilon).

Each K_epsilon is REFLECTION-POSITIVE since any finite Gram quadratic is

    Σ_i,j conj(c_i)c_j K_epsilon(t_i,t_j)
       = E_p[ |Σ_i c_i exp(-t_i X_epsilon)|² ] >=0.

As epsilon->0+, the Laurent expansion h(1+z)=1/z-gamma+O(z) gives uniformly on compacts of t,u>=0:

    **K_epsilon(t,u) -> K_*(t,u)=1/(1+t+u)**

and this is positive since

    K_*(t,u)=Integral_0^infty exp(-x)*exp(-t*x)*exp(-u*x) dx.

Thus a genuine positivity-preserving nontrivial **RG/scaling limit** exists. The limiting Hilbert space is L²([0,infty),e^(-x)dx), feature vectors x->exp(-t*x). Its first analytic correction is

    K_epsilon(t,u) = 1/(1+t+u)
      -gamma*epsilon*(t+u)/(1+t+u)+O(epsilon²).

The Laplace transform of X_epsilon converges to 1/(1+r); hence by the probability-measure Laplace continuity theorem

    X_epsilon ==> Exp(1) in distribution.

This uses only the simple pole at s=1, NOT the RH zero distribution.

## Exact relationship to the earlier critical-half-density wall

From research/prime_plancherel_OS_wall_2026_11_16.md, define J_(1/2)(t)[n]=sqrt(Lambda(n))*n^(-1/4-t), which is ell² if and only if t>1/4.

Define t_epsilon(v)=1/4+epsilon*(1/2+v). Then

    <J_(1/2)(t_epsilon(t)),J_(1/2)(t_epsilon(u))>/h(1+epsilon)
      = K_epsilon(t,u).

This approaches the **normalizability boundary from its positive convergent side** while rescaling both vectors and their norms, rather than analytically continuing the prime kernel to t=0 (which is negative and fails OS). The limiting Hilbert-space representation is different; no zeta/Weil isometry is claimed.

## Shifted F_theta-style negative control: same fixed point

Let theta>0 and a_theta(n)=Lambda(n)cosh(theta log n). Its positive Dirichlet series is

    h_theta(s)=Σ a_theta(n)n^-s = [h(s-theta)+h(s+theta)]/2.

It has rightmost pole at 1+theta, residue 1/2. Thus

    h_theta(1+theta+epsilon*(1+t+u))
      / h_theta(1+theta+epsilon)
        -> 1/(1+t+u)

by exactly the same pole argument, for every fixed t,u>=0. This shifted-weight control has zeros displaced off critical axis in corresponding completed products; the arithmetic weight model is not asserted to be a stand-alone L-function. **Therefore the positive Cauchy fixed point is NOT RH-discriminatory.** Any argument deriving RH merely from this fixed point would equally apply to the shifted counterexample and be invalid.

This is a precise separation: universal local/scale positivity is proved, while the global arithmetic completed Weil positivity remains open. Avoid conflating RG limits with analytic continuation or with the completed reflected Weil form.

## Reproducibility and Lean tasks

Numerical audit: experiments/abel_prime_common_map/verify_prime_os_RG_fixed_point.py, 75-digit mpmath. Checks O(epsilon) and O(epsilon²) convergence at decreasing epsilon, a positive Cauchy-kernel quadratic as a positive exp-integral, and shifted model behaviour separately.

Lean targets: log-derivative simple-pole asymptotics; positive discrete-prime probability distribution; generic Laplace/Hankel Gram positivity; positive Cauchy kernel Gram via exponential integral; compact-uniform kernel limit; explicit countercontrol showing fixed-point universality. None proves ARP/OB6/RH.
