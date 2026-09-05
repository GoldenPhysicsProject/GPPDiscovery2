# Codex/GPT rotation — 2026-09-05 03:26Z

Scope: Codex/GPT track only. No Claude-owned work inspected.

## Verify2 certification

`codex/lean-workbench` head `1f8be68a49ba450887c350585b2186e7f9108a1a` passed full Build #2045 and cold changed-Lean #899. The exact countable quadratic number-gas Massieu/Fisher metric now has a nonnegative quadratic form with zero set exactly the zero tangent vector. This completes the pointwise positive-definite/separation package.

`main` cannot currently be fast-forwarded to this head: GitHub comparison reports the branches diverged, with the workbench ahead by 169 commits and behind main by 5 from their merge base. Reconcile those five main-only commits into the workbench before certified promotion; do not overwrite main.

## Yang–Mills generalized-cut obstruction

Added `discovery/generalized_cuts/presewing_residue_noninjectivity_audit.py`. Exact rational refactorization

`A -> h A`, `B -> B/h`

leaves the sewn product `C=A B` invariant but changes the factorwise residue at an additional propagator. For the explicit family in the audit,

`Res(hA)-Res(A) = lambda (a+1)(a+b)`,

which is generically nonzero; a concrete rational witness is included. Therefore a topology projector requiring factorwise extra-propagator residues cannot factor through the collapsed two-particle sewing alone. Generic Ds4 YM CI #13 passed on `1749c9651faeceb810477a79a8a614830aaa6df9`.

Next amplitude construction: retain the additional uncut denominators on the two generic nonzero-mu tree factors, impose the genuine triple cut, take residues/root sums, then apply the existing Badger T1/T2/T3 subtraction/moment machinery. Only afterward identify box/triangle/bubble master coefficients and lock FDH conventions.

## Prime-gas curvature

Added exact symbolic audit `discovery/number_thermodynamics/quadratic_confinement_curvature_symbolic_identity.py` and CI gate. For centered moments m_k,

`D = det(g) = m2*m4 - m3^2 - m2^3`,

and exact polynomial elimination proves

`det(C) = det(H) - D^2`,

with all mean dependence cancelling. Hence, in the existing curvature convention,

`R = (D^2-det(H))/(2 D^2)`.

The centered H is the degree-3 moment Gram matrix, so `det(H)>=0` together with the now-certified `D>0` yields the rigorous structural target `R<=1/2`. The high-precision discovery audit has stable examples of both curvature signs, so do not assert `R<=0`. Curvature CI #1 passed on `82cbfd2d11c466517368659bc5eec04931d2eb30`.

## Principal-series / Weil / RH source mining

The focused arithmetic principal-series paper continues to identify the exact global boundary as complete monotonicity, equivalently positive Gaussian-semigroup Gram factorization, of the explicit prime+Archimedean heat trace. Its causal Dirichlet-heat construction recovers the complete prime-power von-Mangoldt boundary anomaly, but the off-diagonal commutators retain a non-summable asymptotic Hilbert–Schmidt floor. Thus local Gamma/Wiener–Hopf positivity and the causal prime anomaly do not yet provide the required global prime–Archimedean positive norm square. No RH claim.

## Spectral / chamber status

The arbitrary-c Gamma/Beta chamber target remains unchanged: prove the real-line logistic change of variables in Lean, then Fourier uniqueness for `rho_c` to obtain `hat(rho_c)(t)=sech(t/2)^(2c)` and the convolution semigroup `rho_c*rho_d=rho_(c+d)`. Beta/Gamma algebra is already available; measure-theoretic substitution/Fourier infrastructure remains the formal bottleneck. No Barnes axiom or unsupported Plancherel identification.

## Scalar box

Raised-box regulator endpoint remains closed at `J_epsilon(S,T) -> 1/6`; no regression.
