# Shadow-pair metric rigidity: why the polarization must be Haar-fixed

Date: 2026-09-18

Consider the two-state first-order shadow block

Q_a =
[[0,-a^{-1}],
 [a,0]],

with a in C*, so Q_a^2=-I.

Let the positive Hermitian metric in the shadow-pair basis be diagonal

G=diag(g_+,g_-), g_+,g_->0.

Then the condition that Q_a be skew-adjoint in the G metric is

Q_a^* G + G Q_a = 0.

Direct multiplication gives the single condition

g_+ = |a|^2 g_-.

Therefore for EVERY nonzero a there exists a positive metric making Q_a skew-adjoint:
take, for example, g_-=1 and g_+=|a|^2.

This is a decisive no-go for a weak Rosati/polarization argument:
"there exists some positive polarization making shadow adjoint" does not force |a|=1.
The metric can absorb the off-critical modulus.

Now impose shadow self-duality of the metric. Let

R=[[0,1],[1,0]]

swap the two orientations. R is G-unitary iff

R^* G R = G,

which is equivalent to

g_+=g_-.

Combining:
g_+=|a|^2g_- and g_+=g_-
implies |a|=1.

For the RH Cayley coordinate a=beta(s)=(s-1)/s, |a|=1 iff Re(s)=1/2.

Thus the correct rigidity theorem is:

FIXED HAAR POLARIZATION + SHADOW ISOMETRY + FIRST-ORDER METRIC COMPATIBILITY
=> critical line.

The key word is fixed. The positive metric must be constructed independently of s and of the zeros. Inversion-invariant Haar measure provides exactly this kind of equal-weight geometry: the two orientations related by r->1/r have equal norm.

In the finite boundary-dipole model R_N is literally unitary and exchanges the two endpoints, so the finite metric is shadow-balanced. The obstruction in the infinite causal limit is that the far endpoint can escape the Hilbert space, destroying the equal-weight comparison exactly where the RH ghost lives.

This clarifies the global target:
construct a completed two-edge arithmetic Hilbert space in which
1. inversion/shadow is a unitary swap,
2. the zero/resonance channel is represented in the space (or rigged completion),
3. the first-order functional shadow operator is skew-adjoint with respect to the SAME fixed Haar metric.

If all three hold, off-critical modulus cannot be absorbed by a state-dependent polarization and the critical line follows.

This also explains why scalar CayleyShadowAdjointBridge is algebraically correct but not by itself a proof: it assumes the two operations are compared in one fixed Hilbert metric. The global analysis must supply that common metric on the actual arithmetic resonance space.