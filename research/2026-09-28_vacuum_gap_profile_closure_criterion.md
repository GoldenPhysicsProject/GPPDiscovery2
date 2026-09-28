# Vacuum-stability criterion: a finite quotient gap plus Riemann-kernel tail control implies RH

Date: 2026-09-28
Status: exact variational reduction. No RH proof. This joins the finite zeta-spectral-triple ground state, the Riemann \(\Phi\) radical profile, the mass-gap viewpoint, and the BPY inverse-Casimir moment criterion.

## 1. Elementary ground-state stability theorem

Let \(Q_j\) be a finite-dimensional self-adjoint operator with ordered eigenvalues
\[
\lambda_{1,j}<\lambda_{2,j}\le\cdots
\]
and normalized ground vector \(u_j\).

Set the finite quotient gap
\[
\Delta_j=\lambda_{2,j}-\lambda_{1,j}>0.
\]

For any normalized trial vector \(v_j\),
\[
\langle v_j,Q_jv_j\rangle-\lambda_{1,j}
=
\sum_{k\ge2}
(\lambda_{k,j}-\lambda_{1,j})
|\langle u_{k,j},v_j\rangle|^2.
\]

Therefore
\[
\boxed{
1-|\langle u_j,v_j\rangle|^2
\le
\frac{
\langle v_j,Q_jv_j\rangle-\lambda_{1,j}
}{\Delta_j}.
}
\]

After choosing the phase/sign of \(u_j\) to maximize the overlap,
\[
\boxed{
\|u_j-v_j\|_2^2
\le
2\,
\frac{
\langle v_j,Q_jv_j\rangle-\lambda_{1,j}
}{\Delta_j}.
}
\]

Thus a small Rayleigh residual only becomes vacuum-wavefunction convergence after division by the first excited-state gap. This is exactly the mass-gap logic.

## 2. Apply the theorem to the finite Weil/zeta-triple vacuum

Let the window be
\[
I_j=[-L_j/2,L_j/2].
\]

Let \(Q_j\) be the finite/truncated Weil operator used to construct the zeta spectral triple, and let \(u_j\) be its normalized lowest eigenprofile.

Take as trial vector
\[
v_j=
\frac{P_j\Phi}{\|P_j\Phi\|_2},
\]
where \(P_j\) is the finite basis/window projection and \(\Phi\) is Riemann's explicit Fourier kernel.

The global \(\Phi\) profile is distinguished zero-independently by
\[
\widehat\Phi\propto \Xi.
\]
The explicit formula therefore makes it the natural global radical/vacuum profile; the finite residual comes from projection/window/exterior error.

Define
\[
\epsilon_j
=
\langle v_j,Q_jv_j\rangle-\lambda_{1,j}\ge0.
\]

Then
\[
\boxed{
\|u_j-v_j\|_2
\le
\sqrt{2\epsilon_j/\Delta_j}.
}
\]

So the spectral-triple convergence problem is reduced to a competition between:
- the exterior/tail error \(\epsilon_j\);
- the finite physical excitation gap \(\Delta_j\).

## 3. Weighted moment convergence criterion

Suppose both \(u_j\) and \(v_j\) are supported in \(I_j\), and normalize them as probability profiles after the usual positive ground-state normalization.

For a fixed integer \(k\ge0\),
\[
\int_{I_j}|x|^k|u_j-v_j|\,dx
\le
\left(\frac{L_j}{2}\right)^k
\sqrt{L_j}\,
\|u_j-v_j\|_2.
\]

Hence
\[
\boxed{
\int |x|^k|u_j-v_j|\,dx
\le
\sqrt{2}\left(\frac{L_j}{2}\right)^k
L_j^{1/2}
\sqrt{\epsilon_j/\Delta_j}.
}
\]

Therefore a sufficient condition for convergence of every fixed polynomial moment is

