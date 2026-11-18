# 2026-11-18 — Global arithmetic No-Ghost Census: Jensen, Burnol, and the precise saturation problem

Author: GPT/Discovery2 (Daniel Toupin / Golden Physics Project). This is a consolidation of known Balazard–Saias–Yor and Burnol/Nyman–Beurling identities with a finite-radius/no-ghost index formulation. **It is NOT a proof of RH.** Read ONON v5.2.1.3 (Spectral-Weil Identification, No-Ghost constraint, Cesàro invariant mean) and GPPVerify OneGhostReduction, FiniteNoGhost, FiniteModelSpaceReflectionNoGo, the prior D2 Hardy/Connes and WWIF notes. No manuscript changed.

## 1. Exact three-way global identity: boundary logarithm = zero census = Hardy ghost norm

Set w=(s−1)/s, s=1/(1−w), and F(w)=w ζ(1/(1−w)) for |w|<1. The s=1 pole is removed; F(0)=1. The right half-plane Re(s)>1/2 maps to the unit disk. Each hypothetical right-half zero ρ of ζ maps to a=(ρ−1)/ρ∈D, multiplicity preserved.

Define finite-radius circular log mean:
  G(r)=1/(2π)∫_0^{2π} log|F(r e^{iθ})|dθ, 0<r<1.
Jensen's formula, with F(0)=1, gives EXACTLY
  G(r)=Σ_{|a|<r} m_a log(r/|a|)≥0.
In particular G(r) is continuous, nondecreasing, and piecewise differentiable with
  r G'(r)=N(r):=Σ_{|a|<r}m_a
at radii free of zeros. This yields the *scale-census* identity
  G(r)=∫_0^r N(u)/u du.
The winding number (1/2πi)∮_{|w|=r}F'(w)/F(w)dw is N(r), when there are no zeros on the contour.

Balazard–Saias–Yor (1999) supplies the global boundary limit:
  G_*:=lim_{r↑1}G(r)
      = 1/(2π)∫_R log|ζ(1/2+it)|/(1/4+t²)dt
      = Σ_{Reρ>1/2}mρ log|ρ/(1−ρ)|≥0.
The weighted measure dt/[2π(1/4+t²)] is exactly the harmonic measure at s=1, i.e. the normalized Haar/Cauchy angular measure induced by Cayley compactification (do not call it the full Haar measure of the idele class group).

Let B be the Blaschke factor of all zeros in Re(s)>1/2 transferred to D, and K_B=H²(D)⊖BH²(D). Its vacuum/constant-vector leakage obeys the Burnol/Hardy projection identity
  D:=||P_{K_B}1||²=1−|B(0)|²,
  |B(0)|=∏_{a}|a|^{m_a}=exp(−G_*).
Therefore the EXACT integrated ghost census is

  [boxed]  D=1−exp(−2 G_*)=1−exp(−2∫_0^1 N(r)/r dr).

Equivalent no-ghost conditions:
  RH  ⇔  N(r)=0 for every 0<r<1
      ⇔  G(r)=0 for every 0<r<1
      ⇔  G_*=0
      ⇔  D=0
      ⇔  K_B={0}
      ⇔  B is a unimodular constant.
These equivalences are classical consequences of Jensen/BSY and Nyman–Burnol, not a new RH theorem.

A useful **noncircular sufficient analytic target** is ANY one sequence r_j↑1 with G(r_j)→0 (because G(r)≥0 and is monotone); or an independently proved upper bound G(r)≤ε(r) with ε(r)→0 as r↑1. That upper bound is RH-strength and has not been established. A theorem merely asserting G(r)≥0 is automatic Jensen positivity and is not useful: **RH is SATURATION of Jensen, not positivity of Jensen**.

## 2. The two WWIF faces cancel SIGNED anomalies even in fake models

The involution s↦1−conj(s) exchanges the two hemispheres of the sphere (w↦1/conj w). It pairs a right-half zero with a left-half zero. If one assigns a signed left-minus-right ghost charge, the pair cancels automatically for ALL completed reflection-symmetric fake models. This is NOT absence of ghosts. A genuine no-ghost theorem must establish the UNSIGNED G_*=0, not merely G_+−G_−=0. This precisely separates a redundant two-face CPT/shadow description from a positive definite physical spectrum.

For a nonreal right-half zero ρ=σ+iγ (σ>1/2), conjugation supplies its partner \barρ. Put q=|(ρ−1)/ρ|²=1−(2σ−1)/(σ²+γ²)<1. The pair forces
  G_*≥−log q,
  D≥1−q²
  =1−[1−(2σ−1)/(σ²+γ²)]²>0.
The previous single-zero lower bound D≥1−q remains true; the pair improves it, assuming zero and conjugate have the stated multiplicity.

## 3. Quantitative finite approximation / a real arithmetic proof target

Under the standard Mellin isometry L²(0,1)→H²(Re s>1/2), the Nyman functions ρ_λ(u)={λ/u}−λ{1/u} (0<λ≤1) have transform
  h_λ(s)=(λ−λ^s) ζ(s)/s.
These are analytic Hardy functions whose values at every hypothetical right-half ζ-zero ρ vanish. Via U:H²(C_{1/2})→H²(D), (Uf)(w)=f(1/(1−w))/(1−w), the target 1/s maps to constant 1.

For arbitrary finite linear combinations h of the transformed Nyman functions, the evaluation inequality at a=(ρ−1)/ρ gives the exact single-zero witness
  ||1−h||²_{H²(D)} ≥ 1−|a|² = (2σ−1)/(σ²+γ²).
