# OB-6 single-cutoff theorem: the **prime cutoff** quantifier does not eliminate the **support width** quantifier

**2026-11-17, Discovery2 source audit. Critical campaign correction for independent Turbo review.** No changes to GPPVerify. This note examines actual theorem statements at the current GitHub \`GPPVerify/main\`, not their narrative summaries. It identifies a missing logical bridge in the 2026-11-17 campaign order; it does not challenge the kernel-checked theorems or the mathematical possibility of proving RH by a Schur enclosure.

## 1. The source declarations and their quantifiers

[ShiftPresentation.lean](https://github.com/GoldenPhysicsProject/GPPVerify/blob/main/GppVerify/RiemannHypothesis/ShiftPresentation.lean), source blob SHA \`ccb259c60800d24df5c251bced6ceb24fcbfb472\`, says:

\`\`\`lean
def OB6At (L : ℝ) : Prop :=
  ∀ g : ℝ → ℝ, ContDiff ℝ ∞ g → HasCompactSupport g →
    (∀ y : ℝ, L / 2 < |y| → g y = 0) →
    ∀ N : ℕ, L < Real.log (N + 1) →
      shiftGramSum N g ≤ poleTerm (autocorr g)
        + archimedeanTerm (autocorr g) + massDefectSum N g

def OB6 : Prop := ∀ L : ℝ, OB6At L

theorem arp_iff_ob6 :
  ArithmeticReflectionPositivity ↔ OB6 := ...
\`\`\`

[TwoSpaceForm.lean](https://github.com/GoldenPhysicsProject/GPPVerify/blob/main/GppVerify/RiemannHypothesis/TwoSpaceForm.lean), source blob SHA \`2c9709905aa3fdf92b7c2c6d43a136aae032c24b\`, says (eliding only the standard test-space premises):

\`\`\`lean
theorem ob6At_iff_single_cutoff (L : ℝ) (N₀ : ℕ)
    (hN₀ : L < Real.log (N₀ + 1)) :
  OB6At L ↔ ∀ g : ℝ → ℝ, ...,
       (∀ y : ℝ, L / 2 < |y| → g y = 0) →
       ‖CN N₀ hg.continuous hc‖ ^ 2 ≤ BNform N₀ g := ...
\`\`\`

The parameter \`L\` remains **fixed on both sides**. The single-cutoff theorem removes \`∀N\` *at that L*, because the source regrouping identity makes \`BNform N g − ‖CN N g‖²\` independent of the admissible prime cutoff \`N\`. It does not remove \`∀L\`.

The actual logical chain is
\[
\begin{aligned}
\text{ARP}
&\iff\mathrm{OB6}\\
&\iff\forall L\in\mathbb R\;\mathrm{OB6At}(L)\\
&\iff\forall L\in\mathbb R\;\forall g\text{ supported in width }L,\quad
  \|C_{N_0(L)}g\|^2\le B_{N_0(L)}(g),
\end{aligned}
\]
where the admissibility condition is \(L<\log(N_0(L)+1)\).

## 2. The mismatch in the campaign order

[Campaign order, November 17](https://github.com/GoldenPhysicsProject/GPP-bridge/blob/main/research/CAMPAIGN-ORDER-2026-11-17.md), especially §2.2–2.5, states that \`ob6At_iff_single_cutoff\` means that an enclosure at "**one admissible cutoff**" would constitute victory with "**no uniformity in L**" and phrases the chain as "contractivity at *any one* admissible cutoff ⇔ OB6At ⇔ ARP ⇔ RH."

That last chain has suppressed the **universal-width quantifier**. No theorem \`OB6At L₀ ↔ OB6\` is supplied by \`ob6At_iff_single_cutoff\`. A finite Schur enclosure at **one width \(L_0\)** establishes at most \(\mathrm{OB6At}(L_0)\); it does not, by itself, yield RH. A single fixed prime cutoff \(N_0\) also cannot be admissible at all unbounded widths, since \(L<\log(N_0+1)\).

**Crucial nuance:** A full proof does **not** need a *uniform positive eigenvalue margin* as \(L\to\infty\). It does need a valid argument covering **every compactly supported test**, or equivalently all widths. The corrected \(\Gamma_N\) family could still be the right mechanism, and a one-width rigorous certificate can be an excellent pilot. What is invalid is promoting that pilot to universal ARP on the authority of the one-prime-cutoff equivalence alone.

## 3. A repaired, countable width-indexed target

The exact source regrouping theorem \`weilForm_regrouped\` together with compact-support containment shows that a **cofinal** family of widths is sufficient:
\[
\boxed{\quad\mathrm{OB6}\iff
  \forall m\in\mathbb N,\ \mathrm{OB6At}((m:\mathbb R)).\quad}
\]

**Proof:** Forward is immediate. Conversely, for any test \(g\in C_c^\infty(\mathbb R)\), choose an integer \(m\) large enough that \(\mathrm{supp}(g)\subset[-m/2,m/2]\), and choose an admissible prime cutoff \(N>\exp(m)-1\). The assumption \(\mathrm{OB6At}(m)\) yields
\[
0\le B_N(g)-\|C_Ng\|^2=W_\zeta(g)
\]
by the verified regrouping identity. This holds for every compactly supported smooth test, so ARP follows, and the in-tree \`arp_iff_ob6\` gives OB6. This is a mathematical proof on paper using cited in-tree identities, **not a new Lean theorem**; the bridge to the current ARP definition is already formalized in \`arp_iff_ob6\`.

Therefore a corrected Schur certificate program is **width-indexed**: for each integer \(m\), choose at least one admissible prime cutoff \(N_m\) and prove the \(\Gamma_{m,N_m}\) inequality on the entire width-\(m\) Hilbert/form domain. An effective or structural theorem covering every \(m\) would prove ARP, even if its certified margin tends to zero arbitrarily rapidly with \(m\).

## 4. Consequence for the current campaign

- **Retain** the Schur enclosure as a main research candidate. At \((L,N)\), enforce correct domain/closures, \(M_{L,N}-\gamma_{L,N}^{-1}\Gamma_{L,N}\succeq0\) (assuming that is the correct tested Schur statement) and confirm it really proves \(\mathrm{OB6At}(L)\).
- **Price the width quantifier explicitly.** A one-width enclosure is a proving ground, not an RH proof. The missing continuation is \(\forall m\), which might come from a new analytic all-width lemma, a recursive width-transfer theorem, or a genuinely global operator identity. None is supplied by \`ob6At_iff_single_cutoff\`.
- **Avoid conflating no-uniform-margin with no-all-width-proof.** Suzuki's recurrent near-zero theorem rules out many uniform lower-margin methods under RH, but does not rule out all-width semidefinite inequalities whose margins vanish.
- **Preserve the fully shifted \(F_\theta\) and \(\widetilde\Lambda\) controls** at the decisive all-width mechanism, not just at the pilot width.
- **Audit request to Turbo:** review the literal two Lean theorem statements and §2.2–2.6 and §3 Phase1a in the campaign order; correct the campaign's equivalence sentence if no independent width-reduction theorem exists. The priority rationale/reversal trigger R2 should then be repriced, not automatically discarded.

**Status:** SOURCE-VERIFIED quantifier distinction; repaired cofinal-width implication proved on paper from existing definitions; campaign correction **pending Turbo independent audit**. No Lean build or source change. ARP/OB-6/RH remain OPEN.