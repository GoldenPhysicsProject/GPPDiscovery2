# GPP Drive mining delta — 2026-09-02

This note records only new chronology/formalization consequences found after the 2026-09-01 pass. It does not revive superseded physical interpretations.

## 1. Residual T-boundary claims survived in a second Verify2 module

The 2026-09-01 cleanup correctly removed the old Majorana/massless-neutrino/mirror-baryon scaffolds from `StandardModel/MajoranaCondition.lean`, but repository-wide mining found duplicates in `NumberTheory/WeylCasimir.lean`:

- `lightest_neutrino_massless : True := trivial`;
- `majorana_from_T_boundary : True := trivial`;
- a vacuous `mirror_baryon_lower_bound : (1 : ℕ) ≤ 1 := le_refl 1` whose prose presented the tautology as a physical T-boundary prediction.

These are not independent open mathematical targets. Their source provenance is the same superseded zitterbewegung/T-boundary layer whose chirality argument depended on the false step that ordinary Wigner time reversal flips helicity. They were therefore removed from Verify2 rather than counted as unresolved proof obligations.

The exact Weyl-vector, Grassmannian, and Spin(8) Casimir calculations in the same file were retained.

## 2. Boson/fermion structure: Spin(8) triality gives a real algebraic bridge, but only at Casimir level

`WeylCasimir.lean` already contains an exact D4 calculation. With Weyl vector

`rho = (3,2,1,0)`

and weights

- vector `lambda_v = (1,0,0,0)`,
- spinor `lambda_s = (1/2,1/2,1/2,1/2)`,
- cospinor `lambda_c = (1/2,1/2,1/2,-1/2)`,

its normalization

`C2(lambda) = <lambda, lambda + 2 rho>`

gives

`C2(lambda_v) = C2(lambda_s) = C2(lambda_c) = 7`.

This was independently rechecked algebraically. It is a genuine exact trace of Spin(8) triality and is relevant to the archive's repeated bosonic-versus-fermionic theme: a vector representation and two spinorial representations sit in a triality orbit with equal quadratic Casimir.

But equality of Casimir eigenvalues is **not** boson/fermion equivalence and does **not** by itself imply equal conformal weights. Any conformal-weight statement needs a separate model-specific relation between the Casimir and the conformal Hamiltonian/Laplacian. Verify2 documentation was corrected accordingly.

The robust boson/fermion research target therefore remains representation type and covering structure:

- vector versus spinor/cospinor triality;
- real/complex/quaternionic type;
- `2pi` sign / `4pi` closure for spinorial lifts;
- comparison with the proved Grassmannian order-four map.

These are exact structural comparisons, not an identification of sectors.

## 3. Mass/orientation v3: the strongest surviving Grassmannian statement was rechecked

The July `mass_orientation_coupling_v3.pdf` states on the big cell of `Gr(2,4)`

`tau(A) = (det A)^(-1) A epsilon`,

with `epsilon^2 = -I`, and claims

`tau^2 = -id`, `tau^4 = id`,

plus

`charpoly(d tau_A)(t) = t^4 - (det A)^(-4)`.

The differential characteristic-polynomial formula was independently checked symbolically from the Jacobian of the four matrix entries. It simplifies exactly to

`t^4 - det(A)^(-4)`.

Thus its eigenvalues are fourth roots of unity scaled by `det(A)^(-1)` over the complexified tangent space, and their moduli on a chosen complex absolute value are `|det A|^(-1)`. The exact `Z4`/inverse-determinant scaling is therefore a legitimate bridge between the Grassmannian and the mass/orientation discussion.

What is *not* promoted is the interpretive jump from this differential spectrum to literal physical fermion statistics, CPT, or a universal mass ontology. Those require additional representation/dictionary theorems.

## 4. Scaled versus scale invariant: sharpen the archive statement

The same `mass_orientation_coupling_v3.pdf` contains a useful but easily overstated proposition. Its actual proof is dimensional: under a common transformation

`m_i -> kappa m_i`

with dimensionless couplings fixed, every **dimensionless ratio built solely from those masses and couplings** is unchanged. That is the exact homogeneous statement.

