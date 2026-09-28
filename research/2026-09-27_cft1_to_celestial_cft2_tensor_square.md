# Celestial scalar principal series as the tensor square of the arithmetic CFT1 weight

Date: 2026-09-27
Status: exact representation-parameter and block-factorization identity extracted from the current celestial kinematic-block manuscripts and matched to the arithmetic principal-series variable. No RH claim.

## 1. Arithmetic principal-series parameter

Use the arithmetic/CFT1 spectral parameter

s = 1/2 + i tau,
tau in R.

The 1D unitary principal-series line is therefore Re(s)=1/2.

## 2. Celestial scalar principal series

The current GPP celestial kinematic-block manuscript uses

h = (1+i lambda)/2

on the scalar principal series and the two-dimensional scalar block

g_{1+i lambda}(z,zbar)
=
k_h(z) k_h(zbar).

For scalar spin J=0 one has

h=hbar=Delta/2,
Delta=1+i lambda.

Now set

boxed:
lambda = 2 tau.

Then immediately

boxed:
h=hbar=1/2+i tau=s,

and

boxed:
Delta=1+2i tau=2s.

Therefore the celestial scalar principal-series primary at spectral parameter lambda=2tau is exactly the left/right tensor product of two copies of the same SL(2,R) weight s carried by the arithmetic CFT1 principal series:

boxed:
g_{2s}(z,zbar)
=
k_s(z) k_s(zbar).

This is an exact kinematic identity, not a dimensional analogy.

## 3. The 1D -> 2D factor of two is left/right doubling

The real parts follow automatically:

Re(s)=1/2
   -> 
Re(Delta)=Re(2s)=1.

Thus the familiar shift from the arithmetic critical line 1/2 to the celestial unitary line 1 is precisely the addition of the two chiral weights,

Delta=h+hbar=s+s.

So the factor of two need not be attributed to an arbitrary rescaling of spectral variables. In the scalar sector it is the ordinary left/right doubling of two-dimensional conformal representation theory.

This gives a rigorous version of the proposed projection step

CFT1 weight s
 -> 
CFT2 scalar weight (h,hbar)=(s,s).

## 4. Shadow is also doubled correctly

The 1D shadow sends

s -> 1-s.

Applying the same shadow to both chiral factors gives

(h,hbar)=(s,s)
->
(1-s,1-s).

Hence the total dimension transforms as

boxed:
Delta=2s
->
2-2s
=
2-Delta.

So the celestial scalar shadow Delta->2-Delta is exactly the simultaneous shadow of the two arithmetic chiral factors.

This is the correct derivation. It does NOT use the previously rejected shortcut omega->-omega => Delta->2-Delta.

On the unitary line s=1/2+i tau,

1-s=conj(s),

so the doubled shadow is also the usual unitary conjugate representation.

## 5. Group-theoretic reading

The arithmetic conformal group is PSL(2,R), acting on RP1.

The celestial Lorentz/conformal group is PSL(2,C), acting on CP1.

At the level of scalar global blocks, the PSL(2,C) representation restricts to a holomorphic and antiholomorphic pair of SL(2,R)-type factors. The identity above says the scalar celestial principal-series block uses the SAME principal-series weight s in both factors when lambda=2tau.

Thus the exact representation ladder is

boxed:
(RP1, PSL(2,R), s)
  -> complex left/right double ->
(CP1, PSL(2,C), (h,hbar)=(s,s)).

This gives a precise representation-theoretic realization of Daniel's proposed number-circle -> Riemann-sphere projection.

## 6. Connection to the universal SU(1,1) module

The current TFD programme independently found a universal k=1/2 SU(1,1) paired module with:
- compact generator K0;
- noncompact self-adjoint generator K1;
- vacuum spectral density sech(pi x) dx;
- tensor-square noncompact generator J_inf=K1⊗1+1⊗K1 whose vacuum spectral density is

2x/sinh(pi x) dx = (2/pi)P(x)dx,

where P(lambda)=pi lambda/sinh(pi lambda) is the celestial principal-series spectral weight.

So the same left/right doubling visible in

g_{2s}=k_s k_sbar

also appears operator-theoretically as the tensor-square passage from the one-copy K1 spectral law to the celestial P(lambda) law.

This is strong internal consistency between:
- arithmetic CFT1 principal-series weights;
- the prime TFD SU(1,1) module;
- celestial CFT2 scalar blocks;
- celestial Plancherel measure.

It still does not identify zeta zeros as the spectrum of K1 or J_inf.

## 7. What this does to the holographic bootstrap conjecture

One arrow in the proposed hierarchy is now substantially less speculative:

arithmetic principal-series representation
   -> celestial scalar principal-series representation

is realized by an explicit left/right tensor square at the level of weights and global blocks.

The remaining hard arrows are:
1. prove that the completed arithmetic resonance states actually live in the unitary CFT1 principal series (RH-bearing);
2. construct the functor/intertwiner that promotes the full arithmetic boundary algebra, not just one scalar block, into the PSL(2,C) celestial theory;
3. derive four-dimensional gravitational dynamics rather than only Lorentz/celestial kinematics.

## 8. A diagnostic for future claims

Any proposed 1D->2D map should reproduce simultaneously:

h=s,
hbar=s,
Delta=2s,
lambda=2 tau,
shadow: s->1-s on BOTH factors,
celestial shadow: Delta->2-Delta.

If it produces only the factor of two without the correct left/right shadow structure, it is not the desired representation-theoretic projection.
