# Fixed-N deterioration is a Galerkin under-resolution signal, not yet a prolate no-go

Date: 2026-09-28
Status: quantitative cross-check against public certified/reference window data plus zero-free GPP computations. No RH claim.

## 1. What the 100-digit N=28 scan actually showed

For the literal CCM prolate trial \(k_\lambda\), at fixed Fourier/Galerkin cutoff \(N=28\):

\[
\begin{array}{c|c|c|c}
c & \tfrac12\log c & \lambda_1^{(N=28)} & \epsilon/\Delta\\
\hline
3  &0.5493&5.0235\times10^{-8}&1.897\times10^{-6}\\
5  &0.8047&9.0681\times10^{-18}&2.758\times10^{-7}\\
7  &0.9730&9.7904\times10^{-28}&1.396\times10^{-7}\\
11 &1.1989&2.2356\times10^{-42}&1.353\\
13 &1.2825&7.6821\times10^{-47}&1.277\times10^{6}.
\end{array}
\]

The c=11,13 values initially look like a failure of the vacuum-gap trial-state route.

That conclusion is premature because the finite Galerkin operator itself has ceased to resolve the true window spectrum at \(N=28\).

## 2. Public full-window/reference data expose the finite-N floor

The recent compact-window study arXiv:2608.24827 reports/reference-computes for the full Weil window:

at half-width \(L=0.8\),
\[
\lambda_1^{\rm even}\sim1.65\times10^{-17},
\qquad
\lambda_2^{\rm even}\sim8.38\times10^{-12},
\]
with certified enclosing bounds at this scale;

at \(L=1.0\),
\[
\lambda_1^{\rm even}\sim5.88\times10^{-30},
\qquad
\lambda_2^{\rm even}\sim2.18\times10^{-23};
\]

at \(L=1.2\),
\[
\lambda_1^{\rm even}\sim7.94\times10^{-49},
\qquad
\lambda_2^{\rm even}\sim1.46\times10^{-41}.
\]

Our \(c\) convention has centered half-width
\[
L_{\rm center}=\frac12\log c.
\]

Thus:
- c=5 corresponds almost exactly to L=0.8, and N=28 already agrees in ground scale;
- c=11 corresponds almost exactly to L=1.2, but N=28 gives
  \[
  \lambda_1^{(28)}=2.24\times10^{-42},
  \quad
  \lambda_2^{(28)}=5.95\times10^{-36},
  \]
  about \(2.8\times10^6\) and \(4.1\times10^5\), respectively, ABOVE the reference full-window scales.

Therefore at c=11 the N=28 finite section is nowhere near the continuum/window spectral floor that the prolate comparison is meant to test.

## 3. This matches the public CCM convergence architecture

CCM explicitly takes the parameters \(N,\lambda\to\infty\).

Recent numerical convergence work on the CCM construction also separates:
- finite-basis/mode error;
- finite-prime/window error;
- numerical roundoff.

So increasing arithmetic precision at fixed \(N\) cannot repair a mode-truncation floor.

The 100-digit scan successfully removed ROUND-OFF as the explanation for the c=11,13 deterioration. The public spectral data now identify FINITE-N UNDER-RESOLUTION as the next explanation to test.

## 4. Why the c=11 Rayleigh number is diagnostic

At c=11, N=28:
\[
\langle k,Q_{28}k\rangle\approx8.05\times10^{-36}.
\]

This is of the same scale as the N=28 first excitation
\[
\lambda_2^{(28)}\approx5.95\times10^{-36},
\]
but about \(5.5\times10^5\) times larger than the public reference
\[
\lambda_2^{\rm full}\sim1.46\times10^{-41}.
\]

So the finite section is making the low-mode energy itself too large. The observed \(\epsilon/\Delta\) at fixed N cannot be interpreted as the continuum prolate-vacuum ratio.

## 5. Immediate falsifier

A dedicated N-scaling scan has been launched at fixed c:
- control: c=7, N=20,28,36;
- frontier: c=11, N=28,36,44,56;
- extension: c=13, N=44,56.

The decisive question is whether
\[
\lambda_{1,2}^{(N)}
\]
move toward the public full-window scales and whether
\[
\epsilon_N/\Delta_N
\]
recovers the small values seen before the N=28 truncation floor.

Outcomes:
- if increasing N repairs the ratio, the prolate route survives and we obtain the required N-vs-lambda coupling;
- if the operator spectrum converges but the prolate ratio remains bad, the literal \(k_\lambda\) vacuum-rigidity route is genuinely falsified.

No conclusion should be drawn before this two-parameter test.
