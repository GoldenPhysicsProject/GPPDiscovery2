# Log-energy discrepancy and the RH decay boundary

Codex/GPT discovery track, 2026-08-24.

This note sharpens the pole-subtraction picture. It is an equivalence/diagnostic bridge, **not a proof of RH**.

## 1. Weighted von Mangoldt counting in logarithmic energy

Let

\[
\psi(X):=\sum_{n\le X}\Lambda(n),
\]

and define the `1/n`-weighted cumulative arithmetic measure

\[
R(x):=\sum_{n\le e^x}\frac{\Lambda(n)}n,
\qquad x\ge0.
\]

The signed pole-subtracted measure from the companion note is

\[
d\rho-dx,
\qquad
\rho=\sum_{n\ge2}\frac{\Lambda(n)}n\delta_{\log n}.
\]

Its cumulative discrepancy is therefore

\[
\boxed{A(x):=R(x)-x.}
\]

## 2. Exact partial summation formula

For `X=e^x`, Stieltjes/Abel partial summation gives

\[
\sum_{n\le X}\frac{\Lambda(n)}n
=\frac{\psi(X)}X+\int_1^X\frac{\psi(u)}{u^2}\,du.
\]

Writing

\[
E(X):=\psi(X)-X,
\]

we obtain exactly

\[
\boxed{
R(\log X)-\log X
=1+\frac{E(X)}X+\int_1^X\frac{E(u)}{u^2}\,du.
}
\]

Whenever the improper integral converges, its limiting constant is fixed by the Laurent expansion of the zeta logarithmic derivative at `s=1`. Since

\[
-\frac{\zeta'}{\zeta}(1+z)=\frac1z-\gamma+O(z),
\]

one has

\[
\boxed{A(x)\to-\gamma}
\]

under the standard prime-number-theorem strength needed for the limit.

Equivalently, subtracting the limiting constant gives the exact tail relation

\[
\boxed{
A(\log X)+\gamma
=\frac{E(X)}X-\int_X^\infty\frac{E(u)}{u^2}\,du,
}
\]

provided the tail integral converges.

## 3. RH implies the critical exponential decay

The classical RH consequence

\[
E(X)=O(X^{1/2}\log^2 X)
\]

implies

\[
\frac{E(X)}X=O(X^{-1/2}\log^2X)
\]

and

\[
\int_X^\infty\frac{E(u)}{u^2}\,du
=O(X^{-1/2}\log^2X).
\]

Hence

\[
\boxed{
A(x)+\gamma=O(e^{-x/2}x^2).
}
\]

The logarithmic-energy discrepancy therefore relaxes to its background constant at precisely the critical exponential rate `e^{-x/2}` (up to polynomial factors).

## 4. Why the exponent 1/2 is the analytic-continuation boundary

For `Re z>0`, the pole-subtracted logarithmic derivative is

\[
-\frac{\zeta'}{\zeta}(1+z)-\frac1z
=\int_0^\infty e^{-zx}\,dA(x).
\]

After separating the constant limit and integrating by parts in the region where justified, the decaying part is governed by a Laplace transform of

\[
A(x)+\gamma.
\]

If

\[
A(x)+\gamma=O(e^{-\alpha x}\operatorname{poly}(x)),
\]

then that Laplace integral naturally extends to

\[
\Re z>-\alpha.
\]

The RH rate `alpha=1/2` therefore reaches

\[
\boxed{\Re z>-1/2.}
\]

Since `s=1+z`, the boundary `Re z=-1/2` is exactly

\[
\boxed{\Re s=1/2.}
\]

This gives a clean real-variable explanation for why the critical-line exponent appears after pole subtraction: it is the decay exponent of the centered arithmetic spectral discrepancy in logarithmic energy.

## 5. Converse status

This note should not be read as an unconditional derivation of that decay. A sufficiently strong bound of the form

\[
A(x)+\gamma=O(e^{-(1/2-\varepsilon)x}\operatorname{poly}(x))
\]

for every `epsilon>0`, together with the exact partial-summation relation and standard Tauberian/explicit-formula control, is essentially another encoding of the classical prime-counting consequences equivalent to excluding zeros to the right of the critical line.

So the result is a **reparameterization of the RH boundary**, not a way around it.

## 6. Relation to the positivity program

Before subtraction, the arithmetic measure is positive and its Laplace--Fourier transform is positive type. Pole removal centers it against the continuum background and produces `dA`, a signed discrepancy measure. The RH problem is then tied to the exact decay/oscillation of this signed discrepancy.

A successful global Weil-square construction must therefore accomplish more than preserve the local Euler-factor positivity: it must incorporate the continuum subtraction and Archimedean completion in a way that reorganizes this signed discrepancy into a positive quadratic functional on the correct test class.

That is the precise frontier.
