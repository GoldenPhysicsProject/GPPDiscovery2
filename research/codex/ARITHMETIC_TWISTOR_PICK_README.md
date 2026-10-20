# Arithmetic twistor line and Pick-kernel laboratory

This is the reproducible, exact-symbolic / high-precision-numerical companion to the GPP-bridge Codex note
`work/codex/2026-10-16_arithmetic_twistor_null_line_shadow_quotient_signed_pick_kernel.md`.

Run:
```sh
python research/codex/arithmetic_twistor_null_line_pick_20261016.py
```

**Mathematical content.** Daniel's Cayley coordinate w=(s−1)/s sits on a *fixed complex twistor line* x_ar=−i σ₃/2. With π=(1,w), ω=σ₃π/2 and the usual SU(2,2)-signature twistor pairing H=ω†π+π†ω, the exact equation is H=1−|w|²=(2Re s−1)/|s|². The anti-linear mirror J(ω,π)=(-σ₁overlineω,σ₁overlineπ) fixes the complex line, exchanges positive/negative H, and maps w↦1/overline w. The holomorphic functional shadow w↦1/w fixes u=[(1+w)/(2(1−w))]², a quotient coordinate on which the critical circle becomes u≤0.

The completed arithmetic amplitude f(u)=ξ(½+√u)/ξ(½) is single-valued because ξ(½+z) is even. Its logarithmic derivative m(u)=f′(u)/f(u) is a Stieltjes function and the associated Pick kernel is positive **if and only if RH**. This is a rigorous RH criterion, NOT an independent proof of the necessary positivity. The true prime+gamma+pole formula for m and its Laplace transform from Suzuki's signed arithmetic scalar are derived in the private note.

The script checks projective twistor equations **symbolically** and examines the Pick kernel at three finite upper-half-plane points numerically. As a negative control it demonstrates that the fake Fθ(s)=ξ(s−θ)ξ(s+θ) has a pole in the upper u-plane and violates anti-Herglotz, despite satisfying the same twistor mirror symmetries. Finite numerical eigenvalues are NOT rigorous interval certificates; shifted fake failure has an independent exact pole argument.

**Next RH-strength task:** Derive a zero-independent positive operator/GNS realization of m(u), with the true signed Euler, Archimedean and polar coefficients. Neither twistor geometry, generic causal fermion spectral action nor principal-series terminology can substitute for that noncircular construction.

## October 16: exact positive-sheet higher-order falsifier

Run `python research/codex/twistor_confluent_hankel_exact_falsifier.py`. For the positive two-mode fake `F_5(z)=cosh(2z)+5cosh(z)`, both the first Fisher/Turan sign `h1=13/48>0` and the adjacent 2x2 Hankel minor `1649/19353600>0` pass. But the nonconsecutive derivative-order minor `h1*h5-h3^2=-7159067/214592716800<0` and the 3x3 Hankel determinant are strictly negative, with an exact rational negative vector. Every coefficient is checked with Fraction formal series division and no zero-location input. This identifies the missing OFF-DIAGONAL real positive-sheet Loewner/Pick positivity condition. The actual xi infinite matrix positivity is still unproved, and RH is OPEN. Details: GPP-bridge `work/codex/2026-10-16_twistor_positive_sheet_confluent_hankel_falsifier.md` and GPPVerify PR #377 (draft Lean arithmetic).


### Actual xi finite Hankel coercivity (unconditional, but finite)

The follow-up exact rational scripts `twistor_xi_hankel3_tail_bound.py` and `twistor_xi_hankel5_rational_bound.py` combine *published* Platt--Trudgian RH verification for zeros through height `3e12`, standard certified first-five zero brackets and Rosser's explicit zero counting to prove strict positivity of the actual xi log-derivative Hankel matrices H3, H4 and H5. In particular the final interval algebra gives `H3 > 1e-23 I`, `H4 > 1e-24 I`, `H5 > 4e-32 I`. The second script uses exact Lagrange interpolation bounds for the low-zero Vandermonde inverse and a rigorously controlled **arbitrary high-zero off-axis tail**. No RH assumption is made above the verified height. Only the numerical rational inequalities are checked by these scripts; the published analytic inputs and infinite Hadamard bridge are not formalized in Lean. **No claim of positivity at every matrix size, no RH or GRH proof.** See the corresponding private bridge note for the full derivation.


