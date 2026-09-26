# Prime TFD / modular-horizon dictionary

Date: 2026-09-26
Status: exact bosonic/KMS algebra from existing AFT prime data; physical identification with a spacetime horizon remains a conjectural intertwiner.

## 1. Prime oscillator at the critical arithmetic temperature

For one prime p, the AFT/number-gas oscillator has energy

\[
E_p=\log p,
\qquad
H_p=E_p N_p.
\]

At arithmetic inverse temperature beta=1,

\[
\rho_p=(1-e^{-E_p})e^{-E_p N_p}
      =(1-p^{-1})\sum_{a\ge0}p^{-a}|a\rangle\langle a|.
\]

This is exactly the critical Haar valuation law

\[
\Pr(v_p=a)=(1-p^{-1})p^{-a}.
\]

Thus the Haar law is literally the Gibbs density matrix of the prime oscillator at beta=1.

## 2. Canonical thermofield-double purification

The normalized purification is

\[
|\Omega_p\rangle
=
\sqrt{1-p^{-1}}
\sum_{a\ge0}p^{-a/2}|a\rangle_L|a\rangle_R.
\]

Write it in the standard two-mode-squeezed form

\[
|\Omega_p\rangle
=
\frac1{\cosh\kappa_p}
\sum_{a\ge0}(\tanh\kappa_p)^a|a,a\rangle.
\]

Then exactly

\[
\boxed{\tanh\kappa_p=p^{-1/2}=e^{-E_p/2}.}
\]

Therefore the finite-place hyperbolic coordinate already used in the arithmetic-shadow program,

\[
\kappa_p=\operatorname{artanh}(p^{-1/2}),
\]

is precisely the two-mode TFD squeezing parameter of the prime oscillator at beta=1.

The mean Bose occupation is

\[
\boxed{
\langle N_p\rangle
=
\sinh^2\kappa_p
=
\frac1{p-1}.
}
\]

The previously derived finite-place Casimir mass therefore satisfies

\[
\boxed{
\mu_p=2\sinh\kappa_p,
\qquad
\mu_p^2=4\sinh^2\kappa_p
       =4\langle N_p\rangle
       =\frac4{p-1}.
}
\]

Equivalently, in terms of the modular energy,

\[
\boxed{
\mu(E)^2=\frac4{e^E-1},
\qquad
E(\mu)=\log\!\left(1+\frac4{\mu^2}\right).
}
\]

So the local finite-place mass-square coordinate is exactly four times the Planck/Bose occupation of the corresponding arithmetic modular oscillator.

## 3. Modular Hamiltonian and principal-series flow

Up to the normalization constant, the one-sided modular Hamiltonian is

\[
K_p=(\log p)N_p.
\]

Its real modular flow acts on an occupation-changing operator by the phase

\[
e^{itK_p}: \quad a_p^\dagger\mapsto p^{it}a_p^\dagger.
\]

This is exactly the same arithmetic phase that appears in
- Bost-Connes time evolution;
- the AFT logarithmic Hamiltonian;
- the Mellin/principal-series character \(n^{it}\);
- the real-place factor of the adelic half-density sewing.

Hence

\[
\boxed{
\text{prime Gibbs energy}
=
\text{modular frequency}
=
\text{principal-series logarithmic frequency}.
}
\]

## 4. Why beta=1 and beta=2pi need not be different temperatures

The Bisognano-Wichmann / horizon convention writes the reduced vacuum state as

\[
\rho\propto e^{-2\pi K_{\rm boost}}.
\]

Modular theory instead calls

\[
H_{\rm mod}=2\pi K_{\rm boost}
\]

the modular Hamiltonian, so the same state is simply

\[
\rho\propto e^{-H_{\rm mod}},
\]

i.e. inverse temperature one relative to \(H_{\rm mod}\).

Therefore the arithmetic critical value beta=1 and the familiar boost-KMS value beta=2pi are compatible under the exact normalization target

