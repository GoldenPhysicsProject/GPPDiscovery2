# Exact Legendre logarithmic-kernel spectrum: completed Weil one-negative-direction reduction to L=43/100

**2026-10-31 | Codex / Discovery2.** New analytic result for the **corrected full v34 semilocal Weil form** on genuinely short prime-free supports. NOT an RH proof. Earlier unconditional all-function full Q positivity extends to L=29/100; the theorem here is **coercivity only on the mean-zero codimension-one subspace**, but it extends to L=43/100 and identifies the remaining Schur obstruction.

## 1. Exact logarithmic-kernel spectral theorem

Define on [0,1] the nonlocal self-adjoint logarithmic Laplacian (quadratic-form sense)

    (Af)(x)=∫₀¹ [f(x)−f(y)]/|x−y| dy.

For monomials (n≥1), **exact polynomial identity**:

    A(x^n)=2 H_n x^n − Σ_(k=0)^(n−1) x^(n−1−k)/(k+1),
    H_n=Σ_(j=1)^n 1/j, H_0=0.

Proof: split the y integral at y=x, use (x^n−y^n)/(x−y)=Σ_(k=0)^(n−1)x^(n−1−k)y^k, and integrate each term exactly. Thus A maps polynomials of degree ≤n to themselves, with leading coefficient 2H_n on the quotient of degree n by degree n−1. A is symmetric on polynomials since

    ⟨g,Af⟩ = (1/2)∫∫[conj(g(x))−conj(g(y))][f(x)−f(y)]/|x−y| dxdy.

The unique shifted Legendre polynomial P_n(2x−1) is orthogonal to all lower degrees, so A P_n is orthogonal to every polynomial of degree ≤n−1. It must therefore be exactly (2H_n)P_n. Polynomial density/closed positive quadratic-form completion extends the diagonalization to the entire finite-energy space.

On a general interval [0,L], the eigenfunctions are normalized shifted Legendre polynomials e_n(x)=sqrt((2n+1)/L) P_n(2x/L−1), with unchanged eigenvalues 2H_n (kernel and integration scale cancel). The exact form

    J0[f]=(1/2)∫_(0<x<y<L) |f(y)−f(x)|²/(y−x) dxdy

satisfies J0[f]=Σ_(n≥1) H_n |⟨f,e_n⟩|². Hence for mean-zero f,

    J0[f]≥||f||²;

for reflection-even mean-zero f, only even indices n≥2 survive, so

    J0[f]≥H_2||f||²=(3/2)||f||²;

for reflection-odd f, only odd indices n≥1 survive, so J0[f]≥||f||².

These inequalities are *sharp for J0*, attained by P1 and P2 respectively.

## 2. The genuine gamma jump controls J0 for L≤1

The corrected completed form has the positive interior jump coefficient

    w(y)=exp(y/2)/(2 sinh y).

For 0<y≤1, sinh(y)/y = ∫₀¹ cosh(ty)dt ≤ cosh y ≤ exp(y²/2) ≤ exp(y/2). The middle inequality follows by differentiating y²/2−log cosh y (derivative y−tanh y≥0). Therefore w(y)≥1/(2y), and

    J_gamma[f]=∫₀ᴸ w(y)∫₀^(L−y)|f(x+y)−f(x)|²dxdy≥J0[f].

This is rigorous for every 0<L≤1, for all f in the relevant form domain.

## 3. Actual completed form, correct sign of both pole channels

For L<log2 no prime powers are active. The exact complete decomposition from discovery/semilocal_full_gamma_prime_pole_sos.md is

    Q_L[f]=∫₀ᴸ (V_L(x)−Γ_L(x)−c∞)|f(x)|²dx
          +J_gamma[f]
          +2|C_f|²−2|S_f|²,

where H(z)=log coth(z/2), V_L=[H(x)+H(L−x)]/2, Γ_L=∫₀ˣr+∫₀^(L−x)r, r(y)=(exp(y/2)−1)/(2sinh y), c∞=log(4pi)+EulerGamma, C_f=∫f(x)cosh((x−L/2)/2)dx, S_f=∫f(x)sinh((x−L/2)/2)dx.

