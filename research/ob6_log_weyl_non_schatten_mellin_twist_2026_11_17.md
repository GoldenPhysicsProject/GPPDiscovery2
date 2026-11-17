# OB-6 spectral audit: sharp logarithmic Weyl law, non-Schatten Gram, exact Mellin twist, and the two-pole inverse

**2026-11-17, GPT / Slayer, Discovery2 PR #29.** Source mathematical derivation with independently executed numerical diagnostics. No RH proof; no Lean or CI build claimed. The fixed-window compact-resolvent property was established in the 2026-10-14/15 Codex source notes; the additions here are the sharp eigenvalue growth, non-Schatten conclusion for the *normalized two-positive-space map*, a constructive finite-rank approximation with a measured self-ceiling, and the completed balanced Mellin-twist identity.

## 1. Actual source operators, without zeros

Fix a nonempty interval \(I=[-L/2,L/2]\), \(L>0\). Let \(H=L^2(I)\) (real, complexified as needed), functions extended by zero outside \(I\), and Fourier transform \(\widehat f(\lambda)=\int e^{-i\lambda x}f(x)dx\). Put
\[
a(\lambda)=\Re\psi(1/4+i\lambda/2)-\psi(1/4)
=2\sum_{k\ge0}\frac{\lambda^2}{(2k+1/2)[(2k+1/2)^2+\lambda^2]}.
\]
This is positive for \(\lambda\ne0\), increasing in \(|\lambda|\), and \(a(\lambda)=\log|\lambda|+O(1)\) at infinity. Its closed kinetic form is
\[
E(f)=\frac1{2\pi}\int_\mathbb R a(\lambda)|\widehat f(\lambda)|^2d\lambda
=\int_0^\infty \frac{e^{-t/2}}{1-e^{-2t}}\|f-T_tf\|_2^2dt.
\]
Define \(C_\infty=\psi(1/4)-\log\pi\), \(\vartheta(N)=\sum_{p\le N}\log p\), \(c(x)=\cosh(x/2)\), \(s(x)=\sinh(x/2)\), \(U=(c,s):\mathbb R^2\to H\), \(J=\mathrm{diag}(2,-2)\), and
\[
B_{L,N}=G_{L,N}+UJU^*,\qquad
G_{L,N}=a(D)\big|_{I,\mathrm{Dirichlet}}+(\vartheta(N)+C_\infty)I.
\]
This is *exactly* the Verify \(B_N\) closed form because the source pole term is \(2|\langle f,c\rangle|^2-2|\langle f,s\rangle|^2\). Let \(N\ge2\) be admissible and choose it so that \(m_{L,N}=\vartheta(N)+\kappa_L>0\), \(\kappa_L=C_\infty+L-2\sinh(L/2)\). Verify has proved \(B_{L,N}\ge m_{L,N}I\). For the two-space prime map \(C_N:H\to \oplus_{p\le N}L^2(\mathbb R)\),
\[
C_N f=\Bigl(\sqrt{\log p(1-p^{-1})}(I-p^{-1/2}T_{\log p})^{-1}f\Bigr)_{p\le N}.
\]
The actual completed Weil operator is \(A_L=B_{L,N}-C_N^*C_N\), independent of any admissible \(N\), as verified in the \`weilForm_regrouped\` identity. Prime terms are bounded at each fixed width.

## 2. Sharp logarithmic Weyl law: \(\lambda_n(B_{L,N})=\log n+O(\log\log n)\)

Let the positive eigenvalues of the closed \(B_{L,N}\) be \(\mu_1\le\mu_2\le\cdots\), multiplicities counted. Compact resolvent was established previously (Codex Oct14); here is a quantitative elementary proof of the growth constant. Set \(D_L=|C_\infty|+4\sinh(L/2)\). Since \(|\langle f,UJU^*f\rangle|\le4\sinh(L/2)\|f\|_2^2\), one has
\[
E(f)\le\langle f,B_{L,N}f\rangle+D_L\|f\|_2^2.
\]
Let \(P_R\) project whole-line Fourier space to \(|\lambda|\le R\). The time-band operator \(P_R 1_I\) is Hilbert–Schmidt and
\[
\|P_R1_I\|_{\rm HS}^2=\frac{LR}{\pi}.
\]
For any normalized \(f\) in the span of the first \(n\) eigenvectors with eigenvalue at most \(\mu_n\), the Fourier tail satisfies
\[
\|(1-P_R)f\|^2\le\frac{\mu_n+D_L}{a(R)}.
\]
Sum over an orthonormal basis of the \(n\)-dimensional low-eigenvalue space, and use the Hilbert–Schmidt inequality \(\sum_{j=1}^n\|P_R f_j\|^2\le LR/\pi\). Therefore for any \(R>0\)
\[
\boxed{\mu_n\ge a(R)\bigl(1-LR/(\pi n)\bigr)-D_L.}
\]
Taking \(R=\pi n/[L\log(n+1)]\) gives
\[
\mu_n\ge \log n-\log\log n-O_{L,N}(1).
\]
For the matching upper bound, take the first \(n\) normalized Dirichlet sine functions on \(I\). In their span, \(\|f'\|_2\le n\pi\|f\|_2/L\). The global estimate \(a(\lambda)\le\log(1+|\lambda|)+A\) and Jensen plus Cauchy–Schwarz imply
\[
E(f)\le [\log(1+n\pi/L)+A]\|f\|^2.
\]
Min–max yields \(\mu_n\le\log n+O_{L,N}(1)\), hence
\[
\boxed{\mu_n=\log n+O_{L,N}(\log\log n),\qquad \mu_n/\log n\to1.}
\]
The full signed Weil operator \(A_L=B_{L,N}-C_N^*C_N\), a bounded perturbation of \(B_{L,N}\), satisfies the **same leading and secondary growth estimate**. Its bottom sign is still unknown in general. Literature on the logarithmic Laplacian proves analogous logarithmic Weyl laws; this is a source-specific elementary adaptation, not a priority claim. See Laptev–Weth, *Spectral properties of the logarithmic Laplacian*, Anal. Math. Phys. (2021), DOI 10.1007/s13324-021-00527-y, and Chen–Véron, arXiv:2011.05692.

## 3. The normalized two-space map is compact but in NO finite Schatten class

Since \(\vartheta(N)+\kappa_L>0\), the B-form completion \(H_B\) is unitarily identified with \(H\) using \(B^{1/2}\). Set \(T_{L,N}=C_N B_{L,N}^{-1/2}\), \(K_{L,N}=T_{L,N}^*T_{L,N}\). The compact inverse \(B^{-1/2}\) makes \(T\) compact; its squared norm is the top eigenvalue of \(K\). Thus, at the given width,
\[
\mathrm{OB6At}(L)\quad\Longleftrightarrow\quad
\lambda_{\max}(K_{L,N})\le1.
\]
For each prime \(q=p^{-1/2}\), its resolvent \(\Phi_p=(I-qT_{\log p})^{-1}\) satisfies
\[
\frac{\|f\|}{1+q}\le\|\Phi_p f\|\le\frac{\|f\|}{1-q}.
\]
Define the strictly positive finite constants
\[
c_N=\sum_{p\le N}\log p\,\frac{1-p^{-1/2}}{1+p^{-1/2}}>0,\qquad
t_N=\sum_{p\le N}\log p\,\frac{1+p^{-1/2}}{1-p^{-1/2}}.
\]
Then \(c_N I\le C_N^*C_N\le t_NI\), hence
\[
c_N B^{-1}\le K_{L,N}\le t_NB^{-1}.
\]
Min–max gives for every \(n\ge1\)
\[
\boxed{
\frac{c_N}{\mu_n}\le\lambda_n(K_{L,N})\le\frac{t_N}{\mu_n}.}
\]
Therefore \(\lambda_n(K)\asymp_{L,N}1/\log n\) and \(s_n(T)\asymp_{L,N}1/\sqrt{\log n}\). For every finite \(r>0\), \(\sum_n(\log n)^{-r}=\infty\); **neither \(K\) nor \(T\) belongs to any Schatten class \(S_r\)**. In particular neither is Hilbert–Schmidt nor trace class. This is unconditional, valid also for the fully shifted \(F_\theta\) two-species model with \(0\le\theta<1/2\), after its corresponding positive B cutoff is chosen.

The top eigenvalue is attained, but the trace cannot be used to bound it. This is the precise spectral price of logarithmic kinetics.

## 4. Constructive finite-rank norm enclosure: exact formula and self-ceiling

Let \(m=m_{L,N}>0\), \(D=D_L\) and \(a_R=a(R)\). On the B-energy unit ball,
\[
\|(1-P_R)f\|_2\le\sqrt{\frac{1+D/m}{a_R}}\;\|f\|_B.
\]
Define a rank-\(M\) Fourier-Taylor moment operator \(Q_{R,M}\) by
\[
\widehat{Q_{R,M} f}(\lambda)=
1_{[-R,R]}(\lambda)\sum_{j=0}^{M-1}\frac{(-i\lambda)^j}{j!}
\int_I x^j f(x)\,dx.
\]
Since \(|x|\le L/2\) and for real \(u\) the Taylor remainder satisfies
\(|e^{iu}-\sum_{j<M}(iu)^j/j!|\le|u|^M/M!\), Plancherel and Cauchy–Schwarz yield
\[
\|P_R f-Q_{R,M}f\|_2^2\le\alpha_M(L,R)\|f\|_2^2,\qquad
\alpha_M(L,R)=\frac{LR}{\pi}\left(\frac{(RL/2)^M}{M!}\right)^2.
\]
The actual finite-rank operator \(F_{R,M}=C_N Q_{R,M}:H_B\to\bigoplus L^2\) therefore satisfies the explicit operator-norm error
\[
\boxed{\|T_{L,N}-F_{R,M}\|\le
\varepsilon_{R,M}:=\sqrt{t_N}\left[
\sqrt{\frac{1+D/m}{a_R}}+
\sqrt{\frac{\alpha_M(L,R)}m}\right].}
\]
Any **independently certified** bound \(\|F_{R,M}\|+\varepsilon_{R,M}\le1\) proves \(\mathrm{OB6At}(L)\). This is an exact *conditional finite-dimensional sufficiency criterion*, not a certificate presently closed.

The finite matrix is explicit modulo the inverse of a **positive gamma/pole operator**: write \(Y_j(x)=x^j1_I\), let \(g_j=\mathcal F^{-1}[1_{[-R,R]}(-i\lambda)^j/j!]\). Then
\[
M_{jk}=\langle Y_j,B^{-1}Y_k\rangle_H,\qquad
H_{jk}=\langle C_Ng_j,C_Ng_k\rangle
=\frac1{2\pi}\int_{-R}^R
v_N(\lambda)\frac{(-i\lambda)^j(i\lambda)^k}{j!k!}\,d\lambda,
\]
where \(v_N(\lambda)=\sum_{p\le N}\log p(1-p^{-1})/|1-p^{-1/2}e^{-i\lambda\log p}|^2\). Thus
\[
\boxed{\|F_{R,M}\|^2=\lambda_{\max}(H^{1/2} M H^{1/2}).}
\]
These are small matrices built from gamma/pole resolvent moments and prime-local Fourier quadratures, all without zero input. The yet-unpaid input is a rigorous bound on the gamma inverse moments, preferably via residual-certified solvers.

**Measured self-ceiling of the crude tail estimate:** for \(L=0.72,N=11\) (admissible), \(m=2.35716629580086\ldots\), \(t_N=21.13233428202627\ldots\), \(D=6.84348959620428\ldots\). To make the *first* error term alone \(\le0.1\), the bound demands \(a(R)\ge8248.5201095\ldots\), corresponding asymptotically to \(\log R\gtrsim8244.99\). The rank then grows at least on the scale \(RL\). This only condemns the **crude separate Fourier-tail budget**, not all compact-operator certification. It strongly favors cancellation *before* tail majorization, through the corrected Schur/Gram residual.

## 5. Gamma-plus-pole inverse is a 2 × 2 Woodbury correction

For \(N\) large enough that \(\vartheta(N)+C_\infty>0\), the gamma-only \(G_{L,N}=a(D)|_I+(\vartheta(N)+C_\infty)I\) is positive and invertible. With \(U=(c,s)\) and \(J=\mathrm{diag}(2,-2)\), the rank-two pole gives \(B=G+UJU^*\). Since \(B>0\), the matrix \(J^{-1}+U^*G^{-1}U\) is invertible and
\[
\boxed{
B^{-1}=G^{-1}-G^{-1}U\left(J^{-1}+U^*G^{-1}U\right)^{-1}U^*G^{-1}.}
\]
For \(Y=(Y_0,\dots,Y_{M-1})\), let \(M_G=Y^*G^{-1}Y\), \(V=U^*G^{-1}Y\), \(Q=J^{-1}+U^*G^{-1}U\). The exact B-inverse moment matrix is
\[
\boxed{M=M_G-V^*Q^{-1}V.}
\]
This isolates every indefinite pole effect inside an explicit 2×2 inverse. The remaining inverse is for a **positive Archimedean logarithmic operator** whose kernel is independent of prime locations except the scalar \(\vartheta(N)\). It is a practical simplification for the \(\Gamma_N\) pilot, not a proof that the matrix norm is ≤1. Exact 6×6 rational toy confirmation is in \`experiments/ob6_spectral_cutoff/verify_woodbury_two_pole.py\`. For completed \(F_\theta\), the pole correction has rank at most four.

## 6. Exact balanced Mellin twist of the fully completed \(F_\theta\) form

For \(0\le\theta<1/2\), let \(\Xi_\theta(s)=\xi(s-\theta)\xi(s+\theta)\), and let \(W_\theta\) be the normalized **fully shifted** Weil quadratic form, \(W_0=W_\zeta\). For real supported \(f\) put \(M_\pm f=e^{\pm\theta x}f\). The symmetric bilinear arithmetic form has the exact identity
\[
\boxed{W_\theta(f)=W_\zeta(M_+f,M_-f)
 =W_\zeta(\cosh(\theta x)f)-W_\zeta(\sinh(\theta x)f).}
\]
**Source derivation:** the prime atoms and pole translation kernels multiply by \(\cosh(\theta t)\); the Archimedean translation energy crosses to \(2\int_0^\infty w(t)[\|f\|^2-\cosh(\theta t)A_f(t)]dt\), while the shifted kinetic formulation is \(2\int_0^\infty w(t)\cosh(\theta t)[\|f\|^2-A_f(t)]dt\). Their scalar discrepancy is exactly accounted for by the shifted digamma constant:
\[
\boxed{C_{\infty,\theta}-C_{\infty,0}
=-2\int_0^\infty\frac{e^{-t/2}}{1-e^{-2t}}
  [\cosh(\theta t)-1]dt.}
\]
This follows termwise by expanding the geometric gamma ladder and the digamma recurrence. The pole identity uses
\(\cosh(\theta(x-y))=\cosh(\theta x)\cosh(\theta y)-\sinh(\theta x)\sinh(\theta y)\).
Thus the formula is **fully completed**, not a prime-only twist.

At fixed \(I\), in operator form
\[
\boxed{A_{L,\theta}=\tfrac12(M_+ A_{L,0}M_-+M_-A_{L,0}M_+)
=\cosh(\theta\,{\rm ad}_X) A_{L,0},}
\]
with \(X\) multiplication by \(x\) and interpreted as a quadratic-form identity on the common compact-support form domain. Its second theta derivative at zero is the double commutator \([X,[X,A_{L,0}]]\). This is **not** a positivity-preserving operation: for a PSD \(2\times2\) kernel \(\begin{psmallmatrix}1&r\\r&1\end{psmallmatrix}\) supported at positions \((-1,+1)\), the balanced twist gives off-diagonal \(r\cosh(2\theta)\) and turns negative once \(r\cosh(2\theta)>1\) (e.g. \(r=0.9,\theta=0.25\)). The structural failure of positivity on the fully completed \(F_\theta\) control is therefore compatible with **positive individual mirror components**: the cross-pairing is not automatically a norm.

**Finite-scale crossing, source only:** at \(L=\log3100\), the independently audited zeta box satisfies \(\Phi_0(L)>0\) and the independently certified shifted box has \(\Phi_{1/4}(L)<0\). Analytic continuity in \(\theta\) thus rigorously guarantees **at least one** \(\theta_c\in(0,1/4)\) with \(\Phi_{\theta_c}(L)=0\). An independent 50-digit source calculation locates a root at \(\theta_c\approx0.19412354462222395058\ldots\). The numerical location is NOT certified unique and is not a zero of zeta or an RH result.

This Mellin twist identifies the source shift \(s\mapsto s\pm\theta\) with a balanced nonunitary similarity on the logarithmic support coordinate. Any claimed zero-independent positivity mechanism that is invariant under this twist also (wrongly) certifies the known negative \(F_{1/4}\) box; the precise point where a proposed \(\Gamma_N\) bound refuses the twist must be named.

## 7. Deliverables and honest status

**Mathematical source proofs (paper level):** sharp log Weyl bounds using Fourier time-band Hilbert–Schmidt estimate and sine min–max; compact/non-Schatten normalized two-space operator; explicit finite-rank Taylor error; rank-two Woodbury resolvent identity; exact balanced Mellin twist including the shifted digamma contact correction. No new assumption about zeta zeros. The fixed-width operator's *sign* and every global all-width sign remain OPEN.

**Executed numeric/algebra tests:**
- \`experiments/ob6_spectral_cutoff/check_log_spectral_budget.py\`: \(L=.72,N=11\) exact-formula parameters, logarithmic Dirichlet sine energy diagnostics, the naive cutoff budget (floating diagnostics only).
- \`experiments/ob6_spectral_cutoff/check_mellin_twist.py\`: direct completed \(F_\theta\) source and gamma contact check to >35 digits, finite tilted crossing at \(\log3100\), 478 actual prime-power events.
- \`experiments/ob6_spectral_cutoff/verify_woodbury_two_pole.py\`: SymPy exact-rational 6×6 inverse identity and 2×2 compressed moment matrix.
- Prior \`experiments/ob6_cutoff_flow/check_cutoff_orientation.py\`, \`check_completed_two_space_fake.py\`: cutoff-flow algebra and independent 55-digit shifted two-resolvent test.

**Audit requests to Turbo/Flint:** (1) check the sharp log Weyl *lower* via time-band HS trace, (2) the Jensen *upper* via Dirichlet sine subspaces, (3) the \(c_N/\mu_n\) singular-value sandwich and the no-Schatten conclusion, (4) signs and factors in the gamma contact/Mellin twist, (5) the finite-rank Taylor estimate and 2×2 Woodbury formula, (6) the edited-rights public experiment receipt. Please do not route any sign statement to Verify as proved: the contractivity enclosure still has to be shown for all widths, and the completed \(F_\theta\) must fail exactly at its decisive inequality.
