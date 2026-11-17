# An unconditional finite-negative-index theorem for the actual Weil form at EVERY finite support width

**2026-11-16, Discovery2.** This is an exact analytic result from prime/gamma/pole coefficients in GPPVerify; no RH, OB-6 or ARP hypothesis. The general compact-resolvent/finite-negative-index observation is standard in pseudodifferential form theory. The **explicit moment-codimension inequality** and a reproducible small-width rational check are the useful formulation for this project. Do NOT present it as new worldwide or as full positivity.

## 1. The source exact form and its positive unbounded archimedean symbol

Take real f∈C_c^infty(I_L), I_L=[−L/2,L/2], extended by zero. Write \(v_n=\Lambda(n)/\sqrt n\), \(V_L=\sum_{\log n<L}v_n\) (finite). The actual sourced Weil form is
\[
 W_L(f)=E(f)+C_\infty\|f\|_2^2
       +2\left(\int_{I_L}f(x)e^{x/2}dx\right)
         \left(\int_{I_L}f(x)e^{-x/2}dx\right)
       -2\sum_{\log n<L}v_n\int f(x)f(x-\log n)dx,
\]
where \(C_\infty=-\gamma-\log\pi-\pi/2-3\log2\) and
\[
 E(f)=\int_0^\infty w(t)\|f-T_tf\|_2^2dt,\quad
 w(t)=e^{-t/2}/(1-e^{-2t}).
\]
Fourier convention \(\hat f(\lambda)=\int f(x)e^{-i\lambda x}dx\) and Plancherel \(||f||²=(2π)^{-1}\int|\hat f|²\). Expanding \(w=\sum_{k\ge0}e^{-(2k+1/2)t}\), using Tonelli for the nonnegative energy, yields
\[
 E(f)=\frac1{2\pi}\int_\mathbb R a(\lambda)|\hat f(\lambda)|² d\lambda,\qquad
 \boxed{a(\lambda)=2\sum_{k\ge0}
   \frac{\lambda²}{(2k+1/2)((2k+1/2)^2+\lambda²)}.}\tag{1}
\]
This is exactly
\[
 a(\lambda)=\Re\big[\psi(\tfrac14+\tfrac{i\lambda}{2})-\psi(\tfrac14)\big].
\]
It is even, nonnegative, increasing in |lambda| and tends to +∞ as |lambda|→∞, because the kth summand increases toward \(2/(2k+1/2)\) and that harmonic series diverges.

For fixed L the remaining terms are bounded quadratic forms:
\[
 \left|2\sum_{\log n<L}v_n A_f(\log n)\right|\le2V_L\|f\|²,
 \qquad
 |\mathrm{Pole}(f)|\le2Le^{L/2}\|f\|².
\]
Define
\[
 \boxed{B(L)=|C_\infty|+2V_L+2Le^{L/2}.}\tag{2}
\]
Then \(W_L(f)\ge E(f)-B(L)\|f\|²\), UNCONDITIONALLY, for every f of this support width.

## 2. All-width finite codimension theorem, with EXPLICIT N(L)

Fix any L>0. Select R>0 with \(a(R)>2B(L)\), possible by (1). Select N∈N with
\[
 \boxed{
 \alpha_N(L,R):=\frac{LR}{\pi}
  \left(\frac{(RL/2)^N}{N!}\right)^2\le\frac12.}\tag{3}
\]
Such N exists for every fixed L and R, by factorial growth.

**THEOREM.** For every nonzero real f∈C_c^infty(I_L) obeying
\[
 \int_{I_L}x^j f(x)dx=0,\quad j=0,\ldots,N-1,
\]
one has
\[
 \boxed{
 W_L(f)\ge [\,a(R)(1-\alpha_N)-B(L)\,]\|f\|²
 \ge [a(R)/2-B(L)]\|f\|²>0.}\tag{4}
\]
In particular the maximal dimension of a subspace on which W_L is negative definite is at most N. This is an unconditional finite-negative-index statement for every finite L, not a statement of positivity on ALL f or any width-uniform finite N.

**PROOF.** For |lambda|≤R, subtract N Taylor terms of \(e^{-i\lambda x}\); their integrals against f vanish by the moments. The integral remainder for the PURELY IMAGINARY exponential satisfies \(|e^{-i\lambda x}-\sum_{j<N}(-i\lambda x)^j/j!|\le(|\lambda x|)^N/N!\), without any unnecessary exponential inflation. Therefore
\[
 |\hat f(\lambda)|\le\int|f(x)|\,\frac{(|\lambda|L/2)^N}{N!}dx
 \le\sqrt L\|f\|\frac{(RL/2)^N}{N!}.
\]
Thus the Fourier mass below R is bounded by \(\alpha_N\|f\|²\). Outside it, a(lambda)≥a(R) by monotonicity. By Plancherel
\[
 E(f)\ge a(R)\int_{|\lambda|>R}|\hat f|²\,d\lambda/(2\pi)
       \ge a(R)(1-\alpha_N)\|f\|².
\]
Subtract the bounded local terms (2) to obtain (4). The moment-zero test subspace has codimension at most N; any negative definite subspace of dimension >N would intersect it nontrivially, contradicting (4). QED.

