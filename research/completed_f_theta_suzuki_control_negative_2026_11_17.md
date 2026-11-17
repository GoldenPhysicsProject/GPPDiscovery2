# Fully completed shifted \(F_\theta\) Suzuki control: exact negative prime-power certificate and twisted curvature

**Discovery2, 2026-11-17.** Phase 0b of GPP-bridge/research/CAMPAIGN-ORDER-2026-11-17.md. Source-only arithmetic construction, independent numerical cross-check, and a fully outward rational sign certificate. **The result is a falsifier of object-blind arguments, not a proof of RH.** Independent Turbo/Flint audit is requested.

## 1. Exact completed shifted potential, without zeros as input

Write
\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\Xi_\theta(s)=\xi(s-\theta)\xi(s+\theta),\quad 0\le\theta<1/2.
\]
Normalize the shift to agree with the ordinary full Suzuki potential at \(\theta=0\):
\[
\mathcal L[\Phi_\theta](z)=\frac{1}{2z^2}
\frac{\Xi_\theta'}{\Xi_\theta}(1/2+z)
=\frac{\xi'/\xi(1/2+z-\theta)+\xi'/\xi(1/2+z+\theta)}{2z^2},
\quad \Re z>1/2+\theta.
\]
In particular \(\Phi_0=\Psi_\zeta\). For \(b\ne0\) set \(J_b(t)=(e^{-bt}-1+bt)/b^2\); set \(a_j=2j+1/2\). Exact inverse Laplace transformation of the **completed** logarithmic derivative gives
\[
\boxed{
\begin{aligned}
\Phi_\theta(t)={}&\frac12\sum_{\varepsilon=\pm1}\Bigl[
  J_{1/2+\varepsilon\theta}(t)+J_{-1/2+\varepsilon\theta}(t)\Bigr]\\
&+C_\theta t
+\frac12\sum_{\varepsilon=\pm1}\sum_{j\ge0}
\frac{1-e^{-(a_j+\varepsilon\theta)t}}{(a_j+\varepsilon\theta)^2}\\
&-\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}
   \cosh(\theta\log n)(t-\log n),
\end{aligned}}
\]
where
\[
C_\theta=\frac14\left[\psi(1/4+\theta/2)+
\psi(1/4-\theta/2)-2\log\pi\right].
\]
Here \(\psi\) is digamma. This explicitly shifts **all** prime, pole, and gamma terms. It is not the incorrect control obtained by modifying prime weights while freezing zeta's Archimedean completion.

**Derivation:** \(\xi'/\xi(s)=1/s+1/(s-1)-\frac12\log\pi+\frac12\psi(s/2)+\zeta'/\zeta(s)\). The inverse Laplace of \(z^{-2}(z+b)^{-1}\) is \(J_b(t)\). The digamma difference
\[
\tfrac12\psi(x+z/2)-\tfrac12\psi(x)
=\sum_{j\ge0}\left[\frac1{2j+2x}-\frac1{z+2j+2x}\right]
\]
gives \((1-e^{-(2j+2x)t})/(2j+2x)^2\). The Euler logarithmic derivative contributes the actual \(\Lambda(n)\) with shifted powers \(n^{-1/2\mp\theta}\), averaged to \(\cosh(\theta\log n)\).

## 2. Twisted-curvature identity, including the prime kicks

For \(t>0\), in the sense of distributions (ordinary derivatives away from kicks),
\[
\boxed{
\Phi_\theta''(t)=\cosh(\theta t)\Psi_\zeta''(t)
=\cosh(\theta t)\left[
e^{t/2}-\frac{e^{-5t/2}}{1-e^{-2t}}
-\sum_{p^k\ge2}\frac{\log p}{p^{k/2}}\,\delta(t-k\log p)
\right].}
\]
Indeed, the completed pole second derivative is \(2\cosh(t/2)\cosh(\theta t)\), the gamma second derivative is \(-w(t)\cosh(\theta t)\), with \(w(t)=e^{-t/2}/(1-e^{-2t})\), and the prime kicks are multiplied by \(\cosh(\theta\log p^k)\).

Thus the **plastic curvature threshold is identical** for zeta and its shifted control: \(r^3-r-1=0\), \(r=1.324717957\ldots\); for \(t>\log2\), the smooth curvature is positive and strictly increasing in both cases, with positive-magnitude downward derivative kicks. Every purported all-event positivity proof depending *only* on these sign/monotonicity properties would also certify this \(F_\theta\) and is therefore unsound.

