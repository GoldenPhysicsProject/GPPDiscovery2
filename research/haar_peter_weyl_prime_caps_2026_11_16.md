# Haar–Peter–Weyl realization of the first-prime Weil obstruction

**GPPDiscovery2 | 2026-11-16 | New representation-theoretic bridge and exact prime cap polynomials.** This is a structural derivation for Turbo/Claude audit, NOT a proof of RH or fixed-window Weil positivity.

## 1. Two different Haar measures, and an exact fixed-window unitary

The logarithmic variable \(x=\log r\) is Haar for the multiplicative group \(\mathbb R_+^\times\):
\[
dr/r=dx.
\]
Mellin Fourier/Plancherel on this NONCOMPACT group has generalized unitary characters \(r^{i\xi}=e^{i\xi x}\). These are the frequency variables used in the actual archimedean energy \(E(f)\). This measure is infinite and cannot be globally identified with the probability Haar measure of a compact group.

Independently let \(G=SO(3)\), \(K=SO(2)\) (rotations fixing the north pole), \(G/K=S^2\). Normalize the invariant probability measure \(d\Omega/(4\pi)\). For a zonal function depending only on \(t=\cos\theta\),
\[
\int_{S^2}F(\cos\theta)\,\frac{d\Omega}{4\pi}
   =\frac12\int_{-1}^1 F(t)dt. \tag{1}
\]
For a fixed width \(L>0\), \(I_L=[-L/2,L/2]\), define
\[
\boxed{(U_L f)(n)=\sqrt L\,f\!\left(\frac L2 n_z\right).}\tag{2}
\]
Then
\[
\|U_Lf\|^2_{L^2(S^2,d\Omega/4\pi)}
   =\int_{I_L}|f(x)|^2dx.
\]
Thus \(U_L:L^2(I_L,dx)\to L^2(S^2,d\Omega/(4\pi))^K\) is an EXPLICIT unitary.

**Crucial scope:** \(U_L\) depends on L. It is a Hilbert-space isomorphism and a coordinate map, NOT an intertwiner between the full \(SO(3)\) action and the multiplicative dilation group; the compact and noncompact Haar measures are distinct. The representation correspondence does not assert \(s=\Delta\), Weil positivity, or RH.

## 2. Peter–Weyl, spherical harmonics and the five moments

The class-one \(SO(3)\) irreducible representations with one K-fixed vector are indexed by nonnegative INTEGER angular momenta n. Their K-spherical matrix coefficients are \(P_n(t)\), the Legendre polynomials. By Peter–Weyl,
\[
e_n(x)=\sqrt{\frac{2n+1}{L}}P_n(2x/L),\quad n\ge0
\tag{3}
\]
is a complete real orthonormal basis of \(L^2(I_L)\). Its lift is
\(U_Le_n=\sqrt{2n+1}\,P_n(n_z)\).

The canonical low-spin projection is
\[
\boxed{\quad
(\Pi_{<m}f)(x)=\int_{I_L}\mathcal K_m(x,y)f(y)dy,\quad
\mathcal K_m(x,y)=\frac1L\sum_{n=0}^{m-1}(2n+1)P_n(2x/L)P_n(2y/L).
\quad}\tag{4}
\]
For m=5, orthogonality to the first five spherical harmonics is EXACTLY the same as the five spatial moment conditions \(\int_{I_L} x^j f(x)dx=0\), j=0,...,4 (triangular change of polynomial basis).

The spherical reflection \(t\mapsto-t\) is realized by an element of \(N_G(K)\) acting on zonal functions (a 180° rotation exchanging poles). It gives \(P_n(-t)=(-1)^nP_n(t)\); consequently the first five exceptional modes split as three even n=0,2,4 and two odd n=1,3. The actual Weil operator commutes with this discrete reflection, not with the full G action.

## 3. The Fourier kernel is the spherical-Bessel Peter–Weyl expansion

