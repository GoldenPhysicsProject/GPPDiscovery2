# Continuous-sech derivative tail and cosh-product bridge

## Scope

Codex/GPT track only. No Claude-owned material inspected.

## 1. Sharp derivative tail

For

\[
\nu_c(x)=\frac{c}{|x|\sinh(\pi|x|)},\qquad
D_c(t,x)=x\sin(tx)\nu_c(x),\qquad c\ge0,
\]

and \(|x|\ge1\), the exact denominator estimate

\[
\sinh(\pi|x|)\ge
\frac{1-e^{-2\pi}}2e^{\pi|x|}
\]

gives

\[
\boxed{
|D_c(t,x)|\le
\frac{2c}{1-e^{-2\pi}}e^{-\pi|x|}}
\]

independently of `t`. Together with the already formalized global core bound

\[
|D_c(t,x)|\le \frac{c|t|}{\pi},
\]

this gives, uniformly on \(|t|\le T\), the piecewise majorant

\[
G_{c,T}(x)=
\begin{cases}
 cT/\pi,&|x|\le1,\\[2mm]
 \dfrac{2c}{1-e^{-2\pi}}e^{-\pi|x|},&|x|>1.
\end{cases}
\]

Its exact mass is

\[
\boxed{
\int_{\mathbb R}G_{c,T}(x)\,dx
=\frac{2cT}{\pi}
+\frac{4ce^{-\pi}}{\pi(1-e^{-2\pi})}.}
\]

Numerically, the sharp tail coefficient is
`2/(1-exp(-2*pi)) = 2.0037418731973212882...`, replacing the previous crude coefficient `4`.
The tail contribution to the `L1` mass at `c=1` is
`0.055124611671792625758...`.

The exact derivative-tail inequality was pushed to GPPVerify2 as the next Lean theorem after the certified `sinh_tail_lower` lemma.

## 2. A direct cosh-product route already latent in Verify2

Verify2 already proves the genuine infinite product

\[
\frac{\sinh(\pi\lambda)}{\pi\lambda}
=\prod_{j=1}^{\infty}\left(1+\frac{\lambda^2}{j^2}\right)
\]

as a `Tendsto` theorem (`GppSinhWeierstrass.tendsto_prod_one_add_sq_div`).
This means no independent Mittag-Leffler theorem is needed merely to obtain the odd-mode cosh product.

Define

\[
S_N(t)=\prod_{j=1}^{N}\left(1+\frac{t^2}{\pi^2j^2}\right).
\]

Then the finite identity

\[
\prod_{n=0}^{N-1}
\left(1+\frac{t^2}{(2n+1)^2\pi^2}\right)
=
\frac{S_{2N}(t)}{S_N(t/2)}
\]

is exact, because the denominator is precisely the product of the even-index factors of `S_{2N}`. The existing sinh-product theorem therefore gives

\[
S_{2N}(t)\to\frac{\sinh t}{t},\qquad
S_N(t/2)\to\frac{\sinh(t/2)}{t/2},
\]

and hence, for `t != 0`,

\[
\boxed{
\prod_{n=0}^{\infty}
\left(1+\frac{t^2}{(2n+1)^2\pi^2}\right)
=\frac{\sinh t/t}{\sinh(t/2)/(t/2)}
=\cosh(t/2).}
\]

The `t=0` case is trivial. This gives a particularly economical Lean route to the half-integer/odd spectral product: reuse the already-certified sinh Weierstrass product and prove only (i) the finite even/odd factor decomposition and (ii) quotient-of-limits bookkeeping.

Logarithmic differentiation of this product is then the exact target

\[
\frac12\tanh(t/2)
=2t\sum_{n\ge0}
\frac1{(2n+1)^2\pi^2+t^2},
\]

which matches term-for-term the series obtained from
`1/sinh(pi*x) = 2 sum_{n>=0} exp(-(2n+1)pi*x)` and the elementary Laplace-sine transform. The product identity therefore connects the existing `SinhWeierstrassProduct.lean` infrastructure directly to the outstanding sine-over-sinh transform.

## 3. Honest front status

- Scalar celestial cut -> Mellin -> dispersion -> raised-box regulator remains closed, with regulator endpoint `1/6`.
- YM/gravity remains blocked before physical coefficient extraction by the explicit opposite/pre-sewing full-conic tree with all factorwise uncut denominators retained. `TreeLoopSewing.lean` proves the all-loop graph count but deliberately keeps the analytic shadow-pair sewing identity as a local hypothesis.
- Principal-series/Weil work retains the exact positive-real half-density, `Delta=2s`, critical-line unitarity, Gamma/Mehler-Fock/Wiener-Hopf and chamber identities. None supplies the missing global prime-plus-Archimedean Weil positivity theorem.
- Prime-gas curvature remains at the certified strict upper bound `R(beta,eta) < 1/2` for `eta>0`; no sign theorem was found.

## Next formal targets

1. Certify/repair `abs_frequencyDerivativeKernel_le_exp_tail`.
2. Package `G_{c,T}` as an `Integrable` majorant and use it for differentiation under the integral.
3. Formalize the odd-mode cosh product by the finite even/odd decomposition plus the already-certified sinh Weierstrass product.
4. Use that product to close the odd partial-fraction/tanh identity and then
   \[
   \int_0^\infty \frac{\sin(tx)}{\sinh(\pi x)}\,dx=\frac12\tanh(t/2).
   \]
