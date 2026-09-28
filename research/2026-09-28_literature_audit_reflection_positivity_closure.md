# Literature audit for the arithmetic-holography / reflection-positivity closure

Date: 2026-09-28
Status: literature orientation only. No theorem here is counted as new GPP mathematics unless separately derived in Discovery2.

The purpose of this audit is not to replace the GPP construction with known work. It is to identify exactly which joints are classical, which candidate mechanisms already have rigorous operator theory behind them, and where the present synthesis still has room to be genuinely new.

## 1. Weil positivity is the correct classical endpoint

Weil's explicit-formula criterion makes RH equivalent to positivity of the completed arithmetic distribution on multiplicative convolution squares. Modern expositions (for example Conrey's Notices survey) emphasize precisely the prime/zero duality and the positivity criterion.

Conclusion for GPP:
calling the target "reflection positivity" is mathematically appropriate, but the phrase itself is not progress. Progress must come from deriving that positivity from a zero-independent state/operator construction.

## 2. de Branges / Lagarias supplies the canonical-system endpoint, not the arithmetic construction

de Branges theory and Lagarias's expositions show that RH can be encoded in Hermite-Biehler/de Branges spaces and self-adjoint generalized differential operators. Under the right positivity/Hermite-Biehler property one gets a Hilbert-Polya operator.

Conclusion for GPP:
the Fredholm/density-matrix and Hardy/model-space targets are compatible with a mature operator theory. The new burden is upstream: construct the correct de Branges/canonical object from primes + Archimedean data rather than assume its positivity.

## 3. Burnol is directly relevant to the co-Poisson/Sonine side

Burnol's work connects:
- co-Poisson/Duffin-Weinberger duality;
- Sonine spaces;
- de Branges spaces;
- complete/minimal systems built from zeta zeros.

Conclusion for GPP:
the current co-Poisson, boundary-ghost and model-space work sits close to a real classical lineage. We should use Burnol as a compatibility check and source of exact functional-analytic tools, not as a substitute for the missing positivity theorem.

## 4. Connes-Consani already isolate Archimedean Weil positivity in a semi-local operator framework

Connes and Consani (2020) derive a conceptual Hilbert-space explanation for positivity of the ARCHIMEDEAN Weil functional using compressed scaling actions, Sonin trace, prolate spheroidal functions and Toeplitz matrices. They explicitly describe the semilocal/global extension as the place where Weil positivity would imply RH.

Conclusion for GPP:
this strongly supports the project's division of labor:
- real place can have an independent positive operator realization;
- the hard theorem is finite-place + real-place sewing.
It also warns against claiming that an Archimedean positive kernel alone addresses RH.

## 5. Bost-Connes gives the exact critical arithmetic KMS system

Bost-Connes constructs a C*-dynamical system with Hamiltonian log n, partition function zeta(beta) for beta>1, and a phase transition at beta=1. The critical beta=1 KMS state exists even though the Gibbs trace diverges.

Conclusion for GPP:
the project's KMS midpoint at beta/2=1/2 is not a decorative analogy. It is the canonical modular midpoint of the standard arithmetic quantum statistical system.

The new GPP result in the companion note is sharper:
the multiplicative shift mu_n has critical midpoint norm squared n^(-1/2), and prime-power shifts weighted by sqrt(log p) reproduce Lambda(p^k)/sqrt(p^k) exactly.

## 6. KMS <-> reflection positivity on a strip is rigorous general theory

Neeb-Olafsson (2019) characterize KMS positive-definite functions in terms of modular objects (Delta,J) and obtain Osterwalder-Schrader quantization. Adamo-Neeb-Schober (2024/2025) develop the disc/half-plane/strip reflection-positive equivalence and its relation to H-infinity positive functionals and standard pairs.

Conclusion for GPP:
there is a ready-made rigorous theorem that can turn a CORRECT arithmetic KMS two-point function into reflection positivity and OS reconstruction. The missing task is identification: show that the Weil form is that two-point function after prime-Archimedean sewing.

