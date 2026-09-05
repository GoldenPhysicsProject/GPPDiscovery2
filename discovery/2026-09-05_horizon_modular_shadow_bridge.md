# Horizon modular route: a stronger target than literal c-triggered annihilation

## Result of the current pass

The black-hole horizon hypothesis becomes substantially sharper when compared with the standard modular structure of QFT near horizons.

The Bisognano-Wichmann theorem identifies the modular flow of a Rindler wedge vacuum algebra with Lorentz boosts, while modular conjugation geometrically exchanges/reflection-relates the wedge to its causal complement and is tied to PCT structure.  For static bifurcate Killing horizons, the Hartle-Hawking-Israel construction gives a state whose exterior restriction is KMS at the Hawking temperature.  Therefore horizon duality and horizon thermality are not unrelated phenomena in standard QFT: they meet in the same modular/KMS architecture.

This is potentially the right standard-theory scaffold for the Shadow proposal.  It is far stronger than saying an infalling massive particle reaches c relative to static observers.

## Candidate GPP bridge

Seek an actual identification on the relevant horizon/twistor algebra

D_epsilon  ?=  J_H,

where D_epsilon is the Shadow/epsilon duality currently being constructed from projective Fourier-incidence geometry and J_H is the modular conjugation associated with the horizon wedge algebra.

Then the physical quotient statement

[x] = [D_epsilon x]

would have an operator-algebra analogue in wedge duality, while modular flow supplies the thermal scale rather than adding a Planck factor by hand.

For a Killing horizon with surface gravity kappa,

beta_H = 2 pi / kappa,
T_H = kappa / (2 pi)

in natural units.  A successful bridge should derive that the state induced by the Shadow horizon construction satisfies the KMS condition at beta_H.

## Why this matters for Daniel's self-annihilation intuition

A literal single-fermion decay psi -> 2 gamma is not the correct field-theoretic formulation.  The safer lifted statement is

psi ⊗ D_epsilon psi -> gamma_+ ⊗ D_gamma gamma_+.

The two fermionic legs can be representatives of one physical quotient orbit while remaining distinct legs of a boundary amplitude.  This is exactly the mathematical role needed for 'the fermion meets its reverse-oriented self' without violating the requirement that annihilation has two incoming conjugate states.

The crucial new possibility is that the thermal character could come from modular/KMS entanglement across the horizon rather than from generic pair-annihilation phase space.  That would make Hawking thermality structural instead of assumed.

## Important limits

- Bisognano-Wichmann is a theorem for wedge algebras in relativistic QFT; identifying its J with D_epsilon is open.
- A generic astrophysical collapse horizon is not an eternal bifurcate horizon.  The local near-horizon Rindler structure survives, but a literal global second white-hole wedge does not.
- A photon exactly generating H+ does not escape classically.  An observable exterior photon must be associated with an event outside/stretched horizon or with quantum horizon dynamics.
- Zero null proper time is invariant; 'photon perspective' is not a literal inertial frame.
- The membrane paradigm can motivate boundary-supported exterior bookkeeping but does not imply a literally empty black-hole interior.

## Formalization

Added `GppVerify/CelestialHolography/HorizonModularDuality.lean` on the focused branch.  It conditionally packages an involutive horizon duality, observable quotient invariance, a two-leg boundary conversion, dual charge/orientation cancellation, Hawking beta/temperature reciprocal bookkeeping, and the exact hard `ShadowModularBridge` hypothesis.  It deliberately does not claim to prove Bisognano-Wichmann/KMS analytically.
