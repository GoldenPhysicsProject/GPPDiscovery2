# Which Way Is Forward? — formalization attack

Date: 2026-09-02
Owner: Codex/GPT
Status: active discovery plan tied to actual GPPVerify theorems

## Goal

Formalize as much of the flagship paper as is honestly reducible to finite algebra, real/complex analysis, matrix identities, and explicit transformation laws. Do not encode open physics as axioms or vacuous `True` theorems. The target is a theorem graph in which the exact core is machine checked and every remaining physical bridge is isolated as an explicit hypothesis/conjecture.

## Existing verified backbone

Already in canonical `GPPVerify`:

- `GrassmannianMass.lean`: chart transition `tau^2=-id`, `tau^4=id`, exact period four.
- `GrassmannianJacobian.lean`: denominator-cleared Jacobian `N^4=D^4 I` via `N^2=D K`, `K^2=D^2 I`.
- `StandardModel/MassOrientationCoupling.lean`: positive Hermitian momentum spinor decomposition and determinant/symplectic mass identity; rest-frame Dirac clock special values and chiral population oscillation.
- `StandardModel/HalfFlipProposition.lean`: Hermitian conjugation/transpose identity, explicit Wigner `T^2=-1` on C^2.
- `QuantumInformation/ChoiMatrix.lean` + `TransposeNotCompletelyPositive.lean`: d=2 no-enactment theorem for transpose/antiunitary conjugation.
- `StandardModel/OrientationMassTime.lean` (new Codex file, commit `47c56912acb34caf655cee1ae4aa0a2822849cc3`): Compton clock/ruler identities, zitter reciprocal pair, relational half-flip sign algebra, universal tangent order-four map, re-exports of Grassmannian fourth-power theorems.

## Paper section -> formal target map

### 1. Oriented gauge lines / half flip

Exact target:

`Q_rel(q,t)=q*t`

- diagonal flip invariant;
- charge-only and orientation-only half flips both negate `Q_rel`;
- the two half flips agree;
- quotient of the four sign pairs by the diagonal Z2 has two classes.

Finite sign algebra is now formalized in `OrientationMassTime.lean`.

Next: replace real-number sign bookkeeping by an actual `Z2 × Z2` quotient/equivalence relation and prove the quotient is equivalent to `Z2`. Then encode Abelian Wilson characters as group homomorphisms and prove path inversion sends a character to its dual.

### 2. Mass as invariant phase density

Exact physical formula:

`omega_C = m c^2 / hbar`, `lambda_C = hbar/(m c)`, hence `lambda_C * omega_C = c`.

Formalized algebraically. Remaining analytic/geometric step: define the free relativistic action/phase on a parametrized timelike curve and formally derive `d theta/d tau = -m c^2/hbar` from the action. This needs a controlled curve/integral/derivative layer, not a postulated equation.

### 3. Dirac rest-frame clock / projective factor two

Existing formalization proves closed-form components and special values. Next targets:

- formalize the 2x2 Pauli matrices as explicit complex matrices;
- prove `U(t)=cos(omega t) I - i sin(omega t) sigma_1` is unitary;
- prove the adjoint action on `sigma_2,sigma_3` rotates by `2 omega t`;
- prove `U(pi/omega)=-I`, `U(2pi/omega)=I` at matrix level;
- connect the already formalized population theorem to the adjoint/Bloch theorem.

This gives a true `SU(2)->SO(3)` projective-clock theorem without claiming it is spatial spin until an intertwiner is built.

### 4. Grassmannian order four and differential

Discovery result:

For `tau(A)=A epsilon/det A`, with tangent `H=A X`,

`d tau_A(A X) = (1/det A) A L(X)`,

where

`L(X)=X epsilon - epsilon tr(X)`.

In row-major coordinates,

`L(x1,x2,x3,x4)=(-x2,-x4,x1,x3)`.

Therefore `L^4=I` and the point dependence is entirely the scalar `D^-1` after tangent trivialization.

New Lean file formalizes the explicit `L^4=I`. Remaining targets:

1. formalize the derivative formula itself using `HasFDerivAt` or a finite-dimensional derivative theorem;
2. prove the coordinate matrix of `L`;
3. prove its characteristic polynomial `t^4-1`;
4. deduce the chart differential characteristic polynomial `t^4-D^-4`;
5. deduce the complex spectrum `{D^-1,-D^-1,iD^-1,-iD^-1}` and equal modulus `1/|D|`.

The already formalized `N^4=D^4 I` is the denominator-cleared polynomial core.

### 5. Physical mass bridge

Existing Lean theorem for a positive 2x2 Hermitian momentum matrix proves

`det p = |<lambda1,lambda2>|^2`.

Do NOT identify the Grassmannian affine chart determinant `D=det A` directly with a dimensionful mass. The correct theorem must construct the physical real/Hermitian slice and projective normalization. Candidate form:

