# Codex/GPT research rotation — continuous sech majorants

Date: 2026-09-07

## Certified starting point

Verify2 head `953a07ff97e818f6e375e463ac3df2286384e3f1` passed full Build #2102. Thus the global quadratic Lévy-density bound is certified:

\[
|x|^2\,\nu_c(x)\le \frac{c}{\pi},\qquad
\nu_c(x)=\frac{c}{|x|\sinh(\pi|x|)},\quad c\ge0.
\]

## New exact pointwise majorants

For the compensated kernel

\[
K_c(t,x)=(1-\cos(tx))\nu_c(x),
\]

two complementary pointwise bounds hold for every real `t,x` and `c>=0`:

1. Since `-1 <= cos(tx)`,
   \[
   0\le K_c(t,x)\le 2\nu_c(x).
   \]
   This is the tail-side domination to combine with the already-derived exponential tail of `nu_c`.

2. Since `1-cos y <= y^2/2` and `|x|^2 nu_c(x) <= c/pi`,
   \[
   0\le K_c(t,x)\le \frac{t^2 c}{2\pi}.
   \]
   This is the origin-side cancellation bound. It makes the removal of the raw `x^{-2}` singularity explicit at the integrand level.

Together these sharpen the future integrability proof to the standard split

\[
K_c(t,x)\le \min\!\left(\frac{t^2c}{2\pi},\,2\nu_c(x)\right),
\]

with the first bound used on a bounded neighborhood of zero and the second used with exponential decay in the tails.

Verify2 workbench commits `63d8b82f51e95383cc6a5fdef0cbdd33ec7f6e49` and `e72649bd2e9fb3bdfe2608eeba1ab4c14f9705d0` encode the two pointwise bounds. They are under CI and must not be called certified until terminal green.

## Spectral/principal-series source mining

The focused `kinematic_block_v1-1.tex` source contains exact useful mathematics: conical Legendre-Q reduction, the shadow degree involution, Mehler-Fock connection, principal-series temperedness, the `Delta=2s` dictionary, and the Gamma/digamma Mellin bridge. It also still describes `P(lambda)=pi lambda/sinh(pi lambda)` as a Plancherel loop measure. Current Codex formalization deliberately keeps the exact Gamma/Wiener-Hopf/phase-space identity separate from a claim that this is the genuine `SL(2,C)` Plancherel density, unless an independent representation-theoretic theorem is supplied.

The statement that zeros of `(1-2^{-s}) Gamma(s) zeta(s)` occur at zeta zeros is tautological because zeta is already a factor; no RH consequence is assigned to it.

## Other active fronts

- Scalar celestial cut/dispersion/raised-box chain remains formally closed at `J_epsilon(S,T) -> 1/6` on its stated physical parameter domain.
- Yang-Mills remains blocked by direct construction of the opposite/pre-sewing full-conic tree with all uncut propagators retained. Existing covariance and complementary-helicity phase cancellation do not determine the physical `D_s=4` master coefficient. Next physical step is vector-minus-scalar sewing followed by genuine Badger `T1/T2/T3` extraction.
- Prime-gas two-parameter thermodynamic geometry remains certified through `R(beta,eta)<1/2` for `eta>0`; no stronger curvature sign was obtained in this rotation.
- Completed-zeta/Weil work remains blocked by unconditional positivity of the completed prime-plus-Archimedean Weil quadratic form. Local principal-series, Gamma, Mehler-Fock, Wiener-Hopf and heat/Hausdorff reductions do not close that global positivity theorem.

## Next exact chamber frontier

After CI terminalizes, formalize the tail exponential bound for `nu_c`, then package the actual integrability of `K_c(t,.)`. The next load-bearing analytic identity is

\[
\int_{\mathbb R} K_c(t,x)\,dx = 2c\log\cosh(t/2),
\]

which is equivalent to the Lévy-Khintchine exponent

\[
\log \operatorname{sech}^{2c}(t/2)=\int_{\mathbb R}(\cos(tx)-1)\nu_c(x)\,dx.
\]

Only after that integral identity is proved should genuine characteristic-function infinite divisibility be promoted. The explicit Gamma-density identity remains the independent Beta/logistic/Fourier-uniqueness route.
