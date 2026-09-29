# Zero survival and two-sided scale growth

Date: 2026-09-29, America/Toronto.
Status: exact abstract lemmas, a limitation of ordinary L2 quotients, and a conditional arithmetic target. The arithmetic growth estimate is NOT proved. RH remains open.

Daniel's question: if unitarity is what forces the zeros into the primitive one-dimensional principal series, where does that theorem come from, and can we see it already?

This note keeps his priority explicit: prove principal-series membership directly if possible; Weil positivity can follow from RH. Neither a full Weil positivity proof nor a full unitary field theory must be imposed as an intermediate requirement.

## 1. Current state and provenance

Read the live bridge bootstrap, research tail, heuristics, Supabase, and the Discovery2 workbench at be2cc539e89c84d93f51616514b74d4f92a9f842. Bridge snapshot: e2c8096e10b200b273246cbc957e2f64b69d48b9.

The other active Codex has adopted the independent review's analytic-family correction and the finite-pole warning. It has since proved the finite zeta-graph current norm bound and exposed the weighted Möbius obstruction in the raw dual character. Those results are not overwritten here.

Relevant existing mathematics:
- CompletedZetaDilationUnitaryBridge.lean: the principal-series/dilation compatibility, explicitly without a zero-location assertion.
- MomentumGeneratorNoPointSpectrum.lean: ordinary log-line momentum has no L2 eigenvectors.
- UnitaryParentLeakage.lean: a unitary parent's compression can leak; isometry requires the hidden channel to vanish.
- Discovery2 research/2026-09-28_rh_selfadjoint_conformal_casimir.md: a real zero Casimir already forces the critical line.
- Discovery2 research/2026-09-28_finite_zeta_graph_dual_mobius_obstruction.md: the raw graph-dual observation remains arithmetic and difficult.
- Supplied v34 manuscript: the Gamma topology can lose the periodization trace; the Nyman--Burnol causal cokernel must be retained by the physical boundary topology.

The present analysis derives the relevant elementary implications directly. It makes no external-literature novelty claim, supplies no new numerical RH evidence, and does not alter GPPVerify.

## 2. The exact scaling character

On L2(R_+,dx), define

(U_t f)(x) = exp(t/2) f(exp(t)x).

A change of variables proves ||U_t f||_2 = ||f||_2. With Mellin convention

Mf(s) = integral_0^infinity f(x) x^(s-1) dx,

one has on any justified Mellin test domain

M(U_t f)(s) = exp((1/2-s)t) Mf(s).

Thus a zero parameter rho would carry the character

exp((1/2-rho)t)
= exp(-(Re rho-1/2)t) exp(-i Im rho t).

The arithmetic work is to realize this character in a topology that retains the zero and provides a two-sided dynamical estimate. The Mellin character calculation alone provides no estimate on its arithmetic realization.

## 3. Exact theorem: zero characters in a unitary realization are principal

Let H be a complex Hilbert space and V_t a unitary group. Suppose a nontrivial zeta zero rho gives a nonzero bounded complex-linear functional ell_rho in H* such that

ell_rho(V_t v) = exp((1/2-rho)t) ell_rho(v)

for every v and every real t.

Because V_t is a surjective isometry,

||ell_rho composed with V_t|| = ||ell_rho||.

The covariance identity also gives

||ell_rho composed with V_t||
= exp((1/2-Re rho)t) ||ell_rho||.

Since ell_rho is nonzero, exp((1/2-Re rho)t)=1 for all t, so Re rho=1/2. QED.

The same conclusion follows for a nonzero Hilbert eigenvector with that character. Bounded eigenfunctionals and ordinary spectral vectors are deliberately stronger than arbitrary distributional resonances.

This isolates two hypotheses:
1. every nontrivial zero survives as a nonzero, continuous arithmetic spectral datum;
2. the completed evolution has the required norm control.

It is invalid to obtain unitarity by completing away the zero data and then declare that they were on the spectrum all along.

## 4. Exact weakening: subexponential growth is sufficient

Full unitarity is unnecessary for the location of the characters.

Let X be a complex Banach space and V_t a group of bounded operators. Suppose

||V_t|| <= C_epsilon exp(epsilon |t|)

for every epsilon>0 and all real t, with C_epsilon independent of t. Suppose each nontrivial zero has a nonzero bounded functional satisfying the same character covariance as above.

Then

