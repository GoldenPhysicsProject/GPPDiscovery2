# 2026-11-18 — Nieto/Hopf equator, Round14D quotient topology and conditional Weil no-gap theorem

Audited J.A. Nieto, *Division-algebras/Poincaré-conjecture correspondence*, arXiv:1303.2673, GPPDiscovery5 Round14D (7e89769) and existing WWIF/no-ghost Lean modules. These are exact geometric/spectral results; **not RH or gravitational dynamics**.

## 1. Exact quaternionic double and equal-weight equator

For u,v∈H with |u|²+|v|²=1, h:S⁷→S⁴⊂H⊕R,
h(u,v)=(2u\bar v, |u|²−|v|²). Its norm is one and it is invariant under the complete right Sp(1) action (u,v)↦(ua,va), |a|=1. The ± simultaneous sign is only one element of this S³ fiber, not automatically physical CPT. The equator h₅=0 ⇔ |u|²=|v|²=1/2. Its image is exactly unit-quaternion S³. Hence the spatial S³ equator and two exact **geometric** half weights occur in the same construction. The 'two bulks' are two 4-balls glued along S³, not extra microscopic degrees of freedom; 1/2 norm is not yet Born probability.

The round Euclidean S⁴ metric ds²=ℓ²(dχ²+sin²χ dΩ₃²), χ=π/2+i t/ℓ, analytically continues to ds_L²=−dt²+ℓ²cosh²(t/ℓ)dΩ₃², global de Sitter with Λ=3/ℓ². The opposite sign −it is the opposite continuation orientation, the SAME Lorentzian metric. This is a selected Wick/real-structure continuation, not the claim that Euclidean S⁴ automatically has Lorentzian signature. Nieto's Cartan-Schouten S³ torsion T±=±ε/ℓ gives equal Ricci 2g/ℓ²; his general 'every parallelizable M³ implies Ric=T²' needs extra skew-torsion/flat metric-compatible connection assumptions (orientable hyperbolic 3-manifolds are parallelizable but have Ric<0). Ricci flow does not turn arbitrary topology into S³.

Independent direct algebra/code test: 500 random quaternion pairs checked S⁷→S⁴ image, Sp(1) fiber, ± symmetry and S³ equator to 7.1e−16; ε contractions give 2δ_ab.

## 2. Euler/Tate two faces, and why quotient norm is the main issue

Round14D correctly exhibits one Tate theta adelic object with Poisson/integer face and Mellin/Euler face. The E_F map's Mellin transform is F(s)Ĥ(s), hence formally annihilates the zero-side pairing against any admissible test (requires full extension beyond compact test domain). This holds for the fakes too. Its ordinary positive Plancherel norm |F|² is NOT the Weil form.

**New exact topological obstruction:** If F∈L∞(R) is nonzero a.e., then M_F on L²(R) has dense image: (ran M_F)^⊥=ker M_{\bar F}=0. Since Xi(t)=ξ(1/2+it) is bounded with isolated zero set, the unweighted quotient L²/closure(ran M_Xi) is zero. Thus Round14D's shorthand 'quotient L²(C_Q)/closure E' cannot be the nontrivial zero-spectrum Connes space without the *specified weighted/Sobolev domain*. Connes (1999) uses weighted L²_δ in the spectral-realization construction. Numerical removal of truncated E directions without a stable topology can produce an artificial apparent positive gap.

## 3. The conditional Weil no-uniform-L²-gap theorem

Assume RH, hence for completed Weil pairing on C_c∞(R) W(g)=Σ_γ m_γ |ĝ(γ)|². Let φ∈C_c∞(−1,1) be real, ||φ||₂=1, and g_L(u)=L^(−1/2)φ(u/L). Then ||g_L||₂=1 and ĝ_L(γ)=√L φ̂(Lγ). Since ξ(1/2)≠0, there is a positive gap between γ=0 and every zero ordinate. For arbitrary integer m≥2, Schwartz decay and the Riemann–von Mangoldt count imply

W(g_L)≤C_m² L^(1−2m) Σ_γ m_γ |γ|^(−2m)→0.

**Therefore RH itself rules out a global c>0 in W(g)≥c||g||²_{L²}.** This does not refute a lower bound with respect to a suitably defined independent **quotient** norm, but it demonstrates that demanding an L-uniform raw-gap is the wrong test.

## 4. Revised executable Round14E target

Specify the ambient weighted Connes/Hardy/Burnol boundary completion and domain of actual signed completed W. Compute the closure R_F=closure(range E_F) in THAT topology; check nontriviality and numerical convergence. Quantify principal angles of tiny Galerkin modes relative to projected R_F across L,N; check how negative *indices* survive in the quotient, rather than a raw L² gap. Run each of ζ, shifted Fθ, EPS, DH with its OWN full explicit formula and pole/gamma factors. Obtain a genuine zero-independent all-prime global no-ghost energy identity before arguing physical spectral completeness. The quaternionic Hopf quotient is positive for **every** F and cannot by itself distinguish zeta from fakes. The arithmetic no-ghost/RH theorem remains OPEN.

Source exact numerics: local companion verify_hopf_no_gap_2026_11_18.py executed PASS. No user manuscripts edited.


## 5. Further exact obstruction: radical quotient preserves ghosts

Let W be a Hermitian form and R=rad W={r : W(r,y)=0 for all y}. The quotient form on V/R is well defined; negative vectors map to negative classes because W(x,x)<0 implies x∉R. Conversely negative classes have negative representatives. Thus taking a quotient by the **true radical** preserves the positive/negative inertia, removing only null directions. In finite dimension this is exactly Sylvester inertia with the radical split off.

Therefore testing whether an Fθ/EPS/DH negative mode survives quotienting by its OWN E_F radical has a **tautologically affirmative** answer. It is not a useful new discriminator. Numerically projecting away an approximate E_F span can change signs only because of truncation/domain errors or because the projected span is not the true radical. The real RH target remains a zero-independent arithmetic energy/sum-of-squares proof of Wζ>=0 and faithful spectral completeness, not 'removing ghosts' by quotienting a null subspace. This correction supersedes item 4 of the revised Round14E test above.
