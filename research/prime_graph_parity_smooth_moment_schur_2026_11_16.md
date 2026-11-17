# All-prime mass, parity, and a smooth-moment Schur certificate for the actual Weil form

**Research note, 2026-11-16.** Exact unconditional source identities, an all-width high-frequency theorem and a *conditional finite-matrix sufficient criterion*. NO RH, ARP, OB-6, or completed celestial identification is proved. Schur theory and Mellin/Fourier coercivity are classical; the source-specific estimates, normalization match and explicit matrix are the additions here.

## 1. Exact source quadratic form and positive-minus-negative structure

For real f in C_c^infty(I), I=[-L/2,L/2], zero-extended, let ell_n=log n, v_n=Lambda(n)/sqrt(n), Cinf=-gamma-log pi-pi/2-3log2<0, and w(t)=exp(-t/2)/(1-exp(-2t)). The source Weil quadratic form (GPPVerify ArchimedeanFloor / ArithmeticReflectionPositivity / ShiftPresentation) is

\[
W_L(f)=E_\infty(f)+C_\infty\|f\|^2+
2\left(\int_I f e^{x/2}\right)\left(\int_I f e^{-x/2}\right)
-2\sum_{\ell_n<L}v_n\int f(x)f(x-\ell_n)\,dx,
\]
\[
E_\infty(f)=\int_0^\infty w(t)\|f-T_tf\|^2dt.
\]

Set d_minus=x+L/2, d_plus=L/2-x, and the STRICT-cutoff staircase V_L(u)=sum over ell_n<L AND ell_n<=u of v_n. The exact mass is m_L(x)=V_L(d_minus)+V_L(d_plus). Write c(x)=cosh(x/2), s(x)=sinh(x/2). At every prime-power shift ell>0,

\[
-2v_n\!\int f(x)f(x-\ell)dx
=v_n\!\int_{I\cap(I+\ell)}(f(x)-f(x-\ell))^2dx
-v_n\!\int_{I\cap(I+\ell)}(f(x)^2+f(x-\ell)^2)dx.
\]

After summing the latter diagonal masses and splitting the pole into c and s:

\[
\boxed{W_L(f)=
\underbrace{E_\infty(f)+\sum_{\ell_n<L}v_n\!\int_{I\cap(I+\ell_n)}(f(x)-f(x-\ell_n))^2dx
+2\langle f,c\rangle^2}_{Q^+_L(f)\ge0}
-\underbrace{\int_I(|C_\infty|+m_L(x))f(x)^2dx
+2\langle f,s\rangle^2}_{Q^-_L(f)\ge0}.}\tag{1}
\]

The pole identity is EXACT: 2(∫ f e^+)(∫ f e^-)=2<f,c>²−2<f,s>². Only ONE negative rank-one pole mode remains, in the odd parity sector. The full W is parity invariant so even and odd test sectors decouple. The negative pole operator has exact norm

\[
\boxed{2\|s\|^2=2\sinh(L/2)-L.}\tag{2}
\]

This is NOT a positivity proof; the spatial potential is still negative and unbounded in strength as L increases.

## 2. Exact prime mass, universal improvement, and the first-prime Lean regression

Let M_L=esssup m_L(x). For all L>0,

\[
\boxed{V_L(L)\le M_L\le V_L(L)+V_L(L/2).}\tag{3}
\]

Indeed, for each u in [0,L] one of u,L-u is <=L/2, while both <=L. The lower bound comes from a neighborhood of the boundary u=0 (because each finite ell_n<L remains visible close to that boundary).

M_L is an exactly FINITE optimization: sort the distinct breakpoints {0,L} union {ell_n, L-ell_n: ell_n<L}, and evaluate V_L(u)+V_L(L-u) at the MIDPOINT of each consecutive open cell. IMPORTANT: merely evaluating at threshold points can overcount a measure-zero simultaneous double jump, and is not always the essential supremum.

The improved global negative budget and quadratic lower bound are

\[
\boxed{B_{\rm graph}(L)=|C_\infty|+M_L+2\sinh(L/2)-L,\quad
W_L(f)\ge E_\infty(f)-B_{\rm graph}(L)\|f\|^2.}\tag{4}
\]

For f orthogonal to s, drop the last pole term. The positive prime graph term and even pole can be retained to improve estimates.

For log2<L<log3 only n=2 enters and its two shifted diagonals cannot coexist at a common positive-measure point because L<2log2. Therefore M_L=log2/sqrt2. At L=18/25,

