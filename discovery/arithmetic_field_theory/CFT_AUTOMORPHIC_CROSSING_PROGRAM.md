# Arithmetic field theory: automorphic crossing is not merely an analogy

## External mathematical evidence

A particularly important recent development is Adve–Bonifacio–Kravchuk–Mazac–Pal–Radcliffe–Rogelberg, *Weyl bound for trilinear periods via conformal bootstrap* (arXiv:2508.20576). Their setup makes several pieces of the proposed arithmetic-field-theory dictionary mathematically exact:

- the relevant global symmetry is `PSL(2,R)` acting by Möbius transformations;
- spectral parameters satisfy `lambda = s(1-s)`, exactly the same shadow-invariant Casimir already formalized in GPPVerify2;
- crossing equations are obtained by decomposing associativity of multiplication on `C^infty(Gamma\G)` into irreducible representations;
- in standard automorphic language the crossing equation is a spectral reciprocity formula;
- trilinear/OPE-like coefficients become automorphic triple-product periods;
- in arithmetic cases their squares are related to central triple-product L-values;
- conformal-bootstrap positivity/averaging methods prove genuine new number-theoretic bounds.

This is strong independent evidence that the CFT/automorphic dictionary is structural, not just linguistic.

## Current GPP theorem ladder

The project now has or is actively formalizing:

1. `x = log a` turns the positive-real modulus flow into a one-dimensional additive translation group.
2. Half-density characters become `exp(x(s-1/2))`; on `s=1/2+i tau` they are unitary Fourier modes `exp(i tau x)`.
3. Shadow `s -> 1-s` is momentum reversal `tau -> -tau` and Hermitian conjugation on the principal line.
4. The shadow-invariant Casimir is `s(1-s)=1/4+tau^2`.
5. The global Eisenstein/Weyl coefficient is a completed-zeta scattering ratio and is unitary on the principal axis away from zeros/poles.
6. At each finite prime, Tate's local zeta integral produces the local Euler factor.
7. `PGL(2,Q_p)` fractional-linear transformations obey exact p-adic conformal distance covariance.
8. Cross-ratio invariance is the next exact four-point kinematic statement and is now under Lean CI.
9. Bost–Connes-type systems provide a genuine C*-dynamical/KMS quantum-statistical sector with zeta/Dedekind-zeta partition functions.

## Stronger conceptual synthesis

The right working model is not simply "the number field is analogous to a 1d CFT." A more precise candidate is an **adelic arithmetic conformal field theory skeleton** whose local components are conformal representation-theoretic systems over all places and whose global arithmetic observables are assembled adelically.

Candidate dictionary:

| QFT/CFT structure | Arithmetic structure |
|---|---|
| spacetime/boundary coordinate | local field / projective line |
| global conformal group in 1d | `PGL(2,K_v)` |
| dilation generator | logarithmic norm / idele modulus |
| primary dimension | principal-series exponent |
| shadow | Weyl reflection |
| quadratic Casimir | `s(1-s)` |
| two-point covariance | local norm covariance |
| cross ratio | field-theoretic projective cross ratio |
| OPE coefficient | trilinear automorphic period candidate |
| crossing | spectral reciprocity / associativity after irreducible decomposition |
| conformal blocks | local/global representation-theoretic special functions |
| thermal Hamiltonian | logarithmic norm Hamiltonian |
| thermal partition function | zeta / Dedekind zeta in arithmetic QSM |
| local scattering/intertwiner | local gamma/Euler factor |
| global scattering matrix | completed L-function / Eisenstein intertwiner |

The table contains statements of different maturity. Kinematic rows are increasingly exact/formal. OPE/crossing/operator-algebra assembly remains the major construction target.

## Concrete next research program

### A. Local finite-place CFT kinematics

- certify full p-adic cross-ratio invariance;
- define scalar two-point kernels `G_Delta(x,y)=|x-y|_p^{-2Delta}` in a domain where real powers are well-defined;
- derive their exact `PGL(2,Q_p)` primary covariance from the already-proved distance law;
- formulate four-point covariance and isolate arbitrary cross-ratio dependence;
- compare with known p-adic CFT/Bruhat–Tits constructions.

### B. Archimedean/automorphic crossing

Formalize the representation-theoretic skeleton suggested by arXiv:2508.20576:

- a product algebra of automorphic vectors;
- two decompositions of a four-point product corresponding to different pairings;
- equality by associativity/commutativity;
- after a spectral-resolution interface, identify this equality as a crossing/spectral-reciprocity equation;
- map trilinear coefficients to the appropriate automorphic periods.

Do not pretend a spectral decomposition theorem exists in Lean before the required Hilbert/automorphic infrastructure is constructed.

### C. Adelic assembly

- assemble Archimedean and p-adic principal-series local data place by place;
- identify normalized local standard intertwiners and their scalar spherical eigenvalues;
- prove the restricted-product/global coefficient equals the completed zeta/L-function factorization in the unramified case;
- relate global Weyl reflection to the existing Shadow framework.

### D. Operator algebra / QSM bridge

The largest conceptual gap toward a literal full CFT is the observable/operator algebra and state structure. Bost–Connes is not a random analogy: it supplies a genuine C*-dynamical system, KMS states, a logarithmic Hamiltonian spectrum, arithmetic symmetry, and zeta partition function. Determine whether an appropriate representation/crossed-product or boundary algebra can carry the `PGL2` conformal action and connect its correlation functions to the automorphic crossing sector.

## RH relevance

This program does not prove RH. Its potential relevance is structural: if the genuine Weil explicit-formula quadratic form can be realized as a reflection-positive/unitary/crossing-positive form in the arithmetic conformal theory, then CFT positivity techniques may become available. The decisive theorem would still have to identify the exact classical Weil form on a sufficient test class and prove its positivity unconditionally.
