# A modular oscillator window with exact Möbius cancellation at fixed holonomy

This comparison window uses the reciprocal oscillator partition product in the compact-boson cylinder. Its logarithm is F(t)=Σ_{m≥1} ℓ(mt), where ℓ(t)=log(1−exp(−t)), t>0. Let T f(t)=f(2t) and D=(T+T⁻¹−2)(T+T⁻¹−5/2). Set K=DF and B=Dℓ. D is a chosen five-scale linear combination. It removes the explicit cusp terms while commuting with inversion. No RH input or zero ordinate is used.

## Exact cancellation at the two distinguished angles

The Dedekind eta inversion formula on the imaginary axis gives F(t)=F(4π²/t)+(1/2)log(2π/t)−π²/(6t)+t/24. The stencil kills the constant, log t, t and 1/t. It is invariant under exchanging T with T⁻¹. Thus K(t)=K(4π²/t) and K decreases exponentially at both ends (in t or in 1/t, respectively). The divisor identity Σ_{n|k} μ(n)=[k=1] and absolute convergence at any fixed t give

    Σ_{n≥1} μ(n)K(nt)=B(t)=(21/128)t²+O(t⁴) as t↓0.

At the half-turn, if C(t)=B(t) and A(t)=Σ(−1)^n μ(n)K(nt), then (1−T)A=−(1+T)C by the even-charge projection. Explicitly A=(T²−(5/2)T+(5/2)T⁻¹−T⁻²)ℓ, using decay at infinity to invert the difference. Hence A(t)=−log 2+(35/128)t²+O(t⁴). Both expansions follow from ℓ(t)=log t−t/2+t²/24+O(t⁴). This proves uniform signed cancellation for an explicit nonzero window at each fixed angle. Its profile differs from the original exp(−t).

## Why the cancellation works and how to expose what it misses

Use Mellin convention f̂(s)=∫f(t)t^(s−1)dt. Write P(s)=(2^s+2^(−s)−2)(2^s+2^(−s)−5/2). Termwise integration for Re s>1 gives

    B̂(s)=−P(s)Γ(s)ζ(s+1),      K̂(s)=ζ(s)B̂(s).

The second identity cancels precisely the reciprocal that Statehood is trying to control. To probe it choose the odd packet K₁(t)=log(t/(2π))K(t), the derivative of (t/(2π))^a K(t) at a=0. It changes sign under the same modular inversion. Its signed amplitude J(t)=Σ μ(n)K₁(nt) has the exact prime-side formula

    J(t)=log(t/(2π))B(t)−Σ_{m≥2}Λ(m) B(mt).

Indeed (μ log)*1=−Λ by differentiating the reciprocal Dirichlet series in its convergent half-plane, or directly on divisors. Its Mellin transform starts on Re s>1 and continues as

    Ĵ(s)=B̂′(s)−log(2π)B̂(s)+B̂(s)ζ′(s)/ζ(s).

P(s) has roots only on Re s=0,1,−1; Γ has no zeros and ζ(s+1) has none in the critical strip. Therefore at any zero ρ with 1/2<Re ρ<1 the last term has a simple pole with nonzero residue ord_ρ(ζ) B̂(ρ). No simplicity assumption. A bound J(1/X)=O_ε(X^(1/2+ε)) for every ε>0 would exclude these poles by absolute Mellin convergence and then give RH by reflection. Decay at infinity in t is immediate from the series. The zero-order identity alone gives no estimate on this first response.

## The square-root part of the response that can be evaluated

The continuous prime-density contribution is exactly zero: ∫B(t)dt=B̂(1)=0. The higher prime powers can be handled unconditionally. With θ(u)=Σ_{p≤u}log p, the PNT θ(u)~u gives

    Σ_p (log p)B(p²/X) = (B̂(1/2)/2)√X + o(√X).

This is partial summation after scaling p by √X, using B(v²)=O(v⁴) at zero and exponentially decreasing tails and derivatives. The coefficient is strictly positive: P(1/2)<0. The sum over k≥3 of (log p)|B(p^k/X)| is O(X^(1/3)): by Chebyshev its unweighted counting mass through u is O(u^(1/3)+u^(1/4)log(2u))=O(u^(1/3)) for u≥2, and exponential decay bounds the dyadic tail. Thus the only part that could exceed the target order is the signed sum over primes to the first power, Σ_p(log p)B(p/X). This isolates a specific smooth prime-side estimate for an independent CFT route; its proof is outstanding. The match with a prime-side strategy is structural. No assertion is made that this is Alpöge's ramp kernel.

Run oscillator_window.py beside check.py for independent finite numerical checks of inversion, both fixed-angle identities and the arithmetic first response. These are floating-point consistency checks; the identities and asymptotics above follow from the analytic arguments.
