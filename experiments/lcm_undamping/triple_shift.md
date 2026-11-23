# Six reflected xi packets at three shift magnitudes

Let H(z)=ξ(1/2+z), in the centered variable, with the real arithmetic Weil pairing. Zero locations are not inputs. For u=r² use O(u)=(H(z+r)−H(z−r))/(2r) and E(u)=((H(z+r)+H(z−r))/2−H(z))/u. The values at zero are removable, and H is radical. Opposite parity vectors have zero pairing. This extends the two-magnitude test in mixed_shift.md.

For P=O or E and squared shifts u,v,w define D_P as the determinant in the Newton divided-difference basis

    P[u],  P[u,v],  P[u,v,w].

For distinct arguments the raw Gram determinant of P(u),P(v),P(w) is Δ² D_P where Δ=(v−u)(w−u)(w−v). Indeed the triangular change of columns from the Newton vectors to the raw vectors has diagonal 1,v−u,(w−u)(w−v). Its square enters the bilinear determinant. At a triple collision the Newton vectors are P(u),P′(u),P″(u)/2. Holomorphic divided differences give the extension across every collision, including a double collision with the third argument different. The normalized determinant is symmetric in its three nodes by continuation from distinct nodes.

The earlier one- and two-magnitude certificates give strictly positive first and second leading minors in the Newton basis. Positive D_O and D_E therefore suffice by Sylvester's criterion. For distinct positive magnitudes r,s,t the original six-face determinant is

    64 (rst)⁶ Δ⁴ D_O D_E,      (u,v,w)=(r²,s²,t²).

The factor 64(rst)⁶ is the square of the face-to-parity determinant: each magnitude contributes a change of variables of determinant magnitude 2r³ after removing H. Repeated magnitudes duplicate original packets. Strict positivity at collisions in the certificate refers to the Newton vectors. The shifted control F_r remains indefinite on the combined span because its restriction to the r-faces already has both signs.

## Validated quadrature

The certificate computes the two raw Gram kernels for the union of three Chebyshev-root grids. Their sizes 64,65,66 have different powers of two in their factorizations, so no mapped roots coincide between grids (the reduced denominator of a root angle (2j+1)/(2n) has a different power of two). Every small gap is retained as an Arb interval in the normalization.

Use s=10+ix, z=s−1/2, m=H′/H. A raw entry integrates 2ε m(z)P(u)(z)P(v)(z) over the whole real x-line with measure dx/(2π), where ε=−1 for O and +1 for E. This is the right-line residue fold of the companion papers. Reflection permits integration on the positive half-line by taking real parts. No complex conjugation is taken in the products on that line. The code uses 392-bit Acb/Arb, step 1/8, and truncation at T=265.

For |Im x|≤7, include an additional translation circle of radius 1/2 to bound the packet series. All s-values needed to bound H there have real part from 2.5 to 17.5 and imaginary part differing from Re x by at most 1/2. With y=|Re x| the rotated gamma integral at angle ±1.4, Γ(Re s/2)≤40320 by log convexity, |ζ(s)|≤2, and the elementary completion factors yield |H|≤B=10¹⁶(1+y)² exp(−0.7y). The Euler and digamma series give |m|≤200(1+y) on the strip using Re s≥3. Cauchy's bound on the translation circle and geometric summation for 0≤u≤1/16 give |O|,|E|≤6B. Each raw integrand is bounded by 10³⁷(1+y)⁵ exp(−1.4y), with full line integral below 10⁴¹. Fourier contour shift and Poisson summation therefore give an aliasing bound 2·10⁴¹/(exp(14π·8)−1). The omitted half-grid tail, with the grid step included, is bounded by the decreasing majorant integrated from T, at most its value at T divided by 1.4−5/(1+T). The program adds both errors after normalization without taking the beneficial normalization factors. All evaluations of ζ for the quadrature lie in its Euler-product half-plane.

## Bound on the full parameter cube

