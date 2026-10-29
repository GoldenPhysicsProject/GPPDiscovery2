> **CORRECTION / ERRATUM (Oct 29, later audit):** The 41–129 mode and multi-support Arb *numerical* margins reported below were computed before fixing a diagonal Archimedean integrand error (extra exponential multiplying the cosine subtraction). Those margins and positivity certificates are **RETRACTED** for the correct matrix. See `discovery/arb_semilocal_weil_matrix.py` corrected commit `77501012`, `discovery/semilocal_log_kinetic_decomposition.md`, and the corrected 41-mode Arb certificate workflow `40967943004`. The analytic H¹, completed logarithmic symbol, Gamma identities and fixed-support compact-resolvent lemmas below use the exact symbolic form and are unaffected. Do not cite the historical 0.26 normalized margins. The **corrected** 41-mode certificate has only a certified margin >10⁻²⁴, and a general all-N bound remains open.

# H¹ continuity and cofinal-support reduction for the exact semilocal Weil matrices

2026-10-29 · Codex / GPPDiscovery2 · analytical workbench note, not an RH proof.

## Source and exact matrix

Daniel Toupin, `arithmetic_principal_series_RH_program-34.tex`, section *The exact semilocal Weil form*. Fix λ>1 and L=2log λ. On [0,L] the orthonormal modes are

`U_n(x)=L^{-1/2} exp(2πinx/L)`.

For f∈H¹([0,L];ℂ), define the one-sided autocorrelation for 0≤y≤L:

`R_f(y)=∫₀^(L−y) f(x+y) conjugate(f(x)) dx`,
`q_f(y)=2 Re R_f(y)`; set q_f(y)=0 for y>L.

For f=U_n the diagonal q_f is `2(1−y/L) cos(2πny/L)`. For a pair (U_m,U_n), the Hermitian polarization gives the real symmetric offdiagonal kernel

`q_mn(y)=[sin(2πmy/L)−sin(2πny/L)]/[π(n−m)]` for m≠n.

Consequently for any finite Fourier polynomial `f=Σ_|n|≤N c_n U_n`, the completed Weil form evaluated on q_f coincides with `c* Q_(λ,N) c` for the actual semilocal matrix of v34, with the full pole, Archimedean and finite prime-power terms. In particular full-matrix positivity includes ALL cross-scale couplings and does not require a Gershgorin condition.

## Concrete H¹ endpoint estimate

For every f∈H¹([0,L]) and 0≤y≤L,

`R_f(y)−R_f(0)
 =∫₀^(L−y) [f(x+y)−f(x)] conjugate(f(x))dx − ∫_(L−y)^L |f(x)|²dx`.

The one-dimensional H¹ translation inequality (valid for the overlap interval) and Cauchy–Schwarz give

`||f(·+y)−f(·)||_(L²(0,L−y)) ≤ y ||f'||₂`,

hence

`|q_f(y)−q_f(0)| ≤ 2y ( ||f'||₂ ||f||₂ + ||f||_∞² )`. (1)

The 1D Sobolev embedding `H¹([0,L])↪C([0,L])` bounds the right-hand side by `C_L y ||f||_(H¹)²`, where C_L is explicit and finite for each fixed L. Polarizing the same estimate yields a locally bounded bilinear control and continuity under H¹ convergence:

`||f_k−f||_(H¹)→0` implies uniform control of `[q_(f_k)(y)−q_(f_k)(0)]/y` and convergence of these quotients in L∞(0,L) (with a suitable cross-term estimate).

In the Archimedean distribution, the potentially singular integrand is `[e^(y/2)q_f(y)−q_f(0)]/[2sinh y]`; (1) plus `e^(y/2)−1=O(y)` makes it integrably bounded and continuous in f under H¹ convergence. The Archimedean tail for y>L is the exact term `−q_f(0)atanh(e^(−L))`, also H¹-continuous; this tail must not be dropped. The pole term is a finite weighted integral on [0,L], and for each fixed λ only finitely many prime powers p^r≤e^L are sampled, each q_f(r log p) being continuous in f already in L². Therefore the **completed semilocal quadratic functional extends continuously to H¹([0,L])** for each fixed L, given the exact v34 distribution formula.

This is a standard analytic argument that should be written as an explicit lemma with constants and then formalized, independently of any spectral/RH claim. It addresses the form-continuity half of support extension and avoids operator-norm Galerkin convergence.

