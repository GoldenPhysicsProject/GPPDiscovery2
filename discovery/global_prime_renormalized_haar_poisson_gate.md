# All-scale arithmetic boundary: exact renormalized prime Dirichlet identity and two distinct positivity tests

2026-10-31. Codex / GPPDiscovery2, motivated by Daniel's request and Claude's GPP-bridge PR #11 comment 6547949677: seek an **infinite principle** rather than more finite-support certificates. **EXACT identities below do not establish Weil positivity or RH.** The prime renormalization algebra is known in Dirichlet-form language; the contribution here is an explicit all-support implementation, a clean counterterm no-go, and a local Satake/Haar discriminator to be combined with the missing global Poisson identity.

## 1. Exact infinite arithmetic source without a finite window parameter

Let f ∈ C_c^\infty(R;C), a_n=log n, w_n=Λ(n)n^{-1/2} for n≥2, q_f(a)=2Re∫_R conj(f(x))f(x+a)dx, and T_af(x)=f(x+a), unitary on L²(R).

For each a≥0, the exact complex-Hilbert identity is

    ||f−T_af||² = 2||f||² − q_f(a).        (1)

For each finite arithmetic cutoff X≥2, set Ψ_{1/2}(X)=Σ_{2≤n≤X} w_n ≥0 and

    D_X[f]=Σ_{2≤n≤X} w_n||f−T_{log n}f||² ≥0.

Then EXACTLY

    D_X[f]−2Ψ_{1/2}(X)||f||²
         = −Σ_{2≤n≤X}w_n q_f(log n).        (2)

Let L=diam supp f. Since q_f(a)=0 for a≥L, the right side **stabilizes exactly as soon as X≥exp(L)**. Thus the infinite renormalized arithmetic boundary is well-defined on the full test space, without choosing a support window:

    \boxed{ -S_\zeta[f]=lim_{X→∞}(D_X[f]−2Ψ_{1/2}(X)||f||²). }   (3)

This is not a new assumption. It is a global exact sum-of-squares MINUS divergent contact counterterm. Because Ψ_{1/2}(X)∼2√X by partial summation and the prime number theorem (a classical unconditional theorem, *not RH*), D_X[f]∼4√X||f||² for any nonzero compactly supported f. In particular **D_X itself does not converge to a finite Hilbert norm**; any argument declaring its positivity to prove Weil positivity has forgotten the necessary divergent subtraction. This is the rigorous obstacle to 'Haar/prime squares automatically imply RH'.

The complete corrected v34 Weil form for compactly supported f is exactly

    Q_\zeta[f] =
        E_\gamma[f]−A_\gamma[f]+P[f]−c_\infty||f||²
        + lim_{X→∞}(D_X[f]−2Ψ_{1/2}(X)||f||²),                 (4)

where Eγ=∫₀∞(q_f(0)−q_f(y))/(2sinh y)dy, Aγ=∫₀∞[(e^(y/2)−1)/(2sinh y)]q_f(y)dy (finite because f compactly supported), c∞=log(4π)+EulerGamma, and pole P=2Re((∫f e^(x/2)dx) conj(∫f e^(−x/2)dx)). These expressions are translation invariant under f(x)↦f(x+b) except pole's inverse-rescaled moments cancel exactly. The same Q underlies the first-prime bookkeeping Q=local Hardy potential+gamma jump+prime graph square+signed pole in the team's L=7/10 theorem. Eq (4) is the precise infinite-scale source identity; it is **not manifestly positive**.

## 2. Local Haar/Satake test discriminates shifted false-zeta but is insufficient globally

Let F_θ(s)=ζ(s+θ)ζ(s−θ), 0<θ<1/2. In Re s>1+θ,

    −F_θ'(s)/F_θ(s)=Σ_n Λ(n)(n^θ+n^(−θ))n^(−s).

