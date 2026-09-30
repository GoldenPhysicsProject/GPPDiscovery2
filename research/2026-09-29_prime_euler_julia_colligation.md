# Prime Euler factors as canonical Julia colligations: local unitarity and the no-leakage RH target

Date: 2026-09-29
Status: exact local operator/scattering identities and a global reduction heuristic. No RH claim.

This note follows the prime-square-root and shadow-KMS boost-rigidity calculations.
The key new observation is that the half-density coefficient p^(-1/2) is exactly
the contraction parameter of a canonical 2x2 unitary (Julia) dilation.
The corresponding transfer function is a Blaschke factor. Thus each prime Euler
channel is already the compression of a lossless two-channel system.

The global RH problem is consequently not local unitarity. It is the theorem that
the completed Poisson/product-formula sewing closes all hidden channels so that a
zeta zero is a true lossless spectral mode rather than an open-system resonance.

## 1. Canonical unitary dilation of the half-density prime contraction

Put
\[
r_p=p^{-1/2},
\qquad
t_p=\sqrt{1-r_p^2}=\sqrt{1-p^{-1}}.
\]

Define
\[
U_p=
\begin{pmatrix}
r_p&t_p\\
t_p&-r_p
\end{pmatrix}.
\]

Then
\[
\boxed{U_p^*U_p=I,\qquad U_p^2=I,\qquad \det U_p=-1.}
\]

So the scalar contraction r_p is the visible corner of a canonical lossless
two-channel system. The hidden-channel amplitude is exactly sqrt(1-p^-1),
the same normalization already present in the prime TFD state.

## 2. Transfer function is an exact Blaschke factor

Write the colligation in blocks
\[
A=r,\quad B=t,\quad C=t,\quad D=-r,
\qquad t^2=1-r^2.
\]

Its scalar transfer function is
\[
\Theta_r(w)
=
D+wC(I-wA)^{-1}B.
\]

Direct algebra gives
\[
\boxed{
\Theta_r(w)
=
-r+\frac{w(1-r^2)}{1-rw}
=
\frac{w-r}{1-rw}.
}
\]

For 0<r<1, this is the elementary Blaschke factor with real zero r.
Therefore
\[
|\Theta_r(e^{i\theta})|=1.
\]

The local half-density prime channel is not merely contractive: it has an explicit
conservative unitary parent.

## 3. Insert the Mellin spectral coordinate

Center the zeta variable:
\[
s=\frac12+z.
\]

At prime p, put
\[
w_p(z)=p^{-z},
\qquad
r_p=p^{-1/2}.
\]
Then
\[
r_pw_p(z)=p^{-s}.
\]

Hence
\[
\Theta_p(s)
:=
\Theta_{r_p}(w_p(z))
=
\frac{p^{-(s-1/2)}-p^{-1/2}}
     {1-p^{-s}}.
\]

Factoring the numerator,
\[
p^{-(s-1/2)}-p^{-1/2}
=
p^{1/2-s}\left(1-p^{-(1-s)}\right),
\]
so
\[
\boxed{
\Theta_p(s)
=
p^{1/2-s}
\frac{1-p^{-(1-s)}}{1-p^{-s}}.
}
\]

Equivalently the local Euler shadow ratio is
\[
\boxed{
\frac{1-p^{-(1-s)}}{1-p^{-s}}
=
p^{s-1/2}\Theta_p(s).
}
\]

On the critical line s=1/2+it, both p^(s-1/2) and Theta_p(s) are phases.

## 4. Exact local energy-defect identity

For real 0<r<1,
\[
\Theta_r(w)=\frac{w-r}{1-rw}.
\]

A direct calculation gives
\[
\boxed{
1-|\Theta_r(w)|^2
=
\frac{(1-r^2)(1-|w|^2)}
     {|1-rw|^2}.
}
\]

For the prime channel,
\[
|w_p|=p^{-(\Re s-1/2)}.
\]

Therefore:
\[
\boxed{
\begin{array}{lll}
\Re s>1/2 &\Longrightarrow& |\Theta_p(s)|<1,\\[2mm]
\Re s=1/2 &\Longrightarrow& |\Theta_p(s)|=1,\\[2mm]
\Re s<1/2 &\Longrightarrow& |\Theta_p(s)|>1,
\end{array}}
\]
away from the elementary denominator poles.

Thus every single prime channel detects the principal-series line as its exact
lossless boundary.

The shadow s -> 1-conj(s) reverses Re(s)-1/2, so it exchanges the
contractive and expansive sides while fixing the lossless line.

## 5. Network interpretation

Let
\[
L_p=\log p.
\]
Then
\[
r_p=e^{-L_p/2},
\qquad
w_p=e^{-zL_p},
\qquad
r_pw_p=e^{-sL_p}=p^{-s}.
\]