## October 16 infinite operator and full all-prime heat (Wolfram)

Two new Wolfram Language reproducers were executed in the connected Wolfram kernel with all symbolic checks passing:

- `twistor_infinite_operator_wolfram_20261016.wl`: using only the positive actual xi theta coefficients, proves a zero-free disk `|u|<=4` by a strictly rational bound `2 xi(1/2)-xi(5/2)>17/3200`, then the infinite Hankel operators `H0=(h_{i+j})` and `H1=(h_{i+j+1})` are both trace class on `l2(N0)`, with `||H1||_1 <= (4/9) f'(4)/(2 f(0)-f(4))`. Finite uniform strict gaps CANNOT survive in infinite compact dimension. The two all-infinite localizers `H1>=0`, `(1/4)H0-H1>=0` together are an exact Hausdorff/GNS **RH EQUIVALENCE**, not an independent proof. Positive doubled xi theta convolution has a globally positive Bochner Hilbert kernel yet off-line zeros, so generic theta positivity and shadow symmetry cannot establish RH.

- `twistor_infinite_prime_gamma_heat_wolfram_20261016.wl`: proves exact inverse-Laplace transformations for the full completed arithmetic Weyl function. The infinite heat trace retains pole `exp(t/4)`, all Archimedean gamma modes (`erfc` tower), and all prime powers in a signed Gaussian Mangoldt sum. Wolfram cross-check at heat time `t=.05` agrees with the first eight certified zeros to `1.2e-24` (numerical, non-interval). **RH iff this complete arithmetic heat trace is completely monotone on t>0**, by Bernstein/Stieltjes. No proof of this complete monotonicity has been supplied.

Full details, including actual infinity-level proof obligations, sources, and strict fake filters, are in the private GPP-bridge notes `work/codex/2026-10-16_infinite_twistor_hankel_hausdorff_gns_wolfram.md` and `work/codex/2026-10-16_infinite_signed_prime_gamma_twistor_heat_wolfram.md`. RH and GRH remain OPEN. Both Wolfram files are zero-independent in their arithmetic *definitions*; the zero-value comparisons are separately labelled diagnostics.


## Oct 17 — Quantomorphism / Chern-Simons / twistor holography (infinite)

The Wolfram script `quantomorphism_chern_simons_twistor_20261017.wl` was executed with exact algebra checks PASS. It develops the arithmetic Bohr phase space `K_phase=PontryaginDual(Q_positive)`, the cylinder-current cocycle `omega(f,g)=Haar(f Dg)`, the compatible positive-frequency polarization, and the full prime-power boundary energy `B(s)=sum_p(log p)^2/(p^s-1)`. The exact local doubled-KMS Fubini–Study metric is `(log zeta)''(s)/4` for s>1. Completion to xi cancels the central double pole using the polar factor, and leaves the Archimedean trigamma: `(log xi)''(1)=pi^2/8-1-EulerGamma^2-2 StieltjesGamma[1]=0.04615431729...`. This is a real global arithmetic identity, not proof of RH.

The script also certifies an **INFINITE all-prime** mismatch: the positive trace-class quartic boundary curvature `A_gauge=diag_p((log p)^4/(p-1)^2)` has scale-free second moment ratio `< 1/20` by *rational atanh enclosures for logs of primes <=1000 plus an analytic bound on every prime >1000*. Actual xi's independently Arb-certified ratio is `>0.06`; hence scalar rescaling cannot identify the naive positive quantomorphism determinant with xi. The necessary next step is a genuinely **non-diagonal prime/Archimedean Poisson/BRST intertwiner** that establishes the full xi determinant or positive Weyl resolvent without using zero locations. Generic Chern–Simons boundary phases and positive twistor disk curvature do not exclude interior Blaschke zeros. The algebraic cocycle is not yet a globally integrated infinite-dimensional quantomorphism gauge group or a 3D Chern–Simons bulk.

Full derivation / external references: private `GPP-bridge/work/codex/2026-10-17_quantomorphism_chern_simons_arithmetic_twistor_infinite.md`. **RH/GRH OPEN.**


## Oct 17: Entire infinite spectral Weyl-law anomaly, Lambert-W comparison, and BRST no-go

