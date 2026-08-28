# AFT coercivity refinement and box-factor target — 2026-08-28

## Correction: a uniform odd spectral gap is stronger than necessary

The previous AFT note isolated the sufficient estimate

\[
\langle \psi,\Delta_-\psi\rangle\ge c\|\psi\|^2,\qquad c>0,
\]

which certainly kills odd harmonic vectors.  But on the causal half-line the
natural Dirichlet Laplacian has spectrum touching zero, so a uniform positive
lower bound is not structurally forced and may be too strong for the completed
AFT complex.

The actual no-ghost requirement is only

\[
\ker \Delta_-=\{0\},
\]

or equivalently vanishing of the reduced odd harmonic/cohomology sector.  A
coercive graph estimate is one route to injectivity, but the proof must not
silently assume a global spectral gap unless such a gap is genuinely derived.

This is consistent with the older principal-series analysis: finite sections
show severe conditioning and no evidence for a uniform lower bound on the
smallest eigenvalue.  Hence the sharp target is injectivity/no escaped trace,
not necessarily a positive gap.

## Exact scalar normal form

The zero-independent finite phase is

\[
q_L(k)=A_\infty(1)k
+\int_0^L w_\infty(a)
\left(\frac{\sin(ka)}a-e^{-a}k\right)\,da
-\sum_{m\log p\le L}\frac{p^{-m/2}}m\sin(km\log p),
\]

with

\[
q_L'(k)=A_\infty(1)
+\int_0^L w_\infty(a)(\cos ka-e^{-a})\,da
-\sum_{m\log p\le L}(\log p)p^{-m/2}\cos(km\log p).
\]

At zero frequency,

\[
q_L'(0)
=2e^{L/2}-P_{1/2}(e^L)+c_\infty
+\frac23e^{-3L/2}-\arctan(\sinh(L/2)).
\]

Therefore a direct polynomial bound on `q_L'(0)` is not an easier arithmetic
subproblem: it is already equivalent to RH through the weighted prime-counting
estimate

\[
P_{1/2}(x)=2\sqrt x+O(\log^M x).
\]

So the AFT route must explain this cancellation structurally, not re-prove the
same bound by elementary estimation.

## Better target: factor the box functional

The Fejer bridge identifies

\[
\Psi(L)=\frac L2(Q_{L,0})_{00}
=\langle\mathcal W,(L-a)_+\rangle,
\]

and Suzuki's criterion is

\[
RH\iff \Psi(L)\ge0\quad\forall L\ge0.
\]

The triangle kernel has the kinematic Hilbert-space factorization

\[
(L-a)_+
=\langle \mathbf 1_{[0,L]},V_a\mathbf 1_{[0,L]}\rangle
\qquad(a\ge0),
\]

so the remaining arithmetic theorem can be stated as follows:

> Construct a zero-independent AFT map `J_L` from the interval vector
> `1_[0,L]` into the physical quotient such that
> \[
> \langle\mathcal W,(L-a)_+\rangle=\|J_L\mathbf1_{[0,L]}\|^2.
> \]

This is strictly sharper than taking a Hilbert-Schmidt norm of the coupled
commutator: the desired functional is linear in the explicit-formula
distribution, whereas a naive operator norm is quadratic in its coefficients.
The factorization therefore has to arise from a quotient/cohomology/relative
trace construction.

## Current AFT wall

The surviving precise alternatives are:

1. prove `ker Delta_- = {0}` in the global Tate boundary complex without
   assuming an unjustified uniform gap; or
2. construct the physical box map `J_L` giving
   `Psi(L)=||J_L 1_[0,L]||^2`; or
3. prove global trace conservation for the finite coupled Dirichlet
   prime--Archimedean operators, with no escaped trace at the boundary.

These are three presentations of the same global no-ghost phenomenon.  No RH
proof is claimed.