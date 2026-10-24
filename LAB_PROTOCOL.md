# RH discovery lab — executable research protocol

This is Codex's **public experimental workbench** in GPPDiscovery2. It is not a repository of claimed RH proofs. Private research journals, source coordination, and unpublished arguments belong only in the GPP-bridge Codex area, with periodic Codex Supabase backups. Other teammates' repositories are readable references, not writable homes.

## Command interface

From the repository root, with Python 3.11 or later:

```bash
python -m rh_lab.cli list
python -m rh_lab.cli check
python -m unittest discover -s tests -v
python -m rh_lab.cli run fake_quartet_control --replay
python -m rh_lab.cli run sine2_cross_trace_budget --replay
python -m rh_lab.cli run sine2_cross_arb --replay  # optional python-flint==0.9.0
python -m rh_lab.cli run ftheta_full_s1_annihilator --replay  # optional numpy/scipy
python -m rh_lab.cli run annihilator_zero_spectral_pairing --replay  # optional mpmath 1.4.1, numpy/scipy
python -m rh_lab.cli run translation_laplace_pole_control --replay  # optional mpmath 1.4.1
python -m rh_lab.cli smoke
```

Core exact scripts need **no installed packages**. Optional Arb cross-check uses `python-flint`, and existing exploratory scripts may require `requirements.txt`. Free GitHub Actions runs the exact core on three Python versions and uploads JSON manifests. Run records are local under `.rh_runs/`, excluded from version control; explicitly chosen, independently reviewed certificate fixtures can be checked into the repo.
`stdin_from` in the catalog declares a producer→verifier pipe. Both are invoked by the runner **without** a shell and the generated input's SHA-256 is included in the run manifest; replay regenerates and checks the input too. A separate free Actions job installs `python-flint==0.9.0` and executes the independent 256-bit Arb comparison.

## Experimental gate

1. **Scope.** Record the exact source definition, normalization, domain, finite/infinite distinction, and dependence on RH or an RH-equivalent statement.
2. **Cheapest falsifier.** State the simplest explicit countermodel or violated parameter regime first, then test it. Run fake-function controls against any conclusion resting only on functional-equation symmetry, principal-series labeling or positivity restricted to the line.
3. **Numerical regime.** Separate arithmetic/source error, discretization, quadrature, truncation, interval rounding, and conditioning. Arb comparisons do not automatically certify an unproved source identity.
4. **Rigorous promotion.** Use exact rationals or directed balls plus a proved infinite-tail estimate. Certify the full *target* with the same support/basis/normalization, not an analogous cross term.
5. **Global promotion.** An all-K estimate, operator-domain theorem, and regulator removal require separate analytic proofs. A finite positive matrix never certifies RH on its own.
6. **Lean promotion.** A formally kernel-checked result applies only to its exact Lean statement and premises. In particular, a model theorem with a missing source-identification hypothesis does not resolve that hypothesis.
7. **Communication.** Transfer reproducible scripts and their public conclusions here; private mathematical notes to Codex's area of GPP-bridge; substantive findings/questions to PR #11; validated Lean targets to Codex's own GPPVerify workbench.

## Evidence semantics

`hypothesis` and `numerical` indicate discovery; `interval_certified` means machine-checkable finite error enclosures; `paper_proved` means a human-checkable analytic argument (not automatically peer-reviewed); `lean_kernel_checked` requires an actual separately identified Lean proof. Labels belong to **specific claims** and are never promoted by the runner. `rh_lab/catalog.json` stores assumptions, falsifiers, and limitations, alongside scripts.

## First active attack: the cross-Arch compensator

The Wave234 sine² **cross** matrix is a negative Gram sum (C=-\sum_n L_nL_n^T). The rational artifact `experiments/arch_hankel_sine2_k6_intervals.json` encloses every entry of this one block. The new `arch_cross_trace_gate.py` extracts an exact **necessary** compensation budget: if a separately defined Hermitian (B) in the *same normalization* satisfies (B+C\succeq0), then

