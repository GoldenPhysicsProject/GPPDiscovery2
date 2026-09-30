# Hardy-strip Hilbertization of E-map cohomology: universal zero retention and exact growth lower bound

Date: 2026-09-29
Status: exact RKHS/Hilbert-space calculations and a zero-retention theorem conditional only on the established E-map Mellin identity on the Poisson test domain. No RH claim.

This reconstructs the interrupted Work-session route visible in Daniel's screenshots:
weighted Hilbert space -> exact kernel -> Hardy-strip quotient -> spectral-bound control.

The live Work branch did not persist those final steps, so they are reconstructed here from first principles and the existing E-map construction.

## 1. Symmetric Hardy-strip space

For a>0 define H_a as the Fourier-Laplace image of measurable h on R with

  ||h||_a^2
    = integral_R |h(xi)|^2 2 cosh(2 a xi) dxi < infinity.

With Fourier normalization

  F(z)=(2 pi)^(-1/2) integral_R h(xi)e^{i xi z} dxi,

F is holomorphic in the strip

  S_a={z: |Im z|<a}.

The weight
  2 cosh(2a xi)=e^{2a xi}+e^{-2a xi}
is exactly the sum of the two boundary Hardy weights, so H_a is the symmetric
two-boundary Hardy space for S_a.

## 2. Exact reproducing kernel

For z,w in S_a,

  K_a(z,w)
   = (1/(2 pi)) integral_R
      e^{i xi(z-conj w)} / [2 cosh(2a xi)] dxi.

Using
  integral_R e^{itu}/cosh(u) du = pi/cosh(pi t/2),
one obtains

  boxed:
  K_a(z,w)
   = [1/(8a)]
     sech( pi (z-conj w)/(4a) ).

In particular, for z=x+iy,

  boxed:
  K_a(z,z)
   = [1/(8a)] sec( pi y/(2a) ).

Hence point evaluation is bounded exactly for |y|<a and blows up at the two strip boundaries.

## 3. The universal width a=1/2 retains every nontrivial zeta zero

Write a nontrivial zero as

  rho=sigma+i gamma,
  0<sigma<1,

and use the centered spectral coordinate

  z_rho=-gamma+i(sigma-1/2),

so that

  rho = 1/2 - i z_rho.

Then

  |Im z_rho|=|sigma-1/2|<1/2.

Therefore every nontrivial zero defines a bounded evaluation functional on the ONE
zero-independent Hilbert space H_{1/2}.

Its exact squared norm is

  ||ev_{z_rho}||^2
   = 1/4 sec( pi(sigma-1/2) )
   = 1/[4 sin(pi sigma)].

So the evaluation norm is finite throughout the open critical strip and diverges only
at the strip boundaries sigma=0,1.

This is an exact Hilbert-retention theorem, not a numerical observation.

## 4. E-map quotient retains every zero continuously

Use the critical Riemann/Connes E-map transfer on a Poisson test domain D,

  E = sum_{n>=1} n^(-1/2) U_n,

with centered Mellin/Hardy evaluation ell_s satisfying

  ell_s(U_m f)=m^(1/2-s) ell_s(f),

and, by the E-map Mellin identity and analytic continuation on D,

  ell_s(E f)=zeta(s) ell_s(f).

Choose D so that its E-images lie in H_{1/2}; for example one may work with a dense
analytic test domain whose Fourier-Laplace transforms decay faster than the fixed strip
weight.

Define

  M = closure_{H_{1/2}} E(D),
  Q = H_{1/2}/M.

At a nontrivial zero rho,

  ell_rho(E f)=0 for every f in D.

Because ell_rho is bounded on H_{1/2}, it also vanishes on M and therefore descends to
a bounded functional on Q.

It is nonzero: point evaluation itself is nonzero on H_{1/2}, so if it vanished on all
of Q it would vanish on all of H_{1/2}. Hence M is proper.

