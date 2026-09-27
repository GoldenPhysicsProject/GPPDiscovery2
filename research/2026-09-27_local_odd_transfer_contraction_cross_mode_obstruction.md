# Exact local odd-transfer contraction and the cross-mode obstruction

Date: 2026-09-27
Status: exact SU(1,1)/TFD Hilbert-space identities. They explain the local contraction but also show why it does not imply the global BPY/RH contraction.

## 1. Reflection of the paired coherent state

Let
\[
|\Omega_r\rangle
=
\sqrt{1-r^2}
\sum_{n\ge0}r^n e_n,
\qquad |r|<1.
\]

Let \(J\) be occupation-parity,
\[
Je_n=(-1)^n e_n.
\]

Then
\[
\boxed{J|\Omega_r\rangle=|\Omega_{-r}\rangle.}
\]

Set
\[
P_\pm=\frac12(I\pm J).
\]

The reflected overlap is
\[
\langle\Omega_r,\Omega_{-r}\rangle
=
(1-r^2)\sum_{n\ge0}(-r^2)^n
=
\boxed{\frac{1-r^2}{1+r^2}}.
\]

For the critical prime state \(r=p^{-1/2}\), this is
\[
\boxed{
\langle\Omega_p,J\Omega_p\rangle
=
\frac{p-1}{p+1}
=
\operatorname{Tr}\rho_p^2.
}
\]

Thus the reduced-state purity is exactly the reflection expectation of the doubled coherent state.

## 2. Exact local contraction ratio

Because \(P_\pm\) are orthogonal projections,
\[
\|P_+\Omega_r\|^2
=
\frac12\left(
1+\frac{1-r^2}{1+r^2}
\right)
=
\frac1{1+r^2},
\]
while
\[
\|P_-\Omega_r\|^2
=
\frac12\left(
1-\frac{1-r^2}{1+r^2}
\right)
=
\frac{r^2}{1+r^2}.
\]

Hence
\[
\boxed{
\frac{\|P_-\Omega_r\|}
{\|P_+\Omega_r\|}
=
|r|.
}
\]

For a prime,
\[
\boxed{
\frac{\|P_-\Omega_p\|}
{\|P_+\Omega_p\|}
=
p^{-1/2}<1.
}
\]

So every individual prime TFD coherent mode satisfies a strict odd/even contraction, with contraction constant exactly equal to its half-density amplitude.

This is the local analogue of the BPY odd-transfer inequality.

## 3. Archimedean spectral picture

Under the exact Jacobi transform,
\[
U\Omega_r(x)
=
\sqrt{\cos2\alpha}\,e^{2\alpha x},
\qquad
r=\tan\alpha.
\]

Reflection is
\[
\alpha\mapsto-\alpha.
\]

Therefore
\[
UP_+\Omega_r
=
\sqrt{\cos2\alpha}\cosh(2\alpha x),
\]
and
\[
UP_-\Omega_r
=
\sqrt{\cos2\alpha}\sinh(2\alpha x).
\]

With
\[
d\mu_0(x)=\operatorname{sech}(\pi x)\,dx,
\]
the exact norm ratio is
\[
\boxed{
\frac{
\|\sinh(2\alpha x)\|_{L^2(\mu_0)}
}{
\|\cosh(2\alpha x)\|_{L^2(\mu_0)}
}
=
\tan|\alpha|
=
|r|.
}
\]

So the TFD contraction becomes a hyperbolic even/odd contraction of exponential tilts on the Archimedean spectral line.

## 4. Why single-mode contraction is not enough

Take two parameters
\[
r=\tan\alpha,\qquad s=\tan\beta.
\]

The coherent-state overlap is
\[
\langle\Omega_r,\Omega_s\rangle
=
\frac{
\sqrt{\cos2\alpha\,\cos2\beta}
}{
\cos(\alpha+\beta)
}.
\]

The reflection/Krein kernel is
\[
\boxed{
K_J(\alpha,\beta)
=
\langle\Omega_r,J\Omega_s\rangle
=
\frac{
\sqrt{\cos2\alpha\,\cos2\beta}
}{
\cos(\alpha-\beta)
}.
}
\]

For two distinct parameters \(\alpha\ne\beta\), its \(2\times2\) determinant is
\[
\begin{aligned}
\det
\begin{pmatrix}
K_J(\alpha,\alpha)&K_J(\alpha,\beta)\\
K_J(\beta,\alpha)&K_J(\beta,\beta)
\end{pmatrix}
&=
\cos2\alpha\,\cos2\beta
\left[
1-\sec^2(\alpha-\beta)
\right]\\
&=
\boxed{
-\cos2\alpha\,\cos2\beta
\tan^2(\alpha-\beta)<0
}
\end{aligned}
\]
whenever \(|\alpha|,|\beta|<\pi/4\) and \(\alpha\ne\beta\).

Thus the reflection form is already indefinite on the span of two distinct coherent tilts.

## 5. Meaning for the RH program

We now have both sides of the local/global distinction explicitly:

\[
\boxed{
\text{one coherent mode}
\Longrightarrow
\|P_-\|/\|P_+\|=|r|<1,
}
\]

but

\[
\boxed{
\text{two distinct coherent modes}
\Longrightarrow
\text{the raw reflection Gram form is indefinite}.
}
\]

Therefore the RH problem cannot be solved merely by observing that every prime/TFD channel is locally contractive. The Archimedean/rational sewing must alter the **cross-mode geometry**.

This is exactly consistent with the existing BPY statement
\[
\mathrm{RH}
\Longleftrightarrow
\|C_\omega\|\le1
\]
on the full polarized exponential subspace: the obstruction is in interference between different exponential tilts, not in any individual mode.

## 6. Sharpened target

The missing global map should be sought as a positive metric/frame operator \(G\) on the exponential-tilt family such that the conjugated reflection kernel
\[
G^{1/2}JG^{1/2}
\]
is nonnegative on the physical adelic/BPY subspace, while preserving the exact completed zeta Weyl function.

The local contraction constants \(p^{-1/2}\) are already correct. What remains is an arithmetic orthogonalization of the cross-prime/cross-tilt terms.
