# Literature-assisted closure: RH from Poisson-smoothed resolvent convergence of the finite zeta triples

Date: 2026-09-28
Status: exact new reduction/synthesis. No RH proof. Public interfaces used: CCM finite self-adjoint zeta spectral triples; Suzuki's shifted-xi inner-function criterion; Burnol/de Branges canonical-system framework. The new contribution here is the resolvent-difference/Poisson smoothing target, which is weaker than full determinant convergence and cancels normalization/exponential ambiguities.

## 1. Finite self-adjoint determinants give inner shifted ratios automatically

Let \(D_j\) be any finite/self-adjoint CCM zeta-triple operator and let
\[
F_j(z)=\det_{\rm reg}(D_j-z)
\]
after removing any fixed nonzero scalar normalization. Its zeros are real.

For \(\omega>0\), define
\[
\boxed{
\Theta_{j,\omega}(z)
=
\frac{F_j(z-i\omega)}{F_j(z+i\omega)}.
}
\]

Because \(F_j\) is real entire with real zeros, \(F_j(z+i\omega)\) has all of its zeros in the lower half-plane. Therefore \(\Theta_{j,\omega}\) is a meromorphic-inner/finite scattering function in the upper half-plane.

Equivalently,
\[
\boxed{
\Theta_{j,\omega}(z)
=
\det\left[
(D_j-z+i\omega)
(D_j-z-i\omega)^{-1}
\right].
}
\]

Any scalar normalization of \(F_j\) cancels. A real exponential factor \(e^{a_jz+b_j}\) contributes only the \(z\)-independent unimodular constant \(e^{-2ia_j\omega}\). Thus this object is substantially less sensitive to regularized-determinant normalization than \(F_j\) itself.

## 2. The phase derivative is a positive Poisson-smoothed spectral density

For real \(x\),
\[
\begin{aligned}
\frac1i\frac{d}{dx}\log\Theta_{j,\omega}(x)
&=
\frac1i\operatorname{Tr}
\left[
(D_j-x-i\omega)^{-1}
-
(D_j-x+i\omega)^{-1}
\right]\\
&=
\boxed{
2\omega\,
\operatorname{Tr}
\left[
(D_j-x)^2+\omega^2
\right]^{-1}
}.
\end{aligned}
\]

Hence
\[
\boxed{
P_{j,\omega}(x)
:=
\frac1i\partial_x\log\Theta_{j,\omega}(x)
>0.
}
\]

If the real eigenvalues are \(\gamma_{j,k}\),
\[
P_{j,\omega}(x)
=
2\omega\sum_k
\frac1{(x-\gamma_{j,k})^2+\omega^2}.
\]

This is exactly the Poisson extension of the finite spectral counting measure.

Crucially, each summand decays like \(\gamma_{j,k}^{-2}\). The shifted-resolvent DIFFERENCE is therefore much better behaved in the ultraviolet than an individual resolvent trace.

## 3. Target shifted ratio is precisely Suzuki's function

Write the centered real entire xi function in spectral variable
\[
F_\xi(z)
=
\xi\left(\frac12-iz\right).
\]

Then
\[
F_\xi(z+i\omega)
=
\xi\left(\frac12+\omega-iz\right),
\]
and
\[
F_\xi(z-i\omega)
=
\xi\left(\frac12-\omega-iz\right).
\]

Therefore
\[
\boxed{
\Theta_{\xi,\omega}(z)
=
\frac{F_\xi(z-i\omega)}
{F_\xi(z+i\omega)}
=
\frac{
\xi(\frac12-\omega-iz)
}{
\xi(\frac12+\omega-iz)
}.
}
\]

This is exactly the family used by Suzuki in the canonical-system/meromorphic-inner criterion for RH.

Thus the CCM finite self-adjoint approximants and Suzuki's de Branges criterion meet through the SAME shifted determinant ratio.

## 4. New closure theorem: full determinant convergence is unnecessary

Assume that for every fixed \(\omega>0\), or merely for a sequence \(\omega_m\downarrow0\), one can prove
\[
\boxed{
\Theta_{j,\omega}
\longrightarrow
\Theta_{\xi,\omega}
}
\]
locally uniformly in the upper half-plane along a cofinal cutoff sequence.

Each \(\Theta_{j,\omega}\) is Schur/inner there. A locally uniform limit is Schur (or identically constant, excluded by normalization/phase data), so \(\Theta_{\xi,\omega}\) has no pole in the upper half-plane.

Now suppose xi had an off-critical zero
\[
\rho=\frac12+\delta+i\gamma,
\qquad \delta>0.
\]
For every \(0<\omega<\delta\), the denominator
\[
\xi\left(\frac12+\omega-iz\right)
\]
vanishes at
\[
z=-\gamma+i(\delta-\omega)
\in\mathbb C_+,
\]
so \(\Theta_{\xi,\omega}\) has an upper-half-plane pole.

Contradiction.

