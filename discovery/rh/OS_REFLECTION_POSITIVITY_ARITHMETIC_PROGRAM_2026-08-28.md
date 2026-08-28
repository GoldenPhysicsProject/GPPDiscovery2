# Arithmetic reflection positivity as the RH bridge

Codex/GPT continuation, 2026-08-28.

## Core structural guess

The Weil paired form has the same architecture as Osterwalder--Schrader reflection positivity.

In OS Euclidean QFT one has:

- an involutive reflection `theta`;
- a positive-time subspace `A_+` of observables/test functions;
- a positive functional/state `omega`;
- the reflected sesquilinear form

  <F,G>_OS = omega(theta(F)^* G),

  with reflection positivity

  <F,F>_OS >= 0  for F in A_+.

After quotienting the null space and completing, the OS reconstruction theorem produces a Hilbert space and a positive-energy time evolution.

For the zeta/explicit-formula problem, the natural arithmetic reflection is

  iota(s) = 1 - conjugate(s),

whose fixed locus is exactly the critical line Re(s)=1/2.

The existing finite Weil paired form has the schematic shape

  Q(c) = sum_rho conjugate(c(iota rho)) c(rho).

On the fixed locus this becomes a sum of absolute squares. Off the fixed locus, interpolation on the pair-support can produce indefinite directions. Thus RH is precisely the statement that the zero spectral support lies on the reflection-fixed locus, equivalently that this paired form is positive on the full admissible test class.

This is structurally the same logic as reflection positivity: positivity of a reflected pairing forces the physical spectral support onto the unitary/fixed subspace.

## What would count as the arithmetic OS axioms

A viable number-theoretic analogue should contain at least:

1. Reflection/involution:
   `theta` induced by the functional equation, s -> 1-conjugate(s).

2. Positive half-space/test algebra:
   a Mellin/Paley--Wiener class associated to positive logarithmic scale (or a Hardy-type half-space), stable under the operations needed by the explicit formula.

3. Positive arithmetic state/function(al):
   a functional defined independently on the prime/geometric side, not by assuming the zero side is positive.

4. Reflection-positive pairing:

      B(f,g) = Omega(theta(f)^* * g)

   with B(f,f) >= 0 for the positive-half test class.

5. Reconstruction:
   quotient by the null space and complete to a Hilbert space carrying the scaling representation. The spectral parameter should then be forced to the unitary principal series, i.e. Re(s)=1/2.

The critical point is item 3-4: positivity must be proved from the prime/geometric side, not imported from the zero expansion.

## Physics-to-number-theory clue from the causal diamond

The causal-diamond Fisher calculation supplies a concrete OS-like model.

The KMS/Fisher kernel at beta=2pi is

  kappa(lambda) = pi lambda / sinh(pi lambda)
                = |Gamma(1+i lambda)|^2,

while the KL Plancherel density is

  rho_KL(lambda) = (2/pi^2) lambda sinh(pi lambda).

Their product is

  rho_KL(lambda) kappa(lambda) = (2/pi) lambda^2 >= 0.

Thus a thermal/modular reflection-positive object times the harmonic-analysis Plancherel measure produces a manifestly positive polynomial spectral measure. The archimedean Gamma factor is therefore not merely an analytic decoration: it can literally be a KMS/reflection-positivity kernel.

This suggests looking for the global arithmetic pairing as a product of local reflection-positive kernels, with the archimedean place supplied by the Gamma/KMS factor and the finite places supplied by prime/local Euler data.

## Number-theory-to-physics clue

Weil's criterion says the desired global positivity is equivalent to RH. Connes--Consani have independently sought a Hilbert-space/trace explanation of Weil positivity using compressed scaling actions on the adele class space. This is strongly consistent with the OS reconstruction viewpoint: construct a positive reflected Hilbert-space form first, then interpret the critical-line spectrum as the unitary reconstructed spectrum.

The function-field Weil proof is also the model: positivity comes from an intersection pairing/Hodge-index-type theorem, and the functional equation supplies the reflection. For number fields, the missing object may be an analytic/operator-theoretic replacement of that positive intersection form.

## Exact research target

Do not try to prove positivity directly from the zero sum.

Instead construct an arithmetic Euclidean/reflection-positive functional on the prime/geometric side:

  Omega_prime(theta(f)^* * f) >= 0,

then prove that the explicit formula identifies it with the Weil quadratic form.

If successful, the chain would be

  prime-side reflection positivity
      -> positive semidefinite Weil form
      -> existing interpolation bridge
      -> RH.

The decisive theorem is therefore an arithmetic reflection-positivity theorem for the admissible Mellin test algebra.

## Candidate implementations to investigate

- multiplicative group R_+^x in logarithmic time, reflection x -> x^{-1};
- Mellin transform, where reflection becomes s -> 1-conjugate(s) after half-density normalization;
- positive-time algebra consisting of functions supported on log x >= 0;
- convolution `f^sharp * f` with f^sharp(x) = x^{-1} conjugate(f(1/x)) or its half-density-normalized version;
- evaluate the explicit-formula distribution on this reflected convolution;
- determine whether each local contribution (archimedean and p-adic) is positive or whether positivity appears only after the global product/cancellation;
- compare directly with Connes--Consani compressed scaling and Sonin-space constructions;
- formulate an abstract Lean reflection-positivity lemma matching the existing `WeilInterpolationBridge` paired form.

## Warning

This is not yet a proof of RH. Weil positivity is itself equivalent to RH, so merely renaming the Weil form "reflection positive" gains nothing. The gain only occurs if reflection positivity is derived independently from an arithmetic state/Hilbert-space construction on the prime/geometric side.
