# Integrated active-front research map — 2026-08-28

This file records the Codex/GPT work program that must be carried forward together rather than as isolated threads.

## 1. Grassmannian / googly / orientation / mass / zitterbewegung

Focused inputs now explicitly in scope:

- `twistor_googly_dtoupin_v5-2.tex`
- `mass_orientation_coupling_v3*.tex`
- `half_flip_proposition_v1*.tex` and `HalfFlip.lean`
- `grassmannian_mass_theorem.py`
- existing Verify2 files `GrassmannianGr24.lean`, `HolographicChain.lean`, `GooglyAntiunitaryExchange.lean`, `GooglyTwistorLift.lean`, `CelestialShadowHelicity.lean`

Established/project structure to preserve:

- Gr(2,4) is represented as actual complex 2-planes in C^4; orthogonal complement gives a self-map because 2=4-2.
- Plucker coordinates of a big-cell frame `[I|A]`, with `A=[[a,b],[c,d]]`, include `p23=det A=ad-bc`.
- The explicit twistor antiunitary involution
  `Theta(Z0,Z1,Z2,Z3)=(i conj Z0,-i conj Z1,-i conj Z2,-i conj Z3)`
  induces on Lambda^2 C^4 the already formalized googly exchange: conjugation on the first three Plucker coordinates and minus conjugation on the last three.
- The celestial shadow map acts `(Delta,J) -> (2-Delta,-J)` in the project formalization. Ordinary bulk time reversal preserves helicity; parity reverses it, so bare T must not be conflated with helicity flip.
- Mass/proper-time phase is already exact standard mechanics:
  `S=-mc^2 int d tau`, `phase=-mc^2 tau/hbar`, hence `d phase/d tau=-mc^2/hbar`.
- Dirac zitterbewegung scale is `omega_Z=2mc^2/hbar`.
- The Grassmannian mass Python experiment uses the chart transition
  `(a,b,c,d) -> (-b/detA,a/detA,-d/detA,c/detA)`
  and claims the mean Jacobian eigenvalue magnitude is `1/|det A|` on the big cell, with `det A` interpreted as a spinor/Plucker mass parameter.

Immediate work:

1. Analytically derive the full Jacobian spectrum of the Gr(2,4) chart transition, not merely numerical mean magnitude, and determine the exact invariant statement.
2. Resolve the normalization inconsistency in the Python header (`massless m=0` versus `|det|=1`) before using the physical dictionary.
3. Descend the explicit anti-linear twistor involution to an honest semilinear self-map on the Gr24 subtype.
4. Compare that induced plane map with Hermitian orthogonal complement/shadow; equality is not assumed.
5. Relate the null screen quotient `k^perp/<k>`, spinor factorization, CP1 twistor incidence line, and Gr(2,4) plane structure by explicit maps. Do not identify them by analogy alone.
6. Seek a derivation of the massive proper-time phase from orientation/chirality coupling rather than re-stating `phase=-m tau`.
7. Determine whether the zitter factor of two arises geometrically from alternating orientation sectors / positive-negative energy interference in the Grassmannian chart dynamics.
8. Integrate the Half-Flip CP/CPTP obstruction as the operational boundary on antiunitary enactment.

## 2. Causal diamond / fixed-volume / Fisher geometry

Focused inputs now explicitly in scope:

- `volume_constraint_entanglement_equilibrium-3(2).tex`
- `verify_volume_constraint-1.py`
- `fisher_form_causal_diamond-2.tex`
- related Fisher/Weil numerical scripts (`bc_weil_experiment.py`, Petz tests where relevant)

Key structure:

- Jacobson-style entanglement equilibrium has a null identity/cosmological direction; the proposed resolution is quotienting that degeneracy by fixing proper volume.
- The diamond conformal factor is claimed/checked to be concircular in Einstein backgrounds, with pure-trace Hessian and eigenvalue equal to minus sectional curvature.
- The boost radial operator is Kontorovich-Lebedev with spectral density
  `rho_KL(lambda)=(2/pi^2) lambda sinh(pi lambda)`.
- At lambda=0 the KL density has an exact double zero:
  `rho_KL=(2/pi) lambda^2+O(lambda^4)`.
- With the extra boost charge, the first-law integrand vanishes cubically at the trivial representation.
- The Fisher/Kubo-Mori kernel is
  `kappa_beta(omega)=(beta omega/2)/sinh(beta omega/2)`.
- At Bisognano-Wichmann beta=2pi the thermal factors cancel, leaving the exact quadratic weight `(2/pi) lambda^2` in the stated normalization.

Immediate work:

1. Separate theorem-grade identities from interpretive claims in both papers and formalize the exact scalar identities first.
2. Prove the KL double-zero and BW cancellation algebraically in Lean before attempting spectral-analysis infrastructure.
3. Build the clean dictionary between diamond Fisher positivity and the Weil positivity architecture without claiming equivalence beyond proved hypotheses.
4. Investigate whether the same fixed-point / trivial-representation exclusion mechanism appears in the Gr(2,4) orientation fixed locus.

