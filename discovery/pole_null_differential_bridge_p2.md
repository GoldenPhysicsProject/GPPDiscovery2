# Pole-null first-order bridge between Discovery2 and Discovery5

**2026-11-01. Exact algebraic bridge; imported numerical certificates not independently replayed in this turn. RH remains OPEN.**

## Support and differential map

Discovery2 uses interval J=(0,s), s=7/10; Discovery5 uses (-L,L), hence L=s/2=7/20 and its edge parameter is
\[
\ell=2L-\log 2=s-\log 2=0.00685281944005\ldots<0.06.
\]
Both supports contain only the p=2 prime-power shift. Do not confuse the two meanings of L.

For \(\xi\in H^1_0(J)\), set \(f=D_+\xi=(\partial_x+1/2)\xi\). Integration by parts gives
\[
\|f\|_2^2=\int_J(|\xi'|^2+|\xi|^2/4)=:\|\xi\|_H^2,\qquad
M_+(f):=\int_J e^{x/2}f(x)dx=0.
\]
Conversely every \(f\in L^2(J)\) with \(M_+(f)=0\) has the unique inverse
\[
\xi(x)=e^{-x/2}\int_0^x e^{t/2}f(t)dt\in H^1_0(J).
\]
Thus \(D_+:H^1_0(J)\to\mathcal M=\ker M_+\) is an isometric isomorphism onto a closed **complex codimension-one** subspace.

## Exact equality of the two Weil forms

For the corrected v34 completed Weil form at this support, the all-scale Discovery2 thermal identity gives
\[
Q_s[f]=P[f]+\frac1{2\pi}\int_{\mathbb R}\Omega(t)|\hat f(t)|^2dt
-2c_2\operatorname{Re}\int_{\mathbb R}\overline{f(x)}f(x+a)dx,
\quad a=\log2,\ c_2=a/\sqrt2,
\]
where \(\Omega(t)=\operatorname{Re}\psi(1/4+it/2)-\log\pi\) and
\(P[f]=2\operatorname{Re}(M_+(f)\overline{M_-(f)})\).
The full contact is present, since
\[
\Omega(t)=-\kappa_\infty+2\int_0^\infty
\frac{e^{y/2}}{2\sinh y}(1-\cos ty)dy,\qquad
\kappa_\infty=\log(8\pi)+\gamma_E+\pi/2.
\]
For \(f=D_+\xi\), the pole term is zero; Plancherel gives
\(|\hat f(t)|^2=(t^2+1/4)|\hat\xi(t)|^2\).
The mixed derivative terms in the prime correlation cancel because the integral of
\(\partial_x(\overline\xi(x)\xi(x+a))\) vanishes. Consequently
\[
\operatorname{Re}\int\overline f(x)f(x+a)dx
=\operatorname{Re}\int(\overline{\xi'}(x)\xi'(x+a)+\overline\xi(x)\xi(x+a)/4)dx
=:B(\xi)
\]
and therefore the **exact smooth-test identity**
\[
\boxed{Q_s[D_+\xi]=\frac1{2\pi}\int(t^2+1/4)\Omega(t)|\hat\xi(t)|^2dt-2c_2B(\xi).}
\]
The RHS is Discovery5 Spectrum & Measure's Q=R-2c2 B after translation to its centered interval. It is a pole-null *restriction* of the genuine completed form, not a new OS covariance.

## Conditional-on-certificate consequence

Discovery5 team/spectrum-measure/CERT_p2_sectors.md reports outward Arb-certified bounds for its real parity sectors:
- reflection-odd \(\xi\): Q >= 0.008 ||xi||_H^2 for \(\ell\le0.21\);
- reflection-even \(\xi\): Q >= 0.009 ||xi||_H^2 for \(\ell\le0.06\).

Both apply at \(\ell=0.7-\log2\). Reality, reflection invariance and complex polarization therefore give, **subject to independent replay of these existing interval certificates and their source normalization**,
\[
\boxed{Q_{7/10}[f]\ge (1/125)\|f\|_2^2\quad
\text{for all smooth }f\in\ker M_+.}
\]
The closed-form extension needs standard domain justification. This directly bounds the full form's negative index by one, consistent with Discovery2's independent full-space comparison theorem. It does NOT settle the single missing direction. Caution: D_+ does not preserve reflection parity, so decompose \(\xi\), not \(f\).

## The exact remaining scalar Schur test

Fix any smooth compactly supported \(v\) with \(M_+(v)=1\), and write uniquely \(f=u+cv\), \(u\in\mathcal M\), \(c=M_+(f)\). Let q be Q's Hermitian polarization. Once the cross-functional q(u,v) is shown continuous in the positive \(\mathcal M\) energy norm, full positivity at this support is equivalent to the **one scalar condition**
\[
\boxed{\Sigma(v)=Q_s[v]-\sup_{u\in\mathcal M,\ u\ne0}
\frac{|q(u,v)|^2}{Q_s[u]}\ge0.}
\]
An infinite supremum means failure. Finite Galerkin minimization alone gives only an **upper** bound on Sigma. A genuine lower certificate must bound the dual-energy residual using the imported 1/125 floor, keeping all signed prime, pole and gamma terms. A positive scalar proves only this fixed-support result, not RH.

## Immediate validation

1. Replay Discovery5 cert/cert_galerkin_Q.py for its p2 sector bounds at ell=0.06 and 0.21; compare the completed digamma/contact and p2 normalization with Discovery2.
2. Compute a smooth normalized \(v\), its full signed Q value, and a certified Schur residual. Do not drop the positive prime-edge gradient or double-spend the Hardy endpoint potential.
3. Promote the first-order range theorem and form correspondence to GPPVerify once independently audited; only then explore the scalar certificate.
4. Keep shifted F_theta, DH/Epstein and CFT controls in the eventual global arithmetic-to-boundary selector test. This local hyperplane result is fake-blind.

Sources: Discovery2 complete_thermal_kms_global_identity.md, first_prime_exact_completed_resource_ledger.md, actual_p2_completed_negative_index_at_most_one_L7_10.md; Discovery5 CERT_p2_sectors.md; original corrected v34 semilocal Weil source.
