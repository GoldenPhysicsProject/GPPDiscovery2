# Horizon / null-infinity exact relationship

## Bottom line

The statement

`black-hole event horizon = local piece of future null infinity`

is false.

The strongest general statement supported by standard GR is instead:

> A black-hole event horizon and null infinity are distinct null boundary structures of the same exterior causal problem.  They admit a common characteristic/null-boundary formalism, but they are not canonically the same boundary, and their physical boundary data differ.

There is, however, a much stronger **special extremal correspondence**: in extremal Reissner-Nordstrom the Couch-Torrence conformal inversion exchanges the future event horizon and future null infinity.  That exact theorem cannot be generalized to nonextremal Schwarzschild without additional proof.

## 1. Exact causal relation

For an asymptotically flat spacetime,

\[
\mathcal B=M\setminus J^-(\mathscr I^+),
\qquad
\mathcal H^+=\partial J^-(\mathscr I^+).
\]

Thus `H+` is defined globally **relative to** `I+`: it is the causal boundary separating points that can communicate with future null infinity from those that cannot.

This gives a real structural relation, but not set-theoretic identity.

For a stationary asymptotically flat black hole, the domain of outer communications is

\[
\mathcal D=I^-(\mathscr I^+)\cap I^+(\mathscr I^-)
\]

(up to the standard causal-set convention used in the source).  Its conformal/global closure has distinct asymptotic and horizon boundary pieces.  A useful precise replacement for Daniel's phrase is therefore:

> `H+` and `I+` are two null faces of the exterior/domain-of-outer-communications boundary problem.

This is stronger than saying only that both are null, but weaker and more accurate than calling one a local piece of the other.

## 2. Schwarzschild Penrose geometry

In maximally extended Schwarzschild:

- `H+` is the future event horizon;
- `H-` is the past/white-hole horizon;
- `H+` and `H-` meet on the bifurcation two-sphere;
- `I+` is the distinct conformal boundary reached by escaping outgoing null geodesics;
- the exterior region lies between the horizon and null infinity in the Penrose diagram.

A physically useful hyperboloidal foliation of the exterior can have spacelike slices running from `H+` to `I+`.  This makes `H+` and `I+` the two ends of one exterior characteristic/radiative problem, but still does not identify them.

In a collapse spacetime there is generally no past white-hole horizon or bifurcation sphere.  Therefore any universal GPP quotient must not rely on the eternal Kruskal `H+ <-> H-` pair as a literal physical second branch.

## 3. Common characteristic/null-boundary category

An event horizon is itself a characteristic hypersurface for the Einstein equations, so characteristic methods apply directly to it.  Null infinity is likewise handled by the asymptotic characteristic problem for the conformal Einstein equations.

This gives a rigorous common category:

\[
\boxed{\text{null hypersurface + spacelike cuts + characteristic data}}
\]

rather than a common geometric location.

Chandrasekaran-Flanagan-Prabhu develop covariant phase space, symmetries, localized charges and fluxes on a **general null boundary**, including nonstationary event horizons.  Their null-boundary symmetry algebra has structural similarities to the BMS algebra at null infinity, including supertranslations.

Therefore horizon cuts and celestial cuts are genuinely analogous instances of codimension-two cuts of null hypersurfaces, and parts of the charge/edge-mode formalism can be written uniformly.

## 4. The boundary data are not identical

The common null-boundary category does not imply identical radiative data.

At future null infinity, asymptotically flat gravity uses Bondi-type free data; the shear and its retarded-time derivative (Bondi News) encode outgoing gravitational radiation.

On an isolated/nonexpanding horizon, by contrast, the null generators are expansion-free and shear-free under the standard horizon conditions.  Its intrinsic geometry and horizon connection are the natural data, and there is no ordinary Bondi-News degree of freedom on an equilibrium isolated horizon.

A generic nonstationary null surface/event horizon can carry shear and flux, and general null-boundary phase space permits such data, but the boundary conditions and symmetry algebra are not automatically the same as at `I+`.

So there is no justified universal statement that a finite horizon carries *the same representation-theoretic data* as celestial infinity.  What is justified is a shared null/Carrollian/characteristic architecture.

## 5. Extremal horizon-null-infinity correspondence: exact special case

Extreme Reissner-Nordstrom has the Couch-Torrence discrete conformal inversion.  It exchanges

\[
\mathcal H^+ \longleftrightarrow \mathscr I^+
\]

in the exterior geometry.

