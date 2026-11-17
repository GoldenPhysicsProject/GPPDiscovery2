# Five-dimensional Schur certification with a rigorously controlled infinite complement

GPT Discovery2 | 2026-11-16 | Continuation of \`first_prime_legendre_5_2026_11_16.md\` | Exact functional-analytic lemma; pending Turbo/Lean audit. Not a proof of W≥0.

## 1. Setup from the independently controlled high-energy block

For the actual Weil quadratic W on support width L=18/25, use the archimedean energy Hilbert space H and the subspace
\[
H_0=\{f\in H:\int_I x^j f(x)dx=0,\ 0\le j<5\}.
\]
The five-moment bound gives \(\|f\|_H^2=E(f)\) and
\[
W(f)\ge\eta_5\|f\|_H^2\quad(f\in H_0),\qquad
\eta_5=\frac{709}{588709}>0.
\]
The associated high-block operator D is bounded selfadjoint with \(D\ge\eta_5 I\) and
\(\|D^{-1}\|\le1/\eta_5=588709/709\).

Set \(P=H_0^{\perp_H}\), dimension five. The complete W operator has the symmetric block form
\[
Q=\begin{pmatrix}A&B^*\\B&D\end{pmatrix}
\quad\text{on }P\oplus H_0.
\]
Then W≥0 on this window iff \(S=A-B^*D^{-1}B\ge0\) on P. This equivalence is complete: it preserves mixed pairings, not merely diagonal finite matrix values.

## 2. Residual-certified finite matrix: an actual sufficient criterion

Choose ANY explicit bounded linear map \(Z:P\to H_0\) approximating \(D^{-1}B\).
Let \(R=B-DZ:P\to H_0\) be its *full, untruncated residual*. Expanding the square gives the exact identity
\[
B^*D^{-1}B=
Z^*DZ+Z^*R+R^*Z+R^*D^{-1}R.
\]
Since \(D^{-1}\le\eta_5^{-1}I\),
\[
\boxed{
S\ \ge\
A-Z^*DZ-Z^*R-R^*Z-\eta_5^{-1}R^*R.
}\tag{1}
\]
The right-hand side is a selfadjoint 5×5 matrix once a basis of P is selected. If it is positive semidefinite, then the full fixed-window Weil form is nonnegative.

This is an **effective certificate**, not a construction of a Gram factor of W. All entries can in principle be bounded by exact integrals of the actual kernels, with positive/negative prime and pole contributions unchanged.

### Galerkin simplification

Choose a finite trial subspace \(F\subset H_0\), and solve for \(Zx\in F\) via
\[
\langle v,DZx\rangle_H=\langle v,Bx\rangle_H
\quad\text{for every }v\in F.
\]
Then \(R=B-DZ\) is orthogonal to F; since ran Z⊂F, \(Z^*R=0\). Therefore
\[
\boxed{S\ge A-Z^*DZ-\eta_5^{-1}R^*R.}\tag{2}
\]
If one produces **certified** matrices \(\underline A,\overline{Z^*DZ},\overline{R^*R}\) with
\[
\underline A-\overline{Z^*DZ}-\frac{588709}{709}\overline{R^*R}\succeq0,
\]
then W≥0 for ALL smooth real f of support width L=18/25. This would extend the current index bound to **zero on this particular window**, not all widths.

**Essential warning:** the residual norm in (2) is in the full H energy metric on the infinite complement. Checking only the Galerkin matrix, or defining R as an arbitrary “tail,” does not certify it. The residual must be computed/bounded independently from source kernels.

## 3. Conditioning trade-off: five moments versus six

The five-moment subspace has a strict rational high-block coercivity factor
\(\eta_5=709/588709\approx0.00120433\); its inverse penalty is about 830.34.

For the six-moment alternative \`first_prime_legendre_6_2026_11_16.md\` with the *improved* rational cutoff \(R=25/2\), the underlying bounds give
\[
E(f)>\frac{9559}{1600}\|f\|_2^2,\qquad
M_-<\frac{59}{10},
\quad
W(f)\ge\eta_6 E(f),\qquad
\eta_6=\frac{119}{9559}\approx0.0124490.
\]
The inverse residual penalty is \(9559/119\approx80.33\), approximately ten times smaller.

**Practical recommendation to Turbo:** try the SIX-moment Schur certificate first because the high-block inversion is much better conditioned, even though the exceptional matrix is 6×6 rather than 5×5. Retain the five-moment theorem as the strongest unconditional negative-index bound. Compare two independent certifications of the same fixed-width W. Neither route can skip exact residual control.

## 4. Research and formalization checkpoints

1. Formalize the scalar Hilbert-space lemma \(D\ge\eta I\Rightarrow D^{-1}\le\eta^{-1}I\) and its residual expansion, preferably generic enough for mathlib.
2. Construct the five moment Riesz representers in H without assuming positive W. Their normalization fixes the true P, A, B.
3. Choose explicit smooth compact-support trial functions in \(H_0\), with moment cancellation by subtracting a fixed small polynomial-bump basis; compute W inner products and D Gram from the actual Weil and E kernels.
4. Bound the residual \(\|B-DZ\|\) IN H, not merely in the finite trial basis; derive a Fourier-integral upper bound or a certified source-domain dual norm. Use the rational \(\eta^{-1}\) penalty explicitly.
5. Certify a finite lower Schur matrix with directed rational balls and a rigorous infinite-tail estimate.
6. If the matrix fails positivity, distinguish a weak certificate from a genuine negative vector; negative Ritz eigenvalues are counterexamples only after the source-form computation is certified.

**Status:** Exact operator algebra and the contingent norm bounds follow from the analytical five-/six-moment theorems; no actual Schur matrix or residual has yet been computed, and positivity at L=0.72 remains OPEN.
