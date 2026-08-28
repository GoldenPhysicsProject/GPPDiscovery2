# Arithmetic Field Theory: reconstruction core

Date: 2026-08-28

## Purpose

This note turns the older Shadow/Haar/OS ideas into a single constructive program called **Arithmetic Field Theory (AFT)**. The aim is not to rename Weil positivity or Hilbert--Polya. The aim is to construct an arithmetic Euclidean field theory from prime/local/adelic data, prove its reflection positivity independently, and then apply the Osterwalder--Schrader reconstruction mechanism.

The logical order is

\[
\text{prime + Archimedean Euclidean data}
\to
\text{AFT Schwinger hierarchy}
\to
\text{reflection positivity}
\to
\mathcal H_{\rm AFT}
\to
H_{\rm AFT}\ge 0
\to
\text{explicit-formula spectral identification}.
\]

Only the last identification can turn this into an RH proof. Positivity may not be imported from Weil's criterion, because that would be circular.

## 1. Primitive geometry

The base scale space is the multiplicative line

\[
X=\mathbb R_+^\times,
\qquad d^\times x=\frac{dx}{x}.
\]

Write

\[
t=\log x.
\]

Then the Shadow Principle's scale inversion is literally Euclidean time reflection:

\[
\Theta:x\mapsto x^{-1}
\quad\Longleftrightarrow\quad
\vartheta:t\mapsto -t.
\]

In the half-density Mellin normalization,

\[
\mathcal M_{1/2}f(s)
=\int_0^\infty f(x)x^{s-1/2}\,\frac{dx}{x},
\]

and for the anti-linear reflection

\[
(\Theta f)(x)=\overline{f(x^{-1})},
\]

direct substitution gives

\[
\boxed{\mathcal M_{1/2}(\Theta f)(s)
=\overline{\mathcal M_{1/2}f(1-\bar s)}}.
\]

Thus the spectral OS reflection is

\[
\boxed{s\mapsto1-\bar s},
\]

whose fixed locus is exactly

\[
\boxed{\Re s=\tfrac12}.
\]

Under the Shadow normalization \(\Delta=2s\), this becomes

\[
\Delta\mapsto2-\bar\Delta.
\]

This is the same involutive spine already isolated in Shadow Principle v2; AFT now adds the Euclidean positivity/reconstruction layer.

## 2. Positive-time algebra

The OS positive-time region \(t>0\) is

\[
\boxed{x>1}.
\]

Let \(\mathcal A_+\) be an algebra of admissible arithmetic observables supported in \(x>1\) (equivalently positive logarithmic time). Let \(\Omega_{\rm AFT}\) be an arithmetic Euclidean state constructed from local data. Define

\[
\boxed{
\langle F,G\rangle_{\rm AFT}
=\Omega_{\rm AFT}\bigl((\Theta F)^*G\bigr).
}
\]

The decisive AFT axiom/theorem is

\[
\boxed{
\Omega_{\rm AFT}\bigl((\Theta F)^*F\bigr)\ge0,
\qquad F\in\mathcal A_+.
}
\]

If this is derived from prime/local geometry, not from the zeros, it is the arithmetic analogue of the OS positivity theorem.

## 3. Arithmetic Schwinger hierarchy

AFT should possess a hierarchy \(A_n\) playing the role of Euclidean Schwinger functions. The first working axiom package is:

- **A0 regularity/growth.** Uniform hierarchy-wide growth sufficient for Mellin continuation and OS reconstruction. This must follow the corrected 1975 Osterwalder--Schrader architecture, not only fixed-\(n\) bounds.
- **A1 scale covariance.** Simultaneous multiplication \(x_j\mapsto e^a x_j\), equivalently translation \(t_j\mapsto t_j+a\).
- **A2 arithmetic reflection positivity.** The reflected positive-time quadratic form is nonnegative.
- **A3 symmetry.** Permutation symmetry, or the appropriate graded/character-valued replacement.
- **A4 clustering.** Factorization at large logarithmic separation, giving a unique vacuum-like cyclic sector.

Assuming the corrected regularity hypotheses and A0--A4, the literal OS steps are:

1. quotient \(\mathcal A_+\) by the null space of the reflected seminorm;
2. complete to \(\mathcal H_{\rm AFT}\);
3. descend positive logarithmic translations to a contraction semigroup;
4. obtain a nonnegative self-adjoint generator \(H_{\rm AFT}\);
5. analytically continue to unitary Lorentzian scale evolution.

## 4. The zero-independent arithmetic two-point candidate

The older arithmetic principal-series program already produced a zero-independent completed prime--Archimedean heat trace

\[
\mathscr K(t)
=\frac1{\sqrt{4\pi t}}
\left\langle\mathcal W,e^{-x^2/(4t)}\right\rangle,
\qquad t>0,
\]

with \(\mathcal W\) built from the real place and the prime-power measure. The natural AFT Euclidean two-point function is

\[
\boxed{C(\tau)=\mathscr K(|\tau|)}.
\]

For positive times \(t_i\), the OS matrix is

\[
\boxed{G_{ij}=\mathscr K(t_i+t_j)}.
\]

The older work proves that positivity of all such matrices is equivalent to RH. Therefore AFT must **derive** this positivity from a more primitive local state/channel. The equivalence is a target diagnostic, not an input axiom.

## 5. Free-field template and the exact missing factorization

For an ordinary free Euclidean field, reflection positivity is exposed by a square-integral factorization

\[
C(\theta f,f)
=\int |\mathcal L f(\lambda)|^2\,d\mu(\lambda),
\qquad d\mu\ge0.
\]

The AFT target is therefore