## 3. RH / principal series / explicit formula / Weil positivity

Established:

- principal-series half-density normalization and `Delta=2s` put the critical line at `Re Delta=1` / `Re s=1/2`;
- completed-zeta response has functional-equation and conjugation symmetries;
- finite Weil pair-support interpolation has been reduced to polynomial interpolation, with a multiplier version when a seed is nonzero on the pair-support;
- finite interpolation + admissible positivity would imply the full finite Weil paired positivity criterion already formalized.

Missing global bridge:

1. Produce admissible Mellin/Paley-Wiener test functions realizing the required finite interpolation while remaining inside the explicit-formula class.
2. Establish a nonvanishing admissible seed on arbitrary finite zero pair-support.
3. Transport actual positivity through the completed explicit formula.
4. Relate the causal-diamond Fisher positive form to the arithmetic form only by an explicit operator/limit theorem, not architecture alone.
5. The uniform critical limit (`beta -> 1+` / regulator removal / complementary-series exclusion) remains a central target.

No RH claim until the positivity bridge closes globally.

## 4. Prime-gas thermodynamics

Established differential hierarchy for beta>1 includes

- `kappa_2'=-kappa_3`,
- `kappa_3'=-kappa_4`,
- `kappa_4>0`,
- hence `kappa_2''=kappa_4>0`,
- entropy slope `S'=-beta kappa_2=-C/beta`.

Do not assert global signs for heat-capacity derivative, entropy curvature, or higher cumulants without proof.

Immediate work: connect this Gibbs/Fisher geometry to the causal-diamond Kubo-Mori form and the adelic/explicit-formula limit, looking for an exact monotone/convex quantity that survives beta -> 1+.

## 5. Spectral Gamma / Mehler-Fock / Wiener-Hopf

Established algebraic structure:

- even positive Gamma spectral weight;
- Gamma-pair recurrence
  `Gamma(a+1+ix)Gamma(a+1-ix)=(a^2+x^2)Gamma(a+ix)Gamma(a-ix)`;
- chamber recurrence factor `R_k(x)` and exact threshold `2x^2` versus `k+1`;
- base Wiener-Hopf/Gamma normalization and product lift across chambers.

Current immediate issue: the dedicated sech CI gate exposed a Lean proof-normalization failure in `SpectralGammaPairRecurrence.lean`. A second repair was committed on Verify2 as `d1f04f90be9407ef5aef0e003528a8753981d900`; certification awaits CI.

Next mathematical work after CI: distinguish algebraic Gamma recurrence from a physical iterated-convolution construction and prove the latter only if an actual convolution operator identity is available.

## 6. Celestial cuts / scalar box / YM / gravity

Established:

- exact celestial two-particle cut geometry and Mellin factors in the focused cuts paper;
- raised-box Gamma residue input;
- pointwise `Q^{-epsilon}->1` in the Euclidean Symanzik region;
- majorant `Q^{-epsilon} <= 1+(A x1 x3)^{-delta}`;
- exact target simplex integral
  `int_Delta3 x1^{-delta} x3^{-delta} = Gamma(1-delta)^2/Gamma(4-2delta)`;
- two-Beta reduction in Discovery2;
- all-plus four-point gravity obstruction previously retracted: it reduces to the known mu^8 scalar-box structure;
- fixed-loop-momentum Ds reconstruction has been formalized.

Immediate work:

1. Formalize the affine 3-simplex as nested interval integrals.
2. Apply two scaled Beta integrals and collapse to the Gamma quotient.
3. Use dominated convergence to obtain the simplex volume `1/6` and close the regulator limit.
4. For generic YM/gravity, derive an honest `Ds=4, mu != 0` gluon sewing numerator/state sum; do not fabricate a numerator from scalar reconstruction.
5. Then advance to generalized/higher-loop cuts.

## 7. Cross-front synthesis targets

The high-value synthesis questions are now explicit:

- Does the Gr(2,4) chart transition encode an intrinsic inverse mass/Compton scale whose unitary/fixed-locus limit matches the orientation complex structure?
- Can the mass-proper-time phase and zitter frequency be derived from the same antiunitary/orientation exchange that induces the googly map on Plucker coordinates?
- Is the causal-diamond trivial-representation double zero the local gravitational prototype of the arithmetic fixed-line/tempered-support mechanism, and can this be promoted from analogy to an intertwining theorem?
- Can prime-gas Gibbs/Fisher geometry provide the missing uniformity estimate at beta -> 1+?
- Can the null screen / spinor / twistor / Grassmannian chain be formalized cleanly enough that helicity, shadow, and orientation are all represented by explicit maps rather than prose identifications?

Every future continuation should update this map when a blocker is removed, a claim is retracted, or a new theorem is certified.
