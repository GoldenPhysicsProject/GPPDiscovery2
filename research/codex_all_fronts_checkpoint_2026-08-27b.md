# Codex all-fronts checkpoint — 2026-08-27 (late run)

This note records Codex/GPT work only. No Claude-side material was inspected.

## 1. Raised `D = 8 - 2 eps` scalar-box residue

For the Euclidean chamber `S,T>0`, use the standard Feynman-parameter form

\[
I_4^{(8-2\epsilon)}(S,T)=\Gamma(\epsilon)J_\epsilon(S,T),\qquad
J_\epsilon=\int_{\Delta_3}
  (Sx_1x_3+Tx_2x_4)^{-\epsilon}\,dx.
\]

The finite `mu^4` dimension-shift limit needs only

\[
\epsilon I_4^{(8-2\epsilon)}\to \frac16,
\]

not the stronger Laurent estimate `I = 1/(6 eps) + O(1)`, because exactly

\[
-\epsilon(1-\epsilon)I(\epsilon)
=-(1-\epsilon)[\epsilon I(\epsilon)].
\]

This reduction is now formalized in Verify2 (`Mu4DimensionShiftAlgebra.lean`).

The analytic residue proof reduces to dominated convergence. On the simplex
interior, `Q=S x1 x3 + T x2 x4 > 0`, so `Q^{-eps} -> 1`. For
`0 < eps <= a < 1`,

\[
Q^{-\epsilon}\le 1+Q^{-a}
\le 1+S^{-a}x_1^{-a}x_3^{-a}.
\]

The majorant is integrable and its nontrivial Dirichlet piece is

\[
\int_{\Delta_3}x_1^{-a}x_3^{-a}\,dx
=\frac{\Gamma(1-a)^2}{\Gamma(4-2a)}.
\]

At `a=1/2` this is exactly `pi/2`. Therefore
`J_eps -> Vol(Delta_3)=1/6`. Since
`eps Gamma(eps)=Gamma(1+eps)->1`, the residue follows.

Executable numerical audit: `research/raised_box_residue_audit.py`.

Honest boundary: this does not yet formalize the simplex integral, dominated
convergence, or the full Yang--Mills/gravity generalized cut. Gravity still has
four uncut denominators after the KLT cut and needs a genuine reduction.

## 2. Weil / Wiener--Hopf / RH bridge

A stale target has been retired. Verify2 already proves on `a>1` that the global
prime-Poisson `tsum` is positive type and, through the von Mangoldt bridge, that

\[
t\mapsto 2\,\Re\left[-\frac{\zeta'(a+it)}{\zeta(a+it)}\right]
\]

is positive type.

`WeilSupportLadder.lean` also already proves:

- exact support doubling for convolution squares;
- exact finite truncation of the prime side on compact support;
- rung-zero disappearance of the prime side below `log 2`;
- the Fourier dictionary
  `int exp(-eps|u|) cos(xu) du = 2 eps/(eps^2+x^2)`.

The RH-level missing statement is therefore not local/global prime positivity.
It is the exact completed explicit-formula transport on convolution-square tests,
followed by finite interpolation from admissible transforms to arbitrary finite
zero coefficients and a positivity-preserving uniform passage through the
critical-line boundary. That remains equivalent in strength to the Weil
criterion and is not being assumed.

## 3. Zeta Gibbs thermodynamics

Another stale target is retired. Verify2 already proves the genuine Gibbs law

\[
\frac{d}{d\beta}\kappa_2(\beta)=-\kappa_3(\beta),\qquad \beta>1,
\]

and strict positivity of `kappa_3`, hence strict decrease of the Fisher variance.
It also contains the Bregman/Jeffreys information-geometric identities and strict
directed-KL orientation.

The next nonduplicative cumulant target is the fourth-cumulant layer:

\[
\kappa_4 = \mu_4-3\mu_2^2,\qquad
\kappa_3'=-\kappa_4.
\]

No sign is asserted for `kappa_4`; unlike `kappa_3` in this arithmetic family,
there is no generic reason for a fourth cumulant to be positive.

## 4. Sech / Wiener--Hopf exact normalization

Verify2 now contains a pushed zero-shift module proving, subject to CI,

\[
\int_{\mathbb R}\frac{dx}{\cosh^2(\pi x)}=\frac2\pi
\]

from the project-certified derivative of `tanh` and explicit endpoint limits.
It then combines the zero and nonzero cases into

\[
\int_{\mathbb R}\frac{dx}
 {\cosh(\pi x)\cosh(\pi(\lambda-x))}
=\frac2\pi\,W_{\mathrm{ext}}(\lambda)
\]

for every real `lambda`, where `W_ext(0)=1` and away from zero
`W_ext(lambda)=pi lambda/sinh(pi lambda)`.

The dedicated sech workflow was expanded to compile the new module explicitly.
At the time of writing that CI job is still running, so this note does not mark
the new theorem certified yet.