For probe fields this can map near-horizon data to asymptotic data.  In particular, the literature relates Aretakis-type horizon charges to Newman-Penrose-type charges at null infinity, and maps soft/horizon data under the inversion.

This is the strongest rigorous realization found so far of Daniel's intuition that a horizon can act as a finite/internal counterpart of null infinity.

But the qualifier is essential:

\[
\boxed{\text{exact for special extremal conformal-inversion geometries, not generic Schwarzschild}}
\]

The zero surface gravity/extremal throat is structurally important.  Nonextremal Schwarzschild has no known analogous conformal isometry exchanging its event horizon with null infinity.

## 6. The 2026 Schwarzschild googly paper does NOT identify the coincidence locus with the horizon

Adamo-Araneda-Seet-Sharma, *Schwarzschild black holes from twistor space* (arXiv:2607.06236), construct a special nonlinear googly solution by placing the relevant anti-self-dual Taub-NUT structure inside the twistor space of self-dual Taub-NUT and restricting to a holomorphic coincidence locus.

The paper explicitly emphasizes that this construction is **local**.  Lorentzian Schwarzschild global topology is obtained only after choosing real conditions and globally extending the resulting real metric.

The paper does not identify the coincidence locus with an event horizon and does not use the event horizon in the holomorphic construction.

This gives a hard negative result:

\[
\boxed{\text{twistor coincidence locus} \neq \text{Schwarzschild event horizon}}
\]

at least as a statement supported by that construction.

This is also conceptually expected: an event horizon is teleological/global, while the paper's coincidence condition is local holomorphic geometry.

If the horizon has a twistor characterization in this construction, it must emerge only after imposing the Lorentzian real structure, global extension, and causal definition.  Determining the preimage/real-locus characterization of `r=2M` inside the completed twistor correspondence is a separate open problem.

### Split-signature exclusion

The same paper states explicitly that the resulting Schwarzschild metric can be given Euclidean or Lorentzian reality conditions, but that **split (ultrahyperbolic) signature is not allowed by their construction**: it would require one of the three spatial Kerr-Schild coordinates to be purely imaginary.

This matters for the GPP programme because split `(2,2)` is our working real slice.  Therefore the 2026 Schwarzschild construction is an external nonlinear consistency check after a change of reality conditions; it cannot be imported as the missing split-signature Fourier/Penrose theorem.

This also cleanly separates two statements:

1. the complex/local holomorphic mechanism can generate a non-self-dual metric conformal to Schwarzschild;
2. the GPP split-signature representation theorem must be established independently before Lorentzian descent.

## 7. Consequence for the GPP quotient idea

The horizon does **not** currently provide evidence that two twistor chiral lifts literally meet at a local holomorphic fixed locus.

The defensible GPP target is instead:

1. construct the same-state dual representation `D_epsilon` from projective Fourier/incidence geometry;
2. formulate horizon data as data on one null boundary `H+`;
3. ask whether `D_epsilon` induces a conjugate/orientation-reversed representation on that same boundary phase space;
4. test whether physical observables or charges descend to a quotient

\[
[x]=[D_\epsilon x];
\]

5. only in special geometries where a genuine horizon/infinity conformal map exists should one attempt to identify the horizon representation directly with celestial-infinity data.

This preserves Daniel's phrase

`There is no other place. Both halves are here.`

in the mathematically respectable form `one geometric null boundary, multiple dual/oriented representations`, without inventing a second spacetime region or declaring `H+=I+`.

## 8. Interaction with the epsilon/Fourier/polarity spine

No horizon-specific epsilon theorem has yet been established.

The plausible common interface is the geometry of null two-plane/incidence data:

- null hypersurfaces are ruled by null generators;
- their spacelike cuts carry the transverse two-dimensional geometry;
- `Gr(2,4)`/Klein and twistor incidence already encode null planes/congruences in the split complexified setting;
- projective Fourier duality exchanges ordinary/dual twistor representatives of the same on-shell state.

The next hard question is therefore not `is H a piece of I?`, but:

\[
\boxed{
\text{Does }D_\epsilon\text{ act functorially on characteristic data/charges of an arbitrary null boundary, and if so does the action specialize consistently at }\mathscr I^+\text{ and }\mathcal H^+?
}
\]

A positive result there would provide an actual common boundary representation theorem.  Until then, the horizon-null-infinity relation remains: general structural analogy/common formalism; exact equivalence only in special extremal cases.
