# AFT box pole channel and boundary-contact correction

Date: 2026-08-28

## Exact scalar decomposition

For the zero Fourier mode of the semilocal Weil matrix,

\[
q_{00}(y)=2\left(1-\frac yL\right),\qquad 0\le y\le L.
\]

The pole contribution is therefore explicitly

\[
\frac L2 W_{0,2}^\sharp(F_{00})
=
L\int_0^L\left(1-\frac yL\right)
\bigl(e^{y/2}+e^{-y/2}\bigr)\,dy.
\]

Direct integration gives

\[
\boxed{
P(L)=8\bigl(\cosh(L/2)-1\bigr)
=16\sinh^2(L/4).
}
\]

Thus the raw pole channel is already one exact positive square,

\[
P(L)=\bigl(4\sinh(L/4)\bigr)^2.
\]

Since

\[
\Psi(L)
=\frac L2(Q_{L,0})_{00}
= P(L)-R_\infty(L)-R_{\rm p}(L),
\]

one might try to prove RH by representing the completed real-plus-prime subtraction as the norm square of a contraction against this pole amplitude.

## This naive defect model fails at the causal endpoint

It cannot be the correct global factorization.

For \(0<L<\log2\), no prime term is present.  From

\[
w_\infty(a)=-\frac1{2a}+\frac74+O(a)
\]

and

\[
\Psi(L)
=A_\infty(1)L
+\int_0^Lw_\infty(a)
\bigl[(L-a)-Le^{-a}\bigr]\,da,
\]

rescaling \(a=Lx\) gives

\[
\int_0^Lw_\infty(a)
\bigl[(L-a)-Le^{-a}\bigr]\,da
=\frac L2+O(L^2).
\]

Hence

\[
\boxed{
\Psi(L)=\left(A_\infty(1)+\frac12\right)L+O(L^2),
}
\]

where

\[
A_\infty(1)
=\frac83-\frac12(\log\pi+\gamma)
+\frac\pi4-\frac32\log2.
\]

By contrast,

\[
P(L)=L^2+O(L^4).
\]

Therefore \(\Psi(L)>P(L)\) for sufficiently small positive \(L\).  So there is no representation of the form

\[
\Psi(L)=P(L)-\|G_L\|^2
\]

with a positive ghost norm for all \(L\).

This rules out the simplest choice of the pole sector as the entire positive ambient channel.

## Physical interpretation

The missing leading term is linear in the slab length.  A linear norm-square is exactly what a local boundary/contact state produces because

\[
\|\mathbf1_{[0,L]}\|_{L^2}^2=L.
\]

Thus the renormalized real-place subtraction is not merely a negative correction to the pole square.  It changes the ultraviolet boundary metric and supplies a contact channel at order \(L\).

A realistic AFT factorization should therefore have at least two positive ambient pieces:

\[
\mathcal H_{\rm amb}
=\mathcal H_{\rm contact}\oplus\mathcal H_{\rm pole}\oplus\cdots,
\]

with the contact piece carrying the endpoint linear term and the pole piece carrying
\(16\sinh^2(L/4)\).

The prime sector must then enter through a nonlocal quotient/Schur/Hodge coupling, not as a standalone positive norm simply subtracted from the pole channel.

## Connection to the existing Green/Krein construction

The old principal-series program already gives the prime term as a polarized difference of positive massive resolvent energies:

\[
\langle\delta_0,R_u\eta_{\mathcal C}\rangle
=\frac14\left(
\|R_u^{1/2}(\delta_0+\eta_{\mathcal C})\|^2
-\|R_u^{1/2}(\delta_0-\eta_{\mathcal C})\|^2
\right).
\]

The full shifted response is

\[
m_*(u)=\mathfrak a_\infty(u)
+\frac14\|R_u^{1/2}(\delta_0-\eta_p)\|^2
-\frac14\|R_u^{1/2}(\delta_0+\eta_p)\|^2.
\]

This is the correct starting point: the prime sector is intrinsically a polarization/cross term, while the Archimedean impedance must supply the positive completion of that Krein difference.

## Revised target

Do not seek

\[
\text{pole norm} - \text{prime norm}.
\]

Seek instead a completed boundary metric in which the Archimedean contact/pole channels and the polarized prime resolvent are assembled first, and only then quotient the odd/ghost sector.  The interval-state positivity target remains

\[
\Psi(L)=\|J_L\mathbf1_{[0,L]}\|^2,
\]

but \(J_L\) must include the real-place contact renormalization.

No RH proof is claimed.
