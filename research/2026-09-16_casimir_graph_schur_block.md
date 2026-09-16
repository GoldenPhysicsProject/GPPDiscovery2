# Casimir graph and exact Euler Schur block — 2026-09-16

Status: exact zero-independent derivations on the safe Euler ray. No RH proof claimed.

## 1. Half-density sawtooth field

Let

\[
w(t)=(1-\{e^t\})e^{-t/2},\qquad t\ge0,
\]

and extend by zero to the negative half-line when a full-line Fourier/Casimir calculation is required. Put

\[
Q=D+\frac12,\qquad Q^*=-D+\frac12,\qquad H_C=Q^*Q=-D^2+\frac14.
\]

On every interval \(\log n<t<\log(n+1)\),

\[
w(t)=(n+1)e^{-t/2}-e^{t/2},
\]

so \(H_Cw=0\) there. All Casimir curvature is concentrated at the logarithms of the integers.

Distributionally,

\[
Qw=\sum_{n\ge2}n^{-1/2}\delta_{\log n}-e^{t/2}
\]

on the open half-line, and after zero extension to the full line the boundary jump at \(t=0\) supplies the \(n=1\) atom.

Applying \(Q^*\), the continuum mode disappears because \(Q^*e^{t/2}=0\), giving

\[
H_Cw=\sum_{n\ge2}\frac1{\sqrt n}\left(\frac12\delta_{\log n}-\delta'_{\log n}\right)
\]

in the open half-line distribution sense.

## 2. Canonical negative Casimir graph energy

The Casimir negative norm is

\[
\|S\|_{-1,C}^2:=\langle S,H_C^{-1}S\rangle.
\]

For \(S=Qw\), Fourier multiplication gives the exact isometry

\[
\|Qf\|_{-1,C}^2=\|f\|_2^2,
\]

because

\[
\frac{|i\xi+1/2|^2}{\xi^2+1/4}=1.
\]

Thus the compensated comb source has finite canonical energy

\[
\langle Qw,H_C^{-1}Qw\rangle=\|w\|_2^2.
\]

No independent comb self-energy or continuum counterterm is introduced: the difference is taken before the inverse Casimir operator is applied.

The norm is elementary. For integer \(N\ge2\),

\[
\int_1^N\frac{(1-\{x\})^2}{x^2}\,dx
=2N-2+H_{N-1}-2N\log N+2\log((N-1)!).
\]

Stirling therefore yields

\[
\boxed{\|w\|_2^2=\log(2\pi)+\gamma-2.}
\]

## 3. Exact Mellin/Fourier transform

For \(s=1/2+i\xi\),

\[
\widehat w(\xi)
=\int_1^\infty (1-\{x\})x^{-s-1}\,dx.
\]

Euler summation gives, for \(\Re s>0\),

\[
\boxed{
\widehat w(\xi)
=\frac{\zeta(s)}{s}-\frac1{s(s-1)}
=\frac{(s-1)\zeta(s)-1}{s(s-1)}.
}
\]

Hence the compensated source has centered Mellin symbol

\[
\boxed{
\widehat{Qw}(\xi)
=s\widehat w(\xi)
=\zeta(s)-\frac1{s-1}.
}
\]

This is to be interpreted as the Fourier transform of the combined compensated source; the comb and continuum pieces should not be transformed separately.

Consequently the graph norm also gives the exact critical-line identity

\[
\frac1{2\pi}\int_{\mathbb R}
\frac{\left|\zeta(\frac12+i\xi)-\frac1{-1/2+i\xi}\right|^2}
{\xi^2+1/4}\,d\xi
=\log(2\pi)+\gamma-2,
\]

with the stated Fourier normalization.

## 4. Euler factor as a Casimir boundary response

Set

\[
u=s(s-1),\qquad \kappa=s-\frac12=\sqrt{u+1/4},\qquad k_u(t)=e^{-\kappa t}.
\]

Then

\[
J(u)=\int_0^\infty w(t)k_u(t)\,dt
\]

and Euler summation becomes

\[
\boxed{F_1(u):=(s-1)\zeta(s)=1+uJ(u).}
\]

Because \(H_Ck_u=-u k_u\), pairing the arithmetic curvature with \(k_u\) gives

\[
\boxed{\langle H_Cw,k_u\rangle=-(s-1)(\zeta(s)-1).}
\]

Equivalently,

\[
(s-1)\zeta(s)=(s-1)-\langle H_Cw,k_u\rangle.
\]

Thus the safe Euler factor is a boundary response of the same massive Casimir operator whose negative graph norm controls the compensated arithmetic source.

## 5. Positive bilinear Casimir graph

For \(u,v>0\), let

\[
R_u=(H_C+u)^{-1}.
\]

Then

\[
\boxed{
\mathcal G_C(u,v)
:=\langle Qw,R_uR_vQw\rangle
=\langle w,H_CR_uR_vw\rangle.
}
\]

This is a positive-semidefinite kernel. It is the Loewner divided-difference kernel of

\[
\boxed{\psi(u)=u\langle w,R_uw\rangle,}
\]

because for the scalar spectral variable \(\lambda\),

\[
\frac{u/(\lambda+u)-v/(\lambda+v)}{u-v}
=\frac{\lambda}{(\lambda+u)(\lambda+v)}.
\]

Therefore \(\psi\) is a zero-independent positive operator-monotone function generated canonically by the compensated integer source. The unresolved question is the exact remainder

\[
\phi_C^{[1]}-\psi^{[1]}.
\]

It must be computed rather than assumed positive.

## 6. Exact non-self-adjoint Schur block for the Euler factor

Let \(H_D=-D^2+1/4\) be the Dirichlet half-line Casimir operator, and let \(\eta=-\delta_0'\) denote the boundary-normal source. Its resolvent produces the decaying defect vector

\[
R_u\eta(t)=e^{-\sqrt{u+1/4}\,t}=k_u(t).
\]

Hence

\[
F_1(u)=1+u\langle w,R_u\eta\rangle.
\]

Define the block pencil

\[
\boxed{
\mathbb B(u)=
\begin{pmatrix}
H_D+u & \sqrt u\,\eta\\
-\sqrt u\,\langle w,\cdot\rangle & 1
\end{pmatrix}.
}
\]

Its scalar lower-right Schur complement is exactly

\[
1+u\langle w,R_u\eta\rangle=F_1(u).
\]

Thus the safe arithmetic factor already has an exact bulk-boundary colligation. The obstruction is explicit: the two off-diagonal channels are \(\eta\) and \(w\), so the block is not self-adjoint in the ordinary Hilbert metric.

A closure theorem must construct a zero-independent positive graph metric, compatible with the co-Poisson/shadow completion, in which these channels become adjoints after the gauge/zero-mode quotient. If that is achieved for the completed prime-Archimedean block, the Schur complement becomes passive and its logarithmic Casimir response is a candidate for the required Loewner-positive \(\phi_C\).

## 7. Immediate next target

Compute the completed block obtained by adjoining the pole-free Archimedean factor

\[
\pi^{-s/2}\Gamma(1+s/2),
\qquad
\xi(s)=\pi^{-s/2}\Gamma(1+s/2)F_1(s),
\]

and determine the exact quadratic-form remainder between the resulting logarithmic Casimir Loewner kernel and the positive graph kernel \(\mathcal G_C\). No positivity claim is made until that remainder is represented explicitly.