# RH relative Higgs field — continuum condensate, exact relative current, and completed reduction
## Date: 2026-09-24
## Status: exact finite causal identities; exact half-line symbol; heat-smoothed bilateral estimate; global RH closure still open

This note pushes the arithmetic Higgs idea one step further.

The exponentially growing \(e^{y/2}\) completion channel is the continuum analogue of the half-density zeta synthesis, with an exact Volterra inverse. The difference between the discrete arithmetic field and this continuum field is therefore a natural relative Higgs field. Its logarithmic current is exactly the difference between the arithmetic von Mangoldt current and the continuum current.

No RH claim is made here.

## 1. Continuum half-density condensate

On \(H_L=L^2(0,L)\), with causal shifts \(V_y\), define
\[
Z_L^{\rm vac}=I+\int_0^L e^{y/2}V_y\,dy,
\qquad
M_L^{\rm vac}=I-\int_0^L e^{-y/2}V_y\,dy.
\]

Direct Volterra convolution gives
\[
\boxed{M_L^{\rm vac}Z_L^{\rm vac}=Z_L^{\rm vac}M_L^{\rm vac}=I.}
\]

Thus the continuum condensate has an exact inverse whose integral kernel decays like \(e^{-y/2}\).

## 2. Exact continuum Higgs current

Let \(X\) be multiplication by the coordinate. Since \([X,V_y]=yV_y\),
\[
P_L^{\rm vac}:=M_L^{\rm vac}[X,Z_L^{\rm vac}]
\]
has the exact kernel
\[
\boxed{
P_L^{\rm vac}
=
\int_0^L\left(e^{y/2}-e^{-y/2}\right)V_y\,dy
=
\int_0^L2\sinh(y/2)V_y\,dy.
}
\]

So the continuum current carries exactly the dangerous \(e^{+y/2}\) large-\(y\) behavior.

## 3. Discrete arithmetic Higgs field

Define
\[
Z_L^{\rm ar}=\sum_{n<e^L}n^{-1/2}V_{\log n},
\qquad
M_L^{\rm ar}=\sum_{n<e^L}\mu(n)n^{-1/2}V_{\log n}.
\]

Then \(M_L^{\rm ar}Z_L^{\rm ar}=I\), and
\[
P_L^{\rm ar}:=M_L^{\rm ar}[X,Z_L^{\rm ar}]
=
\sum_{n<e^L}\Lambda(n)n^{-1/2}V_{\log n}.
\]

## 4. Relative Higgs field

Define
\[
\boxed{
H_L=M_L^{\rm vac}Z_L^{\rm ar}=(Z_L^{\rm vac})^{-1}Z_L^{\rm ar}.
}
\]

All operators lie in the same commutative causal convolution algebra, so \(Z_L^{\rm ar}=Z_L^{\rm vac}H_L\). Therefore
\[
\boxed{
P_L^{\rm ar}=P_L^{\rm vac}+H_L^{-1}[X,H_L].
}
\]

The relative Higgs current
\[
\boxed{
P_L^{\rm rel}:=H_L^{-1}[X,H_L]
=
P_L^{\rm ar}-P_L^{\rm vac}
}
\]
is exactly the arithmetic current with the continuum condensate removed.

## 5. Half-line spectral symbol

On the infinite causal half-line, Laplace transform sends \(V_y\) to multiplication by \(e^{-zy}\). For \(\Re z>1/2\),
\[
Z^{\rm vac}(z)
=
1+\int_0^\infty e^{-(z-1/2)y}\,dy
=
\frac{z+1/2}{z-1/2}.
\]

Putting \(s=z+1/2\),
\[
Z^{\rm vac}(z)=\frac{s}{s-1},
\qquad
Z^{\rm ar}(z)=\zeta(s).
\]

Hence
\[
\boxed{
H(z)=\frac{s-1}{s}\zeta(s).
}
\]

The continuum pole at \(s=1\) has been divided out. The nontrivial zeros of the relative Higgs field are precisely the nontrivial zeta zeros. In centered coordinate \(z=s-1/2\), RH is exactly confinement of all nontrivial Higgs defects to \(\Re z=0\). This is a reformulation, not a proof.

## 6. Completed Archimedean channel after Higgs subtraction

The completed real-place density is
\[
w_\infty(y)
=
e^{-y/2}+e^{y/2}
-\frac{e^{-y/2}}{1-e^{-2y}}.
\]

