# Googly/CPT source audit

## Source

GDrive `googly_cpt_section.tex` contains the historical claim that the celestial shadow map `Delta -> 2-Delta` is literally the boundary manifestation of CPT, with the key derivation step asserting that time reversal sends positive Mellin energy `omega` to `-omega` and therefore `Delta=1+i lambda` to `2-Delta`.

## Correction

That derivation is not valid as written.  The standard celestial Mellin transform is over positive energy `omega>0`; replacing `omega` by a negative value is not an operation internal to that Mellin integral, and no equation in the source proves that time reversal acts on the principal-series parameter by `lambda -> -lambda`.  Consequently the manuscript's theorem `shadow = CPT` and its claimed resolution of the googly problem are not established by that argument.

Likewise, the statement that the shadow of a self-dual operator is anti-self-dual "by construction" requires an actual helicity/intertwiner theorem; it cannot be inferred solely from the conformal-dimension reflection.

## Exact structure that *is* now formalized

The current Verify2 route is stronger mathematically and should replace the historical argument as the construction layer:

1. `GooglyAntiunitaryExchange.lean` defines the six-coordinate antiunitary exchange on Plucker data.
2. `GooglyTwistorLift.lean` defines

   `Theta(z0,z1,z2,z3) = (i conj z0, -i conj z1, -i conj z2, -i conj z3)`.

3. Verify2 proves conjugate-linearity, involutivity, coordinatewise Hermitian norm preservation, and the exact exterior-square identity

   `Plucker(Theta v1, Theta v2) = googlyExchange(Plucker(v1,v2))`.

Thus the googly exchange is not an ad hoc bivector sign rule: it is the induced exterior-square action of a concrete antiunitary involution of `C^4`.

## Correct next theorem

Package `Theta` as a conjugate-semilinear equivalence and use it to map complex rank-two submodules of `C^4`.  Prove that its action on the associated projective Plucker class agrees with the already-formalized googly exchange.  This descends the construction to genuine `Gr(2,4)` planes.

Only after that plane-level map exists should one compare it with:

- Hermitian orthogonal complement,
- Hodge/self-dual versus anti-self-dual decomposition,
- celestial shadow intertwiners,
- physical parity/time-reversal/CPT.

Any equality among those structures must be separately proved.  In particular, do not use the old `omega -> -omega` Mellin argument as a theorem.

## Salvageable physical hypothesis

A CPT interpretation remains a viable *hypothesis*: on the critical principal series, shadow sends `Delta=1+i lambda` to `2-Delta=1-i lambda`, i.e. `lambda -> -lambda`, which is complex conjugation of the unitary dilation character.  This representation-theoretic fact is already compatible with the half-density/shadow formalization.  What remains open is identifying the relevant antiunitary physical CPT operator with that representation-theoretic conjugation and with the plane-level googly map.