`|D| = m/mu`

for a chosen reference scale `mu` determined by the chart normalization.

This is presently the decisive geometry-to-physics bridge. It should be derived from explicit Pluecker coordinates / Klein correspondence, not assumed.

### 6. Feynman/Stueckelberg switchback

Formalization should start from exact algebra, not historical language.

Targets:

- finite-dimensional gamma-matrix realization sufficient to prove `C gamma^mu^T C^-1 = -gamma^mu` in a fixed representation;
- define the numerator `slash p + m` and prove charge conjugation maps it to `-slash p + m`;
- denominator invariance under `p -> -p`;
- conclude algebraic propagator identity `C S_F(p)^T C^-1 = S_F(-p)` as a rational-matrix identity away from the pole/regulator issue;
- keep the `i epsilon` distributional boundary prescription as a separate analytic layer.

Historical Feynman/Stueckelberg interpretation remains prose/source context; the formal theorem is the propagator identity.

### 7. State + observable conjugation

Abstract Hilbert-space theorem target:

For unitary or antiunitary symmetry `Theta`, transformed state and observable are

`psi' = Theta psi`, `A' = Theta A Theta^-1`.

Prove equality of relational probabilities/real expectation values with the correct antiunitary conjugation rule. This is the clean formal version of "complete conjugation preserves relational statements" and must be distinguished from holding the observable fixed.

### 8. Hodge orientation / chirality

Targets:

- finite exterior-algebra statement: orientation reversal negates the 4D volume element;
- Hodge star on 2-forms changes sign under orientation reversal;
- in Lorentzian signature, after complexification, +/-i eigenspaces are exchanged;
- finite Clifford algebra statement: changing the orientation volume element negates `gamma5`, hence swaps projectors `(1∓gamma5)/2`.

These should be formalized independently before any claim of one common Z2.

### 9. Celestial shadow

Already broad infrastructure exists. Flagship-specific exact target:

`(h,hbar)->(1-h,1-hbar)` implies `(Delta,J)->(2-Delta,-J)`.

Also formalize distinct involutions:

- shadow `Delta -> 2-Delta`;
- conjugation `Delta -> conj Delta`;
- anti-linear composition `Delta -> 2-conj Delta`;
- fixed locus iff `Re Delta = 1`;
- under `Delta=2s`, fixed locus iff `Re s=1/2`.

No RH consequence beyond the fixed-locus identity.

### 10. Observer/record section

Only the abstract logic should be formalized now:

- an involution `iota` on states;
- operational observables invariant under `iota`;
- therefore all statistics built only from those observables coincide.

The physical claim that the real observer algebra is invariant is not formalizable without an observer model and must remain a hypothesis. Thermodynamic arrow inheritance remains open.

### 11. Electroweak obstruction

Formal finite targets:

- complex conjugation sends Jarlskog invariant `J` to `-J`;
- encode finite CKM-like 3x3 complex matrix expression and prove sign reversal under entrywise conjugation;
- later build representation bookkeeping for SM chiral multiplets.

The existence of a full orientation-conjugation functor on the Standard Model remains open.

### 12. Cosmological double-sign invariant

Pure algebra target:

If `H'=-H` and `Sdot'=-Sdot`, then `sign(H' Sdot')=sign(H Sdot)` away from zeros.

Straightforward and worth formalizing, but does not imply a second thermodynamic branch.

### 13. Googly / twistor reconstruction

Do not formalize "googly solved" as a theorem. Formalize the commuting-square criterion itself as a structure of maps and equalities. Populate only the linearized pieces that are actually available. The nonlinear Penrose/shadow reconstruction remains the major gravity target.

## Highest-value proof sequence

1. Build exact Z2xZ2 quotient for the half flip.
2. Finish the `SU(2)` projective Compton clock as explicit matrices.
3. Formalize Grassmannian differential formula and characteristic polynomial.
4. Build the projective/Klein normalization that connects Pluecker mass data to physical `m`.
5. Formalize the free Dirac propagator charge-conjugation identity.
6. Formalize state+observable conjugation covariance.
7. Hodge/chirality orientation exchange.
8. Celestial shadow/conjugation distinction.
9. Jarlskog sign and cosmological double-sign invariant.
10. Only then attempt the Grassmannian-to-Dirac order-four intertwiner and microscopic temporal-lift model.

## Hard theorem target

Construct a Lorentz-covariant map on the physically normalized massive slice

`Phi : Gr_mass -> H_Dirac`

such that a Grassmannian quarter-turn is carried to the quarter-step of the internal Dirac clock,

`Phi (tau A) = U_quarter (Phi A)`.

A successful construction would make the common order-four structure an actual intertwining theorem. Failure is equally informative and must be recorded as an obstruction rather than patched by analogy.
