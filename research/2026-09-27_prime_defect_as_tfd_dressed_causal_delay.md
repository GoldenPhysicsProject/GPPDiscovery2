# Prime de Branges defect as a TFD-dressed causal delay line

Date: 2026-09-27
Status: exact local Hilbert-space factorization. This gives a concrete causal realization of each prime channel and isolates the relative ghost as free-delay subtraction. No RH proof.

## 1. The logarithmic prime length is an inner delay

Fix a prime \(p\) and write
\[
L_p=\log p,
\qquad
a_p=p^{-1/2}.
\]

The exponential
\[
\phi_p(z)=e^{iL_p z}
\]
maps the upper half-plane to the unit disk:
\[
\Im z>0
\quad\Longrightarrow\quad
|\phi_p(z)|=e^{-L_p\Im z}<1.
\]

Its upper-half-plane de Branges/Schur defect kernel is
\[
D_{\phi_p}(z,w)
=
\frac{
1-\phi_p(z)\overline{\phi_p(w)}
}{
-i(z-\bar w)
}.
\]

Since
\[
\frac{
1-e^{iL_p(z-\bar w)}
}{
-i(z-\bar w)
}
=
\int_0^{L_p}
e^{it z}\overline{e^{itw}}\,dt,
\]
we have the exact Gram representation
\[
\boxed{
D_{\phi_p}(z,w)
=
\int_0^{L_p}
e^{itz}\overline{e^{itw}}\,dt.
}
\]

Thus the primitive logarithmic length \(L_p\) is literally the length of a causal delay-line Hilbert space
\[
L^2([0,L_p],dt).
\]

## 2. Dress the delay by the prime TFD/Blaschke channel

Let
\[
B_a(\zeta)=\frac{\zeta-a}{1-a\zeta},
\qquad 0<a<1.
\]

Its disk defect is rank one:
\[
\frac{
1-B_a(\zeta)\overline{B_a(\eta)}
}{
1-\zeta\bar\eta
}
=
f_a(\zeta)\overline{f_a(\eta)},
\]
where
\[
f_a(\zeta)
=
\frac{\sqrt{1-a^2}}{1-a\zeta}.
\]

For \(a=a_p=p^{-1/2}\), \(f_{a_p}\) is exactly the boundary amplitude of the critical prime TFD coherent state.

Now compose:
\[
\boxed{
\Theta_p^{\rm in}(z)
=
B_{a_p}\!\left(e^{iL_pz}\right).
}
\]

This is an inner function on the upper half-plane.

## 3. Exact composition defect factorization

Using
\[
1-B_a(\phi_z)\overline{B_a(\phi_w)}
=
\frac{
1-B_a(\phi_z)\overline{B_a(\phi_w)}
}{
1-\phi_z\overline{\phi_w}
}
\left(
1-\phi_z\overline{\phi_w}
\right),
\]
we get
\[
\boxed{
D_{\Theta_p^{\rm in}}(z,w)
=
f_{a_p}(\phi_p(z))
\overline{f_{a_p}(\phi_p(w))}
D_{\phi_p}(z,w).
}
\]

Substituting the delay-line Gram representation,
\[
\boxed{
D_{\Theta_p^{\rm in}}(z,w)
=
\int_0^{L_p}
F_{p,t}(z)
\overline{F_{p,t}(w)}
\,dt,
}
\]
with
\[
\boxed{
F_{p,t}(z)
=
e^{itz}
\frac{\sqrt{1-p^{-1}}}
{1-p^{-1/2}e^{iL_pz}}.
}
\]

Therefore every prime has an explicit causal Hilbert-space realization:
\[
\boxed{
\text{prime channel}
=
\text{finite delay line of length }\log p
\quad\text{dressed by its TFD coherent defect}.
}
\]

## 4. The diagonal is exactly the positive group delay

For real \(x\),
\[
D_{\Theta_p^{\rm in}}(x,x)
=
L_p
\frac{1-a_p^2}
{1-2a_p\cos(L_px)+a_p^2}.
\]

