# AFT global no-ghost coercivity target — 2026-08-28

## Status

No proof of RH yet.

The old arithmetic principal-series work already isolates the correct zero-free cohomology and the correct global obstruction more sharply than the naive local-prime Hodge picture.

## Correct ghost complex

For

\[
\rho_\lambda(u)=\left\{\frac{\lambda}{u}\right\}-\lambda\left\{\frac1u\right\},
\qquad 0<u<1,
\]

let \(\mathcal N\) be their closed span in \(\mathcal X=L^2((0,1),du)\). Under the Mellin isometry

\[
\mathcal X\simeq H^2(\Re s>1/2),
\]

one has

\[
\widehat{\rho_\lambda}(s)=\frac{\lambda-\lambda^s}{s}\zeta(s),
\qquad
\widehat{\mathcal N}=B H^2,
\]

where \(B\) is the Blaschke product over zeros of \(\zeta\) with \(\Re\rho>1/2\). Therefore the zero-free two-term complex

\[
0\to \mathcal N\xrightarrow{\iota}\mathcal X\to0
\]

has reduced odd cohomology

\[
\boxed{
\overline H^1\simeq\mathcal X/\mathcal N\simeq H^2\ominus B H^2=K_B.
}
\]

Hence

\[
\boxed{RH\iff K_B=0\iff \overline H^1=0.}
\]

This is the correct ghost space. It is not the naive finite-prime Gamma--Möbius--Koszul cohomology.

## Why local contractions cannot close it

The previous program proves several negative results that must remain hard constraints:

- one-prime resolvents do not preserve the Tate--Poisson boundary domain;
- with two or finitely many primes, irrational-rotation small divisors make the Koszul range dense and nonclosed;
- periodization is not closable in the Gamma \(\dot H^{1/8}\) topology;
- bilateral Gaussian heat destroys positive-time support, so it cannot provide the causal global homotopy.

Thus the no-ghost theorem must be genuinely global and nonlocal.

## Causal replacement

The correct positive-time semigroup is Dirichlet heat \(E_t\) on \(L^2(\mathbb R_+)\). For unilateral translation \(V_a\),

\[
\operatorname{Tr}(E_tV_a-V_aE_t)
=
\frac{a}{\sqrt{4\pi t}}e^{-a^2/(4t)}.
\]

With

\[
R_p=-\log(I-p^{-1/2}V_{\log p}),
\]

this recovers the complete prime-power part

\[
\sum_p\operatorname{Tr}[E_t,R_p]
=
\frac1{\sqrt{4\pi t}}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)^2/(4t)}.
\]

The Archimedean term is a continuous subtraction partner. The completed arithmetic object is therefore a relative trace, not a sum of independently positive traces.

## Sharpened theorem target

Construct a closed global boundary differential \(D_{\rm AFT}\) using Tate--Poisson summation and the explicit prime--Archimedean data, on a graph topology that retains the Nyman--Burnol cokernel, such that its odd Laplacian

\[
\Delta_- = D_{\rm AFT}^*D_{\rm AFT}+D_{\rm AFT}D_{\rm AFT}^*
\]

satisfies a uniform coercive estimate

\[
\boxed{
\langle \psi,\Delta_-\psi\rangle
\ge c\|\psi\|^2,
\qquad c>0.
}
\]

Then any odd harmonic state obeys

\[
0=\langle \psi,\Delta_-\psi\rangle\ge c\|\psi\|^2,
\]

so \(\psi=0\). Hence the odd physical cohomology vanishes. If the relative heat supertrace is simultaneously identified with the zero-independent arithmetic heat trace \(\mathscr K(t)\), Hodge cancellation leaves a positive even heat trace, giving complete monotonicity and RH.

This elementary implication has now been formalized in Lean as `ArithmeticNoGhostCoercivity.lean`. The unproved content is the arithmetic construction of \(D_{\rm AFT}\) and the positive constant \(c\).

## Trace-escape reformulation

The later finite-section analysis sharpens the same obstruction. Finite coupled prime--Archimedean operators converge at the scalar Gaussian trace level, but Hilbert--Schmidt convergence does not preserve trace. Possible off-line zeros are precisely the trace that can escape in the boundary limit.

Thus an equivalent target is:

\[
\boxed{
\text{global trace-class convergence + no escaped trace + positive limiting spectral measure.}
}
\]

At zero frequency this appears as the exact growth criterion

\[
RH\iff q_L'(0)=O(L^3)
\]

(and in fact any polynomial bound suffices in the cited normal form). This gives a concrete analytic route to the same no-ghost theorem: prove a uniform finite-section spectral gap / trace-conservation estimate for the zero-independent corrected phase family.

## Immediate next attack

The most promising route is now not another local Euler factorization. It is to derive a global energy identity for the corrected coupled phase operator whose boundary term is the Tate--Poisson trace and whose bulk term is manifestly nonnegative. The desired estimate should have the schematic form

\[
\|D_{\rm AFT}\psi\|^2+\|D_{\rm AFT}^*\psi\|^2
\ge c\|\psi\|^2
-
\text{controlled boundary remainder},
\]

then show the corrected Archimedean counterterm cancels the remainder uniformly as the support cutoff tends to infinity.

That is the precise place to use the new Gamma/Fisher/KL identity: as the positive Archimedean bulk metric inside a global relative energy estimate, not as a standalone reweighting of the ghost sector.
