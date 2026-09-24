# RH discovery: heat-smoothed stability and a polynomial boundary-coupling target
## A possible bypass of the time-zero causality obstruction

**Date:** 2026-09-24  
**Status:** Sections 1--4 are exact. Section 5 is a conditional closure theorem whose missing hypothesis is one explicit heat-level boundary/Feshbach identity. This is not an RH proof.

## 1. Fixed-window heat regularization does not weaken the RH detector

Fix one triangle window
\[
h_\ell(u)=(1-|u|/\ell)_+,
\qquad
C_\ell(t)=\mathcal W(h_\ell(\,\cdot-t)).
\]

Let
\[
g_\tau(t)=\frac1{\sqrt{4\pi\tau}}e^{-t^2/(4\tau)},
\qquad \tau>0,
\]
and define the heat-smoothed translated correlation
\[
\boxed{
C_{\ell,\tau}(t)
=
(g_\tau*C_\ell)(t).
}
\]

The convolution is well-defined because the arithmetic Weil distribution has at most
the standard \(e^{|t|/2}\)-type growth and the Gaussian dominates every exponential.

If
\[
\lambda_\rho=\rho-\frac12,
\]
then the fixed-window zero expansion gives
\[
C_\ell(t)
=
\sum_\rho H_\ell(\lambda_\rho)e^{\lambda_\rho t}.
\]
Gaussian convolution therefore gives the exact spectral expansion
\[
\boxed{
C_{\ell,\tau}(t)
=
\sum_\rho
H_\ell(\lambda_\rho)
e^{\tau\lambda_\rho^2}
e^{\lambda_\rho t}.
}
\tag{1}
\]

The extra factor
\[
e^{\tau\lambda_\rho^2}
\]
is never zero.

Hence heat regularization changes the residues but does not delete any zeta exponent.

Let
\[
\Theta
=
\sup_\rho\left|\Re\rho-\frac12\right|.
\]

The same positive-Laplace/Landau proof used for the unsmoothed fixed-window theorem now gives:

### Theorem 1
For every fixed \(\ell,\tau>0\), the least exponential rate needed for an eventual
one-sided upper bound on \(C_{\ell,\tau}\) is exactly \(\Theta\):
\[
\boxed{
\Theta
=
\inf\left\{
\alpha\ge0:
C_{\ell,\tau}(t)\le M_\alpha e^{\alpha t}
\text{ eventually}
\right\}.
}
\tag{2}
\]

In particular,
\[
\boxed{
\mathrm{RH}
\iff
C_{\ell,\tau}(t)
\text{ is eventually bounded above by }e^{o(t)}.
}
\tag{3}
\]

Proof: for \(\alpha>\Theta\), the Gaussian factor gives even stronger convergence in
the zero sum, so the upper estimate is immediate. Conversely, if an upper bound with
\(\alpha<\Theta\) held, put
\[
G(t)=M e^{\alpha t}-C_{\ell,\tau}(t)\ge0.
\]
Its Laplace transform equals
\[
\frac{M}{z-\alpha}
-
\sum_\rho
\frac{
H_\ell(\lambda_\rho)e^{\tau\lambda_\rho^2}
}{
z-\lambda_\rho
}.
\]
Landau's theorem forces the abscissa of a positive Laplace transform to be a real
singularity. There are no positive-real zeta exponents, while every off-axis zero
with real part \(>\alpha\) still contributes a nonzero nonreal pole because neither
\(H_\ell(\lambda_\rho)\) nor the Gaussian factor vanishes. Contradiction.

Thus the heat smoothing does **not** erase the RH obstruction.

## 2. Heat-smoothed two-box energy

Let
\[
E_{\ell,\tau}(t)
=
C_{\ell,\tau}(0)-C_{\ell,\tau}(t).
\]

Exactly as in the unsmoothed case,
\[
\boxed{
\mathrm{RH}
\iff
E_{\ell,\tau}(t)
\ge
-\exp(o(t)).
}
\tag{4}
\]

Any polynomial lower bound is sufficient.

This is important because the time-zero Hodge/Koszul contraction is known to fail,
whereas the project already has an exact bounded positive-time Ward homotopy.

The old no-go theorem "bilateral heat destroys Tate causality" remains correct.
The present criterion does not ask the Gaussian to preserve the Tate Hardy domain.
It uses heat only as a nonvanishing spectral regulator and tests semiboundedness of
the resulting real arithmetic correlation.

Thus the old obstruction and the new criterion concern different statements.

## 3. Existing exact heat-level prime cancellation

The project already proves, on the compact prime boundary, the exact positive-time identity
\[
\boxed{
\{d,H_\tau\}
=
(I-P_0)e^{-\tau\mathcal L_p}.
}
\tag{5}
\]

