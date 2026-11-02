# Theta-lattice zero prediction, phase quantization, and one-mode arithmetic stability test

Date: 2026-11-02  
Project: GPP Discovery2, exploratory numerical research  
Status: **independently reproduced numerical experiment, not interval-certified; no proof of RH**

## Executive result

The exact completed-ξ theta representation gives an unusually efficient **finite integer-lattice predictor** for the first zeta zeros. The Archimedean gamma phase alone predicts their approximate locations (errors about 0.37--0.69 in the first five); adding theta modes labeled only `n=1,2` predicts the first five with errors ranging from `2.5e-9` to `0.0038`; adding `n=3` makes the first five agree within observed double-precision quadrature errors (up to `1.4e-7` at the fifth zero).

A separate adversarial experiment exposes a fine dependence on the exact integer-lattice weights. Multiplying just the `n=2` term by `1.00008` (a `+0.008%` change) produces a real-entire, reflection-symmetric deformation of completed ξ with **off-critical-line zeros within the critical strip** at approximately

\[
s=0.1986402303+31.1927894925i,\qquad
s=0.8013597697+31.1927894925i,
\]

plus their complex conjugates. As the `n=2` weight increases from one, the two on-axis zeros originally at 30.4248761259 and 32.9350615877 collide at approximately `t=31.21941756`, `alpha=1.000073050695`; above this they move off the real `t` axis.

This is **not a counterexample to RH**, since the deformed entire function is not zeta and is not claimed to have an Euler product. It is a sharp stress test of any alleged derivation of RH from gamma geometry, the functional equation, reality, or reflection symmetry alone. The exact arithmetic weights matter.

## 1. Exact theta source and arithmetic labels