Therefore:

  boxed:
  EVERY nontrivial zeta zero survives as a nonzero bounded functional
  on one fixed zero-independent Hilbert quotient Q.

This closes the continuity/no-escape problem at the level of symmetric strip retention.

The price appears in the dynamics below.

## 5. Exact scale action on H_a

For t real define

  (V_t F)(z)=e^{i t z}F(z).

On Fourier coefficients this is translation:
  h(xi) -> h(xi-t).

Therefore

  ||V_t||^2
   = sup_xi cosh(2a(xi+t))/cosh(2a xi)
   = e^{2a|t|},

so

  boxed:
  ||V_t|| = e^{a|t|}.

This is sharp.

At z_rho,

  ev_{z_rho}(V_tF)
    = e^{i t z_rho} ev_{z_rho}(F)
    = e^{(1/2-rho)t} ev_{z_rho}(F).

Thus the retained zero functional carries EXACTLY the desired centered Mellin character.

For a=1/2 the ambient bound is

  ||V_t|| = e^{|t|/2}.

That is exactly the full critical-strip width and therefore gives only the classical
0<Re rho<1 constraint, not RH.

## 6. Universal spectral-growth lower bound

The previous calculation is a special case of a norm-independent theorem.

Let H be any normed realization with a bounded nonzero functional ell_rho and scale
operators V_t satisfying

  ell_rho(V_t x)=e^{(1/2-rho)t}ell_rho(x).

For t>0,

  e^{(1/2-Re rho)t} ||ell_rho||
    = ||ell_rho o V_t||
    <= ||ell_rho|| ||V_t||.

Hence

  ||V_t|| >= e^{(1/2-Re rho)t}.

Applying the same argument to -t gives

  ||V_{-t}|| >= e^{(Re rho-1/2)t}.

Therefore any two-sided exponential growth exponent omega obeys

  boxed:
  omega >= |Re rho-1/2|.

Equivalently, if

  ||V_{+/-t}|| <= C e^{omega t},

then every retained zero satisfies

  |Re rho-1/2| <= omega.

If the growth is subexponential, omega can be taken arbitrarily small and RH follows.

This proves that no change of Hilbert norm can simultaneously:
- retain an off-line zero as a bounded exact Mellin character, and
- make the corresponding scale action subexponential.

A failed norm search therefore does not weaken the principal-series strategy; it shows
that the remaining estimate is genuinely arithmetic.

## 7. Quotient dynamics and the exact remaining issue

Because E is built from commuting dilations, E(D) is algebraically invariant under every
U_m and, on a suitable common analytic domain, under the continuous scale action.
Hence M is invariant whenever the action extends boundedly to H_{1/2}, and V_t induces a
quotient operator V_t^Q.

The quotient norm can be strictly smaller than the ambient norm. The zero functionals
give the unavoidable lower bound

  ||V_t^Q|| >=
  sup_rho exp[(1/2-Re rho)t]

for positive t, and the reflected bound for negative t.

Thus the quotient-growth exponent detects exactly how far the retained spectrum leaves
the principal-series axis.

What is NOT automatic is

  ||V_t^Q|| = e^{o(|t|)}

or contraction. Proving that would already exclude off-line zeros.

This is precisely the arithmetic Hilbertization theorem isolated in the E-map note,
now with an explicit universal retaining Hilbert space and quotient.

## 8. Relation to the existing Hardy leakage criterion

The v34 manuscript studies

  Theta_omega(z)
   = xi(1/2+omega+iz)/xi(1/2+omega-iz)

