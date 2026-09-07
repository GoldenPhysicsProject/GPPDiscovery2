# Drive mining delta — 2026-09-07

## Scope and promotion rule

This pass treats the Drive as a chronological archive, not an authority. Older physical identifications are retained only when their mathematical content survives later corrections and independent checking. The principal new delta is a precise separation between the celestial spectral weight and the arithmetic Suzuki/Weil screw kernel.

## 1. Spectral-weight chronology: exact screw function, false direct zeta identification

The archive note `rh_screw_kernel_status.md` starts from

\[
P(\lambda)=\frac{\pi\lambda}{\sinh(\pi\lambda)}
\]

and defines

\[
g_P(t)=\int_{\mathbb R}\frac{\cos(\lambda t)-1}{\lambda^2}P(\lambda)\,d\lambda.
\]

Using the already-established Fourier transform

\[
\int_{\mathbb R}e^{i\lambda t}P(\lambda)\,d\lambda
=\frac{\pi}{2}\operatorname{sech}^2(t/2),
\]

one gets, under the same Fourier normalization,

\[
g_P''(t)=-\frac{\pi}{2}\operatorname{sech}^2(t/2).
\]

With `g_P(0)=g_P'(0)=0`, direct integration gives

\[
\boxed{g_P(t)=-2\pi\log\cosh(t/2)}.
\]

Independent check: differentiating the closed form gives

\[
g_P'(t)=-\pi\tanh(t/2),\qquad
g_P''(t)=-\frac{\pi}{2}\operatorname{sech}^2(t/2),
\]

so the closed form is exact once the Fourier-transform identity is fixed.

The same archive note numerically tests the stronger conjecture that this kernel is a rescaling of Suzuki's zeta screw kernel and reports large residuals. Therefore the direct identification

\[
K_{\mathrm{Weil}}=cK_P
\]

must be treated as falsified, not as an RH bridge.

### Formal consequence

Verify2 already formalizes the same hyperbolic spectral weight

\[
P(\lambda)=\frac{\pi\lambda}{\sinh(\pi\lambda)}
\]

under the name `wienerHopfWeight`, plus exact shifted-sech convolution identities. It does not currently formalize `g_P`, its log-cosh closed form, or a Suzuki screw comparison. A clean low-risk target is therefore:

1. define the continuous extension of `wienerHopfWeight` at `lambda=0` rather than relying on totalized division;
2. formalize the elementary ODE/primitive statement that any twice-differentiable `g` with
   `g''(t)=-(pi/2) sech(t/2)^2`, `g(0)=g'(0)=0` equals `-2*pi*log(cosh(t/2))`;
3. keep any arithmetic Suzuki/Weil identification outside the theorem statement.

This is a real spectral-weight/RH connection, but a negative one: the celestial cut weight supplies a canonical comparison kernel, not the completed arithmetic kernel itself.

## 2. RH positivity chronology: positivity appears only after prime–Archimedean completion

The same status note decomposes Suzuki's arithmetic screw function as

\[
g=g_\infty+g_{\mathrm{prime}},
\]

with

\[
g_{\mathrm{prime}}(t)=
\sum_{\log n\le |t|}
\frac{\Lambda(n)}{\sqrt n}(|t|-\log n).
\]

Its finite-grid tests found both `K_infty` and `K_prime` strongly indefinite while their completed sum was numerically positive semidefinite on the tested grids. Numerical tests are not proofs, so only the structural warning is promoted:

> Do not seek RH by proving positivity of the prime contribution or the Archimedean contribution separately. The viable object is the completed prime–Archimedean form.

This aligns with the later causal heat-trace program: prime-power atoms can be transformed exactly into Fourier/Dirichlet and heat-boundary representations, but positivity must be sought only after the Archimedean completion is incorporated.

Thus the strongest safe form of the arithmetic wave-particle picture is now

\[
\text{prime-power atoms}
\longleftrightarrow
\text{Dirichlet/Fourier modes}
\longleftrightarrow
\text{causal heat response},
\]

followed by a separate unresolved completion step

\[
\text{prime part}+\text{Archimedean part}
\longrightarrow
\text{positive spectral/Weil object}.
\]

The final arrow remains RH-level mathematics.

## 3. Relation to the celestial-cut / scale-invariant thread

The spectral weight used above is the same hyperbolic factor that survives the corrected celestial two-particle cut chronology. Therefore a real exact cross-front bridge exists:

\[
\text{celestial cut weight }P(\lambda)
\longrightarrow
\text{Fourier }\operatorname{sech}^2
\longrightarrow
\text{log-cosh screw }g_P.
\]

But chronology now forbids appending

\[
g_P=\text{Suzuki zeta screw}
\]

or

\[
P=\text{Weil spectral measure}.
\]

The cut factor remains a derived celestial spectral weight. Its occurrence in an exact positive-type/screw construction is mathematically interesting but is not an RH proof and does not replace the prime–Archimedean explicit formula.

## 4. Scaled versus scale invariant

No new correction displaced the surviving rule from the July/August layers:

- scale covariance means a quantity transforms homogeneously under a common rescaling;
- scale invariance means the net homogeneity degree is zero;
- for the two-particle celestial cut this occurs at `Delta_5 + Delta_6 = 2` because the explicit mass-scale exponent vanishes;
- the half-density factor in weighted Mellin inversion is a Jacobian correction and becomes plain inversion after conjugation to multiplicative Haar space.

These are exact analytic statements and should remain separated from broader physical claims that all absolute mass scales are unobservable.

## 5. Orientation / googly / zitterbewegung status unchanged by this pass

No archive item found today overturns the corrected separation:

- celestial shadow flips `(Delta,J)` as `(2-Delta,-J)`;
- Wigner time reversal reverses momentum and spin together and therefore preserves helicity;
- worldline orientation reversal is distinct from Wigner `T`;
- representation dualization and path reversal obey the Wilson-line identity `W_{R*}(gamma)=W_R(gamma^{-1})`;
- in the Abelian sign reduction, charge sign and worldline orientation enter through the product `ct`;
- Grassmannian orientation has a genuine `Z4` structure where separately proved;
- zitterbewegung retains the exact frequency `omega_Z=2mc^2/hbar` but does not by itself identify the negative-energy component with a cosmological shadow sheet.

No physical equality among these operations should be promoted without an additional equivariant theorem.

## 6. Boson/fermion and gauge hierarchy status unchanged

No nontrivial `SU(1)` construction appeared. `SU(1)` is trivial. The safe gauge labels remain `U(1)`, `SU(2)`, `SU(3)`, while exceptional stabilizer chains such as

\[
G_2\supset SU(3)\supset S(U(2)\times U(1))
\]

are separate structures and do not themselves derive the Standard Model direct product.

Spinorial `4pi` closure, Grassmannian `Z4`, and exact representation-theoretic identities remain legitimate mathematical parallels, but `fermion = half a boson` is not a theorem and should not be used as ontology.

## 7. Stub/axiom reduction consequences

Today's archive comparison does not justify deleting an additional RH theorem stub: the Suzuki/Weil positivity step is genuinely the hard theorem. It does, however, sharpen what must *not* become an axiom/stub:

- no axiom `P = Weil measure`;
- no axiom `g_P = Suzuki screw`;
- no prime-only positivity axiom;
- no Archimedean-only positivity axiom.

The correct formal decomposition is to prove the celestial `P -> sech^2 -> logcosh` chain independently, prove exact prime/heat identities independently, and leave only the completed prime–Archimedean positivity/operator factorization as the RH-level gap.

## 8. Upgradeability / formal-tree note

Current Verify2 contains `MehlerFockSpectralWeight.lean` and `SechConvolutionWienerHopf.lean`; their theorem statements are elementary hyperbolic algebra and are appropriately narrower than the old physical interpretation. A future formal `g_P` module should import these exact constructions rather than duplicate the spectral-weight definition, and should define the removable value at the origin explicitly to avoid dependence on Lean's totalized division convention.

## Promotion ledger

**Promote:**

- the exact log-cosh primitive associated with the celestial spectral weight;
- the distinction between the canonical celestial screw kernel and Suzuki's arithmetic screw kernel;
- the requirement that RH positivity be sought at the completed prime–Archimedean level;
- the existing arithmetic atom/Fourier/heat transform chain.

**Do not promote:**

- direct `QG/celestial kernel = Weil kernel` claims;
- positivity inferred from finite numerical grids;
- prime-only or Archimedean-only RH positivity;
- any revived `shadow = T`, `SU(1)` gauge, or zitterbewegung-cosmology equality unsupported by a separate theorem.