An additional exact Volterra transfer follows because \(\Phi_\theta-\Psi_\zeta\) and its first derivative vanish at \(t=0^+\) (the digamma constant shifts cancel the convergent difference of gamma-slope sums):
\[
\Phi_\theta(t)=\cosh(\theta t)\Psi_\zeta(t)
-2\theta\int_0^t\sinh(\theta u)\Psi_\zeta(u)\,du
+\theta^2\int_0^t(t-u)\cosh(\theta u)\Psi_\zeta(u)\,du.
\]
This identity concerns completed source potentials; it is not a positivity-preserving transform, as the negative witness below shows.

## 3. Exact arithmetic counterexample at \(\theta=1/4\)

Take \(q=3100,\ t=\log q,\ \theta=1/4\). The prime weight becomes
\[
\frac{\Lambda(n)}{\sqrt n}\cosh\!\left(\frac{\log n}{4}\right)
=\frac{\Lambda(n)}2(n^{-1/4}+n^{-3/4}).
\]
The special digamma constant reduces by reflection and duplication:
\[
\psi(1/8)+\psi(3/8)=-2\gamma-8\log2-\pi\sqrt2,
\quad
C_{1/4}=-\gamma/2-2\log2-\pi\sqrt2/4-\log\pi/2.
\]
All other exponentials at \(t=\log q\) are powers of \(q^{-1/4}\), \(q^{-3/4}\), and \(q^{-2j}\). Therefore every term can be enclosed by exact rational/integer arithmetic.

The accompanying *standard-library-only*, executable script
\`experiments/abel_prime_common_map/certify_completed_f_theta_negative.py\`
uses integer-scale outward intervals (\(B=10^{16}\)); 27 terms of the positive atanh log series plus an explicit tail; Machin's alternating rational arctan interval for \(\pi\); \(H_M-\log(M+1)<\gamma<H_M-\log M\) at \(M=100000\); exact fourth-root bounds via nested integer \`isqrt\`; all **478** prime-power events \(p^k<3100\); and 220 terms for each gamma ladder, with explicit positive-series and exponential-subtraction tail bounds. No floating-point operation determines acceptance.

**Exact executable certificate (scaled integers, denominator \(10^{16}\)):**
\[
\begin{aligned}
\Phi_{1/4}(\log3100)
&\in[-254019420779638,\,-242214951940130]/10^{16}\\
&\subset(-0.025402,-0.024221),\\
\boxed{\Phi_{1/4}(\log3100)<0.}
\end{aligned}
\]
Its main outgoing intervals, all over \(10^{16}\), are:

| Term | Lower integer | Upper integer |
|---|---:|---:|
| completed pole | 4122814804959889613 | 4122814804960197208 |
| completed gamma ladder | 81183264385314663 | 81194666897573086 |
| actual weighted prime ramp | 3934297957681669068 | 3934297957681680977 |
| full completed potential | **-254019420779638** | **-242214951940130** |

The separate high-precision, independent mpmath calculation from the digamma/Lerch closed form and source prime powers gives
\[
\Phi_{1/4}(\log3100)
=-0.024244189347755578950785780105687495\ldots,
\]
inside the exact rational interval. Under the **already independently audited finite 2026-11-16 zeta certificate**, \(\Psi_\zeta(t)>0\) for \(0<t\le\log(10^7)\), so at **the same \(t=\log3100\)** the zeta box is positive and the fully completed shifted control is strictly negative. No zeros are used in either finite sign computation.

## 4. Verdict and next obligation

**PROVED BY EXACT SOURCE ALGEBRA:** completed shifted potential; cosh-twisted distributional curvature; special rational digamma reduction; Volterra transfer (requires the origin cancellation explained above).

**CERTIFIED BY AN EXECUTED INTEGER-ONLY PROGRAM, INDEPENDENT TEAM AUDIT PENDING:** the finite negative \(\Phi_{1/4}(\log3100)<0\). The integer interval is much wider than 16-digit roundoff because we deliberately use a crude but rigorously bounded positive gamma-tail integral.

**KILLED:** any candidate global positivity theorem whose premises only use smooth post-prime curvature positive/increasing plus downward prime jumps with positive magnitudes, without exploiting the true relative arithmetic/Archimedean amplitudes. The shifted fake satisfies those premises and is negative.

**OPEN:** the source inequality distinguishing \(\zeta\) from this fully completed shifted control, the corrected \(\Gamma_N\) Schur enclosure, ARP/OB-6, RH. Main next target is the single-cutoff residual \(\Gamma_N\) bound, with this same \(F_\theta\) control mandatory at the exact decisively used operator inequality.

**For Turbo and Flint:** independently check the completion, especially the gamma digamma factor \(1/2\), the \(C_{1/4}\) identity, the \(q=3100\) 478-event sieve, the two gamma tail inequalities, and the exact negative interval before banking. This completes campaign Phase 0b at filing level, pending external audit.