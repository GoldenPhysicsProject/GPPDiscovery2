# Edge-derivative hierarchy: why the finite arithmetic vacuum gap should beat the Riemann tail

Date: 2026-09-28
Status: asymptotic derivation plus a sharpened closure target. No RH proof. This explains an existing numerical pattern and connects the Riemann-kernel radical tower to the vacuum-gap criterion.

## 1. Large-edge asymptotic of the Riemann kernel

For \(x\to+\infty\), Riemann's standard kernel has leading term
\[
\Phi(x)
=
\left(
2\pi^2 e^{9x/2}
-3\pi e^{5x/2}
+\cdots
\right)e^{-\pi e^{2x}},
\]
so
\[
\boxed{
\Phi(x)
\sim
2\pi^2 e^{9x/2}e^{-\pi e^{2x}}.
}
\]

Its logarithmic derivative therefore satisfies
\[
\frac{\Phi'(x)}{\Phi(x)}
=
\frac92-2\pi e^{2x}+o(1),
\]
hence
\[
\boxed{
\Phi'(x)
\sim
-2\pi e^{2x}\Phi(x).
}
\]

Iterating the dominant derivative gives, for every fixed \(k\),
\[
\boxed{
\Phi^{(k)}(x)
\sim
(-2\pi)^k e^{2kx}\Phi(x).
}
\]

## 2. At the zeta-triple window edge the hierarchy is polynomially separated

The finite Weil window has logarithmic half-width
\[
A=\log\lambda,
\qquad
L=2\log\lambda.
\]

At \(x=A\),
\[
e^{2A}=\lambda^2.
\]

Therefore
\[
\boxed{
\frac{|\Phi^{(k)}(A)|^2}{|\Phi(A)|^2}
\sim
(2\pi)^{2k}\lambda^{4k}.
}
\]

In particular the first derivative tail is larger than the vacuum tail by the scale
\[
\boxed{
|\Phi'(A)|^2/|\Phi(A)|^2
\sim
4\pi^2\lambda^4.
}
\]

Any local exterior quadratic form whose leading edge behavior is comparable on these narrow tails inherits the same \(\lambda^{4k}\) hierarchy.

## 3. This explains the previously mysterious numerical gap ratios

The independent GPP/Claude exterior-energy experiment measured
\[
E_{\rm ext}(\Phi')/E_{\rm ext}(\Phi)
\]
growing from roughly \(4.4\times10^2\) to \(7.7\times10^3\) across the tested window sequence.

The simple edge prediction is
\[
\text{ratio}\asymp \lambda^4
\]
up to a fixed factor from the derivative and the exterior energy density.

The observed values divided by \(\lambda^4\) are of roughly constant order, exactly as the asymptotic above predicts.

Thus the growing "excitation/vacuum" separation has a direct analytic origin: each derivative of the global radical profile costs two additional powers of \(e^x\) in amplitude at the edge, hence four powers of \(\lambda\) in quadratic energy.

## 4. Radical translations naturally generate this tower

If \(R_a(x)=\Phi(x-a)\), then every \(R_a\) remains in the global radical family because in Fourier space
\[
\widehat{R_a}(t)=e^{-iat}\widehat\Phi(t)
\]
retains the \(\Xi\) zero factor.

Expanding near \(a=0\),
\[
R_a
=
\sum_{k\ge0}
\frac{(-a)^k}{k!}\Phi^{(k)}.
\]

So the derivative tower is the tangent tower of the exact translation family of radical states.

This identifies the near-null finite-window excitations found numerically as the natural Goldstone-like translation descendants of the global arithmetic vacuum.

The word "Goldstone-like" is only a physics analogy; the exact statement is the translation/derivative identity above.

## 5. Why a collapsing absolute gap can still be enough

Both the finite ground energy and the first excited near-radical energy may tend to zero as the window expands.

For RH closure we do NOT need an absolute cutoff-uniform gap.

The vacuum-profile criterion needs only
\[
\frac{\epsilon_\lambda}{\Delta_\lambda}
\to0
\]
fast enough relative to powers of \(L=\log\lambda^2\).

If
\[
\epsilon_\lambda
\asymp E_{\rm ext}(\Phi)
\]
and the first orthogonal radical descendant has energy
\[
\Delta_\lambda
\gtrsim
c\lambda^4E_{\rm ext}(\Phi),
\]
then
\[
\boxed{
\epsilon_\lambda/\Delta_\lambda
=
O(\lambda^{-4}).
}
\]

Since every fixed power of \(L\) grows more slowly than \(\lambda^4\),
\[
L^M\epsilon_\lambda/\Delta_\lambda\to0
\]
for every fixed \(M\).

That is exactly sufficient for convergence of ALL fixed polynomial moments of the finite ground profile to the Riemann profile, hence for all BPY inverse-Casimir trace moments and RH.

So a relative polynomial gap is enough even though the absolute spectrum collapses toward the radical.

## 6. The actual missing theorem is now narrower

To turn this asymptotic into a proof, establish three facts zero-independently:

1. **Radical exterior reduction.**  
   The low finite-window spectrum is represented by exterior energies of global radical continuations.

2. **First-descendant coercivity.**  
   After removing the vacuum direction, every admissible radical continuation has exterior energy at least the scale of the first translation descendant:
   \[
   E_{\rm ext}(R)
   \gtrsim
   c\lambda^4E_{\rm ext}(\Phi)
   \|R_\perp\|^2.
   \]

3. **No non-radical intruder.**  
   The full finite Weil form has no lower negative/complementary mode outside this radical tower. This is the arithmetic Hodge-index/reflection-positivity statement.

Items 1 and 2 are an information-theoretic/prolate concentration problem. Item 3 is the genuinely arithmetic sign theorem.

## 7. Link to the prolate-wave asymptotics

The recent zeta-spectral-triple programme proves for low prolate modes that their failure of perfect time-frequency concentration is exponentially small:
\[
1-\chi_n(\lambda)
=
e^{-4\pi\lambda^2}
\times
\text{polynomial in }\lambda
\times(1+o(1)).
\]

The Riemann kernel itself is built from the \(n=0\) and \(n=4\) Hermite/prolate sectors.

Therefore the common exponential factor \(e^{-4\pi\lambda^2}\) and the polynomial separation among low prolate modes are exactly the kind of structure predicted by the edge-derivative calculation above.

This strongly suggests that the required finite quotient gap should be proved as a COMPARISON theorem between:
- the exterior Weil energy on the radical continuation space; and
- the prolate concentration defect.

That comparison would turn known prolate spectral separation into the gap estimate needed for vacuum-profile convergence.

## 8. Direct theorem target

The highest-value next lemma is therefore:

> **Arithmetic-prolate gap comparison.**  
> On the physical radical-continuation quotient at window scale \(\lambda\), the completed Weil exterior quadratic form is uniformly comparable, on the first few low modes and with sufficient lower control on their orthogonal complement, to the prolate concentration-defect form.

If the comparison is strong enough to yield
\[
\Delta_\lambda
\gtrsim
\lambda^4\epsilon_\lambda,
\]
the moment-compactness theorem closes the spectral-triple convergence problem without tracking individual zeta zeros.
