# Two precise constraints on prime-edge sewing and finite-prime completions

Date: 2026-09-27. Status: proved obstructions for the stated models, not a no-go for every possible RH construction.

## 1. Boundary gluing alone cannot compactify unbounded prime edges

Consider a Hilbert space containing mutually orthogonal interval interiors
\[
\bigoplus_p L^2(0,\ell_p),\qquad \ell_p=\tfrac12\log p.
\]
Suppose a self-adjoint \(H\) acts as \(-d^2/dx^2+1\) in every interior, and its global sewing changes endpoint conditions only. More precisely, its domain includes the minimal interval domain \(H^2_0(0,\ell_p)\), embedded in a single edge, with zero in every other channel. This includes arbitrary self-adjoint endpoint coupling to an additional Archimedean bath.

Then
\[
\boxed{[1,\infty)\subseteq\sigma_{\mathrm{ess}}(H).}
\]
**Proof.** For \(k\ge0\), choose distinct primes \(p_j\to\infty\). Let
\[
\chi(y)=\sqrt{630}\,y^2(1-y)^2,\quad 0<y<1,
\]
so \(\|\chi\|_2=1,\ \|\chi'\|_2^2=12,\ \|\chi''\|_2^2=504\), and \(\chi=\chi'=0\) at both endpoints. On edge \(p_j\) define
\[
f_j(x)=\ell_{p_j}^{-1/2}\chi(x/\ell_{p_j})e^{ikx}.
\]
These are orthonormal minimal-domain vectors. An exact calculation gives
\[
\|(H-(1+k^2))f_j\|^2
=\frac{48k^2}{\ell_{p_j}^2}
+\frac{504}{\ell_{p_j}^4}\longrightarrow0.
\]
The weakly null Weyl sequence proves the assertion. QED.

In particular the unquotiented network cannot have compact resolvent. If it is semibounded, its heat operator cannot be trace class for any positive time.

This does not exclude a scalar boundary observation supported only on a discrete reducing subspace, a cohomological quotient discarding interior modes, or a new interior confining/nonlocal operator. It does exclude identifying the ordinary full heat trace of a graph with unmodified growing prime edges with the desired discrete arithmetic heat trace.

The constructive order must therefore specify the physical quotient or bulk cancellation before making a trace-class/discrete-spectrum claim.

## 2. A naive finite-prime replacement cannot be Stieltjes

For a finite prime set \(\mathcal P\), keep the exact Archimedean term and define
\[
B_{\mathcal P}(s)=\frac1{s-1}-\tfrac12\log\pi
+\tfrac12\psi(1+s/2)
-\sum_{p\in\mathcal P}\frac{\log p}{p^s-1},
\]
\[
m_{\mathcal P}(u)=
\frac{B_{\mathcal P}(1/2+\sqrt{1+u})}{2\sqrt{1+u}}.
\]
The finite prime sum cannot cancel the rational pole at \(s=1\). Consequently \(m_{\mathcal P}\) has a pole at
\[
u=-3/4
\]
with residue \(+1\). It already violates the required support \([1,\infty)\).

There is a stronger obstruction. On the upper bank of \(u=-1-k^2\), \(k>0\), its putative Stieltjes density is
\[
\rho_{\mathcal P}(1+k^2)
=-\frac1\pi\Im m_{\mathcal P}(-1-k^2+i0)
=\frac{\Re B_{\mathcal P}(1/2+ik)}{2\pi k}.
\]
The real parts of \(1/s+1/(s-1)\) cancel on the critical line. Thus
\[
\Re B_{\mathcal P}(1/2+ik)
=\frac12\Re\psi(1/4+ik/2)-\frac12\log\pi
-\sum_{p\in\mathcal P}\log p\sum_{m\ge1}p^{-m/2}\cos(mk\log p).
\]
At \(k=0\),
\[
\tfrac12\psi(1/4)-\tfrac12\log\pi
-\sum_{p\in\mathcal P}\frac{\log p}{\sqrt p-1}<0,
\]
because \(\psi(1/4)=-\gamma-\pi/2-3\log2<0\). Continuity proves negative density on a nonempty interval \(0<k<\epsilon_{\mathcal P}\).

Hence this finite-prime target is not Stieltjes even if the support restriction is relaxed to \([0,\infty)\). Positive real-axis values are insufficient.

The recorded controls at \(k=0.1\) give negative densities for prime cutoffs \(0,2,7,31,97\), while \(m_{\mathcal P}(1)\) remains positive. These values illustrate the exact sign proof; they are not an all-cutoff numerical assertion.

## 3. The full functional equation explains what must cancel

For the exact completed \(B\),
\[
B(1/2-r)=-B(1/2+r).
\]
Together with reality, this gives \(\Re B(1/2+ik)=0\) away from zeros on that line. Thus the continuous branch density of the naive finite cutoffs disappears after the full analytic completion, while genuine zero poles remain.

The cancellation of this continuous density is unconditional and follows from the functional equation. It does not locate every remaining pole on the real spectral cut: a centered zero \(z=\rho-1/2\) creates the pole \(u=z^2-1\).

Therefore a viable finite approximation must sew/cancel the pole and continuum channels before claiming a positive Stieltjes parent. Keeping the real-place term fixed while simply truncating the prime current cannot be the desired positive approximating sequence.
