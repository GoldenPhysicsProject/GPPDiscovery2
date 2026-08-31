# Arithmetic wave-particle / orientation synthesis — 2026-08-29

This note records a research synthesis after comparing current Verify2 mathematics, the
August Discovery2 fronts, and time-layered GPP Drive material. It is a map of exact facts,
corrections, and testable conjectural bridges — not a new proof claim.

## 1. Orientation cluster: what survives the chronology

The older googly lineage suggested identifying several reversals too quickly. Later work
sharpens the picture.

### Exact structures already established

1. On the Gr(2,4) big cell, the orientation/chart map satisfies

   \[
   \tau^2=-\mathrm{id},\qquad \tau^4=\mathrm{id}
   \]

   on the nonzero-determinant domain. The determinant controls the scale in the chart/Jacobian
   formulas. This is the clean Z/4 or quarter-turn structure behind the project's
   zitterbewegung/orientation language.

2. Rest-frame massive Dirac evolution has Compton phase rate

   \[
   \omega_C=mc^2/\hbar
   \]

   and chirality-population / zitterbewegung rate

   \[
   \omega_Z=2\omega_C=2mc^2/\hbar.
   \]

   The factor two comes from the Clifford algebra and gives the familiar sign/restoration
   pattern under the corresponding spinorial cycle.

3. Celestial shadow acts on labels as

   \[
   (\Delta,J)\mapsto(2-\Delta,-J).
   \]

   On the principal series, the dimension reflection is complex conjugation of the spectral
   coordinate. The later mass-orientation manuscript explicitly corrects the stronger old idea
   that this should be a literal internal-charge flip: internal charge labels are left untouched.

4. A current googly construction gives an antiunitary orientation exchange on bivectors and an
   explicit antiunitary twistor-level phase lift. Its equality with the geometric Gr(2,4)
   orthogonal-complement shadow map is not yet proved.

### Working synthesis

The common candidate is therefore not `shadow = time reversal = charge conjugation` as a literal
identity. A more defensible organizing object is an orientation/complex-structure exchange whose
representation can appear as:

- SD/ASD exchange or helicity reversal;
- complex conjugation / antiunitarity on spectral coordinates;
- chirality/energy-sign mixing in a massive spinor;
- a Z/4 lift with square `-1` even when the projected operation is a Z/2 involution.

This gives a precise place to test a boson/fermion distinction: compare representations in which
the relevant lifted reversal squares to `+1` with spinorial/quaternionic representations in which
it squares to `-1`. This is only a research target until the representation categories and maps are
specified and proved.

Do not use `SU(1)` loosely. The mathematical group SU(1) is trivial. If older notes use an
`SU(1)->SU(2)->SU(3)` ladder, determine whether the first object was really U(1), a one-state
phase sector, a rank-one stage, or something else before formalizing it.

## 2. Scale versus scale invariance

The later mass-orientation manuscript makes the clean distinction:

- a massless/free conformal sector is scale-free;
- a mass term introduces a proper-time/Compton scale;
- a uniform rescaling of all dimensional masses is not itself an observable when only
  dimensionless ratios are retained.

Current Verify2 scalar-box regulator algebra independently exhibits exact dimensionless scale
invariance of the kinematic variables `R^2` and `kappa^2` under common scaling, while the rational
`1/(SU)` prefactor carries degree `-2`. This suggests treating `scaled` versus `scale-invariant`
as a grading by homogeneity/representation weight, not as two unrelated physical sectors.

A useful formal target is therefore a small homogeneity API: functions or kernels with an exact
scaling degree, together with the dimensionless invariants obtained by quotienting the common
scale. This can connect the scalar-box regulator, massive Compton scale, Mellin principal-series
weights, and projective Grassmannian data without asserting they are the same dynamics.

## 3. Arithmetic wave-particle duality: exact mathematical core

This phrase can be made precise enough to be useful.

### Discrete/arithmetic side ('particle' coordinates)

The canonical atoms are prime powers `p^m`, with von Mangoldt weight

\[
\Lambda(p^m)=\log p.
\]

They are discrete local Euler-factor events/energies at logarithmic positions `m log p`.

### Oscillatory/continuous side ('wave' coordinates)

For `a>1`, Verify2 proves termwise

\[
\Lambda(p^{k+1})p^{-a(k+1)}
 \cos((k+1)t\log p)
=
(\log p)\,r^{k+1}\cos((k+1)\theta),
\]

with `r=p^{-a}` and `theta=t log p`, and resums the full tower into the radial Poisson response

\[
2\sum_{k\ge0}\text{primePowerMode}_{p,k}(a,t)=W_{p,a}(t).
\]

