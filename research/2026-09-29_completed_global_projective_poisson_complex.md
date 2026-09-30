# The completed global-projective Poisson complex that retains the Mellin character

Date: 2026-09-29
Status: exact categorical construction through the zero-survival stage; exact Haar norm law; exact finite Poisson completion. The final subpower/physical-Hilbert identification is isolated and NOT proved here. No RH claim.

This note corrects the naive idea of using only the scalar cofiber
  [1 --xi(s)--> 1].
That scalar cofiber detects a zero but forgets the spectral parameter s. It therefore cannot by itself force principal-series membership.

The correct zero object must retain the multiplicative density character.

## 1. Ambient global category

Let U_ab be the full category of finite abelian groups with surjective homomorphisms, in the global-representation sense of Barrero--Barthel--Pol--Strickland--Williamson.

It is a multiplicative global family:
- subgroups of finite abelian groups are finite abelian;
- quotients are finite abelian;
- finite products are finite abelian.

Work over k=C.

The tensor unit 1 is projective because the trivial group belongs to U_ab. Hence it is compact in D(U_ab).

For cyclic groups write
  c_n := c_{C_n}=e_{C_n,C},
the standard projective associated to the trivial Out(C_n)-representation.

Barrero et al. give
  c_d(C_n) = C[s_d(C_n)],
where s_d(C_n) is the set of normal subgroups N of C_n with C_n/N ~= C_d.

Since C_n has a unique subgroup of each possible index,
  dim c_d(C_n)=1_{d|n}.

This is the divisor-incidence matrix.

## 2. Categorified zeta and Mobius automorphisms

Fix N and put
  P_N = direct_sum_{1<=n<=N} c_n.

For each d|n there is a canonical one-dimensional quotient-incidence morphism
  q_{n,d}: c_n -> c_d
corresponding to the unique kernel in C_n whose quotient has order d.

Normalize the basis so that quotient composition satisfies
  q_{d,e} q_{n,d} = q_{n,e}
for e|d|n.

Define the finite half-density zeta endomorphism
  Zcal_N : P_N -> P_N
by its (d,n)-component
  (Zcal_N)_{d,n}
    = sqrt(d/n) q_{n,d}       if d|n,
    = 0                       otherwise.

In the projective-generator basis its matrix is exactly Z_N^T, where the already formalized arithmetic operator is
  Z_N(n,d)=sqrt(d/n) 1_{d|n}.

Define
  (Mcal_N)_{d,n}
    = mu(n/d)sqrt(d/n) q_{n,d}
for d|n.

Then
  Mcal_N Zcal_N = Zcal_N Mcal_N = id_{P_N}.

Indeed, the coefficient of q_{n,e} in the composition is
  sqrt(e/n) sum_{e|d|n} mu(d/e)
or the reversed Mobius convolution, which vanishes unless e=n.

Thus the project zeta gauge is literally a natural automorphism of a finite projective global object, not merely a numerical matrix.

Let
  Dcal_N|_{c_n} = (log n) id_{c_n}.
Then the existing identity
  M D Z - D = L_Lambda
categorifies to
  Mcal_N Dcal_N Zcal_N - Dcal_N = Lcal_{Lambda,N},
whose quotient component is the half-density von-Mangoldt coefficient.

This recovers the entire finite zeta/Mobius/logarithmic gauge inside the global projective category.

## 3. The density-line global representation

For s in C define a one-dimensional global representation L_s by

  L_s(G)=C,

and for every surjection alpha:H ->> G with kernel size k=|ker alpha|,

  alpha_s^*(z)=k^{-s} z.

Functoriality is exact because kernel sizes multiply in composites:
if K ->> H ->> G, then
  |ker(K->G)| = |ker(K->H)| |ker(H->G)|
for finite surjections, so the multiplicative characters multiply.

Automorphisms have kernel size 1, hence Out(G) acts trivially.

There is an algebraic natural isomorphism
  tau_s: 1 -> L_s,
  tau_s(G)=|G|^{-s}.
Indeed, for alpha:H->>G,
  |ker alpha|^{-s}|G|^{-s}=|H|^{-s}.

Therefore every L_s is algebraically isomorphic to the tensor unit. In particular:
  - L_s is projective;
  - L_s is compact in D(U_ab);
  - every structural pullback is nonzero, so its canonical generator is torsion-free.

IMPORTANT NO-GO:
the ordinary algebraic global category cannot distinguish Re(s).
All density lines L_s are isomorphic there.
The spectral information lives in the HILBERT enrichment / norm growth.

## 4. Counting-Haar enrichment: the exact one-half theorem

