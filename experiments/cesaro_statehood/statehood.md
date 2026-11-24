# What statehood can detect: a one-prime control and the missing scalar estimate

Use centered z=s−1/2 and H(z)=ξ(1/2+z). The state space used in the first calculation is the Besicovitch B² completion of finite sums of real-frequency characters on the log-time line under their symmetric Cesàro mean-square norm. This is a specified sector; it makes no assumption of completeness for zeros of H.

## A positive invertible arithmetic multiplier hides an entire ghost lattice

Modify the ordinary zeta Dirichlet series at exactly one prime by

    Z*(s)=ζ(s)(1+5·5^(−s)+5·5^(−2s)).

Its coefficients 1+5[5|n]+5[25|n] are positive integers and multiplicative. In the conductor-25 completion, multiplying by 5^(s−1/2) (a constant normalization of the conductor factor) gives the even entire control H*(z)=H(z)D(z), where D(z)=√5+2cosh(z log 5). Thus reflection and reality are preserved. On B², convolve by the centered xi theta kernel, equivalently multiply each character of frequency t by H(it). This is bounded: the theta kernel is integrable. Translation by log 5 is unitary and D acts as √5 I+U+U*, with spectrum contained in [√5−2,√5+2]. It has a bounded inverse by a norm-convergent Neumann series. In particular the two completed convolutions have **exactly the same kernel and the same range** (they commute, D is onto). Every approximate-null-vector norm is comparable in both directions with constants √5±2. This does not identify their full spectra, their Weil forms, or the rooted arithmetic data.

Nevertheless D vanishes at

    z=±log((√5+1)/2)/log(5) + (2k+1)πi/log(5),     k∈ℤ.

These are genuine off-line zeros inside the critical strip because 1<(√5+1)/2<√5. Each has divergent symmetric Cesàro primary norm. This exhibits the failure of an inference from the null space of the mean-square convolution alone to completeness for all complex zeros. It applies even if the entire family of zero-energy states and the closed range are known. This control is deliberately imprimitive and its modified Euler factor is not the standard degree-one factor of ζ.

## Which integer identity excludes the control?

Suppose the ordinary Dirichlet inverse of Z=ζ·∏P_p(p^(−s)), with finitely many local polynomial factors P_p(0)=1, has bounded coefficients on each individual prime-power chain. At p its inverse coefficients have generating function (1−X)/P_p(X) near zero. Boundedness gives a holomorphic sum for |X|<1. Multiplication by P_p and uniqueness of Taylor coefficients extend the identity throughout this disk. A root of P_p there would force 1−X=0, impossible. In particular no such local multiplier can introduce a zero in Re s>0. For the example the inverse starts 1,−6,25,−95,350 at 5⁰ through 5⁴. For ζ the corresponding coefficients are 1,−1,0,0,…. This is a local exclusion theorem; the argument does not apply to zeros of an analytically continued infinite Euler product.

## The precise remaining analytic bound

The unconditional prime-torus H² states Z_s and M_s obey Z_s M_s=1 in H¹ at each Re s>1/2 (D2, 2026-09-27_bohr_hardy_zeta_mobius_cancellation.md). That prior result uses μ*1=δ₁, orthogonality, and Cauchy–Schwarz. It is an identity of Haar equivalence classes. Even the actual finite reciprocal products have squared Haar norm ∏(1+p^(−2σ)) and supremum ∏(1+p^(−σ)); the first stays bounded for σ>1/2 and the second diverges up through σ=1. The supremum on each finite torus equals the supremum along the Kronecker line by rational independence. This obstruction is to global uniform point evaluation. It leaves open estimates on individual compact scalar windows.

For example take the genuine entire smoothed Möbius sums B_X(s)=Σ μ(n)n^(−s)exp(−n/X). A sufficient new analytic input would be: on one common sequence X_j→∞, for every closed disk K contained in Re s>1/2 the area integrals ∫_K |B_Xj(s)|² dA are bounded in j. By the disk submean inequality this gives uniform bounds on smaller compact sets. Montel and a diagonal subsequence yield a holomorphic limit B on the half-plane. Dominated convergence identifies B=1/ζ on Re s>1. Meromorphic continuation gives ζB=1 throughout, with the pole at 1 canceled. There can be no ζ zero in that half-plane, and reflection gives RH. Conversely the classical RH-implied bound Σ_{n≤x} μ(n)=O_ε(x^(1/2+ε)) gives those compact bounds for all X≥1 by partial summation against x^(−s)exp(−x/X). This is a criterion; the compact bounds have not been proved here. The area is ordinary complex-plane area at the actual integer phases. Replacing it with Haar average on the prime torus removes the required estimate.

## Exact scope of the formal Gram proposition

In GPPVerify/CesaroWeilGram.lean the quantifiers of WeilIsGram allow the approximating family to depend on the entire test configuration, after its scalar kform value q is specified. Assuming HPsi, q≥0. Choose a single zero exponent and real coefficient √(q/2) for every ε. CesaroAbelState.lean defines abelValue(ε,0)=2 for ε>0. Thus the self-form is identically q there, and the one-sided limit and positivity clauses follow. Together with the existing theorem hPsi_of_weilIsGram, this gives equivalence on paper. This singleton does not realize individual primary labels or furnish a common arithmetic construction of Gram vectors. It consumes exactly the unknown sign. The project already describes the equivalence; the explicit witness explains why it cannot mediate the missing analytic estimate on its own.

The independent integer checks in check.py use only the Python standard library. The statements above are paper derivations. No Lean build or RH proof is claimed.
