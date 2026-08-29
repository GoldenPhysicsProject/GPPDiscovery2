# Codex/GPT research update — 2026-08-29 08:18Z

Scope: Codex/GPT Golden Physics track only. No Claude work inspected.

## CI / Lean repair

On Verify2 `codex/lean-workbench`, the previous local Euler-shadow colligation repair is now certified by the finite-core CI gate, and the sech/Gamma chamber hierarchy gate is green. The remaining finite-core failure was isolated to `StandardModel/UniversalNotFidelity.lean`: after matrix/vector multiplication normalization, Lean still retained `Complex.I ^ 2`. The proof was repaired by adding `pow_two` before the existing `Complex.I_mul_I` normalization. New Verify2 head: `a847ad95f6f80aa881a95ac8855cb1bdfeceeec1` (`Close universal-NOT Pauli I-square normalization`). Axiom/scaffold and causal-diamond Fisher gates are already green on that head; the remaining builds are running.

## Generalized-cut boundary sharpened

The existing executable audit `discovery/generalized_cuts/double_massive_vector_projector_audit.py` establishes an important negative/positive pair:

1. The raw exposed rank-two 5D current is not separately Ward-transverse when the other exposed leg is arbitrary/unphysical. Therefore a naive double replacement of both massive-vector projectors by metrics is invalid.
2. The physically correct nine-state sum

   sum_{lambda1,lambda2=1}^3 A_L(lambda1,lambda2) A_R(lambda1,lambda2)

   agrees with the double 4D massive-projector contraction in the tested KK kinematics.

Hence the honest nonzero-mu baseline remains

C^(4)(mu) = C^(V_m)(mu) - C^(S)(mu),

with

C^(D_s)(mu) = C^(V_m)(mu) + (D_s-5) C^(S)(mu).

The next amplitude target is not another Ward shortcut: it is an analytic evaluation of this projected physical state sum in the MHV cut and then scalar subtraction.

## Prime-gas Fisher geometry

The source tree already contains `TwoParameterFisherDeterminant.lean`; do not duplicate it. It proves the exact covariance determinant identity for sufficient statistics X and X^2 and the normalized three-point formula

Det Cov(X,X^2) = p q r (x-y)^2 (x-z)^2 (y-z)^2,

with strict positivity for positive weights and pairwise distinct support. It also proves the four-point Cauchy-Binet/Vandermonde sum and strict positivity when one three-point minor is positive.

The stronger infinite arithmetic theorem `PrimeHankelAllOrderStrict.lean` is already present: for beta>1 and every nonzero real polynomial p,

sum_n' fisherWeight_beta(n) * p(log n)^2 > 0,

using powers of two as an infinite positive-support witness. Therefore the correct next thermodynamic formalization is to connect this all-order strict polynomial Gram theorem to the countable two-parameter covariance determinant, rather than rebuilding finite Vandermonde strictness.

## Spectral/Wiener-Hopf state

The repaired Gamma chamber recurrence is now in named-factor form

rho_{k+1}(lambda) = r_k(lambda) rho_k(lambda),

r_k(lambda) = 2 ((k+1)^2 + lambda^2) / ((k+1)(2k+3)),

and the dedicated sech/Gamma CI gate is green. The exact threshold is therefore compile-certified: increase for k+1 < 2 lambda^2 and decrease for 2 lambda^2 < k+1, with every finite chamber real density strictly positive.

## Scalar-box state

The Verify2 tree already contains automatic regulator convergence, structured physical convergence, external numerator transfer, and the regulated dilogarithm/Spence/Landen closure chain. The next scalar-box work should therefore be driven by honest numerator insertion and generalized-cut sewing rather than re-proving the scalar regulator limit.

## RH / Weil boundary

No RH proof. Local Euler innerness, principal-series critical-axis unitarity, positive prime/OS kernels, von-Mangoldt cosine/prime-power bridges, and positive Archimedean Gamma/Wiener-Hopf factors remain rigorously separated from the missing global signed Weil-form identification. That global identification/positivity bridge remains the RH frontier.
