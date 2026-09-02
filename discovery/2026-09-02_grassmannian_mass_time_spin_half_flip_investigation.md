# Grassmannian mass–time–spin–half-flip investigation

Date: 2026-09-02
Branch: `codex/discovery-workbench`
Status: discovery mathematics; exact results are separated from physical identifications and theorem targets.

## 1. Starting point already formalized in GPPVerify

On the big cell of `Gr(2,4)`, write

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad D=\det A=ad-bc\neq0,
\]

and

\[
\varepsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
\tau(A)=\frac{A\varepsilon}{D}.
\]

`GppVerify/GrassmannianMass.lean` proves

\[
\det \tau(A)=D^{-1},\qquad \tau^2(A)=-A,\qquad \tau^4(A)=A,
\]

and proves that the period is exactly four on the big cell.

`GppVerify/GrassmannianJacobian.lean` defines the denominator-cleared Jacobian numerator `N` and proves

\[
N^2=D K,\qquad K^2=D^2 I,\qquad N^4=D^4I.
\]

`GppVerify/StandardModel/MassOrientationCoupling.lean` separately proves the positive Hermitian momentum factorization and determinant/symplectic identity

\[
p=\lambda_1\lambda_1^\dagger+\lambda_2\lambda_2^\dagger,
\qquad
\det p=|\langle\lambda_1,\lambda_2\rangle|^2,
\]

under its stated positivity hypotheses, and formalizes the rest-frame clock-locking special values and chiral populations.

The old tangent-space claim `J^2=-I` is false and has already been retired. The nonlinear map itself, not its same-point Jacobian, is the object satisfying `tau^2=-id`.

## 2. New exact simplification of the differential

The Jacobian admits a much cleaner analytic form than the raw 4x4 numerator matrix suggests.

For a tangent perturbation `H in M_2`, Jacobi's determinant formula gives

\[
dD_A(H)=D\,\operatorname{tr}(A^{-1}H).
\]

Differentiating

\[
\tau(A)=D^{-1}A\varepsilon
\]

gives

\[
d\tau_A(H)
=\frac1D\left(H\varepsilon-A\varepsilon\operatorname{tr}(A^{-1}H)\right).
\tag{2.1}
\]

Now left-trivialize the tangent space by writing

\[
H=AX.
\]

Then Eq. (2.1) becomes

\[
d\tau_A(AX)=\frac1D A\,\mathcal L(X),
\]

where the **universal tangent operator** is

\[
\boxed{\mathcal L(X)=X\varepsilon-\varepsilon\operatorname{tr}X.}
\tag{2.2}
\]

Thus `d tau_A` is similar, via the invertible left-multiplication map `X -> AX`, to the constant operator

\[
\frac1D\mathcal L.
\tag{2.3}
\]

This completely separates geometry from scale: all dependence on the point `A` is the single scalar `D^{-1}`; all quarter-turn structure lives in one universal operator `L`.

For

\[
X=\begin{pmatrix}x&y\\z&w\end{pmatrix},
\]

Eq. (2.2) gives

\[
\mathcal L(X)=
\begin{pmatrix}
-y&-w\\x&z
\end{pmatrix}.
\]

Repeated application gives

\[
\mathcal L^2(X)=
\begin{pmatrix}
w&-z\\-y&x
\end{pmatrix},
\]

\[
\mathcal L^3(X)=
\begin{pmatrix}
z&-x\\w&-y
\end{pmatrix},
\]

and exactly

\[
\boxed{\mathcal L^4=I.}
\tag{2.4}
\]

This is a substantially cleaner theorem target for Lean than reasoning through generic eigenvalue multisets.

## 3. Exact characteristic polynomial follows immediately

In the ordered coordinate basis `(x,y,z,w)`, the universal operator is

\[
[\mathcal L]=
\begin{pmatrix}
0&-1&0&0\\
0&0&0&-1\\
1&0&0&0\\
0&0&1&0
\end{pmatrix}.
\]

Direct symbolic factorization gives

\[
\chi_{\mathcal L}(t)
=(t-1)(t+1)(t^2+1)=t^4-1.
\tag{3.1}
\]

Therefore, by similarity (2.3),

\[
\boxed{
\chi_{d\tau_A}(t)=t^4-D^{-4}.
}
\tag{3.2}
\]

Over `C`,

\[
\operatorname{spec}(d\tau_A)
=\left\{D^{-1},-D^{-1},iD^{-1},-iD^{-1}\right\}.
\tag{3.3}
\]

Hence every differential eigenvalue has exactly the same modulus:

\[
\boxed{|\lambda|=|D|^{-1}.}
\tag{3.4}
\]

