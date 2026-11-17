# One-sided Cesàro envelopes and recurrent zeros of the completed Suzuki potential

**GPPDiscovery2 research, 2026-11-17; independent Turbo audit requested.** This note synthesizes *published* Suzuki (2023) with classical Landau Laplace theory and finite-torus recurrence. No RH proof or claim of historical priority. Full working derivation and checks are in the private GPP-bridge Codex research ledger.

## Exact completed normalization

Let xi(s)=s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)/2. For t>0 put

\[
\Psi(t)=4(e^{t/2}+e^{-t/2}-2)
-\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n)
+\frac{C_\infty t}{2}
+\sum_{j\ge0}\frac{1-e^{-(2j+1/2)t}}{(2j+1/2)^2},
\]

where \(C_\infty=\psi(1/4)-\log\pi\), with psi the **digamma** function. This is Suzuki's complete 2023 potential; in the GPPVerify Weil normalization, the interval box satisfies \(W(1_{[-t/2,t/2]})=2\Psi(t)\). Suzuki, JLMS 108 (2023), DOI 10.1112/jlms.12785, proves RH iff \(\Psi\ge0\) on all t and RH iff \(\Psi=O(1)\). His Laplace identity is

\[
\mathcal L\Psi(z)=\frac1{z^2}\frac{\xi'}{\xi}(1/2+z),\quad \Re z>1/2. \tag{1}
\]

## Theorem A: one-sided polynomial lower envelope

For **each fixed nonnegative integer** m,

\[
\boxed{\mathrm{RH}\iff \exists C,T\ge0\ \forall t\ge T:\quad
\Psi(t)\ge-C(1+t)^m.} \tag{2}
\]

Proof: Under RH Suzuki's theorem gives \(\Psi\ge0\). Conversely, choose C,T with (2) and let \(h(t)=1_{[T,\infty)}(t)(\Psi(t)+C(1+t)^m)\ge0\). Its Laplace transform, for \(\Re z>1/2\), is

\[
\mathcal Lh(z)=\frac{\xi'}{z^2\xi}(1/2+z)
+C\sum_{j=0}^m {m\choose j}\frac{j!}{z^{j+1}}
-\int_0^T e^{-zt}[\Psi(t)+C(1+t)^m]dt. \tag{3}
\]

The last term is entire; the middle term has poles only at zero; and xi(1/2+z) has no zeros for **real** z>0. If RH fails, functional equation symmetry gives a zero rho with Re rho>1/2. The first term has a noncanceling pole at \(z_0=\rho-1/2\), so the abscissa of convergence \(\sigma_c\) of the nonnegative h is at least \(\Re z_0>0\). Suzuki's unconditional growth bound makes \(\sigma_c\le1/2\) finite. Landau's theorem for Laplace transforms of eventually nonnegative functions requires a singularity at the **real** point \(\sigma_c>0\), contradicting (3), which is analytic at every positive real point. QED.

**Contrapositive:** If RH is false then for each m and every C>0, arbitrarily large t satisfy \(\Psi(t)<-C(1+t)^m\), hence

\[
\liminf_{t\to\infty}\frac{\Psi(t)}{(1+t)^m}=-\infty. \tag{4}
\]

This remains an RH-strength bound to prove, although it is weaker than requesting a pointwise nonnegative potential. This is an application of classical Landau logic, not a new RH criterion claimed historically.

## Theorem B: strictly positive finite scales return arbitrarily close to zero under RH

Suzuki's unconditional zero representation, under RH, reduces to the uniformly absolutely convergent cosine series

\[
\Psi(t)=\sum_{\gamma\ \mathrm{all}}\frac{1-\cos(\gamma t)}{\gamma^2}
=2\sum_{\gamma>0}\frac{m_\gamma(1-\cos\gamma t)}{\gamma^2},\qquad
\sum_\gamma\gamma^{-2}<\infty. \tag{5}
\]

Here gamma ranges over real ordinates of completed xi zeros and multiplicities are counted. For any epsilon, choose finitely many ordinates so the remaining uniform tail is <epsilon/2. Simultaneous recurrence for the **finite** circle-rotation family (a consequence of Dirichlet pigeonhole, with no assumption of rational independence) gives arbitrarily large t with all retained phases close to 2pi multiples, making the head <epsilon/2. By Suzuki Theorem 1.7 (strict positivity under RH),

\[
\boxed{\mathrm{RH}\implies
\Psi(t)>0\ \forall t>0,\quad\liminf_{t\to\infty}\Psi(t)=0.} \tag{6}
\]

Uniform convergence and Cesàro integration yield the positive mean

\[
\lim_{X\to\infty}\frac1X\int_0^X\Psi(t)dt
=\sum_\gamma\gamma^{-2}
=\frac{\xi''(1/2)}{\xi(1/2)}
=0.0462099862308379415778676208606780\ldots. \tag{7}
\]

The Hadamard identity in (7) pairs roots into \((1+z^2/\gamma^2)^{m_\gamma}\) for xi(1/2+z)/xi(1/2). Independent algebraic evaluation uses
\[
\frac{\xi''(1/2)}{\xi(1/2)}
=-8+\tfrac14\psi_1(1/4)
+\left[\zeta''/\zeta-(\zeta'/\zeta)^2\right](1/2).
\]
The companion mpmath experiment checks these two expressions to >50 digits. This is a **conditional** recurrence theorem and a normalization check, not numerical support for RH.

## Theorem C: one-sided integer-log Cesàro sequence criterion

For each fixed integer m>=0,

\[
\boxed{\mathrm{RH}\iff
\inf_{n\ge2}\frac{\Psi(\log n)}{(1+\log n)^m}>-\infty.} \tag{8}
\]

The source derivative between kicks is

\[
\Psi'(t)=2(e^{t/2}-e^{-t/2})+C_\infty/2
+\sum_{j\ge0}\frac{e^{-(2j+1/2)t}}{2j+1/2}
-\sum_{\log k<t}\frac{\Lambda(k)}{\sqrt{k}}. \tag{9}
\]

For t>=log2 the gamma sum is bounded, and the elementary estimate \(\sum_{k\le e^t}\Lambda(k)/\sqrt k\le2te^{t/2}\) gives \(|\Psi'(t)|\le K(1+t)e^{t/2}\) a.e. The potential is locally absolutely continuous across kicks. Thus

\[
\sup_{\log n\le t\le\log(n+1)}
|\Psi(t)-\Psi(\log n)|
\le K'\frac{1+\log(n+1)}{\sqrt n}\longrightarrow0. \tag{10}
\]

Any polynomial lower bound on integer samples extends to real t, so (2) applies. Conversely RH implies the integer inequality. Under RH, (5) is uniformly almost periodic and thus uniformly continuous; the logarithmic integer grid has mesh tending to zero. Its returns near zero persist on integer samples. Consequently, for **every** fixed m>=0,

\[
\boxed{\liminf_{n\to\infty}
\frac{\Psi(\log n)}{(1+\log n)^m}
=\begin{cases}0,&\mathrm{RH},\\-\infty,&\neg\mathrm{RH}.\end{cases}} \tag{11}
\]

## Practical arithmetic target

Write \(\Psi(t)=F(t)-A(t)\), where
\(A(t)=\sum_{k\le e^t}\Lambda(k)k^{-1/2}(t-\log k)\)
and F is Suzuki's **complete** smooth pole+gamma baseline, not the gamma-free substitute. RH follows already from a bound, at all sufficiently large integers n,
\[
A(\log n)\le F(\log n)+C(1+\log n)^m. \tag{12}
\]
No sign, uniform positive gap, or eigenvalue margin is required. This is relevant to the original arithmetic–Cesàro construction but is **not proved**; the source signed prime-error envelope remains RH-strength. In particular, (6) shows a **uniform** strictly positive lower gap for Psi at all large scales is impossible *if RH is true*. Test every proposed bound on fully completed shifted F_theta, not only positive prime weights.

**Audit targets:** (i) Laplace abscissa and real-axis analyticity in the Landau step; (ii) recurrence without rational independence; (iii) xi Hadamard multiplicity normalization; (iv) derivative/interpolation bound and gamma/pole constants. Historical credit belongs to Suzuki and Landau. No Lean/CI proof of this synthesis yet.