# Zeta Gibbs cumulant generator and Renyi entropy

Codex/GPT discovery track, 2026-08-24.

For real `beta>1`, let

`P_beta(n)=n^(-beta)/zeta(beta)`,  `n>=1`,

and define the arithmetic energy/random variable

`X(n)=log n`.

Everything below is an exact consequence of the absolutely convergent Dirichlet series.
No analytic continuation into the critical strip is used.

## Exact moment-generating function

For real (or complex, in the common convergence strip) `u` with

`Re(beta-u)>1`,

one has

`E_beta[exp(u X)]`

` = (1/zeta(beta)) sum_{n>=1} n^(-beta) n^u`

` = zeta(beta-u)/zeta(beta)`.

Thus the cumulant-generating function is

`K_beta(u)=log E_beta[e^(uX)]`

`         = log zeta(beta-u)-log zeta(beta)`.

Consequently

`kappa_m(beta) = d^m/du^m K_beta(u)|_(u=0)`

`              = (-1)^m d^m/d beta^m log zeta(beta)`.

The first cases are

`kappa_1 = - (log zeta)' = E[log n]`,

`kappa_2 =   (log zeta)'' = Var(log n) > 0`,

`kappa_3 = - (log zeta)'''`,

and so on.  The earlier alternating derivative-sign hierarchy is therefore not a collection
of unrelated identities: it is the ordinary cumulant hierarchy of one Gibbs random variable.

## Prime-mode factorization of the CGF

Using the Euler product in the same domain,

`K_beta(u)`

` = sum_p [ log(1-p^(-beta)) - log(1-p^(-(beta-u))) ]`.

Equivalently, if `K_p` is the independent geometric occupation of prime `p`,

`P(K_p=k)=(1-p^(-beta))p^(-beta k)`,

then

`E[e^(u log(p) K_p)]`

` = (1-p^(-beta))/(1-p^(-(beta-u)))`,

and the global MGF is the product of these local MGFs.  This makes additivity of all
cumulants automatic.

The maximal real open interval around `u=0` allowed by the global Dirichlet series is

`u < beta-1`.

The boundary `u=beta-1` is exactly where the shifted partition function reaches the zeta
pole.  In large-deviation language, the pole is therefore also the finite-temperature
boundary of the exponential-moment domain.

## Exact Renyi entropy

For Renyi order `alpha>0`, `alpha != 1`, with `alpha*beta>1`,

`sum_n P_beta(n)^alpha`

` = zeta(alpha beta)/zeta(beta)^alpha`.

Hence

`H_alpha(beta)`

` = 1/(1-alpha) * log(sum_n P_beta(n)^alpha)`

` = [log zeta(alpha beta) - alpha log zeta(beta)]/(1-alpha)`.

This is the exact Renyi spectrum of the zeta Gibbs ensemble.

Prime factorization gives the equivalent additive form

`H_alpha(beta)`

` = sum_p { log(1-p^(-alpha beta)) - alpha log(1-p^(-beta)) }/(alpha-1)`.

Taking `alpha -> 1` formally recovers the Shannon/Gibbs entropy already recorded:

`S(beta)=log zeta(beta)-beta zeta'(beta)/zeta(beta)`.

The limit itself should be formalized with differentiability rather than treated as an
algebraic substitution.

## Why this matters for the active program

1. The zeta partition function is not merely analogous to a thermal partition function:
   shifting its argument generates the exact exponential moments of `log n`.
2. The pole at `beta=1` controls both the partition function and the boundary of the global
   cumulant-generating domain.
3. Renyi entropies are exact zeta ratios, giving a second information-geometric family beyond
   the Fisher metric/variance.
4. None of these facts extends positivity into the critical strip by itself.  Any such bridge
   still requires a justified completed/continued object.

## Formalization targets

- Prove the finite-truncation MGF ratio algebraically first.
- Lift to the countable Gibbs distribution using the existing summability infrastructure on
  `beta>1`.
- Derive `kappa_2=variance` from the CGF and connect it to the already verified Fisher theorem.
- Formalize the Renyi zeta-ratio identity for `alpha beta>1`.
