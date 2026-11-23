# Positivity for four xi faces at two arbitrary distinct magnitudes

Use the centered completion H(z)=ξ(1/2+z) and the real Weil pairing of the adjacent notes. The filter H lies in its radical. For u=r² define two classes

    O(u)=(H(z+r)−H(z−r))/(2r),
    E(u)=((H(z+r)+H(z−r))/2−H(z))/u.

Both are entire in u, by their Taylor series at zero. O is odd in z, E even. Their cross-parity pairings vanish. For P=O or E the relevant normalized two-shift determinant is

    d_P(u,v) = ([P(u),P(u)][P(v),P(v)]−[P(u),P(v)]²)/(u−v)².

Equivalently d_P is the Gram determinant of P(u) and (P(v)−P(u))/(v−u); if v=u the second vector is P′(u). This last definition has no singularity and extends holomorphically in both squared shifts, using the complex bilinear continuation of the real pairing.

The companion certificate encloses both d_P above zero on the entire square [0,1/16]², including its diagonal. Positivity of the diagonal norms of O and E was certified in shift_interval.md. By the two-by-two determinant test, both same-parity blocks are positive definite at distinct u,v, and the four classes combine orthogonally across parity. Returning to the original four packets H(z±r), H(z±s) for 0<r<s≤1/4 gives strict positivity for every nonzero real coefficient vector. The original determinant is 16 r⁶s⁶ (u−v)⁴ d_O d_E: at each magnitude the change from the odd and even normalized packets has determinant of magnitude 2r³, after discarding H. Repeated or zero magnitudes produce dependent or null original packets; the normalized certificate on the boundary concerns the limiting divided differences. The shifted control F_r=H(z+r)H(z−r) remains indefinite on the four-face span since it already has both signs on its two r-faces. Hence the added directions preserve the ζ/control distinction.

## Arithmetic integration

Use Re z=4, s=1/2+z. For real sample u,v and P with parity sign ε, integrate 2εm(z)P(u)(z)P(v)(z), with m=H′/H, over real t=Im z with measure dt/(2π). This is the same residue fold as null_interference.md. Real half-line integration uses conjugation. No zero ordinates enter. The program evaluates the raw Gram matrices on two disjoint Chebyshev grids, 36 and 37 nodes mapped to [0,1/16]. Products are bilinear, without conjugation on the integration line. The raw determinant is divided by the certified nonzero squared gap only at the sample nodes, in ball arithmetic.

For the trapezoid error allow |Im t|≤2 and use the Taylor series in the translation of H on a circle of radius 1/2. For the interpolation bound keep t real and use radius 2 in the translation, permitting |u−1/32|,|v−1/32|≤1. In either setting the shifted s values used to bound H have real part between 2 and 7 and imaginary part differing from Re t by at most 2. The rotated gamma integral, Γ(Re s/2)≤6 by log convexity, |ζ(s)|≤2, and the elementary factors s(s−1)π^(−s/2)/2 give the bound

    B=10⁵ (1+|Re t|)² exp(−π|Re t|/8)

for |H| on the indicated circles. The Euler and digamma series as in shift_interval.md give |m|≤150(1+|Re t|). If the translation-circle radius is ρ, Cauchy bounds the jth Taylor coefficient by B/ρ^j. Summing the odd and even series bounds O and E by 6B on the t-strip at the real sample nodes (u≤1/16, ρ=1/2). On the parameter disks (ρ=2, |u|≤33/32) both packets and their u derivatives are bounded by 2B by summing the geometric series and its derivative. The divided difference is the segment average of the derivative; the disk is convex. Thus for each required Gram integrand, including the divided-difference basis on the parameter disks, an absolute majorant is 10¹⁵(1+|Re t|)⁵ exp(−π|Re t|/4). Its full line integral is <10¹⁹ (expand the polynomial and integrate). In particular the bilinear contour entries on the parameter disks have absolute value <10¹⁹ and |d_P|≤2·10³⁸<10⁴⁰.

The trapezoid step is 1/12 up to T=210 on the positive axis. Fourier contour shift on the t-strip bounds the whole-grid aliasing error before normalization by 2·10¹⁹/(exp(4π·12)−1). The half-grid omitted tail after multiplication by the step is bounded by the integral of the decreasing majorant from T, bounded by its value there divided by π/4−5/(1+T). The program adds both errors conservatively after normalization. Every point operation uses 192-bit Arb or Acb balls.

## Continuous square enclosure

Put a=1/32 and R=1. Univariate interpolation of the normalized determinant at n mapped Chebyshev roots has error ≤3·10⁴⁰/62ⁿ on the real interval: on the complex circle the Cauchy formula uses the ratio of the monic node polynomial bounds 2(a/2)ⁿ/(R−a)ⁿ, with contour factor R/(R−a). The interpolation operator on real data has sup norm ≤2n, by the discrete cosine coefficient formula. Decomposing the tensor interpolation error as (I−I_x)d + I_x(I−I_y)d gives the sum of the two univariate error budgets, the second multiplied by 2·36. Finally the constant tensor Chebyshev coefficient plus or minus the sum of absolute values of all the other coefficients encloses the polynomial on the square. The script includes all arithmetic, integration and interpolation errors before checking positivity.

Run mixed_shift.py beside null_interference.py with python-flint 0.9.0. The result is an arithmetic certificate with analytic bounds and has not been formalized in Lean.

## Ranges and the sign of the actual mixed face entry

The complete run encloses d_O between 1.5998·10⁻¹⁷ and 1.6071·10⁻¹⁷, and d_E between 3.0394·10⁻²⁰ and 3.1047·10⁻²⁰ (rounded outwards). Write g_P(u,v)=[P(u),P(v)]. The identity g_P(u,v)²=g_P(u,u)g_P(v,v)−(u−v)²d_P, the previous diagonal bounds, and |u−v|≤1/16 show that g_O(u,v)>3.74·10⁻⁶ and g_E(u,v)>1.27·10⁻⁶: their squares exceed these thresholds squared and continuity fixes the positive sign from the diagonal. Positive semidefiniteness gives g_E(u,v)<1.29·10⁻⁶ by Cauchy–Schwarz. For σ,τ∈{−1,1}, the ζ pairing of H(z+σr) and H(z+τs) is σ τ r s g_O(u,v)+r²s²g_E(u,v). As rs≤1/16, it has the sign of σ τ for positive r,s. Thus the cross-magnitude entry with opposite faces is strictly negative even while the full four-face form is positive definite.
