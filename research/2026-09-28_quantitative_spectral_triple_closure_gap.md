# Quantitative closure of the zeta-spectral-triple missing step from a relative vacuum gap

Date: 2026-09-28
Status: exact analytic reduction using the 2025 Connes--Consani--Moscovici setup. No RH proof. It sharpens their second missing step to one explicit asymptotic inequality.

## 1. What is already proved in the zeta-spectral-triple programme

Let the logarithmic window have length
\[
L=2\log\lambda.
\]

The recent spectral-triple construction has:
- the true normalized lowest Weil eigenprofile \(\xi_\lambda\);
- an explicit prolate/Riemann trial profile \(k_\lambda=\mathcal E(h_\lambda)\);
- a theorem that the Mellin/Fourier transform of \(k_\lambda\) converges to Riemann's \(\Xi\) uniformly on closed substrips
\[
|\Im z|<\frac12.
\]

Their stated missing analytic step is to prove that \(k_\lambda\) approximates the true ground profile \(\xi_\lambda\) accurately enough.

## 2. Gap estimate converts Rayleigh control into profile control

Let
\[
\epsilon_\lambda
=
\langle k_\lambda,Q_\lambda k_\lambda\rangle
-\lambda_{1,\lambda}
\]
after normalized projection into the same finite/window Hilbert space, and let
\[
\Delta_\lambda
=
\lambda_{2,\lambda}-\lambda_{1,\lambda}>0.
\]

The elementary ground-state stability theorem gives
\[
\boxed{
\|\xi_\lambda-k_\lambda\|_2
\le
\sqrt{2\epsilon_\lambda/\Delta_\lambda}
}
\]
after choosing the common sign/phase.

Thus their qualitative approximation problem is a quantitative vacuum-residual / excitation-gap problem.

## 3. L2 profile control gives uniform transform control on every closed critical substrip

Both profiles are supported in a log interval of length \(L\). For
\[
|\Im z|\le a<\frac12,
\]
Cauchy--Schwarz gives
\[
\begin{aligned}
|\widehat{\xi_\lambda}(z)-\widehat{k_\lambda}(z)|
&\le
\int_{-L/2}^{L/2}
|\xi_\lambda(x)-k_\lambda(x)|e^{a|x|}\,dx\\
&\le
\sqrt L\,e^{aL/2}
\|\xi_\lambda-k_\lambda\|_2.
\end{aligned}
\]

Since
\[
e^{aL/2}=\lambda^a,
\]
we obtain the explicit bound
\[
\boxed{
\sup_{|\Im z|\le a}
|\widehat{\xi_\lambda}(z)-\widehat{k_\lambda}(z)|
\le
\sqrt{2L}\,
\lambda^a
\sqrt{\epsilon_\lambda/\Delta_\lambda}.
}
\]

Therefore the second missing step is solved if, for every fixed \(a<1/2\),
\[
\boxed{
L\,\lambda^{2a}
\frac{\epsilon_\lambda}{\Delta_\lambda}
\longrightarrow0.
}
\]

Since the worst closed substrips have \(a\) arbitrarily close to \(1/2\), a convenient sufficient condition is
\[
\boxed{
L\,\lambda^{1-\delta}
\frac{\epsilon_\lambda}{\Delta_\lambda}
\to0
\quad
\text{for every }\delta>0.
}
\]

## 4. The edge-derivative prediction is much stronger than required

The independent edge analysis predicts
\[
\epsilon_\lambda/\Delta_\lambda
=
O(\lambda^{-4})
\]
if the first excited near-radical mode is the translation derivative of the Riemann vacuum.

Insert this into the transform estimate:
\[
\sqrt{L}\lambda^a
\sqrt{\epsilon_\lambda/\Delta_\lambda}
=
O\!\left(
\sqrt{\log\lambda}\,
\lambda^{a-2}
\right).
\]

For every \(a<1/2\),
\[
a-2<-3/2,
\]
so this tends rapidly to zero.

Thus the predicted relative vacuum gap is far stronger than what is needed to close uniform convergence on the entire open strip.

## 5. Consequence with the already-proved prolate convergence

The 2025 paper already proves
\[
\widehat{k_\lambda}(z)
\to
\Xi(z)
\]
uniformly on every closed substrip \(|\Im z|\le a<1/2\).

Hence the single estimate above would give
\[
\widehat{\xi_\lambda}(z)
\to
\Xi(z)
\]
on the same substrips.

Each finite \(\widehat{\xi_\lambda}\) has only real zeros because it is the regularized determinant of a self-adjoint finite zeta spectral triple.

Hurwitz then gives the critical-line conclusion.

So their second missing step reduces to:

\[
\boxed{
\text{prove }
\epsilon_\lambda/\Delta_\lambda
=
o\!\left(
\lambda^{-1+2\delta}/\log\lambda
\right)
\text{ for every }\delta>0.
}
\]

The expected \(O(\lambda^{-4})\) would close it with enormous margin.

## 6. This also explains exactly why the mass-gap analogy matters

The explicit prolate profile already knows the correct Riemann limit.

What it does NOT know is whether it is the true arithmetic vacuum.

The quotient gap \(\Delta_\lambda\) supplies precisely that stability:
\[
\text{small trial energy}
+
\text{isolated ground state}
\Rightarrow
\text{vacuum wavefunction rigidity}.
\]

This is the same mathematical use of a mass gap in QFT: it prevents a tiny perturbation from rotating the vacuum into an uncontrolled orthogonal state.

## 7. The two stated missing steps collapse toward one

The first missing step in the spectral-triple paper is:
- smallest Weil eigenvalue simple;
- ground eigenvector even.

The second is:
- \(k_\lambda\) approximates that ground eigenvector.

A quantitative simple-even theorem with a lower bound on the first excitation gap \(\Delta_\lambda\) supplies the essential input for BOTH.

Thus the highest-value target is no longer generic determinant convergence. It is:

\[
\boxed{
\text{prove a quantitative simple-even finite Weil ground-state gap.}
}
\]

The current KMS metric / parity cross-resolvent / arithmetic Hodge-index programme is aimed exactly at that theorem.
