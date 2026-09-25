# RH signed self-adjoint heat realization criterion — positivity of cohomology is unnecessary
## Date: 2026-09-24
## Status: exact criterion; strictly weaker than the previous even-cohomology Hodge closure target

Let
\[
F(z)=\frac{\xi(1/2+z)}{\xi(1/2)}
\]
and let
\[
m_*(u)=\frac{F'(\sqrt{1+u})}{2\sqrt{1+u}\,F(\sqrt{1+u})},
\qquad u>0.
\]
The existing zero-independent completed heat trace \(\mathscr K(t)\) satisfies
\[
m_*(u)=\int_0^\infty e^{-(1+u)t}\mathscr K(t)\,dt.
\]

The previous Hodge closure criterion asked for
\[
\mathscr K(t)=\operatorname{Tr}_{H^{\rm even}}e^{-tL_H}
\]
with no odd cohomology, so that \(\mathscr K\) is completely monotone. That positivity is stronger than RH requires.

## Theorem — signed self-adjoint realization already forces RH

Suppose there exists a signed Borel measure \(\mu\) supported on \([0,\infty)\), with enough local variation/exponential integrability that
\[
\mathscr K(t)=\int_{[0,\infty)}e^{-t\lambda}\,d\mu(\lambda)
\qquad(t>0)
\]
and Fubini gives
\[
m_*(u)
=
\int_{[0,\infty)}
\frac{d\mu(\lambda)}{u+1+\lambda}.
\]
Then RH holds.

Equivalently, it suffices that the exact completed heat trace be the ordinary graded heat trace of a fixed nonnegative self-adjoint operator:
\[
\mathscr K(t)
=
\operatorname{Tr}(e^{-tL_+})
-
\operatorname{Tr}(e^{-tL_-}),
\]
with the two traces/relative spectral measure defined strongly enough to yield the displayed signed Stieltjes transform. No assumption that the odd sector vanishes is needed.

### Proof

The signed Stieltjes transform
\[
\int_{[0,\infty)}\frac{d\mu(\lambda)}{u+1+\lambda}
\]
is holomorphic on
\[
\mathbb C\setminus(-\infty,-1].
\]

On the other hand the unconditional Hadamard expansion gives
\[
m_*(u)
=
\sum_{\zeta\bmod\{\pm1\}}
\frac{m_\zeta}{u+1-\zeta^2},
\]
where \(\zeta\) runs over the centered nonzero zeros of \(F\), with positive integer multiplicities.

Thus every zero \(\zeta\) produces a pole at
\[
u=\zeta^2-1.
\]
There can be no cancellation of such a pole: the residue is its positive multiplicity, and the only identification already made is \(\zeta\sim-\zeta\).

Since \(m_*\) is holomorphic off the negative real cut, every \(\zeta^2-1\) must belong to \((-\infty,-1]\). Hence
\[
\zeta^2\in(-\infty,0].
\]
Therefore each nonzero centered zero is either purely imaginary or real.

There are unconditionally no real centered nontrivial zeros: \(F(r)=\xi(1/2+r)/\xi(1/2)\ne0\) for real \(r\). Hence every centered zero is purely imaginary.

Therefore every nontrivial zeta zero has real part \(1/2\).

QED.

## Why this matters for the Higgs/Feshbach program

The target is now weaker than the earlier no-ghost theorem.

We do **not** need:
- complete monotonicity of \(\mathscr K\);
- positivity of its spectral measure;
- concentration of completed cohomology in even degree.

We only need:
- a fixed positive-metric/self-adjoint completed operator;
- a genuine signed/graded spectral measure on the real nonnegative axis;
- exact equality of its graded heat trace with the zero-independent arithmetic \(\mathscr K(t)\).

Odd states may survive. Their spectral weights may enter with minus signs. They still cannot generate the nonreal resolvent poles produced by an off-critical zero.

This fits the unitary-dilation Higgs mechanism precisely: the full-line delay/Koszul parent is already self-adjoint and massive. The remaining theorem is solely to identify the co-Poisson/Archimedean boundary reservoir so that its graded relative heat trace is exactly \(\mathscr K(t)\). Positivity after grading is no longer load-bearing.
