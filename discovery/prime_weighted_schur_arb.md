# Weighted Hardy-Schur completion through L=39/25 with three genuine prime-power atoms

2026-10-31, Codex / GPPDiscovery2. **Unconditional all-functions theorem**
for the corrected actual signed arithmetic source and completed positive
Archimedean kinetic. This strengthens the unweighted L=38/25 endpoint
certificate. The remaining completed contact/pole/regular-gamma terms
are not yet dominated. **This is not RH or global completed Weil positivity.**

## Theorem

For all `0<L<=39/25=1.56` and all admissible complex functions
supported in `[0,L]`, with the exact form terms

    q_f(a)=2 Re integral_R conj(f(x)) f(x+a)dx,
    E_L[f]=integral_0^infty (q_f(0)-q_f(y))/(2sinh y)dy,
    S_L[f]=sum_(p^r<=exp(L)) (log p)/sqrt(p^r) q_f(rlog p),

we have

    E_L[f]-S_L[f] >= (1/250)||f||².                  (T)

This includes the complete prime-power source `{2,3,4}` at the rational
endpoint. Neither a finite Fourier cutoff nor RH is assumed.

## Step 1: exact completed Hardy potential

Set `H(t)=log coth(t/2)>0`, `V_L(x)=[H(x)+H(L-x)]/2`. By zero
extension, the translated squared difference `||f(.-y)-f||²`
contains both disjoint exterior contributions

    integral_0^min(y,L)|f(x)|² dx
     + integral_max(0,L-y)^L|f(x)|² dx.

Integrating against `dy/(2sinh y)` and using
`int_t^infty csch(y)dy=H(t)` yields

    E_L[f] >= integral_0^L V_L(x)|f(x)|² dx.         (H)

Furthermore `H''(t)>0`, and Jensen gives

    V_L(x) >= H(L/2) for every 0<x<L.              (J)

## Step 2: an exact weighted prime-graph square

For any positive weight profile `h(x)` and each active prime-power
shift `a=log(p^r)` of weight `w=(log p)/sqrt(p^r)`, the exact identity

    w*h(x)*h(x+a)*|f(x)/h(x)-f(x+a)/h(x+a)|²
       = w*[h(x+a)/h(x)*|f(x)|²
               +h(x)/h(x+a)*|f(x+a)|²
               -2 Re(conj(f(x))*f(x+a))] >=0

holds pointwise for `0<=x<=L-a`. Thus the signed prime source obeys

    S_L[f] <= integral_0^L d_(L,h)(x)|f(x)|² dx,

where

    d_(L,h)(x) = sum_(p^r<exp L) w_(p^r)*[
        1_(x+a<L) h(x+a)/h(x)
          +1_(x>a) h(x-a)/h(x)].

Together with (H), `E-S >= integral(V-d_h)|f|²`. Choose

    h_L(x)=V_L(x)^(-1/10),  alpha=1/10.

Then the **dimensionless Schur ratio** is

    R_L(x)=d_(L,h)(x)/V_L(x)
       =sum_(p^r<exp L) w_(p^r)*[
          1_(x+a<L)/(V_L(x)^(9/10)*V_L(x+a)^(1/10))
         +1_(x>a)  /(V_L(x)^(9/10)*V_L(x-a)^(1/10))].

Any proof `R_L(x)<=199/200` uniformly gives

    E_L-S_L >= (1/200) H(L/2)||f||².                (S)

The positive h-profile is only an **exact SOS multiplier**, not an
extra restriction on physical test functions.

## Step 3: rigorous continuum Arb certificate

The checked Python/FLINT Arb implementation is
`discovery/prime_weighted_schur_arb.py` on GPPDiscovery2.

At `L0=39/25`, there are exactly three prime-power atoms:

    n=2, shift log2, weight log2/sqrt2,
    n=3, shift log3, weight log3/sqrt3,
    n=4, shift log4, weight log2/2.

The code first proves outward Arb containments for **rational**
lower/upper brackets of log2, log3 and log4. Then it recursively
partitions the entire `x in [0,L0]` into rational closed intervals.
For each cell it proves a uniform upper bound on R, not a midpoint
or dense-grid evaluation:

1. On a rational cell `[u,v]`, use H decreasing to certify
   `V_L(x)>=[H(v)+H(L-u)]/2` for **all** x in the cell.
2. For each translated branch `x±log n`, use rigorous rational
   brackets for the shifted subinterval. Intersect with `[0,L]`,
   and obtain a lower bound for its V by the same monotone formula.
3. Sum **upper Arb enclosures** of
   `w/[V_lower(x)^(9/10)*V_lower(x±a)^(1/10)]` for every possibly
   active shift. Omitted terms are certified impossible on the cell.
4. If the upper Arb enclosure is not strictly below `199/200`, bisect
   the rational interval and repeat. Every cell that remains in the
   final exhaustive partition passes, with no unverified gaps.

At 192-bit precision, the **entire continuum** passes after only 44
adaptive rational cells, maximum dyadic depth 10. The largest
certified cell upper enclosure is

    R_L0(x) < 0.99440190275228017331704204877... < 199/200.

Jensen's minimum is

    H(L0/2)=0.99058272282923890504193252414...,

so the final scalar Arb comparison is

    (1-199/200)*H(L0/2)
       =0.00495291361414619452520966262... > 1/250.

No arbitrary floating tolerance is used to close the proof.

## Step 4: uniformity in all shorter supports

Write `x=tL` for fixed `t in (0,1)`. The potential

    V_L(tL)=[H(tL)+H((1-t)L)]/2

decreases as L grows. On any active shifted edge, both arguments
in `V_L(tL+a)=[H(tL+a)+H((1-t)L-a)]/2` increase with L;
likewise for `V_L(tL-a)`. Thus each denominator in `R_L(tL)`
decreases as L grows and each nonnegative edge coefficient increases.
The set of active prime edges only increases with L. Therefore

    R_L(tL) <= R_L0(tL0) < 199/200 for all 0<L<=L0.

Since H(L/2) decreases with L, the endpoint bound (S) then holds
uniformly with `H(L0/2)`. This proves (T) for all 0<L<=39/25.

## Scope and next mathematics

For corrected completed Weil quadratic form

    Q_L[f]=(E_L[f]-S_L[f]) + P_L[f]
           -(log(4pi)+EulerGamma)||f||² - A_L[f],

(T) is a **positive first-three-prime arithmetic/kinetic supplier**;
it alone is not enough to cover the contact subtraction and the
negative pole/tilt channel. Previous all-function completed Q_L>0
remains established only through L<=5/32, while finite 201-mode
positivity at L=2log(5/2) is independently Arb-certified but not
a uniform-in-N or all-support proof. The bridge now needs an exact
moment-aware coercivity estimate on the rest of this operator and
control beyond p=5 activation.
