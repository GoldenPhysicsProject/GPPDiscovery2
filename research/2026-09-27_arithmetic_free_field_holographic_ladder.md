# The arithmetic free field: prime Fock space -> number circle -> BPY four-field vacuum -> celestial Plancherel

Date: 2026-09-27
Status: exact operator/probability identities assembled into one holographic ladder. No RH claim. Some scalar thermal-circle/BPY identities were already present in earlier GPP notes; the new point here is the explicit prime-Fock/unitary and Gaussian-second-quantization synthesis.

## 1. Arithmetic one-particle Hilbert space

Let H_ar=ell2(N_{>=1}) with basis e_n and arithmetic Hamiltonian

H e_n=(log n)e_n.

Unique factorization gives the canonical unitary

U:H_ar -> tensor_p ell2(N_0),
U e_n = tensor_p e_{nu_p(n)},

under which

boxed:
U H U^{-1}=sum_p(log p)N_p.

Therefore

boxed:
e^{-H} e_n=n^{-1}e_n,
qquad
e^{-2H}e_n=n^{-2}e_n.

On the geometric number-circle realization, e_n(theta)=exp(in theta) and |D|e_n=n e_n, so

boxed:
H=log|D|,
qquad
e^{-2H}=|D|^{-2}=Delta^{-1}

on the positive-frequency sector.

Thus the inverse circle Laplacian is exactly the exponential of minus twice the free prime-occupation Hamiltonian.

## 2. The BPY variable is the squared norm of a Gaussian field over the arithmetic Hilbert space

Let G_a, a=1,...,4, be independent standard real cylindrical Gaussian vectors on H_ar. Since e^{-H} is Hilbert-Schmidt,

Y_a=(2pi)^(-1/2)e^{-H}G_a

is an honest H_ar-valued Gaussian vector.

Its squared radius is

boxed:
Q=sum_{a=1}^4 ||Y_a||^2
=
(1/(2pi)) sum_{n>=1}sum_{a=1}^4 G_{n,a}^2/n^2.

This is exactly the BPY variable used in the RH programme.

Equivalently, under the number-circle/interval realization it is the L2 radial norm of four independent Brownian-bridge/free scalar components:

Q=(pi/2)sum_a int_0^1 B_a(u)^2 du.

So the completed-zeta probability model is literally a four-component Gaussian field built on the same integer mode Hilbert space that unique factorization identifies with prime occupation space.

## 3. Exact Gaussian determinant

For a positive trace-class covariance C=(2pi)^(-1)e^{-2H}, the four real Gaussian components give

E exp(-tQ)
=
det(I+2tC)^(-4/2).

Hence

boxed:
E exp(-tQ)
=
det(I+(t/pi)e^{-2H})^{-2}
=
product_{n>=1}(1+t/(pi n^2))^{-2}.

Using the Euler product for sinh,

boxed:
E exp(-tQ)
=
( sqrt(pi t)/sinh sqrt(pi t) )^2.

No Riemann zeros enter.

## 4. Exact celestial Plancherel square

Let

P(lambda)=pi lambda/sinh(pi lambda).

At t=pi lambda^2,

sqrt(pi t)=pi|lambda|,

so

boxed:
E exp(-pi lambda^2 Q)
=
P(lambda)^2.

Therefore the square of the celestial/Archimedean principal-series weight is exactly the Gaussian vacuum partition function of the four-component arithmetic free field.

Equivalently,

boxed:
P(lambda)
=
det(I+lambda^2 e^{-2H})^{-1}

for one two-real-component/one-complex Gaussian pair, while the four-component BPY field gives its square.

This is the cleanest exact bridge currently known between:
- prime occupation energies log p;
- the integer/number-circle spectrum n;
- the BPY four-field vacuum;
- the celestial Plancherel factor.

## 5. Xi is the Mellin radial observable of the same field

The BPY identity gives, for every complex s after analytic continuation,

boxed:
E[Q^{s/2}]=2 xi(s).

At the critical tilt

dP_{1/2}=Q^{1/4}dP_G/[2xi(1/2)],

with X=(1/2)log Q,

boxed:
xi(1/2+z)/xi(1/2)
=
E_{1/2}[e^{zX}].

Thus one and the same arithmetic Gaussian field has:
- a Laplace transform equal to the square of the celestial Plancherel weight;
- a Mellin transform equal to completed zeta.

This is not a proof of RH because Laplace positivity does not force the Mellin Fisher zeros onto the unitary axis.

## 6. Why the four components are physically suggestive but not yet a theorem of spacetime dimension

The exact Euclidean field has four real target components. It may be viewed as a random worldline/bridge

B:[0,1]->R^4

with Gaussian action and radial observable Q proportional to int |B|^2.

After Lorentzian continuation of the target metric, projectivized null directions in R^{3,1} form CP1 ~= S2, the celestial sphere. This makes the appearance of four BPY components striking in the proposed RP1 -> CP1 holographic ladder.

What is proved:
- exactly four Gaussian components occur in this BPY realization of xi;
- their radial Laplace determinant is P(lambda)^2;
- CP1 is the null-direction sphere of 3+1 Lorentzian geometry.

What is not proved:
- that the BPY component count uniquely derives physical spacetime dimension;
- that Wick rotating this auxiliary Gaussian target produces Einstein gravity.

This should be treated as a sharp structural clue and a target for a rigidity theorem.

## 7. A Fock-of-Fock interpretation

The one-particle Hilbert space of the Gaussian BPY field is itself the prime-occupation Fock space:

H_ar ~= tensor_p ell2(N_0).

The BPY Gaussian probability space is therefore the Gaussian/second-quantized field built over an arithmetic Fock space.

Schematic exact hierarchy:

prime generators
 -> prime occupation Fock H_ar
 -> number-circle geometry via H=log|D|
 -> four-component Gaussian field over H_ar
 -> radial determinant P(lambda)^2
 -> Mellin radial response xi(s).

This gives a mathematically concrete version of a "chain of holograms": successive descriptions reorganize the same spectrum rather than introducing unrelated structures.

## 8. Spectral-rigidity observation for the number circle

Exponentiating the arithmetic Hamiltonian gives the positive spectrum

e^{2H}: n -> n^2.

Any connected compact one-dimensional Riemannian manifold is a circle, and its Laplacian spectrum fixes its circumference up to the usual scale normalization. Thus once one asks for a connected compact one-dimensional local geometry whose positive Laplacian modes realize the spectrum n^2, the circle is forced up to scale.

This is a modest but literal rigidity statement behind the number-circle picture.

## 9. Why this still does not close RH

The free positive operator e^{-2H} has eigenvalues n^{-2}; its Fredholm determinant is sinh(pi z)/(pi z), not xi(1/2+z).

The target RH operator A must have very different normalized trace invariants. Earlier GPP work gives

Tr A^2/(Tr A)^2 ~=0.06963238,

whereas the normalized circle inverse Laplacian gives 2/5.

Therefore the Riemann zeros cannot be the free circle/BPY covariance spectrum. They must be collective modes generated after the Mellin tilt and prime-Archimedean completion.

The exact bridge above tells us where the collective operator must come from: not a new Hilbert space, but a nontrivial response/Hessian/Schur operator of this already-identified arithmetic Gaussian vacuum.
