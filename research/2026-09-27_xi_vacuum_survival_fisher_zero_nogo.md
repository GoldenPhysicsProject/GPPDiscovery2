# Xi as an exact BPY vacuum survival amplitude, and a strong-log-concavity Fisher-zero no-go

Date: 2026-09-27
Status: exact zero-independent vacuum-amplitude representation plus an explicit counterexample killing a tempting naive closure. No RH claim and no zeta-zero data used in the counterexample.

## 1. Exact BPY vacuum survival amplitude

The existing BPY/Gaussian realization gives, for the positive random variable Q,

E[Q^(s/2)] = 2 xi(s).

On the critical line s=1/2+i t,

2 xi(1/2+i t)
=
E[ Q^(1/4) exp(i t (log Q)/2) ].

Work in the underlying probability Hilbert space L2(P). Define

psi = Q^(1/8),
H = (1/2) log Q

as a multiplication operator. H is self-adjoint on its natural domain and

||psi||_2^2
=
E[Q^(1/4)]
=
2 xi(1/2).

With the normalized vacuum vector

Omega = psi / ||psi||,

one obtains the exact identity

boxed:
xi(1/2+i t)/xi(1/2)
=
<Omega, exp(i t H) Omega>.

Thus the centered completed zeta function on the unitary line is literally a vacuum survival / Loschmidt amplitude, equivalently the characteristic function of the spectral measure of H in Omega.

This statement is unconditional and uses no zero locations.

## 2. Fisher-zero interpretation

Let a general nontrivial zero be

rho = 1/2 + beta + i gamma.

Write s=1/2+i t. Then rho corresponds to the complex time

boxed:
t = gamma - i beta.

Therefore:
- a critical-line zero beta=0 is a real-time zero of the vacuum survival amplitude;
- an off-critical zero beta!=0 is a complex-time Fisher zero.

RH can therefore be phrased exactly as:

boxed:
all nontrivial Fisher zeros of this BPY vacuum survival amplitude occur at real time.

This is a useful physical reformulation. It is NOT yet a proof because generic self-adjoint vacuum amplitudes can have complex Fisher zeros.

## 3. Cheap falsifier: self-adjointness and positive spectral measure are insufficient

Any self-adjoint H and normalized Omega produce a positive-definite characteristic function

phi(t)=<Omega,e^(itH)Omega>.

It is tempting to infer that positivity/unitarity should force the zeros of phi to real t. This is false.

An explicit smooth positive even spectral density is

q_{A,eps,b}(x)
=
C^(-1) exp(-A x^2/2)(1+eps cos(bx)),

with A>0, b>0, and 0<eps<1.

It is strictly positive because

1+eps cos(bx) >= 1-eps >0.

Its normalized characteristic function is exactly

boxed:
phi(t)
=
exp(-t^2/(2A))
[1+eps exp(-b^2/(2A)) cosh(bt/A)]
/
[1+eps exp(-b^2/(2A))].

The Gaussian prefactor never vanishes, so zeros satisfy

cosh(bt/A)
=
- exp(b^2/(2A))/eps.

Put

C0 = exp(b^2/(2A))/eps > 1.

Then the zeros are

boxed:
t =
(A/b)
[
 +/- arcosh(C0)
 + i pi(2k+1)
],
k in Z.

They are genuinely off the real axis and off the imaginary axis.

Therefore:

boxed:
positive spectral measure + self-adjoint survival Hamiltonian
does NOT force RH-type zero location.

This kills a naive Hilbert-Polya-by-characteristic-function argument.

## 4. Even arbitrarily strong uniform log-concavity is insufficient

The counterexample can be made uniformly strongly log-concave.

Let

q(x) proportional to exp(-A x^2/2)(1+eps cos bx).

Since

d^2/dx^2 log(1+eps cos bx)
=
-eps b^2 (cos bx + eps)/(1+eps cos bx)^2,

one has the simpler universal upper bound

d^2/dx^2 log(1+eps cos bx)
<=
eps b^2/(1-eps).

Hence

boxed:
(log q)''(x)
<=
-A + eps b^2/(1-eps).

By taking A arbitrarily large, the density is arbitrarily strongly log-concave while retaining the explicit off-axis Fisher zeros above.

For the concrete choice

A=12, eps=0.1, b=1,

the curvature bound is

(log q)'' <= -11.888888...,

yet the first zero pair includes

t approximately +/-36.421090 + 37.699112 i.

So even the project's strong unconditional log-concavity theorem for the Riemann/BPY density cannot by itself imply RH.

This is exactly the kind of attractive shortcut the heuristics require us to kill cheaply.

## 5. What survives: two different vacuum-spectrum statements

The counterexample forces a clean distinction.

### A. Exact BPY survival Hamiltonian

H=(1/2)log Q is an unconditional self-adjoint multiplication operator and

Xi(t):=xi(1/2+i t)/xi(1/2)
=
<Omega,e^(itH)Omega>.

Its Riemann zeros, if on the line, are real-time orthogonality nodes of one vacuum autocorrelation.

They are NOT eigenvalues of H.

### B. Conjectural collective Fredholm fluctuation operator

The much stronger RH-equivalent target is

F(z)=xi(1/2+z)/xi(1/2)
=
det(I+z^2 A),

with A>=0 trace class constructed without zero input.

If such A exists, its eigenvalues are inverse squared collective frequencies and positivity forces every zero to the imaginary z-axis.

This is not a generic characteristic-function property. It is a Lee-Yang/Fredholm-stability property of the completed vacuum.

Therefore the phrase "zeros are the vacuum spectrum" should mean the spectrum of the COLLECTIVE FLUCTUATION/FREDHOLM operator, while the BPY H gives the exact vacuum survival representation.

## 6. Physics interpretation

The arithmetic system now has two rigorous spectral roles:

1. microscopic arithmetic Hamiltonian / BPY survival dynamics;
2. collective fluctuation determinant after prime-Archimedean sewing.

That is physically natural. In ordinary many-body theory, the Hamiltonian generating microscopic time evolution and the Hessian/response operator whose determinant encodes collective resonances need not have the same spectrum.

The Riemann zeros should therefore be sought in the second object.

## 7. New search criterion

Any proposed RH closure based only on one or more of the following is now disqualified unless extra structure is supplied:

- self-adjointness of a survival Hamiltonian;
- positivity of its spectral measure;
- positive definiteness of the critical-line characteristic function;
- evenness;
- smoothness;
- arbitrarily strong log-concavity.

The missing property must be stronger and should resemble one of:
- positive Fredholm determinant structure;
- Lee-Yang/stable-entire-function structure;
- de Branges/Herglotz canonical-system structure;
- a positive Schur complement whose determinant is exactly F;
- a globally sewn density matrix with the exact BPY Renyi trace powers.

This detector should be applied to every future "vacuum stability implies RH" argument.
