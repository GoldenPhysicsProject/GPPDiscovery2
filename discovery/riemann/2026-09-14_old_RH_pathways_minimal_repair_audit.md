# Old RH pathways: minimal-repair audit rather than discard

Date: 2026-09-14
Status: diagnostic synthesis; several exact corrections and replacement targets; **not a proof of RH**

## Purpose

The older ONON RH pathways should not be treated as all-or-nothing objects. Several of them begin from structures that survived later audits, then make one unjustified promotion. The right question is therefore: **what is the first invalid step, and can it be replaced by a theorem from the newer prime–Archimedean program while preserving the original spine?**

The answer is encouraging. Pathways 1–4 repeatedly encounter the same missing operation in different language: turning formal, virtual, probabilistic, or principal-series data into a **positive causal arithmetic Hilbert-space spectral object**. The current heat/Ward/Löwner/Hardy program isolates this operation exactly.

This note records the salvage map. It is deliberately conservative: corrected claims are separated from conjectural repairs.

---

## 1. Pathway 1: Haar / Cesàro — the old proof spliced causality and shadow symmetry

### 1.1 Valid beginning

Write logarithmic scale as

\[
x=\log r,
\qquad r\in\mathbb R_+^\times,
\]

and the centered real exponent as

\[
\delta=\sigma-\frac12.
\]

The half-density character is then

\[
r^{\sigma-1/2}=e^{\delta x}.
\]

The critical line is exactly the unitary locus `delta=0`; inversion/shadow sends

\[
x\mapsto -x,
\qquad e^{\delta x}\mapsto e^{-\delta x}.
\]

This structural observation is correct and survives.

### 1.2 First invalid step in ONON v12

The manuscript defines the symmetric average

\[
M_{\rm sym}(\delta,T)
=\frac1{2T}\int_{-T}^{T}e^{2\delta x}\,dx.
\]

For `delta != 0`, however,

\[
M_{\rm sym}(\delta,T)
=\frac{\sinh(2\delta T)}{2\delta T},
\]

and therefore

\[
M_{\rm sym}(\delta,T)\longrightarrow+\infty
\qquad(\delta\ne0).
\]

The old text incorrectly states that the symmetric Cesàro mean tends to zero on one side of the center. Its own explicit power formula contains the growing term `R^{|2 sigma-1|}/log R`; the subsequent limit evaluation is the error.

A second issue is conceptual. Amenability guarantees existence of invariant means on `L^infty`, not uniqueness of a canonical invariant mean on a noncompact amenable group. Moreover off-center exponential/power characters are unbounded, so one cannot simply apply an `L^infty` invariant mean to them.

### 1.3 The intended one-sided statement is actually true

The one-sided **causal** average is

\[
M_+(\delta,T)
=\frac1T\int_0^T e^{2\delta x}\,dx.
\]

Then exactly

\[
\lim_{T\to\infty}M_+(\delta,T)
=
\begin{cases}
0,&\delta<0,\\
1,&\delta=0,\\
+\infty,&\delta>0.
\end{cases}
\]

Thus the trichotomy ONON wanted belongs to a **causal half-line average**, not an inversion-symmetric two-sided average.

The shadow-reflected mode has exponent `-delta`. Consequently

\[
e^{\delta x}\text{ is bounded on }x\ge0\iff\delta\le0,
\]

while

\[
e^{-\delta x}\text{ is bounded on }x\ge0\iff\delta\ge0.
\]

Hence

\[
\boxed{
\text{causal mode and its shadow are simultaneously bounded}
\iff \delta=0
\iff \sigma=\frac12.}
\]

This is an exact elementary theorem and is much closer to the original geometric intuition than the failed symmetric-Cesàro calculation.

### 1.4 What is still missing

The boundedness lemma alone does **not** prove RH. One must prove that every arithmetic resonance/zero participates in the same causal realization **together with its co-Poisson/shadow partner**.

That missing step is now recognizable as the modern Hardy/no-leak theorem. For

