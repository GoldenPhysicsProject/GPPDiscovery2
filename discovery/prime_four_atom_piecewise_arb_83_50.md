# Prime Hardy-Schur rational supersolution at L=83/50 (1.66)

2026-10-31 Codex / GPPDiscovery2. Exact analytic Hardy + weighted edge-SOS reduction, Arb input enclosures, and a **1,024-cell exact-rational witness**. GitHub Actions confirmed success.

## Verified conclusion

For the corrected v34 semilocal positive Archimedean kinetic E and actual signed prime-power source S, and **all** complex finite-kinetic f with support in [0,L], **0<L≤83/50=1.66**:

\[
\boxed{E_L[f]-S_L[f]\ge \frac{1}{1250}\|f\|_2^2.}
\]

At L0=83/50 the complete active prime-power set is {2,3,4,5}. This is a **weaker numeric margin but a larger window** than the prior L=41/25=1.64 with 1/125.

## Rigorous proof and certificate

The Hardy zero-extension inequality E≥∫V|f|² uses V_L(x)=½[H(x)+H(L−x)], H(z)=log coth(z/2). A nonnegative prime adjacency A h(x)=Σ w_n [1_(x+a_n<L) h(x+a_n)+1_(x>a_n)h(x−a_n)], a_n=log n, w_n=log p/sqrt n. The exact weighted edge square gives S≤∫(A h/h)|f|². A positive profile satisfying A h≤ρ V h therefore gives E−S≥(1−ρ)∫V|f|².

At L0=83/50, choose ρ=999/1000 and an explicit strictly positive piecewise **rational** h on 1024 rational equal cells (each height denominator 10⁶, determined initially by float iteration then frozen as rational). The reproducible Python/FLINT 256-bit script checks:

1. Rational two-sided brackets for log2, log3, log4, log5 rigorously contain Arb logarithms.
2. Rational upper weights rigorously exceed each Arb log(p)/sqrt(n).
3. Convex symmetry of V means each cell's exact minimum is at the clamped midpoint L/2. A rational lower bound for V at that point is Arb verified.
4. All possible shifted-target cell indices are conservatively covered from exact rational bounds (possible overcount). The 1024 one-sided Schur inequalities use Python Fraction ONLY, checking
Σ_{edges} w_n^+ max_(possible targets j) h_j < (999/1000) V_i^- h_i.
5. Minimum **exact rational slack = 186490315607513/1000000000000000 ≈ 0.1864903156** (at cell 327), strictly positive.
6. Arb reports H(L0/2) in interval centered at 0.93468421038545189384880814023... with ~7.61×10⁻⁷⁷ radius; comparison H(L0/2)>4/5 yields (1−ρ)H(L0/2)>1/1250. The actual scalar from H is about 0.00093468421.
7. For all shorter support intervals the identical ambient E and S forms are tested by zero-extending the f supported in the shorter interval into [0,L0]. No hypothesis about monotonicity of discontinuous h is needed.

This is an **all-functions proof for the specified quadratic form**; the Arb component verifies only transcendental inequalities. The floating-point iteration used to discover the rational h does not certify anything by itself.

**Source:** https://github.com/GoldenPhysicsProject/GPPDiscovery2/blob/codex/discovery-workbench/discovery/prime_four_atom_piecewise_arb_83_50.py

**CI:** https://github.com/GoldenPhysicsProject/GPPDiscovery2/actions/runs/41212545778 **SUCCESS**, exact head 3eebf71a393ed890140cf96c7cd0f5a557975efc. The immediately preceding coarse 512-cell ρ=.99 run 41212481566 FAILED, at cell 0. That failure is recorded and was not silently misreported.

## Logical boundary and obstruction

This is E−S, not the full completed Weil form Q = (E−S)+P−c∞||f||²−A. Full completed Q positivity still only certified on prime-free supports L≤5/32. At L≥1.66, the Hardy-local-potential-only proof is close to the spectral threshold: approximate (not certified) positive prime adjacency spectral radius / V is ~0.98 and rises beyond 1 near L≈1.68. Consequently extending this *particular positive supersolution method* much farther may require the positive **interior jump** and **prime edge squares** retained in discovery/semilocal_full_gamma_prime_pole_sos.md rather than only Hardy boundary potential.

**Next:** prove a moment-aware bound using full jump energy, pole parity decomposition, and negative contact + gamma tilt. Verify already includes PathSOS and PoleCoshSinh finite algebra; do not restate those as new. RH remains open.
