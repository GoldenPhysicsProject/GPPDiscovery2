# A genuine scalar bound near Re s=1 and what is still required at 1/2

Use B_X(s)=Σ μ(n)n^(−s)exp(−n/X) at the actual integer phases. All bounds below are for the natural numbers. The only deep unconditional input in the moving-strip result is the classical zero-free-region estimate M(y)=Σ_{n≤y}μ(n) ≪ y exp(−c√log y) for some c>0 (the classical de la Vallée Poussin strength suffices). This does not assume RH. Constants below are existential, not explicit numerical cutoffs.

## A piece of the requested bound

There exists a>0 such that for every finite T and all sufficiently large X,

    sup |B_X(s)| ≪_T 1    (1−a/√log X ≤ Re s ≤ 2, |Im s|≤T).

The same estimate holds for B′_X(s). In particular it also bounds the area integrals on subsets of that moving rectangle, proportionally to their area.

Proof. Write L=log X, take 0<a<c/(2√2), and split the sum at Y=X². Beyond Y, both the series and its derivative have uniformly negligible absolute tails, since Re s≥1/2 for X large and exp(−n/X)≤exp(−X/2)exp(−n/(2X)). Up to Y apply partial summation to n^(−s) exp(−n/X) times either 1 or log n. With t=log y∈[0,2L], the absolute integrand is bounded by a constant depending on T times

    (1+t) exp((1−Re s)t−c√t) (1+y/X)exp(−y/X) dt.

Indeed the second factor in parentheses comes from differentiating the exponential cutoff and the other factor covers the logarithmic derivative in s. The first exponential is ≤exp(−c√t/2) by the choice of a. Its integral against (1+t) is finite. The upper endpoint in partial summation satisfies the same bound (and the exponential cutoff there is exp(−X)). This proves both assertions. At fixed Re s=1 the same partial summation and dominated convergence identify the limit with 1/ζ(1+it), with value zero at the pole t=0, by taking the boundary value from the right. The strip width here tends to zero. It gives no bound at a fixed σ<1.

## A one-real-sequence version of the outstanding input

Let S(x)=Σ μ(n)exp(−n/x). For this smoothing RH is equivalent to the following real scalar bound alone:

    for every ε>0, |S(k²)| ≪_ε k^(1+ε) for all positive integers k.

Proof. For x≥1, |S′(x)|≤x⁻² Σ n exp(−n/x)=[2x sinh(1/(2x))]⁻²≤1. Between consecutive squares the error from the nearest sampled value is therefore O(√x). The proposed bound gives S(x)≪_η x^(1/2+η) for every η>0. For Re s>1 absolute convergence gives

    ∫₀∞ S(x)x^(−s−1) dx = Γ(s)/ζ(s).

At zero S(x) decays exponentially in 1/x. At infinity the proposed growth bound gives absolute locally uniform convergence for Re s>1/2, hence a holomorphic continuation of the reciprocal there since Γ has no zeros or poles there. Reflection finishes the implication. Conversely RH implies the classical M(y)≪_η y^(1/2+η). Partial summation with exp(−y/x) gives S(x)≪_η x^(1/2+η); specialize to squares and relabel η. This reduction uses no square-root cancellation assumption in the interpolation between neighboring samples. The hard part is the bound on the samples themselves. The unconditionally available zero-free-region estimate only gives S(x)≪x exp(−c′√log x): split partial summation at √x and bound exp(−c√log y) above it.

## Why local prime-power bounds plus torus cancellation do not supply the difference

Twist the genuine coefficients by the completely multiplicative sign λ(n)=(−1)^Ω(n). The new series for the forward object is ζ(2s)/ζ(s) on Re s>1. Its inverse has coefficients λ(n)μ(n)=μ(n)², still bounded by 1, with exactly the same support and coefficient magnitudes as the genuine inverse. Dirichlet convolution of the two twisted coefficient sequences is still δ₁. On each prime torus this is the Haar-preserving rotation z_p↦−z_p, so even the joint Haar laws agree with those of the genuine forward/inverse pair where defined. On the actual real scalar sequence the rotated inverse obeys

    Σ μ(n)² exp(−n/x) = x/ζ(2)+O(√x)   (x≥1).

Indeed μ(n)²=Σ_{d²|n}μ(d) gives Σ_{n≤y}μ(n)²=y/ζ(2)+O(√y) by the floor error and the absolutely convergent d⁻² tail. Partial summation then gives the displayed formula. At x=k² it grows quadratically in k. The twist changes the forward coefficients and does not provide a counterexample to a theorem assuming the full ζ data. It rules out arguments using only rotation-invariant mean estimates, coefficient magnitudes, local boundedness and the convolution identity. The untwisted signs at the actual integer phases carry essential information.

These are analytic derivations. The square-sample bound and Statehood for all complex zeros have not been proved here.
