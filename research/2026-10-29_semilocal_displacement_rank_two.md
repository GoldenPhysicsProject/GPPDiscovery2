# Corrected Weil matrix: rank-two displacement and certified parity assembly

2026-10-29. Golden Physics Project / Codex Discovery2. Exact structural
identity plus Arb experiments. **No global Weil positivity or RH proof.**

## Source and conventions

This uses the *corrected* completed semilocal form in Daniel Toupin's
`arithmetic_principal_series_RH_program-34.tex` and
`discovery/arb_semilocal_weil_matrix.py`, including the full Archimedean
subtraction and its tail, finite prime powers and pole. It does **not**
reuse the numerically invalidated pre-correction 129-mode margins.

Let `lambda>1`, `L=2 log(lambda)`, `k_m=2 pi m/L`, and

    w_(p,r) = (log p) / p^(r/2),   a_(p,r)=r log p,
    (p^r <= lambda^2).

For distinct integers m,n, the exact Fourier-mode autocorrelation kernel is

    q_mn(y) = [sin(k_m y) - sin(k_n y)]/[pi (n-m)],
    q_mn(0)=0.

The last zero makes the Archimedean contact and tail subtractions vanish
off diagonal. Therefore define the *one-index* arithmetic transform

    g_m = int_0^L [2 cosh(y/2) - exp(y/2)/(2 sinh y)] sin(k_m y) dy
          - sum_(p^r <= lambda^2) w_(p,r) sin(k_m a_(p,r)).         (1)

The apparent 1/y singularity in (1) is removable **after multiplication
by sin(k_m y)**; the integrand approaches `-k_m/2` at zero. The Arb
evaluator uses `sin(k_m z)/z = k_m sinc(k_m z)` and
`sinh(z)/z = sinc(i z)` to analytically enclose this endpoint.

The exact corrected matrix obeys, with diagonal entries evaluated from
the complete original expression,

    Q_mn = [g_m - g_n]/[pi (n-m)]                 (m != n).       (2)

Writing `S=diag(m)` and `u=(1,...,1)`, we obtain **exactly**

    Q S - S Q = (g u^T - u g^T)/pi.                             (3)

The displacement/commutator rank is at most two for **every** number
of modes. This is not a statement that Q itself has rank at most two.
The identity holds for the whole corrected arithmetic–Archimedean form,
not just a fitted numerical kernel.

Since `g_(-m)=-g_m` and `Q_(-m,-m)=Q_(m,m)`, the reflection `m -> -m`
commutes with Q. In the normalized parity basis

    e_0=U_0,  e_m=(U_m+U_(-m))/sqrt(2),
    o_m=(U_m-U_(-m))/sqrt(2)    (1<=m<=N),

the complete `(2N+1) x (2N+1)` matrix splits orthogonally into an
`(N+1) x (N+1)` even block and an `N x N` odd block. In terms of Q:

    E_00=Q_00, E_0m=sqrt(2) Q_0m,
    E_mn=Q_mn+Q_(m,-n),   O_mn=Q_mn-Q_(m,-n).                (4)

Both parity blocks must be positive. Equations (2)–(4) give a faster
Arb verification route: N sine transforms plus N+1 complete diagonal
entries, instead of 2N²+O(N) independently integrated entries. The
reconstruction of Q from `g` is algebraic, and parity block LDL is exact
up to outward interval rounding.

## Independent verification (python-flint/Arb 0.9.0)

`semilocal_displacement_rank_two.py` implements (1)–(4) and compares
each selected entry with a separately integrated direct entry; all
comparisons require intersecting Arb balls. That intersection is an
important regression, not itself a proof of analytic identity (which
follows above). It raises on any undecidable/negative LDL pivot.

- At `lambda=5/2`, `N=2` (5 modes), all 15 independent comparisons
  overlap and all five full LDL pivots are strictly positive.
- At `lambda=5/2`, `N=20` (41 modes), **all 861** independent direct
  entry enclosures overlap at 512-bit Arb and 1e-85 integration tolerance;
  all 41 LDL pivots strictly positive. The parity method independently
  certifies 21 even and 20 odd pivots.
- At `lambda=5/2`, `N=40` (81 modes), **193 sampled** independent
  direct entry enclosures overlap at 1024-bit Arb and 1e-180 integration
  tolerance; all 81 full LDL pivots are strictly positive. The original
  earlier 81-mode certificates using the incorrect diagonal are *not*
  being revived; this is a corrected independent recomputation.
- At `lambda=5/2`, `N=64` (129 modes), **413 sampled** independent
  entries agree with the original direct integral and the **65 even and
  64 odd parity-block LDL pivots are all rigorously positive** at
  1024-bit Arb and 1e-180 integration tolerance. This is the first
  *corrected* 129-mode certification after the original diagonal error.

The Arb context is global. Importing an unrelated helper that sets
`ctx.prec=160` *after* matrix construction silently drops precision
during LDL. This script imports its LDL helper before setting the
requested precision, and direct comparisons/LDL then run at that
explicit precision. A failed interval pivot is **undecidable**, not
evidence of a negative eigenvalue.

## The Schur gap and next move

The one-index formula is a **structure theorem for the unpaid cross
coupling**, not an inequality controlling it. The completed form still
has arbitrarily many modes and arbitrarily long support. In particular,
the signed prime sine phases in (1) persist at high m, so g_m need not
decay. The rank-two commutator does not imply a rank-two or small-norm
low/high coupling. Nonetheless it permits fast high-precision continuum
approximations and potentially analytic displacement-structured
Schur/resolvent estimates.

Use the unconditional frequency-cover coercivity from
`semilocal_frequency_band_certificate.py` for the full infinite high
sector. To conclude fixed-support positivity, a **one-sided** bound on
the low-block Schur complement (or the equivalent dual-energy residual)
is still needed. Astra's variational identity in
`GPP-bridge/work/2026-10-23_astra_schur_variational_frontier.md`
gives the right mathematical formulation even without uniform inverse
coercivity. Grok's C.15 tail audits warn against replacing such a
one-sided price by a symmetric norm or finite-block observation.

The off-diagonal formula can also be decomposed as a universal sine
integral plus a smooth O(1/m) archimedean remainder and prime phases:

    g_m = -(1/2) Si(2 pi m) + int_0^L b(y) sin(k_m y) dy
          - sum_(p^r <= lambda^2) w_(p,r) sin(k_m a_(p,r)),
    b(y) = 2 cosh(y/2) - exp(y/2)/(2 sinh y) + 1/(2 y),
    b(0) = 7/4.                                             (5)

`b` extends smoothly at zero. The smooth integral is O(1/m) by
integration by parts, while the prime oscillations do not decay.
Equation (5) isolates where arithmetic influences the cross-coupling;
its bound must still be proved in a form that pays for the exact prime
phases. A future shifted-product fake control should be passed through
the same pipeline to avoid accidental RH-by-general-kernel logic.