\[
B_{\rm graph}(18/25)
=|C_\infty|+\frac{\log2}{\sqrt2}+2\sinh(9/25)-18/25
=5.877965579449248\ldots
\]

This is EXACTLY the quantity M_minus in the kernel-checked GPPVerify file GppVerify/RiemannHypothesis/FirstPrimeNegativeBound.lean, whose theorem M_minus_lt proves M_minus<147/25. Thus (4) extends that IN-TREE benchmark to every prime threshold, without making its RH-strength bound automatic.

**UPGRADED THEOREM (2026-11-16):** The companion note research/weighted_chebyshev_global_superadditivity_sharp_prime_mass_2026_11_16.md proves, UNCONDITIONALLY and for ALL real x,y>=1, V(xy)>=V(x)+V(y). It uses two published non-RH Chebyshev bounds and 40,401 finite inequalities certified by exact integer arithmetic. Hence the above general coarse upper bound upgrades to the EXACT identity

\[\boxed{M_L=V_L(L)\qquad\text{for every support width }L>0.}\]

For the boundary convention ell_n=L, this is an essential-supremum identity: perturb the two distance arguments downward, use superadditivity at sum L-2eps, then take an a.e. argument; the reverse inequality holds on a positive-measure neighborhood of an endpoint. The all-width sharp mass budget is therefore B_graph(L)=|Cinf|+V_L(L)+2sinh(L/2)-L, WITHOUT any unproved step. This improves the old |Cinf|+2V(L)+2Le^{L/2} estimate and exactly recovers the first-prime Lean M_minus constant. The global Chebyshev theorem is NOT RH-discriminatory; positive shifted F_theta weights are now PROVED to share superadditivity for ALL theta>=0 by the monotone-reweighting closure theorem in research/monotone_reweighting_f_theta_falsifier_central_deficit_2026_11_16.md.

## 3. Improved unconditional all-width high-moment coercivity

Archimedean Fourier symbol (for \hat f(lambda)=∫ f(x)e^{-i lambda x}dx) is
\[
a(\lambda)=2\sum_{k\ge0}\frac{\lambda^2}{(2k+1/2)[(2k+1/2)^2+\lambda^2]}
=\Re[\psi(1/4+i\lambda/2)-\psi(1/4)].
\]
It is even, nonnegative, increasing and diverges to +infinity. Choose R>0 such that a(R)>2 B_graph(L). Pick N so

\[
\alpha_N(L,R)=\frac{LR}{\pi}\left(\frac{(RL/2)^N}{N!}\right)^2\le1/2.
\]

Then EVERY smooth real h with first N moments ∫_I x^k h(x)dx=0 for k<N satisfies

\[
\boxed{W_L(h)\ge\delta_{L,R,N}\|h\|^2,\quad
\delta_{L,R,N}=a(R)(1-\alpha_N)-B_{\rm graph}(L)>0.}\tag{5}
\]

Proof: moment cancellation bounds |\hat h(lambda)|<=sqrt(L)||h||(RL/2)^N/N! for |lambda|<=R. Plancherel ensures at least (1-alpha_N) of Fourier mass outside ±R, where the positive archimedean symbol costs at least a(R). Then apply (4). This is the rigorous finite-index result, now with source-optimal parity pole and exact graph mass. It does NOT control the low moments.

PNT yields V_L(L)~2e^{L/2}, so B_graph grows at least e^{L/2}; whereas a(R)=log R+O(1). Therefore this COARSE cutoff proof requires R of order at least exp(const*e^{L/2}), and the Taylor moment count N grows with R L. The poor complexity is a limitation of this method, not a theorem forbidding improved arithmetic cancellations.

## 4. Exact smooth-moment Schur reduction, with fully finite sufficient matrix

Fix L,R,N as in (5). Choose eta>=0 smooth and compactly supported inside I, positive on an open subinterval. The N×N moment matrix H_ij=∫_I eta(x)x^{i+j}dx is SPD. Define smooth cardinal tests

\[
\phi_j(x)=\eta(x)\sum_{k<N}(H^{-1})_{kj}x^k,\qquad
\int_I x^i\phi_j(x)dx=\delta_{ij}.
\]

Every smooth f decomposes uniquely as f=u+h, u=sum_{j<N}mu_j phi_j, mu_j=∫x^j f, and h has first N moments zero. BOTH pieces remain in the form domain. CORRECTION (2026-11-16): Earlier this sentence incorrectly excluded raw polynomial indicators from the logarithmic Weil form domain. In fact a(D)=O(log(2+|lambda|)), while polynomial indicators have Fourier decay O(1/|lambda|), so they belong EVEN to the L² operator domain. Smooth cardinal functions above remain valid, but the canonical orthonormal Legendre basis is simpler and eliminates moment Gram inverses. See research/legendre_schur_domain_correction_variance_2026_11_16.md for the corrected F−delta^-1(H−F²) finite test.

