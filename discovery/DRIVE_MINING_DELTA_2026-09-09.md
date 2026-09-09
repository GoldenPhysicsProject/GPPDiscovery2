# Drive mining delta — 2026-09-09

## Scope and promotion rule

This pass compared the March `decoding_reality_*` arithmetic-statistics sequence (through the July-uploaded `decoding_reality_v5-1.pdf`) against the later August finite-prime CAR/Koszul/Hodge formalization in Verify2. The purpose was to separate a persistent old slogan — “Fermi–Dirac from the p=2 Euler factor” — from the genuinely multiplicative fermionic arithmetic that the later prime-Fock construction actually supports.

Only exact identities or standard consequences proved independently below are promoted. The old physical confidence claims attached to them are not.

## 1. Chronology correction: the 7/8 thermal factor is not the p=2 Euler factor

The `decoding_reality` sequence repeatedly states

\[
\eta(s)=(1-2^{1-s})\zeta(s)
\]

and identifies the multiplier `1-2^{1-s}` with “the p=2 Euler factor,” using `s=d+1` to obtain the familiar fermion/boson thermal ratio

\[
1-2^{-d},
\]

in particular `7/8` for `d=3`.

The thermal identity is correct. The Euler-factor interpretation is not.

For `Re(s)>1`, splitting the zeta series into odd and even terms gives exactly

\[
\eta(s)=\sum_{n\ge1}(-1)^{n-1}n^{-s}
       =(1-2^{1-s})\zeta(s).
\]

But the genuine local Euler factor of zeta at `p=2` is

\[
\zeta_2(s)=(1-2^{-s})^{-1}.
\]

Removing the `p=2` Euler factor from the global Euler product multiplies zeta by

\[
1-2^{-s},
\]

not by `1-2^{1-s}`. These are different for every finite `s`.

There is a second decisive test: the coefficient sequence of `eta`,

\[
a_n=(-1)^{n-1},
\]

is not multiplicative. For example

\[
a_2a_2=(-1)(-1)=+1\neq a_4=-1.
\]

Therefore `eta(s)` has no Euler product of the ordinary multiplicative Dirichlet-series type. Calling `1-2^{1-s}` “the p=2 Euler factor” is mathematically incorrect.

### Promotion status

Promote:

* `eta(s)=(1-2^{1-s}) zeta(s)`;
* the massless thermal Fermi/Bose ratio `1-2^{-d}` in `d` spatial dimensions under the standard equal-degeneracy comparison.

Do not promote:

* `1-2^{1-s}` as the p=2 Euler factor;
* the claim that the physical Fermi/Bose distinction is derived from the single prime `p=2`.

This correction applies even though the wording survives into the later `decoding_reality_v5-1` revision.

## 2. The genuine fermionic prime gas: squarefree occupancy

The later Verify2 prime-Fermion work supplies the correct multiplicative arithmetic object.

Let

\[
x_p=p^{-s}.
\]

The ordinary zeta Euler factor is

\[
B_p(s)=\frac1{1-x_p}=1+x_p+x_p^2+\cdots,
\]

which is exactly the partition factor for an unrestricted nonnegative occupation number `k_p=0,1,2,...` at each prime.

A one-mode fermionic/exterior channel permits only occupancy `0` or `1`, so its local partition factor is instead

\[
F_p(s)=1+x_p.
\]

The elementary identity

\[
1+x=\frac{1-x^2}{1-x}
\]

gives, for `Re(s)>1`,

\[
\boxed{
\prod_p(1+p^{-s})
=\frac{\zeta(s)}{\zeta(2s)}
}
\]

and hence

\[
\boxed{
\sum_{n\ge1}\frac{\mu(n)^2}{n^s}
=\frac{\zeta(s)}{\zeta(2s)}.
}
\]

This is the exact fermionic prime-gas partition function: `mu(n)^2` restricts the integer states to squarefree integers, i.e. each prime generator is occupied at most once.

This is a much stronger and cleaner arithmetic realization of Fermi exclusion than the old `p=2` eta slogan.

## 3. The graded fermionic partition is the Möbius Dirichlet series