This upgrades the old numerical `mean |eigenvalue|` observation: there is no averaging phenomenon. All four moduli are identical because the tangent operator is a universal fourth-root-of-unity operator multiplied by `D^{-1}`.

This should replace the current open `differential_charpoly : True` scaffold in `MassOrientationCoupling.lean`.

## 4. Why `tau^2=-id` does not imply `(d tau_A)^2=-I`

The chain rule gives the correct relation:

\[
d(\tau^2)_A
=d\tau_{\tau(A)}\circ d\tau_A
=-I.
\tag{4.1}
\]

The two Jacobians are evaluated at different points. In general

\[
d\tau_{\tau(A)}\neq d\tau_A,
\]

so Eq. (4.1) does **not** imply

\[
(d\tau_A)^2=-I.
\]

This is the conceptual explanation of the earlier false tangent-space complex-structure claim. The order-four structure belongs globally to the nonlinear transition; the same-point tangent map has its own period-four spectral polynomial (3.2).

## 5. A stronger normalized tangent theorem

Define the determinant-normalized differential

\[
\widehat J_A:=D\,d\tau_A.
\]

By Eq. (2.3), `hat J_A` is similar to `L`. Therefore

\[
\boxed{\widehat J_A^4=I}
\tag{5.1}
\]

and

\[
\boxed{\chi_{\widehat J_A}(t)=t^4-1.}
\tag{5.2}
\]

This is point-independent. The Grassmannian transition thus separates canonically into

1. a universal `Z_4` tangent action;
2. one reciprocal scalar `D^{-1}`.

This is mathematically sharper than saying merely that the transition has period four.

## 6. Exact eigenvectors of the universal tangent operator

The four eigenspaces are one-dimensional over `C`. In `(x,y,z,w)` coordinates one may choose

\[
v_{+1}=(1,-1,1,1),
\]

\[
v_{-1}=(1,1,-1,1),
\]

\[
v_{+i}=(-1,i,i,1),
\]

\[
v_{-i}=(-1,-i,-i,1).
\]

Consequently eigenvectors of `d tau_A` are obtained by left multiplication with `A`:

\[
H_\zeta=A X_\zeta,
\qquad
\zeta\in\{1,-1,i,-i\},
\]

with eigenvalue `zeta/D`.

This explicit basis should make the Lean characteristic-polynomial theorem much easier: instead of invoking an abstract nonsymmetric spectral theorem, one can either formalize `L^4=I` plus its 4x4 determinant, or verify four explicit eigenvectors after complexification.

## 7. Physical mass bridge: what is already proved and what is not

There are **two determinant statements** and they must not be silently identified.

### 7.1 Standard massive momentum determinant

For a Hermitian momentum bispinor

\[
p_{\alpha\dot\alpha}=p_\mu\sigma^\mu_{\alpha\dot\alpha},
\]

standard spinor-helicity gives

\[
\det p=p^2=m_{\rm phys}^2
\]

and the rank-two decomposition

\[
p=\lambda_1\lambda_1^\dagger+\lambda_2\lambda_2^\dagger,
\qquad
m_{\rm phys}^2=|\langle12\rangle|^2.
\]

The determinant/symplectic part is already formalized in `momentum_spinor_decomposition`.

### 7.2 Grassmannian chart determinant

The big-cell matrix `A` has

\[
D=\det A=p_{23}/p_{01}
\]

in the standard Plücker normalization `p_{01}=1`.

Calling `|D|` *the* physical mass requires an explicit dictionary from the projective Plücker coordinates of the 2-plane to the dimensionful Hermitian momentum matrix. The current Lean definition `massParameter := |D|` names a chart parameter; it does not by itself prove `|D| = m_phys`.

This is the main physical bridge theorem still required.

Likely clean formulation: choose a physical scale `mu_*` and a real/Hermitian slice of the Grassmannian momentum chart, then prove

\[
m_{\rm phys}=\mu_*\,F(|D|)
\]

for the correct projectively invariant `F`. If the chosen normalization makes `F(r)=r`, state the normalization explicitly. A dimensionful mass cannot be literally equal to an unscaled projective coordinate without such a choice.

## 8. Mass–clock–ruler theorem once the bridge is fixed

Independently of the Grassmannian interpretation, for a massive worldline

\[
S=-m_{\rm phys}c^2\int d\tau
\]

implies

\[
d\phi=-\frac{m_{\rm phys}c^2}{\hbar}\,d\tau,
\qquad
\omega_C=\frac{m_{\rm phys}c^2}{\hbar}.
\]

The reduced Compton ruler is

