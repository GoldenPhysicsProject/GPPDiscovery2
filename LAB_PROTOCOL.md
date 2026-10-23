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

## Threat model

The runner executes **trusted catalog scripts** with no shell interpolation, source hashes, fixed cwd, timeouts, and reproducible output hashes. It is **not** a process sandbox and cannot promise that scripts have no filesystem or network side effects; code review remains necessary. The committed manifest intentionally contains no credentials or private inputs.