**Mathematical significance:** This proves the UV side of full Weil positivity is under unconditional control, for each individual finite support window, and converts any possible negative index to finitely many moment directions with an explicit albeit astronomically inefficient bound. It does **not** prove that these remaining directions are nonnegative, nor does it provide a mechanism for N(L) as L→∞. The latter remains the hard RH-strength step. Existing GPPVerify sector certificates at small widths are MUCH sharper than this crude universal bound. Finite negative index is weaker than a uniform strictly positive lower margin and does not imply RH.

## 3. Tiny fully exact integer audit for L=1/8 (deliberately weaker than in-tree full positivity)

At L=1/8 there are NO prime terms, because L<log2. Use R=3000, N=1000. Crude elementary constant enclosures
\[
 \gamma<0.58,\quad \log\pi<1.15,\quad \pi/2<1.6,\quad \log2<0.7
\]
give \(|C_\infty|<5.43\). Also \(2Le^{L/2}=e^{1/16}/4<4/15\). Thus \(B(1/8)<5.43+4/15=1709/300<57/10=5.7\).

For R=3000 and \(\ell_k=(4k+1)/2\), each positive term in (1) is the RATIONAL
\[
 \frac{16R²}{(4k+1)[(4k+1)^2+4R²]}.
\]
The exact INTEGER loop (k=0..10000), flooring each term after multiplication by 10^6, sums to 11,524,558. Therefore
\[
 a(3000)\ge\frac{11524558}{10^6}>23/2=11.5.
\]
For N=1000, \(N!\ge(N/e)^N>(N/3)^N\), \(\pi>3\) and \(RL/2=375/2\) yield
\[
 \alpha_{1000}(1/8,3000)
 <125(9/16)^{2000}
 <125(9/16)^{10}
 =435848050125/1099511627776<1/2.
\]
Hence on the first-1000-moments-zero subspace
\[
 \boxed{W_{1/8}(f)>(23/4-57/10)\|f\|²=(1/20)\|f\|².}\tag{5}
\]
This certificate is not an advance over the ALREADY proved in-tree GPPVerify RungZeroWide result which gives positivity for ALL tests at L=1/8. It is an exact-integer cross-check of the NEW GENERAL mechanism for any L.

Script: experiments/abel_prime_common_map/verify_allwidth_finite_index_certificate.py (Python built-in fractions, integer math only for the finite receipt). All underlying transcendental inequalities are elementary explicit side lemmas; the script does not constitute a Lean formalization of them.

## 4. Stronger conceptual corollary: closed form / compact resolvent

The multiplier a(lambda) grows to infinity while support is fixed in I_L; hence the form domain with \(E(f)+\|f\|²\) embeds compactly into \(L²(I_L)\): uniformly bounded energy controls Fourier mass at large frequency; bounded support gives compactness of the low-frequency projection through its Hilbert–Schmidt kernel. The prime and pole terms are bounded perturbations, so the closed Weil form on I_L is semibounded and its associated selfadjoint operator has compact resolvent. Its eigenvalues diverge to +∞ and only finitely many can be negative. One can avoid invoking functional analysis altogether for the *index* claim by the explicit moment proof above.

## 5. Proper research boundary

The **positive prime Gaussian → Cauchy RG → Carleman → celestial P** universal scale ladder is distinct from this ACTUAL source Weil-form theorem. The thermal P(D) is a bounded smoothing multiplier tending to zero at high frequencies; W has logarithmically growing a(D) and finite prime/pole bounded perturbations. Therefore W cannot equal any bounded covariance form under a bounded L² identification; a genuine state-operator correspondence needs an unbounded energy-domain map and precise local arithmetic completion.

For a potentially RH-valid all-width induction one needs to control the FINITE but GROWING low-energy negative block and its cross Schur coupling at every width. Neither finite-index theorem nor universal positive RG kernel gives this; the F_theta shifted off-line countercontrol is still mandatory.

Upstreamable Lean targets: Fourier symbol a, a(R) monotone/diverges, support-moment Fourier concentration bound, finite-codimension positivity from unbounded coercive symbol + bounded perturbation. All are valid independent of RH, and the abstract lemmas can go to Mathlib.
