# RH as existence of a global density matrix: BPY cumulants as Renyi trace powers

Date: 2026-09-27
Status: exact equivalence, conditional spectral identification under RH. No external search used.

Let

F(z)=xi(1/2+z)/xi(1/2)

and, near z=0,

log F(z)=sum_{m>=1} kappa_{2m} z^(2m)/(2m)!.

Define the BPY cumulant moments

mu_n=(-1)^n kappa_{2n+2}/(2n+1)!,

and

R=mu_0/2=kappa_2/2 > 0.

The current RH program already proves that RH is equivalent to (mu_n) being a positive Stieltjes/Hamburger moment sequence, and equivalently to the intrinsic Hausdorff contraction representation.

## 1. Normalize the moment sequence as trace powers

Define, for m>=1,

tau_m := mu_{m-1}/(2 R^m).

Equivalently,

tau_m
=
(-1)^(m-1) kappa_{2m}
/
[2 (2m-1)! R^m].

Since mu_0=2R,

tau_1=1.

Under RH,

mu_n
=
2 sum_{gamma>0} m_gamma gamma^(-2n-2).

Also

R
=
sum_{gamma>0} m_gamma gamma^(-2).

Define

x_gamma := 1/(R gamma^2).

Then

sum_gamma m_gamma x_gamma=1,

and

boxed:
tau_m
=
sum_gamma m_gamma x_gamma^m.

Thus under RH the normalized BPY cumulants are exactly the power traces of a positive trace-one operator whose eigenvalues are x_gamma.

## 2. Density-matrix criterion for RH

The following are equivalent.

1. RH.

2. There exists a positive trace-class operator rho with

   rho >= 0,
   Tr rho = 1,

   such that for every integer m>=1,

   boxed:
   Tr(rho^m)
   =
   tau_m
   =
   mu_{m-1}/(2R^m).

3. There exists a positive trace-one operator rho such that

   boxed:
   F(z)=det(I+R z^2 rho).

Proof of (1)->(2):
under RH take rho diagonal with eigenvalues
x_gamma=(R gamma^2)^(-1), repeated with zero multiplicity m_gamma.
Their sum is one, and the displayed trace powers follow.

Proof of (2)->(1):
let rho have eigenvalues x_j>=0, counted with multiplicity. Since Tr rho=1, 0<=x_j<=1. Define the positive finite measure

nu = 2R sum_j x_j delta_{R x_j}.

Then

int lambda^n dnu(lambda)
=
2 R^(n+1) sum_j x_j^(n+1)
=
2R^(n+1) Tr rho^(n+1)
=
mu_n.

Hence (mu_n) is a Stieltjes moment sequence. By the already-proved BPY cumulant--Stieltjes equivalence, RH follows.

## 3. Fredholm determinant identity

Assume (2). Since rho is trace class,

log det(I+R z^2 rho)
=
sum_{m>=1}
(-1)^(m+1)
(R^m z^(2m)/m)
Tr rho^m

near z=0.

Insert the prescribed trace powers:

=
sum_{m>=1}
(-1)^(m+1)
z^(2m)
mu_{m-1}/(2m).

Using

mu_{m-1}
=
(-1)^(m-1) kappa_{2m}/(2m-1)!,

the signs cancel and

log det(I+R z^2 rho)
=
sum_{m>=1}
kappa_{2m} z^(2m)/(2m)!
=
log F(z).

Both sides are entire, so

boxed:
F(z)=det(I+R z^2 rho).

Conversely, such a positive trace-class determinant has zeros only at

z = +/- i / sqrt(R x_j),

so the determinant identity itself forces every zero of F onto the imaginary axis and therefore proves RH.

Thus

boxed:
RH
iff
F(z) is the fermionic Fredholm determinant of a positive density matrix after the intrinsic BPY scale R.

## 4. Spectral density matrix under RH

Under RH,

boxed:
spec(rho_RH)
=
{1/(R gamma^2): gamma>0},

with the Riemann-zero multiplicities.

This is not a zero-based construction for a proof; it is the spectral identification of the operator whose zero-independent construction is required.

The proof target is now very concrete:

boxed:
construct rho >= 0, Tr rho=1 directly from the BPY / adelic / modular data,
without using the zeros,
and prove its trace powers equal the normalized BPY cumulants.

That alone proves RH.

## 5. Renyi interpretation

For m>1 define

S_m(rho)
=
(1/(1-m)) log Tr(rho^m).

Then the RH target prescribes every Renyi entropy directly from the BPY cumulants:

boxed:
S_m
=
(1/(1-m))
log[
(-1)^(m-1) kappa_{2m}
/
(2(2m-1)! R^m)
].

So RH is equivalent to the statement that this cumulant-derived sequence is physically admissible as the Renyi spectrum of one density matrix.

The first conditions are the familiar density-matrix inequalities:
Tr rho^2 <= 1,
Tr rho^3 <= Tr rho^2, etc.,
but the full condition is stronger: all power traces must arise from one common positive spectrum.

## 6. Relation to the existing positive-contraction criterion

The intrinsic Hausdorff theorem gives

mu_n=R^n <Omega,C^n Omega>,

with 0<=C<=I and ||Omega||^2=mu_0=2R.

Let sigma be the spectral measure of C in Omega, so

mu_n/R^n = int x^n dsigma(x),
sigma([0,1])=2R.

Under RH its measure is

boxed:
dsigma(x)
=
2R sum_gamma m_gamma x_gamma delta_{x_gamma}(dx),

where x_gamma=(R gamma^2)^(-1).

Thus sigma/(2R) is the size-biased eigenvalue law of rho_RH. Its moments satisfy

int x^n dsigma(x)/(2R)
=
sum_gamma m_gamma x_gamma^(n+1)
=
Tr(rho_RH^(n+1)).

Equivalently,

boxed:
Tr(rho^m)
=
(1/(2R)) int x^(m-1) dsigma(x).

Important caveat: an arbitrary positive contraction representation does not by itself manufacture a trace-class density matrix. De-biasing sigma by x must recover the spectral counting measure, including the exact multiplicities in the Fredholm model. For the fixed BPY sequence that extra structure follows after the Stieltjes criterion has forced RH and the poles/residues of -H'/H identify the atoms. It should not be assumed in advance.

This is the precise bridge between the BPY contraction, the fermionic Fredholm target, and the global density-matrix spectrum.

## 7. Connection to the prime TFD program

Each prime already carries a local TFD density matrix. The rho required here is not their naive tensor product: its eigenvalues scale as inverse squared global resonance frequencies, and the zeros are collective modes.

The natural next construction target is therefore a **global sewn density operator** obtained after:
1. primitive m=1 scattering renormalization;
2. m=2 determinant/vacuum renormalization;
3. Archimedean SU(1,1) K0/K1 sewing;
4. physical no-ghost projection.

If that global reduced state has the BPY trace powers above, its Fredholm determinant is automatically F and RH is closed.

This formulation turns the RH proof problem into a positive trace-class state-construction problem rather than a direct zero-location argument.
