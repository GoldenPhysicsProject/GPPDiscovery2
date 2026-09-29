# Shadow-KMS rigidity: off-line zero pairs are boosts, not Hilbert rotations

Date: 2026-09-29
Status: exact local Hilbert/Krein and prime-TFD theorems; sharpened RH reduction. No RH claim.

This note continues the prime-square-root hypercube attack. The new point is that the
functional-equation pair of a hypothetical off-line zero already carries a canonical
two-dimensional **split-unitary boost**. To force the principal series one does not need
global Weil positivity: it is enough to show that this two-dimensional zero-pair sector
inherits any nondegenerate positive Hilbert metric from the physical Poisson/KMS
completion.

A second exact theorem shows that the prime TFD/KMS state and its shadow partner are
thermodynamically inequivalent away from Re(s)=1/2: their finite-prime overlap collapses
to zero. This identifies the critical line as the unique shadow-self-dual KMS sector.

## 1. Prime square roots linearize multiplication as Lorentz rapidity

For x>0 define the square-root Cayley coordinate
\[
\beta(x)=\frac{\sqrt x-1}{\sqrt x+1}.
\]
Equivalently
\[
\beta(x)=\tanh\left(\frac14\log x\right).
\]

Hence multiplication becomes the exact Einstein/Mobius addition law
\[
\boxed{
\beta(xy)
=
\frac{\beta(x)+\beta(y)}
     {1+\beta(x)\beta(y)}.
}
\]

Indeed, putting q=sqrt(x), r=sqrt(y),
\[
\frac{q-1}{q+1}\oplus\frac{r-1}{r+1}
=
\frac{qr-1}{qr+1}.
\]

Thus the positive multiplicative group is represented by one-dimensional Lorentz boosts.
Let
\[
a(x)=\frac14\log x,
\qquad
B(x)=
\begin{pmatrix}
\cosh a(x)&\sinh a(x)\\
\sinh a(x)&\cosh a(x)
\end{pmatrix}.
\]
Then
\[
\boxed{B(xy)=B(x)B(y),\qquad B(x^{-1})=B(x)^{-1}.}
\]

For a prime p, the velocity coordinate is exactly
\[
\beta_p=\frac{\sqrt p-1}{\sqrt p+1}.
\]

This gives a precise meaning to the square-root-prime pattern: prime multiplication is
additive in the hyperbolic rapidities log(p)/4.

## 2. The TFD/DtN block is the positive metric attached to the same Cayley variable

At kappa=1/2 and interval length ell=log p, the exact prime TFD /
Dirichlet-to-Neumann block is
\[
D_p=
\frac1{2(p-1)}
\begin{pmatrix}
p+1&-2\sqrt p\\
-2\sqrt p&p+1
\end{pmatrix}.
\]

Writing beta=beta_p, one gets
\[
D_p
=
\frac1{4\beta}
\begin{pmatrix}
1+\beta^2&-(1-\beta^2)\\
-(1-\beta^2)&1+\beta^2
\end{pmatrix},
\]
with eigenvalues
\[
\boxed{\lambda_-=\frac{\beta}{2},\qquad
\lambda_+=\frac1{2\beta}},
\]
and
\[
\boxed{\det D_p=\frac14.}
\]

So the same Cayley coordinate that turns multiplication into boost addition also
diagonalizes the positive prime-local modular metric.

## 3. A hypothetical off-line zero pair is exactly a split-unitary boost

Let
\[
\rho=\frac12+\delta+i\gamma,
\qquad
\rho^\sharp:=1-\bar\rho
=\frac12-\delta+i\gamma.
\]

The centered half-density scaling characters are
\[
\chi_\rho(t)
=
e^{(1/2-\rho)t}
=
e^{-\delta t}e^{-i\gamma t},
\]
and
\[
\chi_{\rho^\sharp}(t)
=
e^{\delta t}e^{-i\gamma t}.
\]

On the pair space C^2 the scale action is
\[
V_\rho(t)
=
e^{-i\gamma t}
\begin{pmatrix}
e^{-\delta t}&0\\
0&e^{\delta t}
\end{pmatrix}.
\]

Let
\[
J=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]
Then for EVERY real delta,
\[
\boxed{V_\rho(t)^*JV_\rho(t)=J.}
\]

Therefore the functional-equation/shadow pair automatically admits a split/Krein-unitary
realization even off the critical line. This explains why functional-equation symmetry by
itself cannot prove RH: an off-line zero pair is a perfectly good hyperbolic boost in an
indefinite metric.

## 4. Positive-metric rigidity: the two-dimensional theorem sufficient for RH

Now suppose there exists a positive-definite Hermitian metric G on this two-dimensional
zero-pair sector such that
\[
V_\rho(t)^* G V_\rho(t)=G
\qquad
\text{for all }t.
\]

Since G>0, its first diagonal entry g_11 is strictly positive. The (1,1) entry of the
invariance equation is
\[
e^{-2\delta t}g_{11}=g_{11}.
\]
For any nonzero t this forces
\[
e^{-2\delta t}=1,
\]
hence
\[
\boxed{\delta=0}.
\]
Therefore
\[
\boxed{\Re\rho=\frac12.}
\]

This is the finite-dimensional positive-metric form of the Astra
zero-survival/unitarity theorem.

It sharpens the load-bearing statement drastically:

> For every nontrivial zero, it is enough to show that the shadow-paired zero datum
> survives as a nondegenerate two-dimensional invariant sector of ANY positive Hilbert
> completion of the physical scale action.

