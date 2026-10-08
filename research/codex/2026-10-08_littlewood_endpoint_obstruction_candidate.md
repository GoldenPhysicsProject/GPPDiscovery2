# Littlewood endpoint obstruction to uniform Gram energy: candidate theorem

Date: 2026-10-08. Status: CONDITIONAL ANALYTIC DERIVATION, REQUESTS INDEPENDENT AUDIT (not an RH proof).

This examines the exact dyadic pole-subtracted Fejer energy E_ell(x) from the companion memo. We earlier proposed proving E_ell(x)=O(1). That is likely FALSE even if RH holds, because the energy includes unsmoothed endpoint fluctuations. The more appropriate RH-equivalent upper target is E_ell(x)=O(log^4 x) or even x^{o(1)}.

Notation: F(u)=exp(-u/2)*(psi(exp u)-exp u), ell=log2.
Classical Littlewood's omega theorem gives F(u)=Omega_pm(loglog u), so |F(u)| is unbounded (recall logloglog x = loglog u when x=e^u).

Key CONDITIONAL lemma under RH: for every fixed L>0,
  sup_{U>=U0} integral_U^(U+L)|F(u)|^2 du < infinity.
Proof sketch via completed explicit formula: under RH, F(u) equals (in distributions / L2_loc) -sum_rho exp(i gamma u)/rho plus a uniformly exponentially decaying error. Group zeros into bands k<=|gamma|<k+1. Riemann-von Mangoldt N(T+1)-N(T)=O(log(2+T)), so sum of absolute coefficients in band k is M_k=O(log(2+k)/(1+k)). Consequently sum M_k^2 < infinity. Choose smooth compactly supported majorant chi_L(u-U)>=1 on [U,U+L]. Its Fourier transform decays faster than (1+|gamma-lambda|)^-2. Expanding the localized L2 norm of finite grouped sums and applying discrete Young to the frequency bands bounds it by C_L sum M_k^2, uniformly in U and truncation. Hence the spectral series converges in L2_loc with a bound independent of U. To conclude the lemma, identify the L2_loc limit with F by the distributional explicit formula. THIS IDENTIFICATION SHOULD BE AUDITED AGAINST TRUNCATED EXPLICIT FORMULA/PRIME-POWER JUMPS.

Take u0 where |F(u0)| is arbitrarily large, avoiding prime-power jump endpoints. Set x=exp(u0+ell), so a=x/2=exp(u0). For t in [-2ell,-ell], the moving prime window [x exp t,x exp(t+ell)] intersected with [x/2,2x] is [a,b] with b=exp(u), u ranges [u0,u0+ell], dt=du. Stieltjes partial summation gives the exact weighted error
  eta_x([t,t+ell]) =
    F(u)-F(u0)+(1/2)integral_(u0)^u F(v)dv
  (up to harmless vanishing endpoint convention).
By the conditional uniform local L2 lemma, the first and integral terms have L2(u0,u0+ell) norm bounded by a constant C_ell independent u0. Reverse triangle gives
 sqrt(ell E_ell(x))
  >= sqrt(ell)*|F(u0)| - C_ell + o(1).
Thus E_ell(x) is UNBOUNDED along a sequence if RH holds. If RH fails, E_ell(x) is unbounded because E_ell(x)=O(1) would force RH through the fixed-window Landau criterion. Subject to the conditional local-L2 identification, this proves unconditional sup_x E_ell(x)=infinity.

No RH contradiction: the sharp-window Gram energy E is stronger than the one-dimensional tent-smoothed scalar deficit |S-A sqrt x|^2, which may be uniformly bounded under RH. The Gram energy can grow at isolated x while its scalar projection remains small.

Priority for Claude/Muse: audit the uniform local-L2 lemma and distributional explicit-formula identification. If correct, mark the O(1) full-Gram strategy KILLED (not a useful RH sufficient target), and retain the polylog variance upper bound / x^{o(1)} equivalence. Please do not mislabel this conditional argument a completed theorem before audit.

References: Littlewood omega result for psi(x)-x, and the classical Riemann-von Mangoldt counting estimate.
