# Penrose quotient and Fourier-support closure

## Status

This note records the 2026-09-04 push on the GPP-native googly programme.  It does not claim the full analytic Penrose/Fourier theorem.

## CI repair

The explicit changed-module gate on GPPVerify PR #173 exposed residual Lean 4.33 fragility in `GrassmannianGooglyDecomposition.lean` even though the root build was green.  The module was rewritten with explicit product extensionality and field normalization so the Euclidean complement, quarter-turn factorization and Plucker/Hodge statements no longer depend on brittle `ext <;> field_simp` behaviour.

## Intrinsic Fourier-support theorem

On a graph plane

\[
Z(r,s)=(r,s,ra+sc,rb+sd),
\]

for a Fourier variable \(\xi\), define

\[
C_1(\xi)=\xi_0+a\xi_2+b\xi_3,
\qquad
C_2(\xi)=\xi_1+c\xi_2+d\xi_3.
\]

The restricted ambient phase factorizes as

\[
Z(r,s)\cdot\xi=r C_1(\xi)+s C_2(\xi).
\]

The formalization now proves the exact equivalence

\[
C_1(\xi)=C_2(\xi)=0
\iff
\forall r,s,\; Z(r,s)\cdot\xi=0
\iff
\xi\in W^\circ.
\]

Thus the finite-dimensional support locus selected by plane integration is intrinsically the annihilator plane, not merely a coordinate coincidence.

## Penrose quotient

For a linear Penrose map \(P:A\to B\), define

\[
a\sim_P a' \iff P(a)=P(a').
\]

The quotient \(A/{\sim_P}\) is the correct home for projective/distributional twistor representatives when regularizations may differ by Penrose-null terms.

A new formal module constructs this quotient explicitly and proves:

1. bulk reconstruction descends to the quotient;
2. the induced bulk map is injective;
3. any representative transform \(F\) satisfying a Penrose intertwiner
   \[
   P_B(Fa)=R(P_A a)
   \]
   automatically respects the quotient and descends;
4. two representative transforms with the same Penrose image induce the same quotient map.

This converts regularization ambiguity from a defect into the expected gauge/quotient structure.

## Projective googly involution

A second new module proves a stronger closure principle.  Suppose there are forward/backward representative transforms \(F,G\) and bulk maps \(R,S\) with

\[
P_B(Fa)=R(P_Aa),
\qquad
P_A(Gb)=S(P_Bb),
\]

and

\[
S\circ R=\mathrm{id},
\qquad
R\circ S=\mathrm{id}.
\]

Then the descended transforms on Penrose quotients are mutually inverse even if

\[
G(Fa)\neq a
\]

as raw representatives.  Representative-level discrepancies lying in the Penrose kernel disappear automatically.

This is important for projective Fourier transforms because polynomial/regularization ambiguities need not obstruct a genuine physical involution.

## Current best chain

The exact finite-dimensional spine is now

\[
D_{\mathrm{Fourier\ support}}
\cong
D_{\mathrm{annihilator}}
\cong
D_{\mathrm{split\ polarity}}
=
D_{\Gr}
=
D_{\mathrm{Hodge}},
\]

with independent ambient-rank-four homogeneity reflection

\[
k\mapsto-k-4
\]

and therefore

\[
h\mapsto-h.
\]

The physical quotient formulation means the target theorem should be stated on Penrose classes, not raw homogeneous representatives.

## Remaining hard theorem

Construct the actual projective/distributional Fourier-Radon transform \(\mathcal F_{\rm proj}\) and prove

\[
P_-\circ \mathcal F_{\rm proj}
=
R_{\mathfrak o}\circ P_+
\]

on the appropriate homogeneous distribution quotient.  Once this representative-level intertwiner is established, quotient descent and involutivity are already formal consequences.

## Falsifiers

The proposed universal mechanism fails if the concrete transform:

- does not descend to the required homogeneous projective classes;
- has the wrong \(-4\) canonical weight shift;
- selects a support locus different from annihilator/polarity;
- fails the Penrose commuting square even modulo the Penrose kernel;
- requires extra noncanonical structure beyond the declared split reality/orientation data.
