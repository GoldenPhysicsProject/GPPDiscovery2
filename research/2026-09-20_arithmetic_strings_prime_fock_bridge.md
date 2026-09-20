# Arithmetic strings: exact prime-Fock correspondence and its limits

Date: 2026-09-20

Motivation: compare the active RH/prime-gas program with the structural claim in
Why String Theory Works v4 that the reusable content of string theory is 2d CFT + multiplicative
Haar/Mellin structure rather than literal spatial strings.

No claim is made that integers are literal physical strings.

## 1. Unique factorization is a bosonic occupation basis

Let P be the set of primes and let

K = { k:P->N_0 : k_p=0 for all but finitely many p }.

Unique factorization gives a canonical bijection

K  <->  N_{>=1},

k |-> n(k)=prod_p p^{k_p}.

Thus the Hilbert space l2(N_{>=1}) is canonically the bosonic Fock occupation Hilbert space over
one-particle prime modes:

|n> = tensor_p |k_p>.

This is stronger than a metaphor. It is an exact basis identification.

## 2. Arithmetic length/energy

Assign primitive mode length

ell_p=log p.

Then the total occupation length is

L(k)=sum_p k_p ell_p
    =log n(k).

The number operator N with N|n>=n|n> is the exponential of the additive length generator:

N=e^L.

Hence for beta>1,

Tr exp(-beta L)
=
sum_n exp(-beta log n)
=
sum_n n^-beta
=
zeta(beta).

Prime by prime,

Z_p(beta)
=
sum_{k>=0} exp(-beta k log p)
=
1/(1-p^-beta),

so the Euler product is exactly the second-quantized bosonic partition function.

## 3. Comparison with the ordinary free-string oscillator basis

A free bosonic string Fock basis is likewise described by finite occupation data

(N_m)_{m>=1},

with oscillator level

Level=sum_m m N_m.

The arithmetic system has the same occupation algebra but a different dispersion relation:

string mode energy: m,
arithmetic prime-mode energy: log p.

Therefore the two Fock spaces are abstractly of the same bosonic occupation type, but their
spectral Hamiltonians are not canonically the same.

The literal statement "an integer is a string" is too strong.

A precise statement is:

integers are multiplicative bosonic Fock states whose primitive modes are primes and whose
additive spectral lengths are log p.

Equivalently, they are unordered finite words/multisets of primitive prime letters.

## 4. Graded/fermionic arithmetic strings

If each prime may be occupied only 0 or 1 times, the basis consists of squarefree integers and

Z_F(beta)
=
prod_p(1+p^-beta)
=
zeta(beta)/zeta(2 beta).

If one takes the fermion-parity supertrace, the local factor is 1-p^-beta and

Z_super(beta)
=
prod_p(1-p^-beta)
=
1/zeta(beta).

Thus the bosonic, fermionic, and graded-fermionic arithmetic state spaces are three exact
statistics on the same primitive prime modes.

## 5. T-duality / shadow / arithmetic orientation

Why String Theory Works v4 isolates the multiplicative involution

t -> 1/t

as the common abstract source of worldsheet T-duality and celestial shadow.

Writing t=e^ell makes this

ell -> -ell.

The arithmetic Haar carrier uses exactly the same logarithmic coordinate u=log r, with scale
inversion r->1/r acting as u->-u. The self-adjoint Haar generator A=-i d/du is odd under this
reflection:

R A R=-A.

Thus the string-theory T-duality coordinate, celestial shadow coordinate, and arithmetic Haar
orientation are exact realizations of the same multiplicative inversion algebra on different
representations.

This does not identify the underlying physical systems.

## 6. Bilateral arithmetic completion and momentum/winding analogy

The ordinary integer Fock sector uses only positive prime occupations. The idelic/shadow
completion naturally supplies reciprocal scales as well. Formally a bilateral local exponent k in Z
has

p^k <-> p^{-k}

under inversion.

This is structurally analogous to a momentum/winding pair exchanged by T-duality, but there is
not yet a theorem identifying the arithmetic exponent k with a physical winding number.

The correct object to investigate is therefore not an ordered string in spacetime, but a
multiplicative two-sided oscillator channel whose orientation reversal is exponent inversion.

## 7. q=5 and the self-dual transfer channel

For a local parameter q the active RH program has

a_q=q^-1/2=tanh kappa_q,
r_q=e^-2kappa_q,
mu_q=2 sinh kappa_q,
u_q=s_q(s_q-1)=(q-1)/4,
mu_q^2=1/u_q.

At q=5,

u_5=mu_5^2=1,
kappa_5=log phi,
r_5=phi^-2.

Thus q=5 is a self-dual point of the arithmetic Casimir/mass reciprocal map u<->1/u.

This resembles the role of the self-dual radius in T-duality only at the level of the normalized
multiplicative transfer parameter. No physical string-radius identification is claimed.

## 8. Possible string/RH use

Why String Theory Works v4 interprets the Regge tower as off-principal-series spectral content,
with the principal series as the universal unitary/massless sector.

The RH program independently singles out the principal series / half-density line as the locus where
functional shadow equals Hilbert adjoint.

A useful research question is therefore:

Can the bad-zero Hardy defect be represented as an arithmetic off-principal-series excitation of
the prime-Fock/Mellin system, while the completed physical boundary condition projects onto the
principal-series sector?

This is not yet a proof mechanism. The danger is circularity: simply declaring off-principal-series
modes unphysical would assume the needed Hilbert admissibility. The value of the string comparison
is to suggest a concrete representation-theoretic completion, not to replace the RH theorem.
