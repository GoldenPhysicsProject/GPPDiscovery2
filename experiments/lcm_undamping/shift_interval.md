# Uniform four-entry sign table on the quarter-shift interval

Take H(z)=ξ(1/2+z), A±=H(z±θ), F=A₊A₋ and S=(A₊+A₋)/2. For every real 0<|θ|≤1/4 the equal-weight packet S has strictly negative energy in F and strictly positive energy in H. The certificate uses arithmetic contours throughout and no fitted frequencies or zero locations. The sizes decrease to zero with different powers.

In the real symmetric pairing [U,V]_P=Σ U(r)V(−r) over centered zeros of P counted with multiplicity, reflection gives the four entries

    [A₊,A₊]_F=[A₋,A₋]_F=0,   [A₊,A₋]_F=[A₋,A₊]_F=2Q_F(S).

The diagonal identities follow from A₊(−r)=A₋(r). For V=(A₊−A₋)/(2θ) and W=(S−H)/θ², put L(θ)=Q_F(V) and K(θ)=Q_H(W). The exact parity-split identities give Q_F(S)=−θ² L and Q_H(S)=θ⁴ K; θ=0 has the removable limits of parity_split.md. Both normalized functions are even. The new work bounds both away from zero on the full closed parameter interval. This result concerns this packet family and does not prove positivity on the full ζ quotient.

## Certified analytic interpolation

Write m=H′/H. On z=2+it use the three contour integrands

    I_L=−2(m(z+θ)+m(z−θ)) V(z)²,     I_K=2m(z) W(z)²,     I_J=−2m(z)V(z)².

Integrate each over the whole t-axis with factor 1/(2π). The residue fold is the one proved in the companion parity-split and null-interference notes. For real parameters the integral is the real half-line integral divided by π. The full integral defines the holomorphic extension in θ; one does not analytically continue a real-part operation.

The code computes 44 Chebyshev-root samples with rigorous errors. Each sample uses the infinite trapezoid rule with step h=1/16, truncated at |t|=128. For real θ∈[0,1/4] the integrands are holomorphic on the closed strip |Im t|≤3/4. For t real they are also holomorphic in the separate parameter disk |θ−1/8|≤1/2, with removable divided differences at zero. The following majorant holds in either domain, with x=|Re t|:

    |I| ≤ 10¹² (1+x)⁵ exp(−πx/4).

Here are details of the bounds. The real parts of the underlying zeta arguments for log derivatives are at least 3/2 in the t-strip and at least 15/8 in the parameter disk. For the H derivatives one may move by another 1/8 in the s-plane and retain 11/8≤Re s≤29/8, with |Im s−Re t|≤3/4. Using |ζ(s)|≤5, the gamma integral rotated by ±π/4, Γ(Re s/2)≤2 by log convexity, and the completion s(s−1)π^(−s/2)/2 gives |H|≤400(1+x)² exp(−πx/8) on these derivative disks. The Euler sum gives |ζ′/ζ|≤72 by log n≤8n^(1/8) and the integral test. The Euler digamma series bounds |ψ(w)|≤1+3|w−1| for Re w≥5/8, hence |m|≤100(1+x) on the needed lines and disks. V is the segment average of H′. W is a triangular average of H″ of total mass 1/2, valid along complex straight segments as well. Cauchy's estimate therefore bounds V and W by 8 and 64 times the preceding H bound. Substitution gives the displayed majorant.

Its integral on either horizontal boundary is <10¹⁶, by expanding (1+x)⁵ and integrating exponentials. By contour shift the Fourier transform at frequency ω is bounded by 10¹⁶ exp(−3|ω|/4). Poisson summation and the two geometric tails give trapezoid error ≤2·10¹⁶/(exp(2π(3/4)/h)−1) before normalization. The omitted positive half-grid tail is bounded by the integrated majorant from T because the envelope is decreasing there; the code includes it even without the reducing factor 1/π. The integral is bounded by the majorant at T divided by π/4−5/(1+T).

On the separate θ-circle the same integrated bound implies |L|,|K|,|J|≤10²⁰. For 44 interpolation nodes mapped from [−1,1] to [0,1/4], let a=1/8 be the interval half-width and R=1/2 the contour radius. The monic node polynomial has sup norm ≤2(a/2)^44 on the interval and modulus ≥(R−a)^44 on the circle. The Cauchy interpolation remainder is at most (8/3)·10²⁰/6^44. Finally the discrete cosine transform gives the Chebyshev coefficients of the interpolant. Its constant term plus or minus the sum of the absolute higher coefficients bounds the entire range since |T_k|≤1. All sample enclosures and transformation operations use Arb balls. Thus the result includes shifts strictly between all the sample points, right down to the removable limit.

Run shift_interval.py with python-flint 0.9.0 and the neighboring null_interference.py. This is an interval-arithmetic certificate and paper derivation.

## Every real mixture of the two faces

Let J=Q_H(V), bounded by the third integral. Under H, S is even and V odd, so their cross pairing is zero. For real a,b the identical packet evaluated in both models has energies

    Q_H(aA₊+bA₋) = (a+b)² θ⁴ K + (a−b)² θ² J,
    Q_F(aA₊+bA₋) = −4ab θ² L.

Hence the ζ restriction is positive definite for each nonzero shift in range, with Gram determinant 4θ⁶KJ; the shifted restriction has determinant −4θ⁴L². The ζ Gram matrix in face coordinates has equal diagonals θ⁴K+θ²J and equal off-diagonals θ⁴K−θ²J. The lower bound for J and upper bound for K give J>K/16, so these off-diagonals are negative throughout. Both models thus have negative interference. The ζ self-pairings more than compensate for it, whereas the shifted self-pairings vanish identically. At θ=0 the faces coalesce into the radical filter and strict inequalities degenerate.

The reproducible outward-rounded enclosures, in units of 10⁻⁶, are L∈(6.50,8.00), K∈(1.28,1.29), J∈(3.75,3.85). These are range enclosures; their endpoints need not be attained.
