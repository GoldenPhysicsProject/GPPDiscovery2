# Continuous chamber all-cumulants theorem and scalar CI state

## Scalar regulator certification

GPPVerify2 `codex/lean-workbench` is at `1e5cfb8ec1881b42ec53e67289528bff241f963f` (`Repair cold simplex-volume integral proof`). Full Build #2019 is green on this exact head. Cold changed-Lean #873 is still running and has passed checkout, source-sorry, Lean/toolchain setup, package restoration, and Mathlib cache restoration; it is currently compiling changed Lean modules. Do not promote `RaisedBoxOuterDCTClosure` until this cold smoke terminates green.

The target remains

`simplexMoment ε S T -> 1/6`

for `S,T>0`, `0<δ<1`, and `ε -> 0+` through `0 <= ε <= δ`.

## Exact continuous Gamma/Wiener–Hopf chamber cumulants

For `c>0`, take the normalized chamber density

`rho_c(x) = 2^(2c-1)/(pi Gamma(2c)) * |Gamma(c+ix)|^2`,

whose characteristic function is

`phi_c(t) = sech(t/2)^(2c)`.

Then

`log phi_c(t) = -2 c log cosh(t/2)`.

Using

`log cosh x = sum_{n>=1} [2^(2n)(2^(2n)-1) B_{2n}/(2n (2n)!)] x^(2n)`,

and the characteristic-cumulant expansion

`log phi_c(t) = sum_{m>=1} kappa_m(c) (i t)^m / m!`,

all odd cumulants vanish and every even cumulant is

`kappa_{2n}(c) = (-1)^(n+1) c (2^(2n)-1) B_{2n}/n`

or equivalently

`kappa_{2n}(c) = c (2^(2n)-1) |B_{2n}|/n > 0`.

The first values are

- `kappa_2 = c/2`
- `kappa_4 = c/4`
- `kappa_6 = c/2`
- `kappa_8 = 17c/8`
- `kappa_10 = 31c/2`
- `kappa_12 = 691c/4`.

Because the chamber parameter enters linearly, every cumulant is additive:

`kappa_m(c+d)=kappa_m(c)+kappa_m(d)`.

This matches the convolution semigroup `rho_c * rho_d = rho_{c+d}` and identifies `c` as an exact additive fluctuation-depth parameter. The result is a spectral/WH theorem only; it is not a statement about the genuine SL(2,C) Plancherel density and does not imply Weil positivity or RH.

Executable exact-rational audit: `experiments/continuous_gamma_chamber_all_cumulants.py`, commit `85b80ff56a71653a973c39ea3c2eaa985126d96d`.

## Other active fronts

Prime-gas: next formal target remains `M3`, `M4` plus the four countable derivatives of `M1`,`M2`, followed by identification of the Massieu Hessian with the already-positive covariance/Fisher matrix.

Weil/RH: no promotion. Missing global theorem remains positivity of the completed prime-plus-Archimedean Weil form on an adequate admissible class.

YM/gravity: no numerator guessed. After scalar closure, proceed to the full fixed-loop-momentum `Ds=4`, `mu!=0` two-massive-vector color-ordered tree, double physical-projector sewing, and FDH scalar subtraction with coupling/color/orientation/normalization retained.
