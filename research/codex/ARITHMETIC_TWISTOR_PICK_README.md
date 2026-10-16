# Arithmetic twistor line and Pick-kernel laboratory

This is the reproducible, exact-symbolic / high-precision-numerical companion to the GPP-bridge Codex note
`work/codex/2026-10-16_arithmetic_twistor_null_line_shadow_quotient_signed_pick_kernel.md`.

Run:
```sh
python research/codex/arithmetic_twistor_null_line_pick_20261016.py
```

**Mathematical content.** Daniel's Cayley coordinate w=(s−1)/s sits on a *fixed complex twistor line* x_ar=−i σ₃/2. With π=(1,w), ω=σ₃π/2 and the usual SU(2,2)-signature twistor pairing H=ω†π+π†ω, the exact equation is H=1−|w|²=(2Re s−1)/|s|². The anti-linear mirror J(ω,π)=(-σ₁overlineω,σ₁overlineπ) fixes the complex line, exchanges positive/negative H, and maps w↦1/overline w. The holomorphic functional shadow w↦1/w fixes u=[(1+w)/(2(1−w))]², a quotient coordinate on which the critical circle becomes u≤0.

The completed arithmetic amplitude f(u)=ξ(½+√u)/ξ(½) is single-valued because ξ(½+z) is even. Its logarithmic derivative m(u)=f′(u)/f(u) is a Stieltjes function and the associated Pick kernel is positive **if and only if RH**. This is a rigorous RH criterion, NOT an independent proof of the necessary positivity. The true prime+gamma+pole formula for m and its Laplace transform from Suzuki's signed arithmetic scalar are derived in the private note.

The script checks projective twistor equations **symbolically** and examines the Pick kernel at three finite upper-half-plane points numerically. As a negative control it demonstrates that the fake Fθ(s)=ξ(s−θ)ξ(s+θ) has a pole in the upper u-plane and violates anti-Herglotz, despite satisfying the same twistor mirror symmetries. Finite numerical eigenvalues are NOT rigorous interval certificates; shifted fake failure has an independent exact pole argument.

**Next RH-strength task:** Derive a zero-independent positive operator/GNS realization of m(u), with the true signed Euler, Archimedean and polar coefficients. Neither twistor geometry, generic causal fermion spectral action nor principal-series terminology can substitute for that noncircular construction.

## October 16: exact positive-sheet higher-order falsifier

Run `python research/codex/twistor_confluent_hankel_exact_falsifier.py`. For the positive two-mode fake `F_5(z)=cosh(2z)+5cosh(z)`, both the first Fisher/Turan sign `h1=13/48>0` and the adjacent 2x2 Hankel minor `1649/19353600>0` pass. But the nonconsecutive derivative-order minor `h1*h5-h3^2=-7159067/214592716800<0` and the 3x3 Hankel determinant are strictly negative, with an exact rational negative vector. Every coefficient is checked with Fraction formal series division and no zero-location input. This identifies the missing OFF-DIAGONAL real positive-sheet Loewner/Pick positivity condition. The actual xi infinite matrix positivity is still unproved, and RH is OPEN. Details: GPP-bridge `work/codex/2026-10-16_twistor_positive_sheet_confluent_hankel_falsifier.md` and GPPVerify PR #377 (draft Lean arithmetic).


### Actual xi finite Hankel coercivity (unconditional, but finite)

The follow-up exact rational scripts `twistor_xi_hankel3_tail_bound.py` and `twistor_xi_hankel5_rational_bound.py` combine *published* Platt--Trudgian RH verification for zeros through height `3e12`, standard certified first-five zero brackets and Rosser's explicit zero counting to prove strict positivity of the actual xi log-derivative Hankel matrices H3, H4 and H5. In particular the final interval algebra gives `H3 > 1e-23 I`, `H4 > 1e-24 I`, `H5 > 4e-32 I`. The second script uses exact Lagrange interpolation bounds for the low-zero Vandermonde inverse and a rigorously controlled **arbitrary high-zero off-axis tail**. No RH assumption is made above the verified height. Only the numerical rational inequalities are checked by these scripts; the published analytic inputs and infinite Hadamard bridge are not formalized in Lean. **No claim of positivity at every matrix size, no RH or GRH proof.** See the corresponding private bridge note for the full derivation.