Exterior/Fock space has a natural parity grading. Taking the supertrace rather than the ordinary trace assigns `+1` to the vacuum and `-1` to the occupied one-prime state. The local graded factor is therefore

\[
S_p(s)=1-p^{-s}.
\]

Globally,

\[
\boxed{
\prod_p(1-p^{-s})
=\frac1{\zeta(s)}
=\sum_{n\ge1}\frac{\mu(n)}{n^s}
}
\]

for `Re(s)>1`.

Thus the exact multiplicative dictionary is

\[
\begin{array}{ccl}
\text{unrestricted prime occupancy} &\longleftrightarrow& \zeta(s),\\
\text{fermionic 0/1 occupancy} &\longleftrightarrow& \zeta(s)/\zeta(2s),\\
\text{fermion-parity supertrace} &\longleftrightarrow& 1/\zeta(s).
\end{array}
\]

This is directly aligned with the later Möbius–Koszul construction: creation/contraction on an exterior algebra of prime generators is not merely analogous to Möbius arithmetic; its basis states are squarefree prime subsets and its parity sign is exactly `(-1)^{number of occupied primes}`, the sign appearing in `mu(n)` on squarefree integers.

## 4. Exact relation to current Verify2 prime-Fermion machinery

`PrimeFermionDirac.lean` correctly formalizes a one-generator exterior algebra with

\[
c^2=a^2=0,
\qquad
ca+ac=1,
\]

and the self-adjoint Hodge–Dirac operator

\[
D(z)=\begin{pmatrix}0&\bar z\\z&0\end{pmatrix},
\qquad
D(z)^2=|z|^2I.
\]

It then chooses

\[
z=1-p^{-s},
\]

whose inverse is the bosonic local zeta factor `(1-p^{-s})^{-1}`.

This is mathematically coherent, but the provenance must be stated precisely:

* the **operator algebra** is fermionic/CAR;
* the chosen **holonomy** `1-p^{-s}` is the inverse denominator of the ordinary bosonic zeta Euler factor;
* this does **not** make `(1-p^{-s})^{-1}` the fermionic partition function.

The actual fermionic one-prime partition factor associated with 0/1 occupancy is `1+p^{-s}`.

This distinction prevents two different uses of “fermionic prime channel” from being conflated.

## 5. Statistics-resolved arithmetic wave expansion

The correction gives a precise new version of the possible arithmetic wave-particle duality.

For `Re(s)>1`, logarithms of the three product structures have exact prime-power expansions:

\[
\log\zeta(s)
=\sum_p\sum_{k\ge1}\frac{p^{-ks}}{k},
\]

\[
\log\frac{\zeta(s)}{\zeta(2s)}
=\sum_p\log(1+p^{-s})
=\sum_p\sum_{k\ge1}\frac{(-1)^{k+1}}{k}p^{-ks},
\]

and

\[
\log\frac1{\zeta(s)}
=\sum_p\log(1-p^{-s})
=-\sum_p\sum_{k\ge1}\frac{p^{-ks}}{k}.
\]

So the same prime-power “wave modes” `p^{-ks}=exp(-ks log p)` carry different statistics through their coefficient/sign structure.

This yields an exact, non-metaphorical refinement:

\[
\boxed{
\text{prime occupation configurations}
\longleftrightarrow
\text{prime-power exponential modes},
}
\]

with bosonic, fermionic, and graded-fermionic statistics distinguished by the local generating factor.

On the critical line `s=1/2+it`, every mode becomes

\[
p^{-k/2}e^{-ik t\log p},
\]

so the same discrete prime-power data is represented as oscillatory logarithmic-frequency modes. This is the exact wave side already feeding the current Euler-log-derivative / Poisson-kernel and causal heat-response fronts.

The RH-level gap is unchanged: these exact local/product identities do not supply the completed prime–Archimedean positivity theorem.

## 6. Consequences for the active fronts

### Prime gas

This pass materially sharpens the statistics dictionary:

* bosonic prime gas: `Z_B=zeta(s)`;
* fermionic prime gas: `Z_F=zeta(s)/zeta(2s)`;
* graded fermionic supertrace: `Z_super=1/zeta(s)`.

The old eta/`p=2` statement should not be used as the prime-gas statistics mechanism.

### RH / Möbius–Koszul

The `1/zeta(s)` identity is the exact global generating series naturally associated with fermion parity on squarefree prime subsets. This is a direct conceptual bridge to the existing exterior/Koszul prime construction, and is stronger than a dimension-count analogy.

It still does not produce a Hilbert–Pólya operator or prove RH. In particular, zeros of zeta are poles of the graded Dirichlet series after analytic continuation, not automatically zero modes of the finite CAR Dirac operator.

### Celestial cut / spectral weight

No new equality with the celestial weight `P(lambda)=pi lambda/sinh(pi lambda)` survives. The statistics-resolved prime products are multiplicative arithmetic objects, while the celestial cut weight is a continuous two-particle Gamma factor. Their exact commonality is transform/generating-function structure only.

### Scaled vs scale invariant

The local variable `x_p=p^{-s}` is dimensionless. Prime-gas statistics therefore changes the generating factor without introducing a new physical scale. This is scale-free arithmetic data; it should not be conflated with the mass homogeneity/zero-degree statements of the celestial cut or Dirac clock.

### Bosonic vs fermionic structure

This pass adds a second exact fermion/boson distinction alongside the SU(2)->SO(3) spinorial one:

1. representation-theoretic: spinor states vs vector observables;
2. occupation-theoretic: exterior 0/1 prime occupancy vs unrestricted prime exponents.

These are mathematically distinct mechanisms that happen to share the fermionic exclusion pattern. No theorem identifies them physically.

### SU(1)/SU(2)/SU(3), googly/shadow/orientation, Grassmannian

No new surviving result changes the corrected status of these fronts in this pass. In particular, literal `SU(1)` remains trivial, and nothing in the prime-statistics correction identifies celestial shadow, Wigner T, worldline reversal, Grassmannian tau, or the prime-Fock parity operation.

## 7. Upgradeability / formalization target

The current Verify2 machinery already contains the CAR/Hodge operator and the zeta local Euler factor. A high-value next file can separate the three local generating factors explicitly before any infinite-product analysis:

\[
B(x)=(1-x)^{-1},\qquad F(x)=1+x,\qquad S(x)=1-x,
\]

and prove finite-prime product identities such as

\[
F(x)(1-x)=1-x^2.
\]

For a finite prime set this needs only commutative-ring algebra, no analytic convergence or new axioms. The infinite identities can then be attached later to Mathlib's Dirichlet/Euler-product infrastructure if useful.

Recommended proof/status labels:

* `bosonicEulerFactor` — ordinary geometric Euler factor;
* `fermionicOccupancyFactor` — two-state exterior partition factor;
* `fermionicParityFactor` — supertrace factor;
* never label `1-2^{1-s}` as an Euler factor.

This is a proof-quality/upgradeability improvement because it prevents the current correct CAR construction from inheriting an old incorrect statistics slogan.

## Promotion summary

Promote:

* `eta(s)=(1-2^{1-s})zeta(s)` as an odd/even-series identity;
* `Z_F(s)=prod_p(1+p^{-s})=zeta(s)/zeta(2s)`;
* `sum mu(n)^2 n^{-s}=zeta(s)/zeta(2s)`;
* `Z_super(s)=prod_p(1-p^{-s})=1/zeta(s)=sum mu(n)n^{-s}`;
* the exact CAR one-prime Hodge–Dirac structure already in Verify2;
* the statistics-resolved prime-power logarithmic expansions;
* squarefree prime subsets as the natural basis of the finite fermionic prime Fock space.

Do not promote:

* `1-2^{1-s}` as the `p=2` Euler factor;
* eta as the fermionic prime-gas Euler product;
* the claim that the physical spin-statistics theorem is derived from prime `2`;
* the bosonic zeta local factor as the fermionic partition factor merely because it appears as the inverse holonomy in a CAR Dirac operator;
* any RH conclusion from these product identities alone.