\[
\mathrm{tr}(B)\geq -\mathrm{tr}(C),\qquad
\lambda_{\max}(B)\geq \max_j(-C_{jj})\geq -\mathrm{tr}(C)/6
\]

More sharply, the fixed integer direction (v=(1000,692,485,342,241,170))
gives the **exact rational Rayleigh witness**

\[
\lambda_{\max}(B)\ \ge\ {v^*Bv\over v^*v}\ \ge\
{v^*(-C)v\over v^*v}\ >\ 0.2138.
\]

The last inequality is checked using the rigorous *upper* interval endpoint
for each cross-Arch entry and only positive integer arithmetic. It is a
**necessary** lower bound on a compensator's largest eigenvalue, not evidence
that an arithmetic compensator exists or that its actual Rayleigh quotient
passes this test.

### A noncoercivity theorem, valid at every finite K

The strictly negative cross-Arch block has a second, apparently paradoxical
feature: its smallest absolute eigenvalue shrinks at least super-exponentially
with the number of translated bumps. Put

\[
\Lambda_K=2K-\tfrac32,\qquad
X_K=\tfrac75(K-1)(K-\tfrac32)+\tfrac7{10}\Lambda_K.
\]

Then the **explicit** annihilating polynomial

\[
P_K(z)=\prod_{m=0}^{K-2}(z-e^{-\frac7{10}(2m+1/2)})
\]

gives a real nonzero coefficient vector in the K-bump basis whose first
K-1 Arch Laplace moments vanish. The remaining tail proves

\[
0<\lambda_{\min}(-C_K)\le
\frac{e^{-X_K}}{\Lambda_K^2(1-e^{-7/5})}.
\]

The paper proof is in `experiments/arch_cross_superexp_null.py` and its
finite numerical corollaries are independently checked using **exact rational
Taylor inequalities**: at K=6 the minimal eigenvalue is below 1e-18; at
K=10 it is below 1e-52. This is strictly a statement about cross-Arch,
not the **completed** form. It explains why even 1e-16 entrywise intervals
are insufficient to certify a tiny lower spectral margin at K=6.

An infinite-dimensional strengthening follows for compactly supported
functions on any interval [a,b] contained in (0,infinity): the negative
cross kernel is strictly positive as a quadratic form after sign reversal.
Indeed L_n(f)=0 for all n would, under x=e^{-2u}, annihilate all polynomial
moments of the finite measure (1/2)f(-log x/2)x^{-3/4}dx. Polynomial density
forces f=0. Yet the operator on L²([a,b]) is compact (continuous kernel),
so there is **no uniform lower spectral gap** on that infinite-dimensional
space. This is compatible with positivity; it rules out coercivity of the
cross-Arch operator alone.

### Exact shifted-frequency adversarial discriminator

For the Wave234 folded control \(F_{1/4}(s)=\zeta(s-1/4)\zeta(s+1/4)\), the
cross-Arch kernel is \(k_\theta(w)=2\cosh(\theta w)k_0(w)\). It has Laplace
rates \(\lambda_n\pm\theta\), so the exact annihilating polynomial above
fails to vanish at the shifted rate \(\lambda_0-1/4=1/4\). The first
shifted Gram square supplies a *strict* lower bound, and the full unshifted
tail supplies an *upper* bound, on the **same exact coefficient vector**.

`experiments/arch_ftheta_shift_gap.py` certifies at K=6 that
\(R_{1/4}(v)>10^{14}R_0(v)\), and at K=10 that
\(R_{1/4}(v)>10^{50}R_0(v)\), entirely through rational arithmetic and
outward intervals. This is an exceptionally sensitive **cross-channel
spectral discriminator**; it does **not** establish that the full theta
Weil form is indefinite, nor that the full zeta Weil form is positive.
An independent 384-bit `python-flint` Arb implementation re-evaluates the
shifted one-mode witness and the finite unshifted head in
`experiments/arch_ftheta_shift_arb_crosscheck.py`; the optional CI Arb job
executes this separately from the fixed-point interval engine.

