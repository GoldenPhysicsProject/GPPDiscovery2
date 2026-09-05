# Codex/GPT rotation — Massieu metric and generic triple-cut boundary

## Prime-gas thermodynamic geometry

Verify2 commit `13e66832df3c7e33ee610a14c002212aa83fdcad` is now fully certified: full Build #2042 and cold changed-Lean #896 both passed.  Hence, for every real beta and every eta>0, the exact countable quadratic number-Gibbs Massieu/Fisher covariance entries satisfy

- `fisherBB beta eta > 0`,
- `massieuFisherDet beta eta > 0`,
- `fisherEE beta eta > 0`.

This completes the strict Sylvester-minor layer.

The next exact theorem was pushed to Verify2 as commit `ca10250a944fbccfce05d9ac9e662fad18b80bab`, file `GppVerify/RiemannHypothesis/NumberGibbsQuadraticMassieuMetric.lean`.  It targets strict positivity of the full quadratic form

    fisherBB a^2 + 2 fisherBE a b + fisherEE b^2 > 0

for every nonzero tangent pair `(a,b)`.  The proof uses

    A (A a^2 + 2 B a b + C b^2)
      = (A a + B b)^2 + (A C - B^2) b^2,

with `A=fisherBB`, `B=fisherBE`, `C=fisherEE`, together with `A>0` and `AC-B^2>0`.  Cold changed-Lean #897 is running on this exact commit; do not call the new quadratic-form theorem certified until that gate terminates green.

## Generic nonzero-mu Yang-Mills topology projection

The current exact generic Ds=4 sewing is still a two-particle-cut Laurent object.  Its unique angle-dependent adjacent tree propagator coordinate is

    x = 1 - beta cos(theta),
    p12^2 = -2 E^2 x,
    p23^2 = 4 E^2.

Thus x^-2, x^-1 and polynomial sectors rigorously encode double/single/zero ancestry of that particular p12 propagator across the two sewn trees.  However, this ancestry is not a master-integral projector.

The existing Badger subtraction implementation is structurally different: it exposes an additional uncut propagator D_R, imposes the triple-cut residue condition D_R=0, sums the two roots branch-free, and then applies the T1,T2,T3 moment map.  For one scalar-flow orientation it gives exactly

    C_tri,one-flow^[2]
      = -i (5 u^2 + 3) / (3(1+u^2)),

with the published full coefficient twice this value; the code deliberately leaves the scalar-flow multiplicity explicit.

Therefore the next honest executable amplitude step is now sharper than 'match conventions': construct a triple-cut lift of the genuine generic nonzero-mu vector-minus-scalar sewing, keeping the additional uncut denominators separately on both tree factors, take their residues, and only then feed the resulting box/triangle data into the existing Badger moment/subtraction machinery.  The one-variable x Laurent decomposition alone is underdetermined for master topology assignment.  No FDH numerator, D-dimensional gravity double copy, or higher-loop coefficient should be promoted before this lift is completed.

## Other fronts

The scalar cut -> dispersion -> regulated raised-box endpoint remains closed at `J_epsilon(S,T) -> 1/6` with no regression.

The principal-series / completed-zeta / Weil boundary is unchanged: Delta=2s, critical-line half-density unitarity, shadow conjugation, and local Gamma/Wiener-Hopf structure remain valid; unconditional positivity of the genuine completed prime-plus-Archimedean Weil quadratic form on an adequate admissible class is still missing.  No RH promotion.

The spectral/chamber target remains the arbitrary-c chain

    Beta(c+ix,c-ix)
      -> logistic real-line integral
      -> Fourier transform rho_c_hat(t)=sech^(2c)(t/2)
      -> rho_c * rho_d = rho_(c+d).

The Beta/Gamma side is already formalized; the real-line change of variables and Fourier uniqueness remain the Lean bottleneck.  No Barnes axiom or unsupported SL(2,C) Plancherel identification is introduced.

No Claude-owned work was inspected in this rotation.