## Conditional dense-extension theorem

Fix λ and suppose **for every integer N≥0** the exact completed matrix `Q_(λ,N)` is PSD. Let f be any smooth function compactly supported strictly inside (0,L). Its periodic extension is smooth; symmetric Fourier partial sums `f_N` converge to f in H¹([0,L]) (indeed in every periodic Sobolev norm). Each finite f_N obeys `Ψ♯(q_(f_N))=c_N*Q_(λ,N)c_N ≥0`. H¹ continuity then gives `Ψ♯(q_f)=lim_N Ψ♯(q_(f_N)) ≥0`.

No uniform eigenvalue gap `λ_min(Q_(λ,N))≥ε` and no operator-norm convergence of compressions is required. Every cross term is already inside Q_N. Note the zero extension of individual periodic modes has endpoint jumps, but the overlap-autocorrelation formula and the H¹ **interval** topology handle them directly; do not assume the zero extensions lie in H¹(ℝ).

A **cofinal sequence of supports suffices**: choose λ_k=2^k, k≥1. Every compactly supported test lies strictly inside [λ_k^−1,λ_k] for sufficiently large k. Consequently, all-N positivity of the semilocal matrices at λ_k for every k, plus the above continuity/identification, would imply the global Weil positivity criterion. Uniform-in-λ error estimates are not necessary for this logical implication.

## Still open, explicitly

1. A proof that Q_(λ_k,N)≥0 for **all** k,N (the analytic arithmetic problem equivalent in strength to the global RH target). Arb checks through N=64 at λ=5/2 and N=32 on several dyadic scales do not give this.
2. Full documentation of the test-function normalization, complex polarization and the equivalence between Ψ♯(q_f) and the exact Weil criterion's admissible dense class. No jump in these bridges may be assumed.
3. If formalizing in Lean, first prove the interval autocorrelation/H¹ bound and the finite-matrix polarization theorem, then the closedness-of-the-positive-cone limit theorem. None of these should be encoded as an axiom.

## Certified finite diagnostics (160-bit FLINT/Arb)

At λ=5/2, N64 (129 modes), all LDL pivots strictly positive, with `0.260089 < 1+λ_min(T) < 0.260094` certified by shifted LDL and rational Rayleigh witness. Dyadic λ=2, N32 (65 modes) gap (0.261656,0.261661); λ=4,N32 gap (0.239675,0.239680); λ=8,N32 gap (0.308723,0.308728); λ=16,N32 gap (0.330676,0.330681). Each checked matrix was certified positive definite. These are finite observations, not the all-N claim.

Code: `discovery/arb_semilocal_weil_matrix.py`, `discovery/arb_one_sided_spectrum_sweep.py` on `codex/discovery-workbench`. Rigorous CI green through the earlier 129-mode sweep; extended workflow remains a separate gate.


## Exact positive Archimedean square supplier

The overlap correlation gives a second exact identity, for every 0≤y≤L:

`q_f(0)−q_f(y)
 = ∫₀^(L−y)|f(x+y)−f(x)|²dx
   +∫₀^y|f(x)|²dx
   +∫_(L−y)^L|f(x)|²dx`. (2)

This follows by expanding the interior square, then adding the two endpoint strips. No spectral hypothesis or RH is involved. Therefore the Archimedean stiffness

`E_∞(f)=∫₀^L [q_f(0)−q_f(y)]/[2sinh y]dy ≥ 0`. (3)

The integral converges by (1), and it is a positive quadratic form. Split the **exact** completed Weil distribution in the v34 convention:

`Ψ♯(q_f)
 = E_∞(f) + ∫₀^L k(y) q_f(y)dy
   + [atanh(e^(−L))−(log(4π)+γ)/2]q_f(0)
   − Σ_(p^r≤e^L) (log p)/sqrt(p^r) q_f(rlog p)`,

where

`k(y)=e^(y/2)+e^(−y/2)+(1−e^(y/2))/(2sinh y)`,

and k has a removable limit at y=0. This is a simple algebraic recombination of pole, exact Archimedean main integral and tail, and prime terms; it has NOT discarded the mandatory tail or made a sign assumption on the remainder.

