# Ground-profile cumulants are the inverse-Casimir moments

Date: 2026-09-28
Status: exact analytic bridge. No RH proof. This connects the finite zeta-spectral-triple ground profile directly to the BPY density-matrix/Fredholm moment targets.

## 1. Setup

Let \(\psi_j(x)\) be an even integrable cutoff ground profile whose normalized bilateral Laplace transform is
\[
F_j(z)
=
\frac{\int_{\mathbb R}\psi_j(x)e^{zx}\,dx}
{\int_{\mathbb R}\psi_j(x)\,dx}.
\]

Assume its corresponding finite self-adjoint zeta triple has positive inverse Casimir
\[
A_j\ge0
\]
and normalized determinant
\[
\boxed{
F_j(z)=\det(I+z^2A_j).
}
\]

When \(\psi_j\ge0\), define the probability law
\[
d\mu_j(x)=
\frac{\psi_j(x)\,dx}{\int\psi_j}.
\]

Then \(F_j\) is the moment-generating function of the even random variable \(X_j\sim\mu_j\).

## 2. Exact cumulant / inverse-spectrum identity

Write
\[
\log F_j(z)
=
\sum_{m\ge1}
\frac{\kappa_{2m}(X_j)}{(2m)!}z^{2m}.
\]

The Fredholm expansion gives
\[
\log F_j(z)
=
\sum_{m\ge1}
\frac{(-1)^{m+1}}m
z^{2m}\operatorname{Tr}A_j^m.
\]

Therefore coefficient comparison yields, for every \(m\ge1\),
\[
\boxed{
\operatorname{Tr}A_j^m
=
\frac{(-1)^{m+1}\kappa_{2m}(X_j)}
{2(2m-1)!}.
}
\]

In particular
\[
\boxed{
\operatorname{Tr}A_j
=
\frac12\operatorname{Var}(X_j).
}
\]

So the inverse spectral moments of the finite principal-series Casimir are not hidden global spectral quantities: they are ordinary cumulants of the finite ground profile in position/log-radius space.

## 3. The limiting Riemann profile gives exactly the BPY targets

Let \(\Phi\) be Riemann's Fourier kernel in the centered normalization
\[
\frac{\xi(\frac12+z)}{\xi(\frac12)}
=
\frac{\int_{\mathbb R}\Phi(x)e^{zx}\,dx}
{\int_{\mathbb R}\Phi(x)\,dx}.
\]

Let \(X_\Phi\) have normalized density proportional to \(\Phi\). Then
\[
\kappa_{2m}(X_\Phi)
=
\left.
\frac{d^{2m}}{dz^{2m}}
\log\frac{\xi(\frac12+z)}{\xi(\frac12)}
\right|_{z=0}.
\]

Hence
\[
\boxed{
t_m
=
\frac{(-1)^{m+1}\kappa_{2m}(X_\Phi)}
{2(2m-1)!}
}
\]
is exactly the BPY/Fredholm target
\[
t_m=\operatorname{Tr}A^m.
\]

Thus the finite-spectral-triple moment convergence theorem can be restated as:

\[
\boxed{
\kappa_{2m}(X_j)\to\kappa_{2m}(X_\Phi)
\ \forall m
\quad\Longrightarrow\quad
\mathrm{RH}.
}
\]

No individual finite eigenvalue needs to be tracked.

## 4. Numerical coincidence already seen by the independent ground-state programme

The current CCM/Riemann-profile experiments independently measured the normalized second moment of the finite ground profile crossing the value
\[
\langle x^2\rangle\approx0.046210.
\]

The intrinsic BPY scale is
\[
R=\frac{\kappa_2}{2}\approx0.0231049931154,
\]
so the exact target variance is
\[
\boxed{
\kappa_2=2R\approx0.0462099862308.
}
\]

Thus the previously observed “0.046210” ground-profile threshold is precisely the first inverse-Casimir trace condition
\[
\operatorname{Tr}A_j\to R.
\]

This identifies an old numerical marker with the first member of the new all-order moment hierarchy.

## 5. A much more tangible convergence theorem

It is enough to prove the following zero-independent profile statement.

Let
\[
\mu_j(dx)=\frac{\psi_j(x)\,dx}{\int\psi_j}.
\]

If
\[
\boxed{
\int x^{2m}\,d\mu_j(x)
\longrightarrow
\int x^{2m}\,d\mu_\Phi(x)
\quad\text{for every }m\ge1,
}
\]
then all even cumulants converge, hence all positive inverse-Casimir trace powers converge, hence the finite positive determinants converge locally uniformly to centered xi, hence RH.

A sufficient analytic package is:
1. local \(L^1\) convergence \(\mu_j\to\mu_\Phi\);
2. uniform integrability of every polynomial moment, e.g. for each \(a>0\) a cutoff-uniform exponential-moment bound on a cofinal tail;
3. positivity/normalization of the ground profiles.

This replaces “prove every spectral zero converges” by “prove the physical ground-state probability profiles converge with controlled tails.”

## 6. Why this interfaces perfectly with the existing tail/radical calculations

The Riemann kernel \(\Phi\) is already the distinguished global radical profile of the completed explicit-formula system. The finite zeta spectral triples use the lowest finite-window Weil eigenprofile.

Therefore the natural proof mechanism is variational rather than zero-by-zero:

- show the window restriction/projection of \(\Phi\) is an approximate ground state with explicitly controlled exterior/tail energy;
- prove a lower bound for the next physical mode (a finite-window quotient gap);
- use an eigenvector-stability estimate to force the normalized finite ground profile toward \(\Phi\);
- upgrade the profile convergence to weighted-moment convergence using the super-exponential Riemann-kernel tails / a uniform tail estimate.

This is exactly where the RH-as-mass-gap viewpoint becomes useful: a gap above the finite ground state is what converts a small Rayleigh residual into convergence of the vacuum wavefunction.

## 7. Circularity warning

One must not assume global Weil positivity in order to prove the finite ground state converges to \(\Phi\); that would simply assume RH.

The needed finite-window gap estimate has to be obtained from the zero-independent finite arithmetic operator (e.g. parity/Hodge-index/interlacing, Bost--Connes/KMS positivity, or the positive bulk Schur complement) uniformly enough to survive the cofinal limit.

So the new target is sharper, not easier by fiat:
\[
\boxed{
\text{prove vacuum-profile convergence from a zero-independent finite quotient gap.}
}
\]

If achieved, principal-series spectral convergence follows automatically through the cumulant/Fredholm bridge.
