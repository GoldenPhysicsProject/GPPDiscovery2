# Completed Suzuki positive-cone dynamics: exact prime kick capacity without eigenvalues

**GPPDiscovery2, 2026-11-16.** A fully explicit ODE/invariant-cone reinterpretation of the **published** 2023 Suzuki full screw potential, complementing the team's existing Lean gamma-FREE cone in GPPVerify/RiemannHypothesis/SuzukiKickCone.lean. This result is elementary analysis for the completed source normalization, and gives an all-prime-power *SUFFICIENT* inequality. No RH proof or all-event positivity is claimed.

## 1. The completed between-kicks dynamics

From the source-corrected notes completed_weil_box_suzuki_plastic_gamma_rung_2026_11_16.md and suzuki_exact_integer_event_parabola_2026_11_16.md, let
\[
 T(t)=\Psi_\zeta(t),\quad P(t)=T'(t),\quad k(t)=F''(t)
 =e^{t/2}-\frac{e^{-5t/2}}{1-e^{-2t}}.
\]
On any interval strictly between consecutive prime-power events q=p^m, after the first event at log2,
\[
 \boxed{T'=P,\qquad P'=k,\qquad k'>0,\quad k>0.}\tag{1}
\]
At an event t_q=log q of weight \(w_q=\Lambda(q)/\sqrt q>0\), \(T\) and \(k\) are continuous, but P has a DOWNWARD jump \(P(t_q^+)=P(t_q^-)-w_q\). The smooth curvature k is strictly increasing for every t>0 and positive for all t>=log2. This is the exact completed gamma+pole dynamics, not an axiom.

## 2. Energy/reserve and its derivative: no hidden approximation

Define the signed energy for T>=0,
\[
 E(t)=2k(t)T(t)-P(t)^2.
\]
Then on any open gap,
\[
 \boxed{E'(t)=2k'(t)T(t).}\tag{2}
\]
Proof: differentiate \(2kT-P²\), use T'=P and P'=k; cross terms cancel. Thus whenever T>=0, E is NONDECREASING between primes. At a prime-power event of weight w,
\[
 \boxed{E(t_q^+)-E(t_q^-)=2wP(t_q^-)-w^2.}\tag{3}
\]
This parallels the existing GPPVerify SuzukiKickCone.lean gamma-free identities, but k(t) is the full *completed* curvature instead of their a0=2cosh(t/2).

Energy E>=0 is too strong as a condition when P>0. The correct one-sided *forward* cone is
\[
 X(t)=\sqrt{2k(t)T(t)},\qquad
 N_+(t)=X(t)+P(t)\quad(T>0).
\]
Its relation to the scalar event parabola barrier is exact:
\[
 \boxed{N_+(t)>0
 \ \Longleftrightarrow\
 2k(t)T(t)-\max(-P(t),0)^2>0.}\tag{4}
\]
For a positive T this is immediate: if P>=0 both inequalities hold; if P<0 square and compare.

In a gap where \(T>0\) and \(N_+>0\),
\[
 N_+'=k+\frac{k'T+kP}{\sqrt{2kT}}
     =\frac{k'T}{X}+k\frac{X+P}{X}.
\]
Therefore
\[
 \boxed{N_+'(t)\ge \frac{k'(t)T(t)}{X(t)}>0.}\tag{5}
\]
The cone is FORWARD-INVARIANT between events. A positive solution T cannot reach zero from above while N_+ stays strictly positive: at its first possible zero its right/left derivative would need to be <=0, whereas the limiting N_+>0 forces derivative >0. Alternatively the monotone curvature parabola gives positivity directly.

At the event, X is continuous (T and k continuous) and P drops w, so
\[
 \boxed{N_+(t_q^+)=N_+(t_q^-)-w_q.}\tag{6}
\]

**CONSEQUENCE (exact prime-kick-capacity criterion):** Given the independently certified positive prime-free initial interval, it suffices for global completed positivity that EVERY prime-power event satisfy
\[
 \boxed{\frac{\Lambda(q)}{\sqrt q}
 <\sqrt{2k(\log q)\Psi_\zeta(\log q)}
         +\Psi_\zeta'((\log q)^-).}\tag{7}
\]
The right side is the pre-event cone reserve, computed from source arithmetic and gamma factors. It is NOT a known theorem for every q. Since \(\Psi\) is continuous at events, condition (7) is equivalent to N_+(post)>0, and to the integer-friendly event inequality (4) with post derivative P. If (7) held for every event then Suzuki 2023 Theorem 1.7 gives RH. It has been proved only for q<=10^7 in the separate finite outward-integer certificate. Do not replace (7) with mere nonnegative prime weights; off-critical shifted controls show that is insufficient.

This is a much more precise "running coupling" than selecting arbitrary multiplicative percent updates: a smooth deterministic curvature grows a reserve and actual von Mangoldt prime-power events subtract exact arithmetic kicks. The global challenge is to prove the kicks always fit, not to guess their positions or conflate finite verification with proof.

## 3. Some independent high-precision sanity checks (NOT theorem inputs)

At q=2: pre-event N_+≈0.612017720912, kick log2/sqrt2≈0.490129071734, post reserve≈0.121888649178.
At q=3: pre≈0.787565574694, kick log3/sqrt3≈0.634284100598, post≈0.153281474096.
At q=4: pre≈0.638384850203, kick log2/2≈0.346573590280, post≈0.291811259923.
The exact rational event checker verifies a strictly positive cone barrier through q=10^7; these floating figures are illustrations only.

## 4. Formalization targets

Adapt GPPVerify/RiemannHypothesis/SuzukiKickCone.lean, where gamma-free T'=P, P'=2cosh(t/2), E'=2sinh(t/2) T, and exact jump identities are already Lean-checked. Introduce *completed* k(t), prove k>0 and k'>0 after log2, then (2),(3),(5),(6), and (4). The shape and purely algebraic event jump lemmas can be Mathlib-upstreamable. Prove a general “strict one-sided cone propagates until next downward kick” lemma for continuous convex-between-kicks potentials. Then tie the finite integer B(q) certificate to the new completed cone. **Do not assert the all-event capacity bound (7).**
