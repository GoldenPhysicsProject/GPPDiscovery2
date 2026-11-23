# LCM discrepancy in the AFT undamping identity

For a real smooth compactly supported log-coordinate packet f let C(t)=∫f(u)f(u+t)du. Use the D2 damping convention Q_a, multiplying C(t) by exp(−a|t|) in the arithmetic explicit formula. We take a=2. No zero data enter.

The previously used arithmetic undamping formula gives

    Q₀−Q₂ = 2∫₀∞ (exp(t/2)−exp(−3t/2)−exp(−5t/2)) C(t) dt
             −2 Σ Λ(n) w(n),
    w(x) = (1−x⁻²) C(log x)/√x,   x≥1.

Under x=exp(t), 2∫w(x)dx cancels the first two smooth terms exactly. Set D(x)=log lcm(1,…,⌊x⌋)−x+1. A prime power pᵏ multiplies the running LCM by p, and every other integer leaves it fixed. Thus dD=ΣΛ(n)δ_n−dx. Integration by parts has no boundary terms since w(1)=0 and w is compactly supported. Consequently

    Q₀(f) = Q₂(f) − K(f) + 2∫₁∞ D(x) w′(x) dx,
    K(f) = 2∫₀∞ exp(−5t/2) C(t) dt.

K is positive semidefinite by its Fourier multiplier 5/((5/2)²+ξ²), using angular frequency ξ. The formula is an exact rearrangement. Integrality accounts for every prime weight, but gives no immediate sign to the last integral.

## An unconditional obstruction to discarding the work

The translation-invariant background Q₂−K has a strictly negative multiplier at frequency zero. With s=5/2+iξ its multiplier is

    Re ψ(s/2) − log π + 2 Re(1/(s−1) + ζ′(s)/ζ(s)),

where ψ is the digamma. Indeed damping shifts the gamma integral by 2, the damped pair of pole exponentials gives 2 Re(1/(s−1)+1/s), and the absolutely convergent prime sum gives 2 Re ζ′/ζ. Subtracting K removes the 1/s term. At ξ=0 the gamma and rational terms alone sum to 4−γ−π/2−3log 2−log π+4/3 < −0.0388 by the quarter-argument digamma formula. The Euler series is strictly negative there. The full multiplier is approximately −0.6163314570.

For real g smooth and compactly supported with ∥g∥₂=1, set f_R(u)=g(u/R)/√R. Plancherel and the substitution η=Rξ give (Q₂−K)(f_R) tending to that negative constant. Dominated convergence follows from logarithmic growth of the gamma multiplier and rapid Fourier decay of g. Therefore even this explicit smooth background fails positivity on allowed finite-width packets for all sufficiently large R. Global positivity would require liminf of the LCM work along these packets to be at least 0.6163314570 (rounded). This necessary payment only concerns this packet family. A lower bound on the work relative to the background for every packet is still open.

## Reproduction

Run `python experiments/lcm_undamping/check.py` with SciPy. It computes integer LCM jumps and independently integrates the piecewise discrepancy. The three columns are Q₀−Q₂, −K and the work. The check uses sine packets and translated pairs, and agrees to absolute error below 1e−10 in four examples. The work takes both signs. These checks use the displayed unnormalized packet convention. The analytic statements above use smooth test packets.
