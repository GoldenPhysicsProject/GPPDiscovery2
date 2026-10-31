# A single all-scale completed prime–Archimedean thermal/KMS Dirichlet identity, with exact contact

Codex/GPPDiscovery2, 2026-10-31. **MAIN RESULT**: an exact, explicit, support-independent representation of the corrected v34 Weil quadratic form on compactly supported smooth complex tests, combining the whole prime-side Bost–Connes midpoint gradient with a positive Archimedean odd-thermal-ladder jump energy. This builds BOTH positive energy sectors from raw arithmetic/thermal structures, while retaining the compulsory negative contact and indefinite pole. **It does not establish positivity of the total completed Weil form, nor RH.** It is an explicit classical Beurling–Deny/Lévy energy representation, now matched to a concrete BC KMS midpoint construction, not a new RH-strength theorem.

## 1. Exact corrected source

For f∈C_c∞(R;C), T_y f(x)=f(x+y), N=||f||², and q_f(y)=2Re⟨f,T_y f⟩, the corrected v34 one-sided completed Weil form is

   Q[f]=E[f]−A[f]+P[f]−c∞N−S_prime[f],

where

   E[f]=∫₀∞ (2N−q_f(y))/(2sinh y)dy,
   A[f]=∫₀∞ [(e^(y/2)−1)/(2sinh y)] q_f(y)dy,
   c∞=log(4π)+γ_E,
   P[f]=2Re((∫_R f(x)e^(x/2)dx) * conjugate(∫_R f(x)e^(−x/2)dx)),
   S_prime[f]=Σ_(n≥2)Λ(n)n^(−1/2)q_f(log n).

Because f compact, S_prime is actually finite. E and A integrals converge for C_c∞. The signs and gamma infinite tail are the same as in the prior Discovery2 corrected complete Weil source and the first-prime resource ledger.

## 2. Archimedean thermal ladder plus an exact scalar counterterm

Define

   wγ(y)=e^(y/2)/(2sinh y)=e^(−y/2)/(1−e^(−2y))
        =Σ_(k=0)^∞ e^{−(2k+1/2)y}  >0,
   r(y)=(e^(y/2)−1)/(2sinh y).

An EXACT pointwise identity holds:

   (2N−q(y))/(2sinh y) − r(y)q(y)
     = wγ(y)(2N−q(y)) − 2N r(y).

Therefore, with the positive translation Dirichlet energy

   Dγ[f]=∫₀∞ wγ(y)||f−T_yf||²dy
        =Σ_(k=0)^∞∫₀∞e^{−(2k+1/2)y}||f−T_y f||²dy ≥0,

we obtain

   E[f]−A[f] = Dγ[f]−2R∞ N,

where R∞=∫₀∞r(y)dy. This scalar admits an ELEMENTARY exact integral:

Let t=e^(−y/2); then r(y)=t/[(1+t)(1+t²)], dy=−2dt/t. Hence

   R∞=2∫₀¹dt/[(1+t)(1+t²)]
      =2[(1/2)log(1+t)−(1/4)log(1+t²)+(1/2)arctan t]_0¹
      =(1/2)log 2 + π/4.

Thus the FULL Archimedean contact is

   c∞+2R∞ = log(8π)+γ_E+π/2 = −[ψ(1/4)−logπ].

The final equality uses the classical digamma identity ψ(1/4)=−γ_E−π/2−3log2. This agrees with the exact Gamma/zero-side normalization used in GPPDiscovery5 team/queen/2026-10-22_noncircular_positivity_spec.md (their Ω(0)=ψ(1/4)−logπ).

**Important**: the gamma energy itself is positive; the completed gamma contribution is gamma energy MINUS its exact contact. Dropping the contact would prove false statements even before adding primes.

## 3. Prime KMS positive gradient and mandatory divergent contact

Let μ_n be BC isometries σ_t μ_n=n^(it)μ_n, μ_n*μ_n=1; ω any normalized state, with the β=1 KMS state the canonical midpoint choice. For n≥2 put a_n=log n and

    B_(n,x)[f]=(f(x)−f(x+a_n)) μ_n.

