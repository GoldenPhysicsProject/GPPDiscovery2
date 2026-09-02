# Major literature correction: nonlinear gravitational googly status

## Finding

The blanket statement that the classical fully nonlinear gravitational googly problem is still wholly unsolved is too strong.

Atul Sharma, `Twistor action for general relativity`, arXiv:2104.07031v2 (2021), explicitly constructs a twistor action for Euclidean vacuum GR and states that it provides a classical fully nonlinear resolution of the googly problem. The paper proves equivalence, via an off-shell Penrose transform, to a chiral Plebanski action that is classically equivalent to Einstein gravity up to a topological term.

Core architecture:

- replace an integrable twistor complex structure by an almost complex structure
  `bar nabla = bar partial + V`;
- its Nijenhuis/curvature obstruction is
  `N = bar nabla^2 = bar partial V + 1/2 [V,V]`;
- integrable `N=0` recovers the self-dual nonlinear graviton sector;
- an off-shell Penrose transform reconstructs a tetrad/metric even when the almost complex structure is not fully integrable, subject to the fiber condition used in Proposition 1;
- a Lagrange multiplier field `B` maps to the opposite-chirality spacetime field;
- the twistor action decomposes as
  `S = S_SD + (kappa^2/4) S_int`;
- Sharma proves that the twistor action reduces to Plebanski GR.

Therefore the most accurate current status is:

1. Classical action-level fully nonlinear GR on twistor space: a serious explicit solution exists (Sharma 2021), though it is Euclidean, uses a background fibration / partially integrable almost-complex structure, and the paper itself lists a fully covariant background-independent formulation and quantum consistency as open next steps.
2. Classical nonperturbative construction of individual generic non-self-dual Einstein metrics as ordinary holomorphic data in a single integrable twistor space remains a different and harder notion; the 2026 Schwarzschild construction is notable precisely in that stricter sense.
3. Penrose's original googly goal and modern uses of the term are therefore not uniform. We must state which notion is meant.

## Consequence for our project

Orientation reversal / shadow / Fourier alone does NOT solve the nonlinear interacting problem: it only exchanges/relabels chiral sectors and, linearly, changes representation. The new exact Lean no-go records this.

Our best route is now to integrate the split-signature insights with Sharma's off-shell almost-complex twistor action instead of trying to invent a new nonlinear completion from orientation alone.

Potential synthesis target:

- complexified off-shell twistor geometry of Sharma as the nonlinear core;
- split (2,2) real slice for real X-ray / half-Fourier / light-transform calculations;
- orientation reversal as the exact geometric operation that exchanges the Hodge labels of the two chiral pieces;
- canonical `-4` weight shift / half-Fourier-light transform as the boundary representation map;
- Grassmannian complement and order-four `tau` retained as a separate finite-dimensional lift structure, not identified with the full nonlinear googly operator without an intertwiner theorem.

## Literature distinction to preserve

Sharma 2021: classical fully nonlinear action equivalent to Euclidean GR, with partially integrable almost complex twistor geometry.

Adamo-Araneda-Seet-Sharma 2026: first construction of a particular non-self-dual Einstein metric (Schwarzschild conformal class) entirely from holomorphic data in a twistor space, a stricter single-integrable-space achievement.

These claims are compatible, not contradictory.