So the shifted fake has positive arithmetic weights w_n^(θ)=2cosh(θ log n)w_n, and **the same exact renormalized positive-jump identity (1)-(3)** holds after replacing w_n by w_n^(θ). The product of completed shifted zetas has an s↔1−s functional equation and its zeros occur off the center at ρ±θ whenever ζ has a center-line zero (known). Thus positivity of every finite jump D_X and reflection symmetry are NOT a sufficient infinite selection principle.

For each prime p, however, the *normalized local two-parameter moment sequence* of F_θ is m_k(p)=p^{kθ}+p^{−kθ}=2cosh(kθ log p), m_0=2. The first Toeplitz moment matrix is

    [[2,2cosh(θ log p)],
     [2cosh(θ log p),2]]

with determinant −4sinh²(θ log p)<0. It is not the moment matrix of a positive measure on S¹: the local Satake parameters p^{±θ} have modulus ≠1. Genuine ζ has one unit Satake parameter α_p=1 and local Toeplitz moments m_k=1, with rank-one PSD matrices. This is an exact local filter rejecting the Fθ counterexample. It is **NOT** an RH proof; local unitarity and Euler products by themselves do not yield the completed global Weil sign. The missing joint input is the actual rational additive Poisson lattice together with the same prime-local factors and Archimedean scattering normalization.

## 3. What is and isn't the missing 'infinite identity'

Equations (3)-(4) provide a uniform, cutoff-independent *identity* on the full test-function space, not a family of support-dependent approximations. The positive D_X terms do not survive removal of the divergent contact. Thus their algebra makes **no positivity claim**, and any attempted derivation using only Haar/group positive type fails the two-atom Gaussian OS falsifier recorded in GPP-bridge work/codex/2026-10-13_haar_lc_affine_modular_os_criterion.md.

**Explicit open target (not an axiom or result):** derive, from the actual unramified additive-adelic Haar intertwiner / Poisson lattice and unitary prime-local data, an honest positive boundary representation of the RENORMALIZED combination (4) that retains the signed counterterm and the indefinite two-pole boundary contribution. Such a derivation must (i) reproduce Q in the first-prime ledger, including its stabilizing mirror-odd source, (ii) distinguish true ζ from the locally nonunitary Fθ and the FE-only DH, (iii) establish all-support positivity without assuming it or importing RH disguised as a spectral hypothesis. No such factorization has been obtained.

## 4. Exact continuum and finite checks

For f=1_[0,L] (a finite-log-energy form-domain test, smooth approximable), q_f(a)=2(L−a)_+ and ||f−T_af||²=2min(a,L). Hence every term of (2) is exactly −2w_n(L−log n)_+, zero if log n≥L. This makes the support-independent *stabilization* transparent, while D_X and Ψ(X) separately diverge. A direct executable regression is discovery/global_prime_renormalization_control.py; it also checks shifted Fθ and the local Toeplitz determinant. Its use of floating arithmetic is only a regression for algebraic identities; the analytic proofs above need no Arb.

## Provenance and links to active workflow

- Prior exact Q resource ledger: discovery/first_prime_exact_completed_resource_ledger.md, CI 41232244549.
- Actual first-prime odd positivity and full-form negative index at most one at L=7/10: discovery/actual_p2_completed_negative_index_at_most_one_L7_10.md, CI 41232909222.
- Local affine Haar involution, smooth counterexample distinguishing group Haar from OS: GPP-bridge work/codex/2026-10-13_haar_lc_affine_modular_os_criterion.md.
- Grok's independent global Dirichlet/Levy analysis: GPPDiscovery5 team/queen/2026-10-22_noncircular_positivity_spec.md (beware Grok's L is HALF width, while here L is FULL support diameter).
- The structural goal is the same RH-strength missing global arithmetic-Archimedean OS positivity; nothing in this note assumes or proves that sign.

**Status: all formulas (1)-(4) rigorous for C_c^\infty tests, local Toeplitz exact; global positivity OPEN, RH OPEN.**
