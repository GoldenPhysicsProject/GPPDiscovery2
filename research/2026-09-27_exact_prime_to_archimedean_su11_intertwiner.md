# Exact prime-to-Archimedean intertwiner: TFD coherent states become exponential tilts of the hyperbolic-secant spectrum

Date: 2026-09-27
Status: exact local unitary-transform identities. Global adelic sewing and RH positivity remain open.

## 1. Start from the explicit Jacobi transform

On
\[
\mathcal K=\ell^2(\mathbb N_0)
\]
let
\[
K_1e_n
=
\frac{n+1}{2}e_{n+1}
+
\frac n2e_{n-1}.
\]

Its vacuum spectral measure is
\[
d\mu_0(x)
=
\operatorname{sech}(\pi x)\,dx.
\]

Let \(P_n(x)=Ue_n\) be the orthonormal polynomial basis in
\[
L^2(\mathbb R,d\mu_0)
\]
which diagonalizes \(K_1\).

The recurrence is
\[
xP_n(x)
=
\frac{n+1}{2}P_{n+1}(x)
+
\frac n2P_{n-1}(x),
\qquad
P_0=1.
\]

## 2. Exact generating function of the spectral polynomials

Define
\[
G(z,x)=\sum_{n\ge0}P_n(x)z^n.
\]

Multiplying the Jacobi recurrence by \(z^n\) and summing gives
\[
2xG
=
(1+z^2)\partial_zG+zG.
\]

Therefore
\[
\frac{\partial_zG}{G}
=
\frac{2x-z}{1+z^2}.
\]

With \(G(0,x)=1\),
\[
\boxed{
G(z,x)
=
\frac{
\exp\!\bigl(2x\arctan z\bigr)
}{
\sqrt{1+z^2}
}.
}
\]

This derives the discrete-to-continuous transform kernel without importing any external special-function formula.

## 3. Transform of a TFD coherent state

For \(0<r<1\), the normalized paired coherent state is
\[
|\Omega_r\rangle
=
\sqrt{1-r^2}
\sum_{n\ge0}r^ne_n.
\]

Applying \(U\),
\[
\begin{aligned}
(U\Omega_r)(x)
&=
\sqrt{1-r^2}
\sum_{n\ge0}r^nP_n(x)\\
&=
\sqrt{\frac{1-r^2}{1+r^2}}
\exp\!\left(2x\arctan r\right).
\end{aligned}
\]

Set
\[
\alpha=\arctan r.
\]

Since
\[
\cos(2\alpha)
=
\frac{1-r^2}{1+r^2},
\]
we obtain the compact form
\[
\boxed{
(U\Omega_r)(x)
=
\sqrt{\cos(2\alpha)}
\,e^{2\alpha x}.
}
\]

Thus an interior SU(1,1) TFD coherent state becomes a normalized exponential tilt of the Archimedean hyperbolic-secant vacuum measure.

## 4. Prime version

For prime \(p\),
\[
r_p=p^{-1/2},
\qquad
\alpha_p=\arctan(p^{-1/2}).
\]

Hence
\[
\boxed{
(U\Omega_p)(x)
=
\sqrt{\frac{p-1}{p+1}}
\exp\!\left(
2x\arctan\frac1{\sqrt p}
\right).
}
\]

But
\[
\frac{p-1}{p+1}
=
\operatorname{Tr}\rho_p^2.
\]

Therefore
\[
\boxed{
(U\Omega_p)(x)
=
\sqrt{\operatorname{Tr}\rho_p^2}
\,e^{2\alpha_px}.
}
\]

The normalization of the Archimedean exponential tilt is exactly the square root of the reduced prime-state purity.

## 5. Exact normalization from the vacuum moment-generating function

The vacuum spectral law satisfies
\[
\int_{\mathbb R}
e^{tx}\operatorname{sech}(\pi x)\,dx
=
\sec(t/2),
\qquad |t|<\pi.
\]

At \(t=4\alpha\),
\[
\int
e^{4\alpha x}\,d\mu_0(x)
=
\sec(2\alpha).
\]

Therefore
\[
\cos(2\alpha)
\int
e^{4\alpha x}\,d\mu_0(x)
=
1,
\]
which proves the normalization of \(U\Omega_r\) directly.

## 6. The prime state is an exponential family on the real-place spectral line

The probability density of \(K_1\) in the state \(\Omega_r\) is
\[
\boxed{
d\mu_r(x)
=
\cos(2\alpha)
\,e^{4\alpha x}
\operatorname{sech}(\pi x)\,dx.
}
\]

