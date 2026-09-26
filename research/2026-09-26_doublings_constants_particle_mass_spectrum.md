# From doubling normalizations to particle spectrum: a unified constants-and-masses target

Date: 2026-09-26
Status: synthesis of exact project results plus a new spectral/heat-kernel research target. No claim that the Standard Model spectrum or all masses have been derived.

## 1. Separate three different questions

A viable unification must not mix:

1. **unit-conversion constants**: \(\hbar,c,G\) in a chosen dimensional presentation;
2. **dimensionless couplings and ratios**: \(\alpha,\sin^2\theta_W,y_f,\lambda_H,\theta_{ij},\delta_{\rm CKM},\dots\);
3. **dynamically generated scales**: Higgs \(v\), \(\Lambda_{\rm QCD}\), neutrino/seesaw scales, cosmological \(\Lambda\).

The current Holographic Chain mathematics supports at most a structural assignment of normalization jobs to the three division-algebra doublings. It does not make every dimensionful scale a unit convention.

## 2. Corrected three-doubling dictionary

### \(\mathbb R\to\mathbb C\): quantum phase

Pontryagin duality gives
\[
\widehat{\mathbb R/\mathbb Z}\cong\mathbb Z,
\qquad
\chi_n(x)=e^{2\pi i n x}.
\]
Quantum time evolution is
\[
U(t)=e^{-iEt/\hbar}.
\]
Matching a period-one phase \(x=\nu t\) gives
\[
E=h\nu,\qquad h=2\pi\hbar.
\]

So \(\hbar\) is best viewed as the conversion between an additive translation generator and angular quantum phase. The factor \(2\pi\) is the period-one/angular normalization.

### \(\mathbb C\to\mathbb H\): causal spacetime norm

For the Hermitian-matrix representation
\[
X=x^0I+\vec x\cdot\vec\sigma,
\]
\[
\det X=(x^0)^2-|\vec x|^2.
\]
Writing \(x^0=ct\) makes
\[
\det X=c^2t^2-r^2.
\]
Thus \(c\) converts laboratory time and length coordinates inside one Lorentzian norm.

### \(\mathbb H\to\mathbb O\): gravitational entanglement normalization

The old claim “octonionic nonassociativity forces curvature and therefore \(G\)” is not established.

Entanglement equilibrium gives the sharper relation
\[
\eta=\frac{c^3}{4G\hbar},
\qquad
G=\frac{c^3}{4\hbar\eta},
\]
where \(\eta\) is the universal area density of vacuum entanglement.

Therefore the third doubling target should be:
\[
\boxed{
\mathbb H\to\mathbb O
\Longrightarrow
\eta_{\rm endpoint}
\Longrightarrow
G.
}
\]

The missing theorem is a derivation of the universal renormalized area density from the endpoint modular/Grassmannian theory.

## 3. Other dimensional constants are not independent doublings

- \(k_B\) converts temperature to energy. If temperature is measured in energy units, \(k_B=1\); it is not evidence for a fourth algebraic doubling.
- Electric charge \(e\) in SI is not the invariant quantity; the physical target is the dimensionless \(\alpha\).
- \(\epsilon_0,\mu_0\) depend on electromagnetic unit conventions.
- \(G_F\) is set by the Higgs scale, \(G_F\sim v^{-2}\) at tree level.
- Planck units follow from \(\hbar,c,G\).
- The physically meaningful hierarchy question is therefore \(v/M_{\rm Pl}\), \(\Lambda_{\rm QCD}/M_{\rm Pl}\), \(m_f/v\), etc.
- The cosmological constant is special: the volume-constraint paper shows that local entanglement equilibrium is blind to its identity/trivial-representation direction, so its value must come from global state/boundary selection rather than the local stationarity principle.

## 4. Three layers of the particle-spectrum problem

The observed spectrum should be separated into:

### A. Species and charges

These should come from representation theory of the internal algebra/gauge group.

### B. Multiplicity

Why three generations is an index/anomaly/topology question, not a mass question. Triality supplies a threefold structure but by itself does not prove three Standard Model generations. Any claimed derivation must identify the actual three chiral modules and exclude a fourth.

### C. Masses and mixings

After electroweak breaking,
\[
m_{f,j}=\frac{v}{\sqrt2}\,\sigma_j(Y_f),
\]
where \(\sigma_j\) are singular values of the Yukawa matrix. Therefore the real mass problem is to derive \(Y_f\) and the scale \(v\).

## 5. New bridge: the failed linear Casimir mass law and the successful Gaussian ansatz are dual heat-kernel pictures

The latest Decoding Reality correctly excludes the direct identification
\[
m_d:m_s:m_b=2:5:9
\]
from the exact Casimir ratios. The exact algebraic ratios survive, but they are not the physical quark masses.

There is a natural reason this direct identification can fail while Casimirs still control flavour.

For a compact homogeneous internal geometry \(X=G/H\), the heat kernel has the spectral expansion
\[
\boxed{
K_t(x,y)
=
\sum_{\pi\in\widehat G_H}
d_\pi\,e^{-t\lambda_\pi}\,
\Phi_\pi(x,y),
}
\]
where the Laplace eigenvalues \(\lambda_\pi\) are Casimir eigenvalues (or Casimir differences for associated bundles).

At short time,
\[
\boxed{
K_t(x,y)
\sim
(4\pi t)^{-d/2}
e^{-d(x,y)^2/(4t)}
\Delta_{\rm VM}^{1/2}(x,y)
\left(1+a_1t+a_2t^2+\cdots\right).
}
\]