Equation (3) is a canonical **unconditionally nonnegative Archimedean supplier**. The rest contains a regular (bounded on fixed windows) continuous kernel, an L² contact coefficient, and finite signed prime-shift correlations. The actual RH-strength task is to show that this positive supplier plus the regular/contact remainder dominates the signed prime energy **for every** admissible f at all cofinal windows. Large positive eigenvalues of normalized cross-coupling are entirely compatible with this decomposition.

Potential tail approach (not yet proved): (3) behaves like a logarithmic-frequency Dirichlet energy for high Fourier modes, while for each fixed λ the finite prime shift operator and the regular kernel are L²-bounded. Quantify a high-frequency coercivity lower bound with low/high Schur cross terms to reduce the all-N problem at each λ to finite rigorous low-mode certificates. A bound on individual high-mode diagonals is insufficient: low/high off-diagonal coupling must also be controlled.


## Global Fourier multiplier of the positive Archimedean supplier

Extend f by zero outside [0,L] to `\tilde f∈L²(ℝ)`. Because `q_f(y)=0` for y>L, the exact Archimedean tail absorbed in (3) gives

`E_∞^full(f)=E_∞(f)+q_f(0)atanh(e^(−L))
 = ∫₀^∞ [q_f(0)−q_f(y)]/[2sinh y]dy`,

where for y≥0 the overlap identity is simply

`q_f(0)−q_f(y) = ||\tilde f(·+y)−\tilde f||²_(L²(ℝ))`.

Using the *unitary* Fourier transform and Tonelli (nonnegative integrand), we obtain the **exact diagonal spectral representation**

`E_∞^full(f) = ∫_ℝ m(ξ) |\widehat{\tilde f}(ξ)|²dξ`,

`m(ξ)=∫₀^∞ [1−cos(ξy)]/sinh(y)dy
     =2 Σ_(j≥0) [ 1/(2j+1)−(2j+1)/((2j+1)²+ξ²) ]
     =Re ψ(1/2+iξ/2)−ψ(1/2) ≥0`,

with ψ the digamma function. The elementary proof is `1/sinh y=2Σ_(j≥0)e^(−(2j+1)y)`, integrate the Laplace transform termwise, and use the digamma partial fractions. At ξ=1, independent SciPy quadrature and complex digamma agree to ~8e−14, an auxiliary floating sanity check of the **analytically exact** identity.

The symbol satisfies `m(0)=0` and `m(ξ)=log|ξ|+O(1)` as |ξ|→∞. Hence this positive part is naturally an **unbounded logarithmic-frequency quadratic form on L²**, with form domain

`D(E)=\{f∈L²(ℝ): ∫m(ξ)|\hat f(ξ)|²dξ<∞\}`.

Compactly supported H¹ functions are in D(E). In this sense insisting on operator-norm convergence of finite-rank Galerkin operators in the unbounded L² realization is not a suitable foundational target. The relevant topology is form convergence / the graph norm of `E_∞^full`.

With the exact pole and gamma combination from the previous section, the **entire completed form** can be rewritten without any discarded tail:

`Ψ♯(q_f)=E_∞^full(f)+∫₀^L k(y)q_f(y)dy
         −[(log(4π)+γ)/2]q_f(0)
         −Σ_(p^r≤e^L)(log p)/sqrt(p^r) q_f(rlog p)`.

For **fixed λ**, the remaining regular convolution kernel, contact term and finite prime-shift correlations give L²-bounded quadratic forms on [0,L]. Thus one has a positive logarithmic-frequency principal form plus a bounded signed perturbation. This is a concrete analytic setup for a *one-sided high-frequency tail and low/high Schur-complement* strategy. Proving that the combined form is globally nonnegative is still the RH-strength problem, not established by the decomposition or finite Arb checks. In particular high-frequency coercivity alone does not control finite negative directions or offdiagonal low/high sewing.

Technical caveat: for the zero-extended f, the full-line logarithmic form may be finite for compactly supported H¹([0,L]) functions with nonzero boundary values because the symbol grows only logarithmically, even though the zero extension need not belong to global H¹.


## Fixed-support compact-resolvent and finite-negative-index reduction

The previous multiplier yields a standard *closed-form* consequence that is stronger than numerical convergence, but weaker than Weil positivity.

