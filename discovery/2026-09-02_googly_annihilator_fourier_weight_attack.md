# Googly attack: annihilator correspondence + four-dimensional Fourier weight

Date: 2026-09-02
Status: active focused attack; no nonlinear googly claim.

## Exact geometric correction

Let V be a four-dimensional complex vector space and let a Penrose flag be

  ell <= W <= V,
  dim ell = 1,
  dim W = 2.

Annihilator duality reverses incidence:

  W^0 <= ell^0 <= V*.

Dimension counting gives

  dim W^0 = 2,
  dim ell^0 = 3.

Therefore annihilation gives a canonical point map on the spacetime Grassmannian

  Gr(2,V) -> Gr(2,V*)

but it does NOT give a pointwise map

  PT = P(V) -> PT* = P(V*).

The annihilator of a twistor line is a hyperplane, not a dual-twistor line. This kills the naive pointwise googly route. The correct category is a reversible flag correspondence / integral transform.

Lean status on `GPPVerify:codex/orientation-mass-time-formalization`:

- `TwistorFlagDuality.lean`
  - dualAnnihilator_antitone
  - dualCoannihilator_antitone
  - recover_annihilatorFlag
  - annihilatorFlag_injective
  - plane_annihilator_finrank_two
  - line_annihilator_finrank_three
  - line_annihilator_not_line
- `TwistorAnnihilatorIncidence.lean`
  - explicit big-cell annihilator plane `[-A^T|I]`
  - row reduction to `[I|-A^{-T}]`
- `GrassmannianGooglyDecomposition.lean`
  - complement C(A)=-A^{-T}
  - tau = R o C
  - C^2=1, R^2=-1, tau^2=-1

## Exact homogeneity advance

Write doubled helicity n=2h in Z. The ordinary Penrose-transform homogeneity is

  k = 2h - 2 = n - 2.

The standard dual-twistor representation of the same physical helicity has homogeneity

  -2h - 2 = -n - 2.

A Fourier transform in four twistor variables changes homogeneous degree by

  k -> -k - 4.

Hence

  -(n-2)-4 = -n-2 = 2(-h)-2.

Thus the universal four-dimensional Fourier shift is exactly the ordinary twistor homogeneity of the opposite helicity. Equivalently:

  twistor weight h --Fourier--> dual-twistor weight h

and numerically this equals

  ordinary twistor weight -h.

This is the missing weight compatibility one would need if dual twistor space is identified with the opposite-orientation twistor description.

Lean status:

- `TwistorWeightDuality.lean`
  - fourierWeight(k)=-k-4
  - fourierWeight involutive
  - fourierWeight(twistorWeight n)=dualTwistorWeight n
  - dualTwistorWeight n = twistorWeight(-n)
  - unique fixed weight k=-2
  - photon pair 0 <-> -4
  - graviton pair 2 <-> -6

## Current candidate linear googly chain

The best current candidate is not a point map. It is:

1. Penrose incidence flag F_{1,2}(V).
2. Annihilator duality to F_{2,3}(V*).
3. A Fourier/Radon/Penrose correspondence transform to dual-twistor cohomology.
4. The universal weight shift k -> -k-4.
5. Opposite-orientation identification of dual twistor geometry.
6. Orientation reversal changes the Hodge operator star_o -> -star_o and therefore exchanges SD/ASD labels.

Desired linear commuting square:

  P_plus o G = R_o o P_minus.

The finite incidence and weight pieces are now exact. Missing:

- analytic/cohomological construction of G on the relevant H^1/Dolbeault classes;
- proof that the Fourier/Radon transform respects the Penrose pull-push and reality structure;
- exact phase/normalization and MHV <-> anti-MHV check.

## Nonlinear bar

Even a complete proof of the linear square is not the full googly solution. The nonlinear target still requires:

- map between nonlinear twistor deformations;
- preservation of integrability / Einstein or Yang-Mills field equations;
- involution modulo gauge/diffeomorphism;
- amplitude equality with exact phases and normalization.

Recent 2026 Schwarzschild work is a special non-self-dual construction, not a universal solution.

## Falsifier

If no canonical cohomological transform induced by the annihilator correspondence yields the weight shift and the opposite-helicity Penrose field with correct reality/normalization, then the Grassmannian/orientation route fails already at the linear googly level.
