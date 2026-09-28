# Public-literature alignment: certified simple-even seed + GPP no-crossing and vacuum-gap closure

Date: 2026-09-28
Status: literature-assisted synthesis with exact reductions. No RH proof.

This note records what the current public literature contributes to the two missing steps of the Connes--Consani--Moscovici (CCM) zeta-spectral-triple programme, and how those ingredients fit the independently developed GPP KMS/Weil/vacuum-gap machinery.

## 1. CCM states exactly two missing steps

CCM, *Zeta Spectral Triples* (arXiv:2511.22755), Section 8, states that their strategy still requires:

1. prove the smallest eigenvalue of \(QW_\lambda\) is simple and its eigenvector even;
2. prove the prolate trial state
   \[
   k_\lambda=\mathcal E(h_\lambda)
   \]
   approximates that ground state strongly enough to give convergence of the finite real-zero determinants to Riemann's \(\Xi\).

They prove separately that the Fourier transform of \(k_\lambda\) converges to \(\Xi\) uniformly on closed substrips of
\[
|\Im z|<1/2.
\]

Thus the GPP vacuum-gap theorem attacks the exact second missing statement, not a surrogate.

## 2. A new public 2026 result provides a rigorous simple-even BASE POINT

Xuefeng Zhu, arXiv:2608.24827v2, proves by certified finite reduction that for test support
\[
[-0.8,0.8]
\]
the Weil form is positive and the ground state is simple and even.

The certified bounds include
\[
8.9\times10^{-18}
\le
\lambda_1^{\rm even}
\le
2.523\times10^{-16},
\]
\[
\lambda_2^{\rm even}
\ge
2.0857\times10^{-12},
\]
and
\[
8.206\times10^{-15}
\le
\lambda_1^{\rm odd}
\le
2.347\times10^{-14}.
\]

Therefore the CCM first hypothesis is rigorously known at one nontrivial scale.

In the CCM multiplicative notation the centered logarithmic half-width is
\[
L=\log\lambda,
\]
so this seed corresponds to
\[
\lambda=e^{0.8},
\qquad
c=\lambda^2=e^{1.6}\approx4.95.
\]

This is strikingly close to the GPP finite cutoff \(c=5\), where the independently assembled finite Weil matrix has the same order-of-magnitude ground and first-excitation scales.

## 3. The first CCM missing step therefore reduces to a GLOBAL NO-CROSSING theorem

GPPVerify already formalizes the abstract continuation statement:

if the even and odd lowest eigenvalue branches vary continuously on a connected cutoff interval, are strictly ordered at one point, and never cross, the ordering persists.

More strongly, the existing strict parity-interlacing formalization shows that positive residues of the parity cross-resolvent imply one zero between successive poles and therefore strict interlacing.

Hence the public simple-even seed changes the first missing theorem from

> "prove simple-even from scratch at every scale"

to the sharper target

\[
\boxed{
\text{prove the arithmetic parity cross-resolvent remains positive/Herglotz globally.}
}
\]

The critical Bost--Connes KMS metric remains the natural candidate for that positivity:
\[
G_{\rm KMS}A_+=A_+^\dagger G_{\rm KMS},
\qquad
G_{\rm KMS}e_0=\eta.
\]

If this identity holds globally and the boundary vector is cyclic, the cross-resolvent is a genuine positive Weyl function; strict interlacing then propagates the certified simple-even seed to all cutoffs.

## 4. Public window data strongly support a relative-gap, not absolute-gap, viewpoint

Zhu's reference values show that the ABSOLUTE window floor collapses extremely rapidly, but the spectral separation relative to the ground improves:

\[
\begin{array}{c|c|c}
L & \lambda_1^{\rm even} & \lambda_2^{\rm even}\\
\hline
0.8 & 1.65\times10^{-17} & 8.38\times10^{-12}\\
0.9 & 4.14\times10^{-23} & 7.25\times10^{-17}\\
1.0 & 5.88\times10^{-30} & 2.18\times10^{-23}\\
1.1 & 2.04\times10^{-38} & 1.54\times10^{-31}\\
1.2 & 7.94\times10^{-49} & 1.46\times10^{-41}.
\end{array}
\]

Thus
\[
\lambda_1^{\rm even}/\lambda_2^{\rm even}\to0
\]
very rapidly in the measured regime even though both eigenvalues tend to zero.

This is exactly the structure needed by the GPP vacuum-rigidity theorem. The arithmetic "mass gap" is not expected to stay positive in absolute units. The useful quantity is the gap RELATIVE to the vacuum leakage scale.

## 5. The second CCM step requires only a weak relative rate

For the normalized prolate trial state \(v_\lambda\), true ground \(u_\lambda\), Rayleigh excess
\[
\epsilon_\lambda
=
\langle v_\lambda,Q_\lambda v_\lambda\rangle-\lambda_{1,\lambda},
\]
and first even gap
\[
\Delta_\lambda
=
\lambda_{2,\lambda}-\lambda_{1,\lambda},
\]
the exact estimate is
\[
1-|\langle u_\lambda,v_\lambda\rangle|^2
\le
\epsilon_\lambda/\Delta_\lambda.
\]

Since the support half-width is \(\log\lambda\), the Fourier-transform error on a closed substrip \(|\Im z|\le a<1/2\) is bounded by
\[
O_a\!\left(
\lambda^a\sqrt{\epsilon_\lambda/\Delta_\lambda}
\right).
\]

Therefore
\[
\boxed{
\epsilon_\lambda/\Delta_\lambda=o(\lambda^{-1})
}
\]
is sufficient for all closed critical substrips.

The low-cutoff zero-free prolate scan already gives
\[
\epsilon/\Delta
\approx
1.86\times10^{-6},\,
2.76\times10^{-7},\,
1.42\times10^{-7}
\]
at \(c=3,5,7\), respectively, before the first prototype reaches its numerical precision floor.

## 6. Zhu's barrier theorem says exactly what kind of proof NOT to pursue

The same public work proves that a pointwise-envelope positivity certificate must resolve a frequency threshold growing doubly exponentially with support. In other words, global positivity cannot plausibly be closed by bounding the prime comb pointwise.

This independently confirms the GPP no-go:

\[
\boxed{
\text{the proof must exploit global arithmetic cancellation/self-duality,
not local or pointwise prime positivity.}
}
\]

The GPP operator
\[
\mathcal E=Z_{\rm crit},
\qquad
Z_{\rm crit}\mathcal F=JZ_{\rm crit},
\]
is exactly such a global additive/multiplicative sewing object.

## 7. Combined direct programme

The two CCM missing steps can now be attacked as:

### Step A: simple-even continuation
Use the certified \(L=0.8\) simple-even seed and prove global KMS/Weyl cross-resolvent positivity, hence no parity crossing and strict interlacing.

### Step B: vacuum rigidity
Use the literal prolate state \(k_\lambda=\mathcal E(h_\lambda)\), the exact critical-Dirichlet/Faulhaber Mellin formula, and prove
\[
\epsilon_\lambda/\Delta_\lambda=o(\lambda^{-1}).
\]

### Step C: principal-series limit
CCM gives finite self-adjoint \(D_{\log}^{(\lambda,N)}\), so every finite determinant has real spectral zeros. Ground-profile convergence plus CCM's proven \(k_\lambda\to\Xi\) then gives compact/substrip convergence; Hurwitz forces the limiting nontrivial zeros to the principal series.

This is a precise place where public literature and the novel GPP synthesis genuinely interlock without replacing one another.