Let `H_L={f∈L²(ℝ): support(f)⊂[0,L]}`, a closed subspace. Define the positive form `E_L(f)=∫m(ξ)|\hat f(ξ)|²dξ` with form domain `D(E_L)=H_L∩D(m(D)^(1/2))` and Hilbert norm `(||f||₂²+E_L(f))^(1/2)`. Since m(ξ)≥0 and m(ξ)→∞ as |ξ|→∞, a form-bounded sequence has uniformly small high-frequency Fourier tails; fixed spatial support gives tightness. Fourier cutoff plus compact spatial support (Kolmogorov–Riesz) makes the form-domain embedding into H_L compact. The associated nonnegative self-adjoint operator A_L has **compact resolvent** and discrete eigenvalues tending to +∞ (counting multiplicity).

The completed remainder `R_L=Ψ♯−E_L` is explicitly **L²-bounded** at fixed L because `|q_f(y)|≤2||f||₂²`. An elementary absolute bound is

`|R_L(f)| ≤ C_L ||f||₂²`,

`C_L=2∫₀^L|k(y)|dy+|log(4π)+γ|
       +2Σ_(p^r≤e^L)(log p)p^(−r/2)`,

where k is the continuous removable-at-zero function in the preceding section. This is intentionally crude but explicit and unconditional. Therefore the completed fixed-support form `A_L+R_L` is closed, lower semibounded, self-adjoint in its form realization, and has compact resolvent. In particular it has **only finitely many negative eigenvalues** (if any).

More quantitatively, if `μ_j(A_L)` are its increasing eigenvalues, the min-max principle gives

`number of negative eigenvalues of completed form ≤ #{j: μ_j(A_L) ≤ C_L}`.

On the spectral complement `E_L(f)≥μ_(J+1)||f||₂²`; if μ_(J+1)>C_L, the full form is strictly positive there, *without* any assumption about RH. But positivity of the entire form additionally requires a **low/high Schur complement bound**, because bounded remainder cross terms can couple low and high sectors. Exact finite Arb certificates for the Fourier-Galerkin matrices cannot simply be substituted for certificates in the spectral basis of A_L without controlling this change of basis and cross couplings.

This provides a precise candidate for the previously missing *operator tail bound*: use the unbounded positive digamma operator as the comparison operator, obtain an explicit high-frequency spectral threshold from C_L, then certify the finite low-energy Schur complement. This avoids demanding operator-norm convergence of an unbounded completed form. **No all-L uniformity, all-N positivity or RH theorem is claimed here.**


## Independent numerical decomposition check and sharpness warning

At λ=5/2, the zero mode f=U₀ yields (ordinary SciPy quadrature, **not** an interval certificate for this decomposition): `E_∞^full=1.171288928002072`, regular+contact `R_reg=0.329543566735458`, prime `P=1.461650201504385`. Therefore `E_∞^full+R_reg−P=0.03918229323314515`, agreeing to floating precision with the previously independently Arb-certified exact Q₀₀≈0.03918229323314478. This checks the full-tail sign and constants in the new decomposition.

The crude all-signs-worst-case remainder bound at λ=5/2 is numerically `∫₀ᴸ|k|≈3.7107968575`, sum of prime-power weights `≈2.1907492782`, and `C_L≈14.9113321832`. Thus requiring m(ξ)>C_L based on this absolute bound would push to extremely high frequencies (roughly exp(C_L)≈3 million before constants), far beyond the tested 129 modes. **This bound is structural but not practically sharp.** Actual progress requires exploiting signs/cancellation in the regular and prime terms and a rigorous low/high cross estimate. Do not claim it already turns finite Arb positivity into a global certificate.


## Exact but limited bridge to celestial modular spectral weight

The attached manuscript `Modular_Thermality_of_the_Celestial_Spectral_Weight.tex` has the independently derived celestial phase-space factor `P(λ)=Γ(1+iλ)Γ(1−iλ)=πλ/csch(πλ)^{-1}`, i.e. `P(λ)=πλ/sinh(πλ)`, and the positive odd-ladder expansion `P(λ)=2πλ Σ_(j≥0)e^{−πλ(2j+1)}`. The new Archimedean supplier above obeys the **exact same odd-index decomposition mechanism**:

`m(ξ)=2ξ² Σ_(j≥0) 1/[(2j+1)((2j+1)²+ξ²)]`

since `csch y=2Σ_(j≥0)e^{−(2j+1)y}`. Writing `S(ξ)=Re ψ(1+iξ)−ψ(1)=Σ_(n≥1)ξ²/[n(n²+ξ²)]`, the digamma duplication formula gives the exact dyadic cancellation

`m(ξ)=2S(ξ)−S(ξ/2)`.

