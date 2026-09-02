# Googly refinement: Lorentzian polarity and the canonical -4 shift

Date: 2026-09-02

## New structural distinction

There are now three mathematically different dualities in the linear googly attack. They must not be conflated.

### 1. Complex incidence duality

For a complex 4-space V, annihilator duality sends a Penrose flag

  ell <= W,  dim ell = 1, dim W = 2

to

  W^0 <= ell^0,  dim W^0 = 2, dim ell^0 = 3.

This is holomorphic/algebraic incidence reversal. It acts canonically on twistor lines / Gr(2,4), but annihilation of a twistor point gives a hyperplane rather than a point.

### 2. Lorentzian real-structure polarity

For Lorentzian twistor space, SU(2,2) preserves a Hermitian form of signature (2,2). In a diagonal basis it gives an anti-linear isomorphism

  rho : T -> T*,
  rho(z0,z1,z2,z3) = (conj z0, conj z1, -conj z2, -conj z3).

Hence

  rho(a Z) = conj(a) rho(Z),
  rho^2 = 1

after the chosen T** ~= T identification.

This supplies a genuine pointwise PT -> PT* map on the Lorentzian real structure, but it is anti-holomorphic / anti-linear. It is not the same operation as annihilator duality.

### 3. Cohomological / Fourier / canonical-degree duality

In the modern amplitude convention, doubled helicity n=2h has twistor weight

  k = n - 2.

Four-dimensional twistor Fourier duality has degree shift

  k -> -k - 4,

so

  n - 2 -> -n - 2 = (-n) - 2,

which is exactly opposite-helicity twistor degree.

The same integer -4 is the canonical-bundle degree of CP^3:

  K_CP3 = O(-4).

Serre duality pairs degrees k and -k-4, although on compact CP^3 it also changes cohomological degree q -> 3-q. Therefore the equality of degree reflections is exact, but one must NOT silently identify compact Serre duality with the desired H^1(open PT) googly transform.

## Important falsification result

Lorentzian polarity alone does not generate the helicity weight flip.

If rho(aZ)=conj(a)rho(Z), then pulling back and conjugating a homogeneous degree-k object preserves degree k. Without the outer conjugation it produces anti-holomorphic scaling by conj(a)^k. Thus the anti-linear real structure solves the pointwise PT/PT* identification problem but not the k -> -k-4 problem.

Therefore a viable linear googly operator needs both:

  Lorentzian polarity / reality structure

and

  a Fourier/Radon/cohomological duality carrying k -> -k-4.

This is a useful obstruction because it prevents the false shortcut 'complex conjugation = googly'.

## Current best linear architecture

Complexified geometry:

  F_{1,2}(V)
    --annihilator-->
  F_{2,3}(V*)

Lorentzian real slice:

  PT --rho--> PT*

Cohomological helicity exchange:

  O(k) --G--> O(-k-4)

Bulk orientation:

  star_o -> -star_o,
  SD <-> ASD.

Target commuting relation:

  P_+ o G = R_o o P_-.

Potential stronger square-root relation:

  G^2 ~= R_o,
  G^4 ~= 1.

## What remains open

1. Construct the actual G on Dolbeault/Cech representatives on the relevant open twistor domain, not just its degree law.
2. Prove it descends to cohomology and is gauge/representative independent.
3. Prove the Penrose-transform commuting square with exact normalization.
4. Match the Lorentzian SU(2,2) reality structure.
5. Check MHV <-> anti-MHV amplitudes including phases and little-group weights.
6. Extend from linearized fields to nonlinear Ward/nonlinear-graviton deformations.

Until 1-3 are done, this is not a solved linear googly theorem. Until 6 is done, it is not a general nonlinear googly solution.
