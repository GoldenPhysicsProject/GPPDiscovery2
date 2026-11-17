# Prime phase recurrence versus averaged cancellation: the arithmetic frequency obstruction in the Weil Schur block

**2026-11-16, Discovery2.** Classical almost-periodic/Kronecker and elementary finite Dirichlet-polynomial mean-square identities applied to the exact prime multiplier of the source Weil form. No RH proof, global reserve invariant, or positive full Weil form. Nontrivial arithmetic phase information is now a specific possible next input, not a presumed positivity theorem.

## 1. The exact Fourier multiplier of the ACTUAL source prime term

At fixed support width L>log2 define v_n=Lambda(n)/sqrt(n), ell_n=log n and
\[
 F_L(\lambda)=\sum_{\ell_n<L}v_n e^{i\lambda\ell_n}.
\]
The real, zero-free Weil form is, for real smooth f supported in I_L,
\[
 W_L(f)=\frac1{2\pi}\int_{\mathbb R}
 \left(a(\lambda)+C_\infty-2\Re F_L(\lambda)\right)
 |\hat f(\lambda)|^2 d\lambda+\mathrm{Pole}(f),
\]
where \(a(\lambda)=\Re[\psi(1/4+i\lambda/2)-\psi(1/4)]\) is the positive, divergent archimedean Fourier symbol (as in the previous notes). The pole is the signed one-rank-per-parity term; see prime_graph_parity_smooth_moment_schur_2026_11_16.md.

This is EXACT, not an approximate prime-wave analogy. The entire extra arithmetic input that a frequency-based proof needs enters through Re F_L(lambda), a truncated logarithmic-derivative Dirichlet polynomial.

## 2. Exact recurrence no-go for any pointwise cancellation bound

The logarithms of distinct rational primes are Q-linearly independent: if Σ_p k_p log p=0 for integers k_p, then Π_p p^{k_p}=1, forcing all k_p=0. By classical Kronecker density for continuous linear flows on a finite torus, for any R>0 and eps>0 there are arbitrarily large lambda>R for which every exp(i lambda log p) is within eps of 1 for every p<exp L.

For any prime power n=p^k<exp L, its phase is (exp(i lambda log p))^k, hence can simultaneously be made arbitrarily close to 1 (finite exponent ceiling). Consequently,
\[
 \boxed{\sup_{\lambda>R}\Re F_L(\lambda)
 =\sum_{\ell_n<L}v_n=:V_L(L)\quad\text{for every finite }R.}\tag{1}
\]
This is a strong NO-GO for using a STRICT UNIFORM PRIME-PHASE CANCELLATION bound on high frequencies to replace the coarse coefficient V(L). It is not a no-go for gamma domination, since a(lambda) grows ~log|lambda| and eventually beats 2V(L) at each FIXED width. Timing the recurrence against gamma is a separate Diophantine/analytic question.

## 3. Exact mean-square cancellation, including a finite-T error term

Let N_L={n>=2: log n<L and Lambda(n)>0} be finite, and S2(L)=Σ_{n∈N_L}v_n². Define sinc(z)=sin z/z (sinc 0=1). For T>0,
\[
 \frac1{2T}\int_{-T}^T(\Re F_L(\lambda))^2\,d\lambda
 =\frac12\sum_{m,n\in N_L}v_m v_n
 \left[\operatorname{sinc}(T(\ell_m-\ell_n))
       +\operatorname{sinc}(T(\ell_m+\ell_n))\right].\tag{2}
\]
All different integers have different logs; all sums ell_m+ell_n are >0. Thus
\[
 \boxed{\lim_{T\to\infty}
 \frac1{2T}\int_{-T}^T(\Re F_L(\lambda))^2d\lambda
 =\frac{S2(L)}{2}.}\tag{3}
\]
Moreover the FINITE-T error from this limit is at most
\[
 \frac{D_L}{2T},\quad
 D_L=\sum_{m\ne n}\frac{v_mv_n}{|\ell_m-\ell_n|}
     +\sum_{m,n}\frac{v_mv_n}{\ell_m+\ell_n}.\tag{4}
\]
This is a finite, explicitly computable, source-arithmetic bound with no zeros and no PNT.

