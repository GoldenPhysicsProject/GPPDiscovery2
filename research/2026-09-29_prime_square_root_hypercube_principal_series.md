# Prime square roots: multiquadratic hypercube, Möbius parity, and the half-density principal-series boundary

Date: 2026-09-29
Status: exact algebraic/representation-theoretic identities and a sharpened RH search heuristic. No RH claim.

Daniel asked what pattern appears when primes are raised to the power \(1/2\). The answer is much more structured than the raw decimal sequence \(\sqrt2,\sqrt3,\sqrt5,\ldots\): square roots turn the prime labels into independent \(\mathbb Z_2\) directions, make the squarefree sector a finite hypercube, identify Möbius parity with a Galois/parity character, and expose the same half-density boundary \(\Re s=1/2\) that appears in the principal series.

## 1. Distinct prime square roots generate an exact Boolean hypercube

Fix distinct primes \(p_1,\ldots,p_r\) and let
\[
K_r=\mathbb Q(\sqrt{p_1},\ldots,\sqrt{p_r}).
\]

The prime classes are independent in
\[
\mathbb Q^\times/(\mathbb Q^\times)^2.
\]
Hence
\[
[K_r:\mathbb Q]=2^r,
\qquad
\operatorname{Gal}(K_r/\mathbb Q)\cong(\mathbb Z/2\mathbb Z)^r.
\]

A basis is
\[
\left\{
\sqrt d:
d\mid p_1\cdots p_r,\ d\text{ squarefree}
\right\}.
\]

Thus every subset \(S\subseteq\{1,\ldots,r\}\) corresponds exactly to
\[
\sqrt{d_S}=\prod_{j\in S}\sqrt{p_j}.
\]

Each Galois automorphism independently flips signs
\[
\sqrt{p_j}\mapsto \epsilon_j\sqrt{p_j},
\qquad
\epsilon_j\in\{\pm1\},
\]
and therefore
\[
\sqrt{d_S}\mapsto
\left(\prod_{j\in S}\epsilon_j\right)\sqrt{d_S}.
\]

This is an exact finite compact \(2\)-torsion harmonic-analysis model. Its characters are indexed by squarefree subsets.

## 2. Möbius parity is literally the global sign character

For squarefree \(d\),
\[
\mu(d)=(-1)^{\omega(d)}.
\]

Take the Galois element that flips every prime square root:
\[
\epsilon_p=-1\quad\text{for every active prime }p.
\]
Then
\[
\sqrt d\mapsto(-1)^{\omega(d)}\sqrt d
=\mu(d)\sqrt d.
\]

So on the squarefree sector, Möbius parity is literally the parity/Galois character of the prime-square-root hypercube.

This gives a precise algebraic realization of the project's recurrent "Möbius as fermion parity" heuristic.

## 3. The squarefree Möbius state is an exact fermionic product state

For a finite prime set \(P\), introduce a two-state local factor
\[
|0\rangle_p,\ |1\rangle_p.
\]
Then
\[
\boxed{
\Psi_P(s)
=
\bigotimes_{p\in P}
\left(
|0\rangle_p-p^{-s}|1\rangle_p
\right)
}
\]
expands as
\[
\boxed{
\Psi_P(s)
=
\sum_{d\mid \prod_{p\in P}p}
\mu(d)d^{-s}|d\rangle
}
\]
over squarefree divisors \(d\).

At the half-density line
\[
s=\frac12+it,
\]
the local occupied amplitude is
\[
p^{-1/2-it}
=
p^{-1/2}e^{-it\log p}.
\]

Thus:
- \(p^{-1/2}\) is the fixed critical radial amplitude;
- \(e^{-it\log p}\) is a pure unitary phase;
- the global \(t\)-dependence is a one-parameter unitary rotation on the prime hypercube.

This is the cleanest finite algebraic picture found so far of the statement "the principal-series parameter is a common global phase attached to every prime."

## 4. The Hilbert threshold is exactly Re(s)=1/2

The finite norm is
\[
\|\Psi_P(s)\|^2
=
\prod_{p\in P}
\left(1+p^{-2\sigma}\right),
\qquad
\sigma=\Re s.
\]

For the infinite product, convergence is equivalent to
\[
\sum_p p^{-2\sigma}<\infty.
\]

Therefore
\[
\boxed{
\Psi(s)\in\text{ordinary prime Fock Hilbert space}
\iff
\Re s>\frac12.
}
\]