Therefore:

- **representation space:** Casimirs enter exponentially as \(e^{-tC_2}\);
- **position space:** the same operator is a Gaussian in geodesic distance.

This is exactly the structural relation the project has been missing.

The phenomenological ansatz
\[
y_j\propto e^{-\kappa d_j^2}
\]
is therefore not naturally paired with \(m_j\propto C_2(j)\). It is naturally paired with a heat operator
\[
\boxed{
Y_f \sim e^{-t\Delta_X},
}
\]
whose eigenvalues are exponential functions of Casimirs.

This explains why a **linear Casimir mass formula can fail by a large factor while Casimir geometry can still govern the hierarchy**.

## 6. A concrete mass-operator target

Let \(P_{L,f}\) and \(P_{R,f}\) select the left- and right-handed zero-mode subspaces for one fermion sector, and let \(x_H\) encode the Higgs vacuum/holonomy.

Define
\[
\boxed{
Y_f(t,x_H)
=
P_{L,f}\,K_t(x_H)\,P_{R,f}.
}
\]

Then
\[
M_f=\frac{v}{\sqrt2}Y_f,
\]
and the physical masses are the singular values of \(M_f\).

This architecture explains, in principle:

- exponential mass hierarchies from heat propagation;
- mixings from non-coincident eigenbases of \(Y_u\) and \(Y_d\);
- sector dependence through bundle representation and Casimir;
- three generations through the dimension/index of the zero-mode subspace rather than through hand-selected three points.

The next theorem must derive \(P_{L/R,f}\), \(x_H\), and \(t\) from the same geometry instead of fitting them.

## 7. Why rational angles are plausible but not yet derived

The fitted/proposed flavour angles in the project are rational multiples of \(\pi\). A non-numerological mechanism would be:

1. the Higgs vacuum is a finite-order holonomy/torsion element of a compact maximal torus;
2. finite-order holonomies have eigenphases that are rational multiples of \(2\pi\);
3. the vacuum is selected as an extremum of a Weyl-invariant spectral determinant or heat-kernel potential.

A candidate potential has the character form
\[
V(U)
=
\sum_{\pi} A_\pi e^{-tC_2(\pi)}\chi_\pi(U),
\]
or an adelically completed analogue.

This is the right way to derive rational angles: as torsion/critical points of a canonical potential, not by fitting rational numbers after the fact.

## 8. Adelic completion of the Yukawa operator

The AFT program suggests a stronger version:
\[
\boxed{
Y_f
=
Y_{\infty,f}
\prod_p Y_{p,f},
}
\]
where

- \(Y_{\infty,f}\) is the Archimedean geometric/heat-kernel factor;
- \(Y_{p,f}\) are finite-place local matrix coefficients/intertwiners;
- the product is understood in a completed adelic sense.

Then
\[
\log Y_f
=
\log Y_{\infty,f}
+
\sum_p\log Y_{p,f},
\]
so enormous mass hierarchies can arise from modest local arithmetic data.

This makes the Decoding Reality hypothesis “dimensionless constants are arithmetic invariants” precise enough to test: each physical Yukawa should be a global adelic matrix coefficient or period with specified local factors.

## 9. Where the other Standard Model constants should live

### Weak mixing
The exact tree-level relation
\[
\sin^2\theta_W=\frac38
\]
is a normalization ratio of gauge generators. The project has several exact occurrences of \(3/8\), but the latest Holographic Chain correctly says their common division-algebra origin is not yet proved.

### Fine structure
The old CKM/\(\alpha\) numerical relation should stay discarded. A viable derivation of \(\alpha\) should instead come from the coefficient of the \(U(1)\) gauge kinetic term in the same internal spectral action or adelic period.

### Strong coupling and \(\Lambda_{\rm QCD}\)
The dimensionless UV coupling \(g_s\) belongs to the gauge kinetic normalization. The hadronic mass scale then arises by dimensional transmutation. Thus most proton/hadron mass should not be fitted as a fundamental Yukawa mass.

### Higgs scale and quartic
The hierarchy \(v/M_{\rm Pl}\) and the quartic \(\lambda_H\) should arise from the endpoint effective potential/spectral action. Without these, absolute Standard Model masses are not yet derived.

### Neutrinos
The exact shadow-odd \(2\oplus1\) low-energy Majorana ansatz is already ruled out because it gives \((m,m,0)\). Any viable shadow mechanism must act at a pre-effective/seesaw level or be softly broken.

## 10. A single spectral architecture for RH and particles

The current program suggests one common pattern.

For RH:
\[
\text{finite-place channels}
+
\text{Archimedean principal series}
\to
\text{global completed transfer determinant},
\]
whose causal normal modes should give the zeta ordinates.

For particles:
\[
\text{internal representation channels}
+
\text{Higgs/vacuum holonomy}
+
\text{adelic local factors}
\to
\text{global Dirac/Yukawa determinant},
\]
whose singular values/eigenvalues give masses.

So a candidate master principle is:

\[
\boxed{
\text{physical spectra are normal-mode spectra of globally sewn local-to-global operators;}
}
\]

the Riemann zeros live in the scale/arithmetic sector, while particle masses live in gauge/internal representations of the same adelic modular field theory.

The decisive test is construction, not analogy: write the global operator without inputting observed masses or zeros, prove its unitarity/positivity properties, and compare its spectrum.
