# A 40-layer sum-of-squares completion for the prime-free Weil form

2026-10-30, Codex / GPPDiscovery2. Unconditional theorem about the
**actual corrected completed Weil semilocal quadratic form on short
supports**, extending the previous all-function result from
`0<L<=1/8`. This is not an RH proof or an all-support theorem.

## Theorem

For every `0<L<=5/32` and every complex `L²` test function supported
in `[0,L]` with finite logarithmic gamma energy, the exact v34
completed Weil form satisfies

    Q_L[f] >= B_40(L) ||f||² >= B_40(5/32) ||f||²
           > (1/200) ||f||².

The form includes the exact pole, infinite Archimedean subtraction tail
and regular gamma tilt. The finite prime-power term is exactly zero,
because `e^L < 2` on this support. The endpoint lower bound was
independently evaluated by outward Arb balls at 256-bit precision:

    B_40(5/32) = 0.00591896750052372600283741057341536... > 0.005.

This is a full infinite-dimensional *form* inequality, not Galerkin
positivity or extrapolation from 201 certified modes.

## Proof: an exact path-graph sum of squares

Define zero-extended correlation

    q_f(y) = 2 Re integral_R conj(f(x)) f(x+y) dx,
    q_f(0) = 2 ||f||².

For any integer k>=2 and any `L/k <= y <= L/(k-1)`, write each
`x in [0,L]` uniquely as `x=t+jy`, with `0<=t<y` and integer `j`.
Each fiber has at most k nonzero entries

    a_j(t)=f(t+(j-1)y),  1<=j<=k,

with zero padding past L. Then

    ||f||² = integral_0^y sum_(j=1)^k |a_j(t)|² dt,
    q_f(y) = 2 Re integral_0^y sum_(j=1)^(k-1)
                  conj(a_j(t)) a_(j+1)(t) dt.

Put `theta=pi/(k+1)` and `w_j=sin(j theta)>0`, with `w_0=w_(k+1)=0`.
The recurrence `w_(j-1)+w_(j+1)=2 cos(theta)w_j` gives **exactly**

    2 cos(theta) sum_(j=1)^k |a_j|²
       -2 Re sum_(j=1)^(k-1) conj(a_j) a_(j+1)
      =sum_(j=1)^(k-1) w_j w_(j+1)
          |a_j/w_j - a_(j+1)/w_(j+1)|² >=0.       (SOS)

This elementary identity avoids any appeal to a black-box numerical
radius theorem. Integrating over fibers proves

    q_f(y) <= 2 c_k ||f||²,  c_k=cos(pi/(k+1)),
    q_f(0)-q_f(y) >= 2(1-c_k)||f||².             (1)

For `0<y<L/K`, use merely `q_f(y)<=2||f||²`.

## Simultaneous positive kinetic and negative gamma-tilt control

Let `c_inf=log(4pi)+EulerGamma`. The exact prime-free decomposition is

    Q_L[f]=E_L[f]+P_L[f]-c_inf||f||²-A_L[f],
    E_L[f]=int_0^infty [q_f(0)-q_f(y)]/(2sinh y) dy,
    A_L[f]=int_0^L r(y)q_f(y)dy,
    r(y)=t²/[(t+1)(t²+1)], t=exp(y/2),
    P_L[f]>= [L-2sinh(L/2)] ||f||².

The entire positive gamma tail `y>=L` supplies

    E_tail[f]=log coth(L/2)||f||².

From (1) on each band `[L/k,L/(k-1)]` (2<=k<=K), we gain

    (1-c_k) log[tanh(L/(2(k-1)))/tanh(L/(2k))]

in positive kinetic energy.

Importantly, (1) also controls the *negative* gamma tilt: the AM-GM
inequalities `t+1>=2 sqrt(t)` and `t²+1>=2t` yield

    0<=r(y)<=sqrt(t)/4 = exp(y/4)/4.

Split the tilt into the same k-layers. Because `c_k>=0`, (1) implies

    A_L[f] <= T_K(L)||f||²,
    T_K(L)=2[(exp(L/(4K))-1)
          +sum_(k=2)^K c_k (exp(L/(4(k-1)))-exp(L/(4k)))].

Therefore define the explicit lower coefficient

    B_K(L) = -log tanh(L/2) + L-2sinh(L/2) - c_inf -T_K(L)
             +sum_(k=2)^K (1-c_k)
                log[tanh(L/(2(k-1)))/tanh(L/(2k))].       (2)

Every term is exact analytically; only the final elementary endpoint
comparison `B_40(5/32)>1/200` uses Arb interval arithmetic.

For fixed K, `B_K(L)` decreases with L: the gamma tail decreases,
`L-2sinh(L/2)` decreases, `T_K(L)` increases (each exponential-band
difference is increasing), and each weighted csch-band integral
decreases because `L/sinh(Lu)` decreases with L. Thus (2) at 5/32
uniformly proves positivity on **all** smaller support lengths.

The analytic+Arb K=40 reproducer is
`discovery/short_support_nilpotent_tower.py`, run alongside the earlier
`discovery/arb_short_support_weil_certificate.py` in the short-support
workflow. Do not mistake this prime-free result for global
prime–Archimedean positivity.

## What this changes, and what it does not

The old 3-layer certificate at L=1/8 had `B_3(1/8)>1/25`.
The new 40-layer construction proves all-function positivity up to
L=5/32, a **25% increase in admissible logarithmic support**. The
analytic coefficient `B_40(5/32)` is positive despite the conservative
gamma bound, and all infinitely many Fourier modes and cross-couplings
within each support are included by (SOS).

The improvement is still **prime-free** (`5/32<log2`). No induction
through the first prime atom is proved. At larger supports a noncircular
signed prime estimate and adjacent/guard-band Schur control remain
necessary. Suggested next numerical/theoretical test: add the first
p=2 logarithmic translation to (SOS) in the same fiber basis and seek
an exact compensated positive-square mechanism, checking the shifted
F_theta fake at each step.
