# Four-component rigidity in the number-circle Gaussian family

Date: 2026-09-27
Status: exact zero-independent rigidity theorem inside a specified Gaussian free-field ansatz. No RH claim.

Let
\[
Q_d=\frac1{2\pi}\sum_{a=1}^d\sum_{n\ge1}\frac{G_{n,a}^2}{n^2},
\]
with independent standard real Gaussians. This is the squared radius of a \(d\)-component Gaussian field over the positive number-circle modes, whose arithmetic Hamiltonian is \(H=\log|D|\) and covariance satisfies \(e^{-2H}=\Delta^{-1}\).

For one Gaussian mode,
\[
\mathbb E e^{-tG^2/(2\pi n^2)}
=(1+t/(\pi n^2))^{-1/2}.
\]
Hence
\[
\boxed{
\mathbb E e^{-tQ_d}
=
\prod_{n\ge1}(1+t/(\pi n^2))^{-d/2}
=
\left(\frac{\sqrt{\pi t}}{\sinh\sqrt{\pi t}}\right)^{d/2}.
}
\]
At \(t=\pi\lambda^2\),
\[
\boxed{\mathbb E e^{-\pi\lambda^2 Q_d}=P(\lambda)^{d/2}},
\qquad
P(\lambda)=\frac{\pi\lambda}{\sinh\pi\lambda}.
\]

Thus \(d=2\) gives one celestial thermal/Plancherel factor \(P\), while \(d=4\) gives \(P^2\), the BPY case.

There is also an elementary rigidity statement. Since
\[
\mathbb E Q_d
=
\frac{d}{2\pi}\zeta(2)
=
\frac{d\pi}{12},
\]
while
\[
2\xi(2)=\frac{\pi}{3},
\]
any member of this isotropic Gaussian family satisfying even the single BPY moment condition
\[
\mathbb E Q_d=2\xi(2)
\]
must obey
\[
\boxed{d=4}.
\]

For \(d=4\), the full BPY theorem strengthens this one-moment match to
\[
\boxed{\mathbb E[Q_4^{s/2}]=2\xi(s)}.
\]

So within the canonical inverse-circle-Laplacian Gaussian ansatz, completed zeta uniquely selects four real Gaussian components. This uses no zero locations and no RH assumption.

This aligns structurally with the independently derived scalar conformal doubling
\[
h=\bar h=s,\qquad \Delta=2s,
\]
because one complex Gaussian sector has two real components and a left/right double has four. That alignment is a research clue only: the auxiliary Gaussian component count is not yet an identification with physical spacetime dimension. Such an identification would require an additional Lorentzian/celestial reconstruction theorem.