Then ω(B*σ_(i/2)(B))=n^(−1/2)|f(x)−f(x+a_n)|². For finite X,

    K_X^BC[f]=Σ_(2≤n≤X) Λ(n)∫_R ω(B_(n,x)*σ_(i/2)(B_(n,x)))dx
             =Σ_(2≤n≤X) Λ(n)n^(−1/2)||f−T_(log n) f||² ≥0,

    Ψ_(1/2)(X)=Σ_(2≤n≤X)Λ(n)n^(−1/2).

Hilbert polarization gives

    K_X^BC[f]−2Ψ_(1/2)(X)N =−Σ_(2≤n≤X)Λ(n)n^(−1/2)q_f(log n).

The right side stabilizes for X≥exp(supp diameter). The positive K_X and Ψ both diverge (Ψ~2sqrt X), but the difference is exact and finite for every compact f.

## 4. The one combined, all-support identity

Substitution yields, with κ∞=log(8π)+γ_E+π/2,

[
\boxed{
Q[f] = P[f] + D_\gamma[f]
+\lim_{X\to\infty}\left(K_X^{\mathrm{BC}}[f]-2\Psi_{1/2}(X)\|f\|_2^2\right)
-\kappa_\infty\|f\|_2^2.}
]

This is the exact sum of (1) a positive Archimedean KMS/odd thermal ladder Dirichlet energy and (2) a positive finite-prime KMS midpoint energy, MINUS the explicit finite Gamma/contact κ∞ and the **divergent** prime renormalization, PLUS the genuine indefinite pole P. No RH assumption is made. The identity is valid at *all support widths*, not a window-by-window estimate, and its first-prime specialization reproduces signed -S2=wD−wM and the opposite pole parity signs. The completed expression is NOT manifestly positive. The whole missing global RH-strength issue is exactly to show the signed contact and pole are sewn in a positive reflected OS Hilbert geometry by a principle unavailable from separate positive energies.

The odd thermal ladder is in the true gamma kernel, not a free parameter chosen to force positivity. It may be interpreted as a modular thermal weight in the celestial dictionary only after the Hilbert-space dynamics and covariance are independently constructed; the equality of functional shapes is not a physical identification of the celestial scattering amplitudes.

## 5. Falsifiers and potential proof target

The positive prime BC energies and gamma thermal ladder also exist in modified arithmetic models; F_theta has positive modified prime coefficients, with unitary Satake Toeplitz obstruction at each p, and DH has the FE without the genuine Euler prime-power monoid. This representation alone does NOT distinguish them.

A candidate full GNS/OS reconstruction must derive, noncircularly, from the SAME arithmetic additive Poisson lattice and its canonical multiplicative automorphisms, a reflected boundary covariance whose renormalized expectation equals EXACTLY (4), including κ∞, the whole prime subtraction and P. Its positive half-space cannot simply be the entire L² space with exchange Θ, because Θ has ±1 eigenvalues; OS positivity is about a restricted test algebra and specific covariance. The identity (4) makes the remaining defect explicit and testable.

Exact source derivations:
- discovery/bc_kms_prime_gradient_all_scale.md (prime midpoint);
- discovery/global_prime_renormalized_haar_poisson_gate.md (prime subtraction);
- discovery/first_prime_exact_completed_resource_ledger.md (signed p2);
- discovery/semilocal_full_gamma_prime_pole_sos.md (completed gamma and pole).

The independent high-precision diagnostic discovery/complete_thermal_kms_identity_audit.py checks the direct corrected v34 formula and the globally positive-gamma/renormalized-prime formula on several compact-support indicator tests (finite log-kinetic form domain, smooth approximable) and the elementary gamma contact. This regression is NOT a Lean verification or an RH positivity proof.

**RH OPEN; full arithmetic–Archimedean OS positivity OPEN.**
