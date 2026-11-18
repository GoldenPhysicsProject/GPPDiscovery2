# 2026-11-18 — Euler three-way closure, completed Weil square, and Cesàro convergence obstruction

## The Euler target, stated precisely

Heart's idea (relayed by Daniel): one function should be presented simultaneously through prime Euler factors, integer/theta Poisson symmetry, and a nonnegative square expansion. This is the right organizing objective, with one correction: the desired sum of squares is the *full completed Weil sesquilinear form* and not pointwise Xi(t). Xi(t) is real but changes sign; even a formally nonnegative Xi(t)^2 proves no RH.

The Euler product and Poisson/theta symmetry are already linked by the completed explicit formula, not two addends with separately nonnegative local contributions. In suitable Weil test conventions, the zero-side full pairing has the form
  W(f)=Σ_{ρ} F_f(ρ) conjugate(F_f(1−conj(ρ))),
where F_f is the appropriate Mellin test transform. Under RH, ρ=1−conj(ρ) and W(f)=Σ|F_f(ρ)|². Without RH the reflected pairing of an off-line pair (ρ,ρ*) on test values a,b is 2 Re(a conjugate(b)) = |(a+b)/sqrt(2)|²−|(a−b)/sqrt(2)|², i.e. one even square minus one odd square. All spectral expressions must include *full complex zero positions*. The constructible task is a zero-independent, all-prime-plus-Archimedean positive square realizing EXACT W (not a pre-imposed norm or a squared determinant), and failing on the shifted control Fθ(s)=ξ(s−θ)ξ(s+θ).

The global pole-removed/signed Gamma-prime-pole Krein decomposition in arithmetic_principal_series_RH_program-34.tex, around its 'completed logarithmic derivative is a Krein square' and 'even Hilbert square minus odd Hilbert square' sections, is the immediate raw material; a naive local factorization is already shown insufficient there. The closed target is an arithmetic *global boundary polarization/quotient* that kills or compensates the negative odd sector, proven without assuming zeros lie on the line. This is exactly the Hodge/CPT doubled-orientation analogy's test.

## Critical audit: rh_cesaro_v2.tex epsilon domain error

The positive regularized state is correctly defined as
  ω_ε(f)= ε/2 ∫_R exp(−ε|u|) f(e^u) du
when the integral absolutely converges. For χ_ρ(e^u)=exp[(ρ−1/2)u], the positive square is
  ω_ε(|χ_ρ|²)=ε/2 ∫_R exp(−ε|u|+ (2 Reρ−1)u) du.
It is finite if and ONLY if ε>|2 Reρ−1|. In this domain it equals ε²/[ε²−(2 Reρ−1)²] >0.
If Reρ≠1/2, the path ε→0+ leaves the form's domain before reaching zero and encounters a pole at ε=|2Reρ−1|. Its formal meromorphic continuation beyond the pole is negative for 0<ε<|2Reρ−1|, and is NOT a positive integral.

Concrete countercheck: Reρ=3/4, so 2Reρ−1=1/2. At ε=1/4 the integral is +∞ and not defined in the chosen domain. The rational analytic continuation is (1/4)²/((1/4)²−(1/2)²)=−1/3. Hence the proof of 'Cesàro reformulation of the positivity argument' that asserts positivity for *all* ε∈(0,ε₀), with ε₀ >2max |Reρ−1/2|, is false: the convergence inequality goes in the other direction. The subsequent 'dominated convergence' assertion across a pole is also invalid. In addition, taking a nonnegative integral after meromorphic continuation would conflate two different functions/domains.

This identifies a specific open proof obligation rather than invalidating the valid critical-axis Cesàro calculation. The true result 'only principal-series exponent has finite Cesàro norm in the ε→0 limit' does NOT, by itself, show that every zeta zero supplies a nonzero finite-norm physical state. Spectral completeness/admissibility must be obtained independently, from prime/theta data.

## Second wording correction in haar_positivity_weil_wightman.tex

Its Weil positivity proof sketch writes 'D_k(square)=Σρ |F(ρ)|² + (local terms always ≥0)' as though completed local contributions are extra positive terms on top of the spectral side. This is not the correct unconditional explicit formula, and the prime/pole local terms do not have individually guaranteed positive signs. The zero-side and prime/Archimedean/pole-side are TWO representations of the SAME Weil form; the zero-side becomes a literal sum of modulus squares under RH, not before it. An off-line pair is indefinite as shown above. This should be corrected in a later manuscript edit, not silently assumed.

## Next global theorem (noncircular)

Construct an arithmetic boundary *-algebra, positive state ω with global prime/theta compatibility and an orientation (anti-linear) real structure J, and a feature map T on the full Weil test space, such that
  W_ζ(f,g)=⟨Tf,Tg⟩_H
holds for the already-defined, fully completed signed Weil form, with all limits converging in a topology that preserves the positive domain. Then prove the factorization globally (without spectral-zero assumptions) and exhibit why shifted Fθ violates the same positivity identity. This is an RH-level theorem and is presently OPEN. Do not confuse the tautology 'if W≥0 take its GNS space' with the construction of a positive ω from independent arithmetic data.

No changes made to Daniel's manuscripts; research note only.
