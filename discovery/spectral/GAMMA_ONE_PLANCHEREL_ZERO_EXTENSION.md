# Gamma-one principal-series Plancherel weight: zero-extension audit

The source-mined principal-series density is

`P(lambda) = pi*lambda/sinh(pi*lambda)`.

For `lambda != 0`, Euler reflection plus the Gamma recurrence give exactly

`Gamma(1+i lambda) Gamma(1-i lambda) = pi*lambda/sinh(pi*lambda)`.

Because `Gamma(1-i lambda) = conj(Gamma(1+i lambda))`, this is the usual modulus-square identity.

## Essential zero boundary

The quotient must **not** be used naively as an all-real Lean definition.  Lean fields totalize division, hence

`pi*0/sinh(pi*0) = 0/0 = 0`,

whereas

`Gamma(1+i*0) Gamma(1-i*0) = Gamma(1)^2 = 1`.

Analytically,

`lim_{lambda->0} pi*lambda/sinh(pi*lambda) = 1`.

Therefore define the all-real principal-series weight by removable extension:

`Pext(lambda) = if lambda = 0 then 1 else pi*lambda/sinh(pi*lambda)`.

Then the intended exact all-real theorem is

`Gamma(1+i lambda) Gamma(1-i lambda) = Pext(lambda)`.

## Lean route

Current Mathlib provides `Complex.Gamma_add_one` and `Complex.Gamma_mul_Gamma_one_sub`.  For `lambda != 0`, set `z=i lambda`:

1. `Gamma(1+z) = z Gamma(z)` by `Complex.Gamma_add_one`;
2. `Gamma(z) Gamma(1-z) = pi/sin(pi z)` by reflection;
3. `sin(i pi lambda) = i sinh(pi lambda)`;
4. cancel the nonzero `sinh(pi lambda)` to obtain `pi lambda/sinh(pi lambda)`.

At `lambda=0`, simplify directly with `Gamma_one` and the branch of `Pext`.

This target is distinct from the already-formalized half-shifted collapsed weight

`Gamma(1/2+i lambda)Gamma(1/2-i lambda)=pi/cosh(pi lambda)`.

It should be added as the exact Gamma realization of the source-mined principal-series Plancherel density before attempting Legendre/Mehler-Fock transform inversion.