Realize L_s(G) as the constant-function line inside l2(G) with counting Haar measure.

Write 1_G for the constant function. Then
  ||1_G|| = sqrt(|G|).

For alpha:H->>G with |ker alpha|=k, the s-twisted pullback sends
  1_G -> k^{-s} 1_H.

Therefore its exact operator norm on the constant line is

  ||alpha_s^*||
  = |k^{-s}| sqrt(|H|/|G|)
  = k^{1/2-Re(s)}.

Thus

  boxed:
  ||alpha_s^*|| = k^{1/2-Re(s)}.

For any nontrivial quotient k>1,

  ||alpha_s^*||=1
  iff
  Re(s)=1/2.

More weakly, iterate a fixed kernel-k quotient r times. The norm is
  k^{r(1/2-Re(s))}.
If both forward transport and its surviving inverse/retraction are bounded by
  exp(o(r)),
then necessarily
  Re(s)=1/2.

This is the finite-Haar/global-representation version of the already-proved continuous dilation theorem.

The principal-series one-half is therefore the UNIQUE Haar-isometric density exponent.

## 5. Exact Poisson-completed scalar without zeta analytic continuation

Let
  psi(x)=sum_{n>=1} exp(-pi n^2 x).

Poisson summation gives the theta relation and the standard entire completion

  Xi_P(s)
   = 1/2
     + [s(s-1)/2]
       integral_1^infinity psi(x)
       [x^{s/2}+x^{(1-s)/2}] dx/x.

This equals the Riemann xi function with the usual normalization.

The formula is:
- zero-independent;
- entire;
- invariant under s -> 1-s;
- already has the s=0,1 pole channels cancelled.

For a finite additive cutoff define
  psi_N(x)=sum_{1<=n<=N} exp(-pi n^2 x)
and
  Xi_N(s)
   = 1/2
     + [s(s-1)/2]
       integral_1^infinity psi_N(x)
       [x^{s/2}+x^{(1-s)/2}] dx/x.

Each Xi_N is entire and exactly shadow-symmetric:
  Xi_N(s)=Xi_N(1-s).

The Gaussian tail gives local-uniform convergence
  Xi_N -> xi
on all compact subsets of C.

So the elementary completion pole is cancelled at EVERY finite N before the limit is taken.

## 6. Correct retentive zero complex

Define the analytic family of two-term global complexes

  K(s):
    0 -> L_s --Xi_P(s)--> L_s -> 0.

This is a complex because the differential is a scalar natural endomorphism of L_s.

Since L_s ~= 1 algebraically, K(s) is perfect and compact.

If xi(s) != 0, the scalar differential is invertible, so
  K(s) ~= 0
in the derived category.

If xi(rho)=0, the differential vanishes and

  H_0 K(rho) ~= L_rho,
  H_1 K(rho) ~= L_rho.

Therefore every nontrivial zero produces a NONZERO COMPACT global object whose homology retains the full rho-density character.

This fixes the fatal defect of the scalar cofiber [1 --xi(s)--> 1], whose zero homology remembers only the unit object and loses s.

Moreover the surviving generator is torsion-free because every quotient pullback is multiplication by a nonzero number.

Thus the zero-survival part is exact:
  xi(rho)=0
  => a compact torsion-free global rho-line survives every finite-abelian quotient refinement.

Barrero et al. Theorem 7.7 is compatible with this and supplies the same no-disappearance conclusion abstractly for any nonzero compact realization; here the density-line model makes the surviving class explicit.

## 7. Finite Poisson complexes

At finite Gaussian cutoff N define

  K_N(s):
    0 -> L_s --Xi_N(s)--> L_s -> 0.

Each K_N(s) is perfect, compact, and entire in s.

At a zero rho_N of Xi_N,
  H_* K_N(rho_N) ~= L_{rho_N}.

Since Xi_N -> xi locally uniformly, Hurwitz/Rouche theory ensures that a genuine zero rho of xi is approximated, with multiplicity, by zeros of Xi_N in sufficiently small isolating disks.

This provides an honest finite compact approximation to every exact zero object.

It does NOT imply those finite zeros lie on the critical line.

## 8. Why this STILL does not prove RH by itself

The algebraic global category regards every L_s as isomorphic to 1.

So compactness and torsion-free survival alone do not force one-half.

The Haar norm law does force one-half if the physical realization of the surviving zero line has two-sided subpower transport.

Hence the remaining load-bearing statement is now exactly:

  PHYSICAL HILBERT REALIZATION THEOREM.

Construct a realization R_phys of the completed projective/Poisson complex such that:

(A) R_phys is faithful on the torsion-free zero homology of K(rho);

