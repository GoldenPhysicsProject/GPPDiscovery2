# Continuous Gamma chamber as an explicit random heat-time subordinator

Codex/GPT discovery track, 2026-09-04.

## Exact input

The focused arithmetic principal-series program uses Euler's product

\[
\operatorname{sech}^2(\xi/2)
=\prod_{k=0}^\infty
\left(1+\frac{\xi^2}{\pi^2(2k+1)^2}\right)^{-2}
\]

and realizes it as the Laplace transform of a positive random heat time built from independent gamma variables of shape two.

The same product immediately extends the construction to every real chamber parameter `c>0`.

## Continuous random heat time

Put

\[
\lambda_k=\pi^2(2k+1)^2
\]

and let `S_{c,k}` be independent gamma random variables with shape `2c` and rate `lambda_k`. Define

\[
S_c=\sum_{k\ge0}S_{c,k}.
\]

Since

\[
\sum_{k\ge0}\lambda_k^{-1}=\frac18,
\]

we have

\[
\boxed{\mathbb E S_c=\frac c4<\infty},
\]

so the nonnegative series is finite almost surely. Also

\[
\sum_{k\ge0}\lambda_k^{-2}=\frac1{96},
\]

hence

\[
\boxed{\operatorname{Var}(S_c)=\frac c{48}}.
\]

For `q>=0`, independence and the gamma Laplace transform give

\[
\begin{aligned}
\mathbb E e^{-qS_c}
&=\prod_{k=0}^\infty
\left(1+\frac q{\lambda_k}\right)^{-2c}\\
&=\boxed{\operatorname{sech}^{2c}(\sqrt q/2)}.
\end{aligned}
\]

Equivalently,

\[
\boxed{\mathbb E e^{-S_c\xi^2}=\operatorname{sech}^{2c}(\xi/2)}.
\]

## Exact additive semigroup

For independent copies `S_c` and `S_d`, each same-rate gamma component adds its shape:

\[
\Gamma(2c,\lambda_k)+\Gamma(2d,\lambda_k)
\stackrel d=\Gamma(2(c+d),\lambda_k).
\]

Therefore

\[
\boxed{S_c+S_d\stackrel d=S_{c+d}}.
\]

Thus the continuous chamber parameter is literally additive random heat time, not merely an exponent in a Fourier multiplier.

## Heat-time Levy measure

The Laplace exponent is

\[
\Phi_c(q)
=-\log\mathbb E e^{-qS_c}
=2c\log\cosh(\sqrt q/2).
\]

Using

\[
\log(1+q/\lambda)
=\int_0^\infty(1-e^{-qt})e^{-\lambda t}\,\frac{dt}{t},
\]

we obtain the explicit positive Levy measure

\[
\boxed{
\Pi_c(dt)
=\frac{2c}{t}\sum_{k=0}^\infty
 e^{-\pi^2(2k+1)^2t}\,dt
}
\]

with

\[
\Phi_c(q)=\int_0^\infty(1-e^{-qt})\Pi_c(dt).
\]

This is the heat-time counterpart of the previously isolated symmetric spectral-position Levy generator for the Gamma chamber.

## Consequence for the Gamma spectral density

Once the Codex/GPT Fourier theorem

\[
\widehat\rho_c(\xi)=\operatorname{sech}^{2c}(\xi/2),
\qquad
\rho_c(x)=\frac{2^{2c-1}}{\pi\Gamma(2c)}|\Gamma(c+ix)|^2
\]

is Lean-promoted under the same Fourier convention as the heat kernel

\[
g_t(x)=(4\pi t)^{-1/2}e^{-x^2/(4t)},
\qquad \widehat g_t(\xi)=e^{-t\xi^2},
\]

Fourier uniqueness gives the positive mixture identity

\[
\boxed{\rho_c(x)=\mathbb E\,g_{S_c}(x)}.
\]

Then `rho_c * rho_d = rho_(c+d)` is simultaneously the Fourier semigroup law and the probabilistic heat-time addition law.

## Boundary

This is a positive Archimedean/spectral theorem. It does not establish positivity of the completed prime-minus-Archimedean Weil form and does not imply RH. In particular, positive heat preconditioning is faithful but non-coercive with respect to the missing arithmetic sign problem.

## Formalization route

1. Formalize the Euler-product/Laplace identity for `sech^(2c)` or derive it from the Beta/logistic Fourier theorem plus a positive mixing theorem.
2. Package finite partial sums of same-rate gamma variables and pass to the monotone nonnegative limit.
3. Prove the first two heat-time cumulants `E S_c=c/4`, `Var S_c=c/48`.
4. Prove the additive law in distribution through Laplace-transform uniqueness.
5. Combine with the Gamma/Beta Fourier theorem to obtain `rho_c = E g_(S_c)` and convolution closure.