\[
\bar\lambda_C=\frac{\hbar}{m_{\rm phys}c},
\]

so

\[
\boxed{\bar\lambda_C\omega_C=c.}
\tag{8.1}
\]

For Dirac zitterbewegung,

\[
\omega_Z=2\omega_C,
\qquad
a_Z=\bar\lambda_C/2,
\]

and therefore

\[
\boxed{a_Z\omega_Z=c.}
\tag{8.2}
\]

If the physical chart bridge yields `m_phys proportional to |D|`, Eqs. (3.4), (8.1) give a genuine geometry/physics dictionary:

\[
|D|\leftrightarrow m_{\rm phys}\leftrightarrow\omega_C,
\qquad
|D|^{-1}\leftrightarrow m_{\rm phys}^{-1}\leftrightarrow\bar\lambda_C.
\]

The key point is reciprocal pairing, not numerology: the same determinant controlling the chart differential controls the two reciprocal Compton scales after the physical normalization is supplied.

## 9. Spin / order-four theorem target

Three exact order-four patterns now coexist:

### Grassmannian

\[
\tau^2=-I,\qquad\tau^4=I.
\]

### Spin cover

For a spin-1/2 rotation,

\[
U(2\pi)=-I,\qquad U(4\pi)=I.
\]

### Rest-frame Dirac clock

With

\[
U_D(t)=e^{-i\omega_C t\sigma_1},
\]

\[
U_D(\pi/\omega_C)=-I,
\qquad
U_D(2\pi/\omega_C)=I.
\]

The existing equalities do not yet prove these are the same `Z_4` representation. The correct theorem target is an intertwiner, not another comparison of periods.

Seek a map

\[
\Phi:\mathcal G_m\to\mathcal H_{\rm Dirac}
\]

or on an appropriate 2-dimensional quotient/subrepresentation such that

\[
\boxed{\Phi\circ\tau=U_{1/4}\circ\Phi}
\tag{9.1}
\]

for a quarter-cycle Dirac/spin operator `U_{1/4}`, and consequently

\[
\Phi\circ\tau^2=(-I)\circ\Phi.
\tag{9.2}
\]

A full four-real-dimensional tangent space cannot be naively identified with one complex 2-spinor merely from dimension counting; an invariant complex structure/real form or a canonical 2-complex-dimensional representation must be specified.

Promising route: the normalized tangent operator `L` already has eigenvalues `1,-1,i,-i`. Complexifying and selecting the `±i` sector gives a natural complex two-plane on which a quarter-turn acts by phases. Determine whether this subspace is canonically the Weyl/chirality space under the Klein/spinor correspondence.

## 10. Half-flip compatibility

For an oriented charged worldline, the exact relational charge is

\[
Q_{\rm rel}=q\,\epsilon_t,
\qquad
\epsilon_t=\operatorname{sgn}(dt/d\lambda).
\]

Therefore

\[
(q,\epsilon_t)\sim(-q,-\epsilon_t),
\]

while either single flip reverses `Q_rel`:

\[
(-q,\epsilon_t)\sim(q,-\epsilon_t)
\]

as the opposite relational class.

Equivalently

\[
(\mathbb Z_2\times\mathbb Z_2)/\langle(-1,-1)\rangle\cong\mathbb Z_2.
\]

The worldline coupling makes this exact:

\[
S_{\rm int}[q,\gamma]=q\int_\gamma A,
\]

\[
S_{\rm int}[q,-\gamma]=S_{\rm int}[-q,\gamma],
\qquad
S_{\rm int}[-q,-\gamma]=S_{\rm int}[q,\gamma].
\]

The open bridge is to derive the worldline-orientation sign from the Grassmannian/Dirac order-four structure rather than postulate it. A plausible architecture is that the **square** of the quarter-turn is the central sign `-1`, while projection to the relational `Z_2` remembers only whether one or both orientation data have been flipped.

Do not identify this with Wigner `T`: `epsilon_t` is geometric line orientation, while Wigner time reversal is antiunitary and preserves the positive-energy spectrum.

## 11. A potentially stronger gauge formulation

The charge half-flip can be packaged as a twisted `U(1)` structure. Complex conjugation is the automorphism

\[
z\mapsto\bar z=z^{-1}
\]

of `U(1)`. Therefore

\[
U(1)\rtimes_{\rm conj}\mathbb Z_2\cong O(2).
\]

If the disconnected `Z_2` is identified with the time-orientation double cover, charge becomes an orientation-twisted weight: changing the orientation trivialization sends `q -> -q`, while the twisted object itself is unchanged.

