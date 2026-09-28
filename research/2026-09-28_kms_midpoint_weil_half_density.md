# Weil half-density weights are exact critical KMS-midpoint norms in the Bost-Connes shift sector

Date: 2026-09-28
Status: exact C*-dynamical/KMS identity; no RH claim. This uses only the standard Bost-Connes time evolution and KMS invariance.

## 1. Abstract shift sector

Let \((\mathcal A,\sigma_t,\omega_1)\) be the Bost-Connes system at its critical KMS inverse temperature \(\beta=1\).

For the canonical multiplicative isometries \(\mu_n\),
\[
\mu_n^*\mu_n=1,
\qquad
\sigma_t(\mu_n)=n^{it}\mu_n.
\]

The KMS state is invariant under the real-time dynamics.

For analytic elements define the midpoint sesquilinear form
\[
\langle A,B\rangle_{\rm mid}
:=
\omega_1\!\left(A^*\sigma_{i/2}(B)\right).
\]

General KMS/standard-form theory identifies this midpoint form with the Osterwalder-Schrader/modular positive form on the appropriate analytic domain.

## 2. Exact orthogonality of multiplicative channels

Since
\[
\sigma_t(\mu_m^*\mu_n)
=
(n/m)^{it}\mu_m^*\mu_n,
\]
invariance of \(\omega_1\) gives, for \(m\ne n\),
\[
\omega_1(\mu_m^*\mu_n)=0.
\]

For \(m=n\),
\[
\omega_1(\mu_n^*\mu_n)=1.
\]

Also
\[
\sigma_{i/2}(\mu_n)=n^{-1/2}\mu_n.
\]

Therefore
\[
\boxed{
\langle\mu_m,\mu_n\rangle_{\rm mid}
=
\delta_{mn}\,n^{-1/2}.
}
\]

Thus the critical arithmetic half-density is exactly the squared norm of the multiplicative shift channel in the KMS midpoint Hilbert form.

## 3. Von Mangoldt weights are midpoint channel energies

For a prime power \(n=p^k\), define
\[
A_{p,k}:=\sqrt{\log p}\,\mu_{p^k}.
\]

Then
\[
\boxed{
\|A_{p,k}\|_{\rm mid}^2
=
(\log p)p^{-k/2}
=
\frac{\Lambda(p^k)}{\sqrt{p^k}}.
}
\]

Hence every finite-place coefficient occurring in the critical Weil explicit formula is literally a critical KMS-midpoint norm square of one prime-power channel.

This is termwise exact and uses no zeros.

## 4. Why this does not trivialize Weil positivity

In the Weil form the prime-power coefficient multiplies a reflected TRANSLATION correlation
\[
h(\log p^k),
\]
and enters with the sign fixed by the explicit formula.

The KMS identity above proves positivity of the local CHANNEL NORM, not positivity of the globally assembled reflected pairing.

The missing operation is exactly the one already isolated in the project:
couple the orthogonal KMS prime channels to the BPY/Archimedean boundary state before scalarization.

In particular, replacing the Weil prime term by a sum of independent positive diagonal norms loses the cross-boundary translation data and cannot prove RH.

## 5. Exact match to the current holographic architecture

The three relevant half-density appearances now have independent exact derivations:

1. prime torus / Hardy:
   \[
   \sum |n^{-s}|^2<\infty
   \iff \Re s>1/2;
   \]

2. BPY decimation:
   \[
   Q_{\rm div}(n)^{1/4}=n^{-1/2}(Q^{(n)})^{1/4};
   \]

3. Bost-Connes KMS midpoint:
   \[
   \|\mu_n\|_{\rm mid}^2=n^{-1/2}.
   \]

So the factor \(n^{-1/2}\) in Weil's prime current is simultaneously:
- a Hardy Hilbert threshold;
- a Gaussian radial scaling dimension;
- a modular/KMS midpoint norm.

The coincidence is structural, not a normalization choice.

## 6. Concrete closure target

For a test function \(f\), seek an operator-valued feature
\[
\mathcal A_f
\]
in a product/standard-form Hilbert space combining:
- the critical Bost-Connes KMS shift channels;
- the BPY Gaussian field;
- the Archimedean SU(1,1)/theta channel;

such that
\[
\boxed{
W(f*\widetilde f)
=
\|\mathcal A_f\|_{\rm OS}^2
}
\]
after the one coherent counterterm is included internally.

The local prime coefficient required by this identity is now already exact. The unsolved part is only the global cross-sheet sewing and its Archimedean counterterm.