\[
\boxed{
L_j^{\,2k+1}\,
\frac{\epsilon_j}{\Delta_j}
\longrightarrow0
\qquad
\text{for every fixed }k.
}
\]

Since the Riemann kernel has super-exponentially small spatial tails, the separate replacement of \(P_j\Phi\) by the full normalized \(\Phi\) contributes negligible moments once \(L_j\to\infty\).

Thus the finite ground-profile cumulants converge to the \(\Phi\) cumulants if the Rayleigh residual beats the finite excitation gap by every fixed polynomial in \(L_j\).

## 4. Combined theorem with the BPY/Fredholm reduction

The previous moment-compactness theorem says that convergence of all ground-profile even cumulants implies convergence of all inverse-Casimir traces:
\[
\operatorname{Tr}A_j^m\to t_m.
\]

Then
\[
\det(I+z^2A_j)
\to
\frac{\xi(\frac12+z)}{\xi(\frac12)}
\]
locally uniformly, and since every finite determinant has only imaginary \(z\)-zeros, Hurwitz gives RH.

Combining the two reductions:

> **Vacuum-stability closure criterion.**  
> If a cofinal family of finite zero-independent zeta triples satisfies
> \[
> L_j^{2k+1}\epsilon_j/\Delta_j\to0
> \quad\text{for every fixed }k,
> \]
> together with the positive-profile and relative-Fredholm normalizations already specified, then RH follows.

This is a direct bridge:
\[
\boxed{
\text{finite vacuum tail}
+
\text{finite mass gap}
\Longrightarrow
\text{vacuum profile convergence}
\Longrightarrow
\text{BPY moment convergence}
\Longrightarrow
\text{principal-series Casimir}
\Longrightarrow
\mathrm{RH}.
}
\]

## 5. Why this may be genuinely easier to attack

The original spectral-triple programme asks for convergence of every individual low eigenvalue to every zeta zero.

The present criterion asks only for two scalar/variational estimates:
1. an upper bound on the Riemann-profile trial residual \(\epsilon_j\);
2. a lower bound on the first excited quotient gap \(\Delta_j\).

The first is governed by the explicit super-exponential Riemann-kernel exterior tail and is already numerically understood.

The second is precisely the kind of theorem the current parity/Hodge-index/interlacing programme is designed to prove.

So the mass-gap analogy is not merely conceptual: the gap is exactly the denominator in the eigenvector-stability estimate that converts the explicit Riemann trial vacuum into the true finite spectral-triple vacuum.

## 6. Existing numerical evidence and what it actually means

Independent high-precision replication of the recent zeta spectral triples reports very small lowest Weil eigenvalues while the next eigenvalue can be substantially separated from the ground:
- at one cutoff the ratio \(\lambda_2/\lambda_1\) is about \(21\);
- at the next reported cutoff it is about \(10^6\).

Separately, the GPP/Claude \(\Phi\)-profile experiments find overlaps with the finite ground profile extremely close to one and rapidly small exterior Rayleigh energies.

These facts are consistent with \(\epsilon_j/\Delta_j\to0\), but are not a proof and the cutoffs are far too small to establish an asymptotic law.

The criterion above tells us exactly what numerical quantity should now be measured:
\[
\boxed{
\epsilon_j/\Delta_j
}
\]
and its polynomially weighted versions, rather than only zero-location error.

## 7. The new sharp analytic target

Prove a zero-independent bound of the form
\[
\epsilon_j
\le
E_{\rm tail}(L_j)
\]
with \(E_{\rm tail}\) super-exponentially small, and a finite-operator gap bound
\[
\Delta_j\ge e^{-o(e^{L_j})}
\]
strong enough that
\[
L_j^M E_{\rm tail}(L_j)/\Delta_j\to0
\]
for every fixed \(M\).

Any much stronger polynomial/exponential lower bound on \(\Delta_j\) would suffice immediately.

This turns the current parity/Hodge-index work into an explicit mass-gap theorem whose quantitative payoff is RH.