At the boundary \(\sigma=1/2\),
\[
\|\Psi_P\|^2
=
\prod_{p\le P}\left(1+\frac1p\right)
\]
diverges only logarithmically in the prime cutoff (equivalently the norm grows like a square root of that logarithm, up to the standard Mertens normalization).

This is another exact origin of the critical one-half:
the principal-series line is the square-summability boundary of the fermionic prime-square-root state.

The phase \(t\) does not affect the norm at all.

## 5. Why the square root is representation-theoretically natural

Write
\[
\ell_p=\log p.
\]
Then
\[
p^{-1/2}=e^{-\ell_p/2}.
\]

In normalized principal-series induction, the square root of the modular character is the canonical half-density normalization. The factor \(1/2\) is therefore not an arbitrary zeta shift: it is the square-root Haar/modular correction that converts the raw scaling character into a unitary one.

Schematically,
\[
p^{-s}
=
p^{-1/2}\,p^{-it}
\quad\text{when}\quad
s=\frac12+it.
\]

The first factor is the modular half-density; the second is a unitary character.

This is the local-prime form of the same mechanism as the exact abstract zero-survival theorem:
a surviving scale character can be unitary only when its real exponent has been reduced to the canonical half-density.

## 6. A second exact square-root pattern: the TFD / Dirichlet-to-Neumann block

The trace-energy calculation gives, at
\[
\kappa=\frac12,\qquad \ell=\log p,
\]
the local matrix
\[
D_p
=
\frac1{2(p-1)}
\begin{pmatrix}
p+1&-2\sqrt p\\
-2\sqrt p&p+1
\end{pmatrix}.
\]

Its determinant is independent of the prime:
\[
\boxed{\det D_p=\frac14.}
\]

Let
\[
q_p=\sqrt p,
\qquad
\beta_p=\frac{q_p-1}{q_p+1}
=
\tanh\left(\frac{\log p}{4}\right).
\]
Then the two eigenvalues are exactly
\[
\boxed{
\lambda_-(p)=\frac12\beta_p,
\qquad
\lambda_+(p)=\frac1{2\beta_p},
}
\]
so
\[
\lambda_-(p)\lambda_+(p)=\frac14.
\]

Thus taking the square root of the prime exposes a Cayley variable
\[
\beta_p=\frac{\sqrt p-1}{\sqrt p+1}
\]
and an exact reciprocal eigenvalue pair.

Under inversion \(p\mapsto p^{-1}\),
\[
\beta_p\mapsto-\beta_p.
\]

This is an exact local self-dual/reflection pattern, not a decimal coincidence.

For \(p=5\),
\[
\beta_5
=
\frac{\sqrt5-1}{\sqrt5+1}
=
\frac{3-\sqrt5}{2}
=
\varphi^{-2},
\]
which is a genuine special identity of the prime \(5\), but no claim is made that all primes organize by the golden ratio.

## 7. What this says about the RH target

The finite prime-square-root sector is already compact and completely understood:
\[
(\mathbb Z/2)^r
\]
with squarefree characters and exact Möbius parity.

The continuous parameter \(t\) enters only through the common phases
\[
e^{-it\log p}.
\]

So the arithmetic Hilbert structure naturally factors into:
- a compact squareclass / fermionic occupation sector;
- one global continuous scaling parameter \(t\);
- the half-density \(p^{-1/2}\) fixed by the modular square root.

This strongly supports the principal-series picture:
the only continuous deformation compatible with the fixed half-density norm is phase motion in \(t\).

But this by itself does NOT prove that every zeta zero survives as a continuous spectral datum in this finite/infinite completion. The no-escape theorem is still the missing step.

## 8. Sharpened experiment/theorem target

Instead of asking vaguely why \(1/2\) appears, use the prime-square-root Fock model to ask:

1. Can the exact Poisson/product-formula boundary map be written on the finite hypercube
   \[
   \bigotimes_{p\le P}\mathbb C^2
   \]
   so that its scalar completed response is holomorphic at every cutoff?

2. Does the map intertwine the common phase evolution
   \[
   |1\rangle_p\mapsto e^{-it\log p}|1\rangle_p
   \]
   with the physical boundary scale evolution?

3. After the Archimedean coupling, does every zero define a nonzero continuous eigenfunctional of that evolution?

If yes, the already-proved zero-survival/subexponential theorem forces every such zero into
\[
s=\frac12+it.
\]

This is potentially a cleaner finite model than the raw all-integer zeta graph because the squarefree/Galois sector is an exact finite compact group with an explicit Peter-Weyl basis.
