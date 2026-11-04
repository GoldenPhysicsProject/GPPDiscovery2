# Golden projective map, exact two-sheet unitarity, and the arithmetic selection gap

Date: 2026-11-04  
Project: Golden Physics Project / RHpositive and Unification  
Status: **exact elementary theorems with numerical regressions; not a completed arithmetic intertwiner and not RH**

## Executive finding

The golden transformation `F(x)=1+1/x` can be **exactly conjugated** to multiplication by `-phi^-2`, where `phi=(1+sqrt(5))/2`. In logarithmic coordinates it becomes an equal-step translation `u -> u-2 log(phi)` plus a swap of two orientation sheets. This gives a canonical unitary operator on the two-sheet Hilbert space `L2(R,du) ⊕ L2(R,du)` **for that chosen projective coordinate and invariant Haar measure**.

The construction supplies an exact kinematic model of a repeated fixed golden step. It also supplies a decisive no-go against identifying this step itself as a Hilbert--Polya operator: the step has **no nonzero normalizable eigenvectors**, only continuous translation spectrum. It **commutes with every unweighted prime dilation** on the same log coordinate and therefore cannot, by itself, select zeta's discrete zero ordinates. The same construction exists for every integer shear `F_a(x)=a+1/x`, so unitarity alone does not select `phi`.

