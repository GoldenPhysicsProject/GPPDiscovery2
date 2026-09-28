# Finite self-dual divisor geometry: the critical KMS/GCD kernel is a Fourier-sublattice Gram matrix

Date: 2026-09-28
Status: exact finite arithmetic/Fourier identities, derived zero-independently. This is a new synthesis inside the GPP programme. No RH claim.

## 1. Finite self-dual model of the number line

Let
\[
G_N=\mathbb Z/N\mathbb Z
\]
with the unitary discrete Fourier transform
\[
(\mathcal F_N f)(k)
=
\frac1{\sqrt N}
\sum_{x\in G_N}
f(x)e^{-2\pi i kx/N}.
\]

For each divisor \(d\mid N\), let
\[
H_d=d\mathbb Z/N\mathbb Z
\]
be the subgroup of multiples of \(d\). Its size is
\[
|H_d|=\frac Nd.
\]

Define the normalized subgroup state
\[
\boxed{
v_d
=
|H_d|^{-1/2}\mathbf 1_{H_d}
\in\ell^2(G_N).
}
\]

These states are completely zero-independent and are built only from the additive lattice and its finite-index sublattices.

## 2. Fourier duality is divisor complementation

The annihilator of \(H_d\) is
\[
H_d^\perp
=
H_{N/d}.
\]

Indeed a character \(x\mapsto e^{2\pi i kx/N}\) is trivial on \(d\mathbb Z/N\mathbb Z\) iff \(k\) is a multiple of \(N/d\).

The normalized subgroup state transforms EXACTLY as
\[
\boxed{
\mathcal F_N v_d
=
v_{N/d}.
}
\]

Proof: on \(H_d^\perp\), the unnormalized Fourier sum equals \(|H_d|\); dividing by \(\sqrt N\sqrt{|H_d|}\) gives
\[
\sqrt{\frac{|H_d|}{N}}
=
\frac1{\sqrt d},
\]
which is exactly the amplitude of the normalized indicator of the annihilator, whose size is \(d\).

Thus the half-density normalization is forced by unitarity of finite additive Fourier duality.

## 3. The critical TFD/GCD kernel appears as the subgroup Gram matrix

For divisors \(d,e\mid N\),
\[
H_d\cap H_e
=
H_{\operatorname{lcm}(d,e)}.
\]

Therefore
\[
\begin{aligned}
\langle v_d,v_e\rangle
&=
\frac{|H_d\cap H_e|}
{\sqrt{|H_d||H_e|}}\\
&=
\frac{N/\operatorname{lcm}(d,e)}
{\sqrt{(N/d)(N/e)}}\\
&=
\frac{\sqrt{de}}{\operatorname{lcm}(d,e)}\\
&=
\boxed{
\frac{\gcd(d,e)}{\sqrt{de}}.
}
\end{aligned}
\]

This is EXACTLY the critical arithmetic TFD two-point kernel previously derived independently:
\[
K_{1/2}(d,e)
=
\frac{\gcd(d,e)}{\sqrt{de}}.
\]

Hence:

\[
\boxed{
\text{critical KMS/TFD geometry}
=
\text{Gram geometry of finite-index sublattices of a self-dual additive number line}.
}
\]

This identifies the KMS half-density and Poisson/Fourier self-duality as two descriptions of the SAME finite geometry, not merely two mechanisms that happen to select \(1/2\).

## 4. Prime inclusions produce the half-density p^{-1/2} exactly

If \(p\mid N/d\), then
\[
H_{dp}\subset H_d
\]
with index \(p\).

Their normalized overlap is
\[
\boxed{
\langle v_d,v_{dp}\rangle
=
p^{-1/2}.
}
\]

Thus the ubiquitous critical factor \(p^{-1/2}\) is simply the cosine/overlap between normalized states of a subgroup and its prime-index sublattice.

This gives a very concrete meaning to the prime KMS midpoint:
a prime is an elementary INDEX-\(p\) refinement of the additive lattice.

Prime powers are repeated subgroup refinements.

## 5. Squarefree primorials give an exact prime Hodge cube

Now take
\[
N=P^\#=\prod_{p\le P}p
\]
squarefree.

Every divisor is uniquely
\[
d_S=\prod_{p\in S}p
\]
for a subset \(S\) of the finite prime set \(\mathcal P_P\).

Therefore the divisor lattice is the Boolean cube
\[
2^{\mathcal P_P}.
\]

Fourier annihilator duality is
\[
d_S
\longmapsto
\frac N{d_S}
=
d_{S^c}.
\]

So on divisor labels,
\[
\boxed{
\mathcal F_N:
S\longmapsto S^c.
}
\]

This is precisely the unsigned combinatorial core of Hodge-star/Poincare duality on an exterior algebra: degree \(k\) is paired with complementary degree \(|\mathcal P_P|-k\).

The Möbius function is
\[
\boxed{
\mu(d_S)=(-1)^{|S|},
}
\]
the fermion/parity grading of that same prime-subset exterior algebra.

Thus at finite primorial cutoff we have, in one exact object:

- additive Fourier self-duality;
- prime factorization;
- a Boolean/exterior prime complex;
- degree-complement duality;
- Möbius fermion parity;
- the critical half-density metric.

This is a concrete Hodge realization of the "self-dual number line" intuition.

## 6. Tensor factorization of the critical Gram matrix

For squarefree \(N\), the Gram kernel factorizes prime by prime.

At one prime \(p\), with local basis "absent/present",
\[
K_p
=
\begin{pmatrix}
1&p^{-1/2}\\
p^{-1/2}&1
\end{pmatrix}.
\]

