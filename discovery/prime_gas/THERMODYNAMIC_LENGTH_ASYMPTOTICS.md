# Prime-gas Fisher thermodynamic-length asymptotics

Status: exact asymptotic discovery record for the Codex/GPT track. No RH inference.

Let
\[
K(\beta)=\log\zeta(\beta),\qquad
g(\beta)=K''(\beta)=\operatorname{Var}_\beta(\log n),\qquad \beta>1,
\]
and define the canonical one-dimensional Fisher coordinate
\[
\tau(\beta)=\int_{\beta_0}^{\beta}\sqrt{g(b)}\,db
\]
for any fixed \(\beta_0>1\). Then \(ds^2=g(\beta)d\beta^2=d\tau^2\).

## Hot/pole end: \(\beta\to1^+\)

Put \(\varepsilon=\beta-1\). From the Stieltjes expansion
\[
\zeta(1+\varepsilon)=\frac1\varepsilon+\gamma-\gamma_1\varepsilon+O(\varepsilon^2),
\]
we get
\[
K(1+\varepsilon)
=-\log\varepsilon+\gamma\varepsilon
+\left(-\gamma_1-\frac{\gamma^2}{2}\right)\varepsilon^2
+O(\varepsilon^3),
\]
so
\[
\boxed{
 g(1+\varepsilon)
 =\frac1{\varepsilon^2}-(2\gamma_1+\gamma^2)+O(\varepsilon)
 }.
\]
Consequently
\[
\sqrt{g(1+\varepsilon)}
=\frac1\varepsilon-\frac{2\gamma_1+\gamma^2}{2}\,\varepsilon+O(\varepsilon^2),
\]
and therefore
\[
\boxed{
 \tau(\beta)=\log(\beta-1)+C_{\beta_0}+O((\beta-1)^2)
 }
\qquad(\beta\to1^+).
\]
Thus the zeta-pole end is at infinite Fisher distance: \(\tau\to-\infty\).

## Cold end: \(\beta\to\infty\)

The Dirichlet series gives
\[
\log\zeta(\beta)
=2^{-\beta}+3^{-\beta}+\frac12\,4^{-\beta}+O(5^{-\beta}),
\]
hence
\[
 g(\beta)
=(\log2)^2 2^{-\beta}+(\log3)^2 3^{-\beta}+O(4^{-\beta}).
\]
Taking the square root,
\[
\sqrt{g(\beta)}
=(\log2)2^{-\beta/2}
+\frac{(\log3)^2}{2\log2}
\left(\frac{\sqrt2}{3}\right)^\beta
+O(2^{-\beta}).
\]
In particular the cold-end Fisher distance is finite. If
\[
\tau_\infty:=\lim_{\beta\to\infty}\tau(\beta),
\]
then termwise integration yields
\[
\boxed{
\tau_\infty-\tau(\beta)
=2\,2^{-\beta/2}
+\frac{(\log3)^2}{2\log2\,\log(3/\sqrt2)}
\left(\frac{\sqrt2}{3}\right)^\beta
+O(2^{-\beta})
}.
\]
The leading constant simplifies exactly because
\[
\int_\beta^\infty (\log2)2^{-b/2}\,db=2\,2^{-\beta/2}.
\]

## Geometric consequence

The Fisher manifold \((1,\infty),g(\beta)d\beta^2\) is isometric to a half-infinite Euclidean interval
\[
(-\infty,\tau_\infty).
\]
The pole \(\beta=1\) is metrically infinitely far away, whereas the zero-temperature endpoint \(\beta=\infty\) lies at finite metric distance and admits a canonical metric completion by one endpoint.

This is a thermodynamic/information-geometric statement only. It does not imply any statement about zeta zeros.
