# 2026-11-18: WWIF double, Klein real forms, plane half weights, and global prime-TFD limit

Source audit: ONON v5.2.1.3 (Klein quadric / spacetime signature / four-face passages), qg_definitive, arithmetic_principal_series_RH_program-34, GPPVerify OrientationCliffordCore, CelestialOrientedNullDoubleCover, OrientationThermofieldDouble, PrimeTFDVonMangoldt, CriticalPrimeTFD, earlier 2026-10-13 spherical Cayley bridge note. Status: exact math + finite computational checks, not a physical gravity or RH theorem.

## A. Equal 1/2 weights come from one oriented plane

An oriented Euclidean 2-plane in R4 is the unit decomposable bivector omega=u∧v. Hodge star on 2-forms has *²=1. With omega±=(omega±*omega)/2, Plücker decomposability omega∧omega=0 gives ||omega+||²-||omega-||²=0. Since the summands are orthogonal, each has norm squared exactly 1/2. Conversely norm equality implies decomposability for a nonzero real bivector in four dimensions. Therefore Gr_2^+(R4)=S²_+×S²_- through the pair of normalized self-dual/anti-self-dual bivectors; its unoriented quotient is (S²×S²)/{(a,b)~(-a,-b)}. Exact geometric 50/50, not an automatically physical Born probability. This upgrades the book's Plücker balance to a concrete oriented-plane/double-sphere dictionary. It matches Daniel's "four faces of two planes" intuition at the level of orientation labels, without deriving physical charge or time.

## B. The same complex carrier admits different REAL signatures

Q4=Gr(2,C4) embedded by p01 p23-p02 p13+p03 p12=0 in CP5 has 4 complex = 8 real dimensions. The projective null cone of R^(5,1) gives Euclidean S4. The projective null cone of R^(4,2) gives Lorentzian (S1×S3)/±; its double cover S1×S3 and causal universal cover R×S3. These are different real forms of one complex quadric, not the same 4-real-manifold; S4 cannot support a global Lorentzian metric (Euler characteristic 2). The Hermitian 2×2 carrier X=tI+xσ1+yσ2+zσ3 has det X=t²-x²-y²-z² exactly. g and -g have the same null cone, but changing overall metric sign is NOT physical CPT by itself.

Hodge *²=(-1)^q on 2-forms in a 4-real-dimensional signature with q negative signs. Thus Euclidean/split signatures admit real ± eigenspaces; Lorentzian has ±i eigenspaces that conjugation interchanges. This is an exact candidate for the "dual chiral faces of one real field" analogy, not a full googly/CPT theorem.

## C. Exact Cayley/sphere boundary with singular ultraviolet point

Use w=(s-1)/s. The critical line Re(s)=1/2 maps precisely to |w|=1, and D(s)=1-conj(s) acts as w->1/conj(w). Under inverse stereographic projection it reflects S² across its equator. Already derived in GPP-bridge/work/codex/2026-10-13_spherical_double_cayley_spinor_null_cone_geometry.md. However G(w)=xi(1/(1-w)) has an essential singularity at w=1, the compactified infinite-ordinate puncture. The spectral line parametrizing Mellin principal series is not automatically the physical celestial S² of null directions. Shadow reflection symmetry does not by itself exclude off-equator zeros (shifted completed F_theta is an exact control).

## D. Global paired prime state: zero signed generator != zero energy != Weil positivity

For each prime p, H±,p=log(p)N± and Omega_p=sqrt(1-p^-1) Σ_{n>=0} p^{-n/2}|n,n>. Exactly (H+,p-H-,p)Omega_p=0, while H± are positive. The cross-sheet correlator log(p)p^{-m/2} is Lambda(p^m)/sqrt(p^m); already proved in GPPVerify/PrimeTFDVonMangoldt. The local reduced entropy is
S_p=-log(1-p^-1)+log(p)/(p-1), and mean positive total energy is 2log(p)/(p-1).
For P a prime cutoff, the product paired state has zero signed generator; however S(P)=sum_{p<=P}S_p=log P+log log P+O(1) by prime asymptotics, while its squared overlap with naive product vacuum is ∏_{p<=P}(1-1/p)~exp(-EulerGamma)/log P -> 0. Cutoff states vacuum-padded into the reference infinite tensor product cannot form a norm-Cauchy sequence: their tail overlap tends to zero. Thus a new GNS/modular infinite-prime representation or renormalization is unavoidable to define a global arithmetic boundary vacuum. This is a genuinely global obstruction that no fixed-window or fixed-prime test can detect. Does NOT prove W_zeta=0 or W_zeta>=0.

Independent reproducible Python tests of 1000 random Hodge-plane decompositions, 500 Cayley points, 500 Hermitian determinant checks, and cutoff entropy through P=100000 all PASS with floating residual <4e-15. Local file produced in session: verify_wwif_global_geometry.py.

## E. Four strict interfaces that cannot be bypassed

1. Ordinary charged CAR distinguishes relative complex structures I,J, q=-IJ. Simultaneous reversal is generally ANTIlinear; cannot be implemented as a nontrivial ordinary complex-linear internal gauge on one Hilbert space. See GPPVerify/docs/orientation_car_kd_blackmirror_synthesis_2026-09-09.md (and Boyle-Deng KD two-sheet prior art, arXiv:2511.11548).
2. TFD/tensor factors versus pure redundancy are different: a paired purification is not a proof that two orientations are literally the same state.
3. Even exact boundary information equivalence does not fix Bekenstein-Hawking entropy A/(4l_P²). Must derive the area cutoff and gravitational coupling, not merely count equal Hilbert spaces.
4. Need exact globally completed SIGNED Weil form (real place, pole, primes, gamma, boundary sewing) as a true positive Hilbert-space form; the trivial Hermitian doubling of an analytic pencil only gives |det|² and loses zeta zeros. Test F_theta and DH controls. This remains the RH-bearing bottleneck.

Research direction: build a single infinite-prime *-algebra/GNS state with an anti-linear orientation real structure and a Lorentzian-real-form null-cone reconstruction; derive the actual Weil pairing (not just the zero difference generator) and prove, rather than assume, positivity and full zero spectral completeness. The geometric half-weight theorem can be formalized independently as an upstream-worthy Grassmannian/Hodge result.
