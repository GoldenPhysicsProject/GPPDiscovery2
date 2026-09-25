# RH Higgs reduction of the exact CCM phase
## Date: 2026-09-24
## Status: exact algebraic reduction; no RH claim

This note identifies the finite completed CCM cosine response directly with the condensate-subtracted relative-Higgs current plus a uniformly tame Archimedean remainder.

## 1. Exact prime and vacuum currents

For the critical causal arithmetic field,
\[
P_L^{\rm ar}
=
\sum_{n<e^L}\frac{\Lambda(n)}{\sqrt n}V_{\log n}.
\]

Its scalar cosine symbol is
\[
p_L^{\rm ar}(k)
=
\sum_{n<e^L}\frac{\Lambda(n)}{\sqrt n}\cos(k\log n).
\]

For the continuum condensate,
\[
P_L^{\rm vac}
=
\int_0^L2\sinh(a/2)V_a\,da,
\]
with scalar cosine symbol
\[
p_L^{\rm vac}(k)
=
\int_0^L2\sinh(a/2)\cos(ka)\,da.
\]

Define the relative Higgs current
\[
P_L^{\rm rel}=P_L^{\rm ar}-P_L^{\rm vac}
\]
and its cosine symbol
\[
p_L^{\rm rel}(k)=p_L^{\rm ar}(k)-p_L^{\rm vac}(k).
\]

## 2. Exact CCM decomposition

The v34 exact completed phase derivative is
\[
q_L'(k)
=
A_\infty(1)
+\int_0^L w_\infty(a)(\cos(ka)-e^{-a})\,da
-p_L^{\rm ar}(k),
\]
where
\[
w_\infty(a)
=
e^{-a/2}+e^{a/2}
-\frac{e^{-a/2}}{1-e^{-2a}}.
\]

Write
\[
r_\infty(a)=w_\infty(a)-2\sinh(a/2)
=
2e^{-a/2}
-\frac{e^{-a/2}}{1-e^{-2a}}.
\]

Then
\[
\boxed{
q_L'(k)
=
-p_L^{\rm rel}(k)+R_{\infty,L}(k),
}
\]
where
\[
\boxed{
R_{\infty,L}(k)
=
A_\infty(1)
+
\int_0^L
\left[
r_\infty(a)\cos(ka)-w_\infty(a)e^{-a}
\right]\,da.
}
\]

This is exact.

Thus the completed CCM response is literally the negative relative-Higgs current plus a purely Archimedean remainder.

## 3. The remainder has no exponential cutoff growth

At large \(a\),
\[
r_\infty(a)=O(e^{-a/2}),
\qquad
w_\infty(a)e^{-a}=O(e^{-a/2}).
\]

At \(a=0\), both \(r_\infty\) and \(w_\infty\) have the same \(-1/(2a)\) singularity, but
\[
\cos(ka)-e^{-a}=O(a+k^2a^2),
\]
and
\[
2\sinh(a/2)\cos(ka)=O(a).
\]

Hence the displayed combination is locally integrable.

For each fixed \(k\), the integral converges as \(L\to\infty\), so
\[
\boxed{
\sup_{L>0}|R_{\infty,L}(k)|<\infty
\qquad\text{for every fixed }k.
}
\]

A direct split at \(a\sim(1+|k|)^{-1}\) gives the global frequency envelope
\[
\boxed{
|R_{\infty,L}(k)|
\le
C\left(1+\log(1+|k|)\right)
}
\]
with \(C\) independent of \(L\).

Therefore all exponential cutoff instability of the exact completed CCM phase is concentrated in the relative-Higgs current \(p_L^{\rm rel}\).

## 4. Zero-frequency identity and the one-scalar RH criterion

At \(k=0\),
\[
p_L^{\rm vac}(0)
=
\int_0^L2\sinh(a/2)\,da
=
4(\cosh(L/2)-1).
\]

Hence
\[
p_L^{\rm rel}(0)
=
P_{1/2}(e^L)-4(\cosh(L/2)-1),
\]
where
\[
P_{1/2}(x)=\sum_{n\le x}\frac{\Lambda(n)}{\sqrt n}.
\]

The exact v34 identity
\[
q_L'(0)
=
2e^{L/2}-P_{1/2}(e^L)+c_\infty
+\frac23e^{-3L/2}
-\arctan(\sinh(L/2))
\]
becomes
\[
\boxed{
q_L'(0)
=
-p_L^{\rm rel}(0)+B(L),
}
\]
with
\[
\boxed{
B(L)
=
c_\infty+4-2e^{-L/2}
+\frac23e^{-3L/2}
-\arctan(\sinh(L/2)).
}
\]

The function \(B(L)\) is uniformly bounded and converges to
\[
c_\infty+4-\frac\pi2.
\]

Therefore the existing one-scalar criterion can be stated exactly as

\[
\boxed{
RH
\iff
p_L^{\rm rel}(0)=O((1+L)^M)
\text{ for some finite }M.
}
\]

Equivalently: RH is exactly polynomial stability of the zero-frequency condensate-subtracted Higgs current.

## 5. Interpretation

The Higgs decomposition has now removed every exponentially large term that is kinematically forced by the continuum vacuum.

What remains is not the raw prime current
\[
\sum\Lambda(n)n^{-1/2}V_{\log n},
\]
but the relative current
\[
H_L^{-1}[X,H_L]
=
P_L^{\rm ar}-P_L^{\rm vac}.
\]

The Archimedean completion contributes only a cutoff-uniform (for fixed frequency) remainder after this subtraction.

Thus the exact RH-critical theorem has narrowed to:

> prove that the relative Higgs current has only subexponential negative growth on the physical boundary.

At \(k=0\), polynomial control is exactly RH. For fixed \(k\), the Archimedean sector cannot be the source of exponential instability.

This is the cleanest exact scalar formulation of the Higgs mechanism obtained so far.