Run `research/codex/quantomorphism_weyl_anomaly_ghost_wolfram_20261017.wl` in Wolfram Language. All exact symbolic checks passed. These are ALL-INFINITE analytical consequences of the classical prime number theorem (PNT) and Riemann–von Mangoldt, not numerical finite-support RH testing.

The honest product-formula gauge Hilbert `l2(N)` with dilation `D=diag(log n)` has exponential eigenvalue counting, and NO bounded selfadjoint perturbation of D can yield the zeta-zero `T log T` law. The prime-only positive trace-class quartic curvature A_CS has the right spectral order, but after scaling its energies E_p=2π(p−1)/log(p)^2, PNT yields an **unwanted `(T/π)loglog T` Weyl-counting surplus**. Equivalently its spectral zeta has a `−log(epsilon)/(π epsilon)` anomaly absent from the RvM ordinate spectral zeta. A rigorously defined nonlinear, subleading gauge/Arch dressing is necessary, not merely scalar coupling renormalization.

An asymptotically *fitted* dispersion E_p=2π(p−1)/[log p(log p−2loglog p−2)] cancels that surplus through O(T), but this is NOT derived from CS physics. An exact positive trace-class comparison Hamiltonian is H_W|n>=2πn/W(n/e)|n>, with principal Lambert W; its smooth counting function is EXACTLY floor[T/(2π)(log(T/(2π))−1)] above threshold. Thus matching Weyl growth and positive selfadjointness alone is easy and does NOT prove RH: the full arithmetic Fredholm/scattering identity remains required. Finally full prime-local boson/Faddeev–Popov-fermion pairing has global graded index `ζ(s)/ζ(s)=1` for Re(s)>1, so naive fully locally paired BRST cancels all arithmetic. True cohomology must retain nonlocal Poisson-Arch unpaired modes.

Complete proof and scope: private GPP-bridge `work/codex/2026-10-17_quantomorphic_infinite_weyl_anomaly_lambert_brst.md`. **RH/GRH OPEN.**


## Oct 17 — Global rational Hardy Shale obstruction (all infinite; strict Fock implementation)

Run `quantomorphism_global_hardy_shale_20261017.wl` in Wolfram Language (exact rational identities PASS). On the genuine all-rational phase Hardy space `l2(Q_positive)`, with polarization `P_plus e_q = 1_(q>=1)e_q` and unitary prime translation `U_p e_q=e_(pq)`, the commutator `[P_plus,U_p]` is **infinite-rank, noncompact and NOT Hilbert-Schmidt** for every prime p. Explicit infinitely many mutually orthogonal boundary-crossing modes are `q_m=(m+1)/(m+p)` (m>=0). Thus the standard Shale–Stinespring restricted-Fock prime-shift implementers do not exist for the naive global Bohr-phase Hardy polarization. Each local one-prime shift has rank-one crossing, but tensoring it with identities on all other primes produces infinite multiplicity: direct-sum local HS energy does not prove global tensor-Fock implementability. No prime-translation-invariant diagonal frequency weight can fix it (unitarity requires constant weight on all Q_positive).

This sharpens the physical construction target: use the ACTUAL norm-one idele-class quotient `C_Q^1≈hat(Z)^×` (profinite, **not** `prod_p U(1)`), with Dirichlet Peter–Weyl character sectors plus the continuous norm/Mellin direction, and a modular/non-Fock or operator-valued CS framework with smooth twistor dimensions. The infinite positive non-Fock KMS product state already exists in the earlier Oct 11 GPP-bridge note; do not claim novelty for that. No actual idelic Chern–Simons characteristic determinant of xi is yet constructed. Details: private `work/codex/2026-10-17_global_quantomorphism_hardy_shale_idele_obstruction.md`. **RH/GRH OPEN.**


## October 17: Celestial OPEs, W1+infinity quantum central charge, and oriented two-sided anomaly cancellation

Connected Wolfram script `research/codex/winfinity_central_charge_orientation_20261017.wl` verifies the quantum differential-operator/W1+infinity spin-2 algebra: `L_n=-z^n(D+(n+1)/2)`, its Witt bracket, and the Kac–Radul positive-mode cocycle `sum_{j=1}^n[((n+1)/2)-j]^2=n(n^2−1)/12`. Thus the **tree celestial w1+infinity WEDGE (m=-1,0,1) is centerless for ANY quantum central charge C**. Vanishing of the classical wedge central term does not imply C=0. The exact two-orientation glued mode `J_n=L_n^+−L_{−n}^-` has central coefficient `(c_+−c_-)(n^3−n)/12`. Matching nonzero positive c_+=c_- cancels the *oriented anomaly* but does not erase either sector's positive stress tensor norm `||L_-2|0>||²=c/2`. This mathematically implements the user's 'positives pointing the other way' insight alongside the Haar-FS anti-symplectic geometry.

