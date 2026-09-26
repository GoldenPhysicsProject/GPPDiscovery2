# Doubling constants as normalization slots: a stricter formulation

Date: 2026-09-26
Status: exact normalization relations plus a conjectural physical assignment. This note deliberately does **not** claim that pure Cayley–Dickson algebra determines the SI values of \(\hbar,c,G\).

## 1. What Holographic Chain v13 actually establishes

The revised paper correctly labels
\[
\hbar\leftrightarrow(\mathbb R\to\mathbb C),\qquad
c\leftrightarrow(\mathbb C\to\mathbb H),\qquad
G\leftrightarrow(\mathbb H\to\mathbb O)
\]
as a conjectural conversion-constant dictionary.

The exact mathematical chain is stronger elsewhere:
- projective inversion in dimension \(d\) gives a unitary half-density;
- Mellin sends inversion to \(z\mapsto d-z\);
- the unitary line is \(\Re z=d/2\);
- dimension doubling is intertwined by \(z\mapsto2z\);
- the eight-real-dimensional endpoint carrier is exactly
  \(M_2(\mathbb C)\cong\mathbb H\oplus\mathbb H\),
  but the octonionic multiplication is not yet derived.

Thus any constants theorem must be built on normalization/representation data, not on the bare statement “there are three doublings.”

## 2. First doubling: \(\hbar\) as phase normalization

The clean statement is not that \(\hbar\) normalizes multiplicative Haar measure.

Pontryagin duality gives
\[
\widehat{\mathbb R/\mathbb Z}\cong\mathbb Z,
\qquad
\chi_n(x)=e^{2\pi i n x}.
\]

Quantum evolution is
\[
U(t)=e^{-iEt/\hbar}.
\]

Writing \(x=\nu t\) and matching the canonical circle character gives
\[
\frac{Et}{\hbar}=2\pi\nu t,
\]
hence
\[
E=h\nu,\qquad h=2\pi\hbar.
\]

So the first doubling can plausibly explain the **role** of \(\hbar\):
it is the conversion from an additive translation generator to a \(U(1)\) phase.
The factor \(2\pi\) is fixed by the period-one versus angular normalization of
\(\mathbb R/\mathbb Z\). No pure algebra fixes the dimensional magnitude of \(\hbar\).

## 3. Second doubling: \(c\) as causal-coordinate normalization

The Lorentzian Hermitian-matrix realization has
\[
X=x^0 I+\vec x\cdot\vec\sigma,
\qquad
\det X=(x^0)^2-|\vec x|^2.
\]

If laboratory time is \(t\), then \(x^0=ct\), so
\[
\det X=c^2t^2-r^2.
\]

Thus \(c\) is the conversion factor needed to put the temporal and spatial
coordinates into one quaternionic/spinorial norm. The geometry can select a
universal null cone and therefore a universal invariant speed; its numerical
value in metres per second is unit convention, not an algebraic invariant.

## 4. Third doubling: replace the old “nonassociativity gives \(G\)” claim

The old idea that octonionic nonassociativity by itself forces Einstein curvature
is not established.

The entanglement-equilibrium paper supplies a much more precise target. With
dimensionless entropy and \(c=1\),
\[
G=\frac{1}{4\hbar\eta},
\]
where \(\eta\) is the universal vacuum-entanglement entropy density multiplying
area. Restoring \(c\),
\[
\boxed{
\eta=\frac{c^3}{4G\hbar},
\qquad
G=\frac{c^3}{4\hbar\eta}.
}
\]

Therefore a genuine \(\mathbb H\to\mathbb O\) derivation of \(G\) should not
try to obtain \(G\) directly from nonassociativity. It should derive the
endpoint entanglement-area normalization \(\eta\). If the final doubling fixes
\(\eta\), then \(G\) follows once the first two conversion constants have been
identified.

This is a concrete theorem target:
\[
\boxed{
\mathbb H\to\mathbb O
\quad\Longrightarrow\quad
\eta_{\rm endpoint}
\quad\Longrightarrow\quad
G=\frac{c^3}{4\hbar\eta_{\rm endpoint}}.
}
\]

## 5. New exact modular identity linking the celestial and causal-diamond papers

The celestial modular spectral weight is
\[
P(\lambda)=\frac{\pi\lambda}{\sinh(\pi\lambda)}.
\]

The causal-diamond/Kontorovich–Lebedev Plancherel density is
\[
\rho_{\rm KL}(\lambda)
=
\frac{2}{\pi^2}\lambda\sinh(\pi\lambda),
\]
and the radial boost operator has eigenvalue \(\lambda^2\).

Therefore, with the same boost/principal-series normalization of \(\lambda\),
\[
\boxed{
\rho_{\rm KL}(\lambda)P(\lambda)
=
\frac{2}{\pi}\lambda^2.
}
\]

Equivalently,
\[
\boxed{
P(\lambda)
=
\frac{2}{\pi}\,
\frac{\lambda^2}{\rho_{\rm KL}(\lambda)}.
}
\]

So the celestial unitarity-cut thermal weight is the Casimir eigenvalue times the
reciprocal causal-diamond Plancherel density, up to the fixed factor \(2/\pi\).
The hyperbolic thermal factors cancel exactly.

This is a genuine algebraic bridge between:
- celestial principal-series phase space,
- Bisognano–Wichmann modular thermality,
- causal-diamond boost harmonic analysis,
- and the entanglement-equilibrium normalization problem.

It does **not** yet determine \(\eta\); a naive integral of the resulting
\(\lambda^2\) density is UV divergent. The research target is to identify the
correct endpoint/area renormalization or relative-entropy subtraction that
turns this spectral pairing into the universal finite area density.

## 6. Unified normalization picture

The sharpened program is therefore

\[
\boxed{
\begin{array}{rcl}
\mathbb R\to\mathbb C
&:&
\text{translation}\to U(1)\text{ phase},
\quad \hbar,\ 2\pi,\\[2mm]
\mathbb C\to\mathbb H
&:&
\text{time}\to\text{Lorentzian spacetime norm},
\quad c,\\[2mm]
\mathbb H\to\mathbb O
&:&
\text{geometric area}\to\text{entanglement density},
\quad \eta\to G.
\end{array}}
\]

The first two constants are kinematic conversion scales. The third is dynamical
and should be derived through the universal entanglement-area density, not asserted
from octonionic nonassociativity.

The strongest possible claim at present is therefore:

> the three doublings plausibly supply three distinct normalization slots, and
> existing modular/entanglement results identify the mathematical job each slot
> must perform; the numerical dimensional values are not yet derived from the
> doubling algebra itself.
