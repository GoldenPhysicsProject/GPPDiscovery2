# Zeta Gibbs differential entropy audit

Date: 2026-08-26

## Scope

Honest real Gibbs axis only: `beta > 1`. No thermodynamic interpretation is extended through analytic continuation.

## Inputs already formalized in GPPVerify2

For the real zeta Gibbs family,

- `A(beta) = log Z(beta)` with `A'(beta) = -U(beta)`;
- `U'(beta) = -g(beta)`;
- `g(beta) = Var_beta(log(n+1)) > 0`;
- `C(beta) = beta^2 g(beta) > 0`.

Here `g` is the Fisher metric coefficient / log-energy variance.

## Differential closure

Define

`S(beta) = A(beta) + beta U(beta)`.

Then exactly

`S'(beta) = A'(beta) + U(beta) + beta U'(beta)`

`          = -U(beta) + U(beta) - beta g(beta)`

`          = -beta g(beta)`.

Therefore, for `beta > 1`,

`S'(beta) < 0`,

and since `C(beta) = beta^2 g(beta)`,

`S'(beta) = -C(beta)/beta`,

`C(beta) = -beta S'(beta)`.

This closes the distinction between the previously named algebraic `entropyBetaDerivative` response and the derivative of an explicit entropy potential.

## Verification target

Formalized in GPPVerify2 as `GppVerify/RiemannHypothesis/ZetaGibbsEntropyDerivative.lean` with a dedicated fast-gate build target.

## Next thermodynamic frontier

The next nonredundant calculus target is the Helmholtz free-energy derivative on `beta > 1`:

`F(beta) = -A(beta)/beta`, hence

`F'(beta) = (A(beta) + beta U(beta))/beta^2 = S(beta)/beta^2`.

After bridging the zeta-axis entropy potential to the existing normalized Gibbs entropy definition, this gives the exact Legendre differential package `F' = S/beta^2`, `S' = -beta g`, `C = beta^2 g` in one compatible coordinate system.