\[
\boxed{
\langle\mathcal W,f*\widetilde f\rangle
=\int |\mathcal L_{\rm AFT}f(\lambda)|^2\,d\mu_{\rm AFT}(\lambda)
}
\]

for the Gaussian-semigroup test algebra first, then a dense admissible class.

This is the precise noncircular theorem still missing.

## 6. New Archimedean positivity clue from the Fisher/Gamma bridge

The causal-diamond Fisher calculation gives the Bisognano--Wichmann/Kubo--Mori response

\[
\kappa_{2\pi}(\lambda)
=\frac{\pi\lambda}{\sinh(\pi\lambda)}
=|\Gamma(1+i\lambda)|^2.
\]

A further exact identity makes its positivity structure explicit:

\[
\boxed{
\int_{-\infty}^{\infty}\operatorname{sech}^2u\,
 e^{-2i\lambda u}\,du
=\frac{2\pi\lambda}{\sinh(\pi\lambda)}.
}
\]

Hence

\[
\boxed{
\kappa_{2\pi}(\lambda)
=\frac12\int_{-\infty}^{\infty}
\operatorname{sech}^2u\,e^{-2i\lambda u}\,du.
}
\]

Because \(\tfrac12\operatorname{sech}^2u\,du\) is a positive measure, Bochner's theorem shows that \(\kappa_{2\pi}\) is a positive-definite function of the principal-series frequency. This gives an explicit Gram/positive-measure realization of the **Archimedean** AFT kernel.

This is stronger than merely knowing \(\kappa_{2\pi}(\lambda)>0\) pointwise: positive definiteness is the structure reflection positivity actually needs.

The KL Plancherel density satisfies

\[
\rho_{\rm KL}(\lambda)
=\frac{2}{\pi^2}\lambda\sinh(\pi\lambda),
\]

so the exact cancellation

\[
\boxed{
\rho_{\rm KL}(\lambda)\kappa_{2\pi}(\lambda)
=\frac{2}{\pi}\lambda^2
}
\]

shows that the Archimedean Plancherel phase space times the modular/Fisher response becomes a flat manifestly nonnegative quadratic spectral weight.

Interpretation: the real-place Gamma factor has the exact form of a modular response kernel whose combination with the natural boost Plancherel measure removes the hyperbolic Jacobian. This is a concrete candidate for the Archimedean leg of the AFT reflection-positive factorization.

## 7. Local-to-global construction target

The next object to construct is a local tensor/product state

\[
\Omega_{\rm AFT}
\sim
\Omega_\infty\widehat\otimes\prod_p'\Omega_p
\]

with:

- \(\Omega_\infty\) represented by the Gamma/Fisher positive kernel above;
- each \(\Omega_p\) represented by a positive transfer kernel encoding the local Euler factor / prime-power ladder;
- a controlled adelic/gluing limit producing the completed explicit-formula state.

The difficult point is not positivity of isolated Euler coefficients; it is preservation of reflection positivity through the global completion/subtraction that couples the prime and Archimedean sectors.

The desired theorem is a completely positive/reflection-positive gluing map

\[
\boxed{
\mathfrak L:\mathcal G_+\to\mathcal A_+
}
\]

such that

\[
\boxed{
q_{\mathcal W}(f,g)
=\Omega_{\rm AFT}\bigl(\Theta(\mathfrak Lf)\,\mathfrak Lg\bigr).
}
\]

This is the sharpened form of the older arithmetic--physical reflection functor problem.

## 8. Relation to the older Shadow/Yang--Mills/string observations

The older papers supply three structural inputs that now fit naturally:

1. **Shadow Principle v2:** inversion, Mellin reflection, celestial shadow, Grassmannian complement, and boundary time reversal are transported forms of one involution.
2. **Yang--Mills construction:** positive boundary representation theory + inverse Mellin + shadow/reflection bridge + OS reconstruction is the correct constructive architecture. AFT should reproduce this architecture arithmetically, not merely imitate its vocabulary.
3. **Why String Theory Works / Haar-Gamma observation:** Gamma/Beta amplitudes are Mellin-Haar objects. The new Fisher identity upgrades this observation: the same Gamma modulus is a positive modular/KMS response kernel.

Thus the emerging common pattern is

\[
\boxed{
\text{Haar measure}
+\text{shadow involution}
+\text{positive representation/local state}
+\text{OS reconstruction}.
}
\]

## 9. RH endpoint and non-circularity firewall

AFT proves RH only if all of the following are obtained independently of zero locations:

1. a genuine arithmetic Euclidean state/hierarchy from prime + Archimedean data;
2. A0--A4, especially reflection positivity;
3. OS reconstruction giving \(H_{\rm AFT}\ge0\);
4. an exact trace/resolvent/determinant identification showing that the nontrivial zeta zeros are spectral points of the reconstructed self-adjoint arithmetic generator.

Then self-adjointness would force the spectral parameter to be real, corresponding to

\[
s=\frac12+i\gamma,
\qquad \gamma\in\mathbb R.
\]

Until step 4 is proved, AFT is a constructive program, not an RH proof.

## Immediate formalization targets

- formalize the reflection involution and critical-line fixed locus (already present in `ArithmeticOSReflection.lean`);
- formalize finite Gram positivity for rank-one heat-semigroup spectral atoms;
- extend to finite positive spectral measures;
- formalize the sech-squared Fourier/Gamma identity when Mathlib support allows;
- define positive-time arithmetic test algebra and semigroup translation;
- formalize null quotient / contraction-semigroup skeleton abstractly;
- attack p-adic/local Euler transfer kernels and search for a completely positive gluing theorem.