No global Weil positivity theorem is required. No spectral gap is required. No full QFT
construction is required. The only forbidden possibility is that the zero datum is lost,
degenerate, or lives only in an indefinite/Krein sector.

## 5. Prime TFD shadow fidelity

The existing normalized prime occupation state is
\[
|\Omega_{p,s}\rangle
=
\sqrt{1-p^{-2\sigma}}
\sum_{k\ge0}p^{-ks}|k\rangle,
\qquad
s=\sigma+it,\quad \sigma>0.
\]

For the anti-linear shadow partner
\[
s^\sharp=1-\bar s=(1-\sigma)+it,
\]
the local overlap is exactly
\[
\boxed{
F_p(\sigma)
=
\langle\Omega_{p,s},\Omega_{p,s^\sharp}\rangle
=
\frac{
\sqrt{(1-p^{-2\sigma})(1-p^{-2(1-\sigma)})}
}{
1-p^{-1}
}.
}
\]
The phase t cancels completely.

By AM-GM,
\[
F_p(\sigma)\le1,
\]
with equality iff
\[
p^{-2\sigma}=p^{-2(1-\sigma)},
\]
hence iff
\[
\boxed{\sigma=\frac12.}
\]

Thus at EVERY single prime the critical half-density is the unique point where the
normalized KMS state is exactly shadow-self-dual.

## 6. Exact off-line orthogonality catastrophe over the primes

Put
\[
\delta=\sigma-\frac12.
\]
A direct calculation gives
\[
\boxed{
1-F_p(\sigma)^2
=
\frac{
p^{-1}(p^\delta-p^{-\delta})^2
}{
(1-p^{-1})^2
}.
}
\]

If delta is nonzero, let d=|delta|>0. For all sufficiently large p,
\[
(p^d-p^{-d})^2
=
p^{2d}(1-p^{-2d})^2
\ge\frac14p^{2d}.
\]
Since 0<F_p<=1,
\[
1-F_p
\ge
\frac12(1-F_p^2)
\ge
\frac18p^{-1+2d}
\ge
\frac1{8p}.
\]

Euler's divergence
\[
\sum_p\frac1p=\infty
\]
therefore gives
\[
\sum_p(1-F_p)=\infty.
\]
Using log x <= -(1-x) for 0<x<=1,
\[
\boxed{
\prod_pF_p(\sigma)=0
\qquad
(\sigma\ne1/2).
}
\]

At sigma=1/2 every local factor is exactly 1, so
\[
\boxed{
\prod_pF_p(1/2)=1.
}
\]

Therefore the shadow-paired prime KMS states display an exact dichotomy:
\[
\boxed{
\text{critical line: identical shadow sector;}
\qquad
\text{off line: thermodynamic orthogonality catastrophe.}
}
\]

This requires no PNT and no zero data.

## 7. Even stronger local modular-spectrum rigidity

The prime state has geometric occupation probabilities
\[
\lambda_k(\sigma)
=
(1-p^{-2\sigma})p^{-2\sigma k}.
\]

They are the eigenvalues of the reduced thermal density matrix. A unitary equivalence of
the sigma and 1-sigma modular states must preserve their spectra. In particular it
preserves the largest eigenvalue:
\[
1-p^{-2\sigma}
=
1-p^{-2(1-\sigma)}.
\]
Therefore
\[
\boxed{\sigma=1/2.}
\]

So if the physical shadow/CPT map is shown to act as a unitary equivalence of even ONE
prime modular factor for a spectral datum, the real part is fixed immediately.

The global orthogonality theorem is stronger evidence that the off-line shadow pair lies
in inequivalent thermodynamic sectors, but the local modular-spectrum argument is the
cheapest rigidity statement.

## 8. What remains to prove for the zeta zeros

The mathematics above does NOT yet identify a zeta zero with a normalizable TFD vector.
That would simply hide the missing theorem.

The exact remaining bridge can now be stated in a very small form:

> **Zero-sector positivity / modular-shadow bridge.**
> The completed Poisson/product-formula construction sends every nontrivial zeta zero
> rho to a nonzero shadow-paired spectral datum whose scale action is the character pair
> V_rho(t), and the induced physical pairing on that pair is positive definite
> (equivalently, the shadow/CPT map is implemented in the positive modular Hilbert
> representation rather than only in a Krein completion).

Then section 4 gives Re(rho)=1/2 immediately.

This target is weaker than:
- global Weil positivity;
- positivity of every test-function quadratic form;
- a full self-adjoint operator with completely identified spectrum;
- Stieltjes positivity of the entire completed resolvent.

It asks only for positivity/nondegeneracy on the two-dimensional sector already singled
out by one hypothetical zero and its anti-linear shadow.

## 9. Why the prime-square-root geometry matters to that bridge

The local prime metric is not guessed. It is already the positive
Dirichlet-to-Neumann/TFD metric, and its Cayley parameter is
\[
\beta_p=(\sqrt p-1)/(\sqrt p+1).
\]

The additive self-dual side already has the finite subgroup-state embedding B_N with
\[
G_N=B_N^*B_N>0.
\]

So the most direct current attack is:

1. construct the finite zero/response pair inside the Poisson-coupled image of B_N;
2. show the finite scale action intertwines with the ambient unitary/self-adjoint
   additive action;
3. retain a nondegenerate limiting two-dimensional pair;
4. positivity then passes from B_N^*B_N to the pair;
5. the boost-rigidity theorem forces delta=0.

This is now the smallest positive-metric statement visible in the project that would
actually close RH.
