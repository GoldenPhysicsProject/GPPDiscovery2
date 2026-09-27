# Riemann-zero unfolding as K0 half-integer quantization on the SU(1,1) real spectral line

Date: 2026-09-27
Status: exact counting identities plus a representation-theoretic interpretation. This does not construct a Hilbert--Polya operator and does not prove RH.

## 1. The universal module already has the right compact spectrum

In the k=1/2 SU(1,1) module,
\[
K_0e_j=\left(j+\frac12\right)e_j,
\qquad j=0,1,2,\ldots
\]

Hence
\[
\operatorname{spec}(K_0)
=
\left\{
\frac12,\frac32,\frac52,\ldots
\right\}.
\]

If the positive nontrivial zero ordinates are indexed
\[
0<\gamma_1\le\gamma_2\le\cdots
\]
with multiplicity and the zero staircase is half-counted at a zero, then by definition
\[
N_0(\gamma_n)=n-\frac12.
\]

Therefore
\[
\boxed{
N_0(\gamma_n)
=
\left(n-\frac12\right)
=
\text{the }K_0\text{ eigenvalue on }e_{n-1}.
}
\]

This is an exact indexing identity. It does not say that gamma_n is an eigenvalue of K0.

## 2. The real place supplies the nonlinear unfolding map

The smooth zero count is
\[
u(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}
+\frac78.
\]

The 2,001,052-zero project dataset gave
\[
\delta_n
=
\left(n-\frac12\right)-u(\gamma_n)
\]
with mean approximately
\[
8.1\times10^{-8}
\]
and standard deviation
\[
0.33216.
\]

Thus
\[
\boxed{
u(\gamma_n)
\approx
\operatorname{spec}_{n-1}(K_0).
}
\]

The average unfolded nearest-neighbor spacing in the stored 2M sample is approximately one.

So the Archimedean Gamma factor maps the raw principal-series coordinate T to an almost uniformly spaced compact-action coordinate.

## 3. Exact phase-counting form

Let
\[
\theta(T)
=
\operatorname{Im}\log\Gamma\left(\frac14+\frac{iT}{2}\right)
-\frac T2\log\pi
\]
be the Archimedean Riemann--Siegel phase, with the usual continuous branch, and let
\[
S(T)=\frac1\pi\arg\zeta\left(\frac12+iT\right)
\]
be understood by midpoint continuation at a zero.

The exact counting relation is
\[
N_0(T)
=
1+\frac{\theta(T)}{\pi}+S(T).
\]

Hence at a zero,
\[
\boxed{
n-\frac12
=
1+\frac{\theta(\gamma_n)}{\pi}
+
S(\gamma_n).
}
\]

Equivalently,
\[
\boxed{
\theta(\gamma_n)+\pi S(\gamma_n)
=
\pi\left(n-\frac32\right).
}
\]

This is an exact phase quantization law for the zero staircase.

## 4. SU(1,1) polarization reading

The same universal module has:
- compact generator K0 with half-integer spectrum;
- noncompact generator K1 with continuous real spectral line and vacuum density sech(pi x) dx.

The celestial/principal-series coordinate is a real noncompact spectral parameter.

This suggests the following precise representation-theoretic reading:

\[
\boxed{
\text{continuous real spectral coordinate}
\;\xrightarrow{\text{global completed phase}}\;
\text{compact half-integer action levels}.
}
\]

The zero ordinates are not eigenvalues of the free K1 operator; K1 has continuous spectrum.

Rather, they are discrete points on the real principal-series line selected by the global phase condition
\[
1+\theta/\pi+S
\in
\frac12+\mathbb Z_{\ge0}.
\]

## 5. Smooth and oscillatory pieces match the two-place decomposition

Stirling gives
\[
1+\frac{\theta(T)}{\pi}
=
u(T)+O(T^{-1}).
\]

So:
- the Archimedean Gamma factor supplies the smooth action/unfolding;
- the arithmetic part S(T) supplies the fluctuating displacement from the half-integer lattice.

The 2M-zero residual
\[
\delta_n
=
(n-\tfrac12)-u(\gamma_n)
\]
is therefore the data-level version of the total phase correction beyond the smooth Archimedean action.

This aligns with the separate Fourier experiment in which the fluctuations reconstruct the prime-power current
\[
\Lambda(n)n^{-1/2}
\]
at logarithmic lengths log n.

## 6. Prime delay interpretation

The finite-prime Blaschke calculation showed that
\[
(\log p)p^{-m/2}
\]
is the m-th Fourier coefficient of the excess group delay of the local prime channel.

Therefore, after the required global renormalization/analytic continuation, the arithmetic phase S(T) should be viewed as the integrated prime-delay contribution to the quantization condition.

Schematically,
\[
\boxed{
\text{Archimedean action phase}
+
\text{renormalized prime scattering phase}
=
\pi\times\text{compact half-integer level}.
}
\]

This is the exact architecture expected of a one-dimensional scattering quantization condition.

The missing theorem is to construct the global causal/passive scattering system whose phase is this completed phase without assuming the zero locations.

## 7. Why this is useful but not tautologically a proof

The equality
\[
N_0(\gamma_n)=n-\frac12
\]
is simply the half-count convention.

The nontrivial project-level content is that the same SU(1,1) module independently supplies:
1. the half-integer K0 spectrum;
2. the continuous K1 principal-series line;
3. the prime coherent-state/Blaschke channels;
4. the Archimedean Plancherel law.

This makes the usual zero-unfolding relation fit a concrete compact/noncompact polarization pair rather than an abstract relabeling.

To prove RH one would still need to show, zero-independently, that the completed scattering/Schur system is self-adjoint/inner so that all selected spectral points lie on the real K1 line.
