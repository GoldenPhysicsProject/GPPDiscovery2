# Explicit Bost–Connes KMS midpoint representation of the RENORMALIZED arithmetic prime source

2026-10-31. Codex/Discovery2. This is a constructive **exact algebraic identity** for the complete prime-side contribution of the corrected Weil distribution on every compactly supported log-line test. It is NOT a new proof of positivity of that distribution, because a divergent KMS contact subtraction remains. It does NOT include the Archimedean gamma/pole and it does NOT prove RH.

## 1. Minimal operator input

Let μ_n (n≥1) be the canonical isometries in the Bost–Connes-type arithmetic C*-dynamical system, satisfying μ_n* μ_n=1, and time evolution σ_t(μ_n)=n^(it) μ_n. Let ω be any normalized state on the algebra for which the analytic continuation of each μ_n is defined (BC β=1 KMS state is a canonical example). Then

   σ_(i/2)(μ_n)=n^(-1/2) μ_n,
   ω(μ_n*σ_(i/2)(μ_n))=n^(-1/2).                (1)

No RH, prime number theorem, zeta zeros or functional equation is used to prove (1). In fact ω(μ_n*μ_n)=1 is sufficient. The choice β=1 supplies the correct half-density.

## 2. The necessary COHERENT gradient embedding

For complex compactly supported test f∈C_c∞(R), put a_n=log n and for every log coordinate x define the algebra element

   B_(n,x)(f) = [ f(x) − f(x+a_n) ] μ_n.

Its KMS midpoint quadratic has an EXACT positive value

   ω( B_(n,x)(f)* σ_(i/2)(B_(n,x)(f)) )
     = n^(-1/2) | f(x)−f(x+a_n) |².           (2)

CRITICAL: the two endpoint amplitudes must live **in the SAME μ_n grade as a difference**. The naive A_(u,v)=u 1+v μ_n has midpoint |u|²+n^-1/2|v|² and is relative-phase-blind (see discovery/naive_bc_kms_midpoint_phase_blindness.md). Formula (2) restores the actual prime interference and all four global/local mirror signs when the counterterm is included.

For each finite X≥2 the manifestly positive KMS form

   K_X[f] = Σ_(2≤n≤X) Λ(n) ∫_R ω(B_(n,x)*σ_(i/2)(B_(n,x))) dx
          = Σ_(2≤n≤X) Λ(n)n^(-1/2) ||f−T_(log n)f||² ≥0.     (3)

Each prime power has Λ(p^r)=log p≥0; other n have Λ(n)=0. The integral is ordinary nonnegative Lebesgue integral, finite for finite X. This is a **noncircular explicit map** from f to the positive KMS energy. It is a direct sum/integral over the prime powers and log-coordinate x, not a claim that the Bost–Connes equilibrium Hilbert space alone is the entire physical Hilbert space.

## 3. The unavoidable, exact divergent contact: matched to completed Weil

Let Ψ_(1/2)(X)=Σ_(2≤n≤X)Λ(n)n^(-1/2) and q_f(a)=2Re ⟨f,T_a f⟩. By exact Hilbert polarization,

    K_X[f] − 2Ψ_(1/2)(X)||f||² = −Σ_(2≤n≤X)Λ(n)n^(-1/2) q_f(log n).  (4)

For compact support of diameter L, all q_f(log n)=0 as soon as n≥e^L. Thus the RIGHT side stabilizes EXACTLY, defining the prime side for EVERY compactly supported f:

   -S_prime[f] =
    lim_(X→∞){ K_X[f] − 2Ψ_(1/2)(X)||f||² }.       (5)

The positive K_X does NOT converge: Ψ_(1/2)(X)~2√X by PNT, and K_X~4√X||f||². The **divergent subtraction is essential**. A new positive operator/norm proof cannot discard it or declare that (5)≥0 just because K_X≥0.

For the first prime, n=2, a=log2, w=log2/√2, and endpoint strips u,v,

   -S_2 = w||u−v||² − w(||u||²+||v||²) = −2w Re⟨u,v⟩.  (6)

It recovers all four double-reflection source eigenvalues and matches the team's exact corrected prime Hardy ledger. This is the **constructive, precisely normalized BC KMS contribution** sought in the project's original Arithmetic Holography §8, up to the still-missing Archimedean sewing.

## 4. What is still NOT established

A faithful global OS/Hilbert representation of the completed Weil form

   Q[f] = E_gamma[f]−A_gamma[f]+P[f]−c∞||f||²−S_prime[f]

would need the canonical ARCHIMEDEAN Gaussian/scattering sector to cancel or dominate the KMS contact (5), match the **indefinite rank-two pole**, and produce positivity on the properly defined OS half-space **for all f**. This is the RH-strength step. No such positive global representation has been constructed by (1)–(6), and the functional equation does not supply it automatically.

False controls: shifted F_theta has altered positive prime weights Λ(n)(n^θ+n^(−θ)) and also permits positive gradient squares of the same form, so this construction ALONE cannot reject it (a local Satake-circle unitarity condition does reject its p^±θ moments). Davenport–Heilbronn has no coherent Euler prime-power product and cannot use the exact same μ_n arithmetic isometries/coefficients, but the completed sign must still be tested independently.

Mathematical caveat: the source identity is algebraic in BC isometries and valid for any normalized state; the existence of an appropriate full locally normal KMS₁ state, choice of completion and crossed-product compatibility belong to the standard BC construction and are not proved by this note. The map B_(n,x) is explicitly defined; **only the resulting prime energy matches Weil, not the missing full reflection positivity**.

## 5. Reproducibility and formalization

The arithmetic test at discovery/bc_kms_prime_gradient_exact.py checks (2)–(6) using exact Gaussian-integer and Fraction computations (including n=4 and 9 prime-power rational square-root weights), with normalized log factors. CI in .github/workflows/bc-kms-prime-gradient.yml. The all-cutoff positive-minus-divergent-contact calculation was previously derived in discovery/global_prime_renormalized_haar_poisson_gate.md and its CI 41233716041. The one-prime sign harness passed CI 41234492625. These are exact algebraic results, not an Arb completed spectral certificate.

**Lean exact new candidate**: finite sum version of (3)–(4) with μ_n isometry and analytic time eigenoperator assumptions; prove finite prime-graded midpoint norm and mandatory counterterm using Hilbert polarization, with no RH hypothesis or open stub claiming positivity. Avoid duplicating PathSOS finite edge identity; the new content is the explicit BC time-midpoint realization.

The team's next genuinely difficult step is now sharpened: produce the Archimedean BC/BPY/TFD boundary map which completes the positive KMS prime energy **after renormalization**, while respecting the true pole signs and excluding fakes. RH remains OPEN.