This is much narrower than inventing an OS theory from scratch.

## 7. Hedenmalm-Lindqvist-Seip explains why scalar boundary evaluation is singular

Their Hilbert-space theory of Dirichlet series is part of the established analytic background for the half-plane evaluation thresholds encountered by the Bohr lift.

Conclusion for GPP:
the Bohr-Hardy result Z_s M_s=1 for Re(s)>1/2 and the failure of identity-point scalarization are not paradoxical. The project should continue treating scalarization as the exceptional map, not internal prime dynamics as the pathology.

## 8. Rodgers-Tao makes "zero margin" a hard design constraint

Rodgers-Tao proved the de Bruijn-Newman constant is nonnegative. Since RH is equivalent to Lambda_DN<=0, RH would mean Lambda_DN=0.

Conclusion for GPP:
a successful mechanism should be exact/reflection-positive at threshold, not a sloppy coercive estimate with unexplained positive margin. This strongly favors KMS midpoint, exact Schur complement, exact OS square, or canonical-system identities.

## 9. The standard modular-surface scattering parent is informative but insufficient

The modular Eisenstein S-matrix contains the ratio Lambda(2w-1)/Lambda(2w), and its bulk Laplacian is already self-adjoint with unitary scattering on Re(w)=1/2.

Conclusion for GPP:
"find a self-adjoint arithmetic bulk" is too weak. RH is an additional resonance-location/width rigidity property. This agrees with the project's Fisher-zero and Julia-colligation no-go results.

## 10. Recent reflection-positivity preprints do not close the gap

A 2026 preprint explicitly titled "Arithmetic Reflection Positivity" reformulates RH through a Herglotz/reflection-positive spectral measure, proves local/finite positivity statements, and leaves preservation in the infinite Euler limit as a conjectural step.

Conclusion for GPP:
the general reflection-positivity slogan is now present in the literature. The GPP novelty must be the specific machinery that crosses the infinite-prime/Archimedean joint:
- Bohr H2/H1 internal continuation;
- connected BPY decimation intertwiner;
- critical first-chaos coercivity;
- exact KMS midpoint realization of Weil half-density weights;
- theta/number-circle reconstruction;
- TFD parity and two-channel renormalization.

## 11. Audit of Claude's ARITHMETIC_HOLOGRAPHY_RIGOROUS.md

The note's main separation is sound:
- mirror symmetry/function equation is proved;
- Mellin half-line/Hardy geometry is standard;
- prime torus/Bohr lift is an exact internal model;
- Weil reflection positivity is RH-equivalent, not proved;
- the bare Riemann split is not a Hermite-Biehler solution.

Two precision points should be kept explicit.

First, the celestial direction sphere CP1 and the complex spectral Delta-plane are different objects. The note itself flags this correctly.

Second, OS reconstruction would produce a self-adjoint reconstructed generator from a proven reflection-positive arithmetic theory, but identifying its full spectral measure with precisely the zeta-zero ordinates still uses the explicit-formula/cyclicity identification. It is a consequence of the completed construction, not of abstract OS positivity alone.

## 12. What the literature suggests we should do next

Do NOT branch into another equivalence criterion.

Use the general KMS/RP theory as a theorem package and attack one exact identification:

Construct a zero-independent analytic operator family A_f in the critical arithmetic KMS standard form, enlarged by the BPY/Archimedean field, such that

  omega_1( A_f^* sigma_{i/2}(A_f) )
  =
  W(f * f_tilde).

The finite-place coefficient Lambda(n)/sqrt(n) is now already explained exactly by the KMS midpoint norm of prime-power shifts.

The connected prime information is now known to embed coercively into the BPY field.

Therefore the only missing piece in this equation is the renormalized cross-channel / Archimedean sewing that converts those local positive midpoint channels into the signed Weil correlation without reintroducing raw scalar evaluation.

That is the direct target.
