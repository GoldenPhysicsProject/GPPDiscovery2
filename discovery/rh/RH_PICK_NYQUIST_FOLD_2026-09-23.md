# RH Pick/Nyquist fold: exact Hermite source for the semilocal Weil matrix

**Discovery note — 2026-09-23**

Status: exact finite algebra plus reproducible numerical verification. This is a discovery-layer result, not an RH proof. Promotion to `GPPVerify` should wait until the identities are formalized.

## 1. Setup

Let

\[
L=2\log\lambda>0,qquad d_n=\frac{2\pi n}{L},qquad n\in\mathbb Z.
\]

The CCM box kernel used in the finite Weil matrix is, for \(0\le y\le L\),

\[
q_{nm}(y)=
\begin{cases}
\displaystyle
\frac{\sin(2\pi m y/L)-\sin(2\pi n y/L)}
     {\pi(n-m)},&n\ne m,\\[8pt]
\displaystyle
2\left(1-\frac yL\right)\cos\frac{2\pi n y}{L},&n=m.
\end{cases}
\]

The off-diagonal formula superficially looks like the divided difference of the
frequency \(y/L\). That is misleading at critical sampling: the correct Hermite
source is the **reflected frequency** \(1-y/L\).

## 2. Exact Nyquist-fold theorem

Put \(\alpha=y/L\) and define

\[
\boxed{
\psi_\alpha(s)=\frac{1}{\pi}
\sin\bigl(2\pi(1-\alpha)s\bigr).
}
\]

Then for every pair of integers \(m,n\),

\[
\boxed{
q_{nm}(y)=
\begin{cases}
\displaystyle
\frac{\psi_\alpha(n)-\psi_\alpha(m)}{n-m},&n\ne m,\\[10pt]
\psi_\alpha'(n),&n=m.
\end{cases}}
\]

### Proof

At an integer \(n\),

\[
\psi_\alpha(n)
=
\frac{\sin(2\pi n-2\pi\alpha n)}{\pi}
=
-\frac{\sin(2\pi\alpha n)}{\pi}.
\]

Hence, for \(n\ne m\),

\[
\frac{\psi_\alpha(n)-\psi_\alpha(m)}{n-m}
=
\frac{\sin(2\pi\alpha m)-\sin(2\pi\alpha n)}
     {\pi(n-m)}
=
q_{nm}(y).
\]

Also

\[
\psi_\alpha'(n)
=
2(1-\alpha)
\cos\bigl(2\pi(1-\alpha)n\bigr)
=
2(1-\alpha)\cos(2\pi\alpha n)
=
q_{nn}(y).
\]

So the diagonal is not an ad hoc completion of the divided-difference matrix.
It is the genuine Hermite derivative of the support-reflected source.

In physical spectral coordinate \(z=2\pi s/L\), define

\[
\boxed{
\phi_{L,y}(z)=\frac{2}{L}\sin((L-y)z).
}
\]

Then the same statement is

\[
q_{nm}(y)
=
\begin{cases}
\displaystyle
\frac{\phi_{L,y}(d_n)-\phi_{L,y}(d_m)}
     {d_n-d_m},&n\ne m,\\[10pt]
\phi_{L,y}'(d_n),&n=m.
\end{cases}
\]

Thus the box kernel is a Loewner/Hermite matrix for the reflected displacement
\(L-y\).

## 3. The Nyquist identity mode

Define

\[
h(s)=\frac{\sin(2\pi s)}{2\pi}.
\]

At all integer nodes,

\[
h(n)=0,qquad h'(n)=1.
\]

Therefore its Hermite-Loewner matrix on the integer grid is exactly the identity:

\[
\boxed{L_h=I.}
\]

In physical coordinate this mode is

\[
h_L(z)=\frac{\sin(Lz)}{L},
\]

