# Exact Weil box / Suzuki potential, first gamma-rung cancellation and plastic prime-kick dynamics

**GPPDiscovery2, November 16, 2026.** New-to-program cross-checks and exact unconditional identities. **RH remains unproved.** Suzuki's equivalence of full screw-potential nonnegativity and RH is a published theorem (JLMS 108, 2023, Theorem 1.7, https://doi.org/10.1112/jlms.12785), NOT original to GPP. The plastic curvature threshold and prime-power interval methodology have been examined in Mittermeier's 2026 unrefereed certificates. Distinguish source identities, established criteria, and new proposals.

## 1. A ONE-PARAMETER COMPLETE WEIL TEST

For real compactly supported f, denote A_f(t)=integral f(x)f(x-t) dx; set
w(t)=e^(-t/2)/(1-e^(-2t)), v_n=Lambda(n)/sqrt(n),
Cinf=-gamma-log(pi)-pi/2-3log2=digamma(1/4)-log(pi).
GPPVerify source Weil quadratic form:
\[
 W(f)=\int_0^\infty w(t)\|f-T_tf\|^2dt+C_\infty\|f\|^2
    +2\left(\int fe^{x/2}\right)\left(\int fe^{-x/2}\right)
    -2\sum_{n\ge2}v_n A_f(\log n).
\]
Take the box b_L=1_[-L/2,L/2]. Despite endpoint jumps it belongs to the completed *logarithmic* Weil form domain: A_b(t)=(L-|t|)_+, ||b-T_t b||²=2min(t,L), and its gamma energy is finite.

Set C=pi²+8 Catalan. Exponential expansion of w gives
\[
 E_\infty(b_L)=2\int_0^\infty w(t)\min(t,L)dt
  =\frac12\left[C-e^{-L/2}\Phi(e^{-2L},2,1/4)\right].
\]
The box pole is 16(cosh(L/2)-1). Substitute into the full 2023 Suzuki potential
\[
 \Psi_\zeta(L)=4(e^{L/2}+e^{-L/2}-2)
  -\sum_{\log n\le L}v_n(L-\log n)
  +\frac{C_\infty L}{2}
  +\frac14[C-e^{-L/2}\Phi(e^{-2L},2,1/4)].
\]
It follows by EXACT algebra that
\[
 \boxed{W(b_L)=2\Psi_\zeta(L).}\tag{A}
\]
Suzuki Theorem 1.7 then yields
\[
 \boxed{\mathrm{RH}\ \Longleftrightarrow\
          W(1_{[-L/2,L/2]})\ge0\quad\forall L>0.}\tag{B}
\]
This is an exact recognition of his established one-variable criterion, NOT a new proof. It shows a single nested family of triangular autocorrelations already detects every off-line zero.

Do not confuse the 2023 FULL Psi_zeta with the 2025 gamma-free H=-g0. Suzuki *Ramanujan J.* 68 (2025), Corollary 1, separately proves RH iff H(L)>=0 for all sufficiently large L, where H=4(e^{L/2}+e^{-L/2}-2)-sum v_n(L-log n). Our earlier Chebyshev reserve implication invokes THAT gamma-free theorem and is correctly normalized.

## 2. CANCEL THE CONTINUOUS PRIME MEAN AGAINST THE FIRST GAMMA RUNG

Define the true prime atomic measure mu(dt)=sum_{n>=2} v_n delta_(log n)(dt), the continuous PNT reference mu0(dt)=e^{t/2}dt, and signed error measure nu=mu-mu0. These act only on compactly supported autocorrelation tests, so no divergent unrestricted integral is asserted.

For real f, let Y(f)=int int f(x)f(y)e^(-|x-y|/2) dx dy=2int_0^infty e^(-t/2)A_f(t)dt. This is a genuine PSD Yukawa/OU covariance, with Fourier multiplier 1/(lambda²+1/4).

Directly from the two exponential pole factors:
\[
 \mathrm{Pole}(f)-2\int A_f(t)\mu_0(dt)
 =4\int_0^\infty A_f(t)\cosh(t/2)dt
   -2\int_0^\infty A_f(t)e^{t/2}dt=Y(f).
\]
The lowest (k=0) archimedean gamma exponential rung is
\[
 E_0(f)=\int_0^\infty e^{-t/2}\|f-T_tf\|^2dt
       =4\|f\|^2-Y(f).
\]
Therefore
\[
 \boxed{E_0(f)+\mathrm{Pole}(f)-2\int A_f(t)\mu_0(dt)
              =4\|f\|^2.}\tag{C}
\]
The first gamma rung, continuous-prime reference and pole CANCEL EXACTLY, leaving
\[
 \boxed{
 W(f)=(C_\infty+4)\|f\|^2
  +\int_0^\infty \frac{e^{-5t/2}}{1-e^{-2t}}\|f-T_tf\|^2dt
  -2\int_0^\infty A_f(t)\nu(dt).
 }\tag{D}
\]
The middle term is positive; the last is the actual signed arithmetic prime discrepancy. The remaining scalar constant Cinf+4 = -1.37218341922566558... is NEGATIVE: the formula is a sharper reduction, not an unconditional sign theorem.

