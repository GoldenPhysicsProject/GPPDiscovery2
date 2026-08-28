# Arithmetic Field Theory: audit of earlier RH/CFT/unitarity/positivity ideas

Codex/GPT synthesis, 2026-08-28.

This note integrates the older manuscripts `rh_arithmetic_field.tex`, `rh_cft_proof.tex`, `haar_positivity_weil_wightman.tex`, and `arithmetic_principal_series_RH_program-26.tex` into the present Arithmetic Field Theory (AFT) program.

## 1. What survives exactly

Several old ideas are mathematically sound and should be retained as AFT structure.

### Multiplicative Euclidean time

Use

\[
t=\log r,
\qquad r\in\mathbb R_+^\times.
\]

Then inversion is Euclidean reflection:

\[
r\mapsto r^{-1}
\quad\Longleftrightarrow\quad
t\mapsto-t.
\]

With the half-density Mellin convention, reflection is transported to

\[
s\mapsto1-\overline s,
\]

whose fixed locus is the critical line.

### Haar-positive squares

For a unimodular group,

\[
P=\Omega^\vee*\Omega,
\qquad
\Omega^\vee(g)=\overline{\Omega(g^{-1})},
\]

is of positive type. This is the common abstract spine behind GNS, Wightman positivity, OS reflection positivity, and Weil's convolution-square criterion.

### Arithmetic OS heat kernel

The strongest later construction defines the zero-independent completed prime--Archimedean heat trace

\[
\mathscr K(t)=\frac1{\sqrt{4\pi t}}\langle\mathcal W,e^{-(\cdot)^2/(4t)}\rangle.
\]

The finite kernel

\[
G_{ij}=\mathscr K(t_i+t_j)
\]

is exactly an OS reflected kernel on positive Euclidean time. Positivity of all such finite matrices is equivalent to RH. Under RH,

\[
\mathscr K(t)=\sum_{\gamma>0}m_\gamma e^{-\gamma^2t},
\]

so OS reconstruction yields a positive Hamiltonian with spectral measure

\[
\mu_H=\sum_{\gamma>0}m_\gamma\delta_{\gamma^2}.
\]

This is the cleanest AFT target presently available.

### Exact Gaussian Weil identity

For

\[
g_t(x)=\frac{e^{-x^2/(4t)}}{\sqrt{4\pi t}},
\qquad g_s*g_t=g_{s+t},
\]

and

\[
f_c=\sum_jc_jg_{t_j},
\]

one has

\[
\boxed{c^*Gc=\langle\mathcal W,f_c*\widetilde f_c\rangle.}
\]

Thus the AFT OS form is literally the Weil form restricted to the heat-semigroup subspace.

### Causal-diamond Fisher prototype

The current project adds the exact physical model

\[
\rho_{\rm KL}(\lambda)\,\kappa_{2\pi}(\lambda)
=\frac{2}{\pi}\lambda^2,
\]

with

\[
\kappa_{2\pi}(\lambda)=|\Gamma(1+i\lambda)|^2.
\]

This supplies an unconditional example in which modular/KMS reflection data and Plancherel measure combine to produce a manifestly positive polynomial spectral density. AFT should search for the arithmetic analogue of this factorization.

## 2. What must be retired

The old `rh_cft_proof.tex` and `rh_arithmetic_field.tex` multiplicity proof is not valid as stated.

The problematic inference is

\[
\text{Plancherel multiplicity }1
\Longrightarrow
\text{zero multiplicity at an ordinate }=1.
\]

For \(L^2(\mathbb R,du)\), the plane waves \(e^{i\gamma u}\) are generalized eigenfunctions in continuous spectrum, not ordinary \(L^2\) eigenvectors. Plancherel multiplicity one means the direct-integral fiber has dimension one almost everywhere; it does not imply that a regularized explicit-formula atom at a particular ordinate equals an eigenspace dimension. The later principal-series manuscript correctly moved away from this shortcut.

Likewise, ordinary boundary unitarity is insufficient. A positive/self-adjoint quantum system can have off-axis zeros of a complex-source partition function. Therefore

