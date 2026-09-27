# Explicit Archimedean Jacobi operator from the same SU(1,1) module as the prime TFD

Date: 2026-09-27
Status: exact self-adjoint operator construction and spectral measure; proposed adelic sewing use remains open.

## 1. One Hilbert space, two generators

Let
\[
\mathcal K=\ell^2(\mathbb N_0)
\]
with basis \(e_n\leftrightarrow|n,n\rangle\).

On the paired two-oscillator representation,
\[
K_0e_n=\left(n+\frac12\right)e_n,
\]
while
\[
K_1=\frac12(K_++K_-)
\]
acts as
\[
\boxed{
K_1e_n=
\frac{n+1}{2}e_{n+1}
+
\frac n2e_{n-1},
\qquad e_{-1}=0.
}
\]

Thus \(K_1\) is an explicit Jacobi operator with off-diagonal coefficients
\[
a_n=\frac{n+1}{2}.
\]

## 2. Self-adjointness

On the finite-support core,
\[
\sum_{n\ge0}\frac1{a_n}
=
2\sum_{n\ge0}\frac1{n+1}
=
\infty.
\]

Therefore the Jacobi operator satisfies the Carleman criterion and has a unique self-adjoint closure.

## 3. Vacuum spectral measure

Let \(e_0\) be the paired vacuum.

The exact vacuum survival amplitude is
\[
\langle e_0,e^{-itK_1}e_0\rangle
=
\operatorname{sech}(t/2).
\]

Since
\[
\int_{\mathbb R}
e^{-itx}\operatorname{sech}(\pi x)\,dx
=
\operatorname{sech}(t/2),
\]
the spectral measure of \(K_1\) at \(e_0\) is
\[
\boxed{
d\mu_{1/2}(x)
=
\operatorname{sech}(\pi x)\,dx.
}
\]

## 4. Explicit discrete-to-continuous spectral transform

Let \(P_n(x)\) be the orthonormal polynomial system determined by
\[
P_0(x)=1
\]
and
\[
\boxed{
xP_n(x)
=
\frac{n+1}{2}P_{n+1}(x)
+
\frac n2P_{n-1}(x).
}
\]

Then the spectral transform
\[
U:\ell^2(\mathbb N_0)
\longrightarrow
L^2(\mathbb R,\operatorname{sech}(\pi x)\,dx)
\]
defined by
\[
Ue_n=P_n
\]
is unitary and satisfies
\[
\boxed{
UK_1U^{-1}=M_x.
}
\]

This is an explicit unitary transform from the discrete paired-occupation basis to a continuous real spectral coordinate.

No identification with a zeta-zero spectrum is made.

## 5. The prime side uses K0 on the same Hilbert space

For prime \(p\),
\[
L_p=\log p.
\]

The universal \(k=1/2\) heat character is
\[
\operatorname{Tr}e^{-L_pK_0}
=
\sum_{n\ge0}
p^{-(n+1/2)}
=
\frac{\sqrt p}{p-1}
=
A_p.
\]

Thus
\[
\boxed{
\text{finite prime covariance uses }K_0,
}
\]
while
\[
\boxed{
\text{Archimedean hyperbolic-secant spectrum uses }K_1,
}
\]
on the same universal paired Hilbert module.

The two operators are different noncommuting generators of one \(\mathfrak{su}(1,1)\) algebra.

## 6. Tensor-square Archimedean operator

Take
\[
\mathcal K_\infty
=
\mathcal K\otimes\mathcal K
\]
and define
\[
\boxed{
J_\infty
=
K_1\otimes I
+
I\otimes K_1.
}
\]

For the product vacuum
\[
\Omega_\infty=e_0\otimes e_0,
\]
the characteristic function is
\[
\langle\Omega_\infty,
e^{-itJ_\infty}
\Omega_\infty\rangle
=
\operatorname{sech}^2(t/2).
\]

Hence its vacuum spectral measure is
\[
\boxed{
d\mu_\infty(x)
=
\frac{2x}{\sinh(\pi x)}\,dx
=
\frac2\pi P(x)\,dx.
}
\]

So \(J_\infty\) is an explicit self-adjoint operator whose vacuum spectral measure is exactly the normalized celestial Plancherel density.

## 7. Concrete realization of the RH preconditioner

The RH Plancherel convolution square root uses
\[
a(x)
=
\sqrt{\frac\pi2}\operatorname{sech}(\pi x).
\]

This is the single-copy vacuum spectral density up to normalization.

The full positive convolution kernel
\[
P=a*a
\]
is therefore the tensor-square vacuum spectral convolution of \(K_1\).

## 8. New sewing target

The local arithmetic and Archimedean structures can now be placed on one universal representation diagram:
\[
\boxed{
\begin{array}{ccc}
\ell^2(\mathbb N_0)
&\xrightarrow{\quad U\quad}&
L^2(\mathbb R,\operatorname{sech}(\pi x)dx)
\\[4pt]
K_0\ \text{discrete}
&&
K_1\ \text{continuous}
\end{array}
}
\]

with:
- primes entering as discrete evolution lengths \(L_p=\log p\) for \(K_0\);
- the real-place regularizer arising from the continuous spectral resolution of \(K_1\);
- the doubled celestial weight arising from \(K_1\otimes1+1\otimes K_1\).

This is an explicit candidate for a single local Hilbert module whose two generator polarizations reproduce both the finite-place TFD covariance and the Archimedean Plancherel metric.

The remaining global problem is to insert the arithmetic translation/prime-power comb and rational functional-equation sewing into this transform and prove that the resulting Schur complement is the positive RH Weyl function. That step is still open.
