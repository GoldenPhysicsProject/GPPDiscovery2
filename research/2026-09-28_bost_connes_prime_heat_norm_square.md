# Critical Bost-Connes midpoint realizes the entire prime Gaussian heat trace

Date: 2026-09-28
Status: exact finite-cutoff identity and canonical quadratic-form limit. No RH claim.

This pushes the KMS-midpoint observation from individual Weil coefficients to the full Gaussian heat observable used in the AFT/OS criterion.

## 1. Critical midpoint Hilbert space

Let \((\mathcal A,\sigma_t,\omega_1)\) be the Bost-Connes system at the unique critical KMS state \(\beta=1\). For analytic elements define
\[
\langle A,B\rangle_{\rm mid}
=
\omega_1(A^*\sigma_{i/2}(B)).
\]

For the canonical multiplicative isometries,
\[
\sigma_t(\mu_n)=n^{it}\mu_n,
\qquad
\langle\mu_m,\mu_n\rangle_{\rm mid}
=
\delta_{mn}n^{-1/2}.
\]

Let \(L\) be the self-adjoint modular-frequency operator on the closed shift span, so
\[
L\mu_n=(\log n)\mu_n.
\]

## 2. Finite von-Mangoldt current vector

For a cutoff \(N\), define
\[
J_N
=
\sum_{2\le n\le N}\sqrt{\Lambda(n)}\,\mu_n.
\]

Then
\[
\|J_N\|_{\rm mid}^2
=
\sum_{n\le N}\frac{\Lambda(n)}{\sqrt n}.
\]

For every \(t>0\),
\[
e^{-L^2/(8t)}J_N
=
\sum_{n\le N}
\sqrt{\Lambda(n)}
e^{-(\log n)^2/(8t)}
\mu_n.
\]

Therefore
\[
\boxed{
\left\|e^{-L^2/(8t)}J_N\right\|_{\rm mid}^2
=
\sum_{n\le N}
\frac{\Lambda(n)}{\sqrt n}
e^{-(\log n)^2/(4t)}.
}
\]

Equivalently,
\[
\boxed{
K_{P,N}(t)
=
\frac1{\sqrt{4\pi t}}
\left\|e^{-L^2/(8t)}J_N\right\|_{\rm mid}^2
}
\]
is exactly the finite-prime-power Gaussian heat term of the completed arithmetic heat trace.

No zeta zeros occur.

## 3. Infinite cutoff is automatically finite after heat smoothing

For every fixed \(t>0\),
\[
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
e^{-(\log n)^2/(4t)}
<\infty.
\]

Indeed \(\Lambda(n)\le\log n\), and after \(x=\log n\) the Gaussian suppresses the \(e^{x/2}\) counting growth super-exponentially in \(x^2\).

Hence \(e^{-L^2/(8t)}J\) exists as a genuine midpoint-Hilbert vector even though the unsmoothed formal current \(J\) is not normalizable at the critical point.

Thus
\[
\boxed{
K_P(t)
=
\frac1{\sqrt{4\pi t}}
\left\|e^{-L^2/(8t)}J\right\|_{\rm mid}^2
}
\]
is an exact zero-independent KMS norm-square realization of the FULL prime-power heat contribution.

## 4. Real-time midpoint correlator is the prime-power Fourier current

For finite \(N\),
\[
\langle J_N,\sigma_u(J_N)\rangle_{\rm mid}
=
\sum_{n\le N}
\frac{\Lambda(n)}{\sqrt n}
e^{iu\log n}.
\]

After Gaussian smearing this converges for all \(u\):
\[
\boxed{
\left\langle e^{-L^2/(8t)}J,\,
\sigma_u\!\left(e^{-L^2/(8t)}J\right)
\right\rangle_{\rm mid}
=
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
e^{-(\log n)^2/(4t)}
e^{iu\log n}.
}
\]

The even real part is precisely the heat-smoothed prime cosine current.

So the finite-place part of the AFT heat kernel is not merely analogous to a thermal correlation: it is literally a critical KMS midpoint two-point function.

## 5. Additive Bost-Connes phases and exact finite-channel orthogonality

At \(\beta=1\), the unique KMS state restricts to Haar on the additive phase algebra:
\[
\omega_1(e(r))=0
\quad\text{for }r\ne0\in\mathbb Q/\mathbb Z.
\]

For
\[
A_{n,r}=\mu_n e(r),
\]
one obtains
\[
\boxed{
\langle A_{m,r},A_{n,s}\rangle_{\rm mid}
=
\delta_{mn}\delta_{rs}\,n^{-1/2}.
}
\]

For the opposite ordering \(B_{n,r}=e(r)\mu_n\),
\[
\boxed{
\langle B_{m,r},B_{n,s}\rangle_{\rm mid}
=
\delta_{mn}\,n^{-1/2}
\,\mathbf 1_{\{n(r-s)=0\ {\rm in}\ \mathbb Q/\mathbb Z\}}.
}
\]

Thus the semidirect ax+b relation supplies a nontrivial finite additive geometry inside each multiplicative energy channel. This is the correct place to couple Euler multiplicativity to lattice/additive self-duality.

## 6. The direct remaining theorem becomes a dilation/compression problem

The completed AFT heat trace has schematic form
\[
\mathscr K(t)
=
K_{\infty+\rm pole}(t)-K_P(t)
\]
with the exact prime term now represented as a midpoint norm square.

Therefore RH would follow if one constructs, without zero data, a positive Archimedean/pole KMS standard-form vector \(J_\infty(t)\) and a contraction \(V_t\) such that
\[
e^{-L^2/(8t)}J
=
V_tJ_\infty(t),
\]
and
\[
K_{\infty+\rm pole}(t)
=
\frac1{\sqrt{4\pi t}}\|J_\infty(t)\|^2.
\]

Then
\[
\mathscr K(t)
=
\frac1{\sqrt{4\pi t}}
\left(
\|J_\infty(t)\|^2-\|V_tJ_\infty(t)\|^2
\right)
\ge0.
\]

For OS/RH one needs the MULTI-TIME version, i.e. a single contraction/standard pair producing the entire Hankel matrix
\[
[\mathscr K(t_i+t_j)]_{ij},
\]
not just scalar positivity at each \(t\).

This is now a sharply defined operator-completion problem. The prime leg is finished exactly.

## 7. Important no-go

A literal spectral intertwiner from the discrete modular operator \(L\mu_n=(\log n)\mu_n\) into a purely absolutely-continuous Archimedean multiplication operator cannot be unitary on eigenvectors: point spectrum cannot be mapped into absent point spectrum by an exact unitary intertwining.

Therefore the required sewing cannot be a naive same-generator isometry. It must be:
- a compression/Schur map,
- a rigged/generalized spectral transform,
- or a nonlinear/second-quantized BPY map.

This is consistent with the already constructed connected BPY decimation intertwiner, where prime multiplication becomes a Koopman decimation rather than a continuous-spectrum eigenvector map.
