# Shadow-Euler Pick matrices: a single shifted glueball family is an RH-equivalent resolvent-Gram test

Date: 2026-09-28
Status: exact complex-analysis reduction. No RH proof. This strengthens the Shadow Euler uniqueness theorem by replacing unknown determinant matching with a directly testable positivity condition on zero-independent xi data.

## 1. The meromorphic inverse-Casimir response

Let
\[
F(u)
=
\frac{\xi(\frac12+\sqrt u)}{\xi(\frac12)}
\]
denote the entire function defined branch-independently by the even reduction
\[
\xi(\tfrac12+z)/\xi(\tfrac12)=F(z^2).
\]

Define
\[
m(u)=\frac{F'(u)}{F(u)}.
\]

The previous completion showed
\[
\mathrm{RH}
\iff
m \text{ is Stieltjes}.
\]

In particular, under RH
\[
m(u)=\sum_n\frac1{u+\gamma_n^2}.
\]

Set
\[
\boxed{
q(u)=-m(u).
}
\]

Under RH, \(q\) is a Pick/Herglotz function on the upper half-plane.

## 2. The Pick kernel is exactly a resolvent Gram kernel

Under RH,
\[
q(z)
=
-\sum_n\frac1{z+\gamma_n^2}.
\]

Therefore
\[
\begin{aligned}
\frac{q(z)-\overline{q(w)}}{z-\bar w}
&=
\sum_n
\frac1{(z+\gamma_n^2)(\bar w+\gamma_n^2)}\\
&=
\boxed{
\left\langle
(C-\tfrac14+z)^{-1}\Omega,\,
(C-\tfrac14+w)^{-1}\Omega
\right\rangle
}
\end{aligned}
\]
in the direct-sum realization with one cyclic coordinate per zero.

Hence the Nevanlinna-Pick kernel
\[
\boxed{
K_q(z,w)
=
\frac{q(z)-\overline{q(w)}}{z-\bar w}
}
\]
is literally a positive resolvent Gram kernel.

This is the exact analytic object the self-adjoint Casimir construction should reproduce.

## 3. One shifted Shadow-Euler family is enough

Fix:
\[
k\ge1,
\qquad
\eta>0.
\]

Let
\[
s_{k,N}=\frac{kN}{k+N},
\qquad
u_{k,N}=(s_{k,N}-\tfrac12)^2,
\]
and shift the physical Shadow-Euler points into the upper half-plane:
\[
\boxed{
z_N=u_{k,N}+i\eta.
}
\]

As \(N\to\infty\),
\[
z_N
\longrightarrow
z_*=(k-\tfrac12)^2+i\eta,
\]
an interior point of \(\mathbb C_+\).

For any finite set \(N_1,\dots,N_M\), form the zero-independent Pick matrix
\[
\boxed{
P^{(M)}_{ij}
=
\frac{
q(z_{N_i})-\overline{q(z_{N_j})}
}{
z_{N_i}-\overline{z_{N_j}}
}.
}
\]

Every entry is computable directly from xi and xi-prime:
\[
q(u)
=
-\frac1{2\sqrt u}
\frac{\xi'}{\xi}
\left(\frac12+\sqrt u\right),
\]
using a consistent square-root branch; equivalently compute \(F'/F\) from the branch-independent entire \(F\).

No zero list is used.

## 4. Theorem: positivity on this one sequence is equivalent to RH

### Forward implication

If RH holds, \(q\) is Herglotz/Pick, hence
\[
P^{(M)}\ge0
\]
for every finite \(M\).

### Reverse implication

Assume
\[
P^{(M)}\ge0
\]
for every finite subset of the sequence \((z_N)\).

By the Nevanlinna-Pick interpolation theorem, the interpolation data
\[
z_N\mapsto q(z_N)
\]
admit a holomorphic Pick function \(h\) on \(\mathbb C_+\).

But \(z_N\to z_*\in\mathbb C_+\), and \(q\) is holomorphic near \(z_*\) because \(F((k-\frac12)^2)\ne0\) for real \(k\ge1\). Since
\[
h(z_N)=q(z_N)
\]
on a sequence accumulating in the domain, the identity theorem forces
\[
h=q
\]
as meromorphic functions on the connected upper half-plane. Since \(h\) is holomorphic, \(q\) has no pole in \(\mathbb C_+\).

Now an off-critical zeta zero
\[
\rho=\frac12+\delta+i\gamma,
\qquad
\delta>0,\ \gamma>0,
\]
produces
\[
u_\rho=(\rho-\tfrac12)^2
=
\delta^2-\gamma^2+2i\delta\gamma
\in\mathbb C_+,
\]
which is a pole of \(q= -F'/F\).

Contradiction.

Functional-equation/conjugation symmetry supplies a zero with \(\delta>0,\gamma>0\) whenever any nontrivial zero is off the line. Hence all nontrivial zeros lie on
\[
\Re\rho=\frac12.
\]

Therefore
\[
\boxed{
\mathrm{RH}
\iff
P^{(M)}\ge0
\text{ for every finite Pick matrix drawn from ONE shifted Shadow-Euler family.}
}
\]

This is stronger operationally than the previous analytic uniqueness theorem: there is no unknown candidate determinant \(D\) to construct before testing. The test is directly on xi data.

## 5. Why the Schur-complement coordinates matter

The unshifted coordinates
\[
s_{k,N}=\frac{kN}{k+N}
\]
are exactly scalar parallel sums / Schur-complement stiffnesses.

Thus the nodes of the RH-equivalent Pick matrices come from physical effective couplings of positive two-channel systems.

The Pick matrix itself is a resolvent Gram matrix of a passive/self-adjoint system.

So the Shadow Euler paper now exhibits the SAME operation twice:
- Schur complements generate the sampling coordinates;
- resolvent Gram positivity tests whether the completed arithmetic response is passive/self-adjoint.

This is the strongest current mathematical bridge between the old glueball formula and the new mass-gap/Casimir programme.

## 6. Finite positivity target for the self-dual divisor model

If the finite self-dual divisor/KMS construction produces approximants
\[
q_P(z)
=
-\langle\Omega_P,(L_P+z)^{-1}\Omega_P\rangle
\]
with \(L_P\ge0\), then their Pick matrices are automatically PSD.

It is therefore enough to prove convergence on the shifted Shadow-Euler nodes:
\[
q_P(z_N)\to q(z_N)
\]
for every fixed \(N\).

The Pick positivity survives the limit entrywise. Hence all finite target Pick matrices are PSD, and RH follows by the theorem above.

This reduces the operator-construction burden again:

> One does not need uniform convergence of determinants or even resolvents on a continuum. It is enough to construct positive finite arithmetic resolvents and prove scalar convergence on one countable shifted Shadow-Euler family with an interior accumulation point.

That is now the sharpest discrete closure target in the programme.