The heat factor removes the irrational-rotation small divisors which destroy the
time-zero bounded Koszul homotopy.

Therefore the nonconstant prime-ghost sector is exactly contractible after any fixed
positive heat time.

What remains is the completed Archimedean boundary coupling.

## 4. The Archimedean synthesis has only polynomial Hilbert--Schmidt size

For a finite arithmetic length cutoff \(n\le e^L\), the exact global Schur architecture
uses the synthesis map
\[
\mathcal C_L e_n
=
n^{-1/2}T_{\log n}\phi.
\]

Let the logarithmic occupation/length operator be
\[
\mathsf L e_n=(\log n)e_n.
\]

Because translations are unitary,
\[
\|\mathcal C_L\|_{\rm HS}^2
=
\|\phi\|_2^2
\sum_{n\le e^L}\frac1n
=
O_\phi(L).
\tag{6}
\]

More importantly,
\[
\boxed{
\|\mathcal C_L\mathsf L\|_{\rm HS}^2
=
\|\phi\|_2^2
\sum_{n\le e^L}\frac{(\log n)^2}{n}
=
O_\phi(L^3).
}
\tag{7}
\]

No prime theorem is needed for this estimate: the actual occupation set is a subset
of the positive integers and
\[
\sum_{n\le X}\frac{(\log n)^2}{n}
\le
C+\int_1^X\frac{(\log x)^2}{x}\,dx
=
C+\frac13(\log X)^3.
\]

Thus the logarithmically differentiated completed boundary synthesis is polynomial-size
in exactly the scale required by the new stability criterion.

This is the key quantitative observation.

## 5. Conditional heat-Feshbach closure theorem

Suppose one can identify the heat-smoothed localized completed Weil form with the physical
boundary compression of a self-adjoint block system
\[
\boxed{
\mathbb H_{\tau,L}
=
\begin{pmatrix}
H_{\tau,L} & V_{\tau,L}\\
V_{\tau,L}^* & B_{\tau,L}
\end{pmatrix},
}
\tag{8}
\]
where

1. \(H_{\tau,L}\ge0\) is the heat-regularized Hodge--Koszul bulk;
2. \(B_{\tau,L}\) is bounded below by a polynomial in \(L\);
3. the completed boundary coupling is obtained from the exact Archimedean synthesis and
   satisfies
   \[
   \|V_{\tau,L}\|
   \le
   \|\mathcal C_L\mathsf L\|_{\rm HS}
   =
   O_\tau(L^{3/2});
   \]
4. the physical compression of (8) is exactly the heat-smoothed Weil quadratic form,
   not a positive majorant and not a modulus square.

Then
\[
\lambda_{\min}(\mathbb H_{\tau,L})
\ge
-\|V_{\tau,L}\|
+\min(0,\inf B_{\tau,L})
=
-\operatorname{poly}(L).
\tag{9}
\]

Indeed, for a normalized vector \((x,y)\),
\[
2\Re\langle V_{\tau,L}y,x\rangle
\ge
-2\|V_{\tau,L}\|\|x\|\|y\|
\ge
-\|V_{\tau,L}\|
(\|x\|^2+\|y\|^2).
\]

By Theorem 1 / equation (4), polynomial semiboundedness of the exact heat-smoothed
physical form forces
\[
\Theta=0,
\]
hence RH.

### What remains

The missing theorem is therefore no longer a time-zero bounded Koszul contraction and
no longer full Hardy causality.

It is the following explicit identity:

> **Heat-level completed Feshbach identity.**  
> Show that the Gaussian-smoothed completed Weil form is exactly the physical boundary
> compression of the already-positive heat-regularized Hodge--Koszul bulk coupled through
> the co-Poisson/Archimedean synthesis map, with no replacement of the arithmetic linear
> functional by a different quadratic majorant.

If this identity holds, the polynomial Hilbert--Schmidt estimate (7) supplies the required
subexponential stability automatically.

## 6. Why this may bypass a previous no-go

The project proved that bilateral heat cannot preserve the causal Tate Hardy space:
\[
F,\ e^{-\tau\lambda^2}F\in H^2
\quad\Longrightarrow\quad
F=0.
\]

That killed the proposal to use Gaussian heat as a **causal homotopy at time zero**.

The present route does something weaker:

- heat regularization is fixed and positive;
- the RH detector survives because its spectral multiplier never vanishes;
- one proves only a polynomial lower-energy bound;
- then the heat regulator is not removed inside the Hardy category.

Thus the previous no-go does not logically rule this route out.

The remaining danger is different: the heat-level Schur/Feshbach physical compression
must reproduce the exact completed Weil functional. If it instead produces a norm square,
a modulus square, or an unrelated positive majorant, the argument does not prove RH.

That exact identification is now the principal target.
