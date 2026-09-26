# Profinite Haar / celestial principal-series bridge

Status: exact lemmas proved algebraically below; RH remains open.

## 1. Critical Haar boundary

Let
\[
\widehat{\mathbf Z}=\prod_p \mathbf Z_p
\]
with normalized additive Haar probability measure \(\mu\), and let
\(\Omega=1\in L^2(\widehat{\mathbf Z},\mu)\).

For \(m\ge1\), define
\[
(V_m f)(x)=\sqrt m\,\mathbf 1_{m\widehat{\mathbf Z}}(x)\,f(x/m).
\]

Because \(\mu(mE)=m^{-1}\mu(E)\), \(V_m\) is an isometry and
\(V_mV_n=V_{mn}\).

Moreover
\[
V_m\Omega=\sqrt m\,\mathbf 1_{m\widehat{\mathbf Z}},
\qquad
\langle\Omega,V_m\Omega\rangle=m^{-1/2}.
\]

For \(m,n\ge1\),
\[
\begin{aligned}
\langle V_m\Omega,V_n\Omega\rangle
&=\sqrt{mn}\,\mu(m\widehat{\mathbf Z}\cap n\widehat{\mathbf Z})\\
&=\frac{\sqrt{mn}}{\operatorname{lcm}(m,n)}\\
&=\frac{\gcd(m,n)}{\sqrt{mn}}\\
&=\prod_p p^{-\frac12|v_p(m)-v_p(n)|}.
\end{aligned}
\]

Thus the critical GCD kernel is exactly the Gram kernel of normalized
divisibility-cylinder vectors in the Haar boundary.

The ghost cylinder law
\[
\mu(v_p=a)=(1-p^{-1})p^{-a}
\]
is therefore literally Haar measure on \(\widehat{\mathbf Z}\), not merely
analogous to it.

## 2. Exact local equivalence: Haar Gram = Poisson kernel = lossless phase

For \(p\) fixed put
\[
r_p=p^{-1/2}.
\]
The finite-place shadow kernel already derived in the arithmetic-shadow paper is
\[
K_p(\theta)=
\frac{1-r_p^2}{1+r_p^2-2r_p\cos\theta}.
\]
Its Fourier series is the Poisson expansion
\[
K_p(\theta)=\sum_{k\in\mathbf Z}r_p^{|k|}e^{ik\theta}.
\]
Therefore its \(k\)-th Fourier coefficient is
\[
\widehat K_p(k)=p^{-|k|/2}.
\]

Consequently
\[
\boxed{
\frac{\gcd(m,n)}{\sqrt{mn}}
=
\prod_p
\widehat K_p\!\bigl(v_p(m)-v_p(n)\bigr).
}
\]

So the global critical GCD Gram kernel is exactly the restricted tensor product
of the local finite-place shadow Poisson kernels.

There is also a lossless scattering realization.  The scalar Blaschke factor
\[
b_p(z)=\frac{z-r_p}{1-r_p z}
\]
is inner on the unit disk.  On \(z=e^{i\theta}\),
\[
\frac{d}{d\theta}\arg b_p(e^{i\theta})
=K_p(\theta).
\]
Thus the same local object appears in three exactly equivalent forms:

1. normalized Haar-cylinder Gram coefficient \(p^{-|a-b|/2}\);
2. Fourier coefficient of the shadow Poisson kernel;
3. phase derivative of a lossless one-channel Blaschke scattering factor.

With \(\theta=t\log p\),
\[
\arg b_p(e^{i\theta})
=
\theta+
2\sum_{m\ge1}\frac{p^{-m/2}}{m}\sin(mt\log p)
\]
(up to a constant branch choice).  Hence the nontrivial local scattering phase
has derivative
\[
2\sum_{m\ge1}(\log p)p^{-m/2}\cos(mt\log p),
\]
which is precisely twice the local von-Mangoldt prime-power current.  The
finite causal phase \(q_L\) is therefore the sharp-length truncation of the
sum of these local lossless phase shifts, together with the pole and
Archimedean counterphase.

This is an exact zero-independent local scattering interpretation of the
prime term.

## 3. Half-density from unitary finite-adelic dilation

Let \(\mathbf A_f\) be the finite adeles with additive Haar measure.  For
\(m\in\mathbf Q_+^\times\), define
\[
(U_mF)(x)=\sqrt m\,F(x/m).
\]
For integer \(m\), the finite-adelic modulus satisfies \(|m|_f=m^{-1}\),
hence \(U_m\) is unitary.  If \(P\) denotes projection from
\(L^2(\mathbf A_f)\) onto \(L^2(\widehat{\mathbf Z})\), then
\[
P U_m P = V_m.
\]

