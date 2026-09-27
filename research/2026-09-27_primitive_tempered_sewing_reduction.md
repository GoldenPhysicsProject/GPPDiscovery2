# Primitive-prime temperateness is sufficient: remove the higher sectors before the spectral test

Date: 2026-09-27. Status: proved sufficient criterion and unconditional elimination of the higher repetitions from the domain obstruction; the primitive cancellation estimate remains open. No RH proof.

Provenance: the signed self-adjoint heat criterion was already recorded on 2026-09-24 in Discovery2 and Supabase research note c6ba80e4-d58e-4821-a8bb-380e20855c9a. It was recovered during this continuation and is not a new result of this turn. The Gaussian-smoothed distribution argument and the primitive/higher-sector reduction below sharpen the domain required for that route.

## 1. Exact completed distribution, including the contact normalization

For \(x>0\),
\[
w_\infty(x)=e^{x/2}-\frac{e^{-5x/2}}{1-e^{-2x}},
\qquad
A_\infty(1)=\frac83-\frac{\log\pi+\gamma}{2}
+\frac\pi4-\frac32\log2.
\]
On smooth compactly supported half-line tests,
\[
\langle\nu_\infty,f\rangle
=A_\infty(1)f(0)
+\int_0^\infty w_\infty(x)[f(x)-f(0)e^{-x}]\,dx.
\]
The second term has a finite limit at zero after subtraction. Set
\[
W=\nu_\infty-\sum_{p,m\ge1}(\log p)p^{-m/2}\delta_{m\log p}.
\]
Define its even distribution on \(\mathbb R\) by
\[
\langle T,\varphi\rangle
=\left\langle W,\frac{\varphi(x)+\varphi(-x)}2\right\rangle.
\]
With \(g_t(x)=(4\pi t)^{-1/2}e^{-x^2/(4t)}\), the previously established exact heat function is \(K(t)=\langle T,g_t\rangle\).

## 2. All \(m\ge2\) channels are already tempered

Let
\[
\nu_{\ge2}=\sum_{p,m\ge2}(\log p)p^{-m/2}\delta_{m\log p}.
\]
For \(X\ge1\),
\[
\begin{aligned}
\nu_{\ge2}([0,X])
&\le\sum_{p\le e^{X/2}}\frac{(\log p)/p}{1-p^{-1/2}}\\
&\le\frac1{1-2^{-1/2}}\sum_{2\le n\le e^{X/2}}\frac{\log n}{n}
=O(1+X^2).
\end{aligned}
\]
Thus its even extension is a positive tempered distribution, unconditionally and without a prime number theorem.

The \(m\ge3\) submeasure has finite total mass:
\[
\sum_{p,m\ge3}(\log p)p^{-m/2}
\le\frac1{1-2^{-1/2}}\sum_{n\ge2}(\log n)n^{-3/2}<\infty.
\]
The \(m=2\) channel may diverge at infinity, but its growth is polynomial in logarithmic distance. It cannot be the source of exponential escape.

The difference
\[
\nu_\infty-e^{x/2}\,dx
\]
is also tempered after even extension: it has the explicit finite-part singularity at zero and an exponentially decaying tail. The contact coefficient is finite and retained.

Consequently
\[
\boxed{T\text{ is tempered}\quad\Longleftrightarrow\quad
\operatorname{Even}\left[
e^{x/2}\,dx-\sum_p\frac{\log p}{\sqrt p}\delta_{\log p}
\right]\text{ is tempered}.}
\]
Here “tempered” means extension as a distribution on Schwartz tests, with cancellations performed before the extension. It does not assert polynomial growth of the total variation of the signed primitive measure.

## 3. Temperateness of \(T\) forces RH

