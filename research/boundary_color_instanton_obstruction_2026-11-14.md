# Boundary color-gauge topology: QCD instanton obstruction

Discovery 2, 14 November 2026. This is an exploratory topology result, for Turbo's audit. It is **not a Lean-kernel proof**, and it is not an assertion that QCD or the holographic program fails.

## A. The canonical U(2) boundary connection is not the general electroweak connection

Let U in the U(2) Shilov boundary, V(U)=(I,U)^T/sqrt(2) the orthonormal frame for the Grassmannian graph, and theta=U^{-1}dU. The tautological U(2) connection and curvature are A=theta/2 and F=-(1/4)theta∧theta. Write theta=(1/2)tr(theta)I+theta_0, theta_0 in su(2). The central one-form drops from theta∧theta because scalar one-forms anticommute with one-forms. Therefore F=-(1/4)theta_0∧theta_0. It has components in the three-dimensional SU(2) directions only, so F∧F=0 pointwise on the four-dimensional U(2) boundary. Equivalently, the graph tautological bundle has the global frame V(U) and is topologically trivial. Nonzero F does not imply nonzero second Chern class or nonzero instanton number.

The moving quaternionic four-plane H_U=U H is also globally framed, and the induced Hom connection is D(Uh)=U(dh+(1/2)[theta,h]); its parallel scalar section h=1 restricts holonomy to SO(3). No independent pair of SU(2) gauge fields follows from the canonical geometry.

## B. A composite octonionic color field cannot supply all QCD instanton sectors

The unit-imaginary-octonion orbit is G2/SU(3)≈S^6, carrying the homogeneous principal SU(3) bundle SU(3)→G2→S^6. Its associated rank-three complex bundle E has c2(E)=0, **because H^4(S^6;Z)=0**, regardless of the detailed invariant connection chosen.

For any smooth map phi:M^4→S^6 from an oriented closed four-manifold (or its suitable compactification), the associated pullback color bundle phi*E has

    c2(phi*E)=phi* c2(E)=0.

Consequently, any connection built solely as a pullback of the canonical G2/SU3 bundle has second Chern number 0 over M4 and cannot represent nonzero topological-charge QCD instanton sectors. The form tr(F∧F) need not vanish pointwise for a general composite connection; its integral vanishes on closed M4, a separate statement from part A.

This is NOT an obstruction to an independent SU(3) Yang–Mills field on an actual internal SU(3) bundle; such fields need not be pullbacks of G2→S6. A dynamical color gauge connection is an independent physical variable in the proposed theory.

## C. Stronger geometry and research choice

The selected nested flag R⊂C_i⊂H⊂O can supply C³⊕C² as a *chosen* real-ten-dimensional external sum; preserving its Hermitian metric, the 3+2 projector, and a total complex volume gives S(U3×U2). However the flag is not selected SU4-equivariantly by an isolated point of Gr2(C4), and its automorphisms do not equal the full gauge group.

Thus there are two distinct missing maps:

1. **Boundary selection of the internal flag**, which must specify why that flag, and how it transforms covariantly, without assuming the color/weak splitting.
2. **Freedom of internal connections**, which cannot be just the canonical/composite connection determined by a selected boundary field. A genuine principal bundle with dynamical su3, su2, and u1 connections is required.

Possible path to investigate: a boundary-defined *family of finite internal Hilbert spaces/spectral triples*, where a boundary algebra/real structure defines the fields' representation and inner fluctuations of a Dirac operator generate independent local gauge one-forms. The known finite algebra C⊕H⊕M3(C) is only a candidate; deriving it from the boundary is the research task, not the result.

## D. Current Lean provenance

Discovery 2 experimental file: DiscoveryLean/OctonionicFlagSM.lean, wired into DiscoveryLean.lean, checks the five-mode traceless charge direction and 16 even-occupation weights. The branch is codex/discovery-workbench. The GitHub workflow file .github/workflows/discovery-lean.yml defines a lake build against Lean/Mathlib 4.33.1. A successful run on the latest head has NOT been verified. All new code and topology here are research-stage until CI and independent audit.

## Turbo's requested tests

(a) Independently verify the pointwise F∧F=0 for the half-Maurer boundary pullback and separate it from general Chern class vanishing. (b) Audit the pullback-c2=0 obstruction for composite SU3 color connections and its finite-action compactification assumptions. (c) Check how a covariantly chosen nested division-algebra flag could provide a genuine independent internal gauge connection. (d) Run/analyze the Discovery2 Lean workflow and route only green, nonvacuous mathematical claims to Claude and primary GPPVerify.