So the unilateral arithmetic isometries are compressions of genuine unitary
finite-adelic dilations.  The coefficient \(m^{-1/2}\) is fixed by Haar
normalization.

Introduce the gauge/dilation phase
\[
\alpha_t(V_m)=m^{-it}V_m.
\]
Then
\[
\langle\Omega,\alpha_t(V_m)\Omega\rangle
=m^{-1/2-it}.
\]
Hence the critical Mellin character \(m^{-s}\), \(s=1/2+it\), is an exact
vacuum matrix coefficient of the Haar-normalized dilation system.  Replacing
\(1/2\) by another real part changes the Haar normalization and destroys this
unitary half-density interpretation.

For finite \(L\),
\[
\left\langle\Omega,
\sum_{\log n\le L}\Lambda(n)\alpha_t(V_n)\Omega
\right\rangle
=
\sum_{\log n\le L}\frac{\Lambda(n)}{\sqrt n}\,e^{-it\log n},
\]
which is exactly the finite prime current appearing in the completed
arithmetic phase \(J_L\).

## 4. Doubled Gibbs / cross-boundary form

For \(\beta>1\), with
\[
|\Psi_\beta\rangle=
\zeta(\beta)^{-1/2}\sum_{n\ge1}n^{-\beta/2}|n,n\rangle,
\]
and multiplicative isometries \(V_m|n\rangle=|mn\rangle\),
\[
\langle\Psi_\beta|V_m\otimes V_n|\Psi_\beta\rangle
=\delta_{mn}m^{-\beta/2}.
\]
Therefore, for finite
\[
A_L=\sum_{\log n\le L}\sqrt{\Lambda(n)}\,V_n,
\]
one has
\[
\langle\Psi_\beta|
\alpha_t(A_L)\otimes A_L
|\Psi_\beta\rangle
=
\sum_{\log n\le L}\Lambda(n)n^{-\beta/2}e^{-it\log n}.
\]
At the boundary \(\beta\downarrow1\), every finite cutoff gives the exact
half-density prime current.  The prime term is therefore a genuine
cross-boundary correlation of the doubled arithmetic state.

## 5. Exact celestial Casimir dictionary

Set
\[
h=s,\qquad \Delta=2s,\qquad \nu=h-1=s-1.
\]
Then
\[
\Delta\mapsto2-\Delta
\iff
s\mapsto1-s
\iff
\nu\mapsto-\nu-1,
\]
and identically
\[
-\nu(\nu+1)=s(1-s).
\]

On the unitary principal series,
\[
s=\frac12+it,\qquad
\Delta=1+i\lambda,\qquad
\lambda=2t,
\]
so
\[
-\nu(\nu+1)=s(1-s)=\frac14+t^2=\frac{1+\lambda^2}{4}.
\]

Thus the celestial conical/Legendre Casimir and the arithmetic massive
half-density Casimir are the same quadratic spectral invariant under the
dictionary.  The \(1/4\) floor is the half-density shift.

## 6. What this changes about the RH target

The exact local picture is now:

\[
\text{Haar cylinder}
\;\longleftrightarrow\;
\text{Poisson/shadow kernel}
\;\longleftrightarrow\;
\text{lossless Blaschke phase}
\;\longleftrightarrow\;
\text{prime-power current}.
\]

The Archimedean/celestial side has, independently,

\[
\text{principal series}
\;\longleftrightarrow\;
\text{shadow }s\leftrightarrow1-s
\;\longleftrightarrow\;
\text{Legendre/Mehler--Fock kernel}
\;\longleftrightarrow\;
s(1-s).
\]

The remaining theorem is global, not local.  One must show that the completed
prime--Archimedean scattering response is the transfer function of a
conservative causal colligation with no incoming defect / no escaped shadow
endpoint.  The existing Hardy-leakage identity then gives RH.

Equivalently, construct an intertwiner that:
- sends the finite-place Haar dilation system to the completed causal Hardy
  representation;
- sends the Archimedean/celestial Casimir to the same \(s(1-s)\) spectral
  variable;
- preserves the completed von-Mangoldt current and pole subtraction;
- makes the completed causal transfer an isometry.

If such an intertwiner is constructed without importing zero data, the
bad-zero model space vanishes and RH follows.

These results do **not** yet establish that final no-escape theorem.
