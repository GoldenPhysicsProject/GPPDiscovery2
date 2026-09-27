# Prime TFD states as massive-edge boundary covariances

Date: 2026-09-26  
Status: exact local theorem package plus a global RH construction target. No external literature search used.

## Universal massive edge

Let
\[
H_\ell=-\frac{d^2}{dx^2}+1
\]
on \([0,\ell]\), \(\ell>0\). Solving \(H_\ell u=0\) with boundary values \(u(0)=a,\ u(\ell)=b\) gives the Dirichlet-to-Neumann matrix
\[
\boxed{
\Lambda(\ell)=
\begin{pmatrix}
\coth\ell&-\operatorname{csch}\ell\\
-\operatorname{csch}\ell&\coth\ell
\end{pmatrix}.
}
\]
Since \(\det\Lambda(\ell)=1\),
\[
\Lambda(\ell)^{-1}=
\begin{pmatrix}
\coth\ell&\operatorname{csch}\ell\\
\operatorname{csch}\ell&\coth\ell
\end{pmatrix}.
\]
Define
\[
\boxed{\Gamma(\ell)=\frac12\Lambda(\ell)^{-1}.}
\]

## Exact prime TFD identification

For a prime \(p\), set
\[
\ell_p=\frac12\log p,\qquad r_p=e^{-\ell_p}=p^{-1/2}.
\]
The critical prime TFD has
\[
C_p=\frac{r_p^2}{1-r_p^2}=\frac1{p-1},
\qquad
A_p=\frac{r_p}{1-r_p^2}=\sqrt{C_p(1+C_p)}.
\]
Using
\[
\frac12\coth\ell=\frac12+\frac{e^{-2\ell}}{1-e^{-2\ell}},
\qquad
\frac12\operatorname{csch}\ell=\frac{e^{-\ell}}{1-e^{-2\ell}},
\]
we obtain
\[
\boxed{
\Gamma(\ell_p)=
\begin{pmatrix}
C_p+\frac12&A_p\\
A_p&C_p+\frac12
\end{pmatrix}.
}
\]

Thus the local arithmetic TFD covariance is literally one half of the Neumann-to-Dirichlet map of a unit-mass one-dimensional edge of length \(\ell_p=\frac12\log p\).

## Mass, Cayley coordinate, and purity

The finite-place mass coordinate is
\[
\mu_p^2=4C_p=\frac4{e^{2\ell_p}-1}.
\]
The covariance determinant is
\[
\det\Gamma(\ell_p)=\frac14.
\]
Its eigenvalues are
\[
\lambda_-(p)=\frac12\tanh\frac{\ell_p}{2}
=\frac12\frac{\sqrt p-1}{\sqrt p+1},
\]
\[
\lambda_+(p)=\frac12\coth\frac{\ell_p}{2}
=\frac12\frac{\sqrt p+1}{\sqrt p-1}.
\]
Hence the finite-place Cayley coordinate is exactly
\[
\boxed{
q_p=\frac{\sqrt p-1}{\sqrt p+1}=2\lambda_-(p).
}
\]

Eliminating one endpoint gives the scalar Schur complement
\[
S_p=C_p+\frac12-\frac{A_p^2}{C_p+1/2}
=\frac12\tanh\ell_p.
\]
But
\[
\tanh\ell_p=\frac{p-1}{p+1}
=\operatorname{Tr}\rho_p^2.
\]
Therefore
\[
\boxed{
S_p=\frac12\operatorname{Tr}\rho_p^2.
}
\]

So integrating out one TFD sheet leaves a positive boundary stiffness equal to one half of the reduced-state purity.

## Prime loops are doubled TFD edges

The primitive arithmetic length is
\[
L_p=\log p=2\ell_p.
\]
Therefore
\[
\boxed{
\zeta_p(s)=\frac1{1-p^{-s}}
=\frac1{1-e^{-2s\ell_p}}.
}
\]
At the critical half-density,
\[
p^{-m/2}=e^{-m\ell_p},
\]
so the von-Mangoldt current amplitude is
\[
\boxed{
(\log p)p^{-m/2}=2\ell_p e^{-m\ell_p}.
}
\]

The same edge therefore supplies the TFD propagation amplitude, the mass/occupation covariance, the Euler primitive length, and the half-density prime-current return amplitude.

Moreover,
\[
A_p=\sum_{k\ge0}e^{-(2k+1)\ell_p},
\qquad
C_p=\sum_{k\ge1}e^{-2k\ell_p}.
\]
Thus anomalous covariance resums odd traversals and normal covariance resums even traversals. The old \(m=1\) and \(m=2\) RH boundary channels are the primitive seeds of these two edge sectors.

## Archimedean place uses the same edge kernel

For the real place let
\[
\ell_\infty=\pi\lambda.
\]
The universal anomalous covariance is
\[
A(\ell_\infty)=\frac1{2\sinh(\pi\lambda)}.
\]
The celestial principal-series weight is
\[
P(\lambda)=\frac{\pi\lambda}{\sinh(\pi\lambda)},
\]
hence
\[
\boxed{
P(\lambda)=2\ell_\infty A(\ell_\infty).
}
\]

The finite modular frequency is
\[
\omega_p=\frac{\log p}{2\pi},
\]
so
\[
\ell_p=\pi\omega_p.
\]
This \(\omega_p\) is a modular-frequency coordinate and must not be confused with the older analytically continued finite-place Casimir coordinate \(i\lambda_p=\sqrt p\).

The completed Archimedean density also satisfies
\[
w_\infty(x)
=
e^{-x/2}+e^{x/2}
-\frac{e^{x/2}}{2\sinh x}.
\]
Since \(A(x)=1/(2\sinh x)\),
\[
\boxed{
w_\infty(x)=e^{-x/2}+e^{x/2}-e^{x/2}A(x).
}
\]
Equivalently,
\[
\boxed{
w_\infty(x)=e^{x/2}-\frac{e^{-5x/2}}{1-e^{-2x}}.
}
\]

So the non-rational thermal subtraction at the real place is literally the anomalous covariance of the same universal massive-edge family, with the standard half-density tilt.

## Global target

Finite places occur at discrete edge lengths
\[
\ell_p=\frac12\log p,
\]
while the Archimedean principal series supplies a continuous edge-length parameter
\[
\ell_\infty=\pi\lambda.
\]

This suggests replacing the abstract two-channel completion problem by a concrete boundary-network problem: construct a self-adjoint metric-graph/canonical-system sewing of the discrete prime edges, the continuum Archimedean edge family, and the already controlled higher-repetition Fock channel, such that the relative Dirichlet-to-Neumann/Schur-complement Weyl function is exactly
\[
m_*(u)
=
\frac{1}{2\sqrt{1+u}}
\frac{\xi'}{\xi}\left(\frac12+\sqrt{1+u}\right).
\]

RH is not proved. The gain is a single explicit local geometry shared by the prime TFD state, finite-place mass operator, Euler loops, von-Mangoldt current, Cayley coordinate, reduced purity, and Archimedean Plancherel weight.
