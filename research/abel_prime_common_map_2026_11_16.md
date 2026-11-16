# An explicit common linear map from prime resolvents to Abel–Cesàro characters

16 November 2026 | GPT research seat | Discovery2 workbench | analytic draft for Turbo audit

## Scope and provenance

This note advances the plan in the uploaded "Put the arithmetic–Cesàro–celestial construction to work" document. The starting arithmetic identity is already in GPPVerify main, files ShiftPresentation.lean, TwoSpaceForm.lean, BNPositivity.lean, PRs #614–615. The Abel state and GNS at the limit are on Flint's flint/workbench branch (CesaroAbelState.lean, CesaroGNS.lean, CesaroWeilGram.lean).

**Claim here:** a constructive, arithmetic-input, COMMON LINEAR map into *single scalar finite-character* Abel–Cesàro spaces whose mixed Gram pairings converge to the existing *positive prime-resolvent block*. This does not realize the full Weil form. The pole, gamma/archimedean block and the signed prime mass defect are not absorbed. No claim about ARP, OB6, RH or celestial dynamical reconstruction.

The construction is not the circular procedure "choose the square root of an assumed positive Weil value": each map is explicitly built out of the already defined prime shift resolvents, a universal rational-frequency basis, and finite Gram-matrix inversion. It is a positive-block realization, not a completed positivity proof.

## Definitions

Work first over the complex Hilbert space H = L²(R,dx), with inner product conjugate linear in the first slot. For ε > 0 let A_ε = L²(R, ε exp(−ε|u|)du), the completion of finite imaginary-character sums under Flint's integral Abel form. Its normalization has ||1||² = 2.

For real frequencies ξ,η,

  <exp(iξu),exp(iηu)>_{A_ε} = 2 ε² / [ε² + (η−ξ)²].                  (A)

For a prime p define ℓ_p = log p, q_p = p^(−1/2), U_p f(x) = f(x−ℓ_p),

  Φ_p = (I−q_p U_p)^(-1) = sum_{k≥0} q_p^k U_p^k,
  w_p = (log p)(1−p^(−1)) > 0.

The actual existing prime Gram block is

  C_N : H → ⊕_{p≤N, prime} H,
  (C_N f)_p = sqrt(w_p) Φ_p f,
  P_N(f,g) = <C_N f,C_N g> = sum_{p≤N} w_p <Φ_p f,Φ_p g>.             (B)

For compact smooth real functions, GPPVerify's normSq_CN identifies P_N(f,f) with shiftGramSum N f. The completion and complex polarization here are analytic extensions, not claims already built by Lean.

## Theorem 1: canonical finite-character approximation of the positive prime block

Fix N≥2 and enumerate the rationals without repeats as τ₁,τ₂,... . Put

  b_j(x)=exp(−|x|/2) exp(iτ_j x) ∈ H,
  G_m(i,j)=<b_i,b_j>=2/[1+(τ_j−τ_i)²], 1≤i,j≤m.

Then G_m is strictly positive definite, and the closed span of all b_j is H.

**Proof:** G_m is Gram, and a finite exponential polynomial with distinct real frequencies cannot vanish almost everywhere; hence positive definite. If h is perpendicular to every b_j, the Fourier transform of exp(−|x|/2) conjugate(h(x)), which is in L¹ by Cauchy–Schwarz, vanishes at all rational frequencies. Continuity gives vanishing at every real frequency; Fourier uniqueness implies h=0. Thus the increasing finite-rank orthogonal projections Q_m onto span{b₁,...,b_m} tend strongly to I.

Explicitly, Q_m h = sum_j a_j(h)b_j, where

  a(h)=G_m^(-1) v(h),       v_i(h)=<b_i,h>.                           (C)

This is one common linear operator on H; coefficients are not selected separately for individual quadratic values.

For each prime let h_p(f)=sqrt(w_p)Φ_p f, δ_p=log p, and form the scalar FINITE character sum

  J_{ε,m,N} f(u) = sum_{p≤N prime} sum_{j=1}^m
                    a_j(h_p(f)) exp(i[δ_p+ετ_j]u).                 (D)

Every exponent has real part zero. Therefore the entire map stays inside the positive-integral domain |Re α|<ε/2, for every ε>0. It is linear in f, and for each finite m it has finite-character output.

For each fixed m, its Abel Gram tends as ε↓0 to

  sum_{p≤N} <Q_m h_p(f),Q_m h_p(g)>.

Indeed, the same-prime blocks have Gram G_m EXACTLY for every ε by (A); different-prime blocks have entries

  C_{pq}^{(m)}(ε)_{ij}
    = 2 ε²/[ε²+(δ_q−δ_p+ε(τ_j−τ_i))²] → 0                    (E)

for p≠q, because logarithms of distinct primes are distinct.

**One-path theorem, not merely iterated limits:** There exists a deterministic m(ε)→∞, depending on N and the fixed rational enumeration but NOT on f or g, such that

  lim_{ε↓0} <J_{ε,m(ε),N} f,J_{ε,m(ε),N} g>_{A_ε}
     = P_N(f,g)                                                       (F)

for ALL f,g∈H simultaneously in the sense of pointwise pairings. In particular the resulting maps are common and linear, preserve mixed pairings in the limit, and use the actual arithmetic resolvents.

Quantitative schedule/proof: for at least two primes let r=# {p≤N}, d=min_{p≠q}|δ_p−δ_q|>0, S_m=1+max_{j≤m}|τ_j|, λ_m=lambda_min(G_m)>0. Under ε≤d/(4 S_m),

  |C_{pq,ij}^{(m)}(ε)| ≤ 8ε²/d²,
  ||C_{pq}^{(m)}(ε)||_op ≤ 8mε²/d².