(B) for quotient towers whose total kernel size is Q,
    the induced maps on the surviving physical zero line and the corresponding
    retractions have norm Q^{o(1)};

(C) the realization is derived from the already-fixed half-density zeta gauge,
    co-Poisson boundary relation, and Riemann Archimedean seed, not from a
    rho-dependent metric.

Then the exact Haar norm law gives
  Q^{|Re(rho)-1/2|} <= Q^{o(1)},
hence
  Re(rho)=1/2.

This proves RH.

## 9. Why the existing estimates are pointed exactly at (B)

The project already has:
- finite half-density Z_N and M_N=Z_N^{-1};
- ||Z_N^{+/-1}|| = exp(o(L)) on divisor-closed sets n<=e^L;
- bounded Riemann-seed synthesis C;
- ||C Z_N|| = exp(o(L));
- the rank-two co-Poisson defect annihilated exactly by K_0=-d^2/du^2+1/4;
- the primal logarithmic current has only logarithmic/polynomial budget.

Thus the numerical size required in (B) is already available for the KNOWN bulk and Archimedean transport pieces.

The missing issue is no longer the estimate itself. It is the exact identification that the rho-line homology of K(rho) is carried by this physical completed transport rather than by the raw Mobius dual character.

Equivalently:
prove the zero line is represented AFTER Poisson/product-formula sewing, before scalarization.

## 10. Exact discrete intertwining with the Riemann seed

Let
  C e_n = n^{-1/2} T_{log n} phi
with the fixed Riemann seed phi.

Let S_m e_n=e_{mn} on the arithmetic coefficient basis, and let T_a be real translation on L2(R).

Then exactly

  C S_m = m^{-1/2} T_{log m} C.

Proof on e_n:
  C S_m e_n
   = (mn)^{-1/2} T_{log(mn)} phi
   = m^{-1/2} T_{log m}
       [n^{-1/2}T_{log n}phi]
   = m^{-1/2}T_{log m}C e_n.

Now a Mellin character a_s(n)=n^{-s} satisfies
  a_s(S_m e_n)=m^{-s}a_s(e_n).

Combining the two relations gives the centered physical character
  m^{1/2-s}.

Thus the exact arithmetic-to-Archimedean synthesis already carries the SAME
half-density-normalized scale character whose modulus is one exactly on Re(s)=1/2.

This is the key structural bridge:
the only remaining question is continuity/survival of the zero functional on the COMPLETED sewn image.

## 11. Smallest final theorem

The RH problem has now been compressed to the following statement.

Completed zero-line retention theorem:
For every nontrivial zero rho of xi, the torsion-free class in H_*K(rho) admits a nonzero continuous realization on the Poisson-sewn Riemann-seed boundary space, and under the exact intertwining
  C S_m = m^{-1/2}T_{log m}C
its forward and backward physical norms are m^{o(r)} along r-fold scale transport.

Once this is proved, no Weil positivity theorem is required:
the character is m^{r(1/2-rho)}, so subpower two-sided transport forces
  Re(rho)=1/2.

This is now the preferred principal-series closure target.


## 12. Exact generalized-eigencharacter identity for the half-density zeta incidence

There is a sharper arithmetic spectral statement hiding in the same matrix.

Let
  z=s-1/2
and define the centered power character
  v_s(n)=n^{-z}=n^{1/2-s}.

For the infinite algebraic transpose of the half-density zeta matrix,
  Z^T(d,n)=sqrt(d/n) 1_{d|n},
we have in the absolute Euler domain Re(s)>1:

  (Z^T v_s)(d)
   = sum_{n:d|n} sqrt(d/n) n^{1/2-s}.

Write n=dm. Then

  sqrt(d/(dm)) (dm)^{1/2-s}
   = m^{-1/2} d^{1/2-s} m^{1/2-s}
   = d^{1/2-s} m^{-s}.

Therefore

  boxed:
  Z^T v_s = zeta(s) v_s.

This is exact wherever the multiple sum converges absolutely.

Hence the centered Mellin character is a generalized eigencharacter of the
half-density zeta incidence transform, with eigenvalue zeta(s).

Formally,
  Z^{-T} v_s = zeta(s)^{-1} v_s.

The finite theorem found earlier,
  (Z_N^{-T}v_s)(d)
   = d^{1/2-s} sum_{m<=N/d} mu(m)m^{-s},
is exactly the cutoff reciprocal-eigenvalue relation. At a zeta zero the inverse
dual necessarily becomes singular.

This is a major conceptual simplification:

  zeta zero = completed generalized kernel character of half-density incidence.

The character itself is explicit and zero-independent:
  v_rho(n)=n^{1/2-rho}.

