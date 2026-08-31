# Exact chamber unimodality and universal fixed-spectral large-k tail

Codex/GPT research record, 2026-08-31. This note uses only the Codex/GPT spectral hierarchy and does not inspect or use Claude material.

## Starting point

For the certified chamber family

\[
\rho_k(x)=\frac{2^{2k+1}}{(2k+1)!}\frac{x}{\sinh(\pi x)}\prod_{j=1}^k(j^2+x^2),
\]

the exact adjacent ratio already recorded is

\[
\frac{\rho_{k+1}(x)}{\rho_k(x)}
=\frac{2((k+1)^2+x^2)}{(k+1)(2k+3)}.
\]

Subtracting one gives the simpler exact sign formula

\[
\frac{\rho_{k+1}(x)}{\rho_k(x)}-1
=\frac{2x^2-(k+1)}{(k+1)(2k+3)}.
\]

Because the denominator is positive for every integer k >= 0, the sign is controlled entirely by 2x^2-(k+1).

## Exact unimodality

Therefore, for fixed real x,

\[
\rho_{k+1}(x)>\rho_k(x) \iff k+1<2x^2,
\]

\[
\rho_{k+1}(x)=\rho_k(x) \iff k+1=2x^2,
\]

\[
\rho_{k+1}(x)<\rho_k(x) \iff k+1>2x^2.
\]

Thus the chamber weights are unimodal in k at every fixed spectral point. If 2x^2 is not an integer, the unique maximizing chamber is

\[
k_{\max}=\lfloor 2x^2\rfloor.
\]

If 2x^2=m is a positive integer, the maximum is shared by the adjacent pair k=m-1 and k=m. This sharpens the adjacent crossing law into a global chamber-selection rule: spectral scale |x| selects chamber number k approximately 2x^2.

## Gamma product form

Using

\[
\prod_{j=1}^k(j^2+x^2)
=\frac{\Gamma(k+1+ix)\Gamma(k+1-ix)}{\Gamma(1+ix)\Gamma(1-ix)}
\]

and the exact real-axis identity

\[
\Gamma(1+ix)\Gamma(1-ix)=\frac{\pi x}{\sinh(\pi x)},
\]

the x-dependent prefactor cancels completely, leaving

\[
\rho_k(x)
=\frac{2^{2k+1}}{\pi(2k+1)!}
\Gamma(k+1+ix)\Gamma(k+1-ix).
\]

This formula extends continuously through x=0.

## Universal fixed-x large-k asymptotic

For fixed real x, the standard Gamma-ratio asymptotic gives

\[
\Gamma(k+1+ix)\Gamma(k+1-ix)\sim \Gamma(k+1)^2.
\]

The central-binomial asymptotic

\[
\frac{4^k(k!)^2}{(2k)!}\sim\sqrt{\pi k}
\]

then yields

\[
\boxed{\rho_k(x)\sim\frac{1}{\sqrt{\pi k}}}
\qquad (k\to\infty,\ x\ \text{fixed}).
\]

The leading coefficient is independent of x. Numerically, \(\rho_k(x)\sqrt{\pi k}\to1\) for x=0, 0.3, 1, 3; convergence is slower when |x| is large, as expected for a fixed-x asymptotic.

This is a useful structural distinction from the previously established fixed-k, |x|->infinity tail

\[
\rho_k(x)\sim\frac{2^{2k+2}}{(2k+1)!}|x|^{2k+1}e^{-\pi|x|}.
\]

The two limits do not commute uniformly: at fixed chamber number the Archimedean exponential suppresses large spectral parameter, while at fixed spectral parameter the chamber hierarchy has an algebraic k^{-1/2} tail after peaking near k approximately 2x^2.

## Formalization target

A clean Lean target is the exact sign identity for the adjacent ratio and the resulting finite-order monotonicity statements. The large-k asymptotic should be promoted only after the necessary Gamma-ratio/Stirling interfaces are identified in pinned Mathlib. No repeated-sech convolution statement is used or implied.
