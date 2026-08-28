# Causal-diamond Fisher form: exact KL cancellation and the RH bridge

Codex/GPT continuation, 2026-08-28.

This records the exact algebraic core of the uploaded `volume_constraint_entanglement_equilibrium-3(2).tex`, `fisher_form_causal_diamond-2.tex`, and `verify_volume_constraint-1.py`, and places it explicitly inside the active RH/spectral program.

## Exact spectral cancellation

The Kontorovich--Lebedev density used for the radial boost operator is

\[
\rho_{\rm KL}(\lambda)
=\frac{2}{\pi^2}\lambda\sinh(\pi\lambda).
\]

The KMS-symmetric Kubo--Mori/Fisher kernel is

\[
\kappa_\beta(\lambda)
=\frac{\beta\lambda/2}{\sinh(\beta\lambda/2)}.
\]

Hence for nonzero spectral parameter,

\[
\rho_{\rm KL}(\lambda)\kappa_\beta(\lambda)
=\frac{\beta}{\pi^2}\lambda^2
\frac{\sinh(\pi\lambda)}{\sinh(\beta\lambda/2)}.
\]

At the Bisognano--Wichmann inverse temperature `beta = 2*pi`, the hyperbolic factors cancel exactly:

\[
\boxed{
\rho_{\rm KL}(\lambda)\kappa_{2\pi}(\lambda)
=\frac{2}{\pi}\lambda^2
}.
\]

The right-hand side extends continuously to zero and has an exact double zero there. Thus the thermal factor in the Plancherel density and the thermal factor in the Fisher metric remove one another at the modular temperature, leaving a flat quadratic spectral measure on the tempered boost dual.

## Why beta = 2*pi is structurally unique

For general positive beta,

\[
W_\beta(\lambda)
=\frac{\beta}{\pi^2}\lambda^2
\frac{\sinh(\pi\lambda)}{\sinh(\beta\lambda/2)}.
\]

As `lambda -> +infinity`,

\[
\frac{\sinh(\pi\lambda)}{\sinh(\beta\lambda/2)}
\sim
\exp\!\bigl((\pi-\beta/2)\lambda\bigr).
\]

Therefore:

- if `beta < 2*pi`, the weight grows exponentially and cannot be a polynomial;
- if `beta > 2*pi`, the positive weight decays exponentially and cannot equal a nonzero polynomial;
- only `beta = 2*pi` removes the exponential factor identically.

This gives the clean analytic reason for the temperature selection claimed in the Fisher-diamond manuscript. A full formal uniqueness theorem would require the corresponding real asymptotic lemmas; the exact cancellation itself is elementary and is a suitable Lean target now.

## First- and second-order trivial-representation suppression

Near zero,

\[
\rho_{\rm KL}(\lambda)
=\frac{2}{\pi}\lambda^2+O(\lambda^4).
\]

Thus the second-order Fisher form has an exact double zero at the trivial representation. In the first-law channel, the boost charge contributes one additional factor of `lambda`, giving cubic suppression

\[
\rho_{\rm KL}(\lambda)\lambda
=\frac{2}{\pi}\lambda^3+O(\lambda^5).
\]

This is the spectral version of the identity/c-number null direction identified with the cosmological term and proper-volume constraint.

## Relation to the active Weil/RH front

The causal diamond provides an unconditional model with the desired architecture:

\[
\text{tempered dual}
+\text{positive Fisher quadratic form}
+\text{distinguished trivial representation of measure zero}.
\]

The arithmetic program has the analogous target:

\[
\text{principal-series/critical spectral line}
+\text{Weil positive quadratic form}
+\text{distinguished pole/trivial contribution}.
\]

The analogy is now exact enough to guide the proof search, but it is not itself an RH proof. The missing arithmetic theorem remains transport of positivity through the completed explicit formula on the full admissible test class, equivalently exclusion of complementary-series spectral support.

The practical lesson is important: do not search merely for another functional-equation symmetry. Search for the arithmetic counterpart of the diamond cancellation mechanism -- a positive modular/Fisher kernel whose thermal or half-density factor cancels the non-flat Plancherel factor and leaves an explicitly positive spectral measure on the principal series.

## Active targets

1. Formalize `rho_KL * kappa_(2*pi) = (2/pi) lambda^2` in Verify2.
2. Formalize the exact double-zero statement at `lambda=0` for the continuously extended weight.
3. Compare this polynomialized Fisher weight with the existing Gamma/Mehler--Fock/Wiener--Hopf chamber weights.
4. Determine whether the completed-zeta explicit-formula kernel admits an analogous KMS/half-density factorization.
5. Preserve the honesty boundary: the causal-diamond positivity is unconditional; the corresponding global Weil positivity remains the RH-equivalent missing joint.