For finitely many distinct putative zeros a_1,...,a_m, let K_ij=(1−\bar a_i a_j)^{-1}; the sharper extremal bound is
  ||1−h||² ≥ 1^* K^{-1}1.
The proof is orthogonal projection of 1−h onto the span of reproducing kernels k_{a_j}, where (1−h)(a_j)=1. This is a **zero-obstruction bound**, not a successful global upper bound. A zero-independent construction of Nyman coefficients with error→0 would force RH; that is the genuinely missing arithmetic task.

Illustrative exact elementary one-function computation: for λ=1/2, ρ_{1/2}(u)=(1/2) if floor(1/u) is odd and 0 otherwise. Thus <1,ρ_{1/2}>=(log2)/2, ||ρ_{1/2}||²=(log2)/4, and optimally approximating 1 by cρ_{1/2} gives squared distance 1−log2. This is a genuine finite arithmetic Gram calculation without zero inputs but is far too large to certify high critical-strip zero-free regions.

## 4. Where the current ONON No-Ghost proof fails

Source: ONON-5-2-1-3.tex §Spectral-Weil Identification and §Ghost states and why they cannot exist (roughly lines 16858–16935 and 20119–20209). Do not silently reuse that proof as unconditional.

- The idele class group C_Q≅K×R_{>0} has infinite multiplicative Haar volume due to ∫_0∞dr/r=∞. Its free scaling generator i d/du on L²(R×K) has purely continuous spectrum and no nonzero L² eigenvectors. A statement 'every zero ordinate is an L² eigenvalue of free A' contradicts this. The functional equation alone gives no such discrete spectrum.
- The document asserts every Hilbert–Schmidt operator is trace class in its spectral-Weil derivation. False: trace class is strictly smaller than Hilbert–Schmidt. For example diagonal eigenvalues 1/n are HS since Σn^-2<∞, but not trace class since Σn^-1 diverges. Combined with the infinite-volume assertion, the proposed identification μ_A=μ_W is not established.
- In §No-Ghost it prints a regularized 'norm' ∫ r^{2σ−1}dr/(2logR) but then evaluates it as if using Haar dr/r. Correct Haar expression (1/(2logR))∫_{1/R}^R r^{2σ−1} dr/r equals 1 at σ=1/2 and +∞ at BOTH σ>1/2 and σ<1/2, due symmetry r↔1/r. It never equals 0 for σ<1/2. Further, the regularized mean on almost-periodic modes is not the ordinary L² norm; real spectral characters are generalized plane waves.
- The ONON argument that unitarity makes all conformal primaries principal-series is too broad without a *faithful physical spectral identification*: excluding off-principal representations from one Plancherel decomposition does not establish that every analytic ζ zero corresponds to an included state.
- A positive Wiener/pushforward density or a positive Haar state is not the completed **signed Weil form**. The missing implication is exactly what the claimed proof needs to demonstrate.

This is an audit, not a rejection of the boundary-first research program. It names the analytic/representation theorem that remains to be built.

## 5. Near-term work that cannot be mistaken for RH

1. Correct the ONON source only after Daniel authorizes a paper edit; keep a dated errata note now.
2. Formalize the *finite-dimensional* kernel/Gram bound and signed-cancellation vs unsigned-defect separation, perhaps in Verify as reusable analytic tools; these require a named consumer and Lean CI.
3. Compute G(r) from **full normalized** F on a sequence r↑1 with rigorous intervals (include a shifted completed Fθ fake), but these are finite zero-free-region certificates only; no extrapolation.
4. Seek a direct prime+Tate/Poisson-derived analytic **upper bound** on G(r) tending to zero, or a uniform Nyman approximation error→0. Existing reflection symmetry and local positive factors only show nonnegativity / equal signed sectors and CANNOT supply this upper bound.
5. Cross-check the actual completed Weil quadratic form separately; the Hardy/BSY scalar defect is a global *equivalent* no-ghost measure, not literally Weil form W.

Source attribution: Balazard–Saias–Yor (1999) arithmetic critical-line log integral; Burnol/Nyman–Beurling (model-space defect); Cayley/Jensen/Pick kernels classical; independent proof synthesis and toy check by D2. Symmetric two-zero toy check: choose a=0.6+0.2i, F(w)=(1−w/a)(1−w/conj a) with F(0)=1; numerical angular mean G(1)=−log|a|²=0.916290731874155 and Hardy leakage 1−|a|⁴=0.84, machine residual ≈2.3e−16. **No RH or full Weil positivity claimed.**


## 6. Representation-theoretic caution: Plancherel support is not the entire unitary dual

The ordinary spherical Plancherel decomposition uses principal-series representations, but SL(2,C) also has complementary-series unitary representations. The book's inference "Re Δ ≠ 1 ⇒ negative norm in every unitary representation" is too broad. A zero Plancherel weight in the regular L² representation means *that representation is not a regular Plancherel summand*, not that it defines a negative-norm or zero-norm vector in every other Hilbert representation. A proof using the celestial principal series therefore additionally needs a faithful spectrum map that does not discard off-line analytic zeros as resonances. This is independent of the correct principal-series Mellin kinematics.

Example source: classification of SL(2,C) unitary dual, including principal, complementary and trivial representations (see standard representation theory and https://www.math.u-bordeaux.fr/~eprovenzi/include/tesidott.pdf Theorem 2.9.2). This matters to ONON "Ghost Theorem" §15720 as well as "Unitarity and No-Ghost" §9873.