Absolute convergence then gives the exact global identity

\[
2\,\Re\!\left[-\frac{\zeta'}{\zeta}(a+it)\right]
=\sum_p W_{p,a}(t),\qquad a>1.
\]

So a discrete prime-power tower and a smooth local Poisson/Fourier response are already two exact
representations of the same arithmetic data on the honest convergence half-plane.

### Heat/spectral side

The August arithmetic-principal-series program defines the completed prime-Archimedean boundary
distribution `W = nu_infty - nu_p` and its Gaussian heat transform `K(t)`. The intended second
dual description is a positive spectral heat expansion

\[
K(t)=\sum_{\gamma>0}m_\gamma e^{-\gamma^2t}.
\]

That expansion is positive exactly at the RH frontier; it must not be inserted as an unconditional
identity with positive critical-line ordinates.

Hence the research program can be stated as an **arithmetic wave-particle transform problem**:
construct and prove the exact commuting transform diagram

\[
\{p^m,\Lambda(p^m)\}
\longleftrightarrow
\text{Poisson/Fourier modes}
\longrightarrow
\text{completed Gaussian heat kernel}
\longleftrightarrow
\text{positive spectral measure},
\]

with the Archimedean factor and subtraction carried explicitly. The first arrow is substantially
formalized. The last positive-spectral arrow is the hard RH-equivalent boundary, not an established
fact.

## 4. Connection to the orientation program

There is a structural analogy worth testing, but not yet identifying:

- orientation side: an involution/antiunitary map plus a lifted Z/4 structure and a fixed/unitary
  locus;
- arithmetic side: reflection `s -> 1-s`, antiunitary conjugation, the principal-series unitary axis,
  and positive-type/OS/heat kernels.

The testable question is whether both arise from a common representation-theoretic construction
of a positive half-density space with an orientation-reversing antiunitary symmetry. A successful
construction must reproduce the *actual* completed Weil/prime-Archimedean form, not merely local
positive Poisson kernels.

## 5. Immediate formal targets

1. Finish the Gr(2,4) big-cell Z/4 packaging and retire the historical `tau^4 : True` stub.
2. Package scaling degree/homogeneity so scale-invariant and scale-carrying quantities can be
   compared exactly.
3. Build a named arithmetic transform diagram around the already-proved prime-power -> Poisson
   tower and finite/global convergence-half-plane identities.
4. Add the Archimedean component as an explicit signed/completed transform and identify exactly
   where positivity is lost or recovered.
5. Mine older googly, mass-orientation, principal-series, and holographic-chain versions for the
   intended U(1)/SU(2)/SU(3) meaning before using the old `SU(1)` language.
6. Keep charge conjugation separate from celestial helicity shadow unless a new theorem supplies
   the missing internal representation action.

## 6. Drive chronology audit added 2026-08-29

### June googly manuscript -> July mass-orientation correction

The June googly submission asserted the strong identity `celestial shadow = physical time reversal`
and then used it to identify the missing helicity sector with a T-conjugate spacetime. The July
`mass_orientation_coupling_v3` manuscript is more careful and should supersede that identification
for present work. Its exact celestial statement is only

\[
(h,\bar h)\mapsto(1-h,1-\bar h),\qquad
\Delta\mapsto2-\Delta,\qquad J\mapsto-J,
\]

with internal charge labels untouched. Therefore the following distinctions are mandatory:

- shadow/helicity reversal: presently defensible;
- antiunitary or complex-conjugation realization: representation-dependent and to be proved;
- physical time reversal T: not to be identified with shadow without an additional theorem;
- charge conjugation C: separate internal operation, not supplied by the celestial shadow map.

This correction removes a conceptual overreach without damaging the exact Gr(2,4) Z/4 or Dirac
clock-locking mathematics.

### July mass-orientation: exact scale statement

The same manuscript gives a useful scale ledger. The free massless Dirac theory is dilatation
invariant; a nonzero mass term introduces the Compton/proper-time scale. Uniform common rescaling
of all dimensional masses while holding dimensionless couplings fixed cannot by itself define an
observable. This supports treating `scale-carrying` versus `scale-invariant` as homogeneity data.

### August scalar-box v19: shadow locus corrected

The v19 loop-from-cuts derivation explicitly supersedes v14-v18. It proves that the two-particle
cut Mellin factor has the form

\[
\Phi(\Delta_5,\Delta_6;M)
=\frac1{8\pi}\left(\frac M2\right)^{\Delta_5+\Delta_6-2}
\frac{\Gamma(\Delta_5)\Gamma(\Delta_6)}{\Gamma(\Delta_5+\Delta_6)}.
\]

Thus `Delta_5 + Delta_6 = 2` is exactly the scale-invariant locus of the cut. It is **not** a
residue-producing shadow pole. On the principal series,

\[
\Gamma(1+i\lambda)\Gamma(1-i\lambda)
=\frac{\pi\lambda}{\sinh(\pi\lambda)},
\]

so the older spectral weight survives as a derived phase-space factor, not as a replacement for
the Feynman loop measure. This is the cleanest current bridge among celestial cuts, Mellin
reflection, principal-series weight and scale invariance.

### August arithmetic-principal-series v34: several RH routes explicitly killed

The latest mined arithmetic manuscript contains important negative results that should constrain
all active formal fronts:

1. The earlier Gamma-polarized one-prime vanishing problem is false as stated.
2. Adding finitely many prime dilations does not repair it: irrational-rotation small divisors give
   dense nonclosed Koszul range, so there is no bounded Green operator / finite-prime contracting
   homotopy.
3. Bilateral Gaussian heat cannot preserve the causal Tate Hardy domain at positive time except
   on the zero vector; therefore no graph norm can turn that bilateral heat flow into the desired
   global Tate homotopy.
4. The causal replacement, the Dirichlet heat semigroup on `L^2(R_+)`, has an exact boundary
   commutator anomaly. For a unilateral translation by `a`,

   \[
   \operatorname{Tr}(E_tV_a-V_aE_t)
   =\frac{a}{\sqrt{4\pi t}}e^{-a^2/(4t)}.
   \]

   Summing the logarithmic prime resolvents recovers exactly the prime-power portion of the
   completed arithmetic heat kernel,

   \[
   \sum_p\operatorname{Tr}[E_t,R_p]
   =\frac1{\sqrt{4\pi t}}
     \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
     e^{-(\log n)^2/(4t)}.
   \]

This last formula is a materially stronger candidate for the `arithmetic wave-particle` bridge than
mere analogy: discrete prime-power atoms become a continuous causal heat-boundary anomaly with the
correct von Mangoldt weight. The unresolved issue is the genuinely global relative
prime-Archimedean trace cancellation and positivity; the individual prime commutators are not
absolutely summable in trace norm.

### Old E8/GPM gauge reconstruction: do not promote

The 2025 E8/GPM files contain the useful empirical vocabulary `SU(3) x SU(2) x U(1)` and shell
counts, but their purported derivation should not be imported into Verify2. Independently checking
the displayed coherence functional

\[
S(G)=\frac{\det G}{(\operatorname{tr}G)^3}
\]

shows by AM-GM that `S <= 1/27`, with equality for **every** positive matrix whose three
eigenvalues are equal. Scale invariance also makes the unrestricted frame space noncompact. Hence
that functional alone cannot imply a unique golden frame up to the E8 Weyl group. The old argument
from a unique maximizing eigenvalue spectrum to a unique frame is invalid. Treat all downstream
shell-to-gauge and cofactor-coupling claims as historical/conjectural unless separately reconstructed.

The safe group-theoretic point remains: `SU(1)` is trivial. The physically meaningful abelian
factor is `U(1)`, and any remembered `SU(1), SU(2), SU(3)` ladder must be translated into an exact
rank/stabilizer statement before use.

## 7. Formalization consequences from this mining pass

- Preserve the exact Z/4 Grassmannian orientation theorem and Dirac factor-two clock relation.
- Strengthen scale formalization using homogeneity, with the scalar-box shadow locus as a concrete
  theorem-level test case.
- Keep celestial shadow, physical T and charge conjugation as separate maps until a commuting
  representation diagram is proved.
- Add the causal Dirichlet-heat prime anomaly to the RH formalization roadmap. It is a high-value
  theorem target because it reproduces the exact prime-power heat contribution without zero data.
- Mark one-prime/finitely-many-prime Koszul contraction and bilateral Gaussian Tate-homotopy routes
  as closed negative fronts; do not spend new proof effort on them unless assumptions change.
- Do not use the old E8 stationary-coherence uniqueness proof to retire Standard Model stubs.
- Current Verify2 `main` has a successful full `lake build` CI at commit
  `4025286936321e43d11f8fa7f9454b69cbe38f68`; its separate Blueprint workflow failure is not a
  Lean compilation failure. Continue to quote sorry/axiom/stub counts separately.

## 8. Drive chronology audit added 2026-08-31

### July orientation–representation quotient sharpens the mass–time–charge bookkeeping

The July 24 `orientation_representation_quotient_v1` manuscript gives the cleanest surviving
mathematical core of the charge/time-orientation idea. For a closed oriented gauge line,

\[
W_{R^*}(\gamma)=W_R(\bar\gamma),
\]

because dual transport is inverse-transpose transport and path reversal is inverse transport. In
the Abelian reduction, if `c=±1` labels a conjugate charge pair and `t=±1` the orientation of the
worldline relative to a chosen arrow, then

\[
W_{c,t}=\exp\!\left(i\,ct\,q_0\int_{\gamma_+}A\right).
\]

The diagonal involution `(c,t) -> (-c,-t)` therefore has the unique nontrivial quotient character

\[
m=ct.
\]

This is a theorem about oriented gauge data. It does **not** identify celestial shadow with Wigner
`T`, and it does **not** turn every self-dual representation into a matter/antimatter binary. It
supplies the precise mathematical content behind the old four-sign bookkeeping while preserving
the later distinction between internal dualization and spacetime/orientation operations.

### Arithmetic v28 -> v34: the Suzuki/semilocal Weil bridge is a later addition

Comparing the August 13 v28 and v34 arithmetic manuscripts shows that the core heat-trace,
reflection-positivity, Hausdorff-moment, principal-series smoothing, Hardy-defect, and causal
Dirichlet-heat anomaly results are already present in v28. The later v34 layer adds a distinct sharp
support-normalization bridge:

\[
\widetilde q_L(k)=q_L(k)-r_L k,
\qquad
r_L=\int_L^\infty w_\infty(a)e^{-a}\,da.
\]

Under RH, the derivative of the normalized phase is a Dirichlet-kernel sum over critical
ordinates, and its Fejer mean is the diagonal of the semilocal Weil matrix. The associated box
diagonal `Psi(L)` is identified with Suzuki's screw function. The manuscript records the known
criterion

\[
\Psi(L)\ge 0\quad\text{for every }L
\]

as RH-equivalent. This does not prove positivity, but it materially links three active fronts that
had been tracked separately: support-normalized prime/Archimedean phase, finite/semilocal Weil
positivity, and the spectral/heat formulation.

This is a better formalization target than inventing another positivity proxy: formalize the exact
normalization term and the identity from the Fejer-averaged phase to the semilocal Weil diagonal,
then connect that diagonal to the existing `SpectralWeil` infrastructure. The current Verify2 code
search contains no Suzuki/screw/Fejer implementation, so this bridge is presently absent from the
formal tree.

### Stub reduction by supersession, not by fake proof

The chronology audit exposed one placeholder that should not remain a proof target at all.
`GppVerify/CelestialHolography/TwistorGoogly.lean` still contained
`googly_resolution_T_image : True := trivial`, representing the superseded strong identification
of the googly/shadow map with physical time reversal. Because later manuscripts explicitly separate
shadow, Wigner `T`, and charge conjugation, the correct reduction is deletion rather than a proof of
the old claim. That placeholder has now been removed from Verify2 `main`, while the exact proved
shadow/helicity theorems remain unchanged.

This is the model for axiom/stub reduction throughout the archive: a historical placeholder may be
retired either by replacing it with a theorem, or by proving that its intended statement was
superseded and deleting it. Stub count is not itself a reason to preserve an invalid target.

### Current synthesis after this pass

The strongest common picture is now a hierarchy, not an identity:

1. **Gauge orientation quotient:** `(R,\gamma) ~ (R^*,\bar\gamma)`, with Abelian invariant `ct`.
2. **Celestial shadow:** `(\Delta,J) -> (2-\Delta,-J)`, with principal-series conjugation on the
   spectral coordinate.
3. **Spinorial lift:** the Gr(2,4) orientation map has a genuine Z/4 lift and massive Dirac dynamics
   supplies the factor-two zitterbewegung/Compton clock relation.
4. **Scale grading:** `Delta_5+Delta_6=2` is a zero-homogeneity cut locus; mass introduces a proper
   scale while projective/principal-series data organize scale-free sectors.
5. **Arithmetic discrete/continuous transform:** prime-power atoms map exactly to Poisson/Fourier
   modes and, through the causal Dirichlet heat anomaly, to a continuous heat-boundary response.
6. **Global RH frontier:** the missing theorem is the completed prime–Archimedean positive relative
   trace / Weil Gram factorization. The later Suzuki bridge gives a concrete semilocal diagonal
   target inside that frontier.

No step in this hierarchy justifies collapsing charge conjugation, shadow, time reversal, or
zitterbewegung into a single operation. What survives is the repeated appearance of dualization,
orientation reversal, reflection, half-density normalization, and positive/unitary fixed loci in
mathematically different representations.
