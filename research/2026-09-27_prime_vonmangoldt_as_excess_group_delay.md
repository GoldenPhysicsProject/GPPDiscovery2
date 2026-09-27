# Prime powers as excess Wigner–Smith delay of local Blaschke channels

Date: 2026-09-27  
Status: exact local and finite-prime identities; global infinite-prime completion remains the RH problem. No external literature search used.

## 1. Start from the already exact local Euler-shadow colligation

For one prime set
\[
L_p=\log p,\qquad a_p=p^{-1/2}.
\]
The local transfer function is
\[
\mathcal T_p(z)=\frac{z-a_p}{1-a_p z}.
\]
This is a Blaschke factor.

On the unit circle write
\[
z=e^{i\theta}.
\]
Then
\[
|\mathcal T_p(e^{i\theta})|=1.
\]

## 2. Exact phase-delay kernel

Differentiate the logarithm:
\[
\frac{d}{d\theta}\arg\mathcal T_p(e^{i\theta})
=
\boxed{
\frac{1-a_p^2}
{1-2a_p\cos\theta+a_p^2}
}.
\]

This is the Poisson kernel
\[
\mathcal P_{a_p}(\theta)
=
1+2\sum_{m\ge1}a_p^m\cos(m\theta).
\]

Therefore the local unitary arithmetic channel has strictly positive phase delay:
\[
\boxed{
\mathcal P_{a_p}(\theta)>0.
}
\]

## 3. The von-Mangoldt half-density current is exactly the excess delay

Put
\[
\theta=tL_p.
\]
The phase delay with respect to the spectral variable \(t\) is
\[
\tau_p(t)
=
L_p\,\mathcal P_{a_p}(tL_p).
\]

Since \(a_p=p^{-1/2}\),
\[
\tau_p(t)
=
L_p
+
2\sum_{m\ge1}
L_p\,p^{-m/2}\cos(mtL_p).
\]

Hence
\[
\boxed{
\sum_{m\ge1}
(\log p)p^{-m/2}
\cos(mt\log p)
=
\frac12\bigl(\tau_p(t)-\log p\bigr).
}
\]

But
\[
\Lambda(p^m)=\log p.
\]
Thus the prime-power half-density current is precisely the local Wigner–Smith/group-delay excess above the free baseline.

For a finite prime set \(\mathcal P\), let
\[
\mathcal T_{\mathcal P}
=
\prod_{p\in\mathcal P}\mathcal T_p.
\]
Phase derivatives add, so
\[
\boxed{
\sum_{p\in\mathcal P}\sum_{m\ge1}
(\log p)p^{-m/2}
\cos(mt\log p)
=
\frac12
\left[
\frac{d}{dt}\arg\mathcal T_{\mathcal P}(t)
-
\sum_{p\in\mathcal P}\log p
\right],
}
\]
up to the harmless sign determined by whether the unit-circle parameter is \(e^{+itL_p}\) or \(e^{-itL_p}\).

So every finite prime tower is a vacuum-subtracted delay spectrum of a finite cascade of exact passive unitary channels.

## 4. The same vacuum subtraction that created the TFD ghost appears here

The raw Poisson kernel is positive:
\[
\tau_p(t)>0.
\]

The arithmetic current removes the baseline
\[
L_p.
\]

This is the phase-delay analogue of the covariance calculation:
- the full TFD covariance with its \(1/2\) vacuum term is positive;
- normal ordering removes the vacuum \(1/2\) and creates an indefinite Krein form;
- the full Blaschke phase delay is positive;
- the explicit prime current removes the free delay \(L_p\) and becomes sign-indefinite.

Thus two previously separate ghosts are the same operation in covariance and scattering language:
\[
\boxed{\text{positivity} \;\longrightarrow\; \text{vacuum/background subtraction} \;\longrightarrow\; \text{relative indefinite object}.}
\]

## 5. Why the Archimedean place is now the natural completion

The infinite baseline
\[
\sum_p\log p
\]
diverges, so the critical arithmetic cascade cannot be completed by summing local free delays literally.

The completed explicit formula instead supplies a renormalized real-place distribution
\[
\mathcal W=\nu_\infty-\nu_{\rm p}.
\]

The new interpretation is:

\[
\boxed{
\nu_{\rm p}
=
\text{renormalized excess delay of the prime Blaschke cascade},
}
\]
while \(\nu_\infty\) must furnish the canonical continuum/background delay needed to define the global relative scattering system.

This is consistent with the exact real-place identity
\[
w_\infty(x)
=
e^{-x/2}+e^{x/2}
-e^{x/2}A(x),
\qquad
A(x)=\frac1{2\sinh x},
\]
because the thermal part of the Archimedean channel is built from the same massive-edge/TFD anomalous covariance as the local prime system.

## 6. Connection to zero density

For a finite lossless cascade, zeros/poles of its analytic continuation are encoded by the phase winding and the phase-delay measure.

The 2M-zero experiment already showed that the oscillating zero density Fourier-transforms back to
\[
\frac{\Lambda(n)}{\sqrt n}
\]
at the logarithmic lengths \(\log n\).

The identity above explains that observation locally:
\[
\frac{\Lambda(p^m)}{\sqrt{p^m}}
=
L_p a_p^m
\]
is exactly the \(m\)-th Fourier coefficient of the excess phase delay of the prime-\(p\) Blaschke channel.

Thus
\[
\boxed{
\text{zero-density oscillations}
\leftrightarrow
\text{global scattering delay}
\leftrightarrow
\text{prime-power returns}.
}
\]

## 7. Sharpened RH target

Ordinary local unitarity is not enough; every finite prime channel already has it.

The global theorem should be formulated as follows:

Construct the renormalized infinite cascade, including the Archimedean background, as a causal/passive inner transfer system whose boundary delay is the completed Weil distribution.

If that construction exists without using zero locations, its poles/resonances must lie on the self-adjoint/unitary spectral axis.

Equivalently, the remaining task is to prove that Archimedean completion converts the vacuum-subtracted prime delay into the positive Weyl/Gram object already known to be equivalent to RH.

This is not yet a proof. It does identify the von-Mangoldt half-density current as a concrete positive-channel observable before renormalization, and it aligns the scattering and TFD versions of the no-ghost problem.
