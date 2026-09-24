# RH discovery: the Archimedean channel is uniformly stable
## Vacuum instability is confined to the coupled pole--prime sector

**Date:** 2026-09-24  
**Status:** exact lower bound on the real-place contribution. This is not an RH proof.

## 1. Archimedean term of the completed explicit formula

For an admissible convolution square
\[
g=f*\widetilde f,
\qquad
g(0)=\|f\|_2^2,
\]
the assembled real-place term is
\[
\mathcal A_\infty(g)
=
-(\gamma+\log\pi)g(0)
+
2\int_0^\infty
\frac{
e^{-2u}g(0)-e^{-u/2}\operatorname{Re}g(u)
}{
1-e^{-2u}
}\,du.
\]

For a normalized state,
\[
g(0)=1.
\]

By Cauchy--Schwarz for translations,
\[
|g(u)|
=
|\langle f,T_u f\rangle|
\le
\|f\|_2^2
=
1.
\]
Hence
\[
1-\operatorname{Re}g(u)\ge0.
\]

Rewrite
\[
e^{-2u}
-
e^{-u/2}\operatorname{Re}g(u)
=
\bigl(e^{-2u}-e^{-u/2}\bigr)
+
e^{-u/2}\bigl(1-\operatorname{Re}g(u)\bigr).
\]

Therefore
\[
\boxed{
\mathcal A_\infty(g)
=
C_\infty
+
2\int_0^\infty
\frac{
e^{-u/2}\bigl(1-\operatorname{Re}g(u)\bigr)
}{
1-e^{-2u}
}\,du
}
\tag{1}
\]
with a state-independent constant
\[
C_\infty
=
-(\gamma+\log\pi)
+
2\int_0^\infty
\frac{e^{-2u}-e^{-u/2}}{1-e^{-2u}}\,du.
\]

The second term in (1) is nonnegative.

## 2. Exact value of the lower floor

Set
\[
x=e^{-u/2}.
\]
Then
\[
2\int_0^\infty
\frac{e^{-2u}-e^{-u/2}}{1-e^{-2u}}\,du
=
4\int_0^1
\frac{x^3-1}{1-x^4}\,dx.
\]

Using
\[
\int_0^1
\frac{x^{a-1}-x^{b-1}}{1-x^q}\,dx
=
\frac1q
\left[
\psi\!\left(\frac bq\right)
-
\psi\!\left(\frac aq\right)
\right],
\]
one obtains
\[
4\int_0^1\frac{x^3-1}{1-x^4}\,dx
=
\psi(1/4)-\psi(1)
=
-\frac{\pi}{2}-3\log2.
\]

Thus
\[
\boxed{
C_\infty
=
-\gamma-\log\pi-\frac{\pi}{2}-3\log2.
}
\tag{2}
\]

Numerically this is approximately
\[
C_\infty\approx -5.37218.
\]

Consequently
\[
\boxed{
\mathcal A_\infty(g)
\ge
-\gamma-\log\pi-\frac{\pi}{2}-3\log2
}
\tag{3}
\]
for every normalized admissible convolution square.

The bound is independent of the support size.

## 3. Consequence for the RH instability problem

The completed Weil form decomposes schematically as
\[
\mathcal W(g)
=
\mathcal P_{\rm triv}(g)
+
\mathcal A_\infty(g)
-
\mathcal P_{\rm primes}(g),
\]
where
\[
\mathcal P_{\rm triv}(g)
=
\int_{\mathbb R}
g(u)\bigl(e^{u/2}+e^{-u/2}\bigr)\,du
\]
is the trivial/pole channel and
\[
\mathcal P_{\rm primes}(g)
=
2\sum_{n\ge2}
\Lambda(n)n^{-1/2}g(\log n).
\]

Equation (3) proves that the Archimedean/metaplectic channel cannot be the
source of an exponentially falling vacuum floor.

Therefore any off-critical zero, whose existence is equivalent to exponential
negative-energy instability in the two-box criterion, must be encoded in the
**coupled cancellation failure**
\[
\boxed{
\mathcal P_{\rm triv}
-
\mathcal P_{\rm primes}.
}
\tag{4}
\]

The real-place tower contributes only a support-independent stable floor plus
a nonnegative translation Dirichlet form.

This is stronger than saying that the Archimedean term is explicit. It says
that it is already harmless for the new semiboundedness strategy.

## 4. Physics interpretation

Equation (1) is a thermal Dirichlet form:
\[
\int_0^\infty
K_\infty(u)\,
\bigl(
1-\operatorname{Re}\langle f,T_u f\rangle
\bigr)\,du,
\qquad
K_\infty(u)
=
\frac{2e^{-u/2}}{1-e^{-2u}}>0.
\]

The place at infinity is therefore a genuine dissipative/stabilizing bath.
It penalizes failure of translation coherence and has a fixed vacuum
renormalization \(C_\infty\).

The exponential instability required by an off-line zero cannot originate
from this bath.

It can only arise from the competition between

- the anti-midpoint trivial mode \(e^{+u/2}\), and
- the midpoint prime lattice \(\Lambda(n)n^{-1/2}\).

This matches the thermodynamic picture of the Bost--Connes transition: the
trivial character is the unique growing/coherent channel.

## 5. Revised minimal target

Combining this result with the vacuum-instability theorem, RH follows if one
proves merely
\[
\boxed{
\mathcal P_{\rm triv}(f*\widetilde f)
-
\mathcal P_{\rm primes}(f*\widetilde f)
\ge
-\exp(o(L))
}
\tag{5}
\]
for normalized test functions of logarithmic support \(L\).

For the fixed-window two-box family, the requirement is even narrower: prove
(5) only on that one orbit.

The Archimedean channel then adds the uniform lower constant (2) and cannot
change the exponential instability exponent.

Thus the remaining RH mechanism is no longer a three-way
prime--Archimedean--pole problem.

At the level relevant to semiboundedness it has collapsed to a
**two-channel pole--prime stability problem**.
