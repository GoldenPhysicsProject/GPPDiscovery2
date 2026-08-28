# Codex continuation — AFT/spectral audit — 2026-08-28

Codex/GPT track only. No Claude work inspected.

## CI checkpoint

At Verify2 `571553fe567d497b054bbba68d292b979184a6d0`, the dedicated spectral, arithmetic-OS, Gibbs, and Fisher workflows are green; aggregate Build was still running when polled. Therefore the repaired full Wiener–Hopf/Gamma chamber hierarchy and the abstract pinned-Mathlib `Aᴴ A` arithmetic OS factorization criterion are now CI-certified.

The certified spectral chain includes the global base normalization

`extendedWienerHopfWeight x = (pi/2) * Re(rhoGamma 0 x)`,

its inverse, the Mehler–Fock all-real chamber family, and the multiplicative hierarchy

`rhoGamma k x = (prod_{j<k} rhoStepFactor j x) * rhoGamma 0 x`,

with positive chamber multipliers. Thus the Gamma/Mehler–Fock/Wiener–Hopf spectral weight is no longer only a base-chamber coincidence: every formal chamber is a positive polynomial/rational multiplier of the same Wiener–Hopf base weight.

## AFT / arithmetic OS advance

The abstract theorem `K=Aᴴ A -> K.PosSemidef` is now CI-green. More importantly, Verify2 `63d7eca93cc499cf793c234c9bd3b620cfb89732` adds `ArithmeticPrimeFactorMap.lean`, an explicit finite prime-local factor rather than another positivity inequality. For cutoff `M`, positive-time samples `t_i`, and prime scale `p`, define

`A(m,i)=sqrt(modeWeight p (m+1)) * modeValue p (m+1) (t_i)`.

The associated local kernel is definitionally

`K_p = Aᴴ A`,

hence positive semidefinite by the certified factorization criterion. On `p>=1`, the square of each real factor amplitude is exactly

`modeWeight(p,m) * modeValue(p,m,t)^2`.

This realizes the original AFT `A^*A` architecture explicitly for every finite positive prime-local sector. Workflow gate added at Verify2 `532fb5a03184d749b186810b10781ad91416e86e`; fresh CI is required for this new file.

This is a genuine narrowing of the RH obstruction. Prime-local factorization is constructible. The remaining problem is the completed global gluing: the standard explicit formula carries the prime contribution with the opposite overall sign, so one cannot simply direct-sum these positive local factors. A successful AFT must couple the prime factors to the Archimedean/vacuum sector through a global no-ghost/defect-cancellation mechanism and then identify the resulting OS form with the genuine Weil quadratic form. No RH claim.

## Gibbs / number thermodynamics

Critical pole removal and the exact cumulant/entropy/free-energy/fluctuation differential layer remain CI-green on `beta>1`:

`H(beta)=(beta-1)Z(beta)>0`,

`log Z(beta)=log H(beta)-log(beta-1)`,

`F(beta)=-log H(beta)/beta + log(beta-1)/beta`.

The next honest analytic input remains regularity/derivative control of `H` as `beta -> 1+`.

## Scalar box

No new scalar theorem this run. Inner affine simplex Beta reduction and outer Beta product remain established; the exact blocker is the nested interval/Fubini endpoint passage and then DCT for the regulator limit.

## Yang–Mills / gravity / higher cuts

No honest new numerator this run. Existing Ward/projector reconstruction remains exact, but the missing object is still the explicit `D_s=4`, `mu != 0` two-massive-vector/two-positive-helicity-gluon tree current. Higher-loop/generalized cuts remain downstream.

## Next frontier

1. CI-certify the explicit prime factor map at `532fb5a...` and repair immediately if needed.
2. Build a finite completed prime–Archimedean toy factorization that exposes exactly where the negative explicit-formula prime sign must be cancelled rather than hidden.
3. Push the raised-box Fubini/DCT layer.
4. Continue searching/deriving the massive-vector `++` current before YM sewing.
5. Connect the now-certified all-chamber Wiener–Hopf factor to the arithmetic Archimedean factor candidate, testing whether the same positive spectral weight can supply the missing completion/gluing sector.
