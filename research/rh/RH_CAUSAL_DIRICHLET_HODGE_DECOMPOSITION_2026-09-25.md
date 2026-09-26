# Exact causal Dirichlet/Hodge decomposition of the non-pole CCM form
Date: 2026-09-25
Status: exact operator identity plus numerical verification. No RH claim.

## 1. Archimedean block as a renormalized causal-shift integral

On H_L=L^2(0,L), let V_y be the unilateral right shift and Q_y=V_y+V_y^*.
The CCM Fourier matrix elements of Q_y are exactly the box kernel.

Write

\[
\rho(y)=\frac{e^{y/2}}{e^y-e^{-y}},
\qquad
C_L=\log(4\pi)+\gamma-
\log\frac{e^L+1}{e^L-1}.
\]

The Archimedean CCM block has the exact operator form

\[
\boxed{
W_R
=
C_L I+
\int_0^L
\rho(y)\bigl(Q_y-2e^{-y/2}I\bigr)\,dy.
}
\]

The subtraction is exactly the diagonal renormalization in the original formula:
\(2e^{-y/2}\rho(y)=2/(e^y-e^{-y})\).
The integrand is finite at y=0 because the 1/y singularities cancel.

Direct numerical reconstruction agrees with the original CCM matrix to machine precision
(max error about 9e-16 in the lambda=3,N=4 audit).

## 2. Every causal shift carries a positive Dirichlet defect

Define

\[
D_y:=2I-(V_y+V_y^*).
\]

Algebraically,

\[
\boxed{
D_y=(I-V_y)^*(I-V_y)+(I-V_y^*V_y).
}
\]

For the unilateral shift, \(V_y^*V_y\) is the projection onto \([0,L-y]\), so

\[
\boxed{
\langle f,D_yf\rangle
=
\|f-V_yf\|^2+
\int_{L-y}^{L}|f(x)|^2\,dx
\ge0.
}
\]

Thus D_y is a genuine jump-Dirichlet energy plus boundary killing.

The generic matrix identity is now in
GPPVerify/ThreadWeilParity/CausalDirichletDefect.lean
on the clean RH branch.

## 3. Exact Hodge form for A=-W_R-W_P

With \(c_n=\Lambda(n)n^{-1/2}\) and the prime block
\(W_P=\sum c_nQ_{\log n}\), one gets

\[
\boxed{
A=-W_R-W_P
=
\mathcal L_L-\kappa_L I,
}
\]

where the positive nonlocal Dirichlet operator is

\[
\boxed{
\mathcal L_L
=
\int_0^L\rho(y)D_y\,dy
+
\sum_{2\le n<e^L}
\frac{\Lambda(n)}{\sqrt n}D_{\log n}
\succeq0,
}
\]

and

\[
\boxed{
\kappa_L
=
C_L+
2\int_0^L\rho(y)(1-e^{-y/2})\,dy
+
2\sum_{2\le n<e^L}\frac{\Lambda(n)}{\sqrt n}.
}
\]

The scalar integral has the closed form, with lambda=e^{L/2},

\[
2\int_0^L\rho(y)(1-e^{-y/2})dy
=
\left[
2\log(1+t)-\log(1+t^2)+2\arctan t
\right]_{t=1/\lambda}^{1}.
\]

So Claude's Hodge-index analogy is not merely qualitative:
the non-pole CCM form is *exactly* a positive Dirichlet generator minus one scalar level.

Therefore

\[
n_-(A)=1
\]

is equivalent to the sharp spectral statement

\[
\boxed{
\lambda_1(\mathcal L_L)<\kappa_L\le\lambda_2(\mathcal L_L).
}
\]

This is a concrete one-dimensional nonlocal Poincare/Hodge-index theorem.

## 4. Numerical spectral check

At lambda=3,N=4 the reconstruction gives

\[
\kappa_L\approx11.1105407584,
\]

and the first eigenvalues of \(\mathcal L_L\) are approximately

\[
6.29147719,quad
11.11054076,quad
11.11054099,\ldots
\]

while the eigenvalues of A begin

\[
-4.81906357,quad
5.0\times10^{-9},quad
2.3\times10^{-7},\ldots.
\]

Thus the observed one-negative-square phenomenon is literally the statement that exactly
one Dirichlet eigenvalue lies below the arithmetic level \(\kappa_L\), while the Phi tower
sits extremely close above that level.

## 5. Why this matters

The missing "arithmetic Hodge index theorem" can now be attacked as a spectral-gap theorem
for an explicit positive jump process, rather than as an abstract indefinite matrix theorem.

The generator has:
- a continuous Archimedean jump measure \(\rho(y)dy\);
- positive prime-power jumps \(\Lambda(n)n^{-1/2}\delta_{\log n}\);
- exact unilateral boundary killing.

The remaining theorem is a sharp Poincare inequality on the primitive subspace.  This is
still RH-strength, but it is a much more concrete object on which comparison,
Cheeger/Birman-Schwinger, oscillation, and Feshbach methods can be tried.

No RH claim is made.