\[
\boxed{
H_{\rm arith}
\stackrel{?}{=}
H_{\rm mod}
=
2\pi K_{\rm boost}.
}
\]

This does not yet identify the arithmetic and geometric modular generators; that is the missing horizon/AFT intertwiner. But it removes the apparent numerical mismatch between the arithmetic Hagedorn boundary and celestial/horizon KMS normalization.

## 5. Golden prime p=5

For p=5,

\[
\tanh\kappa_5=\frac1{\sqrt5},
\qquad
\sinh\kappa_5=\frac12.
\]

Hence

\[
\boxed{
\mu_5=2\sinh\kappa_5=1.
}
\]

And

\[
\kappa_5=\operatorname{arsinh}(1/2)=\log\varphi.
\]

Thus the golden point is the unique prime-local TFD channel whose normalized Casimir mass is exactly one:

\[
\boxed{
p=5
\iff
\mu_p=1
\iff
\kappa_p=\log\varphi.
}
\]

Combined with the celestial continuation already derived,

\[
i\lambda_p=\sqrt p,
\]

this gives

\[
p=5
\iff
i\lambda=\sqrt5
\iff
s=\varphi
\iff
\mu=1
\iff
\kappa=\log\varphi.
\]

This is one exact object seen in five coordinate systems.

## 6. Global arithmetic TFD and the Hagedorn/no-escape boundary

For beta>1 the global number-gas TFD is

\[
|\Psi_\beta\rangle
=
\bigotimes_p
\sqrt{1-p^{-\beta}}
\sum_{a\ge0}p^{-\beta a/2}|a,a\rangle_p,
\]

with normalization controlled by

\[
Z(\beta)=\prod_p(1-p^{-\beta})^{-1}=\zeta(\beta).
\]

As beta approaches 1 from above,

\[
\prod_p(1-p^{-1})=0,
\]

and the normalized global state escapes the ordinary finite-energy Fock sector even though every finite set of prime marginals remains perfectly regular.

This is exactly the singular boundary already encountered in the arithmetic-shadow ghost/no-escape problem.

The new interpretation is:

> the critical Haar ghost is the local marginal data of an infinite arithmetic thermofield-double state at the modular/Hagedorn boundary.

Any RH proof through AFT must therefore control the global completion of this infinitely entangled product state, not the individual prime channels.

## 7. Entanglement entropy

The prime-p reduced entropy is exactly

\[
S_p
=
-\log(1-p^{-1})
+
\frac{\log p}{p-1}.
\]

The second term dominates the global divergence. The critical product state therefore has divergent total left-right entanglement, just as continuum horizon entanglement is UV divergent.

This is structural evidence for the horizon analogy, not an equality of regulators or areas.

## 8. Unified operator dictionary

The present exact local chain is

\[
\boxed{
p
\to
E_p=\log p
\to
e^{-E_p/2}=p^{-1/2}
\to
\kappa_p=\operatorname{artanh}(p^{-1/2})
\to
\langle N_p\rangle=\sinh^2\kappa_p
\to
\mu_p^2=4\langle N_p\rangle.
}
\]

At the same time

\[
p^{-it}=e^{-itE_p}
\]

is the Lorentzian/principal-series modular phase.

Thus the finite-place mass coordinate and the real-place unitary phase are the Euclidean and Lorentzian faces of one prime modular mode.

## 9. Physics target

The strongest unification target is now to construct a single adelic modular standard form in which

1. the finite-place reduced state is the Haar geometric law;
2. the modular Hamiltonian has spectrum \(\log n\);
3. modular real-time is the principal-series/Mellin flow;
4. modular conjugation realizes the arithmetic shadow involution;
5. the Archimedean sector supplies the Bisognano-Wichmann/celestial normalization;
6. OS reconstruction gives the physical real-place Hilbert space;
7. the AFT no-ghost quotient eliminates the bad Hardy/Nyman sector.

If this exists, the number-gas, p-adic CFT, celestial principal series, horizon thermality, and RH no-escape problem are pieces of one modular field theory rather than separate analogies.
