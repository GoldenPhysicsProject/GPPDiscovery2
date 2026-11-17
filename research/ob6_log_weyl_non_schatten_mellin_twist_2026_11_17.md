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


## 8. An actual first-prime width pilot from the complete source, not zero data

The companion \`experiments/ob6_spectral_cutoff/galerkin_two_pole_source.py\` independently assembles the **entire** width-\(L=0.72\) form in the Dirichlet sine basis from the closed gamma kinetic, rank-two pole, and the only supported von Mangoldt event \(n=2\). Use \(N=11\), \(\vartheta(N)=\sum_{p\le11}\log p\) and \(v_2=\log2/\sqrt2\). In the normalized sine basis \(\phi_j(x)=\sqrt{2/L}\sin(j\pi(x+L/2)/L)\), exact elementary overlap integration yields, for \(t\in[0,L]\),
\[
S_{nn}(t)=(1-t/L)\cos(k_nt)+\frac{\sin(k_nt)}{k_nL},
\quad k_n=n\pi/L,
\]
\[
S_{nm}(t)=
\begin{cases}
0,&n+m\ \text{odd},\\
\frac{2[k_n\sin(k_mt)-k_m\sin(k_nt)]}{L(k_n^2-k_m^2)},&n+m\ \text{even},\,n\ne m.
\end{cases}
\]
The gamma matrix is obtained by directly integrating
\[
E_{nm}=2\int_0^L w(t)[\delta_{nm}-S_{nm}(t)]dt+
2\delta_{nm}\bigl[\operatorname{atanh}(e^{-L/2})+\arctan(e^{-L/2})\bigr].
\]
Together with \(U=(\langle\phi_n,\cosh(x/2)\rangle,\langle\phi_n,\sinh(x/2)\rangle)\), assemble
\(G=E+(\vartheta(11)+C_\infty)I\),
\(B=G+U\,\mathrm{diag}(2,-2)U^*\),
\(V=\vartheta(11)I+2v_2S(\log2)\).
The exact identities \(W=B-V=E+C_\infty I+UJU^*-2v_2S(\log2)\) and Woodbury \(B^{-1}\) are verified numerically inside the code; representative sine overlap entries were also independently checked against direct spatial quadrature.

**Floating-point diagnostics (NOT outward-certified):**

| sine modes \(M\) | largest generalized eigenvalue of \(Vx=\lambda Bx\) | smallest Euclidean eigenvalue of \(W_M\) |
|---:|---:|---:|
| 4 | 0.99985340606846 | 0.0011355532 |
| 8 | 0.99986798160470 | 0.0010226303 |
| 12 | 0.99986825231423 | 0.0010205335 |
| 20 | 0.99987108384306 | 0.00099860066 |
| 32 | 0.99987676260939 | 0.00095461446 |
| 48 | 0.99988186476824 | 0.00091509492 |
| 64 | 0.99988349872877 | 0.00090243806 |
| 100 | 0.99988584951998 | 0.00088422902 |

At \(M=100\), split into six low and 94 high sine modes; the **finite** high block bottom is about 1.36284, and the full finite Schur complement's smallest eigenvalue about 0.0008842962. This is encouraging for the *single-width proving ground*, but it is **not an inequality on the infinite high complement**. These Ritz tests lower-bound the true \(\lambda_{\max}(K)\); being below one does not certify continuum contractivity. The sharp all-width obstruction remains untouched.

**The actual next calculation:** use the *existing* six-moment theorem at width 0.72 (Discovery2 \`first_prime_legendre_6_2026_11_16.md\`: rational full high-block energy coercivity \(119/9559\)) to obtain an independently bounded full residual \(R=B-DZ\) for a finite Galerkin approximation of the six-dimensional Schur block. The signed pole can be removed from the positive gamma inverse with the \(2\times2\) Woodbury formula above; the remaining source error needs an **honest** infinite-complement energy-dual bound, not a further growing Ritz matrix. The novel Fourier-Taylor error from §4 is mathematically valid but too expensive as the *only* tail estimate. Preserve the fully completed \(F_{1/4}\) shifted control as the exact falsifier.

## 9. Conditional strict spectral gap on each finite window (not a proof)

Under **RH as an assumption**, the Weil explicit formula becomes a sum of nonnegative squares of Fourier/Mellin samples at all critical ordinates. If \(W_\zeta(f)=0\) for a supported nonzero test, every such Fourier sample vanishes. The transform of a compactly supported \(L^2\) function is an entire function of exponential type \(L/2\), whose zero-counting function is \(O_L(T)\) unless it vanishes identically. The actual zeta zero count grows \(N_\zeta(T)\asymp T\log T\). Thus under RH, \(W_\zeta(f)=0\) forces \(f=0\), including the B-form closure by continuity and finite-sum lower bounds.

Since \(K_{L,N}\) is compact, the top eigenvalue is attained. Under RH it cannot equal one, so
\[
\mathrm{RH}\ \Longrightarrow\ \|T_{L,N}\|<1
\quad\text{for every coercive fixed }(L,N).
\]
Conversely, strict contractivity for a cofinal sequence of widths implies OB6 and hence RH by the in-tree theorem. This gives a **conditional strict-gap reformulation**, consistent with the proven collapse of any *uniform-in-width* margin. The RH assumption is load-bearing in the argument, and no method for proving these gaps unconditionally is supplied here. Audit the extension of the critical-line spectral squares to the B-form closure before formalizing this corollary.


## 10. A better exact inverse: parity splits the signed 2×2 Woodbury matrix into TWO SCALARS

This improves §5. The centered interval I is invariant under \(Rf(x)=f(-x)\). The zero-extended kinetic \(a(D)|_I\) and \(G_{L,N}\) commute with R. The pole vectors \(c(x)=\cosh(x/2)\) and \(s(x)=\sinh(x/2)\) satisfy \(Rc=c,\ Rs=-s\). Hence \(G^{-1}\) also commutes with R, and
\[
\boxed{\langle c,G^{-1}s\rangle=0.}
\]
Thus the Woodbury \(2\times2\) correction matrix is **DIAGONAL**:
\[
J^{-1}+U^*G^{-1}U
=\operatorname{diag}\bigl(\tfrac12+\alpha,-\tfrac12+\beta\bigr),\quad
\alpha=\langle c,G^{-1}c\rangle,\quad \beta=\langle s,G^{-1}s\rangle.
\]
If \(G>0\), then
\[
B=G+2cc^*-2ss^*>0
\ \Longleftrightarrow\ 
\boxed{2\beta<1}
\]
because the even block \(G_++2cc^*\) is automatically positive, and the odd block \(G_--2ss^*\) obeys the sharp rank-one criterion. In this regime
\[
\boxed{
B^{-1}=G^{-1}
-\frac{2}{1+2\alpha}(G^{-1}c)(G^{-1}c)^*
+\frac{2}{1-2\beta}(G^{-1}s)(G^{-1}s)^*.}
\]
So the finite inverse-moment matrix in §5 requires only **two scalar resolvent numbers**, not a general \(2\times2\) inverse. The even pole decreases the inverse; the odd pole increases it. This is an exact separation of the two bound-state channels; it gives no positive sign for \(B-C^*C\) on its own.

At \(L=.72,N=11\), 24-mode source Galerkin yielded \(\alpha\approx0.11040413247320424\), \(\beta\approx0.000936345930310688\), mixed entry \(<10^{-18}\), and hence \(1-2\beta\approx0.99812730814\). Direct parity-Woodbury inverse agreed with the complete 24-mode inverse to \(8.4\times10^{-17}\). These are **floating numerical illustrations** of the exact parity theorem, not a continuum certificate.

## 11. The first-prime *healed bound state*: a scalar Krein criterion for the even Weil sector

Let the actual **pole-removed** source operator on \(H=L^2(I)\) be
\[
H_L=a(D)|_I+C_\infty I
-2\sum_{\log n<L}\frac{\Lambda(n)}{\sqrt n}\,
\tfrac12(T_{\log n}+T_{-\log n})\big|_I,
\]
with the convention \(\langle f,H_Lf\rangle=E(f)+C_\infty\|f\|^2-
2\sum v_n A_f(\log n)\); here \(T_t+T_{-t}\) is the symmetric compression, and each coefficient is chosen so that its quadratic is \(2v_n A_f(t)\). It commutes with reflection. Denote its even and odd restrictions by \(H_+\), \(H_-\), with the same \(c,s\) as §10. The **full** source Weil operator is
\[
\boxed{W_+=H_+ +2cc^*,\qquad W_-=H_--2ss^*.}
\]

**Abstract rank-one healing theorem.** Let \(H_+\) be selfadjoint, invertible, bounded below, with compact resolvent, **exactly one negative eigenvalue** \(-a\), \(a>0\), and strictly positive remaining spectrum bounded below by \(b>0\). Let \(c\) be any nonzero vector. Then
\[
\boxed{H_++2cc^*\succeq0
\quad\Longleftrightarrow\quad
1+2\langle c,H_+^{-1}c\rangle\le0.}
\]
Proof: split \(H_+=-a\,ee^*+H_{\rm pos}\), \(c=\gamma e+d\), \(d\perp e\). The positive lower block is \(H_{\rm pos}+2dd^*>0\). Schur complement of that block is \(-a+2|\gamma|^2/(1+2\langle d,H_{\rm pos}^{-1}d\rangle)\). This is nonnegative iff \(2|\gamma|^2\ge a[1+2\langle d,H_{\rm pos}^{-1}d\rangle]\), which is precisely \(1+2[-|\gamma|^2/a+\langle d,H_{\rm pos}^{-1}d\rangle]\le0\). This proof does not pay the smallest **healed** Weil eigenvalue; it inverts the **unhealed** operator whose negative mode is separated from zero. It generalizes immediately to any positive rank-one coefficient \(t\).

Similarly, if the pole-removed odd operator is strictly positive, then
\[
\boxed{H_--2ss^*\succeq0
\quad\Longleftrightarrow\quad
2\langle s,H_-^{-1}s\rangle\le1.}
\]

**Finite source diagnostics; NOT infinite-dimensional certification.** The source-only 48-mode sine Galerkin at \(L=.72,N=11\) has the following values:

| sector | unhealed \(H\) spectrum near bottom | healed full \(W\) bottom |
|---|---|---|
| even | \(-1.33296384,\ +0.52577364,\ +1.10506433,\dots\) | \(+0.0009150949\) |
| odd | \(+0.06482933,\ +0.91117579,\dots\) | \(+0.0521888367\) |

At 48 even modes (24 parity-even sine vectors), the scalar is
\[
\langle c,H_+^{-1}c\rangle\approx-0.5004078247260165,\quad
1+2\langle c,H_+^{-1}c\rangle\approx-0.000815649452033.
\]
The **critical pole coefficient** for this truncated model is \(-1/\langle c,H_+^{-1}c\rangle\approx1.99837003058\); the true coefficient is \(2\). In contrast, the pole-removed even source is **strongly indefinite** with one negative eigenvalue near \(-1.333\). The rank-one positive pole heals that isolated negative bound state and leaves a thin positive residual. The odd no-pole block is already positive, and its negative pole reduces but does not erase the finite gap. This strongly suggests the small first-prime obstruction is a **single even bound-state compensation**, not a failure of the gamma high-frequency tail.

**Independent check:** \`experiments/ob6_spectral_cutoff/verify_parity_pole_scalar.py\` uses exact SymPy rational matrices to check the abstract inertia/scalar equivalence, then the source-only 48-mode Galerkin to check parity blocks, spectral indices, \(q=\langle c,H_+^{-1}c\rangle\), and the odd criterion. These numbers must not be used as proof of the continuum spectral index or infinite resolvent scalar.

**A concrete alternative Phase1 proving-ground target:** at \(L=18/25\), certify (i) the infinite pole-removed even operator \(H_+\) has exactly one negative eigenvalue, with a nonzero spectral gap around zero; (ii) \( \langle c,H_+^{-1}c\rangle\le-\frac12\) by a certified resolvent-vector and full residual norm bound; (iii) the odd operator \(H_-\) is strictly positive with \(2\langle s,H_-^{-1}s\rangle\le1\). Then **full** width-.72 Weil positivity follows without the six-moment Schur matrix. Compare the cost with the existing six-moment residual-certified route; whichever certifies first wins the proving ground. Across **all** widths, the source index and the scalar threshold are not proved and remain independent obligations. The fully completed \(F_{1/4}\) control must be run through exactly this parity-resolvent mechanism before any promotion to an all-width claim.

**Strict limitation:** even an all-width proof that the pole-removed operator has at most one negative direction is only a necessary part of the even task; the sharp scalar compensator condition still decides whether the source Weil form is nonnegative. This is a *different decomposition of the same wall*, not a shortcut proving RH.


## 12. Source correction: \(L=.72\) IS ALREADY PROVED in Lean; the useful frontier is \(L=1.15\)

**Important bibliographic and campaign correction.** The direct theorem
\[
\boxed{\texttt{GppWindowBL036.weilForm\_autocorr\_nonneg\_l036\_unconditional}}
\]
already exists on **GPPVerify/main**, file \`GppVerify/RiemannHypothesis/WindowBL036.lean\`, blob \`9ffe8edcb9af2a27c6f5b19273699863e9b89d7a\`. It proves \(W_\zeta(f)\ge0\) for **all real smooth tests supported on \([-9/25,9/25]\)**, precisely full width \(L=18/25=.72\), using an independently kernel-checked 100-piece digamma minorant. Its source explicitly states no custom axioms/sorries. This predates the present research: our 6-moment and sine-Galerkin pilots at width .72 should be classified as **alternative geometric decompositions and reproduction tests**, NOT attempts at the first full proof at that width. No separate positivity certificate at .72 is owed.

The legitimate continuation is **width \(L=1.15\)**, where the prime powers \(2\) and \(3\) both enter. The new source-only program \`experiments/ob6_spectral_cutoff/galerkin_parity_two_primes.py\` evaluates each actual prime power \(p^k<e^L\) and includes a controlled *remove-prime-3* experiment. At 48 Dirichlet sine modes (24 in each parity), it finds:

| Width \(L\) | unhealed even negative eig | next unhealed even positive eig | even scalar \(F_L(0)\) | full even Ritz bottom | full odd Ritz bottom |
|---:|---:|---:|---:|---:|---:|
| 0.72 | −1.33296384 | +0.52577364 | −8.15649e−4 | +9.15095e−4 | +5.21888e−2 |
| 1.05 | −2.06879340 | +0.00400343 | −2.36830e−7 | +3.03937e−7 | +5.44377e−5 |
| 1.15 | −2.27247979 | +0.00031562 | −8.37179e−9 | +1.10410e−8 | +3.71337e−6 |

Here \(F_L(0)=1+2\langle c,H_+(L)^{-1}c\rangle\) is the exact Krein scalar *evaluated in the finite Galerkin space*. None of these 48-mode positivity readings are rigorous for the infinite operator; the \(L=.72\) sign has a **separate existing Lean proof**. The widening shows how both the even scalar margin and the odd pole margin collapse.

### 12.1 Exact Krein secular equation for the soft eigenvalue

For each fixed width where \(H_+\) has one negative eigenvalue and a gap around zero, define the meromorphic scalar
\[
\mathfrak F_L(z)=1+2\langle c,(H_+(L)-z)^{-1}c\rangle.
\]
The rank-one resolvent formula gives the **exact spectral equation**
\[
\boxed{z\in\rho(H_+)\text{ is an eigenvalue of }W_+
\iff \mathfrak F_L(z)=0.}
\]
In each real resolvent gap, 
\[
\boxed{\mathfrak F_L'(z)=2\|(H_+-z)^{-1}c\|^2>0.}
\]
If \(F_L(0)<0\) and the soft healed eigenvalue \(\lambda_+\) lies before the next pole of \(H_+\), the mean-value theorem yields
\[
\boxed{\lambda_+=
-\mathfrak F_L(0)/\mathfrak F_L'(\xi),\quad0<\xi<\lambda_+.}
\]
So \( -F_L(0)/[2\|H_+^{-1}c\|^2]\) is a **first-order spectral prediction** from the unhealed, gapped resolvent. It precisely connects the scalar pole-compensation margin to the positive soft mode; this is not a new positivity theorem, but it identifies the single mode responsible for the near-collapse.

**Numerical comparison (48-mode finite source):**

| \(L\) | \(\mathfrak F_L'(0)\) | first-order \(\lambda_{\rm pred}\) | directly diagonalized \(\lambda_{\min}(W_+)\) |
|---:|---:|---:|---:|
| 0.72 | 0.89170505 | 9.14708e−4 | 9.15095e−4 |
| 1.05 | 0.77918894 | 3.03945e−7 | 3.03937e−7 |
| 1.15 | 0.75823362 | 1.10412e−8 | 1.10410e−8 |

This shows the **unhealed Krein scalar**, not a matrix-size artefact, controls the soft even Galerkin eigenvalue across three widths. The errors at widths 1.05 and 1.15 are extremely small because the mode itself is tiny compared with its unhealed spectral gap. This remains a *numerical* observation, not a theorem comparing widths.

### 12.2 Prime 3 is essential to the odd-sector cancellation

At \(L=1.15\), removing **only the \(n=3\) off-diagonal prime source** while retaining the same archimedean, pole, and scalar prime-mass terms gives, at 48 sine modes:

| Variant | lowest odd Weil Ritz eigenvalue | lowest even Weil Ritz eigenvalue |
|---|---:|---:|
| True primes \(2,3\) | \(+3.71337\times10^{-6}\) | \(+1.10410\times10^{-8}\) |
| Prime \(3\) omitted | \(-0.0284045\) | \(+2.31278\times10^{-8}\) |

Thus the prime \(3\) term supplies a **positive refund to an odd, oscillating direction** even though its coupling coefficient \(\Lambda(3)/\sqrt3\) is positive and it enters the Weil form with an overall minus sign. The missing-prime-3 odd sector becomes negative. This is a direct, source-only arithmetic selectivity test: no estimate replacing the actual prime set by a generic positive mass bound can retain this refund.

A cheap candidate **explicit negative test** for the prime-3-omitted signed form is
\[
f(x)=\sum_{j=1}^8 a_j\sqrt{2/L}\sin(2j\pi(x+L/2)/L),\quad
(a_1,\ldots,a_8)=(1,1.071,0.624,0.107,0.206,0.120,0.073,0.118).
\]
The source-only normalized Rayleigh quotients are **−0.00303599** when \(3\) is removed and **+0.03340466** when it is included. Coefficients have three exact decimal places (rational input), but the transcendental source integrals were evaluated in ordinary floating point; independent outward Arb/rational certification is needed before labelling these signs *CERTIFIED*. This is an excellent small falsifier for a candidate proof that ignores multiplicative prime composition.

### 12.3 The actual next proving ground

The *existing* width-.72 Lean theorem is not to be rebuilt. Carry the **rank-one Krein pole identity** and **secular scalar running function \(\mathfrak F_L\)** to \(L=1.15\). Work separately:

1. Certify that the infinite-dimensional pole-removed \(H_+(1.15)\) has exactly one negative mode and a positive spectral gap on its complement (the 48-mode next positive eigenvalue \(\sim3.16\times10^{-4}\) is a sighting, not a lower bound).
2. Certify the scalar \(1+2\langle c,H_+^{-1}c\rangle\le0\) with an error **much smaller than \(8\times10^{-9}\)**; ordinary floating precision or a crude \(\|H^{-1}\|\) bound is unlikely to suffice.
3. Certify \(H_-(1.15)>0\) and \(2\langle s,H_-^{-1}s\rangle\le1\); its 48-mode pole loading \(\sim0.99983996\) is also close to saturation.
4. Independently certify the explicit 8-term odd negative test after prime-3 removal to anchor the arithmetic-specific source refusal.
5. Test the *completed shifted* \(F_{1/4}\) against any general lemma before banking it. The all-width lift remains open even if width 1.15 is certified.

This is a legitimate potential improvement in **conditioning** (invert the unhealed gapped operator, not the nearly singular healed operator), but the tiny scalar margins mean it remains technically challenging. The existing general Legendre-moment Schur route and the new scalar secular route should be compared on their actual full infinite-residual certification costs.