This should not be promoted as the unrestricted claim that a common rescaling of particle masses changes no physical observable in an arbitrary interacting QFT. An independently fixed dimensionful scale (for example one introduced by dimensional transmutation, a background curvature scale, a temperature, a cutoff, or an external apparatus not co-scaled with the system) supplies a comparison and can make the rescaling observable. The manuscript itself later invokes the trace anomaly, which is precisely the warning that classical scale reasoning is not the whole interacting quantum story.

So the durable distinction is:

- **scaled/covariant:** an observable changes homogeneously under a common scale transformation;
- **scale invariant:** a dimensionless degree-zero combination is unchanged because no independent dimensionful reference remains;
- **anomalous/dimensionally transmuted:** quantum dynamics can generate an independent scale and break the naive classical scaling statement.

This aligns cleanly with the celestial-cut result already isolated in prior passes: the scalar-box factor becomes scale-independent specifically on the zero-homogeneity locus `Delta5 + Delta6 = 2`; scale independence is a precise homogeneity statement, not the absence of all dimensional data everywhere.

## 5. SU(1), SU(2), SU(3): no literal SU(1) sector found

A new exact Drive search for `SU(1)` did not uncover a GPP construction in which `SU(1)` is a nontrivial gauge factor. The hits were either unrelated literature/search noise or ordinary `SU(N)` notation. The mathematical verdict remains unchanged and is now stronger by negative provenance: `SU(1)` is the trivial group, so a remembered `1,2,3` ladder must be reconstructed as something such as

`U(1), SU(2), SU(3)`,

a rank/dimension ladder, or a stabilizer chain. It should not be encoded as a nontrivial `SU(1) -> SU(2) -> SU(3)` theorem.

## 6. Arithmetic wave-particle and RH front: no scalar-Gaussian work should be duplicated

Comparison of arithmetic-principal-series v25 and v34 confirms the chronology already found on 2026-09-01:

- the heat-trace/complete-monotonicity/OS-reflection-positive architecture is already present by v25;
- v34 adds the causal Dirichlet heat boundary commutator, the von-Mangoldt prime-power anomaly, the finite-prime obstruction analysis, and the support-normalized phase / Fejer / Suzuki bridge.

Therefore the useful new action is not to reprove the scalar Gaussian transforms already in Verify2. The missing operator/global layer remains:

1. formal Dirichlet heat semigroup on the half-line;
2. unilateral translation commutator and trace anomaly;
3. prime resolvent/logarithm expansion with von Mangoldt weights;
4. completed prime-Archimedean relative trace cancellation;
5. positivity / semilocal Weil / Suzuki norm-square bridge.

This is the precise arithmetic version of the proposed wave-particle language: discrete prime-power atoms are represented through oscillatory Fourier/Poisson modes and through causal heat-boundary responses. The dual descriptions are exact where derived; the positive completed spectral realization is still the RH-level obstruction.

## 7. Formal action taken

Updated `GppVerify/NumberTheory/WeylCasimir.lean` on Verify2 `main` to:

- remove the residual superseded T-boundary neutrino stubs;
- remove the vacuous mirror-baryon tautology carrying a physical interpretation;
- retain the exact Weyl/Grassmannian/Spin(8) calculations;
- correct the Spin(8) triality prose so equal quadratic Casimirs are not presented as an automatic conformal-weight theorem.

Commit: `ac4b074c92c18f26285cc0da3b4ec190272d0fec`.

## 8. Next mining/formal consequences

- Search all remaining Verify2 scaffolds for **provenance duplication**: a stub may survive in a second module after its source premise has been superseded elsewhere.
- Treat the Grassmannian differential spectrum `t^4 - det(A)^(-4)` as exact geometry; isolate any physical dictionary as a separate theorem rather than embedding it in comments.
- If a scale theorem is formalized, state it as invariance of degree-zero combinations under common scaling, with hypotheses excluding an independent dimensionful scale.
- Preserve Spin(8) triality Casimir equality as a representation-theoretic comparison target for boson/fermion structure, not as sector identity.
- On RH, move upward to the causal operator/relative-trace layer rather than rebuilding already formalized scalar heat identities.
