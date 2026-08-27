# Raised-box simplex dominated-convergence majorant

For the Euclidean massless four-point box, write the second Symanzik polynomial on the Feynman simplex as

\[
Q(x)=A x_1x_3+B x_2x_4,
\qquad A=-s>0,\quad B=-t>0.
\]

The raised box in \(D=8-2\epsilon\) has the Feynman-parameter factor

\[
J(\epsilon)=\int_{\Delta_3} Q(x)^{-\epsilon}\,d\sigma(x).
\]

The needed residue theorem is \(J(\epsilon)\to\operatorname{Vol}(\Delta_3)=1/6\) as \(\epsilon\to0^+\). A single channel monomial gives a uniform integrable majorant; no sector decomposition is required.

Fix \(0<\delta<1\) and \(0\le\epsilon\le\delta\). For \(q>0\),

\[
q^{-\epsilon}\le 1+q^{-\delta}.
\]

Since \(Q(x)\ge A x_1x_3\) on the simplex and \(-\delta<0\),

\[
Q(x)^{-\delta}
\le A^{-\delta}x_1^{-\delta}x_3^{-\delta}.
\]

Hence almost everywhere on the simplex,

\[
0\le Q(x)^{-\epsilon}
\le 1+A^{-\delta}x_1^{-\delta}x_3^{-\delta}.
\]

The majorant is integrable for every \(\delta<1\). The Dirichlet integral is explicit:

\[
\int_{\Delta_3}x_1^{-\delta}x_3^{-\delta}\,d\sigma
=
\frac{\Gamma(1-\delta)^2}{\Gamma(4-2\delta)},
\]

under the convention in which \(\operatorname{Vol}(\Delta_3)=1/6=1/\Gamma(4)\). Thus dominated convergence yields

\[
J(\epsilon)\longrightarrow \frac16.
\]

Combined with the Verify2 theorem \(\epsilon\Gamma(\epsilon)\to1\) and the existing dimension-shift algebra,

\[
\epsilon I_4^{(8-2\epsilon)}\to\frac16,
\qquad
-\epsilon(1-\epsilon)I_4^{(8-2\epsilon)}\to-\frac16.
\]

## Formalization target

1. Define the standard 3-simplex measure/model used by Mathlib.
2. Prove the pointwise `rpow` bound for `0 <= eps <= delta < 1`.
3. Establish integrability of `x1^(-delta) * x3^(-delta)` on the simplex, preferably from a Dirichlet/Beta integral already in Mathlib; otherwise derive by iterated Beta integrals.
4. Apply dominated convergence to obtain the simplex moment limit.
5. Connect the actual raised-box Feynman-parameter representation to `RaisedBoxResidueAssembly.lean`.

This is a genuine analytic closure route, not a numerical argument.