# RH Cayley-Li Higgs hierarchy
## Date: 2026-09-24
## Status: exact Cayley/Higgs/Li identities and a new finite-unitary convergence target

The arithmetic Higgs construction has a natural coordinate already present elsewhere in the project:

\[
z=\beta(s)=\frac{s-1}{s}=1-\frac1s.
\]

This is precisely the Cayley coordinate used by Li's criterion.

## 1. Critical line = Higgs unit circle

Solve
\[
s=\frac1{1-z}.
\]

Then
\[
|z|<1
\iff
|s-1|<|s|
\iff
\Re s>\frac12,
\]
and
\[
\boxed{
|z|=1
\iff
\Re s=\frac12.
}
\]

Thus the critical line is exactly the unit circle of the Higgs/Cayley coordinate.

The relative arithmetic Higgs field found earlier is
\[
H(s)=z\,\zeta(s).
\]
At the pole vacuum \(s=1\), \(z=0\), the pole of zeta is canceled and
\[
H(1)=1.
\]

So the relative Higgs field has a canonically normalized vacuum at the center of the disk.

## 2. Normalized completed Higgs field

Define
\[
\Phi(z)
=
2\,\xi\!\left(\frac1{1-z}\right).
\]

Since \(\xi(1)=1/2\),
\[
\Phi(0)=1.
\]

The nontrivial zero \(\rho\) maps to
\[
z_\rho
=
1-\frac1\rho
=
\frac{\rho-1}{\rho}.
\]

Therefore RH is exactly
\[
\boxed{
|z_\rho|=1
\quad\text{for every nontrivial zero }\rho.
}
\]

In Higgs language: every defect of the completed order parameter lies on the vacuum boundary circle.

## 3. Li coefficients are connected Higgs cumulants

The logarithm of the normalized completed Higgs field has the exact Taylor expansion
\[
\boxed{
\log\Phi(z)
=
\sum_{n\ge1}\frac{\lambda_n}{n}z^n,
}
\]
equivalently
\[
\boxed{
\frac{\Phi'(z)}{\Phi(z)}
=
\sum_{n\ge1}\lambda_n z^{n-1}.
}
\]

Thus the Li coefficients are exactly the connected Taylor cumulants of the completed Higgs effective action about the normalized vacuum \(z=0\).

Their zero representation is
\[
\lambda_n
=
\sum_\rho
\left[
1-
\left(1-\frac1\rho\right)^n
\right]
=
\sum_\rho(1-z_\rho^n),
\]
with the usual symmetric interpretation.

Li's criterion is therefore the exact Higgs stability hierarchy
\[
\boxed{
RH
\iff
\lambda_n\ge0
\quad\text{for every }n\ge1.
}
\]

If RH holds, \(z_\rho=e^{i\theta_\rho}\) and conjugate/reflection pairing gives
\[
(1-z_\rho^n)+(1-\overline{z_\rho}^{\,n})
=
2(1-\cos(n\theta_\rho))
=
4\sin^2(n\theta_\rho/2)\ge0.
\]

Each critical zero then contributes a nonnegative phase mass to every Higgs cumulant.

## 4. Finite self-adjoint model gives an automatically positive Li hierarchy

Let \(\mathcal D_N\) be any finite self-adjoint spectral approximant with real eigenvalues \(t_j\). Define its Cayley unitary
\[
U_N
=
(\mathcal D_N+\tfrac i2 I)
(\mathcal D_N-\tfrac i2 I)^{-1}.
\]

For a real eigenvalue \(t\),
\[
u(t)
=
\frac{t+i/2}{t-i/2}
=
\frac{(1/2+it)-1}{1/2+it},
\]
so this is exactly the same Cayley coordinate \(z_\rho\) for a hypothetical critical zero \(\rho=1/2+it\).

Define the finite Li/Higgs energies
\[
\boxed{
\Lambda_n^{(N)}
=
\operatorname{Tr}
\left(
I-\frac{U_N^n+U_N^{*n}}2
\right).
}
\]

Because \(U_N\) is unitary,
\[
I-\frac{U_N^n+U_N^{*n}}2
=
\frac12(I-U_N^n)^*(I-U_N^n)
\ge0.
\]

Hence
\[
\boxed{
\Lambda_n^{(N)}\ge0
\quad\text{for every finite }N,n.
}
\]

This is an exact finite Higgs-mass hierarchy.

## 5. UV suppression is automatically inverse-square

For one real spectral point \(t\),
\[
|1-u(t)|
=
\frac1{\sqrt{t^2+1/4}}.
\]

Since
\[
|1-u^n|\le n|1-u|
\]
on the unit circle,
\[
1-\Re u(t)^n
=
\frac12|1-u(t)^n|^2
\le
\boxed{
\frac{n^2}{2(t^2+1/4)}.
}
\]

Therefore high finite spectral points contribute only inverse-square weight to every fixed Li cumulant.

This is exactly the same UV principle already found for the finite Weyl function: raw high-energy mass is irrelevant; inverse moments control compact/low-order observables.

## 6. New closure target

The finite CCM boundary construction already gives a real-rooted self-adjoint quotient and hence a unitary Cayley transform. It therefore produces an automatically nonnegative sequence \(\Lambda_n^{(N)}\).

A new sufficient theorem is:

> For each fixed \(n\), prove that along the physical diagonal cutoff
> \[
> \Lambda_n^{(N(L))}\longrightarrow\lambda_n.
> \]

Then every Li coefficient is a limit of nonnegative finite Higgs masses:
\[
\lambda_n\ge0
\quad\forall n,
\]
and Li's criterion gives RH.

This target is potentially weaker than convergence of every individual finite spectral point because the test function
\[
1-\Re u(t)^n
\]
decays as \(O_n(t^{-2})\). Therefore the already-developed UV escape/inverse-moment machinery is exactly adapted to it.

The proof would need:
1. identification of the resolved finite spectral counting measure with the physical completed-zeta spectral data on every fixed window;
2. a uniform unweighted inverse-square tail bound for the finite self-adjoint spectrum, or another trace-class domination sufficient for the Cayley test;
3. convergence of the finite counting trace against the fixed Cayley test functions.

This bypasses the unproved finite Weyl residue law because \(\Lambda_n^{(N)}\) counts eigenvalues with their algebraic multiplicities rather than Weyl residues.

The remaining convergence theorem is still RH-strength and is not claimed here. But it is a new, sharply UV-soft formulation of the closure problem in which positivity is exact at every finite cutoff.
