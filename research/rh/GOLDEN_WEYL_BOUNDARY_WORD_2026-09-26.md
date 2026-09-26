# Golden Weyl boundary word: corrected same-coordinate bridge
Date: 2026-09-26
Status: exact scalar algebra + exact finite Suzuki symmetry; operator identification with the completed arithmetic pole update remains open. RH is not proved.

## 1. What was killed

The tempting identification

    x(z) = 2 B(z) / A(z)

with Suzuki's normalized Herglotz/Weyl function is impossible globally.

Suzuki has A(i)=0 while, in the normalized finite extension construction, B(i) != 0 and

    m(i) = -i (A(i)-B(i))/(A(i)+B(i)) = i.

Thus 2B/A is a projective deficiency response with a pole/degeneracy at the normalization point, not the physical Herglotz resolvent/Weyl scalar.

This distinction must be preserved.

## 2. The corrected physical coordinate

Use the genuine finite Suzuki Weyl function

    m(z) = -i W_pi(z)/W_0(z)
         = -i (A(z)-B(z))/(A(z)+B(z)).

The exact parity identities W_pi(-z)=W_pi(z), W_0(-z)=-W_0(z) give

    m(-z) = -m(z).

The opposite 0/pi self-adjoint boundary condition has the canonical Weyl function

    m_dual(z) = -1/m(z).

Therefore spectral reflection followed by opposite-boundary duality is

    m -> -m -> -1/(-m) = 1/m.

Now define the reciprocal physical Weyl coordinate

    y = 1/m.

On y, the same composite is exactly

    S: y -> 1/y.

This is the missing reciprocal operation in the *physical* Weyl channel.

## 3. Krein feedback supplies the translation

For a scalar Green/Weyl response m, unit rank-one Krein feedback is

    K(m) = m/(1+m).

Its reciprocal is

    1/K(m) = 1/m + 1.

Hence in the same coordinate y=1/m,

    T: y -> y+1.

Therefore the physical three-operation boundary word

    spectral reflection
      -> opposite-boundary Weyl duality
      -> unit Krein feedback

acts on y as

    T S(y) = 1 + 1/y.

The fixed-point equation is

    y^2 - y - 1 = 0,

with positive fixed point phi.

No coordinate switching occurs between S and T.

## 4. Exact equivalence with the previous parity Schur coordinates

Set

    x = 2m,
    y = 2/x = 1/m.

Then reflection + boundary duality gives

    x -> 4/x,

while unit Krein feedback gives

    x -> 2x/(x+2).

These are exactly the previously isolated poleDual and oddSchur transformations.

Thus the algebra previously found in the projective Suzuki ratio has a second, physically cleaner realization directly in the normalized Weyl coordinate:

    y = reciprocal Weyl impedance.

The earlier basis-consistency no-go remains valid for *reflection alone*:
reflection followed immediately by an additive shear gives an affine involution.
The correction is that the canonical opposite-boundary duality was missing between reflection and feedback.

## 5. Arithmetic normalization: why the half-density pole pair matters

In the CCM finite Weil matrix,

    W_02 = (1/2) |c><c| - (1/2) |s><s|,

where c is even and s is odd. The c,s vectors are the Cauchy evaluation modes at

    t = +i/2, -i/2,

equivalently the completed-zeta pole/reflection points

    s = 1, 0.

Thus the relevant boundary directions are exactly the half-density exponential modes e^{+u/2}, e^{-u/2}, not arbitrary vectors.

Sherman-Morrison on the two parity channels gives the exact maps

    x -> 2x/(x+2)      (plus 1/2 rank-one channel),
    x -> -2x/(x-2)     (minus 1/2 rank-one channel),

or, in y=2/x,

    y -> y+1,
    y -> y-1.

So the arithmetic completion already contains the translation generators with the same half-density normalization.

## 6. Modular / transfer-matrix invariant

The golden return map

    y -> 1 + 1/y

is represented projectively by

    F = [[1,1],[1,0]], det F = -1.

Its square is

    F^2 = [[2,1],[1,1]], det = 1, tr = 3,

with eigenvalues phi^2 and phi^-2.

This is the same trace-3 hyperbolic SL(2,Z) class independently found in the unit-mass Casimir/Wiener-Hopf transfer sector. The robust invariant is the trace-3 hyperbolic conjugacy class; the numerical coordinate phi becomes meaningful only after the arithmetic boundary normalization is fixed.

## 7. The one load-bearing operator theorem still missing

Do NOT declare the bridge complete until the following is proved or falsified.

**Completed Weyl-pole feedback theorem (target).**
Show that, under the canonical finite Suzuki/CCM boundary triple with half-density pole modes, adding the completed pole hyperbolic-plane channel induces on the normalized physical Weyl/Green scalar the unit Krein transform

    m -> m/(1+m)

(up to a fixed sign/orientation convention already accounted for by parity).

Equivalent formulations are acceptable:
- a Schur-complement identity in the finite parity blocks;
- a determinant-ratio/Krein resolvent identity for W_0,W_pi;
- an equality between the CCM boundary Green scalar and the Suzuki Weyl scalar after the fixed half-density normalization.

If this theorem holds, the shadow/reflection and pole update genuinely act on the same scalar boundary channel and the modular/golden word is structural, not a basis trick.

If it fails, record the exact Möbius coefficient. A non-unit coefficient would identify precisely where the arithmetic completion departs from the golden conjugacy class.

## 8. Relevance to RH closure

Even if the completed Weyl-pole feedback theorem holds, the golden fixed point alone does not prove RH.

The useful possible consequence is dynamical: the square return map has stable multiplier phi^-2. If the completed arithmetic boundary evolution can be shown to stay in the corresponding stable cone/projective sector, it could provide a uniform no-escape / boundary-transfer bound. The current RH frontier only needs subexponential semiboundedness of the completed localized Weil form; polynomial control is sufficient.

This is therefore a plausible mechanism for the missing global boundary estimate, not a replacement for that estimate.

## Formalization

GPPVerify branch `codex/rh-boundary-closure`:
- `GppVerify/RiemannHypothesis/GoldenWeylBoundaryWord.lean`
- commit 6ec7c1c873df5318ba8b7e0669c4a6802edf4900

The module formalizes:
- physical Suzuki Weyl reflection;
- canonical negative-reciprocal boundary duality;
- reciprocal-coordinate Krein translation;
- golden return word in y=1/m;
- equivalence to x->4/x and oddSchur in x=2m;
- the no-go at z=i for identifying 2B/A with the normalized Weyl scalar.

CI state at time of writing: no workflow run/status attached to the connector-created commit; do not claim build certification yet.