Subtract the continuum current density:
\[
r_\infty(y)
:=
w_\infty(y)-2\sinh(y/2).
\]

Then
\[
\boxed{
r_\infty(y)
=
2e^{-y/2}
-\frac{e^{-y/2}}{1-e^{-2y}}.
}
\]

Therefore
\[
r_\infty(y)=O(e^{-y/2})
\qquad(y\to\infty).
\]

So the entire \(e^{+y/2}\) tail of the completed pole/real-place channel is exactly the continuum Higgs current. The origin retains the usual renormalizable \(-1/(2y)\) singularity, already handled by the standard local subtraction.

Up to the explicit bounded contact/subtraction term, the completed causal Weil operator can therefore be organized as
\[
\boxed{
\mathcal W_L^{\rm cpl}
=
-\left(P_L^{\rm rel}+(P_L^{\rm rel})^*\right)
+
R_{\infty,L},
}
\]
where \(R_{\infty,L}\) has no exponentially growing large-\(y\) density.

Thus all possible exponential instability has been localized to the relative Higgs current.

## 7. Difference-field identity

Let
\[
E_L=Z_L^{\rm ar}-Z_L^{\rm vac}.
\]

The inverse resolvent identity gives
\[
M_L^{\rm ar}-M_L^{\rm vac}
=
-M_L^{\rm ar}E_LM_L^{\rm vac}.
\]

Hence
\[
\boxed{
P_L^{\rm ar}-P_L^{\rm vac}
=
M_L^{\rm ar}\left([X,E_L]-E_LP_L^{\rm vac}\right).
}
\]

This isolates the exact next norm problem: control the arithmetic inverse only on the connected difference source \([X,E_L]-E_LP_L^{\rm vac}\), not on the whole scalar Hilbert space.

## 8. Heat-smoothed continuum approximation on the bilateral line

Let \(U_y\) be bilateral translations on \(L^2(\mathbb R)\), and
\[
H_\tau=e^{\tau\partial_x^2},\qquad\tau>0.
\]

Then
\[
\|\partial_xH_\tau\|
=
\sup_{\xi\in\mathbb R}|\xi|e^{-\tau\xi^2}
=
\frac1{\sqrt{2e\tau}}.
\]

For
\[
F_0(x)=x^{-1/2}U_{\log x}H_\tau
\]
one has
\[
\|F_0'(x)\|
\le
x^{-3/2}
\left(
\frac12+\frac1{\sqrt{2e\tau}}
\right).
\]

An interval-by-interval Euler estimate gives, uniformly in \(N\),
\[
\boxed{
\left\|
\sum_{n=1}^N n^{-1/2}U_{\log n}H_\tau
-
\int_1^N x^{-1/2}U_{\log x}H_\tau\,dx
\right\|
\le
2+\sqrt{\frac{2}{e\tau}}.
}
\]

Since \(x=e^y\),
\[
\int_1^N x^{-1/2}U_{\log x}H_\tau\,dx
=
\int_0^{\log N}e^{y/2}U_yH_\tau\,dy.
\]

Thus at fixed positive heat time the discrete half-density field equals continuum condensate plus a cutoff-uniform bounded fluctuation in bilateral operator norm.

Likewise
\[
F_1(x)=(\log x)x^{-1/2}U_{\log x}H_\tau
\]
has integrable operator derivative, giving a cutoff-uniform bound for the corresponding first logarithmic moment. One simple bound is
\[
C_1(\tau)
\le
4+\frac{4}{\sqrt{2e\tau}}+\frac2e.
\]

Important limitation: these heat-smoothed estimates are bilateral. They do not by themselves transfer the exact causal Möbius inverse. That transfer is the remaining connected Hodge/Feshbach problem.

## 9. Current frontier

The structure is now
\[
Z^{\rm ar}=Z^{\rm vac}H,
\]
so
\[
\text{arithmetic current}
=
\text{vacuum current}
+
\text{relative Higgs current}.
\]

The completed real-place channel contains exactly the vacuum current's exponential tail. After subtraction, the residual real-place density decays.

The many-prime Hodge construction independently supplies
\[
\|D_L^{-1}\|=O(\sqrt L e^{-L/2})
\]
on the critical half-density line.

The remaining theorem is therefore:

> prove a subexponential directional bound for the relative-Higgs current
> \(H_L^{-1}[X,H_L]\) on the completed physical boundary, using the massive
> many-prime Hodge parent and the connected difference source.

A polynomial/subexponential bound closes RH through the already-proved fixed-window instability criterion.
