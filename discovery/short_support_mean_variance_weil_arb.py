"""256-bit Arb certificate for a full completed Weil all-functions theorem at L=29/100.

ANALYTIC SUPPLIER (see adjacent .md):
 - exact full gamma/prime/pole SOS;
 - no primes for L=29/100<log2;
 - mean/mean-zero decomposition f=a+g, with ∫g=0;
 - J_jump >= L*w(L)*||g||² from exact pairwise variance identity;
 - pole cosh/sinh = 2|C|²-2|S|²;
 - bound local V-Gamma-c via V>=H(L/2), Gamma<=exp(L/4)-1;
 - complex Young inequality for cross term C=a*C0+∫g*(c-c_bar).

All sign decisions below are certified Arb ball inequalities, not floats.
This certifies Q_L[f] >= ||f||²/100 for every admissible f supported
within [0,L] for 0<L<=29/100. It does NOT imply RH.
"""
from flint import arb, ctx, fmpq

ctx.prec = 256
q = lambda n, d=1: arb(fmpq(n, d))

L = q(29, 100)
eta = q(1, 100)
cinf = (4 * arb.pi()).log() + arb.const_euler()
H = -(L / 4).tanh().log()
gamma_upper = (L / 4).exp() - 1
local_lower = H - gamma_upper - cinf
wL = (L / 2).exp() / (2 * L.sinh())
C0 = 4 * (L / 4).sinh()
cosh_var = L / 2 + (L / 2).sinh() - C0**2 / L
sinh_normsq = (L / 2).sinh() - L / 2
mean_bound = local_lower + 2*(1-eta)*C0**2 / L
fluct_bound = local_lower + L*wL - 2*(1/eta - 1)*cosh_var - 2*sinh_normsq

assert q(0)<L<arb(2).log(), "The claimed interval must be prime-free."
assert cosh_var > 0 and sinh_normsq > 0
assert (L/4).exp() > 1
assert mean_bound > q(1,100), "Mean mode fails the theorem"
assert fluct_bound > q(1,100), "Mean-zero mode fails the theorem"
assert min(float(mean_bound),float(fluct_bound)) > .01
print("support L=", L)
print("V_min=H(L/2) =", H)
print("Gamma_upper =", gamma_upper)
print("contact c_infty =", cinf)
print("uniform local potential lower =", local_lower)
print("J >= L*w(L) variance; L*w(L)=", L*wL)
print("cosh-centered variance norm squared =", cosh_var)
print("odd sinh moment norm squared =", sinh_normsq)
print("MEAN-CHANNEL lower bound (Arb):", mean_bound)
print("MEAN-ZERO-CHANNEL lower bound (Arb):", fluct_bound)
print("CERTIFIED full completed Q_L[f] >= 1/100 ||f||² for all f supported "
      "inside [0,29/100], using zero extension for shorter supports.")
print("Prime-free local theorem ONLY; RH remains OPEN.")
