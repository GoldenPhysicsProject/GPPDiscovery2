# Shadow Euler completion: unconditional Casimir product, Stieltjes/Fredholm RH criterion, and glueball uniqueness set

Date: 2026-09-28
Status: exact reformulation and new synthesis extracted from Daniel Toupin's May 2026 paper "The Shadow Euler Identity". No RH proof is claimed.

## 0. Audit of the May paper

The paper contains a useful structure but mixes two levels:

- the product written only with positive ordinates \(\gamma_\rho\),
  \[
  \xi(\tfrac12+z)/\xi(\tfrac12)
  =
  \prod_{\gamma>0}(1+z^2/\gamma^2),
  \]
  is RH-conditional;
- the genuinely unconditional object is the product over the centered zero/Casimir variables.

The right completion is therefore to promote the Casimir variable, not the ordinate, to the primary spectral coordinate.

## 1. Unconditional centered entire function

Define
\[
X(z)
=
\frac{\xi(\tfrac12+z)}{\xi(\tfrac12)}.
\]

The functional equation gives
\[
X(-z)=X(z).
\]

Hence there is a unique entire function \(F\) with
\[
\boxed{
X(z)=F(z^2),
}
\]
namely
\[
F(u)=\sum_{m\ge0} a_{2m}u^m
\]
if \(X(z)=\sum a_{2m}z^{2m}\).

Because \(X\) has order one in \(z\), \(F\) has order \(1/2\) in \(u\). Therefore its canonical product has genus zero and no nonconstant exponential prefactor:
\[
\boxed{
F(u)=\prod_j\left(1-\frac{u}{u_j}\right),
}
\]
where
\[
u_j=(\rho_j-\tfrac12)^2
\]
with one zero from each functional-equation pair
\[
\rho\leftrightarrow1-\rho.
\]

This product is unconditional.

## 2. Unconditional conformal-Casimir Euler identity

Set
\[
c=s(1-s),
\qquad
u=(s-\tfrac12)^2=\frac14-c,
\]
and for a nontrivial zero
\[
c_\rho=\rho(1-\rho)
=\frac14-u_\rho.
\]

Then
\[
1-\frac{u}{u_\rho}
=
\frac{c_\rho-c}{c_\rho-\frac14}.
\]

Therefore the exact unconditional product is
\[
\boxed{
\frac{\xi(s)}{\xi(\tfrac12)}
=
\prod_{\rho/\{\rho\sim1-\rho\}}
\frac{c_\rho-s(1-s)}
{c_\rho-\frac14}.
}
\]

This is the correct unconditional form of the Shadow Euler identity.

The Riemann hypothesis is exactly
\[
\boxed{
c_\rho\in[\tfrac14,\infty)
\quad\text{for every nontrivial zero}.
}
\]

Indeed for
\[
\rho=\beta+i\gamma,
\]
\[
\Im c_\rho
=
\gamma(1-2\beta),
\]
so reality of the Casimir already forces \(\beta=1/2\) for a nonreal zero, and then
\[
c_\rho=\frac14+\gamma^2.
\]

Thus the old ordinate product is not the starting theorem; it is the principal-series specialization of the unconditional Casimir product.

## 3. Exact positive-Fredholm equivalence

RH is equivalent to existence of a positive trace-class operator \(A\) such that
\[
\boxed{
F(u)=\det(I+uA).
}
\]

Proof.

If RH holds, write the zeros
\[
\rho_n=\frac12\pm i\gamma_n.
\]
Then
\[
u_n=-\gamma_n^2
\]
and
\[
F(u)
=
\prod_n\left(1+\frac{u}{\gamma_n^2}\right).
\]
Since
\[
\sum_n\gamma_n^{-2}<\infty,
\]
the positive operator with eigenvalues
\[
\lambda_n=\gamma_n^{-2}
\]
is trace class and gives the determinant.

Conversely, if
\[
F(u)=\det(I+uA),
\qquad A\ge0,
\]
then every zero of \(F\) lies at
\[
u=-\lambda^{-1}\le0.
\]
Hence every centered zero satisfies
\[
(\rho-\tfrac12)^2\in(-\infty,0),
\]
so
\[
\Re\rho=\frac12.
\]

This is exactly the current GPP positive-Fredholm target, now derived directly from the Shadow Euler paper.

## 4. Exact Stieltjes criterion

