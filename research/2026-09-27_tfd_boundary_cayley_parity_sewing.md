# TFD boundary Cayley transform, parity determinants, and the actual Schur operation

Date: 2026-09-27. Authoring process: Codex discovery continuation.
Status: exact finite-dimensional identities and explicitly delimited analytic consequences. RH remains open. No external mathematical sources used.

## 1. Keep the spectral parameter in the covariance

For the positive interval equation \(-f''+q^2 f=0\), length \(\ell>0\), \(q>0\), the Dirichlet-to-Neumann matrix is
\[
\Lambda_\ell(q)=q
\begin{pmatrix}
\coth(q\ell)&-\operatorname{csch}(q\ell)\\
-\operatorname{csch}(q\ell)&\coth(q\ell)
\end{pmatrix}.
\]
Write \(Q_\ell(q)=\Lambda_\ell(q)/q\) and
\[
\Gamma_\ell(q)=\tfrac12\Lambda_\ell(q)^{-1}.
\]
At \(q=1,\ \ell_p=\tfrac12\log p\), this is exactly the existing prime TFD covariance. Its continuation with \(q\) is a boundary resolvent; keeping the prefactor \(1/q\) matters for the spectral positivity question.

Let \(S=\begin{pmatrix}0&1\\1&0\end{pmatrix}\) and \(x=e^{-q\ell}\). Direct diagonalization gives
\[
Q_\ell(q)=(I-xS)(I+xS)^{-1},
\qquad
\boxed{(I-Q_\ell)(I+Q_\ell)^{-1}=xS.}
\]
Thus the Cayley transform of the normalized TFD precision is the attenuated sheet-exchange transfer itself.

**Proof.** On the symmetric and antisymmetric endpoint vectors, \(Q_\ell\) has eigenvalues \(\tanh(q\ell/2)\) and \(\coth(q\ell/2)\). Their Cayley images under \((1-y)/(1+y)\) are \(x\) and \(-x\). QED.

This differs from the scalar Cayley coordinate of a covariance eigenvalue. Both come from the same matrix, but their arguments and signs must be stated.

## 2. The full double and one parity channel have different determinants

Set \(s=q/2\) and \(\ell=\ell_p\), so \(x=p^{-s}\). For a finite prime set \(\mathcal P\),
\[
T_{\mathcal P}(s)=\bigoplus_{p\in\mathcal P}p^{-s}S.
\]
Let \(T_+\) and \(T_-\) be its restrictions to symmetric and antisymmetric endpoint parity. Then
\[
\det(I-T_+)=\prod_{p\in\mathcal P}(1-p^{-s}),
\qquad
\det(I-T_-)=\prod_{p\in\mathcal P}(1+p^{-s}),
\]
but
\[
\boxed{\det(I-T_{\mathcal P})=\prod_{p\in\mathcal P}(1-p^{-2s}).}
\]
Consequently, for \(\Re s>1\),
\[
\det(I-T_+)^{-1}=\zeta(s),\quad
\det(I-T_-)^{-1}=\frac{\zeta(2s)}{\zeta(s)},\quad
\det(I-T)^{-1}=\zeta(2s).
\]
The last paired product has its own absolute-convergence domain \(\Re s>1/2\). The ordinary Fredholm determinant of \(I-T\) requires \(T\) trace class, hence \(\Re s>1\); below that, “paired product” is the appropriate terminology.

The cancellation is also visible in the trace:
\[
\operatorname{Tr}T^m=
\begin{cases}0&m\text{ odd},\\2\sum_p p^{-ms}&m\text{ even}.\end{cases}
\]
An unprojected trace over both sheets discards every odd traversal. It therefore discards precisely the anomalous sector that must be retained to reconstruct the full Euler current.

This is an observable/sector distinction, not an assertion that doubling is invalid. A global construction must specify whether it takes a full trace, a parity projection, a supertrace, a conditional covariance, or a cross matrix element.

## 3. Covariance parity recovers the current exactly