Its modulus is
  |v_rho(n)|=n^{1/2-Re(rho)}.

Thus the principal-series question becomes exactly whether the completed generalized
kernel character lives in the physical half-density boundary with subpower scale growth.

## 13. Archimedean multiplier completes the same eigenvalue

The fixed Riemann seed satisfies, with the established Fourier convention,

  phihat(t) zeta(1/2+it)=Xi(t),

where Xi is the centered completed zeta function.

Thus on the parameter
  s=1/2+it,
the arithmetic eigenvalue zeta(s) from section 12 is multiplied by the Archimedean
seed factor to give the completed eigenvalue.

This means the completed Poisson/Riemann synthesis is not adding an unrelated scalar
completion. It completes the eigenvalue of the SAME half-density incidence character.

The desired completed operator should therefore be read schematically as

  arithmetic half-density incidence
      --Archimedean Riemann-seed multiplier-->
  completed incidence,

with generalized character v_s and completed eigenvalue xi(s) (up to the fixed
normalization convention relating Xi(t) and xi(s)).

At xi(rho)=0, the completed generalized character v_rho is a kernel character.

This provides the missing non-arbitrary spectral interpretation of the retentive
cofiber K(rho).

## 14. Global-representation dual object and the remaining topology

Let
  P = direct_sum_{n>=1} c_n.

P is projective because projectives are closed under direct sums.

In a multiplicative global family, Barrero et al. record that projectives are also
closed under internal Homs. Therefore the internal functional object

  P^vee := Hom(P,1)

is again projective.

At the trivial group,
  P^vee(1)=Hom_A(P,1)
contains the product of the coefficient lines Hom(c_n,1), so centered power
characters are honest algebraic boundary elements there, not merely informal
sequences.

This is useful but does NOT by itself solve RH:
the completed generalized eigenrelation involves the transpose/multiple direction and
the Hilbert topology of that boundary element. Algebraic projectivity/injectivity does
not control the norm of the infinite dual character.

The exact missing promotion is:

  show that the Poisson/Riemann completion sends the algebraic generalized
  kernel character v_rho into a nonzero CONTINUOUS element/functional of the
  physical Haar-half-density boundary, with two-sided subpower transport.

Once this is done,
  |v_rho(n)|=n^{1/2-Re(rho)}
and the Haar quotient theorem force Re(rho)=1/2.


## 15. Important weakening: one-sided contractive survival plus the functional equation is enough

The previous formulation asked for two-sided subpower transport of a single zero line.
That is stronger than necessary because zeta already supplies the reflected companion zero.

Let V be an isometry (a contraction is enough) on a Hilbert realization, and let a
nonzero bounded functional ell_s satisfy
  ell_s(Vx)=chi_s ell_s(x),
with
  chi_s=m^{1/2-s},
  m>1.

Then
  ||ell_s o V|| <= ||ell_s||,
while covariance gives
  ||ell_s o V||=|chi_s| ||ell_s||.

Since ell_s is nonzero,
  |chi_s|<=1.

But
  |chi_s|=m^{1/2-Re(s)}.

Therefore
  Re(s)>=1/2.

Now use the unconditional zeta symmetry:
if rho is a nontrivial zero, then
  rho^sharp = 1-conj(rho)
is also a nontrivial zero.

If the SAME one-sided contractive survival theorem applies to every zero, it applies to
rho^sharp and gives
  Re(rho^sharp)>=1/2,
i.e.
  1-Re(rho)>=1/2,
so
  Re(rho)<=1/2.

Combining:
  boxed: Re(rho)=1/2.

Thus we do NOT need:
- a unitary group;
- a surjective isometry;
- two-sided scale transport;
- an inverse/retraction with a controlled norm.

We need only:

  EVERY zero survives as a nonzero bounded eigenfunctional of ONE common
  half-density quotient isometry/contraction.

The functional equation supplies the opposite inequality automatically.

This is materially weaker than the Astra two-sided theorem and fits the global-representation
tower much better, because its structural pullbacks are naturally one-sided.

## 16. New smallest closure theorem

Contractive zero-retention theorem:

Construct one zero-independent physical Hilbert completion H_phys of the half-density
global-projective / Poisson boundary and, for one fixed quotient scale m>1, an isometry
or contraction V_m on H_phys such that for every nontrivial zero rho there is a nonzero
bounded functional ell_rho with

  ell_rho(V_m x)=m^{1/2-rho} ell_rho(x).

Then RH follows immediately by section 15 and the functional equation.

This is now weaker than the two-sided subpower target and should be attacked first.

