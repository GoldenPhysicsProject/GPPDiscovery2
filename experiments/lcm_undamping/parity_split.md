# Derivative packets after quotienting by the xi null filter

Let H(z)=ξ(1/2+z), with centered Laplace variable z. For real time packets use the real symmetric pairing [U,V]_P=Σ U(r)V(−r) over the centered zeros of an even real completion P, counted with multiplicity. Write Q_P(U)=[U,U]_P. All transforms below decrease exponentially in imaginary height on vertical strips. We use the standard explicit formula and paired Hadamard expansion for ξ. RH is not assumed.

## Positive two-dimensional subspace

H is in the radical of its own pairing. Put E₁=H′ and E₂=H″/2. Then [E₁,E₂]_H=0 by parity and pairing r with −r. The arithmetic certificate gives 2Q_H(E₁) ∈ (7.6488,7.6490)·10⁻⁶ and Q_H(E₂) ∈ (1.2850,1.2852)·10⁻⁶. The two classes are therefore independent modulo the radical, and every nonzero real combination has strictly positive energy. Here and below the magnitudes depend on the standard ξ normalization.

## Shift splitting of the null direction

Write A=H(z+θ), D=H(z−θ), Fθ=AD, S=(A+D)/2, V=(A−D)/(2θ), and W=(S−H)/θ². For real nonzero θ,
 
    Q_Fθ(S) = −θ² Q_Fθ(V),          Q_H(S) = θ⁴ Q_H(W).

At each zero of Fθ one has S²=θ²V² because S²−θ²V²=AD. S is even and V is odd, which supplies the minus sign in the first pairing. The second equality uses the full radical property of H. At θ=0 the removable limits are V=H′ and W=H″/2. Also F₀=H², whose pairing is twice that of H. By continuity the very same even packet S has positive ζ energy and negative shifted-model energy for every sufficiently small nonzero real shift. At θ=1/4 the script independently certifies Q_Fθ(V) ∈ (6.5100,6.5102)·10⁻⁶ and Q_H(W) ∈ (1.2810,1.2812)·10⁻⁶. No selected carrier or zero height is used. The argument does not quantify the neighborhood or cover the intervening shifts.

Continuity follows on Re z=5/4 from the arithmetic contour below. Divided differences are averages of derivatives on the shift segment; in any small closed shift neighborhood around zero the gamma decay is uniform, and all logarithmic derivatives there are evaluated in the Euler convergence half-plane.

## Why the entire derivative family tests the full form

For this paragraph, coefficients are real. In log time write H(z)=∫φ(u)exp(zu)du, absorbing normalization into the standard Riemann theta kernel. Here φ is smooth, even, strictly positive everywhere, and all its derivatives decrease faster than every exponential. For u≥0 this follows from the explicit theta series with positive factors 2πn²exp(2u)−3; evenness supplies the negative half. Then H^(j) is the transform of u^j φ(u).

A sufficient norm for continuity of the Weil pairing on these packets is the sum of the weighted L¹ norms of g, g′ and g″ with weight exp(|u|). Two integrations by parts give |U(σ+it)| ≤ C ∥g∥/(1+t²) uniformly for |σ|≤3/4. The zero count gives absolute convergence and continuity of the bilinear sum. Compact smooth cutoff approximations to u^j φ converge in this norm. Conversely, for any real smooth compact g write k=g/φ. It is smooth and compact. Fourier inversion expresses g as an integral of modulations φ(u)exp(iyu) against the rapidly decaying Fourier transform of k. The weighted norm of a modulation grows at most as (1+|y|)², so truncation and finite Riemann sums converge in that norm. At fixed y, Taylor polynomials of exp(iyu) times φ converge in the same norm, including both derivatives, by double-exponential decay. Taking real parts gives approximation by real polynomial multiples of φ. Thus positive semidefiniteness of all finite derivative matrices is equivalent to Weil positivity on the usual real compact tests. Each matrix splits into even and odd blocks. The null row j=0 may be deleted. With E_j=H^(j)/j!, the implementation also certifies the first two-dimensional block in each parity: (E₁,E₃) and (E₂,E₄). Together these give a positive definite four-dimensional subspace modulo the radical. Extending these block tests to all orders remains open.

## Arithmetic reproducibility and absolute errors

Use python-flint 0.9.0 and run parity_split.py alongside null_interference.py. No zero ordinates enter. With z=5/4+it, m=H′/H, mθ=Fθ′/Fθ, the right-line residue fold for the first four outputs integrates the real parts of −4m(H′)², 2m(H″/2)², −2mθ V² and 2m W² on t≥0, divided by π. This uses the exponential decay and the contour folding justified in null_interference.md. For j,k of the same parity the further entries use 2(−1)^k m E_j E_k. All expressions are analytic in the complex quadrature variable before taking real parts. The script uses exact rational shifts, 112-bit Arb point enclosures, and Gauss nodes and weights enclosed by Arb.

Here are bounds specific to this certificate. On disks of radius 1/4 around real t in [0,110], the previous file's bounds |H shifted| < 200000 and |m shifted| < 400 apply (the real parts of the zeta arguments lie between 5/4 and 9/4). For the central jet apply Cauchy on an additional radius 1/8 in the s variable; its real part then remains in [11/8,17/8], and the same elementary gamma/Euler bounds apply at heights <112. Hence |H′| ≤ 8·200000 and |H″/2| ≤ 64·200000. For θ=1/4 use |V| ≤ 4·200000 and |W| ≤ 32·200000. For j=3,4 the Cauchy factor is 8^j, so even the fourth coefficient is bounded by 4096·200000. Substitution bounds every integrand by 10²¹. The order-32 rule on panels of width 1/8 integrates degree 63 exactly. Cauchy on those disks and positivity of the quadrature weights give total finite integral error ≤ 2T·10²¹·4⁻⁶⁴/(1−1/4).

On the real tail t≥110 the rotated-gamma bound applies also on the central s-disks of radius 1/8, with |H| ≤ 20(1+t)²exp(−πt/8) there (absorbing the imaginary-height displacement). Cauchy supplies factors 8 and 64 for the first two Taylor coefficients. On the integration lines |m shifted| ≤ 20(1+t). Combining these bounds, including both terms of mθ, and factors up to 4096 for the fourth coefficient, gives 10¹²(1+t)⁵exp(−πt/4) for each integrand. Integrate this majorant using its logarithmic derivative as in null_interference.md. The program includes both errors before making any sign assertion. This is a paper derivation with an interval-arithmetic certificate, not a Lean proof.

The odd (E₁,E₃) determinant is enclosed by 1.600e−17 ± 3.64e−21; the even (E₂,E₄) determinant by 3e−20 ± 1.07e−21. The mixed entries in both two-dimensional blocks are strictly negative. The entire four-dimensional form is positive definite.
