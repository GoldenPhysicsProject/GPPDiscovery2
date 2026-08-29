# Number field as a one-dimensional conformal/QFT system: exact-program ladder

Date: 2026-08-29
Track: Codex/GPT
Status: research program with several exact layers already formalized

## Guiding principle

The arithmetic-field-theory program should not rest on verbal analogy.  For each CFT/QFT concept, ask for the precise arithmetic object carrying the same mathematical structure and prove the equivalence/intertwining law.  The strongest present claim is not yet that a number field is a complete 1d CFT in every axiomatic sense.  The evidence instead organizes into a theorem ladder whose first layers are exact and whose missing layers are identifiable.

## Layer 0: the arithmetic space is literally one-dimensional

For a number field `K`, the ring of integers `O_K` is a Dedekind domain, and `Spec(O_K)` is an arithmetic curve of Krull dimension one.  Closed points are nonzero prime ideals.  This is genuine one-dimensional arithmetic geometry, not a dimensional analogy.

The Archimedean places belong in the compactified/arithmetic-completed curve, so the correct global object is inherently local-plus-Archimedean, matching the completed zeta/L-function structure.

## Layer 1: exact GL(1) conformal scale kinematics

The positive real modulus group `R_{>0}^x` is the scale group.  Set

`x = log a`.

Then multiplication of scales becomes one-dimensional translation:

`log(ab)=log a+log b`.

The half-density-normalized arithmetic character is

`chi_s(a) = exp(log(a) (s-1/2))`.

In logarithmic coordinate,

`psi_s(x)=chi_s(exp x)=exp(x(s-1/2))`.

Therefore

`psi_s(x+y)=psi_s(x) psi_s(y)`.

On the critical/principal line

`s=1/2+i tau`, 

this becomes exactly

`psi_tau(x)=exp(i tau x)`,

so the arithmetic spectral parameter `tau` is literally the one-dimensional Fourier momentum conjugate to logarithmic scale.  Shadow gives

`s -> 1-s`, hence `tau -> -tau`,

and therefore exchanges a unitary mode with its inverse/Hermitian conjugate.

This layer is now a Verify2 candidate in `ArithmeticConformalKinematics.lean` (commit `2b39354479450127717749e21bcf920edc66df5b`; CI certification pending at the time of this note).  The next formal improvement is to package `psi_s` as the standard Mathlib additive-character/representation structure rather than only theorem-level equations.

## Layer 2: Tate harmonic analysis is an actual arithmetic field-theory transform layer

Tate's thesis supplies genuine local/global harmonic analysis on the adeles:

- additive characters;
- self-dual Haar measures;
- Fourier transform;
- local zeta integrals;
- restricted products over places;
- Poisson summation;
- Mellin characters of the idele class group;
- the global functional equation assembled from local data.

Thus Fourier/Mellin duality, local-to-global factorization, and Shadow-like functional reflection already exist as exact arithmetic theorems.  The physics task is to identify the correct state/observable interpretation rather than invent an analogy.

Important normalization: the clean centered shadow law uses multiplicative Haar measure `da/a` and the centered exponent `s-1/2`.  One must not silently replace it by a bare Lebesgue Mellin kernel without the Jacobian.

## Layer 3: PGL(2) is the natural global 1d conformal completion

The global conformal transformations of a one-dimensional compactified coordinate are Möbius transformations, represented by `PGL(2)`/`PSL(2,R)` in the real setting.  Number theory already has exactly this group and its adelic form.

The arithmetic candidates are therefore not arbitrary:

- `PGL(2,A)` principal series;
- Eisenstein series;
- Weyl reflection;
- standard/Knapp--Stein intertwining operators;
- spherical vectors and local components;
- Casimir eigenvalues;
- scattering matrices built from completed L-functions.

The Weyl element exchanges the inducing parameter with its reflected value, structurally the same `s <-> 1-s` operation as arithmetic Shadow after the half-density normalization.  The project should make this exact at the operator level and compare its local eigenvalues with the already formalized Euler-shadow colligations and Archimedean Gamma/Wiener--Hopf factors.

This is the most promising rigorous route from the already-proved GL(1) scale sector to a genuine arithmetic global-conformal representation theory.

## Layer 4: local factors as scattering/intertwining data

The project already has exact local structures:

- local Euler factors and logarithmic responses;
- a real orthogonal 2x2 colligation whose transfer function is a Blaschke factor;
- exact prime-Poisson kernels;
- Gamma/Mehler--Fock spectral weights;
- Wiener--Hopf positive factors;
- completed-zeta reflection and principal-series response.

The next question is whether these are the local scattering/intertwining eigenvalues of one common adelic PGL(2) operator.  If yes, the prime and Archimedean sectors are not merely similar pieces: they are local components of a single automorphic/conformal scattering operator.

Concrete target:

`M(s) = tensor'_v M_v(s)`

with a global Weyl/intertwining operator `M(s)` whose scalar spherical coefficient reproduces the appropriate completed zeta ratio and whose unitarity on `Re s=1/2` is the arithmetic principal-series unitarity statement.

This must be checked with the exact convention used by the existing completed-zeta modules; no zero-dependent definition is allowed.

## Layer 5: Bost--Connes gives a genuine arithmetic quantum statistical system