Next target: obtain an exact source-to-target map for (B), enclose prime, pole, and diagonal-Arch contributions, then test the complete (K=6\) matrix and uniform (K\to\infty\) inequalities. The distinct rounded `Phat6` does **not** inherit any enclosure from the cross block until this map is established.

### Source-normalized full S1 probe: a PNT-residual identity

Using the *same* annihilator coefficients from the preceding cross-Arch
experiment, `experiments/arch_annihilator_full_s1_probe.py` now assembles
the complete **Wave234 S1** prime, pole and gamma/Arch parity scalars.
The two prime contractions can be evaluated efficiently using the
autocorrelation coefficients of \(P_K\) and the coefficients of \(P_K^2\)
respectively. Source normalization was independently checked by assembling
the entire parity matrices: at K=6 the resulting minimum eigenvalues agree
with Turbo's Wave234 table for both zeta and \(F_{1/4}\).

Two algebraic observations are valid *exactly*, independently of quadrature:

1. With \(r_m=r_0q^m\), \(r_0=e^{-7/20}\), \(q=e^{-7/5}\), the reversed
   coefficient vector of \(P_K(z)=\prod_{m=0}^{K-2}(z-r_0q^m)\) is given by
   the **finite Gaussian q-binomial formula**

   \[
   v_{K-1-j}=(-r_0)^j q^{j(j-1)/2}
   \begin{bmatrix}K-1\\j\end{bmatrix}_q.
   \]

   It converges for fixed j to an edge profile with Gaussian q-binomial
   replaced by \(1/(q;q)_j\); the resulting coefficient sequence decays
   superexponentially in j. The test vectors are hence an explicit
   q-series boundary filter, not accidental numerical eigenvectors.

2. Let \(V_K(u)=\sum_jv_j b_0(u-a_j)\). Because the sine-squared bump is
   symmetric about its midpoint, the sewing autocorrelation
   \(C_V(t)=\sum_{jk}v_jv_kG_0(t-a_j-a_k-1)\) is **exactly** the convolution
   \((V_K*V_K)(t)\). Thus its continuous PNT density contribution satisfies

   \[
   \int_0^\infty e^{t/2} C_V(t)\,dt
   =\left(\int_0^\infty e^{u/2}V_K(u)\,du\right)^2=:A_K^2.
   \]

   The polynomial has the root \(r_0=e^{-7/20}\), so the *opposite*
   \(e^{-u/2}\) Mellin moment vanishes exactly; consequently the zeta
   **diagonal pole term vanishes**, and its even/odd pole contributions
   are \(\pm A_K^2\). Define the weighted prime/PNT discrepancy
   \(\mathcal E_K^{\mathrm{prime}}=X_{V_K}-A_K^2\), with
   \(X_{V_K}=\sum_n\Lambda(n)n^{-1/2} C_V(\log n)\). Put
   \(E_K=\mathrm{Arch}_{++}(V_K)-2D_K\), where \(2D_K\) is the diagonal
   prime term, and \(C_K=\mathrm{Arch}_{+-}(V_K)\). The *full* zeta parity
   Rayleigh numerators therefore obey the **exact structural identity**

   \[
   \boxed{P^+_K(V_K)=E_K+C_K-\mathcal E_K^{\mathrm{prime}},\quad
   P^-_K(V_K)=E_K-C_K+\mathcal E_K^{\mathrm{prime}}.}
   \]

   Hence nonnegativity on **this family of directions** is exactly
   \(E_K\ge|\mathcal E_K^{\mathrm{prime}}-C_K|\). Proving it uniformly
   remains an open arithmetic estimate. It is much narrower than a proof
   of global Weil positivity or RH.

