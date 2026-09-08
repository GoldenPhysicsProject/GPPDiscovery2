# Codex/GPT research rotation — 2026-09-08 run 11

Scope: Codex/GPT work only. No Claude-owned material inspected or used.

## Live state checked

- GPPVerify2 `codex/lean-workbench`: `1207fa9ff9e6f61243d05ea9df78131200276166`.
- Full Build #2124: success on that exact head.
- Changed-Lean #976: success on that exact head.
- No new Lean theorem was pushed this run; the new analytic statements below are discovery-stage until their supporting measure/Fourier or entropy calculus is formalized cleanly.

## Principal-series / chamber front

The remaining mixed integral in the current A4 reduction is

`A = E_p[D(t)^2 q(t)^2]`,

with

`p(t)=8t/sinh(2*pi*t)`,
`q(t)=(pi/2)tanh(pi*t)`,
`D(t)=Re psi(1/2+it)-psi(1/2)`.

A new exact normalization was isolated. Set

`nu(dt)=p(t)q(t)^2 dt`.

Because the existing phase law gives `E_p[q^2]=1`, `nu` is a probability measure. More explicitly, under

`y=tanh(pi*t)`

its pushforward to `(-1,1)` has density

`f_nu(y)=|y| atanh(|y|)`.

Thus

`A = 2 int_0^1 y atanh(y) D(atanh(y)/pi)^2 dy`.

The characteristic function is also exact. With

`mu(t)=(pi/2)sech^2(pi*t)` and `phi(s)=s/(2 sinh(s/2))`,

`p q^2 = -t mu'(t)` implies

`chi_nu(s)=phi(s)+s phi'(s)`.

The compact-support moments are

`E_nu[y^(2n)] = (1/(n+1)) sum_{k=0}^n 1/(2k+1)`.

This does not yet prove the candidate

`A = 1/2 - 2 log 2 + 4 log^2 2`,

but it converts the last A4 obstruction into an ordinary L2 expectation against a normalized compactly supported law. The executable audit is `discovery/principal_series_A_phase_weight_measure_audit.py`.

The previously proved Fourier closure

`C=E_p[(D')^2]=16 log 2 - 2 pi^2/3`

and the exact relation for `B=E_p[D q D']` remain unchanged. Hence A is still the only independent analytic target before the A4 formula can be promoted.

## Prime/number-gas thermodynamics front

For

`Z(beta,eta)=sum_{n>=2} exp[-beta X_n-eta X_n^2]`, `X_n=log n`,

let the normalized Gibbs law be `p_n` and define Shannon entropy

`S=log Z + beta E[X] + eta E[X^2]`.

Fix `(beta,eta)` and scale along the natural-parameter ray by `tau>0`:

`Y_n=beta X_n+eta X_n^2`, `p_n(tau) proportional exp[-tau Y_n]`.

Then exactly

`d/dtau log Z_tau = -E_tau[Y]`,
`d/dtau E_tau[Y] = -Var_tau(Y)`,

so

`dS_tau/dtau = -tau Var_tau(Y)`.

For beta>1 and eta>=0, Y is nonconstant on n>=2, hence

`dS_tau/dtau < 0`.

At tau=1,

`beta S_beta + eta S_eta = -Var(beta X+eta X^2) < 0`.

Because the Hessian of log Z is the Fisher covariance matrix `g` of `(X,X^2)`, the same variance is the radial Fisher norm

`(beta,eta) g (beta,eta)^T = Var(beta X+eta X^2) > 0`.

Defining `C_rad(tau)=tau^2 Var_tau(Y)` gives the exact fluctuation/entropy identity

`dS_tau/d(log tau) = -C_rad(tau) < 0`.

This is independent of scalar-curvature sign and does not revive the retracted `R<=0` conjecture. The executable finite-truncation audit is `discovery/prime_gas_radial_entropy_fisher_audit.py`.

## Amplitudes front

No new master coefficient was promoted. The scalar celestial cut -> Mellin -> dispersion -> regulated box chain remains closed in its stated scope, including the derived two-particle factor `P(lambda)=pi lambda/sinh(pi lambda)`. The focused scalar-box paper explicitly distinguishes this Gamma/phase-space factor from the genuine SL(2,C) Plancherel density and leaves the all-topology/higher-loop theorem open.

The honest next amplitude frontier remains convention-locked generic YM topology projection/normalization, then generic gravity/helicity sectors, higher multiplicity, and generalized higher-loop cuts. The previously closed adjacent-MHV YM and four-graviton all-plus one-loop examples remain benchmarks only.

## Completed-zeta / Weil front

No RH-bearing theorem was added. Positive-real half-density/principal-series unitarity, Delta=2s, exact spectral/chamber laws, Mehler-Fock and Wiener-Hopf structures remain local exact mathematics. The unresolved arithmetic obstruction remains global completed prime-plus-Archimedean Weil positivity / Schur gluing.

## Next frontier

1. Attack the compact-law representation of A using `chi_nu=phi+s phi'` and the digamma cosine kernel; seek a hyperbolic cancellation analogous to the successful C closure.
2. Formalize the radial entropy identity in Lean if the existing zeta-Gibbs expectation/covariance API exposes the needed derivative lemmas without premise-only wrappers.
3. Resume convention-locked generic YM topology projection rather than extrapolating from special helicity benchmarks.
