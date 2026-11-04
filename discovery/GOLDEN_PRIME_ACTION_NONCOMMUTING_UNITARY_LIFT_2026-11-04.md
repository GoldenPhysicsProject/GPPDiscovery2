# Natural prime dilations do not commute with the golden Möbius step

Date: 2026-11-04. Golden Physics Project / Discovery2.
Status: **exact elementary identities and reproducible numerical controls.** This is a refinement of [`GOLDEN_UNITARY_CROSSRATIO_AND_ARITHMETIC_NO_GO_2026-11-04.md`](GOLDEN_UNITARY_CROSSRATIO_AND_ARITHMETIC_NO_GO_2026-11-04.md), not a proof of RH.

## 1. Why the choice of prime coordinate matters

The earlier commutation theorem was for the deliberately simple **same-coordinate** action `V_p f(u)=f(u+log p)` with `u=log|C(x)|`. That is a valid model but **not** the usual arithmetic dilation `D_p:x->p*x` transported through the golden coordinate. These different definitions of prime action should not be conflated.

For `phi=(1+sqrt5)/2`, set `C(x)=(x-phi)/(x+phi^-1)` and `G(y)=-phi^-2*y`. Then `C(F(x))=G(C(x))` for `F(x)=1+1/x`. The inverse is

\[
x=C^{-1}(y)=\frac{\varphi+\varphi^{-1}y}{1-y}.
\]

The **actual** conjugate of the arithmetic prime dilation is the fractional linear map

\[
\boxed{P_p(y):=C\bigl(pC^{-1}(y)\bigr)
=\frac{\varphi(p-1)+(\varphi+p\varphi^{-1})y}
{p\varphi+\varphi^{-1}+(p-1)\varphi^{-1}y}.}
\]

Writing `P_p(y)=(A_p+B_p y)/(C_p+D_p y)`, its matrix determinant in this convention is

\[
B_pC_p-A_pD_p=p(\varphi+\varphi^{-1})^2=\boxed{5p},
\quad P_p'(y)=\frac{5p}{(C_p+D_py)^2}>0.
\]

Consequently `P_p` has both a zero and a pole on the negative `y` sheet for every `p>1`; its action switches the logarithmic sheets in a position-dependent way. It is **not** a constant translation `u->u+log p`.

## 2. Exact unitary prime lift with a nonconstant Jacobian

Let `H=L²(R^×,dy/|y|)`, equivalent to `L²(R,du)⊕L²(R,du)` by `y=epsilon*exp(u)`. For an almost everywhere invertible real Möbius transformation `h`, define the half-density pullback

\[
(\mathcal U_h f)(y)=\left|\frac{y h'(y)}{h(y)}\right|^{1/2}f\bigl(h(y)\bigr).
\]

This is exactly unitary on `H`, because the change of variables `z=h(y)` gives

\[
\int |\mathcal U_hf(y)|^2\frac{dy}{|y|}
=\int |f(z)|^2\frac{dz}{|z|}.
\]

The maps, and their inverses, are defined almost everywhere; zero/pole points have measure zero. Singular square-root factors are part of the unitary change of density and must not be discarded. Applying this to the prime map gives

\[
\boxed{(\mathcal P_p f)(y)
=\left(\frac{5p|y|}{|A_p+B_py|\,|C_p+D_py|}\right)^{1/2}
f\bigl(P_p(y)\bigr).}
\]

The golden step is the simpler `\mathcal U_Gf(y)=f(-phi^-2 y)`: its half-density is identically one. **Thus both golden and natural prime maps admit exact unitary lifts on the same Hilbert space.** This does *not* automatically establish physical Herglotz/OS positivity.

## 3. Noncommutation is exact, not just numerical

`G` and `P_p` fail to commute for every `p>1`. Indeed, as `y->0`,

\[
(P_p\circ G)(0)=\frac{\varphi(p-1)}{p\varphi+\varphi^{-1}},
\qquad
(G\circ P_p)(0)=-\varphi^{-2}
\frac{\varphi(p-1)}{p\varphi+\varphi^{-1}}.
\]

These limits are distinct and the maps differ on a neighboring open interval. Because the half-density representation retains the transformed argument, the corresponding unitaries do not commute either. The simpler direct identity in `x` is `F(p x)=1+1/(p x)` versus `pF(x)=p+p/x`.

This **qualifies** the earlier same-`u` commutation no-go: it remains true for its explicitly defined toy operators `V_p`, but does not apply to `\mathcal P_p`. The natural prime operators introduce a genuine nonabelian arithmetic/geometric interaction, which could be relevant to a boundary intertwiner.

## 4. Reproducible checks and what remains open

Run `experiments/golden_arithmetic_prime_nonlinear_probe.py` (Python, NumPy, SciPy):

| Prime | `B*C-A*D` | Squared norm before/after | `|P_p(G(.2))-G(P_p(.2))|` |
|---|---:|---:|---:|
| 2 | 10 | 3.467460714142 / 3.467460714142 | 0.577943 |
| 3 | 15 | 3.467460714142 / 3.467460714142 | 0.814930 |
| 5 | 25 | 3.467460714142 / 3.467460714142 | 1.025197 |
| 7 | 35 | 3.467460714142 / 3.467460714142 | 1.121699 |

Quadrature discrepancies for the squared norms are `<=1.1e-13`; the numerical results check, rather than replace, the exact measure-theoretic identity. The operator commutator on a complex-valued two-sheet test state is also nonzero for all four primes.

**Still not established:** that these prime maps are the **correct** prime operators of the completed zeta explicit formula, let alone Hecke operators, a canonical positive arithmetic-to-celestial covariance, or a discrete spectral selector. `D_p` is one projective matrix, while full prime Hecke correspondences have multiple branches and normalization constraints. The mere existence of noncommuting unitaries does not make RH true. The bare golden unitary alone still has no normalizable eigenvectors.

## 5. Best next attack

1. Work in a common physical boundary representation and derive, rather than postulate, the prime operators from the completed arithmetic distribution; test whether they are single `D_p` lifts, Hecke sums, or a different construction.
2. Test compatibility of **the normalized Weyl function** and the unit Krein feedback with these lifted actions, domains, gamma/pole counterterms and the two orientations. `GPPVerify/GoldenWeylBoundaryWord.lean` already proves the conditional algebraic word, not the arithmetic identification.
3. Check the exact Hecke multiplication relations and adjointness before claiming that the noncommuting operators quantize the continuous parameter `t`. Seek a completed positive determinant or true bound-state condition and run shifted-zeta, Davenport–Heilbronn, and theta-weight controls.
4. Formalize rational Möbius conjugation, determinant `5p`, Jacobian half-density, and noncommutation in GPPVerify; the new results in this note are not yet Lean certified.

No claim of a new zero computation or RH proof is made.
