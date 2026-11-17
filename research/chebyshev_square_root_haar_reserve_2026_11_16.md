# A one-state Chebyshev square-root reserve: rigorous sufficient criterion for RH

GPPDiscovery2, 2026-11-16. **Exact analytic implication, not a proof of its hypothesis.** New finite integer certification to 10 million; no Lean compilation. Credit Suzuki's prior scalar RH criterion and prior computational work.

## 1. Proven literature and scope

Masatoshi Suzuki, *On variants of Chebyshev's conjecture*, *Ramanujan Journal* 68 (2025), article 95, DOI 10.1007/s11139-025-01238-9, Corollary 1: RH if and only if \(H(t)=-g_0(t)\ge0\) for all sufficiently large t, where
\[
H(t)=4(e^{t/2}+e^{-t/2}-2)-
\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n).
\]
The criterion and screw-function provenance are **Suzuki's prior work**. Also relevant: Pedro Caceres, *Cross-Energy of Dirichlet Partial Sums, Part 11*, Hexagon:2610.00661v2 (Nov 2026), an unrefereed preprint claiming rigorous flat-channel positivity calculations to \(x=2.15\cdot10^{29}\) and warning that exact \(\Lambda=\mu*\log\) structure is essential. Its numerical results have not been independently reviewed here. Our \(10^7\) certificate below concerns a **different, stronger pair of inequalities**, and is not the largest flat-channel verification.

## 2. Half-density memory: exact Chebyshev-to-Suzuki identity

Define
\[
\Psi(x)=\sum_{n\le x}\Lambda(n),\quad
V(x)=\sum_{n\le x}\Lambda(n)/\sqrt n,\quad
R(x)=\Psi(x)-x,
\]
and critical-half-density signed memory
\[
B(t)=\int_0^t e^{-u/2}R(e^u)\,du,\qquad t\ge0.
\]
By elementary partial summation (no RH assumption), for \(x=e^t\ge1\):
\[
\boxed{B(t)=2\Big(V(x)-\Psi(x)/\sqrt x-\sqrt x+1\Big).}\tag{1}
\]
Indeed \(\int_1^x\Psi(y)y^{-3/2}dy=2\sum_{n\le x}\Lambda(n)(n^{-1/2}-x^{-1/2})\).

The original Suzuki reserve satisfies the exact Volterra identity
\[
\boxed{
H(t)=t-4+4e^{-t/2}-B(t)-\tfrac12\int_0^t B(u)\,du.
}\tag{2}
\]
Equivalently
\[
H(t)=t-4+4e^{-t/2}
 -\int_0^t [1+(t-u)/2]e^{-u/2}R(e^u)\,du.\tag{3}
\]
These identities express the ALL-prime running reserve with a *single causal memory variable*. This half-density integration is not automatically positive. It is a different kernel from the positive gamma kernel in the Weil form.

**General sufficient lemma**: if \(B(t)\le M\) for all \(t\ge0\) and for a constant \(M<2\), then \(H(t)\ge(1-M/2)t-4-M+4e^{-t/2}\), which is eventually positive; Suzuki Corollary 1 therefore gives RH. A particularly simple adequate inequality is \(B(t)\le0\) for all t. It has NOT been proved globally.

## 3. Exact square completion: isolate one arithmetic reserve

For \(x\ge2\), put \(P=\Psi(x)>0\), \(V=V(x)\), \(z=\sqrt x\), and define
\[
\mathcal G(x)=2\sqrt{\Psi(x)}-1-V(x).
\]
The elementary identity \(z+P/z-2\sqrt P=(z-\sqrt P)^2/z\) transforms (1) into
\[
\boxed{
B(\log x)=-2\mathcal G(x)
-\frac{2}{\sqrt x}\big(\sqrt x-\sqrt{\Psi(x)}\big)^2.
}\tag{4}
\]
The second term is an **exact nonpositive square**, not an estimate. The only remaining possibly positive contribution to B is a scalar arithmetic reserve \(-2\mathcal G\).

Thus the following is a rigorous **RH-sufficient but OPEN arithmetic statement**:
\[
\boxed{
\left(1+\sum_{n\le q}\frac{\Lambda(n)}{\sqrt n}\right)^2
\le 4\sum_{n\le q}\Lambda(n)
\quad\text{for every prime power }q=p^k\ge2.
}\tag{5}
\]
Because \(V,\Psi\) are constant between prime-power thresholds, (5) implies \(\mathcal G(x)\ge0\) for all \(x\ge2\). By (4), \(B(t)\le0\) for \(t\ge\log2\). When \(0<t<\log2\), \(V=\Psi=0\) and \(B(t)=-2(e^{t/2}-1)<0\). Thus \(B(t)\le0\) for every t>0. Identity (2) gives \(H(t)>0\) for all t≥4. **Suzuki's theorem then implies RH.**

The implication is established. The premise (5) is **NOT** established for all prime powers, and no claim of an original RH proof is made. A brief literature search did not turn up this exact inequality, but no priority/novelty claim follows from that alone.

## 4. Universal one-state event update

