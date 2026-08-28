# Arithmetic Field Theory: causal Dirichlet relative-trace front

Date: 2026-08-28

## Executive result

The old arithmetic-principal-series work contains a substantially sharper construction than the naive positive tensor-product picture. The correct prime sector is not merely a direct sum of positive heat atoms. It admits a zero-independent realization as a **causal boundary anomaly** for the Dirichlet heat semigroup on the positive logarithmic half-line.

Let `E_t` be the Dirichlet heat semigroup on `L^2(R_+)`, and let `V_a` be unilateral translation by `a>0`. The exact trace anomaly is

\[
\operatorname{Tr}(E_tV_a-V_aE_t)
=
\frac{a}{\sqrt{4\pi t}}e^{-a^2/(4t)}.
\]

For a prime `p`, define

\[
R_p=-\log\bigl(I-p^{-1/2}V_{\log p}\bigr)
=\sum_{m\ge1}\frac{p^{-m/2}}{m}V_{m\log p}.
\]

Applying the commutator trace term by term gives

\[
\frac{p^{-m/2}}{m}
\frac{m\log p}{\sqrt{4\pi t}}
\exp\!\left[-\frac{(m\log p)^2}{4t}\right]
=
\frac{\log p}{\sqrt{4\pi t}}
\frac{1}{\sqrt{p^m}}
\exp\!\left[-\frac{(\log p^m)^2}{4t}\right].
\]

Thus the Euler logarithm repetition factor `1/m` cancels the repeated orbit length `m log p` exactly, producing the von Mangoldt coefficient. Summing over primes and repetitions yields

\[
\boxed{
\sum_p \operatorname{Tr}[E_t,R_p]
=
\frac1{\sqrt{4\pi t}}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\exp\!\left[-\frac{(\log n)^2}{4t}\right].
}
\]

This is a zero-independent operator realization of the complete prime-power block of the arithmetic heat trace.

## Why this changes the AFT construction

The earlier local AFT model correctly showed that every individual prime-power heat atom is a positive rank-one OS kernel. But the completed explicit formula is not the ordinary trace of a direct sum of those positive atoms. The old work shows that the physically natural global object is a **relative trace**: the prime boundary anomaly is paired with a continuous Archimedean subtraction.

This resolves why the naive tensor-product positivity stalls. The minus sign is not an arbitrary negative sector; it is the subtraction required to renormalize a boundary anomaly.

The exact operator-level Archimedean regularization found there is

\[
B_{a,t}=\frac{[E_t,V_a]}{a},
\qquad
B_{a,t}\to [E_t,-\partial_x]
\quad\text{in trace norm as }a\to0,
\]

with

\[
\|B_{a,t}-B_{0,t}\|_1=O_t(a^{1/2}).
\]

Hence the local real-place subtraction

\[
w_\infty(a)\bigl(B_{a,t}-e^{-a}B_{0,t}\bigr)
\]

is locally trace-norm integrable. This gives a concrete candidate for the Archimedean component of the AFT relative field.

## The real obstruction

The separate prime commutators are not absolutely summable in trace norm. Their Hilbert--Schmidt norms have a nonzero asymptotic floor after the relevant normalization. Scalar Gaussian convergence occurs only after taking diagonal traces. Therefore the completed prime--Archimedean object must be constructed as one coupled relative operator before positivity is asked for.

This is now the first-class target:

\[
\boxed{
\text{construct a coupled relative operator }\mathcal C_t
\text{ with }\operatorname{Tr}\mathcal C_t=\mathscr K(t)
\text{ and prove a positive/cohomological factorization.}
}
\]

The old work already gives finite-support coupled operators whose sine transform is controlled by an explicit phase `q_L`. After restoring the real-place tail counterterm `r_L`, the corrected phase is

\[
\widetilde q_L(k)=q_L(k)-r_Lk.
\]

Its Gaussian phase derivative tends to the arithmetic heat trace. The zero mode reproduces Suzuki's screw function, and positivity of that screw function for every support length is itself equivalent to RH. This identifies the missing norm square but does not yet construct it.

## Cohomological interpretation

The rigorous zero-free ghost model remains the reduced odd cokernel of the Nyman--Burnol Tate boundary inclusion. Under Mellin transform it is isometric to the bad-zero model space `K_B`. Therefore the correct AFT complex should not be a naive finite-prime Koszul complex: those have contracting-homotopy or nonclosed-range obstructions.

The correct architecture is instead:

\[
\text{Tate boundary space}
\xrightarrow{\ d_{\rm AFT}\ }
\text{causal Dirichlet relative field space},
\]

with a graph norm strong enough to make the global relative operator coercive, while preserving the Tate cokernel. The no-ghost theorem then becomes the statement that the completed physical cohomology is purely even.

## Exact formalization added

`GppVerify/CelestialHolography/ArithmeticEulerLogAnomaly.lean` formalizes the algebraic heart of the causal anomaly: for every nonzero repetition `m`,

\[
\frac1m(m\log p)=\log p,
\]

and therefore every finite Euler-logarithm truncation agrees term-by-term with the corresponding finite von-Mangoldt prime-power sum.

## Status

This does **not** prove RH. It improves the construction problem from an unspecified signed gluing to a concrete operator-theoretic one:

1. prime block = exact causal Dirichlet boundary anomaly;
2. real place = exact continuous relative subtraction;
3. completed arithmetic heat trace = scalar limit of a coupled relative trace;
4. missing theorem = positive/cohomological factorization of the coupled relative operator, equivalently the arithmetic no-ghost theorem.

The immediate next attack should be on the finite-support coupled operator and its corrected phase `\widetilde q_L`: seek an exact factorization of the corresponding finite Weil matrix as `T_L^* J T_L`, then determine whether the Fisher/Gamma kernel supplies the missing positive metric that converts `J` to a physical positive quotient after the Tate boundary cokernel is imposed.