An independent SciPy digamma check at ξ=1.3 agrees to 7e−16. Thus the celestial modular factor and the arithmetic Weil gamma supplier both use the odd-frequency ladder of the hyperbolic cosecant/Gamma family, albeit in **different transforms and with different physical roles**: P is the cut phase-space weight, m is a positive logarithmic-frequency quadratic-form symbol. This establishes a concrete special-function and thermal-ladder bridge, **not** an identification of scattering amplitudes with prime distributions, not a bulk-boundary map, and not a proof of RH.


### Doubling from the half-shift Gamma family

Define a normalized real analytic Gamma modulus family (for a>0)

`P_a(ν)=Γ(a+iν)Γ(a−iν)/Γ(a)²`.

The celestial weight is exactly `P_1(ν)=πν/sinh(πν)`. The arithmetic positive multiplier is its **half-shift dimension derivative**

`m(ξ) = (1/2)[∂/∂a log P_a(ξ/2)]_(a=1/2)`.

This is immediate from `∂_a logΓ(a+iν)=ψ(a+iν)` and the real-part identity. Meanwhile the Γ duplication formula at `z=1/2+iξ/2` gives

`P_1(ξ) = P_1(ξ/2) P_(1/2)(ξ/2)`,

`P_(1/2)(ν)=1/cosh(πν)`,

or explicitly `P(ξ)=P(ξ/2) sech(πξ/2)`. This is an **exact scale-doubling factorization** relating the a=1/2 and a=1 unitary-axis Gamma modulus sectors. It mirrors the project's formal shift `Δ=2s` at the level of Gamma normalizers, but should not be described as a proved representation-theoretic equivalence, holographic identification or scattering/RH theorem without an actual intertwiner.


## Rigorous symbol-tail and high-Fourier subspace certificate (corrected formula)

The completed **corrected** semilocal quadratic form has a stronger exact full-line Fourier representation. For f supported in [0,L], with Fourier transform normalized by dξ/(2π),

\[
Q_L[f]=\int_{\mathbb R}H_L(\xi)|\widehat f(\xi)|^2\,\frac{d\xi}{2\pi},
\quad H_L(\xi)=m(\xi)+2\int_0^L k(y)\cos(\xi y)\,dy-c_\infty-2\sum_{p^r\le e^L}w_{p,r}\cos(\xi r\log p).
\]

This follows *exactly* from Plancherel's identity \(q_f(y)=2\int_{\mathbb R}\cos(\xi y)|\widehat f(\xi)|^2d\xi/(2\pi)\), the full Archimedean subtraction tail and the definitions in the preceding sections. It is independent of any Galerkin quadrature implementation. Here \(c_\infty=\log(4\pi)+\gamma\), \(w_{p,r}=(\log p)p^{-r/2}\), and

\[
k(y)=2\cosh(y/2)-r(y),\quad r(y)=\frac{t^2}{(t+1)(t^2+1)},\quad t=e^{y/2}.
\]