For \(z=\xi L/2\) and normalized unitary Fourier transform on the additive log-Haar group,
\[
\boxed{\quad
\widehat{e_n}(\xi)=
  \sqrt{\frac{L(2n+1)}{2\pi}}(-i)^n j_n(z),\quad
j_n(z)=\frac12 i^{-n}\int_{-1}^1 e^{izt}P_n(t)dt.\quad}\tag{5}
\]
The sign and phase in (5) follow from \(\int_{-1}^1e^{-izt}P_n(t)dt=2(-i)^n j_n(z)\).
This is the axisymmetric Peter–Weyl expansion of the plane wave,
\[
e^{-izt}=\sum_{n\ge0}(2n+1)(-i)^n j_n(z)P_n(t).\tag{6}
\]
Equations (5)–(6) give an exact basis for the **mixed** Fourier/archimedean quadratic form:
\[
E_{nm}=\int_{\mathbb R}a(\xi)
 \overline{\widehat e_n(\xi)}\widehat e_m(\xi)\,d\xi,\quad
a(\xi)=2\int_0^\infty\frac{e^{-u/2}}{1-e^{-2u}}(1-\cos\xi u)du.\tag{7}
\]
This is a legitimate Fourier/Haar-to-Peter–Weyl matrix identity with the actual real-place multiplier. The operator is not diagonal in n because \(a(\xi)\) is not induced by the \(SO(3)\) Casimir. For finite n,m, these integrals converge: the \(e_n\) are supported piecewise-polynomial functions with 1/ξ Fourier decay and \(a(\xi)=O(\log(2+|\xi|))\).

## 4. Prime 2 is a coupling between two tiny opposite polar caps

For the first-prime window \(L=18/25\), \(\ell=\log2<L<\log3\), define
\[
\alpha=2\ell/L\in(1,2),\qquad
h=2-\alpha=2(1-\ell/L).
\tag{8}
\]
The prime shift \(x\mapsto x-\ell\) acts on latitude as \(t\mapsto t-\alpha\). It is NOT an SO(3) rotation and does not commute with Peter–Weyl irreducible projections.

The overlap of the shifted interval with the original is t∈[α−1,1], of length h. Each polar cap carries normalized sphere Haar mass \(h/2=1-\ell/L\approx 0.03729558256\), while the physical log-length of each edge is \(L-\ell\approx 0.02685281944\). Consequently the visible prime is a **north/south polar-cap coupling** involving only about 3.73% of the sphere probability measure on each side.

For the unnormalized Legendre polynomials, the **exact** prime-shift matrix coefficient is
\[
\begin{aligned}
J_{nm}(\alpha)
 &=\frac12\int_{\alpha-1}^{1}P_n(t)P_m(t-\alpha)\,dt\\
 &=\frac{(-1)^m}{2}\int_0^h P_n(1-u)P_m(1-h+u)\,du.
\end{aligned}\tag{9}
\]
The actual \(L^2(I_L)\)-normalized correlation coefficient is
\[
 A_{nm}(\ell)=\sqrt{(2n+1)(2m+1)}J_{nm}(\alpha).
\tag{10}
\]
The Weil *quadratic* depends on the symmetrization
\(C_{nm}=(A_{nm}+A_{mn})/2\). A change of variables gives
\[
A_{mn}(\ell)=(-1)^{n+m}A_{nm}(\ell),\tag{11}
\]
so C_{nm}=0 for opposite parity, exactly as expected from the nontrivial normalizer/Weyl reflection.

Every \(J_{nm}\) is a finite polynomial in h with rational coefficients and a factor h, because the integrand in (9) is polynomial. No quadrature, zeta zeros or special-function uncertainty is needed to evaluate the prime matrix.

For example (these are **unnormalized** J diagonal coefficients; multiply by 2n+1 to obtain the normalized diagonal):
\[
J_{00}=\frac h2,\qquad
J_{11}=-\frac{h(h^2-6h+6)}{12},\qquad
J_{22}=\frac{h(3h^4-30h^3+100h^2-120h+40)}{80}.\tag{12}
\]
The first low even mode has \(A_{00}=h/2>0\), so its prime term \(-2vA_{00}\) is destabilizing. The first low odd mode has \(A_{11}=3J_{11}<0\) for \(0<h\ll1\), so its prime term is **stabilizing**. This sign difference is a concrete arithmetic reason the first-prime even sector is numerically much closer to zero than the odd sector. It does not establish sector-wide signs, since arbitrary odd/even functions may oscillate within a cap.

## 5. The exact complete Weil matrix, not a positive model

