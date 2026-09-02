# Split-signature Penrose/Fourier googly reduction

## Key correction

The linear googly problem should be formulated in the complexified theory with split signature (2,2) as the calculational real slice, not with Lorentzian SU(2,2) polarity as the fundamental mechanism.

In split signature:

- real twistor space is RP^3;
- the Penrose transform becomes the real X-ray transform on projective lines;
- lambda and tilde-lambda are independent real SL(2,R) spinors;
- Witten half-Fourier transforms relate momentum wavefunctions to twistor and dual-twistor representations;
- the full twistor-to-dual-twistor Fourier transform is a change of representation through the same momentum wavefunction;
- celestial chiral light transforms correspond to the half-Fourier transforms, and their product is ordinary shadow.

## Exact linear commuting-square mechanism

Let M_h be a momentum-space solution of fixed helicity h. Let

T_h : M_h -> Tw_h

be the half-Fourier transform to twistor space, and

Tbar_h : M_h -> TwDual_h

be the complementary half-Fourier transform to dual twistor space.

Define the full twistor Fourier map by

F_h = Tbar_h o T_h^{-1}.

For the real split Penrose/X-ray transforms P and P*, the standard reconstruction formulae imply

P(T_h m) = B(m),
P*(Tbar_h m) = B(m),

for the same bulk massless field B(m). Therefore

P* o F_h = P

on the domain where Fourier inversion and the X-ray transforms are valid.

This is the actual linear Penrose/Fourier commuting square. It is not a conjectural identification of shadow with Wigner time reversal.

## Why this becomes googly

The Fourier representation change alone reconstructs the same tensor field. The helicity/SD-ASD exchange enters only when orientation is reversed.

In split signature, star^2=+1 and the real two-form space decomposes into +/-1 eigenspaces. Under orientation reversal:

star_o -> -star_o.

Thus the same tensor that is SD for orientation o is ASD for -o, and conversely.

So after interpreting the dual-twistor representation as the opposite-orientation twistor geometry, the exact linear statement is

P_+ o F = R_o o P_-,

where R_o does not alter the underlying tensor components; it changes the orientation used to define Hodge chirality.

This is the cleanest linearized googly reduction found so far.

## Weight check

For doubled helicity n=2h, twistor weight is k=n-2. Four-dimensional Fourier/Serre duality gives

k -> -k-4 = -n-2,

which is the dual-twistor weight for the same physical momentum state and numerically the ordinary twistor weight of opposite helicity -h. This is exactly compatible with the orientation relabeling above.

## Celestial check

Brown-Gowdy-Spence establish in split signature that half-Fourier transforms correspond to chiral light transforms. Their product gives

(h, hbar) -> (1-h, 1-hbar),

hence

Delta -> 2-Delta,
J -> -J.

Thus the same operator chain has the required celestial shadow labels without identifying shadow with T or CPT.

## Literature anchors

- Brown, Gowdy, Spence, Celestial Twistor Amplitudes, Phys. Rev. D 108, 066009 (2023), arXiv:2212.01327.
- Mason, Gravity from holomorphic discs and celestial Lw_{1+infty} symmetries: split Penrose/X-ray and half-Fourier formulae.
- Aryapoor, The Penrose Transform in the Split Signature, Differential Geometry and its Applications 30 (2012) 334-346.
- Eastwood, The Twistor Construction and Penrose Transform in Split Signature.

## Formalization

New exact reduction module:

GppVerify/CelestialHolography/SplitSignaturePenroseFourierSquare.lean

It formalizes the representation-change theorem and orientation-induced chirality relabeling. The analytic Fourier/X-ray inversion hypotheses remain external mathematical inputs until integral/function-space formalization is added.

## Remaining gap before claiming linear googly solved

Need to instantiate the abstract bridge with the concrete split-signature function spaces and prove:

1. half-Fourier inversion with the exact normalization and allowed distributions;
2. X-ray/Penrose reconstruction for helicity +/-1 and +/-2 (or general n/2);
3. compatibility of the twistor-to-dual-twistor transform with projective homogeneity and parity labels;
4. the orientation identification between dual twistor geometry and the opposite-orientation copy;
5. gauge/cohomology equivalence where one analytically continues back to complex/Lorentzian signature.

The nonlinear googly problem remains separate and much harder: full Ward/nonlinear-graviton data must be transported, not just linear massless fields.
