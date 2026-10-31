# An infinite-negative-index no-go for the naive additive-time OS reflection of the completed Weil distribution

**2026-10-31, Codex / GPPDiscovery2.** This is a new exact **no-go for one particular additive-time Osterwalder–Schrader ansatz**, not a no-go for RH, Weil positivity in the correct Toeplitz sense, or general adelic/celestial reflected Hilbert constructions.

## 1. Kernel dictated by the actual v34 completed distribution, away from contact

From the original paper's Section "The exact semilocal Weil form", the completed one-sided distribution at strictly positive y away from arithmetic atoms is the ordinary real-analytic function
\[
A(y)=e^{y/2}+e^{-y/2}-\frac{e^{y/2}}{2\sinh y},\qquad y>0.
\]
At the first arithmetic shift \(a=\log2\) it has an additional **negative point mass** \(-w\delta_a\), \(w=(\log2)/\sqrt2>0\). The gamma contact proportional to \(F(0)\) is supported at y=0, not at y=a. Every subsequent prime-power atom is at y≥log3.

A naive additive OS proposal replaces the translation-invariant Toeplitz pairing of the Weil criterion with the reflected Hankel pairing
\[
B(h)=\iint_{t,s>0}\overline{h(t)}h(s)\,W(t+s)\,dt\,ds.
\]
**Important distinction:** the Weil criterion concerns positive type of the original difference/convolution kernel; OS reflection positivity of this *same* kernel with t+s is strictly stronger and not implied by RH. The following theorem refutes only the naive substitution \(W(t+s)\) as the OS covariance, not an independently constructed boundary covariance.

## 2. Explicit rigorous all-dimensional theorem at a fixed rational strip

Set
\[
\delta=\frac1{100},\qquad I=(a/2-\delta,a/2+\delta)\subset(0,\infty),\qquad (I+I)\subset(0,\log3).
\]
For \(h\in C_c^\infty(I;\mathbb C)\) (or \(L^2(I)\) by the bounded form extension), the actual completed distribution restricted to I+I gives **exactly**
\[
\boxed{
B_I(h)=\int_I\int_I\overline{h(t)}A(t+s)h(s)\,dt\,ds
-w\int_I\overline{h(t)}h(a-t)\,dt.
}
\]
The positive-time strip reflection \(Rh(t)=h(a-t)\) is a self-adjoint unitary involution \(R^2=I\). Its +1 and −1 eigenspaces are both infinite dimensional. Define the smooth real symmetric integral operator K with kernel \(A(t+s)\) on I. The true OS-naive operator on I is \(K-wR\).

**Uniform analytic kernel bound.** The elementary rational inequalities \(2/3<\log2<3/4\) give, for t,s∈I,
\[
16/25<t+s<4/5.
\]
We have \(\exp((t+s)/2)<\exp(2/5)<3/2\), \(\exp(-(t+s)/2)<1\), and \(2\sinh(t+s)>2(t+s)>32/25\). Thus
\[
|A(t+s)|
\le \frac32+1+\frac{3/2}{32/25}
=\frac{235}{64}<4.
\]
The Schur bound on an interval of length \(2\delta=1/50\) yields
\[
\boxed{\|K\|_{L^2(I)\to L^2(I)}<\frac{2}{25}.}
\]
Also \(w=(\log2)/\sqrt2>(2/3)/(3/2)=4/9\). Hence
\[
\boxed{
\begin{array}{ll}
Rh=+h\quad\Rightarrow\quad B_I(h)<-\frac{82}{225}\|h\|^2,\\[2mm]
Rh=-h\quad\Rightarrow\quad B_I(h)>+\frac{82}{225}\|h\|^2,
\end{array}
}
\]
for nonzero h (the inequalities are strict, with rational uniform margin \(\frac{82}{225}\approx0.36444\)). Both subspaces are infinite-dimensional and contain arbitrarily many linearly independent smooth compactly supported functions. In fact R commutes with K, because A(t+s) is invariant under simultaneous t→a−t, s→a−s **only if** A(y)=A(2a−y), which generally FAILS; therefore DO NOT use a block diagonalization claim for the complete K-wR. Nevertheless the quadratic lower and upper inequalities on the ± eigenspaces are exact regardless of whether K commutes with R. On the direct sum, K may couple the two eigenspaces, but its norm is too small to remove either sign. The raw reflection kernel has **infinite positive and negative index**. (This follows either by its two infinite-dimensional definite subspaces or by essential-spectrum stability under the Hilbert–Schmidt perturbation K.)

No infinite test-function limit, zeta zeros, RH assumption, PNT estimate, or numerical eigenvalue argument is needed. In particular the result is valid entirely below the **next** arithmetic shift log3 and uses the correct Archimedean real-place density, pole, and arithmetic atom with all contact terms correctly located.

## 3. Meaning for KMS/BPY/TFD and the celestial boundary

This **kills the naive candidate** that simply declares the reflected additive Weil distribution \(W(t+s)\) to be an OS-positive covariance. It cannot be OS-positive even if RH is true. A viable OS strategy must therefore use a genuinely different boundary covariance plus an explicit map from the arithmetic test algebra whose resulting **restricted** pairing recovers the Toeplitz Weil form after renormalization and signed pole/contact sewing. Do not try to prove OS positivity of the raw reflected distribution itself.

The result is compatible with the exact all-scale thermal/KMS identity
\(Q=P+D_\gamma+\lim_X(K_X-2\Psi(X)\|f\|^2)-\kappa_\infty\|f\|^2\):
positive KMS energies may occur in a *different Hilbert space*, but the renormalization and cross-place intertwiners cannot be replaced with the naive additive Hankel kernel.

This theorem does not settle whether the actual adelic additive/multiplicative Poisson lattice supplies the required (different) reflected positive Hilbert pairing, nor any global Weil positivity/RH. Ftheta and DH controls remain mandatory after any new candidate is specified.

## 4. Reproducibility

The attached script \`discovery/arb_raw_weil_os_negative_index.py\` outward-certifies the few strict scalar inequalities (ln2 interval, exp(2/5), w>4/9, and 2δ sup|A|<2/25) with FLINT/Arb. The all-dimensional sign proof is the analytic Schur norm inequality above; no finite eigenvalue computation is used as a substitute. Strictly speaking the constructed \(h\) need not respect a particular yet-undefined adelic Hardy-positive subalgebra; that restriction is exactly what a future valid OS candidate has to specify.

**Open frontier:** the true, distributionally renormalized prime–Archimedean form needs a *nontrivial* arithmetic half-space structure, not the obvious \(C_c^\infty(0,\infty)\) with additive exchange reflection. This is a necessary exclusion of a false route, not the constructive missing identity.
