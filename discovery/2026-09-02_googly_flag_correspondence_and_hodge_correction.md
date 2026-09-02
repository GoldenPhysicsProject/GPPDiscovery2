# Googly route refinement: flag correspondence, not pointwise PT map

## Correction: applying Hodge star is not the SD↔ASD exchange

For Euclidean four-dimensional Hodge star on 2-forms,

*² = +1,

and the decomposition is into ±1 eigenspaces. Therefore applying `*` preserves each eigenspace:

- self-dual component: `*F_+ = +F_+`,
- anti-self-dual component: `*F_- = -F_-`.

In the Plucker basis `(01,02,03,12,13,23)`, with

s1=(p01+p23)/2,
s2=(p02-p13)/2,
s3=(p03+p12)/2,

a1=(p01-p23)/2,
a2=(p02+p13)/2,
a3=(p03-p12)/2,

the Hodge/complement map gives exactly

s_i -> s_i,
a_i -> -a_i.

Thus the Hodge/complement operation `C` is NOT itself the operation that swaps SD and ASD.

The actual sector exchange comes from reversing the spacetime orientation, which changes the Hodge operator itself:

*_{-o} = -*_o.

Then a field satisfying

*_o F = +F

satisfies

*_{-o} F = -F,

so the same underlying two-form is relabelled from SD to ASD. In Lorentzian signature, after complexification, the analogous statement exchanges the ±i eigenspaces because orientation reversal again sends `*` to `-*`.

This distinction must be kept explicit in the paper.

## Exact incidence meaning of the Grassmannian complement

A complexified spacetime point in the Klein correspondence is a 2-plane

W subset V = C^4,

or projectively a line P(W) subset PT=P(V).

The canonical dual operation is the annihilator

W -> W^0 subset V*,

where W^0 is again 2-dimensional.

On the big cell W(A) represented by `[I|A]`, the annihilator is represented before row reduction by

[-A^T | I].

If det A != 0, row reduction gives

[I | -A^{-T}],

so the Grassmannian complement map

C(A)=-A^{-T}

is exactly the annihilator-plane construction.

This is now formalized at the explicit incidence level in `TwistorAnnihilatorIncidence.lean`.

## Crucial structural point

There is no canonical pointwise map

PT -> PT*

coming from annihilator alone.

A 1-dimensional twistor line `ell subset V` has annihilator `ell^0 subset V*` of dimension 3, not dimension 1. Conversely, a 2-plane W has a 2-dimensional annihilator W^0. Thus complement duality is canonical on spacetime/twistor lines (Gr(2,4)), not on individual projective twistors.

This is not a failure. It suggests the correct googly operation should be a correspondence/integral transform rather than a pointwise map.

## Penrose correspondence interpretation

The ordinary twistor double fibration uses the flag variety

F_{1,2}(V) = { ell subset W subset V : dim ell=1, dim W=2 },

with projections

PT=P(V) <- F_{1,2}(V) -> Gr(2,V).

The Penrose transform is a pull-push/integral transform through this correspondence.

Annihilator reverses inclusions:

ell subset W

implies

W^0 subset ell^0 subset V*.

So it maps a `(1,2)` flag to a `(2,3)` dual flag. This is precisely the natural incidence geometry for the dual Penrose correspondence, whose twistor-side base is the projective dual space.

Therefore the right candidate for the googly map is not a function on twistor points. It is a transformation of the Penrose correspondence itself induced by annihilator duality, followed by the appropriate pull-push/cohomological transform.

This is conceptually much stronger than the old slogan `googly = shadow` because celestial shadow is also an integral intertwiner, not a pointwise reflection of celestial coordinates.

## New proposed commuting architecture

Original correspondence:

PT <- F_{1,2}(V) -> Gr(2,V).

Dual correspondence:

PT* <- F_{2,3}(V*) -> Gr(2,V*).

Annihilator gives the middle/base maps

F_{1,2}(V) -> F_{2,3}(V*),
Gr(2,V) -> Gr(2,V*).

The field-level googly transform should be the induced pull-push intertwiner between the associated cohomology representations.

Only after constructing this induced transform should we compare it to celestial shadow / Knapp-Stein intertwining and to orientation reversal on the bulk curvature.

## Relation to tau factorization

We now have the exact finite-dimensional decomposition

tau = R o C,

where

C(A)=-A^{-T},   C²=I,
R²=-I,          R⁴=I,
RC=CR.

Thus `C` is the annihilator/complement geometry and `R` is the extra order-four lift. This suggests a clean separation:

- googly incidence geometry lives in `C` plus orientation reversal of the Hodge operator;
- the order-four/spinorial sign structure lives in the lift `R`;
- `tau` packages both.

This is promising, but it is not yet a proof that R is the physical spin lift.

## Falsifiers

1. If annihilator duality fails to induce the required cohomology map between the two Penrose correspondences, the proposed googly resolution fails even though the finite Grassmannian factorization remains true.
2. If the induced transform has the wrong helicity homogeneity or fails MHV↔anti-MHV normalization, it is not the physical googly transform.
3. If nonlinear Ward/deformation integrability is not preserved, the result is at most a linearized googly solution.