Define the localized symmetric Weil operator on compactly supported smooth φ:

\[
A_L\phi=\mathbf1_I a(D)\phi+C_\infty\phi
+e^{x/2}\langle e^{-x/2},\phi\rangle
+e^{-x/2}\langle e^{x/2},\phi\rangle
-\sum_{\ell_n<L}v_n(T_{\ell_n}+T_{-\ell_n})\phi\big|_I.
\]

The Fourier multiplier a(D)φ is L² because φ is smooth and a(lambda)=O(log(2+|lambda|)); hence A_Lφ∈L². Let F_ij=W_L(φ_i,φ_j)=<φ_i,A_Lφ_j>, and let H0={h∈L²(I): ∫x^k h=0,k<N} with orthogonal projection P0. Set b_j=P0 A_L φ_j and Z_ij=<b_i,b_j>.

Z has an explicit finite-matrix projection formula: let p_i(x)=x^i, G_ij=∫_I x^{i+j}dx (SPD), and v_ij=<p_i,A_Lφ_j>. Then

\[
\boxed{Z_{ij}=\langle A_L\phi_i,A_L\phi_j\rangle-v_i^\mathsf{T}G^{-1}v_j.}\tag{6}
\]

Completing the square, with δ=δ_{L,R,N}>0,

\[
W_L(f)\ge\mu^\mathsf{T}(F-\delta^{-1}Z)\mu+
\delta\left\|h+\delta^{-1}\sum_j\mu_j b_j\right\|^2 .
\]

Thus the FINITE, explicit, source-arithmetic matrix S_safe(L,N)=F−δ^-1 Z has the decisive implication

\[
\boxed{S_{\rm safe}(L,N)\succeq0\quad\Longrightarrow\quad W_L(f)\ge0\quad
\text{for ALL smooth supported f}.}\tag{7}
\]

No PSD assertion about this matrix has been established! Finite computation of F and Z requires rigorous enclosures of local gamma and prime terms.

There is an EXACT Schur EQUIVALENCE using the still-infinite but positive high-sector inverse: let D>=δ be the positive selfadjoint operator of the restricted closed form on moment-zero H0. Then

\[
\boxed{W_L\succeq0\iff
S_{\rm exact}:=F-[\langle b_i,D^{-1}b_j\rangle]_{ij}\succeq0.}\tag{8}
\]

Proof: minimize over the high-sector h for each fixed moment vector mu. Since 0<=D^-1<=δ^-1 I, we have S_safe<=S_exact<=F in PSD order. (8) is an exact Schur reformulation; (7) is a computable one-way test. It would be WRONG to assert that testing F alone suffices without cross coupling.

## 5. Shifted controls, scripts, Lean upstream, and honest scope

Generic nonnegative fake prime coefficients also admit a graph SOS and moment Schur construction. Therefore **the decomposition, its all-width finite index, and the universal Carleman ladder are NOT RH-discriminatory.** A valid full-width proof of (7) must exploit true von Mangoldt structure in the finite entries and fail the shifted off-line F_theta control. The now-PROVED superadditivity of V sharpens the mass estimate but does not provide RH discrimination; positive shifted weights PROVABLY share the inequality for every theta>=0.

Reproducible scripts:
- experiments/abel_prime_common_map/probe_prime_graph_mass.py: sampled finite-step graph mass maxima, old/new B comparison, and 4-million-pair FLOATING-POINT superadditivity probe only.
- experiments/abel_prime_common_map/verify_moment_schur_exact.py: exact rational 5-dimensional toy checks the projection and Schur factors; NOT a Weil positivity test.

Mathlib-upstream targets: prime shift graph exact diagonal mass identity; parity rank-one pole; essential supremum of a finite step potential; bump moment-cardinal construction; abstract closed-form Schur complement in a positive high subspace and safe finite matrix projection. Formalize the first-prime M_minus recovery against the already checked Verify declaration before claiming any new Lean result.

**BOTTOM LINE:** An exact SOURCE-DEFINED finite Schur matrix and a positive high-frequency complement now exist for every finite width. Its positivity at all widths remains equivalent to an RH-strength task; no RH proof, no new global positivity theorem, no Lean build claimed.