**Critical audit:** the user's earlier `qg_definitive.tex` claims five independent proofs c=0. One explicit step constructs even positive `|C_(1+iλ)|²|C_(1+iλ')|²` before then asserting the odd gamma-function PHASE cancels it: the phases are already gone, so this does NOT calculate the TT central OPE. The manuscript also contains an erroneous `c/2*6=c/2` bracket simplification, and equates unrelated twistor H¹ with the Lie algebra H² cocycle. Thus individual celestial c=0 remains NOT established. A physically plausible anomaly-free candidate is c_+=c_- (difference zero) without requiring chiral c=0; true quantum OPE loop/contact-term calculation still needed. Neither charge cancellation nor geometric mirror proves RH or Weil positivity.

Full private research/audit note: `GPP-bridge/work/codex/2026-10-17_winfinity_ope_central_charge_orientation_anomaly_audit.md`. Draft algebra-only Lean theorems: GPPVerify PR #385 `CelestialHolography/WInfinityCentralSewing.lean`; CI required before verified claim. **RH/GRH OPEN.**


## October 17 — COMPLETE celestial cut, quantum TT OPE, and missing rational 1-loop all-plus anomaly

New connected-Wolfram 13/13-check script `research/codex/celestial_cut_walgebra_one_loop_central_audit_20261017.wl`. It reads the user's superseding *Loops from Cuts in Celestial Mellin Space v19*, not the superseded failed z-sewing attempt. On the shadow principal series, the exact entire scalar two-particle cut is the **positive** weight `w(lambda)=lambda/[8*sinh(pi*lambda)]` and its full Fourier kernel is `K(t)=sech(t/2)^2/16`. **Exact all-spectrum OS obstruction:** at strictly positive times log2 and log3, the reflected Hankel matrix is `[[1/25,3/98],[3/98,9/400]]` with strict NEGATIVE determinant `-891/24010000`. Ordinary positive-definite Haar/FS cut does NOT automatically yield OS positivity. This entire-spectral obstruction is independent of primes or RH. Draft Lean PR #385 adds `CelestialHolography/ShadowCutOSObstruction.lean` with exact rational proof; Fourier transform analytic bridge not Lean checked.

**Gamma c=0 manuscript correction:** `qg_definitive.tex`'s displayed factor `|Gamma(1+i lambda)^3/Gamma(2+3i lambda)|^2` has exact positive closed form `pi^2 lambda^2(4+3*csch(pi*lambda)^2)/[3*(1+9 lambda^2)]`, tends to `4*pi^2/27` at infinity, and its DOUBLE Gaussian-regulated integral diverges as `16*pi^5/(729*epsilon)` rather than vanishing by odd phases. That radial expression is NOT the chiral TT OPE, so actual c remains undetermined. A controlled current/Wick model on the SAME infinite cut Hilbert measure gives stress-tensor OPE c=N for ANY N positive integer; mirrored sectors cancel oriented central difference if equal N, but individual c and their Weyl sum stay positive.

**Mandatory gravity one-loop ingredient missing from v19 scalar box:** all-plus graviton one-loop amplitudes are NONZERO rational while all usual FOUR-dimensional unitarity cuts vanish (Bern–Dixon–Perelstein–Rozowsky 1998, hep-th/9809160). D-dimensional dimension shifting including `mu^8` is required to recover them. Bittleston JHEP01(2023)018 shows a separate one-loop chiral OPE associativity defect from a twistor gravitational anomaly, canceled by a fourth-order axion/Green–Schwarz mechanism or certain matter choices. This failure is **not identical** to a nonzero Virasoro central charge. A faithful quantum celestial stress calculation must determine BOTH the physical chiral TT Schwinger contact `-(pi*c/12)*partial_z^3 delta^2` and the one-loop associator from actual graviton rational/soft flux amplitudes, with mirror and UV/IR prescription. The source scalar-cut weight and central cancellation ALONE cannot do it; claiming c=0 or RH would be incorrect.

Private full source/audit and proof note: `GPP-bridge/work/codex/2026-10-17_full_celestial_cut_quantum_TT_central_OS_and_allplus_anomaly.md`. All 13 Wolfram checks PASS; Lean PR #385 CI pending. **Physical quantum c+/c-, RH and GRH OPEN.**


## October 17: full all-spin quantum celestial twistor / arithmetic Ward package

Executed in connected Wolfram kernel, exact PASS:
- research/codex/winfinity_fullspin_halfdensity_haar_loop_20261017.wl: Kac–Radul full differential-operator cocycle, quantum free-fermion Dirac sea Schwinger trace and half-density mirror n→−n, D→−D−1; anti-invariance for EVERY spin (8 checks).
- research/codex/celestial_twistor_moyal_full_quantum_ope_20261017.wl: Moyal quantization of the ACTUAL published celestial twistor Poisson w-infinity OPE, all polynomial orders. Example [x³,y³]_star/h=9x²y²+3h²/2, with exact anti-symplectic quantum mirror sign (5 checks). Moyal deformation is distinct from Kac–Radul loop central cocycle.
- research/codex/winfinity_fulltower_prime_gamma_ward_20261017.wl: ALL m≥2 completed xi thermal-cumulant identity, Euler all-primes plus gamma all-modes minus polar, tests m=2..7 PASS. These are potential arithmetic Ward data, NOT physical celestial OPE charges yet.

GPPVerify draft PR #385 includes WInfinityFullSpinMirror.lean as a root-imported arbitrary symbol/all-n Lean theorem, along with Fubini–Study orientation and Virasoro central sewing; CI pending. The true norm-one idèle-class Haar coefficient algebra admits an exact all-spin 2-cocycle, but standard quantum Fock implementability and actual gravity-loop central charges are not established. Earlier qg_definitive.tex claimed global holomorphic CS Ω on compact CP3, which has canonical O(-4) and NO global holomorphic volume; open/meromorphic or Calabi–Yau supertwistor geometry needed. Private proofs/audit: GPP-bridge work/codex/2026-10-17_full_winfinity_halfdensity_haar_one_loop_arithmetic_ward.md and work/codex/2026-10-17_celestial_twistor_moyal_quantum_ope_beyond.md. **RH/GRH OPEN** until physical arithmetic Ward module yields faithful positive completed xi determinant or all-signed Weil cut norm.


## October 20: Astra/Turbo Cesàro meets xi multiplicity-sensitive Bohr trace

Wolfram companion: research/codex/cesaro_xi_multiplicity_bohr_parseval_20261020.wl (executed; exact symbolic multiplicity inequalities PASS). Let prime-defined J(t)=int_1^(exp t)(psi(x)-x)x^-3/2 dx; Astra's kappa and explicit L² trivial-zero transient R(t), and B=J-kappa-R. **IF RH** (simplicity NOT assumed), integrated explicit formula plus Bohr Parseval give lim_(T->infty) T^-1 int_0^T|B(t)|²dt = 2 sum_(gamma>0) m_gamma²/[gamma²(gamma²+1/4)]. The actual xi Hadamard log-derivative difference is C_xi=8[xi''(1/2)/(2xi(1/2))-xi'(1)/xi(1)] = 2 sum m_gamma/[gamma²(gamma²+1/4)]. Thus mean−C_xi = 2 sum m_gamma(m_gamma−1)/[...] >=0, with equality iff all zeros simple, under RH. C_xi≈0.0000742731943834958 (Wolfram, not interval). A PRIME-SIDE limsup mean<=C_xi implies RH plus simplicity via Astra's Laplace growth criterion, and conversely RH+simplicity give equality; **this is an equivalence, NOT a proof of the missing signed-discrepancy upper bound**. Critical: Bohr norm uses multiplicity SQUARED; the xi determinant trace uses multiplicity LINEARLY. Do not silently assume simplicity or continue ONON's positive Abel mean past its convergence strip. Full private proof: GPP-bridge work/codex/2026-10-20_cesaro_bohr_xi_multiplicity_trace_threshold.md; posted to PR11 for Claude/Astra/Turbo independent audit, Grok unavailable. RH/GRH and simplicity OPEN.
