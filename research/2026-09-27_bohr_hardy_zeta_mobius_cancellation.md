# Bohr-Hardy zeta/Mobius cancellation beyond the scalar Euler domain

Date: 2026-09-27
Status: exact zero-independent Hilbert-space theorem. No RH claim and no zero data.

This note follows the arithmetic Hardy-AdS2 / prime-torus synthesis and applies the project heuristic "cancel before scalarization" literally.

## 1. Prime torus Hardy space

Let

K_ar = product_p S1

with Haar probability measure. For every positive integer

n=product_p p^(nu_p(n))

define the character

chi_n(z)=product_p z_p^(nu_p(n)).

Unique factorization makes {chi_n:n>=1} an orthonormal basis of the positive Hardy cone H2_+(K_ar).

For s=sigma+i t with sigma>1/2 define

Z_s(z)=sum_{n>=1} n^(-s) chi_n(z),

M_s(z)=sum_{n>=1} mu(n)n^(-s)chi_n(z).

Both series converge in H2 because

sum_n |n^(-s)|^2 = zeta(2 sigma)<infinity

and |mu(n)|<=1.

In fact

boxed:
||Z_s||_2^2 = zeta(2 sigma),

and, using the squarefree Euler product,

boxed:
||M_s||_2^2
=
sum_n mu(n)^2 n^(-2 sigma)
=
product_p (1+p^(-2 sigma))
=
zeta(2 sigma)/zeta(4 sigma).

Both are H2-valued holomorphic functions on Re s>1/2 because all coefficient derivatives acquire only powers of log n, still locally square-summable there.

## 2. Finite-prime cancellation is exact

For a finite prime set P define

Z_{s,P}(z)
=
product_{p in P}(1-p^(-s)z_p)^(-1),

M_{s,P}(z)
=
product_{p in P}(1-p^(-s)z_p).

The first is the bosonic geometric tower and the second is the signed two-level/Mobius factor.

Pointwise on K_ar,

boxed:
Z_{s,P} M_{s,P}=1.

This is local prime-by-prime cancellation, not an asymptotic statement.

## 3. The cancellation survives the infinite-prime limit in H1 for Re s>1/2

As P increases through the primes,

Z_{s,P}->Z_s in H2,
M_{s,P}->M_s in H2.

The second convergence holds because product_p(1+p^(-2sigma)) converges exactly when sigma>1/2.

By Holder,

||Z_{s,P}M_{s,P}-Z_sM_s||_1
<=
||Z_{s,P}-Z_s||_2 ||M_{s,P}||_2
+
||Z_s||_2 ||M_{s,P}-M_s||_2
->0.

Since every finite product is exactly one,

boxed:
Z_s M_s = 1
in L1(K_ar), for every Re s>1/2.

This extends the exact zeta/Mobius inverse relation as a compact-group Hardy identity strictly beyond the ordinary scalar Euler-product domain Re s>1.

It does NOT say that scalar zeta(s) is nonzero there, because scalarization is the difficult step below.

## 4. Why this does not trivially prove RH

For Re s>1, evaluation at the arithmetic phase point

alpha_0=(1,1,...)

is justified by absolute convergence and

Z_s(alpha_0)=zeta(s),
M_s(alpha_0)=1/zeta(s).

For 1/2<Re s<=1, point evaluation at alpha_0 is not a bounded functional on H2(K_ar). The H2 identity therefore cannot simply be evaluated termwise.

This is the exact boundary-evaluation obstruction.

A naive argument

"Z_s M_s=1 in H1, therefore zeta(s) cannot vanish"

is invalid because it silently assumes continuity and multiplicativity of the singular scalar boundary evaluation.

This is a particularly useful no-go: the internal arithmetic state is already invertible in the correct compact Hilbert-space sense throughout the open critical half-plane. The nontrivial zero problem lives in the reconstruction/scalarization map, not in failure of the internal prime state.

## 5. Physical reading: exact boson/fermion cancellation before scalarization

At each prime,

(1-p^(-s)z_p)^(-1)

is the bosonic occupation tower, while

(1-p^(-s)z_p)

is the signed local Mobius/fermionic factor.

Their product is one before any scalar observable is taken.

Thus the prime-torus theory has an exact graded cancellation:

boxed:
bosonic Euler field x Mobius ghost field = vacuum.

Both separate H2 norms diverge at the critical half-density sigma->1/2+, while their product remains exactly one in H1 for every sigma>1/2.

This is an explicit realization of the project heuristic:
KEEP THE GRADED OBJECT UNTIL CANCELLATION IS COMPLETE; DO NOT TAKE SEPARATE SCALAR NORMS FIRST.

The divergence at sigma=1/2 is therefore not evidence that the paired internal system fails. It says the individual boson and ghost sectors cease to be ordinary H2 vectors at the boundary.

## 6. Holographic reconstruction interpretation

The scalar completed zeta response should be viewed as a reconstruction/evaluation of the internal prime-torus Hardy state after coupling to the real-place/Archimedean channel.

The exact internal inverse identity suggests a sharpened RH target:

Construct a completed reconstruction map E on the globally sewn prime-Archimedean algebra such that, for Re s>1/2,

1. E agrees with ordinary scalar Euler evaluation in Re s>1;
2. E respects the required product/inverse identity on the physical quotient;
3. E is continuous in the topology supplied by the completed boundary theory.

If E(Z_s M_s)=E(1)=1 and multiplicativity holds on the relevant pair, then E(Z_s) cannot vanish in the open half-plane. By the functional equation this would force all nontrivial zeros to the boundary Re s=1/2.

This reconstruction theorem is RH-strength and is not proved here. The gain is localization: the prime-side inverse already exists; the missing theorem is precisely continuity/multiplicativity of completed scalar reconstruction.

## 7. Relation to current project objects

This structure aligns with several independently derived pieces:

- the BPY/Gaussian arithmetic gauge M(s)Z(s)=I in the safe scalar/operator domain;
- the Hardy model-space statement that off-critical zeros appear as inner/Blaschke defects;
- the primitive-temperateness theorem, which isolates boundary-distribution admissibility;
- the TFD rule that the symmetric observable must be selected before tracing the doubled system;
- the critical Gibbs weak-escape mode at sigma=1/2.

The new point is that the prime-torus Hardy realization makes cancellation exact all the way down to Re s>1/2 BEFORE scalar evaluation.

## 8. New frontier

Do not try first to prove positivity of the scalar prime series.

Instead construct the scalar reconstruction map from the already-invertible internal H2 pair.

Candidate mechanisms to test:
- Archimedean Schur/Feshbach compression;
- a rigged-Hardy evaluation functional controlled by the primitive discrepancy;
- a de Branges/Rovnyak quotient where the bad-zero model space is exactly the failure of reconstruction multiplicativity;
- a BPY connected-state matrix coefficient in which the vacuum evaluation is replaced by an honest bounded observable.

If the reconstruction map can be made an algebra homomorphism on the physical quotient without assuming zero locations, RH closes immediately.
