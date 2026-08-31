# Raised-box real outer Beta bridge

## Exact reduction

The real singular part left after the certified `x3` and `x2` affine integrations has outer kernel

\[
K_\delta(x)=x^{-\delta}(1-x)^{2-\delta},\qquad 0<x<1,
\]

with physical range `0 < δ < 1` (integrability only needs `δ < 1`). Put

\[
a=1-\delta,\qquad b=3-\delta.
\]

Then `a>0`, `b>0`, and

\[
K_\delta(x)=x^{a-1}(1-x)^{b-1}.
\]

Hence the remaining outer integral is exactly the Euler Beta integral

\[
\int_0^1 x^{-\delta}(1-x)^{2-\delta}\,dx
 = B(1-\delta,3-\delta)
 = \frac{\Gamma(1-\delta)\Gamma(3-\delta)}{\Gamma(4-2\delta)}.
\]

Combining this with the already-certified inner factors gives the one-channel nested singular majorant

\[
\frac{B(1-\delta,3-\delta)}{(1-\delta)(2-\delta)}
 = B(1-\delta,3-\delta)B(1-\delta,2)
 = \frac{\Gamma(1-\delta)^2}{\Gamma(4-2\delta)}.
\]

The middle equality follows from

\[
B(1-\delta,2)
 = \frac{\Gamma(1-\delta)\Gamma(2)}{\Gamma(3-\delta)}
 = \frac{1}{(1-\delta)(2-\delta)}.
\]

Thus the real nested majorant and the previously formalized complex Beta/Gamma certificate have exactly the same constant; the outstanding Lean task is a *real-valued integrability/AE bridge*, not another special-function identity.

## Stable numerical check

Direct quadrature becomes poorly conditioned as `δ -> 1-`. The substitution

\[
x=t^{1/(1-\delta)}
\]

cancels the left endpoint singularity exactly:

\[
x^{-\delta}\,dx=\frac{dt}{1-\delta},
\]

so

\[
B(1-\delta,3-\delta)
 = \frac1{1-\delta}\int_0^1
   \left(1-t^{1/(1-\delta)}\right)^{2-\delta}dt.
\]

`experiments/raised_box_real_outer_beta.py` evaluates this nonsingular representation against `mpmath.beta`, including `δ=0.99`.

## Formalization boundary

Mathlib already supplies `Complex.betaIntegral_convergent` for positive real parts, and the existing GPP `RaisedBoxSimplexBetaLayer.outer_beta_convergent` applies it at `(1-δ, 3-δ)`. The next useful Lean theorem should transfer that certificate to the real kernel `x ^ (-δ) * (1-x) ^ (2-δ)` on `[0,1]` (or prove it directly), then combine it with the existing real inner/middle slice theorems. Once a real `L¹` majorant over the nested affine simplex is available, the remaining regulator step is boundary-face AE removal plus nested dominated convergence for `simplexMoment ε S T -> 1/6`.

No RH, YM, or gravity claim is strengthened by this computation; it closes only the exact real scalar-box majorant algebra needed before DCT.
