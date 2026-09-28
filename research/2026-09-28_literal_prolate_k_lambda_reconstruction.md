# Literal prolate k_lambda reconstruction in the finite Weil basis

Date: 2026-09-28
Status: exact finite construction plus zero-free numerical test harness. No RH claim.

This note implements the specific educated guess from Connes--Consani--Moscovici rather than the naive truncated Riemann Phi control.

## 1. Source construction

For cutoff
\[
c=\lambda^2,
\]
use the prolate wave operator
\[
PW_\lambda
=
-\partial_x\bigl((\lambda^2-x^2)\partial_x\bigr)
+
(2\pi\lambda x)^2.
\]

Set
\[
z=x/\lambda,
\qquad
\gamma=2\pi\lambda^2.
\]
Up to an additive scalar in the eigenvalue, the eigenfunction problem is
\[
\boxed{
\left[
-\partial_z((1-z^2)\partial_z)
+\gamma^2 z^2
\right]\psi
=
\Lambda\psi.
}
\]

This form is ideal for a Legendre-Galerkin solver.

## 2. Exact even Legendre matrix

Let
\[
\phi_\ell(z)
=
\sqrt{\frac{2\ell+1}{2}}P_\ell(z)
\]
be the orthonormal Legendre basis.

Multiplication by z obeys
\[
z\phi_\ell
=
a_\ell\phi_{\ell+1}
+
b_\ell\phi_{\ell-1},
\]
where
\[
a_\ell
=
\frac{\ell+1}{\sqrt{(2\ell+1)(2\ell+3)}},
\qquad
b_\ell
=
\frac{\ell}{\sqrt{(2\ell-1)(2\ell+1)}}.
\]

Therefore on one parity sector,
\[
\langle\phi_\ell,z^2\phi_\ell\rangle
=
a_\ell^2+b_\ell^2
\]
and
\[
\boxed{
\langle\phi_{\ell+2},z^2\phi_\ell\rangle
=
a_\ell a_{\ell+1}.
}
\]

So the prolate operator is a real symmetric tridiagonal matrix in the even basis
\[
\ell=0,2,4,\ldots.
\]

The first and third even eigenvectors are the modes labelled n=0 and n=4.

## 3. The zero-integral combination has an especially simple exact form

Let \(v^{(0)}\) and \(v^{(4)}\) be the normalized coefficient vectors of those two even modes.

All Legendre polynomials \(P_\ell\), \(\ell>0\), integrate to zero on \([-1,1]\). Hence the integral of an even prolate mode is determined solely by its \(\ell=0\) coefficient.

Therefore the required CCM combination with vanishing integral is simply
\[
\boxed{
v_\lambda
=
v^{(4)}_0\,v^{(0)}
-
v^{(0)}_0\,v^{(4)}.
}
\]

Its \(\ell=0\) coefficient vanishes identically:
\[
(v_\lambda)_0
=
v^{(4)}_0v^{(0)}_0
-v^{(0)}_0v^{(4)}_0
=0.
\]

Thus the defining condition
\[
\int h_\lambda(x)\,dx=0
\]
is enforced algebraically, not by quadrature or fitting.

## 4. Critical arithmetic transfer

For \(u\in[\lambda^{-1},\lambda]\), define
\[
\boxed{
k_\lambda(u)
=
\mathcal E(h_\lambda)(u)
=
u^{1/2}
\sum_{n\ge1}h_\lambda(nu).
}
\]

With the time-limited prolate profile on \([-\lambda,\lambda]\), the sum is finite:
\[
n\le\lambda/u.
\]

At the lower endpoint \(u=\lambda^{-1}\), this has at most
\[
\lambda^2=c
\]
terms.

So the literal CCM educated guess is computationally cheap once the two prolate modes are known.

## 5. Independent inversion/evenness diagnostic

In centered logarithmic coordinate
\[
y=\log u,
\qquad
|y|\le\log\lambda,
\]
the physical finite Weil ground state is even.

The test harness therefore records the odd leakage
\[
\boxed{
\eta_{\rm odd}
=
\frac{\|k_\lambda(e^y)-k_\lambda(e^{-y})\|_2^2}
{\|k_\lambda(e^y)+k_\lambda(e^{-y})\|_2^2+
 \|k_\lambda(e^y)-k_\lambda(e^{-y})\|_2^2}.
}
\]

Local prototype values for \(c=3,5,7,11,17\) were already tiny and rapidly decreasing, consistent with the near-Fourier-invariance of the low prolate modes. This is a control, not a proof of any asymptotic statement.

## 6. What is measured against the actual finite Weil operator

The script discovery/rh/prolate_k_lambda_gap_scan.py builds the same finite \(Q(c)\) as the existing connes-cvs calculation, projects the even part of \(k_\lambda\) into the same Fourier basis, and computes:

- overlap with the true even ground vector;
- Rayleigh excess
  \[
  \epsilon
  =
  \langle k_\lambda,Qk_\lambda\rangle-\lambda_1;
  \]
- first even excitation gap
  \[
  \Delta=\lambda_2-\lambda_1;
  \]
- the decisive ratio
  \[
  \boxed{\epsilon/\Delta};
  \]
- residual-to-second-level distance;
- inversion/odd leakage.

No Riemann-zero ordinates are used anywhere.

## 7. Why this test is decisive

The previous direct truncated-Phi control achieved very high L2 overlap but catastrophically bad \(\epsilon/\Delta\) as the cutoff increased. That showed that overlap alone is not the correct closure diagnostic.

The literal CCM prolate state is specifically designed to reduce the boundary/time-frequency leakage responsible for that failure.

Therefore:

- if its \(\epsilon/\Delta\) also deteriorates, the present vacuum-gap closure route needs a different trial state or different quotient;
- if \(\epsilon/\Delta\) instead stabilizes or decreases rapidly, then the missing CCM approximation theorem has been converted into a quantitatively plausible mass-gap estimate.

The scan is zero-independent and therefore an honest discriminator.