At a prime-power threshold \(q=p^k\), let \(a=\log p\), \(P=\Psi(q^-)\), \(V=V(q^-)\). Then
\[
\mathcal G(q)-\mathcal G(q^-)
 =2(\sqrt{P+a}-\sqrt P)-a/\sqrt q
 =a\left(\frac{2}{\sqrt{P+a}+\sqrt P}-\frac1{\sqrt q}\right).
\tag{6}
\]
Between events \(\mathcal G\) is constant. Its positive or negative kick is controlled by the difference between **arithmetic scale** \(\sqrt{\Psi}\) and **physical coordinate** \(\sqrt q\). This is the new running-coupling target, not a postulated monotonicity claim. In fact \(\Psi(q)\le q\) at every q cannot be assumed, because the Chebyshev error oscillates.

## 5. Independently executed exact-integer finite certificate

\`experiments/abel_prime_common_map/certify_suzuki_sqrt_reserve.py\` checks simultaneously, at **every** prime-power event \(q\le10^7\),
\[
4\Psi(q)>(1+V(q))^2,\qquad
D(\log q^+)=2(\sqrt q-1/\sqrt q)-V(q)>0.
\tag{7}
\]
The finite run checked **665,134 distinct prime-power events**, including **664,579 primes**, all passing. Every log p is enclosed by the positive rational atanh expansion after dyadic reduction:
\[
\log(m)=2\sum_{j=0}^{15}\frac{z^{2j+1}}{2j+1}+R_{16},
\quad z=(m-1)/(m+1)\le1/3,\quad
0\le R_{16}<\frac{9}{4}\frac{3^{-33}}{33}<10^{-12}.
\]
Outward-rounded integers at scale \(10^{12}\) enclose all log series, and \( \lfloor 10^{12}\sqrt q\rfloor=\mathrm{isqrt}(10^{24}q)\) gives exact sqrt bounds. At each event, the program uses *lower* \(\Psi\), *upper* V, *lower* sqrt, *upper* inverse sqrt; all acceptance comparisons are exact integers. No floating point, zeta zeros, PNT or RH assumption enters. Re-execution on Nov 16 took approximately five seconds.

The smallest certified D lower bound was
\[
D(\log q^+)>\frac{924084490627}{10^{12}},\quad\text{minimum at }q=2.
\]
The smallest certified rational lower bound of \(4\Psi(q)-(1+V(q))^2\) was
\[
\frac{552104071748384642654975}{10^{24}}>0,\quad\text{minimum at }q=2.
\]
Because D increases strictly between prime powers, this proves \(D(t)>0\) for \(0<t\le\log10^7\). Because V and Psi are constant between events, this separately proves \(\mathcal G(x)>0\) for \(2\le x\le10^7\), whence \(B(t)<0\) for \(0<t\le\log10^7\). These are **finite mathematical assertions certified by reproducible integer computations**, not an infinite theorem or a Lean build.

## 6. Strong off-line control, normalized to the original zeta weights

For \(0<\theta<1/2\), consider the positive *comparison weights*
\(a_\theta(n)=\Lambda(n)\cosh(\theta\log n)\). They equal the average of the prime-side weights from \(\xi(s-\theta)\xi(s+\theta)\), normalized to \(a_0(n)=\Lambda(n)\). They are a deformation of the prime coefficients, not the entire explicit formula of an \(L\)-function.

Let \(\Psi_\theta(x)=\sum_{n\le x}a_\theta(n)\) and \(V_\theta(x)=\sum_{n\le x}a_\theta(n)/\sqrt n\). By the **proved prime number theorem** and partial summation,
\[
\Psi_\theta(x)\sim\frac{x^{1+\theta}}{2(1+\theta)},\qquad
V_\theta(x)\sim\frac{x^{1/2+\theta}}{2(1/2+\theta)}.
\]
Hence
\[
\boxed{
\frac{V_\theta(x)^2}{4\Psi_\theta(x)}
\sim\frac{1+\theta}{8(1/2+\theta)^2}x^\theta
\longrightarrow\infty.
}\tag{8}
\]
Therefore the global inequality (5) **eventually fails** for every positive theta, despite each new prime's local gamma-energy coupling still tending to zero like \(O(p^{\theta-1/2})\). This is a nontrivial global negative control that the local asymptotic-freedom law could not pass. The unaveraged \(\xi(s-\theta)\xi(s+\theta)\) product doubles the weights even at theta=0; its failure is less diagnostic.

## 7. Open mechanism and audit

The remaining true RH-strength question is whether exact von Mangoldt coefficients obey \(\mathcal G(q)\ge0\) for **ALL** prime powers, not merely the verified range. A valid proof must carry Euler-product/Möbius structure \(\Lambda=\mu*\log\) and genuine correlations; mere PNT, prime sparsity, finite computation or local weak gamma couplings cannot do it.

Lean targets: generic square completion (4), Chebyshev summation-by-parts (1), Volterra rule (2), one-state event formula (6), finite prime-power event sufficiency, and conditional implication (5)→Suzuki's H-sign. Port the integer script as a checker or compact bounded proof; no replacement of infinity by finite calculation. The separate source exact Weil positivity/ARP and a full proof of RH remain OPEN.