By functional-equation symmetry, no zero can lie on the opposite side either. Hence RH.

Therefore:

\[
\boxed{
\text{Local-uniform convergence of the finite shifted scattering ratios for }
\omega_m\downarrow0
\Longrightarrow \mathrm{RH}.
}
\]

This is weaker-looking than convergence of \(F_j\to F_\xi\): overall normalization and linear Hadamard exponential factors cancel automatically.

## 5. Equivalent Herglotz/Poisson target

On the real boundary,
\[
\frac1i\partial_x\log\Theta_{\xi,\omega}(x)
=
\boxed{
2\Re\frac{\xi'}{\xi}
\left(\frac12+\omega-ix\right)
}.
\]

Under RH this equals the positive Poisson sum
\[
2\omega\sum_\gamma
\frac{m_\gamma}
{(x+\gamma)^2+\omega^2}
\]
(up to the fixed sign convention \(x\leftrightarrow-\gamma\)).

So the convergence target can be written without any zero input as
\[
\boxed{
2\omega\,\operatorname{Tr}
\left[(D_j-x)^2+\omega^2\right]^{-1}
\longrightarrow
2\Re\frac{\xi'}{\xi}
\left(\frac12+\omega-ix\right).
}
\]

The right side is computed directly from xi/gamma/primes; no zeta-zero ordinates are required.

This is a Poisson-smoothed RESOLVENT convergence problem.

## 6. Why this may be easier than the BPY moment hierarchy

The existing moment-compactness theorem asks for every inverse-Casimir moment
\[
\operatorname{Tr}A_j^m\to t_m.
\]

That is strong enough to recover the whole entire determinant.

The present criterion asks instead for convergence of a smoothed Cauchy/Poisson transform at fixed positive height \(\omega\). Spectrally this suppresses high-frequency errors by
\[
((x-\gamma)^2+\omega^2)^{-1}.
\]

This is exactly the topology in which self-adjoint strong-resolvent convergence and Weyl-function convergence are naturally formulated.

Thus the direct mass-gap/Schur machinery may have a better chance of proving this smoothed convergence than all raw trace moments.

Once the result is available for a countable sequence \(\omega_m\to0\), no unsmoothed zero-by-zero limit is needed.

## 7. Canonical-system interpretation

Because each finite \(\Theta_{j,\omega}\) is inner, de Branges theory assigns a positive semidefinite canonical-system Hamiltonian \(H_{j,\omega}(a)\).

Suzuki's programme asks for the corresponding positive Hamiltonian structure for the xi ratio down to every \(\omega>0\).

The new finite-limit route is therefore:

\[
\boxed{
\text{CCM self-adjoint triple}
\to
\Theta_{j,\omega}\text{ inner}
\to
H_{j,\omega}\ge0
\to
\text{compact/tight canonical-system limit}
\to
\Theta_{\xi,\omega}\text{ inner}
\to
\mathrm{RH}.
}
\]

This is the canonical-system analogue of the GPP physical-Casimir limit.

The critical KMS/Poisson sewing operator
\[
\mathcal E=Z_{\rm crit},
\qquad
Z_{\rm crit}\mathcal F=JZ_{\rm crit},
\]
is a natural candidate for proving tightness/identifying the limit because Burnol's co-Poisson/Sonine theory is precisely the Fourier/Mellin Hilbert-space interface underlying these canonical systems.

## 8. Immediate zero-free numerical falsifier

For each finite cutoff \(j\), extract the finite self-adjoint spectral data from the actual Weil ground state and compare
\[
P_{j,\omega}(x)
=
2\omega\sum_k
\frac1{(x-\gamma_{j,k})^2+\omega^2}
\]
against
\[
P_{\xi,\omega}(x)
=
2\Re\frac{\xi'}{\xi}
\left(\frac12+\omega-ix\right)
\]
on compact x-windows and several \(\omega\)'s.

This comparison uses xi directly but NO zero list.

If the Poisson-resolvent error decays dramatically even where raw eigenvalue convergence is difficult, that identifies the topology in which the proof should be attempted.

If it does not, this route should be deprioritized.

## 9. Literature boundary / novelty statement

Known public ingredients:
- CCM: finite zero-independent self-adjoint zeta triples and real-zero determinants;
- Suzuki: the shifted xi ratio \(\Theta_\omega\) and its meromorphic-inner/canonical-system RH criterion;
- Burnol/de Branges: co-Poisson, Sonine spaces, and canonical-system Hilbert structures.

New synthesis proposed here:
- use the CCM finite determinants only through their SHIFTED SCATTERING RATIOS;
- replace full determinant/eigenvalue convergence by Poisson-smoothed resolvent-difference convergence;
- exploit cancellation of regularization/linear-exponential ambiguities;
- take a sequence \(\omega_m\downarrow0\) to exclude every possible off-critical zero.

This is now a concrete alternative closure route beside the BPY moment and vacuum-profile routes.