For \(u>0\), define the shadow response
\[
\boxed{
m(u)
=
\frac{F'(u)}{F(u)}
=
\frac{1}{2\sqrt u}
\frac{\xi'}{\xi}
\left(\frac12+\sqrt u\right),
}
\]
with the removable value at \(u=0\).

Under RH,
\[
m(u)
=
\sum_n\frac{1}{u+\gamma_n^2},
\]
so \(m\) is a Stieltjes transform of the positive spectral measure
\[
\mu=\sum_n\delta_{\gamma_n^2}.
\]

Conversely, if the zero-independent function \(m\) is a Stieltjes function, then it is holomorphic on
\[
\mathbb C\setminus(-\infty,0]
\]
and can have poles only on the negative real axis. But its poles are exactly the zeros \(u_j\) of \(F\). Hence all \(u_j<0\), and RH follows.

Therefore
\[
\boxed{
\mathrm{RH}
\iff
m(u)
=
\frac{1}{2\sqrt u}\frac{\xi'}{\xi}(\tfrac12+\sqrt u)
\text{ is Stieltjes}.
}
\]

This is the resolvent/Weyl form of the Shadow Euler identity.

## 5. Complete-Bernstein form

Let
\[
\Phi(u)=\log F(u),
\qquad u>0.
\]

Under RH,
\[
\Phi(u)
=
\sum_n\log(1+u/\gamma_n^2).
\]

Each summand is a complete Bernstein function, hence so is \(\Phi\).

Conversely, if the zero-independent \(\Phi\) extends as a complete Bernstein function on the slit plane, then \(F=e^\Phi\) is zero-free off the negative real axis. Since \(F\) is entire, all of its zeros lie on the negative real axis, giving RH.

Thus
\[
\boxed{
\mathrm{RH}
\iff
\log\frac{\xi(\tfrac12+\sqrt u)}{\xi(\tfrac12)}
\text{ is a complete Bernstein function of }u.
}
\]

This corrects the old paper's RH-conditional "Haar positivity" statement: complete monotonicity/Stieltjes positivity is not a consequence already proved there; it is an exact RH-equivalent target.

## 6. The Shadow Euler glueball coordinates are scalar Schur complements

The paper's special evaluation point is
\[
s_{k,N}=\frac{kN}{k+N}.
\]

This has an exact variational meaning:
\[
\boxed{
\min_{x+y=z}
\left(kx^2+Ny^2\right)
=
\frac{kN}{k+N}z^2.
}
\]

So \(s_{k,N}\) is the effective stiffness / parallel sum / scalar Schur complement of two positive channels with stiffnesses \(k\) and \(N\).

The associated shadow coupling satisfies
\[
a_{k,N}^2
=
\left(s_{k,N}-\frac12\right)^2
=
\frac14-s_{k,N}(1-s_{k,N}).
\]

Thus the old Yang--Mills/glueball evaluation points are naturally adapted to the CURRENT GPP architecture:
- integrate out positive bulk channels;
- obtain a Schur-complement effective coupling;
- evaluate the arithmetic Casimir/Fredholm determinant at its distance from the principal-series threshold.

This connection was not visible in the May formulation.

## 7. One fixed Kac--Moody level gives a uniqueness set

Fix any integer
\[
k\ge2.
\]

As \(N\to\infty\),
\[
s_{k,N}
=
\frac{kN}{k+N}
\longrightarrow k,
\]
and therefore
\[
u_{k,N}
=
\left(s_{k,N}-\frac12\right)^2
\longrightarrow
\left(k-\frac12\right)^2.
\]

The points \(u_{k,N}\) are distinct and have an accumulation point inside the positive real domain.

Therefore, if \(D(u)\) is ANY analytic candidate determinant on a connected neighborhood of the positive axis and one proves
\[
\boxed{
D(u_{k,N})
=
\frac{\xi(s_{k,N})}{\xi(\tfrac12)}
\quad\text{for every }N
}
\]
for just one fixed \(k\ge2\), then the identity theorem forces
\[
D(u)=F(u)
\]
throughout the connected analytic domain.

This is a useful reduction:

> A zero-independent positive operator construction does not have to be matched to xi at every spectral parameter. It is enough to prove the determinant identity on one infinite Shadow-Euler/glueball family with an interior accumulation point.

If the candidate \(D\) is a positive Fredholm determinant
\[
D(u)=\det(I+uA),
\qquad A\ge0,
\]
then this discrete family alone would force RH.

## 8. Moment/Hankel completion of the old sum rules

Define zero-independent Taylor invariants
\[
t_m
=
(-1)^{m+1}m\,[u^m]\log F(u).
\]

Under RH,
\[
t_m
=
\sum_n\gamma_n^{-2m}
=
\operatorname{Tr}A^m.
\]

Hence the old Shadow Euler sum rules become the current inverse-Casimir trace hierarchy.

The exact zero-independent RH target is not merely
\[
t_m>0.
\]

It is that \((t_m)\) is a Stieltjes moment sequence, equivalently that the full Hankel families
\[
\boxed{
H^{(0)}_{ij}=t_{i+j+1},
\qquad
H^{(1)}_{ij}=t_{i+j+2}
}
\]
are positive semidefinite for every finite size, with the required determinacy/growth.

This is precisely the BPY Hankel/Gram target already present in the current programme.

So the May paper's spectral-moment section was pointing at the right invariant but stopped one level too early: individual positivity of moments is weaker than the full Stieltjes/Hankel condition.

## 9. What this contributes to the current closure attempt

The Shadow Euler paper now supplies three useful pieces:

1. **The correct variable** is
   \[
   u=\frac14-s(1-s)=(s-\tfrac12)^2,
   \]
   the defect from the principal-series Casimir threshold.

2. **The physical sample points** \(s_{k,N}=kN/(k+N)\) are actual Schur-complement couplings, matching the current vacuum-quotient/mass-gap machinery.

3. **One fixed level is a uniqueness set.** If the finite self-dual divisor/KMS construction can produce a positive Fredholm determinant and prove equality with xi only on that discrete family, analytic uniqueness finishes the determinant identification globally.

The remaining load-bearing theorem is therefore sharper than before:

> Construct the positive physical inverse-Casimir operator \(A\) from the self-dual divisor/Hodge/KMS system, and prove its determinant agrees with the Shadow Euler ratios at one fixed \(k\ge2\) for all \(N\).

That would imply
\[
F(u)=\det(I+uA)
\]
and therefore RH.
