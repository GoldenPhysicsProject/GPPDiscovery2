# Exact two-sheet decomposition of the BPY vacuum and emergent O(4) component symmetry

Date: 2026-09-27
Status: exact zero-independent Gaussian/probability identities. No RH claim. The Lorentzian interpretation is a research hypothesis, not a derived spacetime theory.

## 1. Split the four-field BPY variable into two identical complex sheets

Write the BPY variable as
\[
Q_4
=
\frac1{2\pi}
\sum_{n\ge1}
\frac{
G_{n,1}^2+G_{n,2}^2+G_{n,3}^2+G_{n,4}^2
}{n^2}.
\]

Group the four real components into two pairs:
\[
Q_+
=
\frac1{2\pi}
\sum_{n\ge1}
\frac{G_{n,1}^2+G_{n,2}^2}{n^2},
\]
\[
Q_-
=
\frac1{2\pi}
\sum_{n\ge1}
\frac{G_{n,3}^2+G_{n,4}^2}{n^2}.
\]

Then
\[
\boxed{Q_4=Q_++Q_-}
\]
with \(Q_+\) and \(Q_-\) independent and identically distributed.

Equivalently define complex Gaussian mode variables
\[
Z_{n,+}=G_{n,1}+iG_{n,2},
\qquad
Z_{n,-}=G_{n,3}+iG_{n,4}.
\]
Each sheet is one complex Gaussian field over the same number-circle/arithmetic one-particle space.

## 2. Each sheet carries exactly one celestial thermal factor

For one two-real-component sheet,
\[
\mathbb E e^{-tQ_\pm}
=
\prod_{n\ge1}
\left(1+\frac{t}{\pi n^2}\right)^{-1}
=
\frac{\sqrt{\pi t}}{\sinh\sqrt{\pi t}}.
\]

At \(t=\pi\lambda^2\),
\[
\boxed{
\mathbb E e^{-\pi\lambda^2Q_\pm}
=
P(\lambda)
=
\frac{\pi\lambda}{\sinh\pi\lambda}.
}
\]

Therefore
\[
\boxed{
\mathbb E e^{-\pi\lambda^2Q_4}
=
P(\lambda)^2
}
\]
simply because the two sheets are independent.

So the square of the celestial Plancherel/thermal factor in the BPY construction is literally the product of two identical complex-sheet vacuum determinants.

## 3. The completed zeta radial variable is the glued two-sheet energy

The BPY theorem says
\[
\boxed{
\mathbb E[Q_4^{s/2}]=2\xi(s).
}
\]

Combined with the exact decomposition above,
\[
\boxed{
2\xi(s)
=
\mathbb E[(Q_++Q_-)^{s/2}].
}
\]

Thus completed zeta is the Mellin radial observable of the SUM of two identical complex Gaussian sheet energies.

This gives a precise two-sheet realization of the earlier geometric intuition:
- one complex sheet carries one \(P(\lambda)\);
- the doubled system carries \(P(\lambda)^2\);
- the nonlinear radial Mellin observable of the glued total energy gives \(\xi(s)\).

The nonlinearity \((Q_++Q_-)^{s/2}\) is crucial. The sheets factorize in Laplace space but not in the Mellin observable. That is a concrete mechanism for collective information to appear only after sewing.

## 4. Sheet exchange and the larger component symmetry

The decomposition has an obvious involution
\[
\mathcal J:(Q_+,Q_-)\leftrightarrow(Q_-,Q_+).
\]

But because all four real Gaussian components have the same covariance, the full Gaussian law is actually invariant under orthogonal rotations of the component index:
\[
\boxed{O(4)}.
\]

The visible sheet-exchange \(\mathbb Z_2\) is therefore only a discrete subgroup of a larger Euclidean internal symmetry of the auxiliary four-field vacuum.

The radial observable \(Q_4\) is \(O(4)\)-invariant.

## 5. Relation to the left/right conformal doubling

Independently the celestial scalar principal-series block satisfies
\[
h=\bar h=s,\qquad \Delta=2s
\]
after \(\lambda=2\tau\).

So there are now two exact doublings:

1. representation doubling:
\[
s\longmapsto(h,\bar h)=(s,s);
\]

2. Gaussian-sheet doubling:
\[
Q_2\longmapsto Q_++Q_-=Q_4.
\]

The first doubles a one-dimensional conformal weight into a two-dimensional scalar primary. The second doubles one complex Gaussian sector into two complex sectors.

Both produce the same factor-of-two architecture without inserting it by hand.

## 6. Why this is suggestive for the RP1 -> CP1 -> Lorentz ladder

A four-real-component Euclidean Gaussian target naturally carries \(O(4)\) component symmetry.

A formal Wick rotation of one target component changes the quadratic form signature from Euclidean \((4,0)\) to Lorentzian \((3,1)\), whose connected Lorentz group acts on the projectivized null cone. That projectivized null cone is the celestial sphere
\[
S^2\simeq\mathbb{CP}^1.
\]

This makes the sequence
\[
\text{two complex arithmetic sheets}
\to
\text{four real components}
\to
\text{Lorentzian null directions}
\to
\mathbb{CP}^1
\]
mathematically coherent at the level of dimensions and symmetry groups.

However, the Gaussian component index is still an auxiliary field index. The present calculation does NOT prove that it is physical spacetime. A genuine derivation would have to show why the component \(O(4)\) symmetry is promoted to spacetime symmetry and why the continuation selects a Lorentzian rather than merely internal signature.

## 7. A new rigidity target

The useful theorem target is now sharper:

Can the combined requirements
- number-circle covariance \(\Delta^{-1}\),
- one-complex-sheet determinant \(P(\lambda)\),
- reflection/sheet doubling,
- BPY completed Mellin reconstruction,
- and locality/covariance of the projected celestial theory

force the auxiliary \(O(4)\) component symmetry to become the Lorentz \(O(3,1)\) symmetry of the next holographic rung?

The first four ingredients are now exact. The last promotion is open.
