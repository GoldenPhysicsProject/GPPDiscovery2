# H¹ continuity and cofinal-support reduction for the exact semilocal Weil matrices

2026-10-29 · Codex / GPPDiscovery2 · analytical workbench note, not an RH proof.

## Source and exact matrix

Daniel Toupin, `arithmetic_principal_series_RH_program-34.tex`, section *The exact semilocal Weil form*. Fix λ>1 and L=2log λ. On [0,L] the orthonormal modes are

`U_n(x)=L^{-1/2} exp(2πinx/L)`.

For f∈H¹([0,L];ℂ), define the one-sided autocorrelation for 0≤y≤L:

`R_f(y)=∫₀^(L−y) f(x+y) conjugate(f(x)) dx`,
`q_f(y)=2 Re R_f(y)`; set q_f(y)=0 for y>L.

For f=U_n the diagonal q_f is `2(1−y/L) cos(2πny/L)`. For a pair (U_m,U_n), the Hermitian polarization gives the real symmetric offdiagonal kernel

`q_mn(y)=[sin(2πmy/L)−sin(2πny/L)]/[π(n−m)]` for m≠n.

Consequently for any finite Fourier polynomial `f=Σ_|n|≤N c_n U_n`, the completed Weil form evaluated on q_f coincides with `c* Q_(λ,N) c` for the actual semilocal matrix of v34, with the full pole, Archimedean and finite prime-power terms. In particular full-matrix positivity includes ALL cross-scale couplings and does not require a Gershgorin condition.

## Concrete H¹ endpoint estimate

For every f∈H¹([0,L]) and 0≤y≤L,

`R_f(y)−R_f(0)
 =∫₀^(L−y) [f(x+y)−f(x)] conjugate(f(x))dx − ∫_(L−y)^L |f(x)|²dx`.

The one-dimensional H¹ translation inequality (valid for the overlap interval) and Cauchy–Schwarz give

`||f(·+y)−f(·)||_(L²(0,L−y)) ≤ y ||f'||₂`,

hence

`|q_f(y)−q_f(0)| ≤ 2y ( ||f'||₂ ||f||₂ + ||f||_∞² )`. (1)

The 1D Sobolev embedding `H¹([0,L])↪C([0,L])` bounds the right-hand side by `C_L y ||f||_(H¹)²`, where C_L is explicit and finite for each fixed L. Polarizing the same estimate yields a locally bounded bilinear control and continuity under H¹ convergence:

`||f_k−f||_(H¹)→0` implies uniform control of `[q_(f_k)(y)−q_(f_k)(0)]/y` and convergence of these quotients in L∞(0,L) (with a suitable cross-term estimate).

In the Archimedean distribution, the potentially singular integrand is `[e^(y/2)q_f(y)−q_f(0)]/[2sinh y]`; (1) plus `e^(y/2)−1=O(y)` makes it integrably bounded and continuous in f under H¹ convergence. The Archimedean tail for y>L is the exact term `−q_f(0)atanh(e^(−L))`, also H¹-continuous; this tail must not be dropped. The pole term is a finite weighted integral on [0,L], and for each fixed λ only finitely many prime powers p^r≤e^L are sampled, each q_f(r log p) being continuous in f already in L². Therefore the **completed semilocal quadratic functional extends continuously to H¹([0,L])** for each fixed L, given the exact v34 distribution formula.

This is a standard analytic argument that should be written as an explicit lemma with constants and then formalized, independently of any spectral/RH claim. It addresses the form-continuity half of support extension and avoids operator-norm Galerkin convergence.

## Conditional dense-extension theorem

Fix λ and suppose **for every integer N≥0** the exact completed matrix `Q_(λ,N)` is PSD. Let f be any smooth function compactly supported strictly inside (0,L). Its periodic extension is smooth; symmetric Fourier partial sums `f_N` converge to f in H¹([0,L]) (indeed in every periodic Sobolev norm). Each finite f_N obeys `Ψ♯(q_(f_N))=c_N*Q_(λ,N)c_N ≥0`. H¹ continuity then gives `Ψ♯(q_f)=lim_N Ψ♯(q_(f_N)) ≥0`.

No uniform eigenvalue gap `λ_min(Q_(λ,N))≥ε` and no operator-norm convergence of compressions is required. Every cross term is already inside Q_N. Note the zero extension of individual periodic modes has endpoint jumps, but the overlap-autocorrelation formula and the H¹ **interval** topology handle them directly; do not assume the zero extensions lie in H¹(ℝ).

A **cofinal sequence of supports suffices**: choose λ_k=2^k, k≥1. Every compactly supported test lies strictly inside [λ_k^−1,λ_k] for sufficiently large k. Consequently, all-N positivity of the semilocal matrices at λ_k for every k, plus the above continuity/identification, would imply the global Weil positivity criterion. Uniform-in-λ error estimates are not necessary for this logical implication.

## Still open, explicitly

1. A proof that Q_(λ_k,N)≥0 for **all** k,N (the analytic arithmetic problem equivalent in strength to the global RH target). Arb checks through N=64 at λ=5/2 and N=32 on several dyadic scales do not give this.
2. Full documentation of the test-function normalization, complex polarization and the equivalence between Ψ♯(q_f) and the exact Weil criterion's admissible dense class. No jump in these bridges may be assumed.
3. If formalizing in Lean, first prove the interval autocorrelation/H¹ bound and the finite-matrix polarization theorem, then the closedness-of-the-positive-cone limit theorem. None of these should be encoded as an axiom.

## Certified finite diagnostics (160-bit FLINT/Arb)

At λ=5/2, N64 (129 modes), all LDL pivots strictly positive, with `0.260089 < 1+λ_min(T) < 0.260094` certified by shifted LDL and rational Rayleigh witness. Dyadic λ=2, N32 (65 modes) gap (0.261656,0.261661); λ=4,N32 gap (0.239675,0.239680); λ=8,N32 gap (0.308723,0.308728); λ=16,N32 gap (0.330676,0.330681). Each checked matrix was certified positive definite. These are finite observations, not the all-N claim.

Code: `discovery/arb_semilocal_weil_matrix.py`, `discovery/arb_one_sided_spectrum_sweep.py` on `codex/discovery-workbench`. Rigorous CI green through the earlier 129-mode sweep; extended workflow remains a separate gate.