Thus the prime TFD states form an exact one-parameter exponential family over the Archimedean vacuum spectral measure.

Natural parameter:
\[
\eta=4\alpha.
\]

Log partition function:
\[
\boxed{
\mathcal A(\eta)
=
\log\sec(\eta/2).
}
\]

This supplies an explicit local finite-to-real statistical intertwiner.

## 7. Moments recover the TFD covariance

For the exponential family,
\[
\langle K_1\rangle_r
=
\mathcal A'(\eta)
=
\frac12\tan(\eta/2)
=
\frac12\tan(2\alpha).
\]

Since \(r=\tan\alpha\),
\[
\frac12\tan(2\alpha)
=
\frac{r}{1-r^2}
=
A(r).
\]

Therefore
\[
\boxed{
\langle K_1\rangle_r
=
A(r),
}
\]
the anomalous TFD covariance.

The variance is
\[
\operatorname{Var}_r(K_1)
=
\mathcal A''(\eta)
=
\frac14\sec^2(2\alpha).
\]

But
\[
C(r)+\frac12
=
\frac{1+r^2}{2(1-r^2)}
=
\frac12\sec(2\alpha),
\]
so
\[
\boxed{
\operatorname{Var}_r(K_1)
=
\left(C(r)+\frac12\right)^2.
}
\]

Consequently the pure-state covariance identity becomes
\[
\boxed{
\operatorname{Var}_r(K_1)
-
\langle K_1\rangle_r^2
=
\frac14.
}
\]

Thus the mean and variance of the **Archimedean continuous generator \(K_1\)** in the transformed prime state reproduce the complete local TFD covariance data.

## 8. Antipodal/sheet-reversed states become opposite tilts

Replacing \(r\) by \(-r\) sends
\[
\alpha\mapsto-\alpha.
\]

Therefore
\[
\boxed{
U\Omega_{\pm r}
=
\sqrt{\cos2\alpha}\,
e^{\pm2\alpha x}.
}
\]

The symmetric and antisymmetric combinations become
\[
\boxed{
U(\Omega_r+\Omega_{-r})
\propto
\cosh(2\alpha x),
}
\]
\[
\boxed{
U(\Omega_r-\Omega_{-r})
\propto
\sinh(2\alpha x).
}
\]

So the sheet/orientation \(\mathbb Z_2\) decomposition becomes the even/odd exponential decomposition on the real spectral line.

This directly resembles the even--odd polarized exponential subspaces already isolated in the BPY reflection problem.

## 9. Exact overlap in both polarizations

In the occupation basis,
\[
\langle\Omega_r,\Omega_s\rangle
=
\frac{\sqrt{(1-r^2)(1-s^2)}}{1-rs}.
\]

In the \(K_1\) spectral representation,
\[
\langle\Omega_r,\Omega_s\rangle
=
\sqrt{\cos2\alpha\,\cos2\beta}
\int e^{2(\alpha+\beta)x}\,d\mu_0(x).
\]

Using the secant moment formula,
\[
\boxed{
\langle\Omega_r,\Omega_s\rangle
=
\frac{
\sqrt{\cos2\alpha\,\cos2\beta}
}{
\cos(\alpha+\beta)
}.
}
\]

The two expressions are identical under
\[
r=\tan\alpha,\qquad s=\tan\beta.
\]

This is a nontrivial check of the intertwiner.

## 10. Why this advances the global target

Previously:
- finite prime TFD states lived in a discrete occupation basis;
- the Archimedean Plancherel metric lived on a continuous real spectral line;
- the required finite-to-real sewing map was unspecified.

Now there is an explicit unitary map \(U\) on the universal paired module such that

\[
\boxed{
\text{prime TFD coherent state}
\quad\xrightarrow{U}\quad
\text{normalized exponential tilt of }
\operatorname{sech}(\pi x)\,dx.
}
\]

Moreover:
- sheet reversal becomes \(\alpha\to-\alpha\);
- symmetric/antisymmetric sectors become \(\cosh/\sinh\) tilts;
- the transformed first two moments reproduce the TFD covariance exactly.

This does not prove the global prime--Archimedean Gram inequality. It does provide a concrete candidate transform in which that inequality can now be attacked: translate the entire prime boundary subspace through \(U\) and compare it directly with the BPY polarized exponential subspace and the Archimedean Schur completion.
