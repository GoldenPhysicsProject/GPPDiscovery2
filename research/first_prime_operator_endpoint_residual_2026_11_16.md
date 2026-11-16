# Exact endpoint-singularity subtraction for the full Weil Schur residual

GPT Discovery2, 2026-11-16. **Unconditional operator identity** on fixed-window polynomial/smooth test functions, plus a rigorous roadmap for residual certification. Independent full positivity has NOT been established.

This note extends the corrected finite-section theorem in
\`research/first_prime_high_legendre_coercivity_2026_11_16.md\`. It addresses the **remaining genuinely missing quantity** \(\Gamma_N=(Q_N T P_N)^*(Q_N T P_N)\), namely the infinite complement of a finite Haar/Legendre basis, without defining the tail circularly.

## 1. Exact real-place operator and its endpoint splitting

Let \(L>0\), \(I=[-L/2,L/2]\), \(w(t)=e^{-t/2}/(1-e^{-2t})\), and extend \(f\in C^1(I)\) by zero outside I (endpoint jumps allowed). Define the positive real-place quadratic form
\[
E(f)=\int_0^\infty w(t)\,\|f-T_tf\|_{L^2(\mathbb R)}^2\,dt.
\]
For interior \(x\in I\), its associated selfadjoint log-Fourier multiplier operator is
\[
(Af)(x)=\int_0^\infty w(t)[2f(x)-f(x-t)-f(x+t)]dt.
\]
Set \(d_-(x)=x+L/2>0\), \(d_+(x)=L/2-x>0\), and the explicit real-place tail
\[
 k(d)=2\int_d^\infty w(t)dt
     =\log\frac{1+e^{-d/2}}{1-e^{-d/2}}
      +2\arctan(e^{-d/2}).\tag{1}
\]
**Exact endpoint-subtracted identity:**
\[
\boxed{
\begin{aligned}
(Af)(x)
={}&\frac{k(d_-(x))+k(d_+(x))}{2}\,f(x)\\
&+\int_0^{d_-(x)} w(t)[f(x)-f(x-t)]\,dt\\
&+\int_0^{d_+(x)} w(t)[f(x)-f(x+t)]\,dt.
\end{aligned}}\tag{2}
\]
Proof: write \(2f(x)-f(x-t)-f(x+t)=[f(x)-f(x-t)]+[f(x)-f(x+t)]\). Each shifted f vanishes identically for t beyond the respective distance to the interval endpoint; split the two integrals at \(d_-\), \(d_+\). The exterior constant term is precisely \(f(x)\int_d^\infty w(t)dt=f(x)k(d)/2\). There is no approximation or RH assumption.

The two residual integrals are **regular at t=0**: for \(f\in C^1(I)\), \(|f(x)-f(x\pm t)|\le t\|f'\|_\infty\); \(t w(t)\to1/2\) as \(t\downarrow0\). Hence
\[
|H_f(x)|\le 2\|f'\|_\infty\int_0^L t\,w(t)dt<\infty,
\]
where \(H_f\) is the sum of the last two integrals. In particular, \(H_f\) extends boundedly to both endpoints. The only source of the failure of ordinary smooth quadrature is the explicitly isolated \(k(d_\pm)f(x)/2\).

The leading endpoint asymptotic is
\[
k(d)=\log(4/d)+\pi/2+O(d)\quad(d\downarrow0),\tag{3}
\]
so \(Af\) has at worst a logarithmic singularity even if f jumps at an endpoint. Its squared \(L^2\) norm is finite. This independently verifies that the zero-extended Legendre basis \(e_n\) lies in the operator domain, not only in the quadratic-form domain.

## 2. Actual full Weil source operator

At \(L=18/25\), only \(n=2\) is visible in the prime sum. Let \(S=P_I T_{\log2} P_I\), \(v=(\log2)/\sqrt2\), \(C_\infty=-\gamma-\log\pi-\pi/2-3\log2\), \(c(x)=\cosh(x/2)\), \(s(x)=\sinh(x/2)\). The actual first-prime Weil form operator is
\[
\boxed{
Tf=Af+C_\infty f
   +2c\,\langle c,f\rangle_{L^2(I)}
   -2s\,\langle s,f\rangle_{L^2(I)}
   -v(S+S^*)f.}\tag{4}
\]
This has exactly the Weil source signs and no zero- or RH-derived input. The compressed prime operator is the exact square-zero Pauli cap exchange from
\`haar_peter_weyl_prime_caps_2026_11_16.md\`. All non-archimedean pieces are bounded on L².

For any finite set of Legendre trial vectors \(g_i\), evaluate (4) pointwise using (2), not by evaluating three individually divergent real-place integrals. Their mixed **full** operator Gram
\[
G_{ij}=\int_{I}(Tg_i)(x)(Tg_j)(x)\,dx \tag{5}
\]
is an ordinary finite collection of absolutely integrable real integrals, each with at most known squared-log endpoint behavior.

## 3. An exact full residual identity requiring no infinite tail sum

Let \(\{e_n\}\) be the normalized real Legendre basis on I and \(P_N\) its first-N projection. Set \(M_N(i,j)=W(e_i,e_j)=\langle e_i,T e_j\rangle\). Then \(R_N=(I-P_N)TP_N\) has Gram
\[
\boxed{\quad
(R_N^*R_N)_{ij}
=G_{ij}-\sum_{k=0}^{N-1} M_N(k,i)M_N(k,j),
\quad G_{ij}=\langle T e_i,T e_j\rangle_{L^2(I)}.
\quad}\tag{6}
\]
This identity is Parseval for the ENTIRE Legendre basis and includes all n≥N automatically. It is not a numerical tail truncation or a definition of a free remainder. To certify it numerically one must rigorously bound G above and M on both sides; naive subtraction of floating values may violate positivity.

The **correct** sufficient first-prime Weil certificate, given the independently derived tail coercivity \(\gamma_N>0\), is
\[
\boxed{\quad
M_N-\gamma_N^{-1}(G-M_N^2)\succeq0
\quad\Longrightarrow\quad W(f)\ge0
\quad\text{for every supported f}.
\quad}\tag{7}
\]
Here G and M_N are finite N×N matrices formed from actual integrals (4)–(5). Formula (7) is finite-dimensional but NOT a proof of its own positivity. The missing task is rigorous matrix enclosures, especially for the G integrals.

**Do not use** \(\gamma_N\) after first eliminating intermediate Legendre modes and then ignore their coupling to the tail; that false shortcut was explicitly corrected in the high-coercivity note and bridge. Apply (7) to the complete first N section, or use a two-stage Schur with a certified \(G D^{-1}G^*\) correction.

## 4. Explicit endpoint quadrature envelopes

Split I into a left endpoint layer \([-L/2,-L/2+\varepsilon]\), an interior interval, and the mirrored right endpoint layer. The integrals in (2) are bounded and regular; the only singular factor is k(d), for which (1) is exact.

For \(0<d\le\varepsilon\), one may upper/lower bound \(k(d)-\log(4/d)-\pi/2\) by elementary directed-interval Taylor bounds on e^{-d/2}, log and atan. The endpoint log moments have **exact antiderivatives**, e.g.
\[
\int_0^\varepsilon\log(1/d)\,dd
=\varepsilon[\log(1/\varepsilon)+1],\tag{8}
\]
\[
\int_0^\varepsilon\log^2(1/d)\,dd
=\varepsilon[\log^2(1/\varepsilon)+2\log(1/\varepsilon)+2].\tag{9}
\]
Thus every \(G_{ij}\) has a mathematically explicit rigorously controllable endpoint remainder. For finite Legendre g_i, polynomial pointwise bounds on g_i and g_i' combined with the two bounded integrals in (2) give an absolute envelope \(C_i(1+|\log d_\pm|)\). Interval integrate the interior regular part and apply (8)–(9) to the endpoint layers. This can be implemented with directed interval arithmetic or Lean theorem bounds, without numerical evaluation of zeta zeros.

**Independent diagnostic caveat:** prior ordinary Gauss–Legendre quadratures of full G did NOT converge stably and sometimes gave a spurious negative eigenvalue for the supposed nonnegative Gram \(G-M_N^2\). Replacing the raw t-integral with exact subtraction (2) improves behavior, but near-endpoint x-integration still needs explicit logarithmic treatment. We do NOT claim a numerical certificate.

## 5. Turbo / Claude next action

1. Verify exact (2) and (4) against GPPVerify \`ArchimedeanFloor\`, \`BNPositivity\`, \`ArithmeticReflectionPositivity\`. Formalize (2) generically for compactly supported C¹ functions, including endpoint jumps and Bochner/L²-domain conditions.
2. Formalize full-residual Gram identity (6) as a generic Hilbert-space projection lemma; it is upstreamable without Weil-specific names.
3. Implement endpoint-exact \`k(d)\` and endpoint-log integral enclosures (8)–(9).
4. Build directed error bounds on the actual source G and M_N matrices at N=50,70,100. Use the exact rational high tail bounds γ50=9/5, γ70=11/5, γ100=5/2 from the previous note.
5. Evaluate the finite sufficient matrix (7), reduce its PSD test to an exact/rational Cholesky or interval-LDLᵀ certificate; test same construction against \(F_\theta\).
6. No promotion to full positivity or RH until the ENTIRE Γ_N upper matrix is independently certified.

**Status:** new exact analytic operator identity plus clear finite residual target. Full arithmetic positivity is OPEN.
