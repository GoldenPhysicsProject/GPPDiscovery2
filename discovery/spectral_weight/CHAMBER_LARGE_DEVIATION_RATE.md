# Exact chamber moment-generating function and large-deviation rate

For the certified Gamma/Mehler-Fock chamber density

\[
\rho_k(x)=\frac{2^{2k+1}}{(2k+1)!}\frac{x}{\sinh(\pi x)}\prod_{j=1}^k(j^2+x^2),
\]

write \(m=k+1\). The exact characteristic function already established on the Codex track is

\[
\widehat\rho_k(t)=\operatorname{sech}^{2m}(t/2).
\]

Analytic continuation \(t=-i\theta\) therefore gives the moment-generating function

\[
M_k(\theta)=\mathbb E[e^{\theta X_k}]=\sec^{2m}(\theta/2),\qquad |\theta|<\pi.
\]

The strip \(|\theta|<\pi\) is sharp: the spectral density has tail \(\rho_k(x)\asymp |x|^{2k+1}e^{-\pi|x|}\), hence exponential moments diverge at and beyond \(|\theta|=\pi\).

Because \(\rho_k=\rho_0^{*m}\), \(X_k\) is distributed as a sum of \(m\) iid \(\rho_0\)-distributed variables. For the one-step law,

\[
\Lambda(\theta)=\log M_0(\theta)=-2\log\cos(\theta/2),\qquad |\theta|<\pi,
\]

and

\[
\Lambda'(\theta)=\tan(\theta/2).
\]

Thus the Legendre transform is explicit. Solving \(x=\Lambda'(\theta)\) gives

\[
\theta_*(x)=2\arctan x,
\]

and therefore

\[
\boxed{I(x)=2x\arctan x-\log(1+x^2)}.
\]

Consequently the sample mean \(\bar X_m=m^{-1}(Y_1+\cdots+Y_m)\), with iid \(Y_j\sim\rho_0\), has Cramer rate function \(I\). Equivalently the chamber variable \(X_k\), with \(m=k+1\), obeys the scaled rate law

\[
\mathbb P(X_k/m\approx x)\asymp e^{-m I(x)}.
\]

Checks:

- \(I(0)=0\), and \(I(x)>0\) for \(x\neq0\).
- \(I'(x)=2\arctan x\).
- \(I''(x)=2/(1+x^2)>0\), so the rate is strictly convex.
- Near the origin, \(I(x)=x^2-\tfrac16x^4+O(x^6)\), consistent with \(\operatorname{Var}(\rho_0)=1/2\): the Gaussian rate begins as \(x^2\).
- For large \(|x|\), \(I(x)=\pi|x|-2\log|x|-2+o(1)\), matching the sharp exponential-moment boundary at \(|\theta|=\pi\).

This is exact Archimedean spectral/probability structure. It does not imply Weil positivity, RH, or an amplitude reconstruction theorem. It also preserves the correction that the sech power lives in transform space; the x-space convolution generator is \(\rho_0(x)=2x/\sinh(\pi x)\).