The exact Riemann-seed intertwining
  C S_m = m^{-1/2} T_{log m} C
already identifies the required half-density quotient dynamics.

What remains is only:
  prove the completed zero functional is bounded/nonzero on the Poisson-sewn image
  for EVERY zero.

The global-representation compact/torsion-free construction supplies the algebraic
nonzero class. The unresolved step is continuity under the physical Hilbert completion.


## 17. Operator-level correction: the E-map mapping cone supplies zero survival without inserting xi by hand

The scalar family K(s) is useful because it retains the density line, but it still
uses xi(s) as a scalar differential. The genuinely zero-independent operator is the
Riemann/Connes E-map itself.

Let
  g(u)=u^(1/2) f(u)
and on multiplicative half-density space use
  (U_n g)(u)=g(nu).

The exact critical transfer is
  Z_crit = sum_{n>=1} n^(-1/2) U_n
on the Poisson test domain / rigged completion.

For a complex Mellin parameter s define the evaluation functional
  ell_s(g)
    = integral_0^infinity g(u) u^(s-1/2) d*u
whenever justified on the chosen test space.

A change of variables gives the exact scale covariance
  ell_s(U_m g)
    = m^(1/2-s) ell_s(g).

Likewise,
  ell_s(Z_crit g)
    = sum_n n^(-1/2) ell_s(U_n g)
    = [sum_n n^(-s)] ell_s(g)
    = zeta(s) ell_s(g)
first in Re(s)>1.

Thus
  boxed:
  ell_s o Z_crit = zeta(s) ell_s.

This is the continuous/operator version of
  Z^T v_s = zeta(s) v_s.

At a nontrivial zeta zero rho, analytic continuation of the E-map Mellin identity gives
  ell_rho o Z_crit = 0.
Therefore ell_rho annihilates the E-map range and defines a nonzero algebraic/rigged
functional on the mapping-cone/cokernel cohomology, provided one chooses a seed with
ell_rho(g) != 0.

The same functional automatically has
  ell_rho o U_m
    = m^(1/2-rho) ell_rho.

So BOTH ingredients of the desired principal-series theorem -- zero survival and the
correct scale character -- arise from ONE zero-independent operator Z_crit.

No zero list and no rho-dependent metric are used.

The completed Riemann seed h is Fourier self-dual and k=E(h) has Mellin transform Xi.
The rank-two co-Poisson defect is killed exactly by K_0=-d^2/du^2+1/4, so the
s=0,1 elementary channels can be removed before taking the cohomology.

This is the operator-level realization that the scalar K(s) was encoding fiberwise.

## 18. Exact analytic obstruction: ordinary L2 closure kills the zero cohomology

One might now take the ordinary L2 closure of Ran(Z_crit) and quotient. That DOES NOT
solve the problem.

In Mellin space the critical transfer is multiplication by
  zeta(1/2-it)
on the real spectral axis (in the rigged sense). This multiplier is nonzero almost
everywhere on R. Consequently its maximal multiplication range is dense in ordinary
L2. The closed L2 cokernel is zero.

This agrees exactly with the independent Astra no-go for the maximal xi multiplier.

Therefore:
- the E-map gives all zero characters in algebraic/rigged cohomology;
- ordinary L2 completion erases them;
- the missing physical topology must retain the E-map cohomology without losing the
  half-density contraction property.

This identifies the no-escape theorem with complete precision.

## 19. Why global representation theory still matters after the E-map correction

The global-projective construction is not replacing the E-map cohomology. It supplies
finite compact arithmetic models of it.

At cyclic finite level:
- c_d(C_n) is divisor incidence;
- Zcal_N is the finite half-density zeta transfer;
- Mcal_N is its Mobius inverse;
- the torsion-free theorem prevents algebraic disappearance under enlargement of the
  finite-abelian quotient system.

The E-map is the continuous Poisson-sewn limit:
  Z_crit = sum_n n^(-1/2) U_n.

Thus the finite projective tower and the continuous E-map are two realizations of the
same half-density incidence transfer.

The exact remaining theorem can now be stated without ambiguity:

  HILBERTIZED E-MAP COHOMOLOGY THEOREM.
  Construct a zero-independent Hilbert/OS completion of the E-map mapping cone such
  that:
  (i) every nontrivial zero functional ell_rho remains nonzero and bounded;
  (ii) one multiplicative quotient/dilation U_m induces a contraction;
  (iii) the Poisson reflection and rank-two completion are preserved.

Then the one-sided reflected contraction theorem proves RH.

This is strictly smaller than proving full Weil positivity, but it is not automatic:
ordinary L2 violates (i), while real-trace Sobolev completions can violate off-real
retention.
