# Codex/GPT cross-front continuation — scalar DCT closure and Fisher strict endpoint

Date: 2026-08-30
Track: Codex/GPT only

## 1. Raised scalar box: analytic regulator limit is now closed

For Euclidean invariants S,T>0, write

Q(x)=S x1 x3 + T x2 x4,  x4=1-x1-x2-x3,

on the standard affine 3-simplex Delta_3.  Verify2 already certifies interior positivity, pointwise convergence Q^{-eps}->1, and the one-channel bound

Q^{-eps} <= 1 + (S x1 x3)^{-delta}

for 0<=eps<=delta and 0<delta<1.  The exceptional boundary set is Lebesgue-null, so pointwise convergence holds almost everywhere for dominated convergence.

The majorant is integrable.  Integrating the spectator x2 coordinate first gives

int_{Delta_3} (x1 x3)^{-delta} dx
 = int_{x1>=0,x3>=0,x1+x3<=1}
     x1^{-delta} x3^{-delta} (1-x1-x3) dx3 dx1
 = B(1-delta,3-delta) B(1-delta,2)
 = Gamma(1-delta)^2 / Gamma(4-2 delta).

Hence

int_{Delta_3} [1 + (S x1 x3)^{-delta}] dx
 = 1/6 + S^{-delta} Gamma(1-delta)^2/Gamma(4-2 delta) < infinity.

Therefore, by dominated convergence along eps->0+,

J_eps(S,T) := int_{Delta_3} Q(x)^{-eps} dx  ->  1/6.

This is an honest analytic closure of the raised-box regulator limit.  The remaining task is formal, not mathematical: package the AE boundary removal and nested interval DCT in Lean.  Mathlib exposes `intervalIntegral.tendsto_integral_filter_of_dominated_convergence`, which accepts an arbitrary countably-generated regulator filter and exactly the eventual-AE domination/interface needed here.

This result should not yet be reported as Lean-certified until the concrete `simplexMoment` theorem is in Verify2 and CI-green.

## 2. Prime-gas Fisher geometry: strict endpoint has a shorter route

Audit correction: `PrimeFisherCenteredGeometry.normalized_centered_quadratic_pos` already proves strict positive-definiteness of the full countable normalized centered score for every beta>1 and nonzero (a,b).  `PrimeFisherCountableGeometry` currently packages only normalized determinant nonnegativity.

The abstract algebraic bridge `StrictQuadraticDeterminant.det_pos_of_quadratic_pos` is already present, and `PrimeFisherHankelSchurBridge` proves the exact Schur identity

 det H3 = m0^3 det Cov(X,X^2).

Thus no countable Cauchy-Binet construction is required.  The shortest formal endpoint is either:

1. identify the centered quadratic expectation with
   A a^2 + 2 B a b + C b^2
   and apply `det_pos_of_quadratic_pos`; or
2. prove strict positivity of the 3x3 raw Hankel determinant from the degree<=2 Gram theorem and apply the existing Schur bridge.

Route (1) is preferred because it identifies the actual statistical metric coefficients and feeds the entropy/free-energy geometry directly.  The only missing Lean content is the summable `tsum` expansion; moments through degree four are already summable.

## 3. Principal-series / spectral / Weil boundary

The focused kinematic paper remains consistent with Verify2: the Mellin transform of (2 sinh t)^{-1} gives (1-2^{-s}) Gamma(s) zeta(s), but this is an archimedean/additive reformulation and does not encode the multiplicative prime interference needed for RH.  The exact one-loop Mehler-Fock/Macdonald resummation to the known dilogarithmic box function is still open.

The all-real Gamma/Wiener-Hopf weight and strict chamber hierarchy are already formalized.  They must remain distinguished from the scalar SL(2,C) Plancherel density and from global Weil positivity.  The global arithmetic frontier remains a relative prime-plus-Archimedean trace/Gram operator with a non-circular positivity/contractivity theorem.

## 4. YM / gravity frontier

No status inflation.  Existing Verify2 modules certify state counts, Ward reconstruction, generic rational defects, mu^4 dimension shifting and mu^8 gravity radial algebra.  The next honest physics theorem is the explicit fixed-loop-momentum mu!=0 Yang-Mills tree numerator together with sewing over the three physical massive-vector polarizations.  Generalized and higher-loop cuts should follow only after that identification.

## 5. CI / branch discipline

Verify2 head 43fe174d534050dfce0b56e1437394dcc7f422fe is still under full-construction and finite-core CI.  No terminal new failure was available during this run, so Verify2 was deliberately not reset with a speculative Lean commit.  The scalar analytic theorem above is recorded here for formalization once the current certification cycle resolves.
