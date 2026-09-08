# Codex/GPT rotation: principal-series C Fourier closure

Date: 2026-09-08
Scope: Codex/GPT only. No Claude-owned material inspected.

## New analytic result

Under

- `p(t) = 8 t / sinh(2*pi*t)`,
- `D(t) = Re psi(1/2+i t) - psi(1/2)`,
- `C = E_p[(D')^2]`,

use the exact sine-transform representation

`D'(t) = integral_0^infty [x/(2 sinh(x/2))] sin(tx) dx`

and the already-established characteristic function

`E_p[e^{i s t}] = sech^2(s/4)`.

The resulting two-kernel integral simplifies by

`sech^2((u-v)/2)-sech^2((u+v)/2)
 = sinh(u)sinh(v)/(cosh^2((u-v)/2)cosh^2((u+v)/2))`.

After `a=(u+v)/2`, `b=(u-v)/2`, then `x=tanh a`, `y=tanh b`, one obtains

`C = 8 integral_0^1 (2x-1) atanh(x)^2 dx`.

The endpoint integrals are

`integral_0^1 atanh(x)^2 dx = pi^2/12`,

`integral_0^1 x atanh(x)^2 dx = log 2`.

Therefore

`C = 16 log 2 - 2 pi^2/3`.

This is an analytic closure, not PSLQ evidence. The executable audit is `discovery/principal_series_C_fourier_closure_audit.py`.

## Consequence for A4

The existing exact fourth-score reduction is

`E[D^4] = 2A + 4B - C + 25/2 - 3*pi^2/2`,

where

`A = E[D^2 q^2]`, `B = E[D q D']`, and `q=(pi/2)tanh(pi t)`.

The previous logistic Barnes calculation proved

`B = 2A - 4 + 8 log 2 - 8 log^2 2 + pi^2/6`.

Substituting the newly proved `C` gives the exact one-target reduction

`E[D^4] = 10A - 7/2 + 16 log 2 - 32 log^2 2 - pi^2/6`.

Hence the entire A4 problem is now reduced to the single mixed integral `A`.
If

`A = 1/2 - 2 log 2 + 4 log^2 2`

is proved, then immediately

`A4 = (1/4)E[D^4]
    = 3/8 - log 2 + 2 log^2 2 - pi^2/24`.

The value of A remains high-precision discovery evidence, not yet an analytic theorem.

## Other active fronts

- Celestial scalar cut -> dispersion -> raised-box regulator endpoint remains `J_epsilon -> 1/6`.
- Adjacent-MHV YM rational and four-graviton all-plus one-loop gravity remain closed benchmarks in their stated scopes. Generic convention-locked YM topology projection, generic gravity/helicity sectors, higher multiplicity, and higher-loop generalized cuts remain open.
- Positive-real half-density / principal-series / Delta=2s / critical-line local unitarity remain exact local structures. No RH promotion: completed prime-plus-Archimedean Weil positivity / global Schur gluing remains open.
- Prime-gas strict Fisher positivity remains formalized. The separate two-parameter zeta-Gibbs curvature has both signs; `R <= 0` remains retracted and `R < 1/2` for eta>0 remains the certified global envelope.

## CI

GPPVerify2 `codex/lean-workbench` remains at `1207fa9ff9e6f61243d05ea9df78131200276166`.
Full Build #2124 and changed-Lean #976 are green on that exact head.
No speculative Lean theorem was pushed in this rotation.

## Next frontier

Prove the single remaining mixed integral

`A = E_p[D^2 q^2] = 1/2 - 2 log 2 + 4 log^2 2`.

The most promising route is the Fourier representation of D together with the positive measure `p q^2 = -t mu'(t)`, whose Fourier transform is `phi(s)+s phi'(s)` for `phi(s)=s/(2 sinh(s/2))`.
