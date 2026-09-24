# RH discovery: the vacuum-instability exponent equals the rightmost-zero displacement
## Quantitative stability criterion for the Weil Hamiltonian

**Date:** 2026-09-24  
**Status:** exact consequence of the fixed-window theorem and its Laplace-transform argument. This is a criterion, not an RH proof.

## 1. Definitions

Fix one window width \(\ell>0\). Let
\[
f_\ell=\ell^{-1/2}\mathbf 1_{[0,\ell]},
\qquad
h_\ell=f_\ell*\widetilde f_\ell
=(1-|u|/\ell)_+.
\]

Let
\[
C_\ell(t)
=
\mathcal W(h_\ell(\,\cdot-t))
=
\sum_\rho H_\ell(\lambda_\rho)e^{\lambda_\rho t},
\qquad
\lambda_\rho=\rho-\frac12.
\]

The window transform
\[
H_\ell(z)
=
\ell
\left(
\frac{\sinh(\ell z/2)}{\ell z/2}
\right)^2
\]
does not vanish at any nontrivial zeta exponent \(\lambda_\rho\).

Define the rightmost displacement
\[
\boxed{
\Theta
=
\sup_\rho \Re\lambda_\rho
=
\sup_\rho
\left(\Re\rho-\frac12\right).
}
\]
By the functional equation, this is also
\[
\Theta
=
\sup_\rho
\left|\Re\rho-\frac12\right|.
\]

Define the one-sided correlation-growth exponent
\[
\boxed{
\sigma_\ell
=
\inf\left\{
\alpha\ge0:
\exists M_\alpha<\infty,\ 
C_\ell(t)\le M_\alpha e^{\alpha t}
\text{ for all sufficiently large }t
\right\}.
}
\]

Finally define the normalized two-box energy
\[
E_\ell(t)
=
\frac{
\mathcal W\left(
(f_\ell-T_tf_\ell)*
\widetilde{(f_\ell-T_tf_\ell)}
\right)
}{
\|f_\ell-T_tf_\ell\|_2^2
}
=
C_\ell(0)-C_\ell(t)
\qquad (t>\ell).
\]

Its instability exponent is
\[
\boxed{
\kappa_\ell
=
\inf\left\{
\alpha\ge0:
\exists K_\alpha<\infty,\ 
E_\ell(t)\ge-K_\alpha e^{\alpha t}
\text{ for all sufficiently large }t
\right\}.
}
\]

## 2. Exact exponent theorem

### Theorem
For every fixed \(\ell>0\),
\[
\boxed{
\sigma_\ell
=
\kappa_\ell
=
\Theta.
}
\tag{1}
\]

Consequently,
\[
\boxed{
\mathrm{RH}
\iff
\kappa_\ell=0
}
\tag{2}
\]
for any one fixed window.

Thus the maximal horizontal displacement of a zeta zero is exactly the
exponential instability rate of the normalized two-box Weil energy.

### Proof: upper bound

Let \(\alpha>\Theta\). Since
\[
\Re\lambda_\rho\le\Theta<\alpha
\]
for every zero and
\[
\sum_\rho |H_\ell(\lambda_\rho)|<\infty
\]
(the window transform is \(O(|\Im\lambda|^{-2})\) uniformly in the critical
strip and \(N(T)=O(T\log T)\)), one has
\[
C_\ell(t)
\le
|C_\ell(t)|
\le
e^{\alpha t}
\sum_\rho |H_\ell(\lambda_\rho)|.
\]
Hence
\[
\sigma_\ell\le\Theta.
\]

Since
\[
E_\ell(t)=C_\ell(0)-C_\ell(t),
\]
the same estimate gives
\[
\kappa_\ell\le\Theta.
\]

### Proof: lower bound

Suppose
\[
C_\ell(t)\le M e^{\alpha t}
\]
eventually for some \(\alpha<\Theta\). Enlarge \(M\) so that the bound holds
for all \(t\ge0\), and define
\[
g(t)=M e^{\alpha t}-C_\ell(t)\ge0.
\]

For \(\Re z>1/2\),
\[
\int_0^\infty e^{-zt}g(t)\,dt
=
\frac{M}{z-\alpha}
-
L_\ell(z),
\]
where
\[
L_\ell(z)
=
\sum_\rho
\frac{H_\ell(\lambda_\rho)}
{z-\lambda_\rho}.
\]

Choose a zero exponent \(\lambda_\rho\) with
\[
\Re\lambda_\rho>\alpha.
\]
Its residue in \(L_\ell\) is nonzero because
\[
H_\ell(\lambda_\rho)\ne0.
\]

The Laplace transform of the nonnegative function \(g\) has some abscissa of
convergence \(a\). Landau's positive-Laplace theorem says that, if \(a\) is
finite, the transform must have a singularity at the **real** point \(a\).

But the meromorphic continuation
\[
\frac{M}{z-\alpha}-L_\ell(z)
\]
has no positive-real zeta poles, because \(\xi(1/2+x)>0\) for real \(x\).
Its only inserted real singularity is \(z=\alpha\). Therefore its abscissa
cannot lie to the right of \(\alpha\).

