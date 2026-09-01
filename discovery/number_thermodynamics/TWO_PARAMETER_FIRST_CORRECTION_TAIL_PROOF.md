# Two-parameter number-Gibbs determinant: rigorous first-correction tail

Codex/GPT track. This closes the analytic tail gap behind the previously identified `(1,2,4)` first exponential correction.

Let

\[
x_n=\log n,\qquad
w_n(\beta,\eta)=n^{-\beta}e^{-\eta x_n^2},\qquad
Z=\sum_{n\ge1}w_n,
\]

and, for `i<j<k`,

\[
V_{ijk}=\prod_{a<b\in\{i,j,k\}}(x_b-x_a),\qquad
Q_{ijk}=x_i^2+x_j^2+x_k^2,
\]

\[
A_{ijk}=(ijk)^{-\beta}V_{ijk}^2.
\]

The countable Cauchy-Binet expansion, once its moment-limit bridge is installed, is

\[
\det g(\beta,\eta)=Z^{-3}\sum_{i<j<k}A_{ijk}e^{-\eta Q_{ijk}}.
\]

The leading and first excited triples are

\[
(1,2,3),\qquad (1,2,4),
\]

because `log(n)^2` is strictly increasing for `n>=1`. Their costs are

\[
Q_0=(\log2)^2+(\log3)^2,
\qquad
Q_1=(\log2)^2+(\log4)^2,
\]

so

\[
\Delta=Q_1-Q_0=(\log4)^2-(\log3)^2>0.
\]

## Uniform remainder gap without identifying the third triple

Remove `(1,2,3)` and `(1,2,4)`. Every remaining ordered triple `i<j<k` is in one of two cases.

1. `i=1,j=2,k>=5`, hence
   \[
   Q_{ijk}\ge Q_{125}=(\log2)^2+(\log5)^2.
   \]
2. `j>=3`. Then `i>=1,j>=3,k>=4`, hence
   \[
   Q_{ijk}\ge Q_{134}=(\log3)^2+(\log4)^2.
   \]

Define

\[
Q_*=\min\{Q_{125},Q_{134}\}.
\]

Both candidates lie strictly above `Q_1`:

\[
Q_{125}-Q_1=(\log5)^2-(\log4)^2>0,
\]

\[
Q_{134}-Q_1=(\log3)^2-(\log2)^2>0.
\]

Therefore

\[
Q_*>Q_1>Q_0.
\]

This avoids any delicate comparison between `Q_125` and `Q_134`; it is enough that the entire remainder has a gap strictly larger than the first-excitation gap.

## Countable tail domination

Fix any `eta0>0`. For `eta>=eta0`, every remainder term satisfies

\[
A_{ijk}e^{-\eta Q_{ijk}}
=e^{-(\eta-\eta_0)Q_{ijk}}A_{ijk}e^{-\eta_0Q_{ijk}}
\le e^{-(\eta-\eta_0)Q_*}A_{ijk}e^{-\eta_0Q_{ijk}}.
\]

Hence

\[
R_\eta
\le e^{-(\eta-\eta_0)Q_*}C_{\beta,\eta_0},
\]

where

\[
C_{\beta,\eta_0}
=\sum_{(i,j,k)\ne(1,2,3),(1,2,4)}
A_{ijk}e^{-\eta_0Q_{ijk}}<\infty.
\]

The finiteness is elementary. The squared Vandermonde is bounded by a fixed polynomial in `log i,log j,log k`; for every real `beta` and `eta0>0`,

\[
n^{-\beta}(1+\log n)^m e^{-\eta_0(\log n)^2}
\]

is summable for each fixed `m`, because the negative quadratic in `log n` eventually dominates both the linear `|beta| log n` term and any logarithmic polynomial. The triple majorant then factorizes into a product of three convergent one-dimensional sums.

Consequently

\[
R_\eta=O(e^{-\eta Q_*}).
\]

Relative to the leading `(1,2,3)` term,

\[
\frac{R_\eta}{A_{123}e^{-\eta Q_0}}
=O(e^{-\eta(Q_*-Q_0)})
=o(e^{-\eta\Delta}),
\]

because `Q_*-Q_0>Q_1-Q_0=Delta`.

The common normalization `Z^{-3}` cancels exactly in the ratio to the leading Vandermonde contribution. Therefore the previously conjectured asymptotic is now analytically justified, conditional only on the already-targeted countable Cauchy-Binet/moment identity:

\[
\boxed{
\frac{\det g}{L_{123}}
=1+C_\beta e^{-\eta\Delta}+o(e^{-\eta\Delta})
}
\]

with

\[
L_{123}=Z^{-3}A_{123}e^{-\eta Q_0},
\]

\[
\boxed{
C_\beta=\left(\frac43\right)^{-\beta}
\frac{4(\log2)^4}{(\log3)^2[\log(3/2)]^2}
}.
\]

No numerical ordering of the third and fourth triples is needed for the proof.

## Formalization boundary

The remaining Lean work is now cleanly separated:

1. specialize the two-parameter number-Gibbs weights and prove their log-moment summability for `eta>0` (all real `beta`), and for `eta=0,beta>1`;
2. connect the existing finite/countable Fisher moment machinery to the exact countable Vandermonde expansion or an equivalent remainder estimate;
3. formalize the elementary cost-gap split above;
4. formalize the fixed-`eta0` dominated tail bound.

The previous vague blocker “uniform countable tail estimate” is therefore no longer an analytic mystery; the proof mechanism is explicit.