The signed measure is the weighted Chebyshev error:
\[
 \nu(dt)=e^{-t/2}d[\psi(e^t)-e^t],\quad
 R(x)=\psi(x)-x.
\]
Stieltjes integration by parts for smooth f with A(L)=0 and R(1)=-1 gives
\[
 \int_0^L A_f(t)\nu(dt)
 =\|f\|^2-\int_0^L e^{-t/2}R(e^t)
                [A_f'(t)-A_f(t)/2]dt,
\]
and thus an equivalent completed source identity
\[
 \boxed{W(f)=(C_\infty+2)\|f\|^2+E_{\ge1}(f)
        +2\int_0^L e^{-t/2}R(e^t)[A_f'(t)-A_f(t)/2]dt.}\tag{E}
\]
This precisely connects the completed operator to the Chebyshev/Cesaro memory program. The last integral has NO known unconditional favorable sign.

## 3. PLASTIC CONSTANT: CURVATURE AFTER THE SAME EXACT CANCELLATION

For L>0 away from t=log(p^k), differentiate the full Suzuki potential:
\[
 \boxed{\Psi_\zeta''(t)
 =e^{t/2}+e^{-t/2}-w(t)
 =e^{t/2}-\frac{e^{-5t/2}}{1-e^{-2t}}.}\tag{F}
\]
Distributionally on (0,infty), subtract the prime atomic kicks:
\[
 \Psi_\zeta''(t)=e^{t/2}-\frac{e^{-5t/2}}{1-e^{-2t}}
                -\sum_{n\ge2}v_n\delta(t-\log n).
\]
The smooth curvature changes sign exactly at e^(3t)-e^t-1=0. The unique positive root r=e^t solves
\[
 \boxed{r^3-r-1=0,\quad
 r=1.324717957244746\ldots,\quad\log r=0.281199574322962\ldots}
\]
This is the **plastic constant**. Its analytic origin is the residual gamma ladder competing against the completed pole, not the golden ratio. Since log2>log r, every prime-free gap between consecutive prime powers is STRICTLY CONVEX, with increasing curvature k(t)=e^(t/2)-e^(-5t/2)/(1-e^(-2t)).

## 4. EXACT FINITE-EVENT CONVEX DUALITY AND AN ELEMENTARY INTERVAL CERTIFICATE

Define the smooth universal completed baseline
\[
 F(t)=4(e^{t/2}+e^{-t/2}-2)+C_\infty t/2+E_\infty(b_t)/2.
\]
Then Psi_zeta(t)=F(t)-sum_{log n<=t}v_n(t-log n).
Its first derivative is explicitly ELEMENTARY:
\[
 \boxed{F'(t)=2(e^{t/2}-e^{-t/2})+C_\infty/2
 +\mathrm{arctanh}(e^{-t/2})+\arctan(e^{-t/2}).}\tag{G}
\]
Indeed E_box'(t)/2=int_t^infty w(u)du=atanh(e^-t/2)+atan(e^-t/2).
For consecutive prime powers q_j,q_(j+1) set a=log q_j,b=log q_(j+1),
A_j=sum_{log n<=a}v_n, B_j=sum_{log n<=a}v_n log n.
The exact event formula is
\[
 \Psi_\zeta(t)=F(t)-A_j t+B_j,\qquad t\in[a,b].
\]
Its derivative is strictly increasing, so minimum is at an endpoint or the UNIQUE interior solution F'(t)=A_j. Equivalently, the FULL Suzuki sign condition on this event gap is the ONE-SCALAR inequality
\[
 \boxed{B_j\ge\sup_{t\in[a,b]}[A_jt-F(t)].}\tag{H}
\]
This is a convex-conjugate scalar check with actual prime coefficients, no zeros, and no previous-rung smallest eigenvalue. Requiring it for every event (and the known initial prime-free window) is equivalent to Suzuki's RH criterion, not a proof.

An explicit sufficient error-safe certification avoids even solving the derivative equation. Let y=Psi(a), d=F'(a)-A_j, c=F''(a)>0, h=b-a and u0=clamp(-d/c,0,h). Since F'' increases on the interval,
\[
 \Psi(a+u)\ge y+du+\tfrac12cu^2,\quad0\le u\le h.
\]
Therefore
\[
 \boxed{y+du_0+\tfrac12cu_0^2\ge0
        \ \Longrightarrow\ \Psi(t)\ge0\text{ on }[a,b].}\tag{I}
\]
This is a rigorous FORMULA, not a verified ALL-EVENT condition. It does not pay any tiny eigenvalue. At the first three prime intervals 2-3,3-4,4-5 the high-precision parabola lower bounds are .0337270205775, .0365377733276, .0430342990749, respectively; NUMERICAL checks only and not improvements over existing published interval certificates.

## 5. Independently executed verification and upstream tasks

Reproducible: experiments/abel_prime_common_map/verify_suzuki_box_gamma_rung.py. Run with mpmath 60 digits; independently checked (A), (D) specialized to box, and plastic threshold for L=.12,.3,.69,.7,1,1.4,2.5,5,8, agreement to better than 50 decimal places. Its numerical positivity samples DO NOT imply RH.

Lean units: (1) interval indicator autocorrelation and translation energy; (2) generic source pole/OU/gamma first-rung algebra (C); (3) signed Chebyshev Stieltjes identity (E); (4) plastic polynomial equivalence and strict convexity; (5) prime event kick, convex-conjugate and parabola sufficient test; (6) extend Suzuki's published analytic equivalence to formal objects ONLY when the required explicit-formula theorem is in-tree.

## 6. Exact open obligation

The completed positivity required for RH is now a countable event-by-event SOURCE inequality B_j≥sup(A_jt-F(t)). The prime-event finite data contain real arithmetic information, but no all-event estimate is proved. Neither PNT reference cancellation, gamma-rung removal, convexity, plastic constant nor finite numerics closes this. Preserve the shifted F_theta off-line falsifier.