\[
\text{self-adjointness alone}\not\Rightarrow\text{RH}.
\]

The later program already contains an explicit finite-dimensional counterexample and correctly identifies OS positivity as strictly stronger than boundary unimodularity or Krein self-adjointness.

## 3. The actual AFT theorem to prove

The correct noncircular target is not "unitarity of the arithmetic field" by itself. It is an arithmetic OS reconstruction theorem derived from prime/local data.

Construct a positive-time algebra \(\mathcal A_+^{\rm AFT}\), reflection \(\Theta\), and Euclidean vacuum functional \(\omega_{\rm AFT}\) from primes, the Archimedean place, and adelic/Haar structure, without using zero locations, such that

\[
\omega_{\rm AFT}(\Theta F\,F)\ge0
\qquad(F\in\mathcal A_+^{\rm AFT}),
\]

and such that the induced two-point function agrees with the completed arithmetic heat kernel:

\[
\omega_{\rm AFT}(\Theta\mathfrak L(g_s)\,\mathfrak L(g_t))
=\mathscr K(s+t).
\]

Equivalently, construct the reflection functor

\[
\mathfrak L:\mathcal G_+\to\mathcal A_+^{\rm AFT}
\]

satisfying

\[
\boxed{
q_{\mathcal W}(f,g)
=\omega_{\rm AFT}(\Theta\mathfrak Lf\,\mathfrak Lg)
}
\]

with dense reflected image and semigroup intertwining.

If this is achieved independently, ordinary OS reconstruction gives a positive Hamiltonian and the established equivalence gives RH.

## 4. Strongest existing zero-independent arithmetic object

The later principal-series program already isolates the exact prime--Archimedean distribution \(\mathcal W\) and heat trace \(\mathscr K\). Scalar positivity is unconditional in the associated massive-resolvent function, but the unresolved property is the full Stieltjes/Pick/OS hierarchy.

This is useful because the unknown theorem has been compressed to

\[
\boxed{
[\mathscr K(t_i+t_j)]_{i,j}\succeq0
\quad\forall\,N,\ t_i>0.
}
\]

There is also a one-sequence compression via two incommensurable heat grids, yielding a Hausdorff moment criterion and an equivalent positive-contraction target

\[
b_n=\langle v,T^nv\rangle,
\qquad0\le T\le I.
\]

These are exact reformulations, not proofs, but they give highly concrete AFT reconstruction targets.

## 5. New synthesis with current Fisher/OS program

The present project suggests the following physics-to-number-theory route:

1. In the causal diamond, identify the positive modular kernel and Plancherel density whose product becomes a flat positive quadratic measure.
2. Translate the same modular/half-density mechanism to the multiplicative/adelic setting.
3. Determine whether the completed Archimedean Gamma factor is the AFT KMS/reflection kernel.
4. Factor the prime--Archimedean heat kernel through a genuine positive Hilbert-space norm or positive transfer semigroup.
5. Prove the arithmetic OS form from that factorization, not from the zero expansion.

The number-theory-to-physics reverse direction is equally important: the explicit formula says the physical theory cannot be merely local/free. The prime powers are discrete logarithmic lengths and the Archimedean term is a continuous counter-density of matching asymptotic strength. AFT should therefore look like a nonlocal Euclidean boundary theory or a positive Hilbert complex whose exact/coexact sectors cancel and whose physical cohomology is positive.

## 6. Main obstruction

The old program already found that several tempting local constructions fail:

- boundary unitarity is too weak;
- raw Wick rotation does not generate the missing positivity;
- the natural fractional radial kernel is conditionally negative before subtraction;
- a fixed local Gamma/Mellin completion has an indefinite interval;
- finite dilation dynamics do not close the global prime--Archimedean positivity problem.

Therefore the likely missing AFT axiom is genuinely global: a no-ghost/Hodge/cohomological positivity statement, or an OS-positive transfer construction that couples all primes to the Archimedean place at once.

This is now the first-class RH/AFT frontier.
