# Codex update: Mehler--Fock repair and phase-space/Wiener--Hopf bridge

Date: 2026-08-28

Scope: Codex/GPT work only. No Claude material inspected.

## CI correction

At Verify2 head `27aae8531292fb2bbf9dabea794de33845e5ded1`, the root Build and Gibbs differential thermodynamics lanes are green. The sech-convolution lane is red only downstream at `SpectralRhoMehlerFockBridge.lean`; the already-built `SpectralRhoChamberProduct.lean` is green and therefore its all-order chamber product is not retracted.

The failing bridge had two independent defects: a complex-cast normalization goal in the base Gamma/Mehler--Fock identity and malformed nested cast syntax in the downstream all-order statements. These were rewritten without weakening the theorem at Verify2 commit `c9e96eed07cd75a24b1b0a8a4ed803c799e73ee2`.

## Exact bridge promoted

The focused scalar-cut derivation identifies the principal-series phase-space weight

P(lambda) = pi lambda / sinh(pi lambda),

with removable value P(0)=1. Verify2 already formalizes this as `extendedWienerHopfWeight` and proves continuity/strict positivity. The normalized Gamma family already has

rhoGamma(0,lambda) = 2 lambda / sinh(pi lambda)

away from zero and rhoGamma(0,0)=2/pi.

Hence the exact all-real relation is

rhoGamma(0,lambda) = (2/pi) P_ext(lambda),

including lambda=0. This has been promoted in new file

`GppVerify/QuantumGravity/SpectralRhoWienerHopfBridge.lean`

at Verify2 commit `290d0ba4a925b5d4adbef456c279f85699c7f03a`.

Equivalent normalization:

P_ext(lambda) = (pi/2) rhoGamma(0,lambda).

This closes a previously split normalization interface between the scalar-cut phase-space paper, Wiener--Hopf spectral weight, and Gamma chamber hierarchy. It does not itself prove a convolution theorem or a Weil positivity theorem.

## Scalar box interpretation audit

The focused scalar-box paper's corrected chain is retained:

1. antipodal two-particle cut geometry with uniform Fubini--Study measure;
2. Mellin image proportional to Gamma(Delta5) Gamma(Delta6) / Gamma(Delta5+Delta6);
3. Delta5+Delta6=2 is exact scale-invariant shadow completeness, not a residue pole;
4. regulated scalar-box cut is closed analytically;
5. fixed-u dispersion reconstructs the Euclidean box;
6. Mellin dispersion is multiplication by 8 pi^2 / sin(pi sigma).

The separate raised-box dimensional-regulator majorant remains open only at the nested affine-simplex/Fubini identification and subsequent DCT layer. `RaisedBoxSimplexBetaLayer.lean` already certifies the one-dimensional scaled Beta identity and convergence half-planes.

## Honest open boundaries

- Spectral: wait for terminal CI on the repaired Mehler--Fock bridge and new all-real Wiener--Hopf bridge. Do not call them kernel-certified before the lane/root Build is green.
- Scalar box: prove the nested simplex integral and DCT rather than restating the one-dimensional Beta layer.
- Arithmetic: local/finite positive-type structures remain insufficient for RH; the missing target is the completed global explicit-formula/Weil quadratic-form identification and unconditional positivity.
- Yang--Mills: the genuine D_s=4, mu!=0 massive-vector sewing numerator remains the next honest numerator calculation; state-count reconstruction is not a substitute.
- Gravity/higher loops: generic helicity and higher-multiplicity generalized cuts remain downstream of honest numerator sewing, while the four-point all-plus gravity sector is already separately closed by its mu^8 scalar-box decomposition.
