# The two positive Archimedean constructions are the K0 and K1 polarizations of one SU(1,1) module

Date: 2026-09-27
Status: exact operator identities. Global arithmetic positivity remains open.

## 1. Universal paired module

Use the lowest-weight \(k=1/2\) SU(1,1) module
\[
\mathcal K=\ell^2(\mathbb N_0)
\]
with
\[
K_0e_n=\left(n+\frac12\right)e_n
\]
and
\[
K_1e_n=
\frac{n+1}{2}e_{n+1}
+\frac n2e_{n-1}.
\]

The compact generator \(K_0\) has the discrete half-integer spectrum.
The noncompact generator \(K_1\) is self-adjoint with vacuum spectral density
\[
d\mu_0(x)=\operatorname{sech}(\pi x)\,dx.
\]

## 2. Gamma--Plancherel defect is a K0 resolvent trace

The exact positive real-place defect in the RH manuscript is
\[
\mathfrak D_q(a,b)
=
\int_0^\infty
\frac{e^{-qx}}{1-e^{-2x}}
(1-e^{-ax})(1-e^{-bx})\,dx.
\]

But
\[
\frac{e^{-qx}}{1-e^{-2x}}
=
e^{-(q-1)x}
\operatorname{Tr}(e^{-2xK_0}),
\]
because
\[
\operatorname{Tr}(e^{-2xK_0})
=
\sum_{n\ge0}e^{-(2n+1)x}
=
\frac1{2\sinh x}.
\]

Therefore
\[
\boxed{
\mathfrak D_q(a,b)
=
\int_0^\infty
e^{-(q-1)x}
\operatorname{Tr}(e^{-2xK_0})
(1-e^{-ax})(1-e^{-bx})\,dx.
}
\]

Define
\[
R_c=(2K_0+c-1)^{-1}.
\]

Although the individual resolvents are not trace class, the second finite difference is trace class, and
\[
\boxed{
\mathfrak D_q(a,b)
=
\operatorname{Tr}
\left[
R_q-R_{q+a}-R_{q+b}+R_{q+a+b}
\right].
}
\]

Thus the positive digamma/Gamma defect is literally a compact-generator resolvent trace of the universal paired module.

## 3. Explicit Hilbert-space Gram dilation

Define on
\[
L^2(\mathbb R_+,dx)\otimes\mathcal K
\]
the feature vector
\[
\boxed{
\Psi_q(a;x)
=
e^{-(q-1)x/2}
e^{-xK_0}
(1-e^{-ax})\,\mathbf 1_{\mathcal K},
}
\]
understood componentwise in the \(K_0\) eigenbasis.

Equivalently,
\[
\Psi_q(a;x,n)
=
e^{-(q-1)x/2}
e^{-x(n+1/2)}
(1-e^{-ax}).
\]

Then
\[
\boxed{
\mathfrak D_q(a,b)
=
\langle\Psi_q(a),\Psi_q(b)\rangle.
}
\]

So the Gamma--Plancherel positivity is ordinary Hilbert positivity on the same paired module used by the prime TFD.

## 4. Celestial Plancherel regularizer is the K1 tensor-square spectral law

The same module has
\[
\langle e_0,e^{-itK_1}e_0\rangle
=
\operatorname{sech}(t/2).
\]

Hence
\[
d\mu_{K_1,e_0}(x)
=
\operatorname{sech}(\pi x)\,dx.
\]

For
\[
J_\infty
=
K_1\otimes I+I\otimes K_1
\]
on the product vacuum,
\[
\langle e_0\otimes e_0,
e^{-itJ_\infty}
e_0\otimes e_0\rangle
=
\operatorname{sech}^2(t/2).
\]

Therefore
\[
\boxed{
d\mu_{J_\infty}(x)
=
\frac{2x}{\sinh(\pi x)}\,dx
=
\frac2\pi P(x)\,dx.
}
\]

So the normalized celestial Plancherel density is the vacuum spectral measure of the tensor-square noncompact generator.

## 5. One representation, two real-place positivity mechanisms

We can now identify the two positive Archimedean constructions already present in the RH program:

\[
\boxed{
\text{Gamma/digamma positive defect}
\longleftrightarrow
K_0\text{ compact-generator resolvent geometry},
}
\]

\[
\boxed{
\text{Plancherel trace-class regularizer}
\longleftrightarrow
K_1\text{ noncompact-generator spectral geometry}.
}
\]

These are not two unrelated analytic tricks. They are two polarizations of the same \(k=1/2\) SU(1,1) representation.

## 6. The real-place identity becomes representation-theoretic

The manuscript identity
\[
\mathfrak D_q(a,b)
=
\int_0^\infty
e^{-(q-1)x}
\frac{P(x/\pi)}{2x}
(1-e^{-ax})(1-e^{-bx})\,dx
\]
now has the exact reading
\[
\boxed{
\frac{P(x/\pi)}{2x}
=
\operatorname{Tr}(e^{-2xK_0}).
}
\]

Thus the principal-series Plancherel function, when evaluated on the logarithmic edge variable \(x/\pi\) and divided by the modular energy \(2x\), is precisely the \(K_0\) heat character.

Meanwhile its Fourier-convolution realization is the \(K_1\) spectral law.

So one and the same scalar \(P\) simultaneously encodes the compact and noncompact spectral resolutions of the paired module.

## 7. Sharpened sewing problem

The global RH construction should now preserve this noncommuting pair rather than use only one scalar kernel.

A natural parent object is the SU(1,1) module equipped with both
\[
K_0,\qquad K_1,
\]
with finite primes inserted through \(K_0\)-thermal/coherent data and the Archimedean completion read through the \(K_1\) spectral transform.

The unresolved theorem is whether the rational/Poisson adelic sewing selects a physical subspace on which the resulting Krein reflection becomes positive.

No local scalar multiplier can do this; the existing ultraviolet and Hardy-space no-go theorems already exclude that. The new point is that there is now an explicit noncommutative parent representation in which such a global projection can be sought.
