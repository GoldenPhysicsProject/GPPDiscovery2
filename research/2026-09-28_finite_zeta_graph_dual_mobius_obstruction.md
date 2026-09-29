# Dual Möbius obstruction in the finite zeta-graph metric

Date: 2026-09-28 America/Toronto / 2026-09-29 UTC
Status: exact finite identity and no-go/reduction. No RH claim.

This note follows the finite zeta-graph current-norm note.

The primal half-density von Mangoldt current is tame in the normalized finite zeta-graph
metric: its norm is at most log N. The natural next question is whether the raw scalar
resolvent character has a comparably tame dual norm. The answer is NO for a very precise
reason: its dual vector is exactly a weighted Möbius partial sum. At the critical character,
the desired subexponential bound is already an RH-equivalent statement.

## 1. Exact inverse-transpose formula

On S_N={1,...,N}, let

  Z_N(n,d)=sqrt(d/n) 1_{d|n}

and

  M_N=Z_N^{-1},
  M_N(n,d)=mu(n/d)sqrt(d/n)1_{d|n}.

For a complex parameter z define the raw scalar character

  a_z(n)=n^(-z).

Its dual representative in the synthesized Euclidean coordinates is

  b_{N,z}:=Z_N^(-T) a_z=M_N^T a_z.

The d-th coordinate is therefore

  b_{N,z}(d)
   = sum_{n<=N:d|n} mu(n/d)sqrt(d/n)n^(-z).

Writing n=dm gives the exact identity

  boxed:
  b_{N,z}(d)
   = d^(-z) sum_{m<=N/d} mu(m)m^(-1/2-z).

Thus the inverse-transpose zeta graph sends a multiplicative resolvent character directly
to a truncated reciprocal-zeta/Möbius Dirichlet sum.

No zeros or analytic continuation enter this identity.

## 2. Exact dual norm in the normalized graph metric

Recall

  G_N=Z_N^T Z_N,
  Gtilde_N=G_N/H_N.

For a coefficient functional a, its dual norm is

  ||a||^2_{Gtilde_N^{-1}}
   = a^* Gtilde_N^{-1} a
   = H_N ||Z_N^{-T}a||_2^2.

Hence for the raw character

  boxed:
  ||a_z||^2_{Gtilde_N^{-1}}
   = H_N sum_{d<=N}
       |d^(-z) sum_{m<=N/d} mu(m)m^(-1/2-z)|^2.

In particular the d=1 coordinate gives the unconditional lower bound

  boxed:
  ||a_z||_{Gtilde_N^{-1}}
   >= sqrt(H_N)
      |sum_{m<=N} mu(m)m^(-1/2-z)|.

Therefore a good dual norm for the raw character is NOT a free consequence of the good
primal current norm.

## 3. At z=0 the subexponential dual bound contains RH

At z=0 define

  A(N)=sum_{m<=N} mu(m)/sqrt(m).

The classical Mertens summatory function is

  M(x)=sum_{n<=x}mu(n).

Partial summation gives both directions:

- if RH holds in the standard equivalent form
    M(x)=O_epsilon(x^(1/2+epsilon))
  for every epsilon>0, then
    A(N)=O_epsilon(N^epsilon);

- conversely, if
    A(N)=O_epsilon(N^epsilon)
  for every epsilon>0, then another partial summation gives
    M(N)=O_epsilon(N^(1/2+epsilon)).

Thus

  A(N)=N^(o(1))

is an RH-strength condition, equivalent to the usual all-epsilon Mertens bound through
partial summation.

Since H_N grows only logarithmically, demanding an exp(o(log N))=N^(o(1)) bound for the
raw critical character's graph-dual norm already demands the same weighted Möbius control.

Therefore:

  boxed:
  DO NOT use a raw power character as the completed boundary functional and then claim
  that a subexponential dual-norm estimate is easier than RH.

It is simply another form of the target.

## 4. What the completion must actually change

The new finite graph theorem remains useful because it separates the two sides sharply:

- primal current: exact norm <= log N;
- raw scalar character: inverse-transpose contains the RH-hard Möbius partial sum.

So the missing completion must alter the observation map before the estimate is taken.

The Archimedean/pole/Poisson sector must not merely be added as an orthogonal direct-sum
decoration. If the total dual norm were a block-diagonal sum

  ||(a_z,a_inf)||^2
   = ||a_z||^2_{Gtilde_N^{-1}} + ||a_inf||^2,

then it could never reduce the arithmetic Möbius lower bound.

A successful global construction therefore needs a genuine graph/quotient/Schur coupling
between the arithmetic and Archimedean channels, so that the physical observable is not
the raw pair evaluated independently.

This is exactly what the product formula and the Riemann E/Poisson map are supposed to
supply.

## 5. Preferred finite formulation

Rather than estimate the raw a_z, construct an explicit zero-independent finite completed
scalar response m_N(u) from a coupled prime-Archimedean graph.

Requirements:

1. m_N is holomorphic on the slit domain at every finite N;
2. the elementary s=0,1 / u=1/4 pole is cancelled at finite N, not only after N->infinity;
3. the physical dual observation is represented only after imposing the Poisson/product
   graph relation;
4. its graph-dual norm is exp(o(log N)) on compact slit-domain sets;
5. in the Euler region m_N converges to the exact completed xi logarithmic response.

Then the primal current's extra factor <=log N is harmless under the already-proved
subexponential vacuum-instability criterion.

## 6. Falsifiers

A proposed completion fails immediately if any of the following is true:

- after eliminating auxiliary variables, its arithmetic dual coordinate is still exactly
  M_N^T a_z with no cancelling graph relation;
- its total norm is a block-diagonal arithmetic plus Archimedean norm, so no cancellation
  of the Möbius coordinate is possible;
- it becomes bounded only because the metric was explicitly tailored to the target
  observation vector, without an independent Poisson/product-formula derivation;
- its finite scalar response retains the u=1/4 completion pole;
- it supplies compact boundedness but no analytic dependence in u.

## 7. Relation to the self-dual-number-line picture

The inverse-transpose formula is the dual counterpart of the earlier statement that
Z_N sends the von Mangoldt current to log(n)/sqrt(n).

Primal direction:
  Möbius/logarithmic current --Z_N--> smooth number-line logarithmic mode.

Dual direction:
  raw principal-series character --Z_N^{-T}--> reciprocal-zeta/Möbius partial sum.

This is an exact finite adjoint manifestation of the same zeta gauge. It explains why the
bulk looks simple while the scalar boundary retains the full RH difficulty.

The global proof must therefore be a theorem about the PHYSICAL adjoint trace after
self-dual Poisson/product-formula sewing, not about the algebraic zeta gauge alone.
