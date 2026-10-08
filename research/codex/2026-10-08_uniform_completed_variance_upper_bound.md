# Uniform completed prime-variance estimate, 2026-10-08

Status: unconditional analytic bound, but not RH. Companion to the full exact Hilbert sewing memo in the same directory.

Let ell=log(2) and d eta_x(v) be the arithmetic von Mangoldt measure
sum_{x/2<=n<=2x} Lambda(n)/sqrt(n) delta_{log(n/x)}(dv)
minus its correct continuum pole measure sqrt(x)*exp(v/2)*1_{[-ell,ell]}dv.
Set
  E_ell(x)=(1/ell)*integral_R |eta_x([t,t+ell])|^2 dt.
This is the exact nonnegative triangular Gram energy of the pole-subtracted dyadic current.

For fixed ell, Korobov-Vinogradov yields
  psi(y)-y=O(y*exp(-c(log y)^(3/5)/(loglog y)^(1/5))).
For all endpoints a,b in [x/2,2x], partial summation with weight u^(-1/2) gives a uniform interval discrepancy
  |sum_{a<=n<=b}Lambda(n)/sqrt(n) - integral_a^b du/sqrt(u)|
   <= C sqrt(x)*exp(-c'(log x)^(3/5)/(loglog x)^(1/5))
for sufficiently large x and c'>0.

Since the sliding window t has support of length 3ell, squaring and integrating gives the GENUINE unconditional signed and pointwise variance inequality
  0<=E_ell(x)
      <= C_ell*x*exp(-2c'(log x)^(3/5)/(loglog x)^(1/5)).
No zero hypothesis used.

By the exact Fourier identity for the tent,
  |S_ell(x)-A_ell sqrt(x)|^2 <= E_ell(x).
Hence this bound recovers a PNT-strength dyadic discrepancy estimate.
Under RH the classical von Koch bound psi(y)-y=O(sqrt(y)log² y) would instead imply E_ell(x)=O(log^4 x). The project's fixed-window criterion gives the converse: E_ell(x)=x^{o(1)} implies RH. Thus uniform variance x^{o(1)} remains an RH-strength estimate. The classical unconditional estimate has exponent 1-o(1), so the crucial power saving is entirely missing.

External classical source: Terence Tao ExpDB blueprint, Distribution of primes: long ranges, Theorem 14.4 (Vinogradov-Korobov bound). This is not a novel zero-free region.

Next target: direct arithmetic cancellation between prime-prime and negative prime-continuum terms in the exact Gram expansion, strong enough to improve x^{1-o(1)} to x^{o(1)}. Pure positivity provides no upper bound; any new signed inequality must use the actual one-channel coefficients and not apply to shifted products F_theta.
