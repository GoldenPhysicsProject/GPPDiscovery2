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