\[
\Theta_\omega(z)
=\frac{\xi(1/2+\omega+iz)}{\xi(1/2+\omega-iz)},
\]

RH is equivalent to vanishing of the anticausal Hardy block

\[
\Pi_-M_{\Theta_\omega}\big|_{H^2_+}=0
\qquad(\omega>0).
\]

So Pathway 1 is not best repaired by a different invariant mean. It is repaired by replacing “regularized `L^2` character” with **causal Hardy admissibility plus exact co-Poisson shadow compatibility**.

---

## 2. Pathway 2: Meyer / Stone — correct trace spine, premature positive-spectral promotion

### 2.1 Valid beginning

Meyer/Weil supplies an unconditional arithmetic trace/distributional realization of the explicit formula. This is genuinely valuable and does not assume RH.

The old pathway correctly recognized that a true Hilbert–Pólya closure should turn arithmetic trace data into the spectral data of a self-adjoint object.

### 2.2 First invalid promotion

The manuscript promotes the Weil/Meyer distribution directly to

\[
\mu_W=\mu_A,
\]

where `mu_A` is treated as the positive projection-valued spectral measure of the raw logarithmic dilation generator

\[
A=-i\frac{d}{d\log r}.
\]

That step is not supplied by the trace formula. A virtual/difference representation or explicit-formula distribution need not be a positive spectral measure of this particular self-adjoint operator.

Moreover, identifying a zero `rho=sigma+i gamma` with the real coordinate `gamma=Im rho` does not constrain `sigma`; `gamma` is real for every complex zero by definition.

### 2.3 Minimal modern replacement

Do not discard the spectral architecture. Replace the **raw dilation generator** by the as-yet-unconstructed positive conservative completion `H` whose arithmetic boundary Weyl channel is already known.

The current program has zero-independent functions

\[
\mathscr K(t),
\qquad
m_*(u)=\int_0^\infty e^{-(1+u)t}\mathscr K(t)\,dt,
\]

and the exact target

\[
\mathscr K(t)=\operatorname{Tr}e^{-tH},
\qquad
m_*(u)=\langle\Omega,(H+1+u)^{-1}\Omega\rangle
\]

for a positive realization. Equivalently the safe impedance

\[
\phi(u)=u\,m_*(u)
\]

must be operator monotone.

Thus the missing promotion in old Pathway 2 is exactly:

> **Weil/Meyer arithmetic trace distribution -> positive conservative prime–Archimedean spectral realization.**

If the Ward/Löwner positivity theorem constructs that realization, the Stone/self-adjointness part of the old pathway becomes legitimate again, but for the correct completed operator rather than bare dilation.

---

## 3. Pathway 3: BPY probability — right positive law, wrong zero-sensitive transform

### 3.1 Valid beginning

The BPY identity is an extraordinary zero-independent positive realization. In the current normalization one may use the four-Brownian-bridge radial variable `Q` with

\[
\mathbb E[Q^{s/2}]=2\xi(s),
\]

and after the positive `Q^{1/4}` tilt,

\[
F(z)
=\frac{\xi(1/2+z)}{\xi(1/2)}
=\mathbb E_{1/2}[e^{zX}],
\qquad X=\frac12\log Q.
\]

The positivity of the underlying probability law is exact.

### 3.2 First invalid step in the old proof

The old contour argument Mellin-inverts `xi(s)` and then says that deforming the contour “picks up residues from zeros” of `xi`, with terms proportional to `xi'(rho)`.

That is false. **Zeros of an analytic integrand are not poles.** Moving a contour through a zero of `xi` produces no residue. Therefore an off-line zero cannot be made to force a sign change in the BPY probability density by that argument.

### 3.3 The exact repair already exists

Use a zero-sensitive transform in which zeros become poles: the logarithmic derivative.

For

\[
r=\sqrt{1+u}>1,
\]

define