Therefore
\[
\boxed{
K_N
=
\bigotimes_{p\mid N}K_p.
}
\]

The local eigenvectors are
\[
(1,1),\qquad(1,-1)
\]
with eigenvalues
\[
1+p^{-1/2},
\qquad
1-p^{-1/2}.
\]

The global Möbius parity vector
\[
\mu(d_S)=(-1)^{|S|}
\]
is exactly the tensor product of all local antisymmetric vectors. Hence
\[
\boxed{
K_N\mu
=
\left[
\prod_{p\mid N}(1-p^{-1/2})
\right]\mu.
}
\]

As the primorial cutoff grows,
\[
\prod_{p\le P}(1-p^{-1/2})
\to0.
\]

So the previously observed critical Möbius-null/Hagedorn direction has an exact finite geometric origin:
it is the all-prime antisymmetric Hodge-parity state whose Gram eigenvalue collapses in the infinite-prime limit.

This is much sharper than saying that "the KMS state becomes singular at beta=1."

## 7. What the primes are doing physically

This gives a concrete interpretation.

The additive number line is self-dual under Fourier/Poisson.

A prime \(p\) does not merely contribute a local Euler factor. It labels the elementary refinement
\[
\mathbb Z
\supset
p\mathbb Z
\]
of the additive lattice.

In the finite self-dual model, Fourier turns a subgroup into its reciprocal/annihilator subgroup:
\[
d\mathbb Z/N\mathbb Z
\leftrightarrow
(N/d)\mathbb Z/N\mathbb Z.
\]

Thus the prime-generated multiplicative hierarchy and the additive Fourier duality are literally acting on the SAME family of lattice states.

The primes are the elementary scale/refinement operators of the self-dual lattice.

The critical \(1/2\) is the normalization that makes those lattice states transform unitarily.

## 8. Why the prime torus alone cannot produce the Riemann spectrum

The compact prime torus carries the multiplicative characters, but its scaling generator has frequencies
\[
\sum_p k_p\log p
=
\log q,
\qquad q\in\mathbb Q_+^\times,
\]
which are dense in \(\mathbb R\).

So compactness of the prime torus by itself does NOT give the discrete Riemann ordinates.

The missing quantization comes from imposing the additive Fourier/Poisson self-duality on the same arithmetic degrees of freedom.

This strongly supports the current picture:

\[
\boxed{
\text{prime Fock/divisor bulk}
+
\text{additive self-dual boundary condition}
\longrightarrow
\text{collective discrete spectrum}.
}
\]

The zeros should therefore be sought as collective modes of the PHYSICAL QUOTIENT of this doubled arithmetic system, not as local prime energies.

## 9. Hodge/Koszul interpretation

The squarefree divisor cube is already the finite prime Koszul complex.

- adding a prime is a creation/coboundary direction;
- removing a prime is its adjoint/boundary direction;
- Möbius sign is fermion parity;
- divisor complementation is the unsigned Hodge-star skeleton;
- the critical GCD/KMS Gram is the physical metric inherited from the additive self-dual group.

The causal prime Koszul gap constructed earlier is therefore naturally the BULK Hodge gap of this divisor complex.

What RH still asks is whether, after coupling this bulk to the additive Fourier-self-dual boundary and the Archimedean real place, the resulting boundary Schur complement is positive/self-adjoint and has principal-series Casimir spectrum.

## 10. Connection to BSD, Hodge, and Yang--Mills

This finite model sharpens the broader trichotomy.

### RH
The prime-divisor Hodge bulk has no mysterious local zeros. The nontrivial zeros must arise after global self-dual sewing. RH says the resulting collective modes lie in the unitary principal series.

### BSD
For an elliptic curve, the scalar local prime refinement is replaced by a nontrivial local Frobenius representation. The natural analogue of the divisor Hodge complex should carry curve-dependent cohomology. The rank then has a plausible interpretation as the dimension of GLOBAL harmonic modes surviving all local sewing conditions; the Neron--Tate regulator is their Gram-volume.

### Hodge conjecture
The finite prime cube makes literal the distinction between abstract cohomological states and geometrically realized lattice/subgroup states. In a motivic generalization, the Hodge question becomes which harmonic cohomology classes are represented by genuine algebraic cycles.

### Yang--Mills
The analogous data are local gauge holonomies/constraints, a gauge/BRST complex, Hodge Laplacian, quotient by exact directions, and a positive gap on physical cohomology-perp. The arithmetic model shows explicitly how a massively gapped bulk can still leave a delicate physical boundary problem after sewing.

The common mechanism is therefore not "all four conjectures are the same." It is:

\[
\boxed{
\text{local generators}
\to
\text{cochain/Hodge bulk}
\to
\text{duality sewing}
\to
\text{physical quotient}
\to
\{\text{sign},\text{nullity},\text{gap},\text{realization}\}.
}
\]

## 11. Immediate research target

The next operator should be constructed first at squarefree primorial cutoff.

Let
\[
\mathcal V_N
=
\operatorname{span}\{v_d:d\mid N\}
\subset\ell^2(\mathbb Z/N\mathbb Z).
\]

On this space:
- the metric is exactly the critical GCD/KMS Gram;
- Fourier is exact divisor complementation;
- Möbius is exact fermion parity;
- prime creation/removal gives the finite Koszul complex.

Tensor this finite self-dual prime Hodge system with the Archimedean scaling line/prolate window and build the physical Schur complement there.

This finite system has EXACT unitarity before the limit, rather than approximate unitarity inferred afterward.

If its physical Casimir determinants converge to centered xi, RH follows while the principal-series property is inherited from finite self-adjointness.

This is now a concrete finite model of "what the primes are doing on the self-dual number line."
