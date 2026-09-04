# Principal-series heat multiplier to integer Gamma-chamber convolution

Codex/GPT discovery track, 2026-09-04.

## Inputs kept separate

The focused arithmetic principal-series program isolates the normalized positive-real multiplier

\[
m(\xi)=\operatorname{sech}^2(\xi/2)
\]

and represents it as a random heat-time multiplier

\[
m(\xi)=\mathbb E\,e^{-S\xi^2}
\]

for a positive random variable `S`.

Independently, the Codex/GPT Gamma-chamber track has isolated the normalized densities

\[
\rho_c(x)=\frac{2^{2c-1}}{\pi\Gamma(2c)}|\Gamma(c+ix)|^2
\]

with Fourier target

\[
\widehat\rho_c(\xi)=\operatorname{sech}^{2c}(\xi/2).
\]

For integer `n>=1`, this gives `widehat rho_n = m^n`.

## Exact integer-depth heat-time bridge

Let `S_1,...,S_n` be independent copies of `S`, and set

\[
T_n=S_1+\cdots+S_n.
\]

Independence gives

\[
\mathbb E e^{-T_n\xi^2}
=\prod_{j=1}^n\mathbb E e^{-S_j\xi^2}
=m(\xi)^n
=\operatorname{sech}^{2n}(\xi/2).
\]

Therefore, once the Gamma-chamber Fourier normalization is promoted, the same multiplier has two exactly compatible semigroup interpretations:

\[
\boxed{\rho_n=\rho_1^{*n}}
\]

in spectral position and

\[
\boxed{T_n=S_1+\cdots+S_n}
\]

in random heat time.

Equivalently, integer chamber depth is simultaneously convolution depth of the Gamma spectral density and additive depth of the corresponding heat-time mixture.

## What this does and does not establish

This is an exact structural consequence of the two stated transform inputs. It does not establish the arbitrary-real-`c` heat-time mixture by itself: extending `T_n` to a continuous convolution parameter requires infinite divisibility of the heat-time law (or an explicit continuous mixing family), which is a separate theorem.

It also does not imply positivity of the completed prime-plus-Archimedean Weil quadratic form and therefore does not prove RH. The arithmetic two-grid/Hausdorff criterion still requires unconditional positivity of the relevant completed sequence/operator.

## Formalization target

1. Promote the arbitrary-`c` Gamma/Beta logistic Fourier transform.
2. Specialize it at positive integers to obtain `rho_n = rho_1^{*n}` by Fourier uniqueness.
3. Package the focused-paper heat representation as a Laplace-transform input and prove the elementary independent-sum identity above.
4. Keep any continuous-`c` heat-mixture extension separate until infinite divisibility of the mixing law is proved.