For complex continuations of u,v,w use the lower line Re z=4 of mixed_shift.md, with a translation circle of radius 2 and real contour variable. On |u−1/32|≤1 the entire series for P has coefficients bounded by B₀/(2^j) for the underlying jth translation coefficient, with B₀=10⁵(1+y)² exp(−πy/8). Explicitly the kth coefficient in squared shift has bound B₀/2^(2k+l) with l=1 (odd) or 2 (even). For divided differences of order j=0,1,2, the complete homogeneous polynomial formula gives the bound

    B₀ 2^(−l) 4^(−j) (1−33/128)^(−j−1) < 2B₀.

This holds simultaneously for all nodes of a divided difference, including repetitions. Consequently each Newton Gram entry has magnitude below 10¹⁹ by the same contour estimate as mixed_shift.md. The determinant is bounded by 6·10⁵⁷<10⁶⁰ on the complex parameter polydisk. The contour form is bilinear there; it extends the real test holomorphically.

For interval half-width 1/32, disk radius 1, and n Chebyshev nodes, Cauchy interpolation error is ≤3·10⁶⁰/62ⁿ as in the two-magnitude certificate. The real sup norm of each interpolation operator is at most 2n. Telescoping the three coordinate interpolations gives total error ≤3·10⁶⁰(62^(−64)+128·62^(−65)+4·64·65·62^(−66)). The constant tensor Chebyshev coefficient plus or minus the sum of absolute values of every other coefficient encloses the interpolating polynomial on the whole cube. All determinant sample errors propagate through the three discrete cosine transforms in ball arithmetic. The script adds the analytic remainder before checking each sign.

Run triple_shift.py beside null_interference.py using python-flint 0.9.0. This is a computational certificate with paper error bounds.

## What would turn a finite-level statement into an all-orders result?

One may restrict a future induction to the predetermined shifts r_n=1/(4n); a continuum certificate at every level is unnecessary. Indeed the closed real span of the time packets for H(z+r_n) contains the packets for every derivative H^(j). To see this, apply any continuous real linear functional annihilating that span. Its evaluation on the packet for H(z+a) is real analytic in a around zero (in fact entire after complexification). In time coordinates this is just exp(au)φ(u), with φ the doubly exponentially decreasing theta kernel. The analytic statement holds in the weighted W^(2,1) packet norm used in parity_split.md, by dominated differentiation on every bounded a-disk. The scalar function vanishes at every r_n, hence identically by accumulation at zero. All its derivatives vanish. Hahn–Banach gives the asserted closed-span inclusion. Polynomial multiples of φ approximate every real smooth compact packet in that norm, as proved in parity_split.md. Thus positivity on every finite prefix of this one sequence implies full Weil positivity; the converse follows by approximation of the translated theta packets. This density argument supplies a sufficient sequence, not an induction step.

## Energy of the third packet after cancellation

For one parity and u≠v, minimize Q(P(w)−aP(u)−bP(v)) over real a,b. Completing the square against the positive two-by-two block gives the ratio of the raw three-by-three determinant to the raw two-by-two determinant. With d_P as in mixed_shift.md, the answer is exactly

    (w−u)²(w−v)² · D_P(u,v,w)/d_P(u,v).

Thus the energy lost when shifts approach each other is accounted for explicitly by squared gaps. The remaining factor is the energy of the second divided difference after its component along the first two Newton vectors is removed. Bounds on that factor concern these prescribed packets, not a uniform lower bound for every packet in every dimension.

## Run results

Outward-rounded cube ranges were 4.8085·10⁻³³ < D_O < 4.8303·10⁻³³ and 1.7487·10⁻³⁶ < D_E < 1.7515·10⁻³⁶. With the preceding two-magnitude certificate these give D_O/d_O > 2.99·10⁻¹⁶ and D_E/d_E > 5.63·10⁻¹⁷. All inequalities use the packet normalization above. A separate run of mixed_shift.arithmetic_grams at (r,s,t)=(1/16,1/8,1/4), using its different contour and quadrature settings, gave normalized determinants 4.820738959·10⁻³³ ± 4.38·10⁻⁴³ and 1.750286293·10⁻³⁶ ± 3.60·10⁻⁴⁶. At the origin a separate point quadrature on xi Taylor jets through degree six gave approximately 4.830259491·10⁻³³ and 1.751451475·10⁻³⁶ (consistency check only).
