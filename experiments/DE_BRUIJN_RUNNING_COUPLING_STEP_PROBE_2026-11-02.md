# A fixed-step running transform for zeta zeros: the de Bruijn--Newman flow

Date: 2026-11-02  
Status: known exact theorem/flow, newly reproduced low-zero numerical step experiment; **no RH proof**

## The precise version of the running-coupling intuition

There is an established one-parameter deformation of the completed zeta function in which **repeating the same small transform really moves its zeros**. It is the de Bruijn--Newman family, not an ad hoc prediction rule.

Write `z=2t`, and let

\[
H_0(z)=\tfrac18\xi\bigl(\tfrac12+iz/2\bigr),
\]

\[
H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)du,
\quad
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
\]

This is exactly the normalization of [Rodgers--Tao, *The de Bruijn--Newman constant is non-negative*](https://arxiv.org/abs/1801.05914). The same heat deformation and its important **non-reversibility** are discussed in the user's existing `arithmetic_principal_series_RH_program-34.tex`, section "Why Wick rotation does not reverse the de Bruijn flow"; this is a targeted numerical connection to that existing work, **not** a newly invented RH equivalence.

Define the step operator by its Fourier multiplier,

\[
T_\delta: \widehat f(u)\longmapsto e^{\delta u^2}\widehat f(u).
\]

Then

\[
T_\delta^{\,k}H_0=H_{k\delta},\qquad
\partial_\lambda H_\lambda=-\partial_z^2H_\lambda.
\]

So **every iteration is the identical transformation**. The increment is additive in `lambda`; its multiplier changes each Fourier mode by the *mode-dependent* percentage `e^(delta*u^2)-1`. A uniform overall percentage would only multiply the entire function and move **no zeros at all**.

At a simple zero `z_j(lambda)`, differentiation of `H_lambda(z_j(lambda))=0` yields the **exact local zero-motion rule**

\[
\boxed{\frac{dz_j}{d\lambda}=
\frac{\partial_z^2H_\lambda(z_j)}{\partial_zH_\lambda(z_j)}.}
\]

In the regime where all zeros are real and simple, this can be rewritten as the interacting-zero evolution `dz_j/dlambda=2 sum_{k ne j} 1/(z_j-z_k)` with the appropriate symmetric summation/regularization (as in Rodgers--Tao). The **local derivative identity** does not require all zeros to be real, but the global real-particle description must not be assumed at `lambda=0` without RH.

## Numerical fixed-step test

Using the exact `Phi(u)` above, its first five integer-lattice terms (higher terms negligible at the demonstrated numerical resolution), numerical quadrature, and independent completed-xi checks, run `experiments/de_bruijn_running_coupling_probe.py`. The `H_0(z)=xi(1/2+iz/2)/8` identity agrees at `z=6,20,28,40` with absolute discrepancies between `2e-16` and `3e-18`.

Repeat the **same transform** with `delta_lambda=0.05`:

| Steps k | lambda=k*0.05 | First zero gamma_1(lambda)=z_1/2 | Second zero gamma_2(lambda)=z_2/2 |
|---:|---:|---:|---:|
| 0 | 0.00 | 14.1347251417 | 21.0220396388 |
| 1 | 0.05 | 14.1202371273 | 21.0031741817 |
| 2 | 0.10 | 14.1057546180 | 20.9843275396 |
| 3 | 0.15 | 14.0912776211 | 20.9654996445 |
| 4 | 0.20 | 14.0768061442 | 20.9466904288 |
| 5 | 0.25 | 14.0623401948 | 20.9278998259 |

An independent check of the zero-motion formula at `lambda=0` gives

- `d gamma_1/d lambda = -0.289815289`; a forward finite difference of step 0.001 gives `-0.289814189`.
- `d gamma_2/d lambda = -0.377497749`; a forward difference gives `-0.377493973`.

This verifies the deterministic zero flow numerically. It **moves the same indexed zeros across different deformed entire functions**. It does *not* map `gamma_1` of the original zeta into `gamma_2` of the original zeta.

## Why this is extraordinarily close to the RH question

A theorem of de Bruijn/Newman gives a finite threshold `Lambda_DN` such that *all* zeros of `H_lambda` are real **if and only if** `lambda>=Lambda_DN`. Consequently:

\[
\mathrm{RH}\iff\Lambda_{\mathrm{DN}}\le0.
\]

Rodgers and Tao proved `Lambda_DN>=0`. Hence the only way RH can hold is

\[
\boxed{\mathrm{RH}\iff\Lambda_{\mathrm{DN}}=0.}
\]

In this precise sense RH asks if **the true arithmetic kernel sits exactly at the critical edge of a zero-stabilizing flow**. That is extremely suggestive for a scale/renormalization or holographic interpretation, but `lambda` has not been shown to be a physical running coupling or boundary RG scale in GPP. A positive lambda can force real-zero behavior on the deformed function without proving what happens at lambda zero; backward evolution need not preserve real zeros.

The pre-existing GPP program identifies a related target: an arithmetic-specific Lee--Yang/Griffiths--Simon-type positivity construction for the true completed weight. The earlier **raw additive Weil OS no-go** remains intact. A proposed boundary reflection-positive covariance would need an arithmetic intertwiner and must distinguish true xi from shifted-zeta, Davenport--Heilbronn, and the new one-mode theta-weight controls.

## Is there instead a fixed increment from one *original* zero to the next?

The coarse, known **smooth phase** does give an approximately uniform coordinate:

\[
y(t)=1+\frac{\vartheta(t)}{\pi},\qquad
y(\gamma_{n+1})-y(\gamma_n)\approx1,
\]

and `theta(t)` comes from the completed gamma factor. In the first ten independently computed zero ordinates, however, the actual `y` increments range from approximately **0.578 to 1.476**, and the raw ordinate ratios range from roughly **1.037 to 1.487**. Thus neither a fixed additive nor fixed percentage step in `t`, nor exactly one unit of gamma phase, matches these zeros. The missing correction is the arithmetic oscillatory phase `S(t)`, whose prime-derived continuation and positivity are part of the unresolved RH structure.

The Riemann--Siegel expansion displays the unitary scaling frequencies explicitly:

\[
Z(t)=2\sum_{n\le\sqrt{t/(2\pi)}}n^{-1/2}
\cos\bigl(\vartheta(t)-t\log n\bigr)+R(t),
\]

where `n^{-it}=e^{-it log n}` is a unitary multiplicative character and `log n=sum_p v_p(n) log p`. This connects gamma-driven phase progression to the logarithmic prime generators of integer scaling, but the remainder is essential; the appearance of primes does **not** establish that zeta zeros are a physical Hamiltonian spectrum. This is the [NIST DLMF Riemann--Siegel formula](https://dlmf.nist.gov/25.10).

## Follow-up acceptance test

One genuinely useful project-level goal is to find an **arithmetically calibrated** flow/positivity mechanism which fixes `lambda=0` as the exact reality threshold, not just a large-positive-lambda region where real zeros are automatic. If a boundary intertwiner purports to supply it, test the original xi kernel and the explicit false controls under the same criterion, and prove a positive spectral measure/Gram factorization with the Archimedean, pole, and all-prime subtraction handled.

This is a research direction, not an existing construction. No claim that RH has been proved.
