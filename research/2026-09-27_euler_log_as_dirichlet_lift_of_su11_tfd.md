# The Euler logarithm is the Dirichlet-space lift of the prime SU(1,1) coherent state

Date: 2026-09-27
Status: exact Hilbert-space identities. This connects the TFD/SU(1,1) module to the prime Fock/log-determinant construction. No RH proof.

## 1. Hardy/SU(1,1) coherent vector

On the compact basis e_m, m>=0, define the unnormalized coherent vector
\[
h_z
=
\sum_{m\ge0}z^m e_m,
\qquad |z|<1.
\]

Its normalized version is
\[
\Omega_z
=
\sqrt{1-|z|^2}\,h_z.
\]

This is the k=1/2 SU(1,1) coherent/TFD state.

Let
\[
N=K_0-\frac12,
\qquad
Ne_m=me_m.
\]

## 2. Half-integrate the nonvacuum coherent state

On the nonvacuum subspace define
\[
N^{-1/2}e_m
=
m^{-1/2}e_m,
\qquad m\ge1.
\]

Then
\[
\boxed{
v(z)
=
N^{-1/2}(h_z-e_0)
=
\sum_{m\ge1}
\frac{z^m}{\sqrt m}\,e_m.
}
\]

Its inner product is
\[
\boxed{
\langle v(z),v(w)\rangle
=
\sum_{m\ge1}
\frac{(\bar zw)^m}{m}
=
-\log(1-\bar zw).
}
\]

Thus the logarithmic Euler kernel is the N^{-1/2} Sobolev/Dirichlet lift of the ordinary SU(1,1) coherent kernel.

## 3. Local bosonic free energy is a Dirichlet norm

For a Gibbs mode of energy E with inverse temperature beta, the TFD amplitude is
\[
z=e^{-\beta E/2}.
\]

Then
\[
\|v(z)\|^2
=
-\log(1-e^{-\beta E}).
\]

For a prime mode E_p=log p,
\[
z_{p,\beta}=p^{-\beta/2},
\]
hence
\[
\boxed{
\|v(z_{p,\beta})\|^2
=
-\log(1-p^{-\beta})
=
\log\zeta_p(\beta).
}
\]

Summing over primes, for beta>1,
\[
\boxed{
\sum_p\|v(z_{p,\beta})\|^2
=
\log\zeta(\beta).
}
\]

Therefore the zeta free energy is literally the total Dirichlet energy of the prime TFD coherent states.

## 4. The prime Fock coherent kernel is the exponential of this Dirichlet kernel

For a complex parameter s with Re(s)>1/2 define the global one-particle vector
\[
v_s
=
\bigoplus_p
\sum_{m\ge1}
\frac{p^{-ms}}{\sqrt m}\,e_{p,m}.
\]

Then
\[
\boxed{
\langle v_s,v_w\rangle
=
\log\zeta(\bar s+w).
}
\]

Passing to bosonic exponential vectors,
\[
\langle\varepsilon(v_s),\varepsilon(v_w)\rangle
=
\exp\langle v_s,v_w\rangle,
\]
gives
\[
\boxed{
\langle\varepsilon(v_s),\varepsilon(v_w)\rangle
=
\zeta(\bar s+w).
}
\]

So the already known prime-Fock zeta kernel is not separate from the TFD construction: it is its Dirichlet-space lift followed by ordinary bosonic second quantization.

## 5. Critical Haar boundary

At
\[
s=\frac12+it,
\]
the local amplitude has modulus
\[
|p^{-s}|=p^{-1/2},
\]
which is exactly the critical Haar/TFD amplitude.

The one-particle norm is
\[
\|v_s\|^2
=
\log\zeta(2\Re s).
\]

Hence
\[
\boxed{
\|v_s\|^2\to\infty
\quad\text{as}\quad
\Re s\downarrow\frac12.
}
\]

The divergence is the prime harmonic divergence in the first repetition mode:
\[
\sum_p p^{-1}.
\]

All diagonal repetition contributions m>=2 remain finite in this Hilbert norm.

Thus the critical global state escapes the ordinary one-particle/Fock Hilbert space while every finite-prime local TFD remains regular.

## 6. Repetition modes and the two regularization channels

The Dirichlet lift makes the repetition normalization explicit:
\[
v(z)
=
z e_1
+
\frac{z^2}{\sqrt2}e_2
+
\frac{z^3}{\sqrt3}e_3+\cdots.
\]

The first two analytic Euler-log terms are therefore exactly the first two compact modes
\[
e_1,\qquad e_2
\]
with the canonical Fock weights
\[
1,\qquad \frac1{\sqrt2}.
\]

This is the Hilbert-space origin of the vectors
\[
g_m(p)=\frac{p^{-m/4}}{\sqrt m}
\]
used in the critical repetition-channel analysis: for real s=1/2 they are the prime-index coefficients obtained by taking the square root of the m-th Euler-log weight.

## 7. Differentiating the Dirichlet kernel gives the SU(1,1) null current

The scalar logarithmic kernel satisfies
\[
z\frac{d}{dz}
[-\log(1-z)]
=
\frac{z}{1-z}.
\]

But the preceding SU(1,1) lightcone calculation gave
\[
\frac{z}{1-z}
=
\langle K_0+K_1\rangle_z-\frac12
\]
for real 0<z<1.

Therefore
\[
\boxed{
\text{Euler free energy}
\xrightarrow{\text{radial derivative}}
\text{SU(1,1) forward-null excess}.
}
\]

After multiplying by E_p=log p and summing over primes, this becomes
\[
-\frac{\zeta'}{\zeta}.
\]

So the free-energy, TFD-covariance, lightcone-current, and von-Mangoldt pictures are successive operations on one local coherent geometry.

## 8. One operator chain

The local structure can now be written as
\[
\boxed{
\Omega_z
\longrightarrow
N^{-1/2}(h_z-e_0)
\longrightarrow
-\log(1-\bar zw)
\longrightarrow
\exp[-\log(1-\bar zw)]
=
\frac1{1-\bar zw}.
}
\]

At finite places this chain becomes
\[
\boxed{
\text{TFD coherent state}
\to
\text{Dirichlet lift}
\to
\log\zeta
\to
\zeta.
}
\]

The remaining RH problem is still global positivity/causal sewing at the critical boundary, but the TFD and prime-Fock constructions are now explicitly the same local module at different Sobolev/Fock levels.