(up to the manuscript's fixed sign convention) and the lower Hardy block

  H_omega = Pi_- M_{Theta_omega}|_{H^2_+}.

It proves the exact zero-one law

  sup_{omega>0} ||H_omega||
    = 0 under RH,
    = 1 otherwise.

The symmetric strip quotient and the Hardy leakage picture are the same obstruction in
two coordinate systems:

- the strip quotient retains the off-axis evaluation functional;
- the shifted Hardy model sees the same zero as an anti-inner pole crossing;
- approaching the zero's real displacement makes a normalized reproducing kernel
  saturate the leakage norm.

Therefore an adaptive Hardy metric can localize an off-line zero with excellent finite
conditioning, but it cannot make the corresponding growth disappear. The growth lower
bound forces the difficulty to reappear as either semigroup expansion or anticausal
leakage.

## 9. Audit of the interrupted Work-session strategy

The Work-session strategy was correct up to its stopping point:

GOOD:
- weighted strip spaces give bounded complex evaluations;
- the quotient by the E-map range retains zero functionals;
- exact reproducing kernels make the topology explicit;
- adaptive Hardy charts remove artificial height and finite-section conditioning costs.

NO-GO:
- choosing a cleverer strip width or Fourier weight cannot by itself prove RH;
- any topology that retains an off-line exact character must exhibit exponential scale
  growth at least equal to its displacement from Re s=1/2;
- a norm that removes that growth without arithmetic input must necessarily erase or
  change the off-line functional.

So the correct next step is not another adaptive Fourier metric. It is to prove that the
POISSON-SEWN ARITHMETIC quotient has zero growth / contraction in the inherited physical
norm.

## 10. Meta-AI claims: what survives audit

Daniel supplied a Meta-AI synthesis involving the Riemann kernel Phi, finite Weil/CCM
ground states, and an empirical N~0.45 lambda^3 law.

Parts that are structurally correct and already supported by project sources:

1. The Shadow-Euler family
   s_{k,N}=kN/(k+N)
   is exactly a scalar Schur/parallel-sum stiffness, and the corresponding
   u_{k,N}=(s_{k,N}-1/2)^2 form an analytic uniqueness set for fixed k.
   This is proved in shadow_euler_identity_completed_v3.

2. The CCM finite Weil form has an exact rank-two boundary/pole channel and a
   rank-two displacement identity. The later boundary-channel reduction removes the
   need to assume a simple even ground state at finite cutoff; exactly one boundary
   channel remains open.

3. The existing Hardy affine atlas really does remove the fixed-chart dimension and
   precision costs: off-line poles generate their own adaptive model-space directions.

4. Ordinary L2 quotients erase the zero cokernel, while stronger real-trace Sobolev
   spaces retain only real traces. This matches the current E-map/strip picture.

Claims NOT accepted without an identified derivation/source:
- the specific asymptotic law N*(L)~e^L;
- the phrase 'doubly exponential asymptotically' for the optimal finite Fourier rank;
- the attribution of that law to a specific 'Theorem 3 in the Weil-positivity-in-
  compact-windows paper';
- the numerical overlap 0.999999954 and the quoted moment percentages, which were not
  found in the current persistent research records;
- the claim that Phi is already proved to be the finite-window ground state.

The exact safe statement is weaker:
a Riemann-kernel trial state whose transform is Xi is naturally near-radical under
finite truncation, but showing that nothing lies below it is a positivity/ground-state
theorem and cannot be inferred merely from nodelessness or high numerical overlap.

## 11. New smallest target after the reconstruction

We now have a concrete universal retaining quotient Q.

The RH-bearing statement can be written with no unspecified topology:

  HARDY-E-MAP QUOTIENT GROWTH THEOREM.
  For Q=H_{1/2}/closure(E(D)), prove that the induced centered scale evolution has
  two-sided subexponential norm growth.

Even weaker, using the functional equation:

  prove one common zero-independent quotient contraction that retains EVERY zero
  functional.

Either statement forces Re rho=1/2.

The advantage over the earlier formulation is substantial:
- zero retention is no longer hypothetical;
- the Hilbert space is explicit;
- the reproducing kernel is explicit;
- the zero-functional norm is explicit;
- the exact unavoidable growth caused by a hypothetical off-line zero is explicit.

The only remaining unknown is the arithmetic estimate on the quotient dynamics.