exp((1/2-Re rho)t) <= C_epsilon exp(epsilon |t|).

Taking logarithms and letting t tend to plus and minus infinity gives

|Re rho-1/2| <= epsilon.

Since epsilon is arbitrary, Re rho=1/2. QED.

More quantitatively, a bound ||V_t|| <= C exp(a|t|) implies
|Re rho-1/2| <= a for every retained zero character.

### Even orbitwise bounds suffice

It is enough, for each rho, to have one v_rho with ell_rho(v_rho) != 0 and

||V_t v_rho|| <= C_(rho,epsilon) exp(epsilon |t|).

Indeed

exp((1/2-Re rho)t) |ell_rho(v_rho)|
<= ||ell_rho|| ||V_t v_rho||,

and the same limit argument applies. A common test vector can serve all zeros if its evaluation at every zero is nonzero. Existence of such a vector and continuity of the evaluations must be established in the actual arithmetic space.

### Meaning for the research target

The minimal dynamical goal can be “no exponential growth in either scale direction while retaining every zero,” rather than an isometric realization. This is compatible with Daniel's request to avoid unnecessarily strong intermediate theorems.

This is a version of the exponential-growth detector already developed elsewhere in the programme. The useful refinement here is the explicit continuity/survival hypothesis and the multiplicity distinction below; it is not a new proof of the missing arithmetic bound.

Do not confuse the time variable t in this theorem with a cutoff N. A bound N^(o(1)) is not a uniform Montel bound and becomes relevant here only through a proved relation between the cutoff observable and this scale evolution (or the earlier exact fixed-window detector).

## 5. Why full unitarity can impose an unintended simplicity condition

This issue depends on the chosen realization. A unitary operator can certainly have an eigenvalue of arbitrary multiplicity. The difficulty concerns the particular analytic jet quotient used to encode multiplicity.

Suppose an entire function F has a zero rho of order m. Locally,

F(s) = (s-rho)^m h(s), h(rho) != 0.

Its local holomorphic quotient is the jet algebra

A_rho = C[w]/(w^m), w=s-rho.

Multiplication by the centered spectral coordinate s-1/2 acts as

T = (rho-1/2) I + N,

where N is multiplication by w, N^m=0, and N^(m-1) != 0.

The induced scale evolution in the sign convention of section 2 is

exp(-tT)
= exp(-(rho-1/2)t)
  sum_(j=0)^(m-1) (-t)^j N^j/j!.

If rho lies on the critical line but m>=2, this has polynomial growth of order m-1 on suitable vectors. In any positive-definite norm on this finite-dimensional jet space, it cannot be a unitary group: nonzero Jordan blocks are incompatible with bounded two-sided evolution.

Therefore requiring the full analytic jet quotient to be unitary can demand BOTH RH and simplicity. RH alone allows repeated zeros.

By contrast, the subexponential criterion allows this polynomial Jordan growth and still forbids every off-line zero.

One can instead seek a semisimple Hilbert realization with degenerate eigenspaces, but the passage from analytic jets to that realization would itself require a construction. It is not legitimate simply to identify a jet multiplicity with m orthogonal eigenvectors.

This is a reason to retain the weaker growth formulation unless a natural semisimple arithmetic realization has already been proved.

## 6. Why the most obvious Hilbert quotient loses the zeros

A potentially tempting proof is:
- start with the ordinary unitary dilation group;
- divide out the arithmetic transfer range;
- inherit unitarity on the quotient;
- read the zeros as quotient eigenmodes.

The middle step is not innocuous.

### 6.1 Closed invariant quotients cannot create point spectrum

Let U_t be a unitary group on H and M a closed subspace invariant under U_t for every real t. Because negative times are included, M is reducing. The quotient H/M is unitarily equivalent to M-perp.

Every eigenvector of the quotient therefore lifts to an eigenvector of the original group. If the original group has no point spectrum, neither does the quotient.

The free logarithmic translation representation on L2(R) has no point spectrum, as the existing Lean file proves directly. Consequently, an ordinary closed invariant quotient of that representation cannot produce discrete normalizable Riemann-zero modes.

This statement does not rule out generalized real-frequency distributions, relative traces, Hardy semigroup models, or a different completed representation. Each requires its own exact arithmetic identification.

### 6.2 The maximal xi multiplier has dense range

In Mellin frequency space put

m(t) = xi(1/2+it).