The Bost--Connes construction is not analogy: it is a C*-dynamical quantum statistical mechanical system with time evolution, KMS equilibrium states, a zeta partition function, a phase transition, and arithmetic/Galois symmetry.  Number-field generalizations replace the rational zeta data by number-field/Dedekind-zeta structures.

This gives the arithmetic-field-theory program an already-existing observable-algebra/QSM sector.  The research task is to determine how this algebra and its modular/KMS flow interface with the PGL(2) principal-series/Shadow sector and with the project's prime-gas thermodynamics.

Potential exact bridge:

- idele norm / scaling flow -> QSM time evolution;
- zeta/Dedekind-zeta -> partition function;
- KMS states -> thermal arithmetic states;
- modular flow -> candidate operator-algebraic realization of scale evolution;
- Galois action -> internal arithmetic symmetry.

## Layer 6: what is still needed before saying 'full 1d CFT'

A full claim must specify an accepted 1d conformal-QFT framework and instantiate its data.  Depending on the formulation, this should include enough of:

1. a Hilbert/state space with positive inner product;
2. a unitary/projective `PSL(2,R)` or `PGL(2,R)` action, or an adelic analogue with a precise real conformal sector;
3. an algebra/net of observables or operator insertions;
4. covariance of those observables;
5. a vacuum/cyclic or distinguished state;
6. two-/three-/four-point functions with the correct conformal covariance;
7. an associative OPE or equivalent composition law;
8. crossing/reflection positivity where appropriate;
9. a precise relation between arithmetic local factors and conformal blocks/intertwiners.

Virasoro is a two-dimensional enhancement and is not a prerequisite for a one-dimensional global conformal theory.  The correct intermediate phrase is `arithmetic conformal quantum mechanics`, `arithmetic global-conformal theory`, or `arithmetic CFT skeleton` until the observable/OPE layer is built.

## CFT/QFT concept-mining dictionary

For every familiar physics concept, search number theory/automorphic theory for the exact structural counterpart:

| CFT/QFT concept | arithmetic object to test |
|---|---|
| spacetime/curve | `Spec O_K`, Arakelov compactification, adele classes |
| scale/dilatation | idele norm, positive-real modulus flow |
| log radial time | `x=log |a|` |
| momentum/energy | spectral parameter `tau` in `s=1/2+i tau` |
| primary weight | inducing exponent / quasicharacter |
| shadow | Weyl reflection / standard intertwiner `s <-> 1-s` |
| conformal group | `PGL(2)` / automorphic action |
| conformal Casimir | principal-series Casimir eigenvalue |
| conformal blocks | local/global spherical functions, Whittaker blocks, Eisenstein components |
| propagator/two-point kernel | Green, Poisson, Harish-Chandra/spherical kernels |
| scattering matrix | automorphic intertwining/scattering matrix |
| loop/trace | trace formula, determinant, periodic-orbit/prime sums |
| particles/modes | primes/prime powers/local places, with caution about statistics |
| partition function | zeta/L-functions; Bost--Connes partition function |
| thermal state | Gibbs/KMS states |
| renormalization/scaling | idele flow, explicit-formula scale decomposition, local conductor flow |
| locality | places/valuations and restricted tensor products; must prove the appropriate operator notion |
| OPE/fusion | Hecke convolution, representation tensor products, Rankin--Selberg/local product structures; this is a hypothesis generator, not yet an identity |
| Ward/trace identity | explicit formula / trace formula; exact correspondence still to be constructed |
| crossing | functional equations/intertwiner associativity; exact CFT crossing identification still open |
| modular theory | Tomita--Takesaki/KMS structure in arithmetic operator algebras; investigate Bost--Connes interface |

The rule is: do not stop at a suggestive row.  Either construct the intertwining map/equality or mark the row as a research hypothesis.

## Immediate formalization sequence

1. CI-certify `ArithmeticConformalKinematics.lean`.
2. Bundle the log-scale mode as a standard character/representation of `(R,+)`.
3. Formalize multiplicative-Haar inversion and the centered Mellin Shadow law at the integral level.
4. Inventory existing Tate/local-zeta modules and make the local-to-global Fourier/Mellin structure explicit.
5. Build a minimal `PGL2` principal-series parameter/Weyl-intertwiner layer, reusing existing Casimir/Eisenstein material when possible.
6. Identify exact local Euler and Gamma factors as eigenvalues/coefficients of that intertwiner if the conventions match.
7. Only then define arithmetic two-/three-point/operator data and test OPE/crossing axioms.
8. In parallel connect Bost--Connes/KMS structure to the already formalized zeta Gibbs/prime-gas thermodynamics.

## RH boundary

The conformal interpretation itself does not prove RH.  The useful possibility is sharper: if the completed arithmetic object can be realized as a genuinely unitary/reflection-positive global conformal operator whose quadratic form is exactly the Weil explicit-formula form on an adequate test class, then critical-line occupancy could follow from that operator structure.  The missing theorem remains the global zero-independent prime-plus-Archimedean assembly and its identification with the genuine Weil criterion.

## Source archive targets mined this run

- `rh_cft_note_revised.pdf`
- `arithmetic_principal_series_RH_program-34.pdf`
- `principal_series_blocks_v2.pdf`
- `CH_v13_13_ADELIC_ASSAULT.pdf`
- `path_c_representation_theory.md`

These should be mined repeatedly for exact propositions, with historical overclaims/corrections stored in Supabase `codex.corrections_ledger` and only the strongest surviving construction promoted to Verify2.