The optional `arch_annihilator_s1_source_check.py` (NumPy/SciPy) yields:

| K | object | \(P^+(V_K)/\|v\|^2\) | \(P^-(V_K)/\|v\|^2\) |
|---:|---|---:|---:|
| 6 | zeta | +0.0000464383 | +0.0013671625 |
| 6 | \(F_{1/4}\) | −0.0034381234 | +0.0063762033 |
| 10 | zeta | +0.0013304888 | +0.0000838035 |
| 10 | \(F_{1/4}\) | +0.0208702571 | −0.0179306592 |

The prime sums here are finite by the exact compact bump support, but
the diagonal digamma integral is truncated and *not* rigorously enclosed.
Changing its numerical cutoff from t=500 to t=800 alters the reported
Rayleigh values by less than 1.4e−11 in these cases. This is useful source
validation and an adversarial falsifier, **not certified positivity**, nor
an identification with the Wave252 Phat6 matrix. The same vectors should
now be studied analytically for all K through the localized smoothed
prime-counting discrepancy and its explicit zero-expansion.

### Exact nontrivial-zero interference identity (classical explicit formula)

We can make that zero expansion fully explicit, without assuming RH.
Let \(\mathcal F_K(z)=\int_0^\infty V_K(u)e^{zu}\,du
=e^{a_0z}S(z)P_K(e^{\delta z})\), and let \(\rho\) range over *all*
nontrivial zeta zeros, counted with multiplicity. Since the sewing prime
test is \(C_{V_K}=V_K*V_K\), its bilateral Laplace transform is
\(\mathcal F_K(z)^2\). Mellin inversion on \(\Re z>1/2\) yields