It follows that the Laplace transform is holomorphic throughout
\[
\Re z>\alpha.
\]

That contradicts the nonreal pole at \(\lambda_\rho\), whose real part is
larger than \(\alpha\).

Therefore no such \(\alpha<\Theta\) is admissible:
\[
\sigma_\ell\ge\Theta.
\]

Because a lower bound
\[
E_\ell(t)\ge-Ke^{\alpha t}
\]
is equivalent to the one-sided upper bound
\[
C_\ell(t)\le C_\ell(0)+Ke^{\alpha t},
\]
the same lower-bound argument gives
\[
\kappa_\ell\ge\Theta.
\]

Combining both directions proves (1).

## 3. Support-radius formulation

Translate the two-box state by its midpoint. Its support lies in
\[
[-R,R],
\qquad
R=\frac{t+\ell}{2}.
\]

Let
\[
e(R)
=
\inf\left\{
\mathcal W(f*\widetilde f):
\|f\|_2=1,\ 
\operatorname{supp}f\subset[-R,R]
\right\}.
\]

Since the normalized two-box state is an admissible vector,
\[
e\!\left(\frac{t+\ell}{2}\right)
\le
E_\ell(t).
\]

Hence, if \(\Theta>0\), the arithmetic Hamiltonian develops normalized states
whose negative energy is exponentially unstable at rate at least \(2\Theta\)
in support radius.

Conversely, any **subexponential lower floor**
\[
\boxed{
\forall\varepsilon>0\quad
e(R)\ge
-M_\varepsilon e^{\varepsilon R}
}
\tag{3}
\]
implies RH.

Indeed, equation (3) applied to the centered two-box state gives
\[
C_\ell(t)
\le
C_\ell(0)
+
M_\varepsilon
e^{\varepsilon(t+\ell)/2}.
\]
Given any \(\delta>0\), choose \(\varepsilon=2\delta\). Then
\[
C_\ell(t)\le M'_\delta e^{\delta t}.
\]
The exponent theorem forces
\[
\Theta=0.
\]

Thus:
\[
\boxed{
\text{polynomial semiboundedness is already enough for RH.}
}
\tag{4}
\]

More generally, any support-dependent lower bound of the form
\[
e(R)\ge-\exp(o(R))
\]
proves RH.

This is substantially weaker than a support-independent constant lower bound.

## 4. Finite CCM formulation

Let
\[
L=2\log\lambda
\]
be the additive support length in the CCM model, and let
\[
\varepsilon_{L,N}
=
\lambda_{\min}(Q_{L,N})
\]
be the lowest unshifted Galerkin eigenvalue.

For fixed \(L\), the matrices \(Q_{L,N}\) are nested principal compressions,
so
\[
\varepsilon_{L,N+1}\le\varepsilon_{L,N}.
\]

If the Fourier spaces form a core for the localized Weil form, their limiting
lowest edge is the localized energy \(e(L/2)\), after the harmless choice of
centering convention.

Therefore the following is sufficient for RH:
\[
\boxed{
\forall\varepsilon>0\quad
\varepsilon_{L,N}
\ge
-M_\varepsilon e^{\varepsilon L}
}
\tag{5}
\]
uniformly along a correct form-core exhaustion.

In particular, any polynomial lower bound
\[
\varepsilon_{L,N}\ge -C(1+L)^A
\]
would prove RH.

There is no need to show
\[
\varepsilon_{L,N}\to0,
\]
no need for a uniform positive gap, and no need to identify every UV pole.

## 5. Physics interpretation

This gives a quantitative instability dictionary:
\[
\boxed{
\sup_\rho\left|\Re\rho-\frac12\right|
=
\text{vacuum-instability Lyapunov exponent}.
}
\]

An off-critical zero is not merely a "bad eigenvalue." It is a nonunitary
dilation resonance whose amplitude grows exponentially with separation.
The two-box state converts that nonunitarity into negative energy at the same
exponent.

RH is therefore equivalent to **zero exponential vacuum instability**.

The arithmetic Hamiltonian need not first be proved positive. It is enough to
show that its negative spectral edge grows slower than every exponential in
the support scale.

That is much closer to the type of stability estimate one normally proves in
mathematical physics.

## 6. Revised proof target

The best current target is now:
\[
\boxed{
\varepsilon_{L,N}\ge-\exp(o(L)).
}
\]

Candidate mechanisms to revisit:

1. Exact Eisenstein factorization
   \[
   \mathscr P_x=B_x^*B_x\ge0.
   \]
   The old route attempted to turn point evaluation into a positive norm.
   We now only need to bound the boundary defect by a subexponential function
   of support.

2. Maass--Selberg / trace estimates.
   Polynomial growth of the relevant truncated Eisenstein boundary norm would
   already suffice.

3. Global Schur quotient.
   A polynomial bound on the negative Schur boundary term is enough; it need
   not vanish and need not be positive.

4. Möbius-gauge Gram square.
   A positive bulk plus a boundary correction of polynomial norm would close
   the argument.

The target has therefore weakened from positivity, to uniform semiboundedness,
and now to **subexponential semiboundedness**.