For t≥1, let \(D=t^3+t^2+t+1\). The elementary polynomial identity \(D-3t^2=t(t-1)^2+1>0\) gives \(0<r(y)≤1/3\). Also \(1≤tD'(t)/D(t)≤3\), hence \(r'(y)=r(y)[1-tD'(t)/(2D(t))]\) satisfies \(|r'(y)|≤1/6\). Since \(2\cosh(y/2)\) is increasing, integration by parts yields, for ξ≠0,

\[
\left|2\int_0^L k(y)\cos(\xi y)\,dy\right|
\le\frac{B_L}{|\xi|},\qquad B_L=8\cosh(L/2)-\frac{10}{3}+\frac L3.
\]

The odd-digamma series establishes that \(m(\xi)\) is increasing with |ξ|. Consequently, defining \(P_L=\sum_{p^r\le e^L}w_{p,r}\), for **every real** |ξ|≥R>0,

\[
H_L(\xi)\ge \gamma_L(R):=m(R)-c_\infty-2P_L-B_L/R.
\]

FLINT/Arb at 192-bit outward-rounded precision **certifies** for λ=5/2, L=2log(5/2), prime powers 2,3,4,5:

- At **R=512**, \(\gamma_L(R)\in 0.0016094462909710492443639877578951592\pm10^{-55}\), strictly positive. Thus the corrected semilocal *symbol* has no negative values for any real |ξ|≥512. The certificate is not sampled frequency data: the monotonicity and integration-by-parts inequalities transfer the one interval evaluation to the entire unbounded tail.
- At **R=1024**, \(\gamma_L(R)\in 0.70342656380156342732959110626409109\pm10^{-55}\).

A stronger full **infinite-dimensional subspace** bound follows. Let \(U_m=L^{-1/2}e^{2\pi imx/L}\) and let \(f\in\overline{\mathrm{span}}\{U_m:|m|>N\}\subset L²(0,L)\) have finite logarithmic kinetic energy. If N>RL/π then, for |ξ|≤R,

\[
|\widehat U_m(\xi)|\le\frac{2\sqrt L}{\pi|m|},\qquad
\int_{-R}^{R}|\widehat f(\xi)|²\,\frac{d\xi}{2\pi}\le \frac{8LR}{\pi^3 N}\|f\|².
\]

This uses Cauchy-Schwarz over infinitely many coefficients, Parseval and \(\sum_{m>N}m^{-2}\le1/N\). Globally, \(m≥0\), \(0≤k(y)≤2\cosh(y/2)\), so \(H_L(\xi)≥-C_L^*\) with the entirely explicit \(C_L^*=8\sinh(L/2)+c_\infty+2P_L\). Partitioning the **Fourier integral** at ±R, without discarding cross terms of the time-limited quadratic form, gives

\[
Q_L[f]\ge\left[\gamma_L(R)-\frac{8LR}{\pi^3N}\bigl(\gamma_L(R)+C_L^*\bigr)\right]\|f\|².
\]

At λ=5/2, R=1024, **N=12,000**, Arb certifies leakage ≤0.04034803314669005, \(C_L^*≈15.889738468201645\), and a strictly positive full-space high-Fourier coercivity coefficient **\(>0.03392499108179978\)**. This estimate holds for *every* (possibly infinite) linear combination of modes |m|>12000 in the form domain, not just a 24001-mode numerical test. Script `discovery/semilocal_symbol_tail_certificate.py` reproduces interval inequalities, including a failing assertion if the margin is not positive.

This materially reduces the previous direct high-Fourier threshold estimate (~1,052,008 modes) to 12,000 at this specific λ. **It does not imply Q_L≥0 on arbitrary f.** The 24,001-mode low block is not certified, and its cross coupling with the positive high subspace requires a genuine Schur complement bound. Nor is this uniform in support λ. No RH claim follows.


**Second dyadic support, independently certified:** λ=2 (L=2log2) has prime-power cutoff 4 (2,3,4), at R=256 the exact symbol tail has a strictly positive interval lower bound; at N=2,000 the infinite high-Fourier subspace has \(Q_L[f]\ge0.1520166276799536776\|f\|²\), rigorously by the same all-real-frequency analytic inequalities plus outward-rounded Arb. Both the λ=5/2 (N=12,000) and dyadic λ=2 (N=2,000) certificates run in the `arb-cross-window.yml` GitHub Actions workflow, latest commit `8b208d28cc27db7b678f2caedf753c98558e7a13`, run **40970191430 SUCCESS**. These fixed-L positive tails still leave their finite low blocks and couplings entirely open.


**Rigorous negative-symbol control at the origin:** The exact closed gamma-tilt integral from `discovery/semilocal_log_kinetic_decomposition.md` gives `H_L(0)=8sinh(L/2)−2I(L)−c∞−2P_L`, with `I(L)=log[2/(1+e^(−L/2))]−(1/2)log[2/(1+e^(−L))]+π/4−atan(e^(−L/2))`. At λ=5/2, 192-bit Arb certifies **`H_L(0)=−0.06814475320760466453958374604394319±2×10^(−56)<0`**. Thus the exact corrected full-line symbol is genuinely *indefinite* as a pointwise multiplier near ξ=0, even though corrected finite Galerkin compressions through 41 modes are rigorously positive. This is not a contradiction: a function with spatial support [0,L] cannot have its Fourier mass concentrated arbitrarily close to ξ=0. The support-induced uncertainty and low/high Schur control are essential. The CI now gates the negative-origin sign and the positive all-real-frequency tail together in `discovery/semilocal_symbol_tail_certificate.py` at commit `fee2fef99a9a8811951121ef527529ecf6b09ca3`, workflow `48fdac07c343e2636f36bf9977ab89b556766d94`.