Since ||a(h_p)||₂ ≤ ||h_p||_H / sqrt(λ_m), the total cross-prime pairing is bounded by

  8 r m ε² / (d² λ_m) · ||C_N f|| · ||C_N g||.                (G)

Choose decreasing η_m>0 satisfying η_m≤1/m, η_m≤d/(4 S_m), η_{m+1}<η_m/2 and 8 r m η_m²/(d² λ_m)≤1/m. Define m(ε)=max{m: ε<η_m} for sufficiently small ε. Then m(ε)→∞, the bound (G) tends to zero, and the same-prime block converges by Q_m→I. This proves (F). If r=1, no cross-prime schedule is needed.

This is a genuine single-SCALAR Abel-character realization, not a formal direct sum: prime channels are separated asymptotically by frequency carriers δ_p=log p, while their internal frequencies coalesce at the Abel scale ε. The map uses no zeta zeros and assumes no Weil positivity.

## Theorem 2: resolvent and local signed-defect controls

Fourier transform diagonalizes U_p as multiplication by exp(−iℓ_p ξ). Thus

  Φ_p^hat(ξ) = 1/[1−q_p exp(−iℓ_p ξ)],
  ||f||/(1+q_p) ≤ ||Φ_p f|| ≤ ||f||/(1−q_p).                    (H)

Both constants are sharp on H: the multiplier attains its extremal moduli at phases π and 0, respectively (approximate plane waves in L² establish sharpness). This includes p=2: 1/(1+2^(−1/2)) and 1/(1−2^(−1/2)). It discharges the analytic counterpart of Verify O2; Lean still needed.

For the actual signed single-prime Weil side of GPPVerify I1,

  D_p = (1−q_p²) Φ_p* Φ_p − I,

with Fourier multiplier

  d_p(ξ) = 2q_p [cos(ℓ_p ξ)−q_p] /
                       [1−2q_p cos(ℓ_p ξ)+q_p²].                   (I)

Its exact range is [−2q_p/(1+q_p), 2q_p/(1−q_p)]. Therefore D_p is indefinite. In particular, the local signed prime contribution log(p)<f,D_p f> CANNOT be the Gram form of a positive-state map on the full domain. Both signs occur for smooth compactly supported test functions, using long localized monochromatic packets. The negative prime mass defect may not be discarded.

For f supported on an interval shorter than ℓ_p, translated copies U_p^k f have pairwise disjoint supports. Consequently

  ||Φ_p f||² = ||f||² / (1−q_p²),     <f,D_p f>=0.              (J)

This explains the cutoff cancellation on short windows and why increasing N does not create a new domination mechanism: Verify already proves the single-cutoff equivalence.

## Theorem 3: a quantitative UNIFORM approximation obstruction

Each J_{ε,m,N} has finite rank as an operator on the infinite-dimensional source H. Therefore for every ε,m it has a unit vector f with J_{ε,m,N}f=0. But p=2 in C_N and (H) imply

  ||C_N f||² ≥ c₂ ||f||²,
  c₂ = [log 2 · (1−1/2)]/[1+2^(−1/2)]² > 0.                  (K)

So for ANY finite-rank common scalar Abel map J,

  sup_{||f||=1} | ||J f||²_{A_ε} − ||C_N f||² | ≥ c₂.           (L)

Thus the convergence in (F) is necessarily strong/pointwise, NEVER uniform in operator norm on the whole L² unit ball. This is a proved structural limitation, not an experimental failure. A uniform estimate is possible only after extra compactness or restriction of the source.

## Explicit scaling / celestial kinematics

Separately let S : L²(R_+,dr/r)→L²(R_+,dω/ω) by (Sf)(ω)=sqrt(2) f(ω²). Changing variables r=ω² proves S unitary. On formal half-density scale characters r^(s−1/2), S sends the exponent to ω^(2s−1), hence the kinematic variable Δ=2s. In logarithmic coordinates S T_{log p}=T_{(log p)/2} S. This intertwines each Φ_p with a celestial-log shift resolvent of step (log p)/2 and the same q_p. It is a representation/measure identity; it does NOT identify zeta zeros with physical celestial states or prove a bulk-boundary dynamical duality.

## Exact next obligation for Turbo/Claude/Flint

1. Audit Theorems 1–3 (especially Gram-matrix inversion, universal ε schedule and sharp finite-rank lower bound). The positive sector now has a legitimate explicit common linear finite-character map, not separate witnesses.
2. Formalize the analytic resolvent operator equality and two-sided bounds, beginning with p=2, in GPPVerify (O2); then the signed Fourier multiplier and its sign range.
3. Formalize finite-character Gram formula, strict positivity of rational-frequency Gram matrices, and convergence of off-carrier blocks. Full density may need Fourier uniqueness already in Mathlib; split small finite algebra from analytic completion.
4. Reconcile a projected B_N form with its REAL polarization and GNS construction (O1 plus polarization). The missing full-Weil map must transport **pole, archimedean and negative mass defect** alongside the positive prime Gram, not just (F).
5. Audit against off-line regulator, common-mass, oblique-compression and F_theta tests before promoting claims. Do not infer ARP/RH from (F).

**Conclusion.** A previously missing explicit common linear Abel–Cesàro realization exists for the positive prime-resolvent block. The signed complete Weil form is still the hard problem. The carrier construction provides a mathematically precise interface and a quantitative no-go for uniform finite-character approximation.