\[
X_{V_K}={1\over 2\pi i}\int_{(c)}
\mathcal F_K(z)^2\left(-{\zeta'\over\zeta}(\tfrac12+z)\right)dz.
\]

The classical explicit-formula contour shift takes residues at the pole
\(z=1/2\), the nontrivial zeros \(z=\rho-1/2\), and the trivial zeros
\(z=-2m-1/2\), \(m\ge1\). The annihilator kills the \(m=0\) Laplace
moment exactly, so the entire folded cross-Arch sum agrees with the
negative trivial-zero contribution in this direction. The result is

\[
\boxed{X_{V_K}-A_K^2-C_K
=-\sum_{\rho}\mathcal F_K(\rho-\tfrac12)^2.}
\]

The sum converges absolutely at each finite K: the bump transform is
\(O_K((1+|\Im z|)^{-3})\) in the critical strip and the number of zeros
up to height T is \(O(T\log T)\). Complex-conjugate zeros make the sum
real. The other, diagonal half of the classical Weil explicit formula
identifies

\[
E_K=\sum_{\rho}\mathcal F_K(\rho-\tfrac12)
\mathcal F_K(\tfrac12-\rho).
\]

Thus the **complete zeta S1 parity forms on this family** are

\[
\boxed{P^\pm_K(V_K)=E_K\pm Z_K,\qquad
Z_K=\sum_{\rho}\mathcal F_K(\rho-\tfrac12)^2.}
\]

When RH holds, \(\rho=1/2+i\gamma\), so combining conjugates makes
\(P^+=4\sum_{\gamma>0}(\Re\mathcal F_K(i\gamma))^2\) and
\(P^-=4\sum_{\gamma>0}(\Im\mathcal F_K(i\gamma))^2\), with
multiplicity. This is a **conditional positivity explanation**, not
a proof of RH. The fake \(F_{1/4}\) shifts the zero arguments by
\(\pm1/4\); in general \(\mathcal F(z)\mathcal F(-z)\) is no longer a
square modulus.

The independent mpmath experiment
`experiments/annihilator_zero_spectral_check.py` compares the first 120
**known on-line zero pairs** and their controlled \(\pm1/4\) shifts to
the separately computed prime/pole/gamma matrices at K6 and K10. All
eight diagonal/sewing comparisons agree within 1e−8; this is a
convergence cross-check, **not a proof that no other off-line zeros exist**
or a rigorously bounded zero tail. The exact exponential boundary-mode
expansion is

\[
\mathcal F_K(z)=e^{a_0 z}S(z)e^{\delta(K-1)z}
\prod_{m=0}^{K-2}(1-r_m e^{-\delta z}).
\]

For every *fixed* \(z\) with \(\Re z>0\), its infinite product tends
to a nonzero q-Pochhammer factor and \(S(z)\neq0\). An individual
hypothetical off-critical zero to the right would therefore introduce
a nonzero exponentially growing oscillatory term into \(Z_K\). The
unproved difficulty is showing such terms cannot cancel *collectively*
across the complete zeta zero set, especially without a maximally
rightward zero or when phases alias on the discrete K lattice. That is
a genuine possible next attack, not a theorem established here.

### Continuous translation: a fixed-profile noncancellation theorem

The preceding spectral-aliasing obstruction disappears if one freezes
\(K\ge2\) and varies the bump train's **overall real translation** \(a\)
continuously, rather than inferring growth from the discrete K sequence.
Put

\[
W_K(z)=S(z)P_K(e^{\delta z}),\quad
V_{K,a}(u)=\sum_j v_j b_0(u-a-\delta j),\quad
\mathcal F_{K,a}(z)=e^{az}W_K(z).
\]

The exact sewn full-form scalar is

\[
C_K(a)=\sum_\rho m_\rho W_K(\rho-\tfrac12)^2
e^{2a(\rho-1/2)},
\]

whose coefficients are absolutely summable, and \(m_\rho\) denotes
the multiplicity of \(\rho\). Crucially \(W_K(z)\neq0\) throughout
\(\Re z>0\): the
polynomial roots have real part \(-2m-1/2<0\) and the sine-squared
Laplace factor has no zeros for \(\Re z>0\).

**Theorem (fixed-profile continuous-translation spectral test).** For
any one fixed \(K\ge2\), the assertion \(C_K(a)\) is bounded for every
real \(a\ge a_* >0\) is *equivalent to RH*. This is a mathematically
complete equivalence, NOT proof that the bound holds.

*Proof.* If RH holds, all \(\rho-1/2\) are imaginary and the absolute
sum of coefficients bounds \(|C_K(a)|\) uniformly. Conversely, bounded
\(C_K(a)\) makes

\[
L_K(p)=\int_{a_*}^\infty e^{-pa}C_K(a)\,da
\]

holomorphic for \(\Re p>0\). On \(\Re p>1\), absolute convergence
permits exchanging sum and integral, giving

\[
L_K(p)=\sum_\rho
\frac{m_\rho W_K(\rho-\tfrac12)^2
e^{-[p-2(\rho-1/2)]a_*}}{p-2(\rho-1/2)}.
\]

The right side extends meromorphically across \(\Re p>0\), normally
convergent away from its discrete poles. A hypothetical off-line zero
\(\Re\rho>1/2\) creates a genuine pole at
\(p=2(\rho-1/2)\) of residue \(m_\rho W_K(\rho-1/2)^2\neq0\).
No distinct zero can cancel that residue at the same point. Analytic
continuation contradicts holomorphy of \(L_K\). Functional-equation
symmetry then yields RH. \(\square\)

This **resolves collective spectral cancellation for continuous
translations**, and shows that proving a uniform prime–Archimedean
sewing bound for even a single fixed profile is sufficient. Such a
bound is itself RH-strength and **is still missing**; the theorem does
not establish positivity of the original form. It does not apply
without further work to the discrete \(K\to\infty\) sequence, where
phase aliases can occur.

**Prior-art correction within GPPVerify (24 October 2026).** The core
bounded-detector \(\Rightarrow\) RH implication was **already
kernel-checked** on main in `GppVerify/RiemannHypothesis/GroundStateDetector.lean`
(PR #418) for a *single* sine-squared window. That Lean proof goes
directly from the prime-side Laplace transform to a zero-free region
using `GppSineSquarePacket.S_ne_zero`; it does **not** require summing
zeros. `SingleQuartetInjection.lean` (PR #422) already addresses
single-mode growth and a blind sampling lattice. The q-polynomial
window above, its explicit trivial-zero/PNT cancellation and the
independent complete Wave234 source checks are the present experiment's
additional content. Do **not** count this fixed-profile bound criterion
as a newly solved RH front. The window-generic Lean extension remains
proposed, and the unconditional arithmetic bound remains the obstacle.

Numerical planted-zero control:
`experiments/translation_laplace_pole_probe.py` uses the first 60
known on-line zero pairs (not all zeta zeros), then their \(\pm1/4\)
shifts. At K6 the RMS interference over unit-length translation
windows stays around 0.00088 for the known on-line terms but grows
from roughly 0.0068 near a=.35 to 1516 near a=25 for the planted
off-critical terms. These are **finite zero-mode demonstrations**,
not estimates for the actual complete arithmetic function.

### Independent arithmetic translation scan (24 October)

`experiments/translated_arithmetic_sewing_scan.py` now evaluates the
**finite, exactly supported prime-power source side** at each continuous
translation (V_{K,a}(u)=V_K(u-a)). Unlike the prior planted-zero test,
the primary signal is computed *without* using any zeros. The exact
translation identities in the source's normalization are

\[
E_K=\mathrm{Arch}_{\rm diag}(V_K)-2D(V_K),\qquad
C_K(a)=C_{\rm arch}(a)-\left[X_K(a)-e^a A_K^2\right],
\quad P_K^\pm(a)=E_K\pm C_K(a).
\]

Here (X_K(a)=\sum_n\Lambda(n)n^{-1/2}(V_{K,a}*V_{K,a})(\log n)),
(A_K=\int e^{u/2}V_K(u)\,du), and
(C_{\rm arch}(a)=-\sum_{m\ge0}e^{-2\lambda_m a}M_m(V_K)^2).
The diagonal (E_K) is translation-invariant; the pole is **exactly**
(e^a A_K^2) because the other Mellin moment was annihilated.

At K=6, the SciPy (t\le500) gamma quadrature gives
(E_6\approx0.0013450382195147), in the **unnormalized** fixed-vector
form. A source-side scan (a=0,.02,\ldots,3) yields a smallest sampled
parity gap of roughly (9.234\cdot10^{-6}) at (a=2.34); its sewing
amplitude uses **99.31%** of the even budget. Independently, the first
120 *known on-line* zero pairs reproduce source sewing at 11 sampled
translations (0\le a\le2) with maximum discrepancy
(<6.3\cdot10^{-11}). The first known zero pair already contributes
about 91.7% of (E_6) to the diagonal spectral weight, and the first
two about 99.15%. The near-saturation thus has a concrete low-mode
interference interpretation, not a mysterious source instability.

These numbers are **numerical, finite-window and finite-zero checks**.
The gamma cutoff error is not a certified infinite-tail enclosure;
unobserved zeros are not ruled out. A finite scan does not establish
(|C_K(a)|\le E_K) for every real (a\), much less the RH-strength
unconditional uniform bound. Turbo independently audited the K=6
unshifted source and the distinction between this fixed-window
smoothed-PNT residual and its stepwise Schur-border fluctuation in
GPP-bridge PR #11, Wave269.

## Threat model

The runner executes **trusted catalog scripts** with no shell interpolation, source hashes, fixed cwd, timeouts, and reproducible output hashes. It is **not** a process sandbox and cannot promise that scripts have no filesystem or network side effects; code review remains necessary. The committed manifest intentionally contains no credentials or private inputs.
