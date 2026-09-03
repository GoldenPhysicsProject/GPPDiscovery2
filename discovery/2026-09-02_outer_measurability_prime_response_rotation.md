# Outer measurability and active-front rotation

Codex/GPT research record, 2026-09-02. Claude material was not inspected or used.

## 1. Scalar-box regulator closure

CI on GPPVerify2 commit `316e4babc5157ee7d8dbc26e5f18f58bdbd19f3c` is genuinely clean: full Build #1959 and changed-Lean smoke #814 both passed. This certifies the corrected affine reversal and the middle-DCT dependency chain.

The exact remaining analytic obstruction was isolated more sharply. Domination is no longer the issue: the outer kernel

\[
x_1^{-\delta}(1-x_1)^{2-\delta}
\]

is already formally interval-integrable for \(\delta<1\), and the fixed-\(x_1\) middle DCT is formalized. The missing interface is measurability in the outer parameter of the *two-inner-coordinate* integral.

To attack exactly that point, GPPVerify2 now has `RaisedBoxOuterMeasurability.lean` at commit `e50ada72a94c89b7064c71b1403f8843c061e5db`. It groups the full affine simplex as a measurable subset of

\[
\mathbb R\times(\mathbb R\times\mathbb R)
\]

and uses product integration to make the full-simplex fiber integral strongly measurable in \(x_1\). The remaining bridge is to identify that product-fiber representation with the original nested interval integral on \(0\le x_1\le1\). Once that equality is certified, the outer DCT can consume the already-certified middle pointwise limit and outer majorant.

The target remains

\[
\operatorname{simplexMoment}(\varepsilon,S,T)\to\frac16,
\]

which immediately feeds the existing Gamma-residue and \(\mu^4\) dimension-shift assembly.

## 2. Positive-real principal series / completed zeta / Weil

Current verified local structure is stronger than a bare critical-line dictionary. With \(\Delta=2s\), the completed-zeta logarithmic response

\[
R(\Delta)=\frac{\Lambda'(\Delta/2)}{\Lambda(\Delta/2)}
\]

is purely imaginary on \(\Re\Delta=1\) away from zeros; equivalently \(-iR\) is real. It is shadow odd,

\[
R(\Delta)=-R(2-\Delta),
\]

and on the principal axis shadow equals conjugation. This is an exact unitary-response structure but not a Weil-positivity theorem.

The global RH-critical gap remains unchanged: construct a concrete admissible transform class carrying the completed prime-plus-Archimedean explicit-formula quadratic form and prove the required positivity. Finite interpolation, local Gamma/Wiener-Hopf positivity, and the completed-zeta phase response do not supply that global positivity.

## 3. Prime-gas fluctuation geometry

For the quadratically confined number gas

\[
Z(\beta,\eta)=\sum_{n\ge2}e^{-\beta L_n-\eta L_n^2},\qquad L_n=\log n,
\]

once countable differentiation is certified, the response matrix of the sufficient-statistic means is exactly the negative Fisher matrix:

\[
\frac{\partial(\langle L\rangle,\langle L^2\rangle)}
{\partial(\beta,\eta)}
=-\begin{pmatrix}
\operatorname{Var}(L)&\operatorname{Cov}(L,L^2)\\
\operatorname{Cov}(L,L^2)&\operatorname{Var}(L^2)
\end{pmatrix}.
\]

Because strict positivity of this covariance determinant is already formalized independently of differentiability, the missing differentiation theorem will immediately imply that the moment map \((\beta,\eta)\mapsto(\langle L\rangle,\langle L^2\rangle)\) has everywhere nonsingular Jacobian and is locally a diffeomorphism, with negative-definite linear response. This is a useful thermodynamic consequence beyond merely saying `log Z` is strictly convex.

The analytic route remains the compact-set domination

\[
|\partial_\beta^a\partial_\eta^b e^{-\beta L-\eta L^2}|
\le e^{B^2/(2\eta_0)}L^{a+2b}e^{-(\eta_0/2)L^2},
\]

which is eventually bounded by a summable \((\log n)^m/n^p\) tail for any \(p>1\).

## 4. Spectral / Mehler-Fock / Wiener-Hopf chambers

The certified adjacent Gamma-chamber law remains

\[
\rho_{k+1}(x)\gtrless\rho_k(x)
\iff 2x^2\gtrless k+1.
\]

Thus the discovery-level global consequence is exact unimodality: for noninteger \(2x^2\), the unique mode is \(\lfloor2x^2\rfloor\); for positive integer \(2x^2=m\), chambers \(m-1,m\) tie. The separate Mehler-Fock convolution-power family remains exact but must not be identified with the Gamma chamber index without an additional theorem.

## 5. Honest Yang-Mills / gravity frontier

No new dynamical numerator was derived in this rotation. The correct next physics object remains the nonzero-\(\mu\) two-massive-vector tree tensor, projected independently on both internal vector lines, followed by dimensional reconstruction

\[
C^{(4)}=C^{(V_m)}-C^{(S)}.
\]

The existing four-point FDH rational closure is an algebraic assembly conditional on the generalized-unitarity coefficients; the next honest advance is to derive those coefficients from the projected tree currents. The all-loop sewing topology theorem supplies graph combinatorics, not this dynamical identity.

## Main-branch bookkeeping

CODEX.md requests promotion of a tested Codex workbench to `main` when CI is green. A non-force fast-forward attempt from `main` to `316e4babc...` was rejected because `main` has diverged. No force update was attempted: overwriting divergent history would be inappropriate without inspecting/merging it, and this run is explicitly restricted to the Codex track.