Thus a prime Euler denominator
\[
1-p^{-s}
\]
is literally the feedback denominator of a one-edge channel of length L_p,
with half-density reflection amplitude e^(-L_p/2).

The local logarithmic derivative is the feedback susceptibility:
\[
-\frac{\zeta_p'}{\zeta_p}(s)
=
\frac{(\log p)p^{-s}}{1-p^{-s}}
=
\sum_{k\ge1}(\log p)p^{-ks}.
\]

So the same unitary colligation generates:
- the half-density p^-1/2;
- the Euler geometric series;
- the prime-power/von-Mangoldt current;
- the TFD hidden-channel normalization sqrt(1-p^-1);
- the principal-series lossless boundary.

## 6. Shadow-paired denominator in hyperbolic form

For s=1/2+z,
\[
(1-p^{-s})(1-p^{-(1-s)})
=
1+p^{-1}-2p^{-1/2}\cosh(z\log p).
\]

Equivalently,
\[
\boxed{
(1-p^{-s})(1-p^{-(1-s)})
=
2p^{-1/2}
\left[
\cosh\!\left(\frac{\log p}{2}\right)
-
\cosh(z\log p)
\right].
}
\]

On the principal series z=it, this becomes
\[
2p^{-1/2}
\left[
\cosh\!\left(\frac{\log p}{2}\right)
-
\cos(t\log p)
\right]>0.
\]

This is another exact local manifestation of the Euclidean-to-unitary rotation
z -> it. It does not by itself constrain global zeta zeros.

## 7. What the global product is trying to say

Formally,
\[
\prod_p
\frac{1-p^{-(1-s)}}{1-p^{-s}}
=
\frac{\zeta(s)}{\zeta(1-s)}
\]
where an appropriate continuation/completion is understood.

The zeta functional equation says that this global finite-place scattering ratio
is exactly balanced by the Archimedean completion factor.

Thus the Gamma/pole channel is not an unrelated correction: it is the global
boundary condition needed to sew the local prime scattering network into the
self-dual completed system.

The extra local phase p^(1/2-s) in the normalized Blaschke factor cannot be
multiplied naively over all primes. Its global meaning must be fixed by the
adelic/product-formula renormalization. This is precisely where naive products
must not be used.

## 8. The no-leakage formulation of the missing RH theorem

A unitary colligation can have contractive transfer after a hidden channel is
compressed away. Therefore seeing |Theta_p|<1 does not violate unitarity of
the parent system; it means probability/energy leaks into the hidden channel.

This gives a concrete reinterpretation of the existing unitary-parent leakage and BPY
vacuum-defect results:

- local prime parent: already unitary;
- visible arithmetic channel: contractive/expansive off the principal line;
- hidden TFD channel: carries the defect;
- principal line: zero local defect.

Consequently the smallest useful global statement is:

> No-leakage zero theorem. Every nontrivial zero of the completed zeta
> response is a genuine spectral mode of the CLOSED Poisson/product-formula
> network, not merely a pole/resonance of the visible compression. Equivalently,
> its total hidden-channel defect vanishes.

If the global hidden channels are an orthogonal/direct-integral sum of the local
Julia defects with positive weights, then zero total defect forces
\[
1-|w_p|^2=0
\]
for every active prime, hence
\[
\Re s=\frac12.
\]

This would close RH immediately.

The crucial missing work is to prove that the exact Riemann E-map / Poisson
completion supplies precisely this closed conservative feedback and that the
zeta divisor is retained as genuine spectral data of it.

## 9. Why independent hidden channels may matter

For Re(s)>1/2, every local defect
\[
\frac{(1-p^{-1})(1-p^{-2(\Re s-1/2)})}
{|1-p^{-s}|^2}
\]
has the same positive sign.

Therefore if the physical completion expresses the global leakage norm as a sum
of these local nonnegative defects, there is no possibility of cancellation
between different primes.

For Re(s)<1/2, shadow reflection moves the datum to the contractive side.
Thus by the functional equation it is enough to establish the positive
no-leakage theorem in one half of the critical strip.

This is potentially stronger than estimating a raw Möbius dual character because
it tries to use positivity BEFORE scalarization, at the level of the canonical
unitary dilation where the prime defects are orthogonal.

## 10. Falsifier

Do not call this a proof unless the following bridge is explicit:

1. construct the global Hilbert colligation from the local prime Julia factors
   together with the Archimedean Poisson channel;
2. identify its physical visible transfer/secular response with the completed
   zeta response, without assuming RH;
3. prove that a zero of xi is a zero-leakage eigenmode of the full colligation,
   rather than merely a resonance/pole of a compression;
4. prove positivity/orthogonality of the hidden defect decomposition;
5. preserve the zero datum in the infinite completion.

Without step 3, ordinary conservative scattering systems can have complex
resonances and no zero-location theorem follows.

This is now a concrete network version of the same zero-survival frontier.