This mathematical construction is standard as a semidirect product / twisted coefficient system; the *physical identification* of its `Z_2` with temporal orientation is an additional hypothesis. It should be investigated using principal `O(2)` bundles or Real `U(1)` bundles rather than asserted as ordinary QED.

A theorem target is:

> Given a time-orientation double cover `M~ -> M`, an `O(2)` bundle whose determinant/disconnected-component bundle is identified with that cover restricts on every chosen time-oriented sheet to an ordinary `U(1)` gauge bundle, while the nontrivial deck transformation exchanges weights `n <-> -n`.

This would make the half-flip a bundle statement rather than sign bookkeeping.

## 12. Current strongest synthesis, with claim boundaries

What is exact/formalized or immediately derivable:

1. `tau^2=-id`, `tau^4=id`, exact period four on the Grassmannian big cell.
2. `det tau(A)=1/det A`.
3. `N^4=D^4 I` for the denominator-cleared Jacobian numerator.
4. New analytic reduction `d tau_A ~ D^{-1} L` with universal `L(X)=X eps-eps tr X`.
5. `L^4=I`, `charpoly(L)=t^4-1`, hence `charpoly(d tau_A)=t^4-D^-4` and all eigenvalue moduli `|D|^-1`.
6. Massive Hermitian momentum has rank two and `det p=m_phys^2=|<12>|^2` under the standard physical identification; determinant/symplectic factorization is already formalized.
7. Proper-time phase rate `omega_C=m_phys c^2/hbar`, Compton ruler `hbar/(m_phys c)`, and their product `c`.
8. Rest Dirac clock special values and chiral population oscillation are already formalized in the current mass-orientation module.
9. The oriented-current/Wilson-line half-flip quotient is exact in its stated sector.

Still open and decisive:

A. prove the exact projective/physical map relating Grassmannian `D` to dimensionful `m_phys`;
B. formalize the new universal tangent operator theorem and close `open_differential_charpoly` without a spectral axiom;
C. construct a canonical Grassmannian-to-spinor/Dirac intertwiner, or prove an obstruction;
D. derive, rather than name, a microscopic temporal orientation variable from that construction;
E. connect the derived orientation variable to the half-flip quotient;
F. derive macroscopic record-arrow inheritance from a many-body/open-system model;
G. test the full construction against chiral electroweak and CP-violating observables.

## 13. Immediate formalization targets

Highest-value next Lean targets in `GPPVerify`:

1. Define `L : Matrix (Fin 2) (Fin 2) R -> Matrix ...` by `X*epsilon - trace X • epsilon` and prove `L^[4] X = X` directly.
2. Prove the differential formula algebraically as a directional rational derivative, or at minimum prove the explicit 4x4 Jacobian is conjugate/similar to `D^-1 * Lmat` using the left-multiplication change of basis.
3. Prove the 4x4 characteristic polynomial directly from the explicit universal matrix `Lmat`; this avoids general eigenvalue enumeration.
4. Deduce `charpoly(d tau_A)=t^4-D^-4` for `D != 0`.
5. Retire `open_differential_charpoly : True`.
6. Add a theorem connecting the existing `momentum_spinor_decomposition` symplectic determinant to the appropriate Plucker coordinate, with all normalization/units hypotheses explicit.

## 14. Falsifiers / likely obstruction points

- If the physical `D <-> m` identification depends on arbitrary projective normalization, mass is not the bare chart determinant; replace it by a projectively invariant ratio plus external scale.
- If no canonical invariant subspace of the Grassmannian `Z_4` representation maps to the Dirac spin representation, the common-order-four story remains analogy rather than unification.
- If temporal line orientation cannot be recovered covariantly without adding hidden structure that violates positive-energy QFT, the literal zitter temporal-switchback hypothesis fails.
- If the proposed time-orientation-twisted `O(2)` bundle introduces an unwanted locally gaugeable charge-conjugation degree of freedom, constrain the `Z_2` projection to equal the fixed spacetime orientation local system rather than treating it as an independent gauge field.

## Bottom line

The strongest new mathematics from this investigation is the universal tangent reduction

\[
\boxed{
d\tau_A \sim \frac1{\det A}\,\mathcal L,
\qquad
\mathcal L(X)=X\varepsilon-\varepsilon\operatorname{tr}X,
\qquad
\mathcal L^4=I.
}
\]

It explains the exact fourth-root spectrum without averaging, repairs the old false `J^2=-I` intuition, and exposes a clean separation between a universal order-four orientation operator and a reciprocal determinant scale. That is the most promising mathematical bridge presently available between the Grassmannian theorem and the mass/Compton/spin programme.