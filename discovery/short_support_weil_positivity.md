# Exact all-dimensional completed Weil positivity on short windows

**2026-10-30 | Codex / GPPDiscovery2 | new self-contained theorem**

Scope: the actual completed one-sided semilocal Weil form \(Q_L\) defined in Daniel Toupin's v34 arithmetic principal-series manuscript. This is an **unconditional all-test-function** theorem for a restricted small support, not an RH proof, not an extrapolation from finite Fourier truncations. It holds on the full logarithmic form domain, including functions with infinitely many Fourier modes.

## Theorem (no-prime completed positivity at all \(0<L\le1/8\))

Let \(0<L\le1/8\). Let \(f\) be a complex \(L^2\) function supported on \([0,L]\) and with finite positive logarithmic kinetic energy, and let \(q_f(y)=2\operatorname{Re}\int_{\mathbb R}\overline{f(t)}f(t+y)\,dt\). The completed exact Weil quadratic form \(Q_L[f]\) satisfies

\[
\boxed{Q_L[f]\ \ge\ B_3(L)\,\|f\|_2^2\
\ge\ B_3(1/8)\,\|f\|_2^2\
>\frac{1}{25}\|f\|_2^2.}
\]

Here
\[
\begin{aligned}
B_3(L)={}&\log(2/L)+L-2\sinh(L/2)-[\log(4\pi)+\gamma]-2L/3\\
&+\frac12\log\frac{\tanh(L/2)}{\tanh(L/4)}
+\bigl(1-1/\sqrt2\bigr)\log\frac{\tanh(L/4)}{\tanh(L/6)}.
\end{aligned}
\]

Direct high-precision evaluation yields \(B_3(1/8)=0.0457249754421483788975168886\ldots\). For all \(0<L\le1/8<\log2\), the finite prime-power source is **empty** because \(p^r\ge2>e^L\). The theorem is genuinely about the completed archimedean-plus-pole form, not a local approximation that omits existing primes.

## Proof

The exact zero-extended positive gamma kinetic energy, **including its infinite tail**, is
\[
E_L[f]=\int_0^\infty\frac{q_f(0)-q_f(y)}{2\sinh y}\,dy.
\]
For all \(y>0\), the integrand is nonnegative because
\(q_f(0)-q_f(y)=\|f(\cdot+y)-f\|_2^2\). For \(y\ge L\), \(q_f(y)=0\), so
\[
E_L[f]\ge \|f\|_2^2\log\coth(L/2)
\ge\|f\|_2^2\log(2/L).
\]
(The last bound uses \(z\coth z>1\) for \(z>0\).)

We improve this crude bound on the inner support using the *exact truncated translation geometry*. For \(L/2\le y\le L\), split the interval into two consecutive y-wide layers. The truncated translation \(T_y f(t)=f(t+y)\) has \(T_y^2=0\). The Cauchy-Schwarz/AM-GM inequality on the two orthogonal layers gives
\[
q_f(y)=2\operatorname{Re}\langle f,T_y f\rangle\le\|f\|_2^2,
\qquad
q_f(0)-q_f(y)\ge\|f\|_2^2.
\]
For \(L/3\le y\le L/2\), the three-layer translation has \(T_y^3=0\). Write the layer norms \(a,b,c\). Then
\[
q_f(y)\le 2(ab+bc)\le
2\sqrt2 b\sqrt{a^2+c^2}
\le\sqrt2(a^2+b^2+c^2)=\sqrt2\|f\|_2^2,
\]
where the last inequality is \(2bu\le b^2+u^2\). Thus
\[
q_f(0)-q_f(y)\ge(2-\sqrt2)\|f\|_2^2.
\]
These inequalities remain valid when the terminal layer is shorter than y because of zero extension. Consequently
\[
\begin{split}
E_L[f]\ge\|f\|_2^2\Big[
\log\coth(L/2)&+\tfrac12\int_{L/2}^{L}\frac{dy}{\sinh y}\\
&+(1-1/\sqrt2)\int_{L/3}^{L/2}\frac{dy}{\sinh y}\Big].
\end{split}
\]
The elementary antiderivative \(\int dy/\sinh y=\log\tanh(y/2)\) gives the two explicit positive logarithms appearing in \(B_3(L)\).

The exact completed Weil form decomposition (see \`discovery/semilocal_log_kinetic_decomposition.md\`) is
\[
Q_L[f]=E_L[f]+P_L[f]-c_\infty\|f\|^2-A_L[f]-S_L[f]
\]
where \(P_L\) is the rank-two pole and \(c_\infty=\log4\pi+\gamma\). At these L, \(S_L=0\). The pole's *sharp* lower eigenvalue is \(L-2\sinh(L/2)\), so \(P_L[f]\ge[L-2\sinh(L/2)]\|f\|^2\). The regular gamma tilt satisfies
\[
|A_L[f]|\le2I(L)\|f\|^2,\qquad
I(L)=\int_0^L r(y)\,dy,\quad
r(y)=\frac{t^2}{(t+1)(t^2+1)},\quad t=e^{y/2}.
\]
For \(t\ge1\), \((t+1)(t^2+1)-3t^2=t(t-1)^2+1>0\), hence \(0\le r(y)<1/3\), giving \(2I(L)\le2L/3\). Combining the positive kinetic lower bound, sharp negative pole bound, gamma/contact terms and no-prime observation gives **exactly** \(B_3(L)\).

Finally \(B_3(L)\) is decreasing as L grows on \((0,1/8]\): \(\log(2/L)\) strictly decreases; \(L-2\sinh(L/2)\) decreases; \(-2L/3\) decreases. Each additional hyperbolic-band integral \(\int_{L/j}^{L/(j-1)}\mathrm{csch}\,y\,dy\) decreases with L, since after scaling it is \(\int_{1/j}^{1/(j-1)}L/\sinh(Lt)\,dt\), and \(z/\sinh z\) decreases for z>0. Therefore the worst endpoint is \(L=1/8\).

**Arb verification:** \`discovery/arb_short_support_weil_certificate.py\` evaluates the exact constant \(B_3(1/8)\) with outward-rounded FLINT/Arb and asserts the rigorous inequality \(B_3(1/8)>1/25\). The analytical proof covers the *infinite-dimensional* form, not just the numerical endpoint.

## Extension toward prime windows

For \(L\ge\log2\), genuine prime-power atoms enter the form. The same methods produce a valid (usually crude) universal bound
\[
Q_L[f]\ge\bigl[B_3(L)-2\!\sum_{p^r\le e^L}(\log p)p^{-r/2}\bigr]\|f\|^2,
\]
which becomes negative long before \(\lambda=2.5\). The central arithmetic task is to prove a **signed/nonlocal**, rather than absolute-value, prime–gamma–pole compensation. No claim of Weil positivity at general L or RH is made.

### Research significance

This supplies a genuine, quantitatively explicit, all-\(N\) positive base window in the exact completed semilocal operator, rather than merely certifying finite Fourier sections. The method uses the causal nilpotence of *time-window translations*, linking the arithmetic log-shift semigroup to a positive gamma coercivity estimate. It does not yet provide an induction on increasing support, since new prime shifts and coupling between separated windows must be paid for with a global noncircular bound.

Provenance: v34 exact Weil form, positive log-kinetic decomposition and corrected gamma diagonal; new two-/three-layer nilpotent numerical-radius bounds.