\[
\boxed{
m_*(u)
=\frac{F'(r)}{2rF(r)}
=\frac{1}{2\sqrt{1+u}}
\frac{\xi'}{\xi}\!\left(\frac12+\sqrt{1+u}\right).}
\]

Now zeros of `F` genuinely become poles of the analytic continuation of `m_*`. The current shifted Stieltjes theorem gives

\[
\boxed{\mathrm{RH}\iff m_*\text{ is Stieltjes with positive support in }[1,\infty).}
\]

Equivalently,

\[
\boxed{\mathrm{RH}\iff \phi(u):=u m_*(u)\text{ is operator monotone on }(0,\infty).}
\]

So the original slogan “probability positivity excludes off-line zeros” was too weak, but not directionless. The required positivity is not scalar density positivity. It is the full Stieltjes/Pick/Löwner hierarchy of the **logarithmic derivative impedance**.

### 3.4 The first Löwner level is already unconditional

Let

\[
\ell(r)=\log F(r).
\]

Under the positive BPY tilted law,

\[
\ell'(r)=\mathbb E_r[X]>0,
\qquad
\ell''(r)=\operatorname{Var}_r(X)\ge0
\qquad(r>0).
\]

Since `u=r^2-1`,

\[
\phi(u)=\frac12\left(r-\frac1r\right)\ell'(r),
\]

and therefore

\[
\boxed{
\phi'(u)
=\frac{(1+r^{-2})\ell'(r)+(r-r^{-1})\ell''(r)}{4r}>0
\qquad(u>0).}
\]

Thus ordinary monotonicity, the `1 x 1` Löwner condition, already follows unconditionally from BPY probability. The first possible obstruction is matrix order `2` or higher.

This is the precise modern descendant of the old probability-positivity intuition.

---

## 4. Pathway 4: celestial principal series — right unitary axis, unsupported arithmetic identification

### 4.1 Valid beginning

The structural statements

\[
\Delta\in1+i\mathbb R,
\qquad
\Delta\leftrightarrow2-\Delta,
\qquad
\Delta=2s
\]

correctly identify the celestial principal-series axis with the critical-line geometry.

The newer program has strengthened this conceptual connection with exact formulas:

1. the thermal circle determinant/Plancherel weight
   \[
   P(z)=\frac{\pi z}{\sinh \pi z};
   \]
2. the BPY random variable whose Laplace transform is `P(sqrt t)^2` and whose Mellin moments are completed zeta values;
3. the exact Riemann–Wigner/Eisenstein identity, where the Riemann Wigner kernel is one fixed differential observable of the completed Eisenstein state at `s=1/2+it`;
4. the Hecke coefficients on that state are the unitary Satake `SU(2)` characters.

These are genuine arithmetic–principal-series bridges absent from the old ONON argument.

### 4.2 First invalid steps in the old implementation

Several concrete promotions are unsupported or incorrect.

**Jordan trace.** For a finite Jordan block

\[
J=\lambda I+N,
\qquad N\text{ nilpotent},
\]

one has exactly

\[
\operatorname{Tr}e^{\beta J}
=n e^{\beta\lambda},
\]

because every positive power of the strictly triangular nilpotent has zero trace. The old formula inserting polynomial/log terms into the ordinary trace is not correct. Logarithmic CFT correlators can contain logarithms; that is a different statement.

**Discretization.** `c=0`, BMS Ward identities, and single-valuedness do not by themselves force a continuous principal-series spectral measure onto the Riemann ordinates.

**Arithmetic identification.** The old argument eventually fixes celestial frequencies by matching them to `Im rho`; that is precisely the map that needed proof.

### 4.3 Minimal modern replacement

Keep principal-series unitarity and shadow symmetry. Replace the unsupported “BMS discretizes into zeta zeros” step by one of the exact arithmetic observables now available, and prove **positivity of that observable**, not positivity of the ambient representation.

Two current targets are particularly natural:

- the automorphic polarized-Wigner theorem for the exact Eisenstein observable;
- the prime–Archimedean Ward/Löwner positivity theorem.

The existing paper *Haar Positivity: From Weil to Wightman* is valuable here because it already separates the issue correctly. It proves the abstract Haar/GNS/Wightman/OS positivity engine and explicitly **imports** the Shadow–arithmetic identification rather than pretending to derive it. The present RH program should supply that imported step.

Thus old Pathway 4 was right about the category of the missing structure—unitarity/reflection positivity—but applied it to the ambient principal series before proving that the arithmetic observable was the physical positive sector.

---

## 5. Pathway 5: completeness — retain as the no-ghost endpoint

ONON already acknowledges that the old Pathway 5 is not independent: it takes RH from the preceding routes and then derives completeness/Hilbert–Pólya consequences.

The modern version is sharper and more useful. In the Nyman–Burnol Hardy model,

\[
X/\mathcal N\simeq K_B,
\]

and

\[
\mathrm{RH}\iff K_B=0.
\]

Reflection symmetry alone does not eliminate the model-space ghost: every nonzero `K_B` already has its own canonical conjugation. The missing statement is a **no-loss/no-ghost theorem**, equivalently vacuum saturation.

So Pathway 5 should be retained as the endpoint that tests whether the completed positive realization has lost any arithmetic state at the boundary.

---

## 6. One common missing theorem behind the old pathways

The old arguments repeatedly make versions of the same promotion:

| old route | valid object | premature promotion | modern replacement target |
|---|---|---|---|
| Haar/Cesàro | half-density, inversion, causal scale flow | regularized character treated as physical `L^2` state | causal Hardy + co-Poisson shadow no-leak |
| Meyer/Stone | explicit-formula / virtual spectral trace | trace distribution treated as positive PVM of raw dilation | positive prime–Archimedean conservative realization |
| BPY | exact positive probability law | scalar density positivity treated as zero-localizing | Stieltjes/Pick/Löwner positivity of log derivative |
| celestial | unitary principal-series + shadow | ambient unitary spectrum identified with arithmetic zeros | positive exact arithmetic observable / Ward realization |
| completeness | Hardy quotient/model space | reflection treated as ghost-killing | no-loss/vacuum-saturation theorem |

These are not five unrelated gaps. They point to one bridge:

\[
\boxed{\text{completed prime–Archimedean causal polarization / no-escaped-trace theorem}.}
\]

Current equivalent faces include

\[
\mathscr K(t)\text{ completely monotone},
\]

\[
[\mathscr K(t_i+t_j)]\succeq0,
\]

\[
[\mathscr J(a_i,a_j)]\succeq0,
\]

\[
\phi(u)=u m_*(u)\text{ operator monotone},
\]

\[
\Pi_-M_{\Theta_\omega}|_{H^2_+}=0,
\]

and

\[
K_B=0.
\]

A proof of this bridge would not merely be a new sixth proof. It would repair the first unjustified promotion in several of the original pathways at once.

---

## 7. Immediate next attacks

1. Derive the matrix-order-2 Löwner inequality for the safe BPY impedance and express it in tilted cumulants. Determine whether it follows from an elementary covariance inequality or isolates the first genuinely new fourth-cumulant constraint.
2. Identify the integrated heat-flux vectors `f_a`, with
   \[
   \widehat f_a(\xi)=\frac{1-e^{-a\xi^2}}{|\xi|},
   \]
   as a canonical restricted Weil/Haar-positive test cone and prove that positivity on their finite span alone is RH-equivalent.
3. Use the exact identity
   \[
   \widehat f_a(\xi)=\int_0^a |\xi|e^{-t\xi^2}\,dt
   \]
   to connect the repaired Pathway-1 causal/shadow picture directly to the boundary-flux OS vectors.
4. Attempt a finite positive passive realization of the Löwner kernels using the Möbius–Hodge occupation bulk as internal states and the Archimedean channel as the boundary port.
5. Formalize the finite atomic Löwner Gram theorem in Lean without any arithmetic/RH assumption.

No RH proof is claimed here. The point is narrower and constructive: the earlier work contains several correct spines. Their failures are localized enough that the current program can target the missing promotion theorem rather than restart from zero.