Let \(C_n=\int_I e_n(x)\cosh(x/2)dx\), \(S_n=\int_I e_n(x)\sinh(x/2)dx\), and \(C_\infty=-\gamma-\log\pi-\pi/2-3\log2\).
Then every finite matrix coefficient is exactly
\[
\boxed{
W_{nm}=E_{nm}+C_\infty\delta_{nm}
+2C_nC_m-2S_nS_m
-2\frac{\log2}{\sqrt2}\,C_{nm}.\tag{13}
}
\]
All real-place, pole, and prime contributions use original signs. By parity, W splits into even and odd blocks. This makes the true five-dimensional exceptional space \(P_0=\mathrm{span}(e_0,\dots,e_4)\) canonical and supplies exact formulas for the low 3×3 and 2×2 blocks and all low–high couplings.

**Caution:** (13) on a finite principal block is NOT the exact five-dimensional Schur complement. The latter includes \(-B^*D^{-1}B\) from the complete infinite-dimensional complement. Haar orthogonality does not make B vanish because the full Weil form is not SO3-invariant.

Averaging/twirling the Weil operator over SO3 would replace it by another rotationally invariant operator and does NOT preserve its original quadratic form. In particular, Haar averaging an indefinite form can mask negative directions. This is a no-go for the shortcut “Haar positivity implies Weil positivity.”

## 6. Independent computation of actual finite Galerkin Ritz values

To check the normalization without relying on a frequency cutoff, I implemented the complete matrix (13) in **real space** using Gauss–Legendre quadrature for the shift correlations, exact positive archimedean tail \(\int_{t>L}\), exact quadrature for pole moments and the n=2 cap overlap. Across 120, 250 and 450 translation nodes, the first Ritz values at n=18 remain stable to ~1e−13:
\[
\begin{array}{c|c|c}
\text{basis size}&\lambda_{\min}(W_{\rm Ritz})&\lambda_{\min}(\text{odd block})\\
16&0.00085169981864&0.04871634166\\
30&0.00085029313212&0.04864913978\\
50&0.00084974316863&0.04863295980
\end{array}
\tag{14}
\]
At n=50 the smallest even Ritz value is ~0.00084974, about 57 times smaller than the odd value. The finite low (n<5) Schur complement after truncating the high Legendre modes to n≤49 has smallest eigenvalue ~0.0008497456, but this remains **floating evidence only**: neither quadrature nor the infinite complementary tail is interval-certified. The Ritz eigenvalues decrease as the trial space increases. They cannot prove positivity of all smooth test functions.

