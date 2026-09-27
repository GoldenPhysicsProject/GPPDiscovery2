# Exact positive Lévy parent of the pole-subtracted completed current

Date: 2026-09-27. Status: proved analytic representation in the Euler half-plane; no RH claim. This is derived from the recovered Archimedean ladder and prime current.

Write \(B(s)=\xi'(s)/\xi(s)\) with the usual entire completed \(\xi\). The digamma recurrence gives
\[
B(s)=\frac1{s-1}-\frac12\log\pi
+\frac12\psi(1+s/2)-J(s),
\quad
J(s)=\sum_{n\ge2}\Lambda(n)n^{-s},
\quad \Re s>1.
\]
The apparent \(s=1\) pole here belongs to the separated rational term; it is cancelled in the full \(B\) by the pole of \(J\). It is not a pole of the entire completed \(\xi\).

## 1. A positive increment function

Fix \(q>1\), and set \(z\ge0\). Define
\[
\phi_q(z)=B(q+z)-B(q)
-\left(\frac1{q+z-1}-\frac1{q-1}\right).
\]
Then
\[
\boxed{\phi_q(z)=
\frac12[\psi(1+(q+z)/2)-\psi(1+q/2)]
+J(q)-J(q+z).}
\]
It has the exact Lévy representation
\[
\boxed{\phi_q(z)=\int_{(0,\infty)}(1-e^{-zx})\,d\nu_q(x)}
\]
with positive measure
\[
\boxed{d\nu_q(x)=
\frac{e^{-(q+2)x}}{1-e^{-2x}}\,dx
+\sum_{n\ge2}\Lambda(n)n^{-q}\delta_{\log n}(dx).}
\]
**Proof.** Expand the continuous density as \(\sum_{k\ge1}e^{-(q+2k)x}\). Termwise integration gives
\[
\sum_{k\ge1}
\left(\frac1{q+2k}-\frac1{q+z+2k}\right)
=\tfrac12[\psi(1+(q+z)/2)-\psi(1+q/2)].
\]
The atomic part gives \(J(q)-J(q+z)\) directly. All summands are nonnegative for real \(z\ge0\). Near zero the continuous density is \(1/(2x)+O(1)\), while the first prime atom is at \(\log2\). Thus \(\int(1\wedge x)d\nu_q<\infty\). QED.

In particular,
\[
\phi_q(0)=0,\qquad
(-1)^{k-1}\phi_q^{(k)}(z)
=\int x^k e^{-zx}\,d\nu_q(x)>0,\quad k\ge1.
\]
This is an unconditional all-order Bernstein hierarchy in the original shift variable. It is not the Stieltjes hierarchy in the squared RH spectral variable.

## 2. A concrete random process, without zero data

There is an explicit realization of the Laplace law
\[
\mathbb E e^{-zX_\tau}=e^{-\tau\phi_q(z)}.
\]
For the continuum part, each \(k\ge1\) contributes a compound-Poisson process of rate \((q+2k)^{-1}\) with exponential jumps of rate \(q+2k\). Its exponent is
\[
\frac1{q+2k}-\frac1{q+2k+z}.
\]
Their expected summed size at time \(\tau\) is
\(\tau\sum_{k\ge1}(q+2k)^{-2}<\infty\), so the nonnegative sum converges almost surely even though the total jump rate diverges.

Independently, each prime power \(p^m\) contributes jumps of size \(m\log p\) with Poisson rate
\[
(\log p)p^{-mq}.
\]
Their total rate is \(J(q)<\infty\). Thus the real-place excited ladder is the infinite-activity part and the prime powers are the finite-rate jump part of one completely specified positive process.

At the safe shifted base \(q=3/2\), the rates are exactly the critically weighted arithmetic current with the extra exponential damping used by the existing massive-resolvent criterion.

## 3. Why this positive parent is not already a Stieltjes parent

The stronger property needed for a complete Bernstein function would be that \(\phi_q(z)/z\) is Stieltjes. Here it is not.

Indeed, Tonelli gives
\[
\frac{\phi_q(z)}z=\int_0^\infty e^{-zt}h_q(t)\,dt,
\qquad h_q(t)=\nu_q((t,\infty)).
\]
The continuous part of \(h_q\) is smooth away from zero, but the prime part has a downward jump of size \(\Lambda(n)n^{-q}>0\) at every prime power \(t=\log n\).

If \(\phi_q(z)/z\) had a Stieltjes representation
\[
a/z+b+\int_{(0,\infty)}(z+\lambda)^{-1}\,d\mu(\lambda),
\qquad a,b,\mu\ge0,
\]
its inverse Laplace transform for \(t>0\) would be
\[
a+\int e^{-\lambda t}\,d\mu(\lambda),
\]
a smooth completely monotone function. The constant \(b\) affects only a delta at \(t=0\). Uniqueness of the Laplace transform excludes equality with a function having a genuine jump on an interior interval. Therefore \(\phi_q\) is Bernstein but not complete Bernstein.

This is a precise obstruction, not a failure of local probabilistic positivity. It explains why a positive jump process in the logarithmic-length variable does not automatically furnish the self-adjoint Stieltjes realization in \(u\).

## 4. What the result changes

The real-place/prime combination now has an explicit positive parent at the level of pole-subtracted current increments. Its Lévy measure contains the exact arithmetic weights and the exact excited Gamma ladder; neither was chosen by fitting zeros.

To finish RH, one still has to show that the prescribed pole restoration and quadratic spectral change
\[
s=\tfrac12+\sqrt{1+u}
\]
produce the required positive spectral measure. The jump representation does not establish this. The sign change and the change of spectral variable must be proved at operator level.

The numerical controls independently compare the digamma formula with quadrature and the prime expression with 160 repetitions for each prime through 97, at \(q=3/2,\ z=0.1,0.7,2,5\). Maximum recorded error: \(8.9\times10^{-16}\), in double precision. The infinite theorem is proved above, not inferred from these checks.