By Chebyshev/Markov, for any eta>0 and finite T,
\[
\frac{|\{\lambda\in[-T,T]:\Re F_L(\lambda)\ge\eta V_L(L)\}|}{2T}
\le\frac{S2(L)+D_L/T}{2\eta^2 V_L(L)^2}.
\]
Taking T→∞:
\[
 \boxed{\mathrm{upper\ phase\ density}\le S2(L)/(2\eta^2 V_L(L)^2).}\tag{5}
\]

Using the established PNT and partial summation (NOT RH),
\[
 V_L(L)\sim2e^{L/2},\qquad
 S2(L)=\sum_{\ell_n<L}\frac{\Lambda(n)^2}{n}
    \sim\frac12 L^2
\]
(the k>=2 prime-power squared terms have a convergent total). Thus the upper phase density at a fixed fraction eta of maximal coherent prime amplitude is
\[
 \boxed{O_\eta(L^2e^{-L}),\quad\text{asymptotic upper bound }
 \frac{L^2}{16\eta^2 e^L}(1+o(1)).}\tag{6}
\]
So maximal coherent prime resonances exist arbitrarily far out by (1), yet are very RARE in asymptotic phase density as L grows. This reconciles the apparent contradiction between no uniform cancellation and excellent typical cancellation.

## 4. Fourier uncertainty suggests a different possible certificate

Any f supported in I_L obeys |hat f(lambda)| <=sqrt(L)||f|| by Cauchy–Schwarz. Hence for measurable B⊂R with finite length,
\[
\boxed{\frac1{2\pi}\int_B|\hat f|^2d\lambda
 \le\frac{L|B|}{2\pi}\|f\|^2.}\tag{7}
\]
This is a source-independent uncertainty estimate, but it can transport rigorous bounds on the MEASURE of the negative spectral set of the **actual** function
m_L(lambda)=a(lambda)+Cinf−2Re F_L(lambda)
into source Weil-form bounds. For example if m_L>=delta>0 off a finite bad set B and m_L>=-M on B, then by (7)
\[
\frac1{2\pi}\int m_L|\hat f|^2
\ge \left[\delta-\frac{L|B|}{2\pi}(\delta+M)\right]\|f\|^2.
\]
The signed pole still needs its one-dimensional odd-channel bound or exact parity treatment.

**This is a sufficient criterion, NOT verified for any new width.** The mean-square density estimate (5) averages over all large lambda and does NOT alone bound the low-frequency bad set B. Nor does it preclude Paley–Wiener wavepackets targeting rare resonances. An actual RH-oriented application must quantify phase cancellation at frequencies below the gamma cutoff, and must fail F_theta controls.

## 5. Numerical checks, existing results, and genuine new question

A numerical source-prime probe gives at L=10: V≈294.012, sqrt(S2/2)≈4.923, so the RMS real prime amplitude is ~1.67% of its maximum coherent amplitude; at L=15 the fraction is ~0.206%. These are elementary finite sums, not RH evidence. The exact mean-square identity (2) and finite-T bound (4) are provable for every L, independent of such sampling.

The key open arithmetic question is now highly specific:
Can one combine Diophantine lower bounds on COHERENT prime-phase recurrence times, frequency-local density estimates for Re F_L, and the increasing gamma energy a(lambda) to certify the remaining LOW-FREQUENCY negative Schur block? A global mean or a naive pointwise weak-coupling inequality is insufficient, as previous fake-prime falsifiers show.

Use true Euler products and compare against the shifted F_theta control, which shares the general Dirichlet-polynomial phase mechanism but has off-critical completed zeros. No automatic RH conclusion follows from (1)-(7). Verify source gamma symbol and Weil normalization before transporting to Lean.
