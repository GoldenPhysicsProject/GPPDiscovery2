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