with \(h_L(d_n)=0\) and \(h_L'(d_n)=1\).

Consequently, if \(Q\) is any Hermite-Loewner matrix on the CCM grid and
\(\varepsilon\in\mathbb R\), then

\[
\boxed{
Q-\varepsilon I
\quad\text{is obtained by replacing}\quad
b(s)\mapsto b(s)-\varepsilon h(s).
}
\]

The ground-state shift is therefore exactly a **Nyquist-edge Hermite correction**.
It changes no sampled values and shifts every sampled derivative by the same
amount. In Fourier-distribution language it modifies only the endpoint
frequency \(|\theta|=1\) (equivalently physical support endpoint \(|u|=L\)).

## 4. Exact source of the pole term

Put

\[
a=\frac{L}{4\pi},qquad
C_L=\frac{2L\sinh^2(L/4)}{\pi^2},
\]

and define

\[
\boxed{
b_{02}(s)=C_L\frac{s}{s^2+a^2}.
}
\]

Then the pole matrix in the CCM formula,

\[
W_{02}(n,m)=
32L\sinh^2(L/4)
\frac{L^2-16\pi^2mn}
{(L^2+16\pi^2m^2)(L^2+16\pi^2n^2)},
\]

is exactly the Hermite-Loewner matrix of \(b_{02}\):

\[
W_{02}(n,m)
=
\frac{b_{02}(n)-b_{02}(m)}{n-m}
\quad(n\ne m),
\qquad
W_{02}(n,n)=b_{02}'(n).
\]

This follows from

\[
\frac{n/(a^2+n^2)-m/(a^2+m^2)}{n-m}
=
\frac{a^2-mn}{(a^2+n^2)(a^2+m^2)}.
\]

## 5. Exact regularized Archimedean source

Let

\[
\rho(y)=\frac{e^{y/2}}{e^y-e^{-y}},
\qquad
r(y)=\frac{1}{e^y-e^{-y}},
\]

\[
\psi_y(s)
=
\frac1\pi
\sin\left(2\pi\left(1-\frac yL\right)s\right),
\qquad
\psi_0(s)=\frac{\sin(2\pi s)}{\pi}=2h(s),
\]

and

\[
\tau_L
=
\frac12\log\frac{e^L+1}{e^L-1},
\qquad
c_0=\log(4\pi)+\gamma.
\]

Define

\[
\boxed{
b_R(s)=
\int_0^L
\left[
\rho(y)\psi_y(s)-r(y)\psi_0(s)
\right]dy
+
(c_0-2\tau_L)h(s).
}
\]

The subtraction makes the integrand regular at \(y=0\): the singular
\(1/(2y)\) pieces cancel before integration.

At every integer \(n\),

\[
b_R(n)
=
-\frac1\pi\int_0^L
\sin\frac{2\pi n y}{L}\,\rho(y)\,dy
=-\alpha(n),
\]

while

\[
b_R'(n)
=
c_0+
\int_0^L
\frac{
2e^{y/2}(1-y/L)\cos(2\pi n y/L)-2
}{e^y-e^{-y}}dy
-2\tau_L.
\]

These are exactly the off-diagonal and diagonal Archimedean data in the CCM
matrix. Hence

\[
\boxed{W_R=L_{b_R}}
\]

on every finite integer node set.

## 6. Exact prime-power source

For the finite prime-power set \(k\le e^L=\lambda^2\), define

\[
\boxed{
b_P(s)
=
\sum_{2\le k\le e^L}
\frac{\Lambda(k)}{\sqrt k}\,
\psi_{\log k}(s).
}
\]

Then the finite-place matrix is exactly

\[
\boxed{W_P=L_{b_P}.}
\]

This is immediate from the Nyquist-fold theorem and linearity.

## 7. A single explicit arithmetic Hermite source for the full matrix

Define

\[
\boxed{
b_W(s)=b_{02}(s)-b_R(s)-b_P(s).
}
\]

Then the full finite semilocal Weil matrix

\[
Q=W_{02}-W_R-W_P
\]

satisfies, for **every** finite node set \(-N\le n,m\le N\),

\[
\boxed{
Q_{nm}
=
\begin{cases}
\displaystyle
\frac{b_W(n)-b_W(m)}{n-m},&n\ne m,\\[10pt]
b_W'(n),&n=m.
\end{cases}}
\]

So all finite Galerkin matrices are principal Hermite-Loewner compressions of
one explicit zero-independent arithmetic source \(b_W\). The source depends
on the support scale \(L\), but not on the Galerkin cutoff \(N\).

This identifies the displacement vector in the rank-two identity explicitly:
up to the conventional additive constant in a Loewner source,

\[
\boxed{\beta_n=b_W(n),\qquad \eta_n=1.}
\]

The rank-two displacement law is therefore the standard Loewner identity

\[
DQ-QD=\beta\eta^T-\eta\beta^T.
\]

## 8. Exact meaning of the ground shift

Let

\[
\varepsilon_N=\lambda_{\min}(Q_N).
\]

Since \(L_h=I\),

\[
\boxed{
Q_N-\varepsilon_N I
=
L_{,b_W-\varepsilon_N h}
\quad\text{on }\{-N,\dots,N\}.
}
\]

Thus the finite Herglotz/Pick completion does not alter the arithmetic
interpolation values \(b_W(n)\). It alters only the unresolved critical-density
derivative channel, by a pure Nyquist endpoint mode.

This is a sharper formulation of the remaining RH obstruction:

> the scalar ground shift is a boundary/Nyquist defect, not a bulk
> prime-by-prime deformation.

It also explains why the shift is invisible in the off-diagonal divided
differences and appears only in the diagonal Hermite data.

## 9. Relation to the two-channel boundary theorem

The boundary-channel theorem uses

\[
DQ-QD=\beta\eta^T-\eta\beta^T.
\]

The present result identifies \(\beta\) concretely as the sampled folded
arithmetic phase \(b_W(n)\). Therefore the abstract two-channel plane
\(\operatorname{span}\{\eta,\beta\}\) is exactly the value/derivative
boundary data of a critical-density Hermite sampling problem.

This suggests a more precise interpretation of the two channels:

- \(\eta\): the universal value channel;
- \(\beta\): the sampled arithmetic phase channel;
- \(I=L_h\): the otherwise invisible Nyquist derivative channel.

A proof of RH still requires controlling the outer limit of the Nyquist defect
or identifying the limiting Herglotz function. This note does not prove that
\(\varepsilon_N\ge0\), \(\varepsilon_N\to0\), or that the limiting
arithmetic Pick function is Herglotz.

## 10. Why this is useful

The old viewpoint treated the diagonal and off-diagonal formulas as somewhat
different pieces. They are not. After the support reflection \(y\mapsto L-y\),
they are a single exact Hermite-Loewner object.

This gives three concrete next attacks:

1. **Nyquist-defect asymptotics.** Bound \(\varepsilon_N\) by studying only the
   endpoint mode \(h\), rather than the entire matrix entrywise.
2. **Weyl-limit identification.** Use the explicit source \(b_W\) to identify
   the finite Herglotz interpolants on an Euler-product-domain vertical
   interval, then apply the existing Herglotz--Vitali theorem.
3. **Residue quantization.** Combine the explicit source with the finite Weyl
   norming-constant identity to attack the observed residue law
   \(-B(t)/A'(t)\propto\sin^2(\pi t)\).

The accompanying script verifies the exact fold, Nyquist identity, pole source,
and the assembled CCM source against the matrix formulas at high precision.