Local reproducibility script: \`experiments/abel_prime_common_map/scan_haar_legendre_weil.py\` (code and outputs must be independently rerun by Turbo). A truly rigorous certificate needs explicit directed interval bounds for the real-place mixed matrix and a dual-norm estimate of the full residual \(B-DZ\), as specified in \`first_prime_schur_residual_certificate_2026_11_16.md\`.

## 7. Research judgement and handoff

- **Established analytically:** Exact Haar probability normalization (1)-(3), class-one Peter–Weyl meaning of the five moments, orthogonal parity splitting, exact prime polar-cap polynomial identities (9)-(13), and precise distinction from multiplicative Haar/continuous Mellin.
- **Numerical evidence:** Ritz spectra in (14), independent real-space quadrature, no interval certification.
- **Not established:** Full first-prime positivity \(W(f)\ge0\), all-width ARP/RH, \(s=\Delta\) as a dynamical arithmetic spectral identification, or Haar positivity of the signed prime subtraction.

**Turbo and Claude next:** formalize the Haar-unitary mapping and the exact prime cap polynomial coefficients (especially (11)-(12)) as finite arithmetic/algebra; build the canonical low 3×3 even and 2×2 odd blocks; bound the true mixed energy/prime/pole couplings and full infinite residual. Prioritize the *even* Schur block, where the observed spectral margin is ~0.00085. Do not twirl the Weil operator, since it is not SO3-equivariant.


## 8. The direct meeting of the two Haar-Plancherel theorems

There is a precise *unitary overlap* between the compact rotational Haar basis and the noncompact multiplicative Haar/Fourier basis; no appeal to a speculative self-duality is needed. From (3) and (5), applying ordinary Fourier Plancherel to the Legendre orthonormality gives
\[
\boxed{\quad
 \int_{-\infty}^{\infty}j_n(z)j_m(z)\,dz
   =\frac{\pi}{2n+1}\,\delta_{nm},\quad n,m\ge0.
 \quad}\tag{15}
\]
Because each spherical Bessel function is real for real z, there is no conjugation ambiguity. The nontrivial phase \((-i)^n\) in the Fourier transform cancels on the diagonal and multiplies an already-zero off-diagonal inner product. Thus (15) follows from the two actual Haar normalizations, not by assuming RH.

An exact normalized bridge matrix for the positive real-place channel is
\[
\boxed{\quad
 E_{nm}=\frac{\sqrt{(2n+1)(2m+1)}}{\pi}\,
  i^n(-i)^m\int_{-\infty}^{\infty}
  a(2z/L)\,j_n(z)j_m(z)\,dz.\quad}\tag{16}
\]
Its quadratic form is nonnegative because \(a\ge0\), even though it has off-diagonal entries. The **signed** Weil matrix is still \(E_{nm}+C_\infty\delta_{nm}+2C_nC_m-2S_nS_m-2v C_{nm}\).

This provides a mathematically exact Haar-to-Haar overlap transform:
\[
\boxed{\;\text{multiplicative Mellin/Plancherel}\ \longleftrightarrow\
   \text{compact spherical Peter–Weyl}\;}
\]
ON THE FIXED SUPPORT INTERVAL, by the L-dependent unitary \(U_L\).
It is a representation-basis change, not an identification of the two groups, not the functional equation by itself, and not proof of a physical spectral correspondence \(s=\Delta\).

### Why the piecewise-polynomial Legendre trial functions are legitimate

The lifted basis \(e_n\) on I extended by zero to \(\mathbb R\) has jump discontinuities at the interval endpoints, so it is not itself a global smooth test. But its archimedean energy is finite: \(|\widehat e_n(\xi)|=O(|\xi|^{-1})\), while \(a(\xi)=O(\log(2+|\xi|))\), hence \(\int a|\widehat e_n|^2<\infty\).

More strongly, these functions belong to the **energy completion** of compactly supported smooth tests. Let \(g_\epsilon=e_n\cdot\chi_{\rm boundary,\epsilon}\) denote the difference between the Legendre function and a smooth cutoff that equals one away from a layer of total thickness O(ε) near the boundary. Then \(\|g_\epsilon\|_2^2=O(\epsilon)\) and \(\|g_\epsilon\|_\infty=O(1)\). **It is important NOT to use an \(H^1\) derivative estimate here:** \(g_\epsilon\) retains the original endpoint jumps. Instead, the boundary-layer cutoff functions have uniformly bounded total variation \(\operatorname{TV}(g_\epsilon)=O(1)\). The standard BV translation estimate \(\|g_\epsilon-T_tg_\epsilon\|_1\le |t|\operatorname{TV}(g_\epsilon)\), combined with \(\|g_\epsilon-T_tg_\epsilon\|_\infty\le2\|g_\epsilon\|_\infty\), gives
\(\|g_\epsilon-T_tg_\epsilon\|_2^2\le C|t|\).
For \(t\ge\epsilon\) use the separate bound
\(\|g_\epsilon-T_tg_\epsilon\|_2^2\le4\|g_\epsilon\|_2^2=O(\epsilon)\).
Splitting the positive translation-energy integral into \(0<t<\epsilon\), \(\epsilon<t<1\), and \(t>1\), and using \(w(t)=O(1/t)\) near zero and \(w(t)=O(e^{-t/2})\) at infinity, gives
\[
\boxed{\quad
 E(g_\epsilon)=O\bigl(\epsilon[1+\log(1/\epsilon)]\bigr)\longrightarrow0.
\quad}\tag{17}
\]
Thus the finite Legendre Ritz calculations are well-defined on the true energy completion, with arbitrarily close smooth approximants. Nevertheless **positivity of every tested Ritz matrix** cannot establish positivity on the completion, because the untested high modes and mixed terms remain uncontrolled.

This completion lemma also provides a concrete, non-circular core for a future Lean construction of the Haar–Legendre Schur complement.


## 9. An exact arithmetic sign law across the ENTIRE first-prime rung

For every width \(\log2<L<\log3\), we have
\[
0<h=2(1-\log2/L)<1
\]
because \(\log3<2\log2=\log4\). Consequently \(h^2-6h+6\ge1\), and the first two normalized Legendre diagonal prime correlations have fixed opposite signs:
\[
\begin{aligned}
A_{00}(\log2)&=h/2>0,\\
A_{11}(\log2)&=-h(h^2-6h+6)/4<0.
\end{aligned}
\]
Multiplying by the actual Weil weight \(-2v\), \(v=(\log2)/\sqrt2>0\), gives
\[
\boxed{
 W^{\rm prime}_{00}=-v h<0,\qquad
 W^{\rm prime}_{11}=\frac{v h}{2}(h^2-6h+6)>0.
}\tag{18}
\]
Thus the unique newly visible prime necessarily pushes the *lowest even* Haar channel downward and the *lowest odd* Haar channel upward throughout the full prime-2-only width interval. No all-mode or all-test sign is inferred.

The finite polynomial identities for n,m≤5 and the Weyl parity relation were checked exactly (symbolic polynomial integration, no floats) in
\`experiments/abel_prime_common_map/verify_haar_prime_caps.py\`. The real-space Ritz diagnostic was committed to
\`experiments/abel_prime_common_map/scan_haar_legendre_weil.py\`.

These source-correct finite algebraic identities are appropriate early Lean targets for Claude and may help prioritize the very small even-sector positivity margin when constructing a rigorously residual-certified Schur complement.


## 10. EXACT polar-cap Pauli decomposition: compressed prime translation is square-zero

The previous cap formula can be strengthened to an exact operator theorem valid for the *entire* first-prime rung \(\log2<L<\log3\). Put \(\ell=\log2\), \(I=[-L/2,L/2]\), and define the left and right edge intervals
\[
 I_-=[-L/2,L/2-\ell],\qquad
 I_+=[\ell-L/2,L/2].
\]
Both have length \(d=L-\ell>0\), and they are disjoint because \(2\ell>L\). Let \(H_\pm=L^2(I_\pm)\) and \(H_{\rm mid}=L^2(I\setminus(I_-\cup I_+))\). These are orthogonal subspaces of \(L^2(I)\).

Let \(S=P_I T_\ell P_I\), where \(T_\ell f(x)=f(x-\ell)\), and \(P_I\) is the compression by \(1_I\). Then \(S\) maps \(H_-\) UNITARILY onto \(H_+\), vanishes on \(H_+\oplus H_{\rm mid}\), and
\[
 \boxed{
 S^2=0,\quad S^*S=P_-,\quad SS^*=P_+,\quad
 (S+S^*)^2=P_-+P_+ .
 }\tag{19}
\]
This is an honest \(L^2\) identity and does not invoke the positive Weil form or RH. Via the identification
\[
L^2(I)\cong L^2([0,d])\otimes\mathbb C^2
 \ \oplus\ H_{\rm mid},
\]
the **selfadjoint prime operator** \(\mathcal P=-v(S+S^*)\) with \(v=(\log2)/\sqrt2>0\) becomes
\[
\boxed{\quad
 \mathcal P\ \cong\ -v\,I_{L^2([0,d])}\otimes
 \begin{pmatrix}0&1\\1&0\end{pmatrix}
 \ \oplus\ 0_{\rm mid}.
}\tag{20}
\]
Thus its exact spectrum is \(\{-v,0,+v\}\), its norm is exactly \(v\), and each of the \(\pm v\) eigenvalues has infinite multiplicity (since \(d>0\)). The positive and negative prime channels are explicitly the symmetric and antisymmetric combinations of the two cap wavefunctions. Their spectral projections are
\[
P_{\pm}^{\rm prime}
=\tfrac12(P_-+P_+\pm(S+S^*)),
\]
with \(\mathcal P=-v P_+^{\rm prime}+vP_-^{\rm prime}\).

**Interpretation:** the local prime crossing has a literal \(2\times2\) Pauli-\(\sigma_x\) structure on each point of the overlapping cap interval. It is not a spin-\(\frac12\) *SO(3) representation* and should not be advertised as a new fundamental spin degree of freedom. Rather, it is the exact two-channel sewing algebra of the arithmetic translation. It makes the signed nature of the prime term unavoidable: Haar projection onto the zonal sector does not turn \(\mathcal P\) into a positive operator.

**Practical result:** use (19)–(20) to build a two-channel exact prime operator in the finite Schur/Galerkin machinery; no numerical quadrature or prime-series truncation is needed for this block. The large but positive archimedean translation energy and the two pole ranks must compensate the negative symmetric cap channel. The isolated prime block by itself is always indefinite on the first-prime rung.

### Exact symbolic/finite tests

A source-independent test harness can verify the nilpotence/partial-isometry identities on explicit two-cap trial wavefunctions and the Pauli factor, though the full \(L^2\) operator theorem is elementary. The exact Legendre cap polynomial source remains \`experiments/abel_prime_common_map/verify_haar_prime_caps.py\`; formalizing (19) requires only interval support and translations, making it an efficient Lean theorem for Claude.

## 11. GPP Drive archive cross-reference and the exact logical boundary

I located and read user-owned archival material in the GPP Drive folder **including its subfolders**:

- **Daniel Toupin, *Plancherel and Peter–Weyl: The Two Spectral Faces of Haar Physics* (April 2026)**, in GPP / Everything: https://drive.google.com/file/d/1i0gau66Gastvci6me5PrF5mSqQxTdlKm/view. The abstract Haar dichotomy between noncompact dilation Plancherel and compact gauge Peter–Weyl is **prior work**, not a new conceptual claim of this note. The **new explicit step here** is the L-dependent isometry (2), the actual Weil matrix (13), and the exact first-prime cap/Pauli operator (19)–(20).
- **Daniel Toupin, *Haar Positivity: From Weil to Wightman* (May 2026; patched version)**: https://drive.google.com/file/d/19diaTG8Zqnx4OBsmbWJZpUAYgJ3Qf1uN/view. Haar-convolution squares yield positive-type TEST KERNELS; the sign of their pairing with the independent arithmetic Weil distribution remains the missing Weil-positivity assertion.
- **GPP archive study *Closing the Haar-Square Trace Identity Gap for the Riemann Hypothesis***: https://drive.google.com/file/d/1wpV3P29VZWbUZBeIS1iUTS3tDd7WJOWZ/view. It distinguishes distributional explicit formulas (Meyer), semi-local Hilbert descriptions (Burnol, Connes–Consani), and the unproved global Haar-square Hilbert trace identification; its independent literature assertions require source audit before promotion.
- **Turbo’s archive note on Haar positivity**: https://drive.google.com/file/d/1dvv6IiMsV6qsmTkavPPJ6Fu2hs5xfqWR/view. Its finite-model \(\zeta/F_\theta\) contrast emphasizes that plain Haar-positive sums are too weak; the true arithmetic distribution must discriminate the deformation. The present Pauli algebra is *object-independent* and therefore cannot by itself be RH-specific.
- **Turbo’s earlier Schur-compression kill test**: https://drive.google.com/file/d/13Cgiw9ieOETH1F6XrIxVqZjgS-0Re7te/view. A finite compression onto a near-kernel constant mode was blind to \(F_\theta\). Do not reproduce that defect when selecting the five/six low Legendre modes; retain the full residual and explicit deformation response.
- **Turbo’s Wave-234 parity/Schur analysis**: https://drive.google.com/file/d/1OxCGm-qV7vdnovQEr0Y-9lR7xtQOEopZ/view. Independently encounters exact even/odd sewing decompositions and opposite-sign pole components, consistent with the full Weil parity blocks here; its bump-train sectors differ from this first-prime fixed-width Haar basis.

**Safety check / one-line no-go.** If \(F=\Omega^\vee*\Omega\) is a positive-definite test function, an arbitrary distribution \(D\) need not satisfy \(D(F)\ge0\): on \(\mathbb R\), take \(D=-\delta_0\). Then \(D(F)=-\|\Omega\|_2^2<0\) for \(\Omega\neq0\). Therefore any proposed closure from “Haar square” to “Weil positive” has to demonstrate a property of the arithmetic distribution, not just the Haar test kernel. Similarly the numerical first-prime \(F_\theta\) control must be checked in the *identical* five/six-moment Schur construction.

**Research focus after reading archive:** prioritize exact source-level prime Pauli sewing + the genuinely arithmetic gamma/pole compensation; do not claim Peter–Weyl or Haar positivity independently implies RH, and do not conflate compact SO(3) unitary irreps with the noncompact principal series.