Pointwise Hardy convexity V_L≥H(L/2) and gamma bound Γ_L≤exp(L/4)−1 yield V_L−Γ_L−c∞≥β(L), with

    β(L) = −log tanh(L/4)−(exp(L/4)−1)−(log(4pi)+EulerGamma).

The squared L² norm of s(x)=sinh((x−L/2)/2) is exactly sinh(L/2)−L/2.

Consequently, for every **reflection-odd** f on [0,L],

    Q_L[f] ≥ [β(L)+1−2(sinh(L/2)−L/2)] ||f||².    (O)

For every **reflection-even and mean-zero** f,

    Q_L[f] ≥ [β(L)+3/2] ||f||².                      (E)

For arbitrary mean-zero f, decompose into reflection-even and reflection-odd pieces. Q commutes with the reflection x↦L−x because all kernels depend only on |x−y|, including both pole terms. Thus the lower bound is the smaller of (O) and (E), without cross-parity terms.

## 4. Arb certificate at L0=43/100

FLINT/Arb 256-bit outward ball evaluation rigorously establishes at L0=43/100=.43:

    β(L0) ≈ −0.9876246112199906...
    B_odd(L0) = β+1−2(sinh(L0/2)−L0/2) ≈ 0.00905493199... > 1/125,
    B_evenmean0(L0) = β+3/2 ≈ 0.51237538878... > 1/2.

Therefore

    Q_L0[f] ≥ (1/125)||f||²

for every complex **mean-zero** admissible f on [0,L0]. The even mean-zero component has stronger margin 1/2. Every shorter centrally embedded support has the same conclusion by ambient zero extension; if reflection parity is used, center the shorter interval at the ambient midpoint.

**CI receipt:** https://github.com/GoldenPhysicsProject/GPPDiscovery2/actions/runs/41218903018 (SUCCESS), code discovery/legendre_log_jump_weil_arb.py on codex/discovery-workbench, commit be9dbbdfbf0ab927c1bddbd280e499cc432df1d0. This Arb run checks scalar endpoint; the exact Legendre operator proof is supplied above, not yet formalized in Lean.

## 5. Consequence: negative index ≤1 and ONE scalar Schur criterion

On L=L0, the codimension-one form restriction to e0⊥ (constant mode e0=1/sqrt(L)) satisfies A=Q|_{e0⊥}≥(1/125)I. In particular, any negative subspace of Q has dimension at most one.

Let m=Q[e0] and b=Π_(e0⊥)(Q e0). The operator Q e0 is a genuine L² vector despite logarithmic endpoint behavior of V, since log(x) is square-integrable. Specifically,

    (Q1)(x)= V_L(x)−Γ_L(x)−c∞+2C0 cosh((x−L/2)/2),
    C0=4sinh(L/4).

Write normalized b(x)=1/sqrt(L) Π_(mean-zero) [V_L−Γ_L−c∞+2C0 cosh((x−L/2)/2)].

Because A is strictly positive and has a bounded inverse, the completed square in the form sense gives the EXACT criterion

    Q_L≥0 iff m−⟨b,A^(-1)b⟩≥0.                     (Schur)

This is an honest unresolved scalar, NOT automatic from m>0 or separate positivity of the mean-zero compression. The numerical finite Galerkin evidence indicates this scalar is positive at L=.43, but no uniform/infinite-dimensional Arb certificate has been obtained for it. Do NOT announce full Q positivity to .43.

The algebraic reduction has become a single even-parity constant-mode sewing cost at this fixed support. To improve support or reach the prime atom at log2, need control this scalar (or a stronger finite/continuum tail Schur) AND maintain mean-zero coercivity when prime translations activate.

## 6. Formalization and cross-team test

Relevant existing modules: GppVerify/RiemannHypothesis/PathSOS.lean, PoleCoshSinh.lean; no duplication. New targeted Lean modules: exact polynomial action A(x^n), Legendre leading coefficient/orthogonality eigenvalue theorem, finite-dimensional harmonic-diagonal form inequality, then continuum density/Fubini. The scalar Arb gate is not a Lean proof.

This develops the existing GPP prime–Archimedean programme. Not a proof of global Weil positivity or RH. Fake F_theta and DH controls still required for any proposed global supplier.
