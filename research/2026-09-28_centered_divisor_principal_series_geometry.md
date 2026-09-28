# Centered divisor coordinate: the principal-series line is the fixed center of finite arithmetic Hodge duality

Date: 2026-09-28
Status: exact finite arithmetic identity and representation-theoretic interpretation. No RH claim.

Let \(N=\prod_p p^{K_p}\), let \(d\mid N\), and define the centered logarithmic divisor coordinate
\[
\boxed{
\ell_N(d)
=
\log d-\frac12\log N
=
\sum_{p\mid N}
\left(v_p(d)-\frac{K_p}{2}\right)\log p.
}
\]

The finite additive Fourier transform sends the normalized divisor-subgroup state
\[
v_d\mapsto v_{N/d}.
\]

But
\[
\ell_N(N/d)
=
\log(N/d)-\frac12\log N
=
-\ell_N(d).
\]

Hence the finite Fourier/Hodge involution acts on the centered arithmetic scale coordinate exactly by
\[
\boxed{
\ell\mapsto-\ell.
}
\]

For real \(t\), define the centered scaling character
\[
\chi_t(d)=e^{-it\ell_N(d)}.
\]
Then divisor complementation sends
\[
\boxed{
\chi_t(N/d)=\chi_{-t}(d)=\overline{\chi_t(d)}.
}
\]

Thus the finite self-dual arithmetic model already carries the unitary reflection law of the one-dimensional principal series.

The ubiquitous half shift is now geometrically transparent. Before centering, the natural scale is \(\log d\). Hodge/Fourier duality reflects it about
\[
\frac12\log N.
\]
Equivalently, every local valuation coordinate
\[
a_p=v_p(d)\in\{0,\dots,K_p\}
\]
is reflected about
\[
K_p/2.
\]

After normalization of subgroup states, the index-\(p\) overlap is \(p^{-1/2}\). Therefore the same \(1/2\) appears simultaneously as:

1. the midpoint of local valuation/Hodge reflection;
2. the half-density required by normalized subgroup inclusion;
3. the Mellin-Plancherel unitary line of the real scaling representation.

This is not three unrelated coincidences. In the finite self-dual divisor model they are manifestations of one centered duality geometry.

What remains nontrivial is spectral QUANTIZATION. The real parameter \(t\) is continuous at this stage. The Riemann ordinates cannot arise from local duality alone. They must be the discrete collective values selected after:
- all prime valuation chains are sewn to the Archimedean coordinate by the product formula;
- additive Poisson self-duality is imposed globally;
- the rational/vacuum direction is quotiented;
- the resulting physical boundary/Casimir operator is reconstructed.

Therefore the current RH target can be stated particularly sharply:

> Prove that the physical quotient of the globally sewn finite self-dual divisor systems converges to a positive Hilbert representation of the centered dilation group. Its generator is then self-adjoint, so every collective spectral parameter \(t\) is real and every associated conformal weight is \(1/2+it\).

The unresolved theorem is not why the center is \(1/2\). The center is now forced geometrically. The unresolved theorem is why the zeros are exactly the spectrum of the positive physical quotient rather than resonances of a nonunitary scalar reconstruction.
