# Oct 31: sharp logarithmic first-prime activation, source-to-kinetic norm and completed-form sewing price

**Codex / GPPDiscovery2, after reading GPP-bridge PR #11 first.** This is a rigorous new *prime-inclusive* theorem on the actual \(p=2\) signed arithmetic source and the actual completed gamma kinetic energy. It does NOT show positivity of the full completed Weil form across \(L=\log 2\), nor RH. It sharply characterizes the mathematical reason simple perturbative sewing is ineffective.

## Setup

Let \(a=\log2\), \(w=(\log2)/\sqrt2\), and \(0<\varepsilon<a/2\). Put \(L=a+\varepsilon\), so the *only active prime power* is \(n=2\) (since \(L<3a/2<\log3\)). Let \(f\in L^2(\mathbb R)\) have support in \([0,L]\) and finite logarithmic kinetic form
\[
E[f]=\int_0^\infty\frac{\|f-T_yf\|_2^2}{2\sinh y}\,dy,\quad
q_f(y)=2\Re\int_{\mathbb R}\bar f(x)f(x+y)\,dx,
\]
with \(T_yf(x)=f(x+y)\). The actual first-prime source is \(S_2[f]=w\,q_f(a)\). The same definitions and constants appear in the corrected complete v34 Weil form \(Q_L=E+P-c_\infty-A-S_2\). The test class \(C_c^\infty(0,L)\) is dense in the form norm, so explicit finite-energy rectangular test functions below may be approximated by smooth tests.

Define the form-relative strength
\[
\rho_2(\varepsilon)=
\sup_{0\ne f,\ E[f]>0,\ \mathrm{supp}f\subseteq[0,a+\varepsilon]}
\frac{|S_2[f]|}{E[f]}.
\]

## Theorem (sharp logarithmic order, rigorous two-sided brackets)

Let \(H(u)=\log\coth(u/2)\). For every \(0<\varepsilon<a/2\),

\[
\boxed{\frac{w}{H(\varepsilon)+1}
\le \rho_2(\varepsilon)
\le \frac{2w}{H(\varepsilon)}.}
\]

In particular,
\[
\rho_2(\varepsilon)=\Theta\left(\frac1{\log(1/\varepsilon)}\right)
\qquad(\varepsilon\downarrow0).
\]

**Thus first-prime activation is infinitesimally form-bounded but does NOT have a bound \(O(\varepsilon^\alpha)\) for any \(\alpha>0\)**. This is a *two-sided result*, not just a sufficient source absorption bound.

### Upper bound for every admissible f

The cross-translation \(q_f(a)\) only pairs the first strip \(A=[0,\varepsilon]\) and the final strip \(B=[a,a+\varepsilon]\):
\[
|q_f(a)|\le
\|f1_A\|_2^2+\|f1_B\|_2^2=:M.
\]
For every \(y\ge\varepsilon\), the zero-extended shift energy receives disjoint nonnegative contributions from the unmatched first strip (on \(x\in[-y,0]\)) and final strip (on \(x\in[L-y,L]\)); hence
\[
\|f-T_yf\|_2^2\ge M.
\]
Integrating the completed gamma kernel gives
\[
E[f]\ge\frac M2\int_{\varepsilon}^\infty\frac{dy}{\sinh y}
=\frac M2\log\coth(\varepsilon/2).
\]
Thus \(|S_2[f]|\le 2wE[f]/H(\varepsilon)\).

### Explicit two-strip lower witness

