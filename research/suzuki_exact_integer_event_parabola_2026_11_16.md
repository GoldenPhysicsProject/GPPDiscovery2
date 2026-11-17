# Exact-integer Suzuki curvature barriers through ten million

**16 November 2026. Status: unconditional finite-range computer-assisted certificate; NOT RH.** Published mathematics: Masatoshi Suzuki, JLMS 108 (2023), Theorem 1.7, identifies RH with nonnegativity of the FULL zeta screw potential at every scale. This work verifies a **finite continuum of scales** using one rigorous outward-integer inequality per prime-power event. Larger finite cutoffs (to 10^10) appear in Mittermeier's separate 2026 certificates; no priority claim is made for the range.

See research/completed_weil_box_suzuki_plastic_gamma_rung_2026_11_16.md for the exact matching of Suzuki's full potential to half the completed Weil form on the interval indicator. That source normalization is essential.

## 1. One finite event tests the entire interval to the next event

Let v_n=Lambda(n)/sqrt(n) and define
\[
 \Psi_\zeta(t)=F(t)-\sum_{\log n\le t}v_n(t-\log n),
\]
where
\[
 F(t)=4(e^{t/2}+e^{-t/2}-2)+C_\infty t/2+C/4
      -4\sum_{j\ge0}e^{-(2j+1/2)t}/(4j+1)^2,
\]
\(C_\infty=-\gamma-\log\pi-\pi/2-3\log2\) and \(C=\pi^2+8G\), G Catalan's constant. At a prime-power event q=p^k, set a=log q and
\[
 A_q=\sum_{n\le q}v_n,\quad B_q=\sum_{n\le q}v_n\log n,\quad
 Y_q=F(a)-A_qa+B_q,\quad D_q=F'(a)-A_q,\quad K_q=F''(a).
\]
The derivative is the right-hand derivative after the event. The curvature \(K_q>0\), and F'' increases throughout every prime-free gap after log2. Taylor's integral inequality gives
\[
 \Psi_\zeta(a+u)\ge Y_q+D_qu+\tfrac12K_qu^2
 \quad \text{from }a\text{ up to the next event}.
\]
Hence
\[
 \boxed{\mathcal B(q)=2K_qY_q-\max(-D_q,0)^2>0}
\]
is sufficient for strict positivity on the ENTIRE next prime-free gap. This uses only actual prime event cumulants and the completed gamma/pole data, and makes no claim for all events.

At integer q>=2 the universal terms evaluate by rapidly convergent POSITIVE rational series:
\[
 F(\log q)=4(\sqrt q+q^{-1/2}-2)+(C_\infty/2)\log q
   +C/4-4q^{-1/2}\sum_{j\ge0}q^{-2j}/(4j+1)^2,
\]
\[
 F'(\log q)=2(\sqrt q-q^{-1/2})+C_\infty/2
   +2q^{-1/2}\sum_{j\ge0}q^{-2j}/(4j+1),
\]
\[
 F''(\log q)=\sqrt q(1-1/[q(q^2-1)]).
\]
Each geometric tail from j>=16 is bounded by
\(q^{-32}/((4\cdot16+1)^r(1-q^{-2}))\), for r=1 or 2.

## 2. Certifying the first prime-free interval

The first event is log2. Put t0=log(3/2), between the curvature transition (log plastic constant) and log2. The potential equals F(t) on (0,log2). The exact rational checkpoint in certify_suzuki_initial_interval.py gives, at scale 10^12:
\[
 40840781026 < 10^{12}F(t_0)<40843330237,
\]
\[
 -38662616299 < 10^{12}F'(t_0)<-38657566156,
\]
\[
 571547606649 < 10^{12}F''(t_0)<571547606650,
\]
with appropriate non-strict endpoint enclosure conventions. The decisive integer inequality is
\[
 2\,F''_{\rm lo}F_{\rm lo}-(F'_{\rm lo})^2
 =45190103399088680826347 >0
 \quad\text{at scale }10^{24}.
\]
Since F'' increases and crosses zero exactly once, F'(0+)=+infinity, F'(t0)<0, F(0)=0 and F(t0)>0 imply F(t)>0 for every 0<t<=t0. For t0<=t<=log2, F''>=F''(t0)>0 and the last integer inequality proves the global tangent parabola stays positive. Thus the initial interval is certified WITHOUT assuming any other finite Suzuki result.

## 3. Exact numerical certificate through q=10^7, rerun independently

Repository executable:
experiments/abel_prime_common_map/certify_suzuki_event_parabola.py

It depends on the exact-integer logarithm/sieve helpers in certify_global_weighted_chebyshev_superadditivity.py, in the SAME directory. The initial certificate is a companion executable:
experiments/abel_prime_common_map/certify_suzuki_initial_interval.py

From that directory run:

    python certify_suzuki_initial_interval.py
    python certify_suzuki_event_parabola.py 10000000

All ACCEPTANCE DECISIONS use Python integers and exact Fraction arithmetic, no floating-point or imported prime table. The 10^12-scaled rational enclosures include: pi from Machin's 16atan(1/5)-4atan(1/239) with alternating-series remainders; Euler gamma from H_100000-log(100001) <= gamma <= H_100000-log(100000); logpi and log2 from positive atanh series; Catalan from an alternating 1000-term series; and prime-powers using exact sieve, integer square-root and dyadically reduced 16-term atanh logs.

Every event computes outward lower bounds Y_lo,D_lo,K_lo and checks the EXACT integer comparison
\[
 2K_{\rm lo}Y_{\rm lo}-\max(-D_{\rm lo},0)^2>0.
\]
This bounds the true \(\mathcal B(q)\) below, because Y,K positive and D at least D_lo. The verified run reported:

    Cinf: -5372188470003/10^12 <= Cinf <= -5372178369744/10^12
    C=pi²+8Catalan:
           17197328150556/10^12 <= C <= 17197330156531/10^12
    ALL 665134 prime-power events q<=10000000 CERTIFIED
    minimum unnormalized polynomial numerator:
           79489292921688034796564 / 10^24 at q=2
    complete initial prime-free interval separately CERTIFIED

Combining these observations with the analytic convexity argument yields:
\[
 \boxed{\Psi_\zeta(t)>0\quad\text{for EVERY real }0<t\le\log(10^7).}
\]
The claimed interval is continuous, not a point grid. The last verified event's parabola also continues to the next prime-power event beyond 10^7, but no assertion about that next event's derivative is needed for the bounded result.

The minimum numerator in the log is NOT the minimum height of the potential. An independent floating scout of the actual parabolic potential margin saw ~0.02752 at q=3089; that floating observation is NOT part of the rigorous certificate.

## 4. Interpretations and exact open obligation

This is a finite-range certificate for the FULL completed Suzuki potential, including prime, gamma and pole terms, equivalent to the completed Weil form on the nested BOX test family. It is not full positivity on arbitrary Weil test functions at a fixed support width, and it is not positivity at arbitrarily large scales. Mittermeier's earlier 2026 certificates reach 10^10, exceeding this new independent finite range.

The tempting all-event sufficient conjecture \(\mathcal B(q)>0\) at every prime power would imply RH via Suzuki's published theorem. It is **not proved** and is stronger than merely requiring Suzuki's potential nonnegative on each interval. The project should check this scalar sufficient criterion against legitimate completed shifted F_theta controls before treating it as a plausible number-theoretic mechanism.

Lean/mathlib targets: box autocorrelation and gamma energy, strict monotonicity of smooth curvature, prime-event parabolic barrier, explicit finite rational gamma and log enclosures. No Lean compilation has been attempted and no world-first result is claimed.
