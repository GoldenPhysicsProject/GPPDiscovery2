# 2026-10-15 polar-aligned Weil multiplier experiment

**Status: algebraic reduction proved, numerical LP failed in tested finite ansatz. RH/GRH OPEN.**

For tests g supported in (-h,h), the full completed zeta polar contribution equals the autocorrelation kernel 2 cosh((x-y)/2), including both even and odd test components:
2(|<cosh(x/2),g>|^2-|<sinh(x/2),g>|^2).

Let W be any even compactly supported continuation with W(t)=cosh(t/2) for |t|<2h. For offsets u_k >= 2h, the cosine symbols cos(u_k xi) vanish in every test quadratic by support separation. Therefore, if the **complete** multiplier
m(xi)=Re digamma(1/4+i xi/2)-log pi -(2 log 2 / sqrt 2)cos(xi log 2)+2 W-hat(xi)-sum_k a_k cos(u_k xi)
can be proved nonnegative on all frequencies, it directly yields full complex Weil positivity for every test in that window. This uses **the actual pole kernel**, not an artificial constant DC lift whose rank-one correction must be subtracted. Only prime 2 enters for h<=1/2.

The code runs a *restricted* floating linear program: W equals cosh(t/2) on [0,2h], continues through 16 piecewise-linear exterior segments to 7, and uses 221 cosine coefficients with offset 2h+k/20. It uses scipy LP on coarse frequency samples and adds offending points. It is not an Arb interval verifier, and its LP feasible/infeasible statuses do not imply a continuum theorem.

Observed local untrusted runs, original version with same formulas and parameters:
- h=0.4: coarse maximum floor approximately -0.00189; fine samples had far more negative narrow dips, so no valid candidate.
- h=0.5: coarse maximum floor approximately -0.00199; fine samples had far more negative narrow dips, so no valid candidate.

These failures do NOT disprove positivity: the exterior ansatz, coefficient bounds, offsets and finite grids are all restrictive. A more flexible positive-definite extension or a dual/spectral operator route may succeed.

At h=1/2, compare against Grok S26 m>=0.0001 PL constant-lift and Astra's positive-pole completion; its C≈7.376 forces |lambda|<0.520705. This polar-aligned alternative completely avoids the artificial negative C|<1,g>|² term, at the cost of a harder global Fourier multiplier extension. See private bridge Codex October 15 notes; do not overwrite Grok/Astra work.