Since xi is a nonzero entire function, its real-axis restriction has isolated zeros and m(t) != 0 almost everywhere. Let M_m be the maximal multiplication operator on L2(R,dt).

For arbitrary g in L2, define

E_n = {t: |t|<=n, 1/n <= |m(t)| <= n},
g_n = 1_(E_n) g,
f_n = g_n/m.

Then f_n is in L2, m f_n = g_n is in L2, and g_n tends to g in L2 by dominated convergence. Hence

closure(Ran M_m) = L2(R).

Thus

L2(R)/closure(Ran M_m) = {0}.

This quotient erases on-line zero information as well. It is a topology failure, not a proof of RH.

The lemma concerns the maximal multiplier, or a domain proved to be a core for it. It does NOT assert without proof that the particular Poisson-restricted E-map has this same full range closure. That domain distinction is exactly what the project must control.

### 6.3 Why this matches the existing manuscript obstruction

The v34 periodization discussion already shows that a plain weighted L2/Sobolev norm can lose pointwise boundary traces. Its Nyman--Burnol construction retains interior zero evaluations in a Hardy space instead.

However, that Hardy structure naturally carries a one-sided contraction semigroup, whose unitary dilation does not itself eliminate interior resonances. To obtain the two-sided bound of section 4 while preserving the relevant arithmetic evaluations is the missing global theorem.

Neither dropping the trace nor taking a unitary parent automatically achieves it.

## 7. Where the arithmetic theorem would have to be derived

The natural place is the domain and norm of the completed Poisson/Möbius boundary construction.

The raw ingredients already exist:
- the half-density E-map combines additive Poisson duality with multiplicative transfer;
- the connected BPY map is bounded and bounded below;
- the finite zeta-graph current has norm at most log N;
- the elementary pole channels and their required cancellation are identified.

What is not established is that these structures give a completed observation or quotient which simultaneously:
- retains the relevant zero characters or the exact completed logarithmic response;
- has controlled evolution or analytic continuation;
- does so in an arithmetically forced topology rather than a norm chosen to exclude unwanted zeros.

The latest Möbius dual obstruction confirms this location. The raw dual character remains hard even though the primal current is tame. An orthogonal addition of an Archimedean space cannot reduce that raw dual norm. Actual coupling through the Poisson graph is required.

Thus the next concrete calculation in a unitary approach is the evolution of the PHYSICAL graph norm or physical boundary response after the Poisson constraint. One should compute its boundary defect explicitly and try to show that it cannot generate exponential growth. Mere invariance of a formal expression is not enough when its domain or closure changes.

## 8. An alternative one-line conclusion through the Casimir

If a nontrivial zero rho = beta+i gamma has gamma != 0 and is represented faithfully as an eigenvalue

c_rho = rho(1-rho)

of a symmetric operator on a positive Hilbert domain, then c_rho is real. Since

Im c_rho = gamma(1-2beta),

beta=1/2 follows.

For an actual point eigenvector, symmetry on its domain is enough for this reality conclusion; one need not first prove every property of a full field theory. A complete self-adjoint resolvent realization supplies a stronger, robust version.

The missing arithmetic identification and nonvanishing of the spectral state remain essential. The scalar Casimir formula alone is already in the programme and is not new progress on that identification.

## 9. What is proved, what is still missing

Proved here by elementary arguments:
- character survival plus unitary evolution forces the principal series;
- two-sided subexponential operator growth, or appropriate orbitwise growth, is sufficient;
- full unitarity of an analytic jet quotient can inadvertently impose simplicity;
- a closed invariant quotient cannot create point spectrum absent from its unitary parent;
- the maximal xi multiplier has dense L2 range, so its ordinary completed cokernel is zero.

Not proved:
- an arithmetic topology retaining all required zero data with the growth bounds;
- a valid completed scalar finite family meeting the global analytic bounds;
- RH, simplicity, or global Weil positivity.

Answer to Daniel: the mechanism and its precise location are visible. The arithmetic estimate that would establish it is not. The missing theorem belongs at the completed boundary/domain map, with survival of the arithmetic spectral data checked alongside norm control.

## 10. Work separation

This note is stored on an isolated Discovery2 topic branch based on the latest active workbench snapshot. The other Codex's workbench and GPPVerify PR are untouched. The full text and reusable lessons are mirrored to GPP-bridge and Supabase. No subagents, paid services, external mathematical searches, numerical claims, or unsolicited agent messages were used.
