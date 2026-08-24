# Number thermodynamics on the convergent half-plane

For real beta > 1, define the canonical distribution on positive integers

`P_beta(n) = n^(-beta) / zeta(beta)`.

This is normalized because `zeta(beta)=sum_{n>=1} n^(-beta)`.

Interpret the arithmetic energy as

`E_n = log n`, so that `exp(-beta E_n)=n^(-beta)`.

Then the exact canonical thermodynamic quantities are:

- Partition function: `Z(beta)=zeta(beta)`.
- Free energy: `F(beta)=-(1/beta) log zeta(beta)`.
- Mean arithmetic energy:

  `U(beta) = E_beta[log n] = - d/d beta log zeta(beta) = -zeta'(beta)/zeta(beta)`.

- Shannon/Gibbs entropy:

  `S_N(beta) = -sum_n P_beta(n) log P_beta(n)`

  `= log zeta(beta) + beta U(beta)`

  `= log zeta(beta) - beta zeta'(beta)/zeta(beta)`.

- Energy fluctuation / susceptibility:

  `Var_beta(log n) = d^2/d beta^2 log zeta(beta)`

  `= zeta''(beta)/zeta(beta) - (zeta'(beta)/zeta(beta))^2 >= 0`.

Thus `log zeta(beta)` is convex on beta>1. This variance is also the Fisher information of the one-parameter Gibbs family with respect to beta, giving a canonical information-geometric metric on the real thermodynamic domain.

## Exact independent-prime factorization

Unique factorization makes the ensemble an actual product of independent geometric prime occupations. Writing

`n = prod_p p^(K_p)`, 

we have, independently for each prime,

`P_beta(K_p=k) = (1-q_p) q_p^k`, `q_p=p^(-beta)`, `k=0,1,2,...`.

Hence

`E[K_p] = q_p/(1-q_p) = 1/(p^beta-1)`,

`Var(K_p) = q_p/(1-q_p)^2 = p^beta/(p^beta-1)^2`.

Because `log n = sum_p K_p log p`, the total thermodynamics decomposes prime-by-prime:

`U(beta) = sum_p log(p)/(p^beta-1) = -zeta'(beta)/zeta(beta)`,

`Var_beta(log n) = sum_p (log p)^2 p^beta/(p^beta-1)^2 > 0`,

`C(beta) = beta^2 Var_beta(log n)
         = sum_p beta^2 (log p)^2 p^beta/(p^beta-1)^2 > 0`.

The entropy is additive as well. For one prime mode,

`S_p(beta) = -log(1-q_p) + beta log(p) q_p/(1-q_p)`

`          = -log(1-p^(-beta)) + beta log(p)/(p^beta-1)`.

Therefore

`S_N(beta) = sum_p S_p(beta)`

throughout beta>1, and this prime sum equals

`log zeta(beta) - beta zeta'(beta)/zeta(beta)`.

This is stronger than a loose boson-gas analogy: on the convergent real axis the zeta Gibbs measure is literally the law of a countable collection of independent geometric occupation variables with one-particle energies `log p`.

## Prime-mode cumulants

The local Massieu potential is

`log Z_p(beta) = -log(1-p^(-beta)) = sum_{k>=1} p^(-k beta)/k`.

Thus for every integer r>=1,

`(-1)^r d^r/d beta^r log Z_p(beta)
 = (log p)^r sum_{k>=1} k^(r-1) p^(-k beta) > 0`.

Summing the independent prime cumulants gives the global strict hierarchy

`kappa_r(beta)
 = (-1)^r d^r/d beta^r log zeta(beta)
 = sum_p (log p)^r sum_{k>=1} k^(r-1) p^(-k beta)
 = sum_{n>=2} Lambda(n) (log n)^(r-1) n^(-beta) > 0`.

In particular,

`d/d beta Var_beta(log n) = -kappa_3(beta) < 0`.

So the Fisher metric is not only positive: it decreases strictly with inverse temperature across the entire convergent phase.

## Physics dictionary to test, not assume

- `log n`: additive position/energy coordinate of multiplicative number space.
- prime `p`: elementary bosonic mode with energy `log p`.
- `log zeta`: pressure / Massieu potential.
- `d^2 log zeta`: fluctuation susceptibility / information metric.
- beta=1 pole: limiting/Hagedorn-type singularity of the naive prime gas.
- analytic completion + functional equation: candidate interacting/renormalized continuation beyond the naive thermodynamic domain.

The last two lines are interpretations. All identities and inequalities above them are exact consequences of the Euler product, unique factorization and Gibbs calculus for beta>1. No positivity is analytically continued into the critical strip.