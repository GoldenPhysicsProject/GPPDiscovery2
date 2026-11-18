# 2026-11-18 — Prime logarithmic gauge is universally ghost-free but blind; Hardy analyticity sees the zeros

Read: GPPVerify/RiemannHypothesis/DirichletLogGaugeIdentity.lean (exact Möbius gauge), PrimeExcessDelay.lean (prime-unitary Blaschke delay, indefinite subtraction), Connes–Consani 2023 ζ-cycles, GPPDiscovery5 Round14D, GPPDiscovery2 Hardy/Nyman–Burnol notes and the 2026-11-18 logarithmic circle/holonomy companion. This is a new exact synthesis, NOT RH.

## 1. A full-prime positive gauge connection can be made globally and is still fake-blind

For σ>1 put Zσ(t)=ζ(σ+it), nonzero and bounded above/below by constants from its absolutely convergent Euler product. Define
  Hσ^Z = L²(R, |Zσ(t)|²dt),
  Uσ:Hσ^Z→L²(R,dt), Uσ f(t)=Zσ(t)f(t).
Uσ is unitary. On domain {f:Zσ f∈H¹(R)} define the transported free momentum
  Dσ=Uσ^{-1}(−i∂t)Uσ.
It is selfadjoint in the POSITIVE weighted Hilbert space, spectrum R and no point eigenvalues. On smooth vectors,
  Dσ=−i∂t+ζ'(σ+it)/ζ(σ+it)
     =−i∂t − Σ_{n≥2}Λ(n)n^{−σ}e^{−it log n}.
The final series converges absolutely for σ>1. This gives an exact all-prime logarithmic *connection* on the spectral variable t, with prime charges Λ and scale shifts log n, and a conserved positive norm. The logarithmic Dirichlet gauge identity from GPPVerify is its arithmetic-convolution analogue: μ*D(ζ*f)=Df+Λ*f.

**But:** it is a pure gauge. Its physical spectrum is that of −i∂t, NOT zeta zeros, and the positive norm is ||ζ f||², NOT the signed completed Weil form. The same construction works for every meromorphic/analytic F nonzero a.e. on a line, including shifted fakes. Thus prime Euler structure plus a positive weighted conjugation does not prove no ghosts for the true Weil form.

Even if Zσ has isolated zeros on the line (as it does at the critical line), the abstract weighted space Hσ^Z and Uσ remain unitary onto ordinary L²: multiplication by Z is invertible **almost everywhere**, and g/Z is allowed in the weighted space. Thus ordinary L² does not register isolated zero positions through this construction. The formal ζ'/ζ differential expression can acquire singularities; defining the operator by the transported DOMAIN maintains the exact unitary equivalence and illustrates that singularities alone do not guarantee bound-state spectra.

## 2. The exact topology change where interior zeros become visible

On the disk Hardy space H²(D), an inner Blaschke factor
  B_a(z)=(z−a)/(1−conj(a)z), |a|<1
has |B_a(e^{iθ})|=1 almost everywhere. Therefore multiplication M_B is UNITARY on full boundary L²(S¹). But M_B:H²(D)→H²(D) is only an ISOMETRY, not onto. Its image B H² has codimension one. Orthogonal complement is K_B=span{k_a}, k_a(z)=1/(1−conj(a)z).

The normalized reproducing vector is k_a/||k_a||, ||k_a||²=1/(1−|a|²), and
  ||P_{K_B}1||² = 1−|a|².
This follows by the reproducing identity <1,k_a>=1.

For multiple zeros with Blaschke product B, the same formula is ||P_{K_B}1||²=1−|B(0)|², and K_B=0 iff B is constant. The Cayley coordinate a=(ρ−1)/ρ maps a hypothetical zero with Reρ>1/2 to |a|<1, yielding
  1−|a|²=(2Reρ−1)/|ρ|²>0.
This is the existing Nyman–Burnol obstruction and it is global. The new synthesis is **why** the ordinary positive boundary norm was blind while the analytic Hardy constraint is not: analytic continuation and point-evaluation continuity forbid treating the inverse 1/B as an admissible Hardy function, although it is a perfectly valid boundary L² multiplier.

Crucial caveat: positivity of Hardy H² is automatic for any B and any shifted fake. The RH-bearing property is the absence of the model-space defect (B constant), not ambient positivity. Proving it independently from prime/theta arithmetic remains open.

## 3. The properly aligned Euler target

The three faces are (i) Tate–Poisson integer/theta arithmetic; (ii) Euler–Möbius logarithmic prime gauge; (iii) an **analytic** Hilbert completion with a faithful zero-spectrum obstruction and the ACTUAL completed signed Weil form.

Two tempting false closures are now ruled out rigorously:
  - merely weighting L² by |ζ|² gives selfadjoint pure gauge even for fakes and never produces zeta zero eigenvalues;
  - merely restricting to a positive Hardy space gives positive norm even when the inner factor B is nonconstant and its ghost/cohomology model space K_B≠0.

A valid global no-ghost theorem must establish the arithmetic **sewing identity** that forces K_B=0 or full Weil positivity, not by assuming point evaluation at every zero is a unitary state. The shifted Fθ control must fail that genuinely arithmetic identity. The opposite-face WWIF holonomy lemma in the companion note correctly says J-unitary mirror balance is insufficient; a positive conserved metric on a **faithful all-zero monodromy space** would suffice, but that metric/domain has not been constructed.

## 4. Useful implication for the research strategy

Rather than asking for uniform raw Weil spectral gaps, identify the exact analytic topology of the Tate/Connes periodized map where boundary point evaluation is continuous and prime Euler convolution is closable. Look for a zero-independent estimate controlling the Hardy cokernel projection P_{K_B}, such as a directly derived contraction |B(0)|=1 from prime/theta data. This is equivalent to RH and is not yet available. A trace identity built on L² alone cannot do it because the L² multiplier theorem erases isolated zeros.

The operator Dσ acts on the *spectral ordinate t* dual to logarithmic scale u; it is NOT the same as the log-circle spatial generator D_log constructed in the companion note. Avoid conflating these variables.

All displayed claims are elementary exact operator/Hardy statements or already Lean formalized arithmetic-convolution identities. No numerical experiment or Lean compilation is needed for their validity; an independent audit should check the domains and the Hardy projection identity.
