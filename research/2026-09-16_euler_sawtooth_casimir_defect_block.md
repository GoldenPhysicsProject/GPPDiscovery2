# Euler sawtooth, Casimir defect, and the coupled boundary block — 2026-09-16

Status: exact identities and structural consequences. No RH proof claimed.

## 1. The safe Euler contraction field

Put

\[
b(t)=1-\{e^t\},\qquad w(t)=b(t)e^{-t/2},\qquad t\in\mathbb R.
\]

For \(t\in(\log n,\log(n+1))\), \(n\ge1\),

\[
b(t)=n+1-e^t,
\qquad
w(t)=(n+1)e^{-t/2}-e^{t/2}.
\]

For \(t<0\), since \(0<e^t<1\),

\[
w(t)=e^{-t/2}-e^{t/2}.
\]

Let

\[
Q=D+\frac12,
\qquad
Q^*=-D+\frac12,
\qquad
H_C=Q^*Q=-D^2+\frac14.
\]

On every open interval between the points \(\log n\), both \(e^{-t/2}\) and \(e^{t/2}\) are zero modes of \(H_C\), hence

\[
H_Cw=0
\]

there.

## 2. Exact first-order distribution identity

At \(t_n=\log n\), \(n\ge1\), the jump of \(w\) is

\[
[w]_{t_n}=n^{-1/2}.
\]

The ordinary part of \(Qw\) is \(-e^{t/2}\), because \(Qe^{-t/2}=0\) and \(Q(-e^{t/2})=-e^{t/2}\). The jumps contribute Dirac masses. Therefore on \(\mathbb R\), distributionally,

\[
\boxed{
Qw=
\sum_{n\ge1}n^{-1/2}\delta_{\log n}-e^{t/2}.
}
\]

The continuum term is an exact adjoint zero mode:

\[
\boxed{Q^*e^{t/2}=0.}
\]

Consequently

\[
\boxed{
H_Cw=Q^*Qw
=
\sum_{n\ge1}n^{-1/2}Q^*\delta_{\log n}.
}
\]

Since

\[
Q^*\delta_a=-\delta'_a+\frac12\delta_a,
\]

this is

\[
\boxed{
H_Cw=
\sum_{n\ge1}\frac1{\sqrt n}
\left(\frac12\delta_{\log n}-\delta'_{\log n}\right).
}
\]

Thus the Euler sawtooth is a piecewise zero-energy Casimir state whose entire curvature is the half-density integer dilation comb. The continuum term in the first-order equation is pure \(Q^*\)-gauge.

## 3. Relation to arithmetic synthesis and shadow adjoint

In logarithmic coordinates the arithmetic synthesis in the principal-series manuscript is

\[
\mathcal P_{\log}=\sum_{n\ge1}n^{-1/2}T_{\log n},
\qquad
(T_ag)(u)=g(u+a).
\]

With this convention the positive-support comb in the first-order identity is the adjoint-orientation synthesis \(\mathcal P_{\log}^*\delta_0\). Hence

\[
\boxed{
Qw=\mathcal P_{\log}^*\delta_0-e^{t/2}.
}
\]

The co-Poisson identity already proves, on its common test domain, that multiplicative inversion implements the adjoint relation for the arithmetic synthesis. Thus the new identity supplies a concrete vector/distribution on which the abstract shadow-adjoint relation acts.

This does not prove the Hardy no-leak theorem. It identifies the exact gauge channel that must be removed or paired by the shadow boundary condition.

## 4. The safe zeta response as a Casimir Poisson transfer

For \(s>1\), put

\[
u=s(s-1),\qquad \kappa=s-\frac12=\sqrt{u+\frac14},\qquad \Omega(t)=e^{-t/2}.
\]

Euler summation gives

\[
(s-1)\zeta(s)=1+uJ(u),
\qquad
J(u)=\int_0^\infty b(t)e^{-st}\,dt.
\]

Let \(H_D=-D^2+1/4\) on \(L^2(0,\infty)\) with Dirichlet boundary. Its Poisson kernel at spectral parameter \(u>0\) is

\[
k_u(t)=e^{-\kappa t}.
\]

Since \(w(t)=b(t)\Omega(t)\),

\[
\boxed{
J(u)=\langle k_u,w\rangle
=\langle Ck_u,C\Omega\rangle,
\qquad
C=M_{\sqrt b},\quad 0\le C\le I.
}
\]

Equivalently, if \(\ell f=f'(0)\) is the inward boundary normal functional,

\[
\ell(H_D+u)^{-1}w=J(u).
\]

Therefore \((s-1)\zeta(s)\) is the scalar Schur complement of the non-self-adjoint boundary block

\[
\mathbb B(u)=
\begin{pmatrix}
H_D+u & w\\
-u\ell & 1
\end{pmatrix},
\]

because

\[
1-(-u\ell)(H_D+u)^{-1}w=1+uJ(u)=(s-1)\zeta(s).
\]

After the usual \(\sqrt u\)-rescaling of the scalar boundary channel, the only failure of ordinary positive-metric self-adjointness is the mismatch between the interior vector \(w=C^2\Omega\) and the boundary normal functional \(\ell\). This is the exact place where a completed shadow/co-Poisson metric would have to identify the two off-diagonal channels as adjoints.

## 5. Pole-free completed factorization

The completion can be written without explicit elementary pole terms:

\[
\boxed{
\xi(s)=
\pi^{-s/2}\Gamma\!\left(1+\frac s2\right)
(s-1)\zeta(s).
}
\]

Hence

\[
\boxed{
\frac{\xi'}{\xi}(s)
=-\frac12\log\pi
+\frac12\psi\!\left(1+\frac s2\right)
+\frac{d}{ds}\log((s-1)\zeta(s)).
}
\]

The shifted Archimedean factor is a positive Gaussian radial moment:

\[
\boxed{
\pi^{-s/2}\Gamma\!\left(1+\frac s2\right)
=\int_0^\infty 2\pi r e^{-\pi r^2}r^s\,dr.
}
\]

The corresponding four-point defect of its logarithmic derivative is positive:

\[
\Delta_q\left[-\frac12\log\pi+\frac12\psi\!\left(1+\frac s2\right)\right](a,b)
=
\int_0^\infty
\frac{e^{-(q+2)x}}{1-e^{-2x}}
(1-e^{-ax})(1-e^{-bx})\,dx\ge0.
\]

This is obtained from the manuscript's Gamma defect together with the recurrence \(\psi(z+1)=\psi(z)+1/z\).

## 6. Why this is not yet RH

The Schur complement above is exact only on the safe Euler side. Its two off-diagonal channels are not ordinary Hilbert adjoints. Constructing a positive, zero-independent completed metric in which the shadow maps the boundary normal channel to the interior arithmetic channel would give a passive coupled block; proving that its logarithmic/Casimir Weyl kernel is exactly \(\phi_C^{[1]}\) would close the missing theorem.

The new content is that the mismatch is no longer abstract:

- bulk operator: \(H_D+u\);
- interior coupling vector: \(w=(1-\{e^t\})e^{-t/2}\);
- boundary coupling: normal trace \(\ell\);
- contraction: \(C=M_{\sqrt{1-\{e^t\}}}\);
- arithmetic curvature: \(H_Cw\), exactly the half-density integer comb;
- gauge channel: \(e^{t/2}\in\ker Q^*\);
- shadow adjoint on arithmetic synthesis: supplied algebraically by co-Poisson.

The next theorem to attack is the exact metric/intertwiner identifying \(w\) and the shadow of \(\ell\) after the Gamma radial channel is included, without inserting any zero data.