Assume \(T\in\mathcal S'(\mathbb R)\). For any fixed \(\epsilon>0\), define
\[
M_\epsilon(u)=\int_0^\infty e^{-(1+u)t}K(t+\epsilon)\,dt,\qquad u>0.
\]
Using \(\widehat f(k)=\int e^{-ikx}f(x)\,dx\) and evenness, the distributional Fourier formula gives
\[
\boxed{M_\epsilon(u)=\frac1{2\pi}
\left\langle\widehat T(k),
\frac{e^{-\epsilon k^2}}{1+u+k^2}\right\rangle.}
\]
For \(u\in\mathbb C\setminus(-\infty,-1]\), the test on the right is Schwartz. It depends holomorphically on \(u\) in every Schwartz seminorm locally off that cut, because its denominator is bounded away from zero on real \(k\), with uniform polynomial control at infinity. Pairing with a fixed tempered distribution therefore proves that \(M_\epsilon\) is holomorphic off the cut.

The exact subordination identity also gives
\[
M_\epsilon(u)=e^{\epsilon(1+u)}
\left[m_*(u)-\int_0^\epsilon e^{-(1+u)t}K(t)\,dt\right].
\]
The short-time integral is entire in \(u\). Indeed, the explicit real-place finite part gives
\[
K(t)=O\!\left(t^{-1/2}(1+|\log t|)\right),\qquad t\downarrow0,
\]
while the first prime length is \(\log2>0\), so the prime contribution is exponentially suppressed at small time. The stated estimate is integrable at zero.

For completeness, the logarithm in that estimate comes from the singular term
\(-1/(2x)\): its renormalized pairing with \(e^{-x^2/(4t)}-e^{-x}\) is
\(O(1+|\log t|)\). The remaining local density is bounded; at large \(x\), the Gaussian controls the \(e^{x/2}\) tail.

It follows that
\[
m_*(u)=e^{-\epsilon(1+u)}M_\epsilon(u)
+\int_0^\epsilon e^{-(1+u)t}K(t)\,dt
\]
extends holomorphically to the same cut plane.

But if \(z=\rho-1/2\) is any nonzero centered zero of \(\xi\), then
\[
m_*(u)=\frac1{2r}\frac{\xi'}{\xi}(1/2+r),
\qquad r^2=1+u,
\]
has a pole at \(u=z^2-1\), with residue equal to the positive integer multiplicity. This follows locally from the logarithmic derivative; no global convergence of a zero sum is needed. The functional equation makes this a single-valued meromorphic function of \(u\).

Holomorphy off \((-\infty,-1]\) forces \(z^2\le0\) real, hence \(z\) is purely imaginary. Thus RH follows. QED.

This is stronger as a construction allowance than demanding a finite-variation signed spectral measure: a fixed tempered spectral distribution, after Gaussian smoothing, is enough. It is not a claim that mere self-adjointness of a formal parent proves the required domain estimate.

## 4. A concrete sufficient primitive estimate

Put
\[
D_1(X)=
\sum_{p\le e^X}\frac{\log p}{\sqrt p}
-2e^{X/2}.
\]
If \(|D_1(X)|\le C(1+X)^N\) for some finite \(C,N\), the primitive signed distribution is the derivative of a polynomially bounded function, up to a contact constant. It is tempered, and the theorem applies.

No such bound is proved here. Prime number theorem asymptotics alone give relative cancellation, not this polynomial bound. Quantum/TFD variance bounds for a random surrogate do not establish it for the deterministic prime sequence.

The general temperateness condition is the immediate domain target; this pointwise primitive bound is a sufficient, potentially stronger way to obtain it.

## 5. Consequence for the active sewing program

The remaining task can be confined to the primitive half-density channel and the pole continuum:
\[
\sum_p(\log p)p^{-1/2}\delta_{\log p}
\quad\text{versus}\quad e^{x/2}\,dx.
\]
The normal \(m=2\) channel, every higher repetition, the excited Gamma ladder, and the contact subtraction are already controlled in the tempered domain. This agrees with the parity determinant identity: the full even sector is governed by \(\zeta(2s)\), which is zero-free in \(\Re s>1/2\).

The sought TFD/Archimedean quotient should be tested for a continuous map into \(\mathcal S'\) on this one compensated primitive channel. If that continuity is actually proved with the exact arithmetic normalization, the Gaussian resolvent argument supplies the no-escape step. At present it remains the missing theorem.
