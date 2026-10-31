# Exact no-double-spending first-prime Hardy boundary tax theorem

**2026-10-31, Codex / Discovery2, after latest GPP-bridge PR11.** Follows the independent 192-bit full-form resource ledger in PR11 comment 6547827691. This is an unconditional ALL-TEST FUNCTION inequality for the **actual completed first-prime source**, not all-test completed Weil positivity and not RH. Unlike naive E−S and potential bounds added independently, it spends the exterior Hardy potential V only ONCE.

## A. Exact source square, true completed form

Let a=log2, w=a/sqrt2, and a<L<3a/2. Set epsilon=L-a, first and last strips A=[0,epsilon], B=[a,L], where no other prime powers are active. For any complex f supported [0,L], let f_A(x)=f(x), f_B(x)=f(x+a) on 0<x<epsilon, M=||f_A||²+||f_B||², D=||f_A-f_B||². Then, EXACTLY,
\[
-S_2[f]=wD-wM,
\quad S_2[f]=w\,2\Re\int_0^\epsilon \bar f_A(x)f_B(x)dx.
\]
There is no approximation, assumed positivity, contact insertion, or cancellation with a separately allocated kinetic energy.

The corrected completed v34 Weil form has the independent exact representation
\[
Q_L[f]=\int_0^L\bigl(V_L(x)-\Gamma_L(x)-c_\infty-w\mathbf1_{A\cup B}(x)\bigr)|f(x)|²dx
+J_\gamma[f]+wD
+2|C_f|²-2|T_f|²,
\]
where H(s)=log coth(s/2), V_L(x)=[H(x)+H(L-x)]/2 is the true gamma exterior Hardy potential, Gamma_L is the exact regular gamma tilt, c_infty=log(4pi)+EulerGamma, J_gamma the true positive interior gamma jump, C=integral f cosh((x-L/2)/2)dx, T=integral f sinh((x-L/2)/2)dx. V is used exactly once; the true prime gradient wD is retained, NOT discarded.

## B. New ALL-FUNCTION Hardy tax-paid supplier to L=31/40

**Theorem.** For every support 0<L≤31/40=0.775, with a< L when p2 is active, set M as above (and M=0 when L≤a). For every complex f,

\[
\boxed{\int_0^L\!\bigl(V_L(x)-w\mathbf1_{A\cup B}(x)\bigr)|f(x)|²dx
\ge H(L/2)\|f\|²+\frac3{1000}M.}
\]

**Proof:** H'(s)=−1/sinh s, H''(s)=cosh s/sinh²s>0 for s>0. Thus V_L is symmetric around L/2, convex and decreasing on (0,L/2). The strip A=[0,epsilon] lies on the left half because L<2a, and B is its mirror. Hence on either strip V_L(x)≥V_L(epsilon)=[H(epsilon)+H(a)]/2, whereas on the complement V_L≥H(L/2). Put

\[
d(L)=\tfrac12[H(L-a)+H(a)]-H(L/2)-w.
\]
Its derivative is \(d'(L)=\tfrac12[H'(L-a)-H'(L/2)]<0\) for a<L<2a because L-a<L/2 and H' strictly increases. Therefore d(L)≥d(31/40) for all a<L≤31/40. Outward 256-bit FLINT/Arb at exact rational L0=31/40 certifies

\[
\boxed{d(31/40)=0.0038548080308340919495\ldots>3/1000.}
\]

Integrate the pointwise strip and complement inequalities against |f|²; the claim follows. For L≤a no prime source exists and V≥H(L/2) from convexity, with M=0. This is all L² tests, not a finite-dimensional matrix result.

## C. Exact prime-inclusive completed Q resource lower bound

The theorem and the exact source square give, for every admissible f and every 0<L≤31/40,
\[
\boxed{
Q_L[f]\ge
\bigl(H(L/2)-c_\infty\bigr)\|f\|²
-\int_0^L\Gamma_L(x)|f(x)|²dx
+J_\gamma[f]+wD+\frac3{1000}M
+2|C_f|²-2|T_f|².
}
\]
If desired use the independent gamma bound Gamma_L(x)≤exp(L/4)-1 to replace the integral. The term J_gamma is the actual full interior gamma kinetic, and **wD is an actual positive prime gradient**. We make NO claim the entire RHS is nonnegative; the constant c_infty and negative odd sinh pole still require signed moment-aware Schur control. The point here is that the TRUE negative prime boundary TAX has been fully paid from the exterior V resource, with a strictly positive spare endpoint contribution and no double spending.

The theorem is stronger in the first-prime sector than paying |S_2| against E by a logarithmic relative-energy bound, because it preserves wD and a positive M while retaining J_gamma.

## D. Scope, controls, receipt

At L=3/4 the earlier exact Legendre f=e1-(2/5)e3 has Q0<0 and actual Q>0, and local first-prime repair in the global-odd/local-even channel. The new inequality is consistent with, but does not prove positive completed Q on all tests even at L=3/4. False shifted F_theta two-species sources have different weights, so their corresponding boundary tax floor must be evaluated separately; there is no RH selector here. At L=31/40 still only p2 is active since 31/40<log3.

Reproducer: GPPDiscovery2 discovery/arb_first_prime_hardy_tax_paid_31_40.py, 256-bit outward Arb certificate of the strict d endpoint plus exact algebraic formulas. Follow exact analytic proof for the all-f assertion; no finite grid is substituted for monotonicity.

**Next meaningful global task:** use this tax-paid Hardy floor plus actual \(J_\gamma+wD\) to obtain a fully positive **one-sided mirror-even/mirror-odd Schur** at some L>log2, with all infinite modes; avoid paying the same exterior V twice. Then seek support-uniform arithmetic PNT discrepancy control and test against F_theta/DH. RH remains open.