Hence
\[
\boxed{
D_{\Theta_p^{\rm in}}(x,x)
=
L_p\,\mathcal P_{a_p}(L_px)
=
\frac{d}{dx}
\arg
\Theta_p^{\rm in}(x).
}
\]

So the de Branges defect density, the TFD phase probability, and the Wigner--Smith delay are not merely analogous: they are the same diagonal kernel.

## 5. Free-delay subtraction produces the arithmetic current

The bare delay has diagonal
\[
D_{\phi_p}(x,x)=L_p.
\]

Therefore the relative diagonal is
\[
\begin{aligned}
D_{\Theta_p^{\rm in}}(x,x)
-D_{\phi_p}(x,x)
&=
L_p\left[
\mathcal P_{a_p}(L_px)-1
\right]\\
&=
2L_p
\sum_{m\ge1}
a_p^m\cos(mL_px).
\end{aligned}
\]

Since
\[
a_p^m=p^{-m/2},
\]
we obtain
\[
\boxed{
\frac12
\left(
D_{\Theta_p^{\rm in}}(x,x)
-D_{\phi_p}(x,x)
\right)
=
\sum_{m\ge1}
\frac{\Lambda(p^m)}{\sqrt{p^m}}
\cos(x\log p^m).
}
\]

Thus the local von-Mangoldt half-density current is exactly half the **relative de Branges density**
\[
\boxed{
\text{TFD-dressed delay}
-
\text{free delay}.
}
\]

## 6. The ghost is now an off-diagonal relative kernel

Define
\[
\boxed{
R_p(z,w)
=
D_{\Theta_p^{\rm in}}(z,w)
-
D_{\phi_p}(z,w).
}
\]

Both terms are positive kernels individually.

Their difference is not generally positive.

This is the exact causal-kernel analogue of the earlier covariance result:
- full TFD covariance is positive;
- normal ordering subtracts the vacuum and creates an indefinite relative form.

Here:
- the full dressed prime delay is positive;
- subtracting the bare propagation delay creates the signed arithmetic relative kernel.

So the covariance ghost and scattering ghost are literally the same subtraction in two representations.

## 7. Finite cascades remain explicitly positive before subtraction

For a finite ordered prime set, let
\[
\Theta_{\mathcal P}^{\rm in}
=
\prod_{p\in\mathcal P}
\Theta_p^{\rm in}.
\]

The product defect identity gives
\[
D_{\Theta_1\Theta_2}
=
D_{\Theta_1}
+
\Theta_1(z)\overline{\Theta_1(w)}
D_{\Theta_2}.
\]

Iterating,
\[
\boxed{
D_{\Theta_{\mathcal P}^{\rm in}}
=
\sum_{p\in\mathcal P}
U_{<p}
D_{\Theta_p^{\rm in}}
U_{<p}^*,
}
\]
where \(U_{<p}\) is multiplication by the preceding inner cascade.

Thus the finite prime cascade has an explicit positive Gram decomposition into transported TFD-dressed delay lines.

The indefiniteness enters only when one passes to the relative/background-subtracted object required by the explicit formula.

## 8. Sharpened global completion target

The completed RH problem can now be phrased as a causal network problem.

At every finite place we have an explicit conservative subsystem
\[
L^2([0,\log p])
\]
with feature map \(F_{p,t}\).

The arithmetic explicit-formula current is obtained by subtracting the direct-sum free-delay background.

The real place must supply the canonical renormalized continuum/background system which turns the infinite relative kernel into the positive completed de Branges kernel.

So the missing theorem is no longer “find a prime Hilbert space.”

The prime Hilbert spaces and their causal feature maps are explicit.

The missing theorem is:
\[
\boxed{
\text{prove Archimedean/rational sewing dominates the infinite free-delay-subtracted prime defect on the physical analytic subspace.}
}
\]

This is exactly the global no-ghost / odd-transfer contraction problem in concrete causal feature coordinates.