The established completed theta identity, already used in [`CELESTIAL_JENSEN_SOURCE_MICROSCOPE.md`](https://github.com/GoldenPhysicsProject/GPPDiscovery2/blob/main/experiments/CELESTIAL_JENSEN_SOURCE_MICROSCOPE.md), is

\[
\xi(s)=\frac12+s(s-1)\sum_{n=1}^\infty\int_0^\infty
e^{u/4-\pi n^2e^u}\cosh\!\left(\frac{s-1/2}{2}u\right)du.
\]

Writing `s=1/2+it`, define

\[
I_n(t)=\int_0^\infty e^{u/4-\pi n^2e^u}\cos(tu/2)du,
\quad
\Xi_N(t)=\frac12-\left(t^2+\frac14\right)\sum_{n=1}^NI_n(t).
\]

Then `Xi(t)=xi(1/2+it)=lim_N Xi_N(t)` exactly. Each `I_n` extends to an even entire function of `t`. The labels `n=2,3` are prime integers and `n=4` is composite, but **these are theta-lattice terms, NOT prime-local Euler-product factors**. No assertion about an Euler-product truncation is justified by these results. The constant `1/2` and the Gaussian/Poisson completion are indispensable.

For real `t`, a non-asymptotic analytic *function-value* truncation bound follows directly from `e^u>=1+u` and `e^{u/4}du = x^{-3/4}dx` with `x=e^u`:

\[
|\Xi(t)-\Xi_N(t)|\le
\left(t^2+\frac14\right)
\frac{e^{-\pi(N+1)^2}}
{\pi(N+1)^2\big(1-e^{-\pi(2N+3)}\big)}.
\]

At the first zero, the bounds are about `5.55e-5` (`N=1`), `3.72e-12` (`N=2`), `5.89e-22` (`N=3`). These **do not certify root positions**: a separate nonzero derivative/interval enclosure, plus interval-certified quadrature, would be required. The displayed numerical residual after `N=3` is floating-point limited.

## 2. Meta-rule from the gamma phase alone

For `t>0`, use the Hardy theta phase

\[
\vartheta(t)=\operatorname{Im}\log\Gamma\left(\frac14+\frac{it}{2}\right)-\frac t2\log\pi.
\]

The smooth Riemann--von Mangoldt counting function is `N_smooth(t)=1+theta(t)/pi`. If its `n`-th zero is placed at the midpoint `N_smooth(t)=n-1/2`, the **heuristic gamma-only predictor** is

\[
\vartheta(t_n^{\rm gamma})=\left(n-\frac32\right)\pi.
\]

The leading Stirling inversion gives an explicit approximate prediction without zeta evaluation:

\[
t_n^{\rm Lambert}
\approx\frac{2\pi a_n}{W_0(a_n/e)},\quad a_n=n-\frac{11}{8},
\]

where `W_0` is the principal real Lambert-W branch for the values considered.

First five results (reference roots **independently computed** by a convergent Euler-transformed alternating eta representation of Hardy `Z(t)`):

| n | Hardy-Z root | gamma midpoint | gamma error | theta `n<=2` predictor | theta `n<=2` error |
|---:|---:|---:|---:|---:|---:|
| 1 | 14.134725141735 | 14.517919628 | +0.383194 | 14.134725144221 | +2.49e-9 |
| 2 | 21.022039638772 | 20.654044969 | -0.367995 | 21.022039236 | -4.03e-7 |
| 3 | 25.010857580146 | 25.491508215 | +0.480651 | 25.010865228 | +7.65e-6 |
| 4 | 30.424876125860 | 29.738510300 | -0.686366 | 30.424322575 | -5.54e-4 |
| 5 | 32.935061587739 | 33.623793073 | +0.688731 | 32.938763876 | +3.70e-3 |

With theta `n<=1`, a blind scan on `12<t<35` finds only two real crossing zeros, near `14.165949688` and `19.563938863`; with theta `n<=2`, the scan finds five roots; with `n<=3`, all five match the independent Hardy-Z reference to within `1.4e-7` in this double-precision test. The `n<=4` scan does not improve the visible precision at this height. At increasing height the completed xi amplitude shrinks rapidly and cancellation becomes serious; a rapidly decaying **absolute** theta tail need not give a small **zero ordinate** error.

The known exact Riemann--von Mangoldt count includes an additional oscillatory term `S(t)=(1/pi) arg zeta(1/2+it)` with a specified continuation convention, so the gamma midpoint alone cannot fix individual ordinates. A prime-based formula for that oscillatory phase requires continuation/regularization; the ordinary Euler-product phase series only converges absolutely when `Re(s)>1`.

## 3. One-theta-mode deformation as an adversarial control

For real `alpha`, change only the `n=2` term:

\[
\boxed{\Xi_\alpha(t)=\Xi(t)-(\alpha-1)\left(t^2+\frac14\right)I_2(t).}
\]

In the `s` coordinate this is the same entire theta expression with coefficients `c_n=1` except `c_2=alpha`. It preserves

\[
\xi_\alpha(s)=\xi_\alpha(1-s),\qquad
\xi_\alpha(\overline{s})=\overline{\xi_\alpha(s)},
\]

because the integral is entire and has the required cosine-hyperbolic/real symmetries. It is *not* assumed to be an authentic completed L-function and no Euler product is asserted.

As alpha increases, the fourth and fifth real-`t` zeros meet. A numerical double-root condition is obtained by eliminating alpha from `Xi_alpha(t)=0`:

\[
\alpha(t)=1+\frac{\Xi(t)}{(t^2+1/4)I_2(t)},\qquad
\alpha'(t_*)=0.
\]

The observed collision is

\[
t_*\approx31.2194175619,\quad
\alpha_*\approx1.000073050695.
\]

With `alpha=1.00008`, two real-`t` zeros cease to be real and a conjugate pair is found at

\[
t\approx31.19278949251\pm0.30135976971i,
\]

equivalently zeros of `xi_alpha(s)` at `s≈0.19864023029+31.19278949251i` and `s≈0.80135976971+31.19278949251i` (and conjugates). Both lie **inside** `0<Re(s)<1` but **off** the line `Re(s)=1/2`.

Two numerically independent evaluations agree:

1. Evaluate completed `xi(s)` from Euler-transformed eta, multiply by the completed gamma factor, then add only the `I_2` perturbation. Complex root residual approximately `9e-23` in double-precision arithmetic.
2. Evaluate the entire deformed theta integral directly with `n=1,2,3,4`; at the same complex root, residual about `1.1e-16`. Higher theta modes have an extremely small analytic tail here.

The tiny residuals **do not** by themselves provide a certified complex-zero enclosure: derivative bounds, quadrature interval enclosures, or an argument-principle/Rouché certificate remain to be constructed. Local real-zero count changes and a conjugate pair's location were observed in numerical scans; no claim of global zero-count completeness is made.

## 4. What the experiment means for GPP

1. **The smooth scaling phase is real information, but insufficient.** It predicts a broad zero-count geometry and approximate ordinates without evaluating zeta, but arithmetic fluctuations determine exact roots.
2. **Finite theta modes are powerful predictors** of low zeros, using an *exact completed identity*. Their efficiency is a numerical representation fact, not a new zero-location theorem or proof of RH.
3. **Reflection symmetry is insufficient for critical-line confinement.** The minuscule `n=2` perturbation retains entire reflection symmetry yet generates a numerical off-line quartet in the critical strip. This makes an extremely concrete false-control target for a proposed arithmetic-to-celestial/unitary boundary construction.
4. **The arithmetic intertwiner must be exact enough to distinguish the true theta weights.** A merely formal principal-series symmetry or gamma phase will accept adversarial deformations; it cannot establish RH. This aligns with the previously certified raw-Weil OS-reflection no-go and the need to build a genuinely different reflection-positive boundary covariance whose arithmetic image is the full signed completed Weil form.

The observed collision/splitting is reminiscent of a symmetry-preserving spectral *exceptional-point-like* bifurcation; this is a **mathematical analogy**, not evidence that an operator, non-Hermitian Hamiltonian, or physical bulk has been constructed.

## 5. Reproduction and next proof obligations

Run `experiments/zero_meta_rule_theta_probe.py` with NumPy/SciPy. It computes the first five Hardy-Z zeros independently via Euler-transformed eta, gamma/Lambert rules, theta finite-mode roots, the first-zero analytic tail bounds, the alpha-controlled root counts, the double-root collision, and the off-line complex root with independent theta-vs-eta residual checks.

The immediately testable mathematical next steps are:

- Interval-certify the `alpha=1.00008` off-line pair (small Rouché disk or interval-Newton), then certify `alpha_*` double-root bifurcation; use it as a formal **false-control**.
- Repeat at greater heights with arbitrary precision and isolate the `S(t)` arithmetic phase via a completed, consistently regularized prime trace. Avoid confusing the theta `n` labels with an Euler-product prime decomposition.
- State the necessary spectral property which is preserved at alpha=1 but necessarily fails for alpha just above alpha*; distinguish mere even/reality symmetry from genuine self-adjointness/positivity plus a faithful arithmetic intertwiner.
- Challenge any proposed global holographic/KMS/OS construction with this theta-weight deformation **and** established shifted-zeta/Davenport--Heilbronn controls before treating it as an RH mechanism.

All figures above are exploratory numerical computations; RH remains open.