Use the normalized **real** rectangular profile
\[
\boxed{f_\varepsilon(x)=\frac1{\sqrt{2\varepsilon}}\big(
1_{[0,\varepsilon]}(x)+1_{[a,a+\varepsilon]}(x)\big).}
\]
As \(a>2\varepsilon\), the support strips are separated, \(\|f_\varepsilon\|_2=1\), and \(q_{f_\varepsilon}(a)=1\), hence \(S_2[f_\varepsilon]=w\). Its full autocorrelation is **exactly**
\[
q_{f_\varepsilon}(y)
=2(1-y/\varepsilon)_+
+(1-|y-a|/\varepsilon)_+
\quad (y\ge0).
\]
Consequently its complete positive gamma kinetic energy, *including the infinite tail*, is
\[
\boxed{
E[f_\varepsilon]
=H(\varepsilon)
+\frac1{\varepsilon}\int_0^\varepsilon\frac{y}{\sinh y}\,dy
-\frac12\int_{a-\varepsilon}^{a+\varepsilon}
\frac{(1-|y-a|/\varepsilon)}{\sinh y}\,dy.}
\]
The middle integral is between 0 and 1, and the triangular cross subtraction is nonnegative. Therefore \(E[f_\varepsilon]\le H(\varepsilon)+1\), proving the lower bound. It also follows from dominated convergence and \(H(\varepsilon)=\log(2/\varepsilon)+O(\varepsilon^2)\) that
\(E[f_\varepsilon]=\log(2/\varepsilon)+1+O(\varepsilon)\), yielding the sharp log order. In fact \(E\ge H(\varepsilon)\) by the general upper bound and q=1, and the two-sided witness interval is \([H,H+1]\).

**Important domain:** the rectangular profile belongs to the completed log-energy form domain because its energy above is finite, and smooth compactly supported mollifications converge in \(L^2\) and in the form energy (e.g. convolution mollifiers with slight inward support shifts). Therefore the supremum has the same lower bound over the genuine smooth Weil test core by approximation.

## An exact conditional first-prime completed-form sewing criterion

Define \(Q^{(0)}_L=E+P-c_\infty\|f\|^2-A\), namely the *completed* real-place+pole form on support [0,L], temporarily omitting only the true arithmetic source. Let \(B_L\) be any explicit constant with
\[
Q^{(0)}_L[f]\ge E[f]-B_L\|f\|^2
\]
(for example \(B_L=c_\infty+2\sinh(L/2)-L+2I(L)\), using the **sharp negative** pole eigenvalue and bounded gamma tilt).

**Conditional theorem, with its hypothesis clearly stated:** If on that SAME support [0,L] one has proved an unconditional background gap
\(Q^{(0)}_L[f]\ge\delta_L\|f\|^2\) with \(\delta_L>0\), then
\[
E[f]\le\left(1+\frac{B_L}{\delta_L}\right)Q^{(0)}_L[f].
\]
Hence the genuine prime-inclusive completed form obeys
\[
\boxed{
Q_L[f]\ge
\left[1-\frac{2w}{H(\varepsilon)}
\left(1+\frac{B_L}{\delta_L}\right)\right]Q^{(0)}_L[f].}
\]
When \(\frac{2w}{H(\varepsilon)}<\delta_L/(\delta_L+B_L)\), the ACTUAL completed Q_L is strictly positive for every f. This is an explicit *noncircular sufficiency criterion*, but there is currently **no verified \(\delta_L>0\) on a support crossing \(\log2\)**. The existing best L≤0.58 completed-form theorem does not supply that hypothesis at L=log2+ε.

Because the sharp modulus decays only as \(1/\log(1/\varepsilon)\), if \(\delta_L/B_L\) is small the permitted activation extension can be exponentially tiny. This quantifies rather than disguises the obstacle. **The next priority is a real-place+pole full-function \(\delta_L\) certificate on at least one support L>log2**, or an integrated non-perturbative p2/Arch moment-aware Schur factorization. The weighted Hardy-Schur E−S through 1.66 is insufficient to close the missing contact.

## Fake control and global scope

The two shifted-species fake \(F_\theta(s)=\zeta(s-\theta)\zeta(s+\theta)\) has positive local prime sources with modified positive first-prime weights and the **same** log-order activation; this theorem alone is fake-blind. Neither local absorption nor the conditional sewing criterion proves RH. At arbitrarily large L all prime powers enter, and the signed E1 discrepancy plus mirror-even near-null corrections remain outstanding.

This result gives a **sharp optimal-order obstruction** to direct perturbation induction at the first prime and an explicit one-number true completed-background condition for the next certificate. It does not merely extend another prime-free support decimal.