In the same parity basis,
\[
\Gamma_{\ell,+}(q)=\frac1{2q}\coth\frac{q\ell}{2},
\qquad
\Gamma_{\ell,-}(q)=\frac1{2q}\tanh\frac{q\ell}{2}.
\]
Hence
\[
q\Gamma_{\ell,+}(q)-\tfrac12=\frac{x}{1-x},
\qquad
q\Gamma_{\ell,-}(q)-\tfrac12=-\frac{x}{1+x}.
\]
Therefore
\[
-\frac{\zeta'}{\zeta}(s)
=\sum_p(\log p)\left[2s\,\Gamma_{\ell_p,+}(2s)-\tfrac12\right],
\qquad \Re s>1.
\]
The full trace instead gives the normal sector:
\[
q\operatorname{Tr}\Gamma_\ell(q)-1
=\frac{2x^2}{1-x^2}=2C(x),
\]
while the parity difference gives the anomalous sector:
\[
\frac q2(\Gamma_{\ell,+}-\Gamma_{\ell,-})
=\frac{x}{1-x^2}=A(x).
\]
These identities recover the local odd/even interpretation with its exact normalization.

In the RH shifted target, \(s=\tfrac12+r,\ r=\sqrt{1+u}\), so the edge parameter is \(q=1+2r\). It is not simply \(r\).

## 4. A genuine positive Schur complement is available, but is a different observable

Eliminating one endpoint from \(\Gamma_\ell(q)\) gives
\[
\boxed{\Gamma_{00}-\Gamma_{01}\Gamma_{11}^{-1}\Gamma_{10}
=\frac{\tanh(q\ell)}{2q}.}
\]
As a function of \(v=q^2>0\), this has the positive spectral expansion
\[
\boxed{\frac{\tanh(\ell\sqrt v)}{2\sqrt v}
=\frac1\ell\sum_{n=0}^{\infty}
\frac1{v+((n+\tfrac12)\pi/\ell)^2}.}
\]
**Proof.** The inverse of the interval Laplacian with Neumann boundary at zero and Dirichlet boundary at \(\ell\) has value \(\tanh(q\ell)/q\) at the Neumann endpoint. Its normalized eigenfunctions have endpoint square \(2/\ell\), and eigenvalues \(((n+1/2)\pi/\ell)^2\). Multiplication by \(1/2\) gives the formula. Equivalently, solve the Green equation and expand in that orthonormal cosine basis. QED.

Thus the local Gaussian conditioning operation really is Stieltjes. At \(q=1\) it is half the reduced purity, \((p-1)/(2(p+1))\). It is not the vacuum-subtracted symmetric response producing \(\zeta'/\zeta\). Positivity of the first cannot be silently assigned to the second.

## 5. The whole even sector can be separated before the unresolved odd completion

In the Euler half-plane,
\[
\log\zeta(s)=\tfrac12\log\zeta(2s)+\sum_p\operatorname{arctanh}(p^{-s}).
\]
Put
\[
H_{\mathrm{odd}}(s)=
\sum_p\left[\operatorname{arctanh}(p^{-s})-p^{-s}\right].
\]
Using the power series definition, \(H_{\mathrm{odd}}\) converges normally for \(\Re s>1/3\): on a compact subset the summands are \(O(p^{-3\Re s})\). Therefore
\[
\boxed{\log\zeta(s)=P(s)+\tfrac12\log\zeta(2s)+H_{\mathrm{odd}}(s)}
\]
initially for \(\Re s>1\).

For \(\Re s>1/2\), the even factor \(\zeta(2s)\) is already an absolutely convergent, zero-free Euler product, and \(e^{H_{\mathrm{odd}}(s)}\) is analytic and zero-free. This isolates the unresolved arithmetic continuation in the primitive factor, together with the already specified Archimedean/pole completion.

Do not interpret this as a proof that \(P(s)\) extends holomorphically to \(\Re s>1/2\). In fact, such a holomorphic continuation agreeing with its defining sum would force \(\zeta(s)\) to have no zeros there (and cannot include the pole at \(s=1\) without its logarithmic singularity). On zero-free simply connected regions avoiding \(s=1\), the identity determines compatible logarithms; it does not remove a bad zero.

The distinction is useful: the two determinant counterterms are not two independent unknown global functions. The full even channel is already determined by the ordinary Euler theory at \(2s\).

## 6. Verification and next construction

The companion script independently checks the Cayley matrices, endpoint Schur complement, and positive mixed-boundary spectral sum. The maximum Cayley residual in the recorded double-precision controls is below \(5\times10^{-16}\); spectral tails have the elementary bound \(\ell/[\pi^2(N-1/2)]\).

The remaining construction must retain the symmetric arithmetic observable, couple it to the exact renormalized real place, and justify a global quotient/limit. Simply conditioning a local TFD sheet is not that construction.