This sharpens [GoldenMobiusAudit.lean](https://github.com/GoldenPhysicsProject/GPPVerify/blob/main/GppVerify/RiemannHypothesis/GoldenMobiusAudit.lean) and [GoldenWeylBoundaryWord.lean](https://github.com/GoldenPhysicsProject/GPPVerify/blob/main/GppVerify/RiemannHypothesis/GoldenWeylBoundaryWord.lean), which already prove the algebraic reflection/dual/Krein-feedback golden word but leave its identification with the *completed arithmetic* pole open. This note adds the projective conjugacy, its correct Hilbert-space measure, and the spectral/prime-commutation controls; it makes **no claim of new formal Lean certification** for these additional facts.

## 1. General Möbius conjugacy: proves both the golden case and controls

For a real `a>0`, let

\[
F_a(x)=a+\frac1x,\qquad
\rho_a=\frac{a+\sqrt{a^2+4}}2,\qquad
\psi_a=-\rho_a^{-1}.
\]

These are the two fixed points of `F_a`, satisfying `rho+psi=a` and `rho*psi=-1`. Define the cross-ratio coordinate

\[
C_a(x)=\frac{x-\rho_a}{x-\psi_a}.
\]

**Exact conjugacy theorem.** On the real projective line away from poles and fixed points,

\[
\boxed{C_a(F_a(x))=-\rho_a^{-2}\,C_a(x).}
\]

Proof: since `a-rho=psi`, `a-psi=rho`, `rho*psi=-1`,

\[
C_a(F_a(x))
=\frac{(a-\rho)x+1}{(a-\psi)x+1}
=\frac{\psi(x-\rho)}{\rho(x-\psi)}
=-\rho^{-2}C_a(x).
\]

At `a=1`, `rho=phi`, `psi=-phi^-1`, and

\[
\boxed{C(F(x))=-\varphi^{-2}C(x),\quad
C(x)=\frac{x-\varphi}{x+\varphi^{-1}}.}
\]

This identity is a projective conjugacy, not a coincidence from fitting zeta zeros. For integer shears `a=1,2,3`, independent numerical regressions give positive fixed points `1.61803398875`, `2.41421356237`, `3.30277563773`, multipliers `-0.38196601125`, `-0.17157287525`, `-0.09167308680`, and identity residuals below `1.4e-15` at the seven sampled non-singular points. **Every** such shear is similarly conjugate to a dilation. `a=1` is distinguished only if one independently justifies the primitive unit translation in the relevant physical/arithmetic boundary problem.

## 2. The exact invariant measure and two-sheet unitary operator

In the golden case let `y=C(x)=epsilon*exp(u)` with `epsilon in {+1,-1}` and `u=log|y|`. The preceding theorem becomes

\[
(\epsilon,u)\longmapsto(-\epsilon,u-2\log\varphi).
\]

The multiplicative Haar measure on the two-sign coordinate is `dy/|y| = du` on each sheet. Its pullback to the original real projective coordinate is

\[
\boxed{d\mu_F(x)=\left|\frac{C'(x)}{C(x)}\right|dx
=\frac{\sqrt5\,dx}{|(x-\varphi)(x+\varphi^{-1})|}.}
\]

It is invariant under `F` because `C(F(x))=kappa*C(x)` and `dy/|y|` is invariant under nonzero scaling. The exceptional points are removed up to measure-zero projective endpoints; the measure is infinite near the fixed points. **This is not ordinary Lebesgue measure or the unmodified `dx/x` measure in the original `x` coordinate.**

On the Hilbert space `H=L2(R,du;C2)`, define

\[
\boxed{(U_\varphi\Psi)_\pm(u)=\Psi_\mp(u-2\log\varphi).}
\]

Then `||U_phi Psi||^2=||Psi||^2` by substitution `v=u-2log(phi)` and permutation of sheets. The inverse is a translation by `+2log(phi)` followed by the same swap, so the isometry is surjective: **unitary**. Moreover

\[
U_\varphi^2\Psi_\pm(u)=\Psi_\pm(u-4\log\varphi).
\]

In the Fourier variable `t` this is the matrix symbol

\[
U_\varphi(t)=e^{-2it\log\varphi}\begin{pmatrix}0&1\\1&0\end{pmatrix},
\quad \text{with eigenphases }\pm e^{-2it\log\varphi}.
\]

Their absolute values are one for **every** real `t`. At `t=14.1347251417+0.3i`, formal analytic continuation of the symbol gives modulus approximately `1.334727425`, but those complex `t` functions are not Hilbert-space eigenvectors; this is only a continuation diagnostic, not an RH mechanism.

An independent numerical `L2` check using two unequal complex/noncomplex Gaussian profiles gives `||Psi||²=3.467460714142106` before and after a step, agreeing to the printed double precision.

## 3. Exact no-point-spectrum theorem

**Theorem.** `U_phi` has no nonzero eigenvectors in `L2(R,du;C2)`.

**Proof.** If `U_phi Psi=lambda Psi` with `Psi!=0`, unitarity gives `|lambda|=1`. Applying `U_phi` twice gives `T_{-4log(phi)} Psi=lambda² Psi`. Thus each component `f` has `|f(u-4log(phi))|=|f(u)|` almost everywhere. Let `L=4log(phi)>0`. The integrals of `|f|²` over every translate of any fundamental interval `[0,L)` are equal. If this common integral is positive, summing over all integer translates forces the full `L2` norm to be infinite. If it is zero, `f=0` almost everywhere. Therefore both components vanish, a contradiction. QED.

This is a **direct obstruction** to taking the bare golden unitary step as a self-adjoint/point-spectrum generator whose eigenvalues are zeta zero ordinates. It is not a statement that no further arithmetic interaction or boundary condition can create bound states.

## 4. Prime dilations commute with the bare golden step

Define the natural unweighted prime scale action on the same log Hilbert space by

\[
(V_p\Psi)_\pm(u)=\Psi_\pm(u+\log p).
\]

Both `U_phi` and `V_p` consist only of translation and a constant orientation swap; therefore

\[
\boxed{[U_\varphi,V_p]=0\quad\text{for every prime }p.}
\]

The Fourier symbols are `U_phi(t)=exp(-2itlog(phi))*sigma_x` and `V_p(t)=exp(itlog(p))*I`, so all real `t` are permitted by these kinematic unitaries. Numerically checked on two test profiles for `p=2,3,5,7`, with sample residuals below `2e-15`; the general identity is elementary exact algebra.

Hence **a collection of unweighted scale shifts, even all primes, does not by itself quantize `t`.** A phase-sensitive arithmetic interaction, nontrivial boundary condition, or positive spectral constraint would have to supply discrete selection. The off-line shifted-xi false control also supports this: the same kinematic unitary exists independently of whether a tested entire function satisfies RH.

## 5. Holomorphic/Herglotz caveat

The real map `F_a(z)=a+1/z` has

\[
\operatorname{Im}F_a(z)=-\frac{\operatorname{Im}z}{|z|^2}.
\]

It reverses the complex upper and lower half-planes. Unitarity of its **real-boundary** half-density representation therefore does **not** imply preservation of a physical Herglotz Weyl function or Osterwalder--Schrader reflection positivity. The existing `GoldenWeylBoundaryWord.lean` carefully includes spectral reflection plus opposite-boundary duality and normalized Krein feedback. Identifying the complete arithmetic pole with that feedback remains open, particularly in light of the certified infinite-negative-index raw-Weil additive OS-reflection no-go.

## 6. Exact golden prime-five amplitude, but no zero selector

The independently defined finite-place shadow kernel on the critical line is

\[
K_{p,1}(1/2+it)=\frac{1-p^{-1}}
{|1-p^{-1/2-it}|^2},
\]

the standard positive Poisson kernel of the unit disk with radial parameter `r=p^-1/2` and boundary angle `theta=t log p`. At `p=5`,

\[
\boxed{K_{5,1}(1/2+it)=\frac2{3-\sqrt5\cos(t\log5)},\quad
\varphi^{-2}\le K_{5,1}\le\varphi^2.}
\]

The associated hyperbolic parameter is `atanh(5^-1/2)=log(phi)`; at `t=0`, the value equals `phi²` exactly, matching the trace-three/discriminant-five modular sector in [GoldenRatioHyperbolicSector.lean](https://github.com/GoldenPhysicsProject/GPPVerify/blob/main/GppVerify/NumberTheory/GoldenRatioHyperbolicSector.lean). However `K_{5,1}>0` for every real `t`: it has **no zero ordinate selector** on its own. This reinforces the all-prime/Archimedean phase requirement.

## 7. Acceptance test for a physical arithmetic-to-celestial golden flow

1. **Canonical identification:** prove the physical completed arithmetic pole acts on the genuine normalized Suzuki Weyl coordinate by the precise unit Krein feedback, with domains and regularization. Avoid swapping the raw projective `A/B` for the physical Weyl function (already ruled out in Lean at the normalization point).
2. **Completed signed arithmetic input:** include all primes, the Archimedean gamma contact, divergent counterterm, and indefinite pole through a faithful intertwiner. The raw Weil distribution cannot itself be a positive OS covariance.
3. **Actual spectral selection:** construct a self-adjoint/positive completed boundary object with discrete zero ordinates (or a characteristic determinant), since the bare golden `U_phi` has no `L2` eigenvalues and commutes with scale shifts.
4. **Adversarial rejection:** run unchanged against `xi(s-theta)xi(s+theta)`, Davenport--Heilbronn, and the `n=2` theta-weight deformation which moves a pair of zeros into the critical strip off the line while retaining reflection symmetry.
5. **Independent formal verification:** add the cross-ratio conjugacy, invariant-measure unitary lift, prime commutation, and no-point-spectrum lemma to GPPVerify after a local/CI Lean build. Existing modules prove the starting golden word but not these Hilbert-space statements.

Reproduction: `experiments/golden_unitary_conjugacy_probe.py` on `codex/discovery-workbench` (NumPy/SciPy). Algebraic theorems above need no floating-point assumptions. **RH remains open.**
