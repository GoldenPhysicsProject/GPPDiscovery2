# Fixed-shift inner-scattering no-go and the zero-resolution condition

**GPPDiscovery2 / Codex research note, 2026-11-15.** Research-stage. This is neither an RH proof nor a counterexample to RH. The control function is an explicit polynomial, not an Euler product. All proofs below are elementary analytic arguments, not yet formalized in Lean.

## Context and the question

GPPVerify proves the one-dimensional Mellin character correspondence (s = Δ₁) in PasterskiShaoDictionary.lean and the implication normalizable_1d_implies_principal in PasterskiShaoNormalizability.lean. The arithmetic zero-to-state claim XiZeroIsNormalizable1dState remains open. ShadowTheory.lean similarly isolates the open ARP / reflection-positivity hypothesis. The November 15 bridge discussion has nominated an all-window arithmetic-to-Klein–Gordon (AKG) pairing after the OddFace(0.5) work.

A possible SPEC/global-scattering route is to show that a ratio of reflected spectral functions is unitary on the real spectral axis, analytic and contractive in the physical upper half-plane. We prove a limitation: **any finite collection of positive spectral regulators permits all these scattering properties while its underlying function has an off-critical quartet**. To detect every off-axis zero by this method requires arithmetic-specific input or a regulator sequence approaching zero.

## Setup

Use z = −i(s−1/2), hence s = 1/2 + iz; the critical line in s corresponds to the real z-axis. A real-entire function means a nonzero entire F with F(conj z) = conj F(z). For a>0 define

\[
E_a(z)=F(z+ia),\qquad E_a^\#(z)=\overline{E_a(\bar z)}=F(z-ia),\qquad
S_a(z)=\frac{F(z-ia)}{F(z+ia)}.
\]

For any real x where the denominator is nonzero, |S_a(x)| = 1 automatically. This boundary unitarity holds regardless of whether F has off-real zeros.

## Theorem 1 (proved): fixed-shift inner scattering can conceal off-axis quartets

Fix a>0, gamma>0 and 0<beta<a. Define the even real polynomial

\[
F_{\gamma,\beta}(z)=[(z-\gamma)^2+\beta^2][(z+\gamma)^2+\beta^2].
\]

Its zeros are z=±gamma±i beta. The arithmetic-variable polynomial G(s)=F_{\gamma,\beta}(−i(s−1/2)) obeys G(1−s)=G(s) and G(conj s)=conj G(s), but has zeros

\[
s=\tfrac12\pm\beta\pm i\gamma,
\]

all strictly off the critical line. Nevertheless the scattering ratio factors exactly as

\[
\boxed{S_a(z)=
\prod_{\epsilon=\pm1}\prod_{\eta=\pm1}
\frac{z-[\epsilon\gamma+i(a+\eta\beta)]}
{z-[\epsilon\gamma-i(a+\eta\beta)]}.}
\]

Both a−beta and a+beta are positive. Each denominator zero lies strictly in the lower half-plane. For Im z>0 and w=u+iv with v>0,

\[
|z-w|^2=(\mathrm{Re}z-u)^2+(\mathrm{Im}z-v)^2
<
(\mathrm{Re}z-u)^2+(\mathrm{Im}z+v)^2
=|z-\bar w|^2.
\]

Therefore every factor, and hence S_a, has modulus strictly below one in the upper half-plane and modulus exactly one on the real axis. **S_a is a finite Blaschke product, an analytic rational inner function, even though G has four off-line zeros.**

**Finite-family corollary (proved).** Given any finite positive shifts a_1,...,a_m, take 0<beta<min a_j. The very same off-line G gives inner functions S_{a_j} for every shift in the finite family. Thus no finite list of fixed-regulator real-axis unitarity, upper-half-plane analyticity or Schur contractivity tests can force the critical line for general reflection-symmetric real-entire data.

**Sharp detection threshold for this control.** If 0<a<beta then z=gamma+i(beta−a) is a genuine upper-half-plane pole of S_a: the denominator vanishes there but the numerator does not. At a=beta a boundary zero/cancellation occurs; the strict zero-free statement for E_a is preferable at that endpoint.

## Theorem 2 (proved): vanishing-shift pole-freeness resolves all zeros

Let F be any nonzero real-entire function. Suppose there is a sequence a_n>0 tending to zero such that each meromorphic ratio

\[
S_{a_n}(z)=F(z-ia_n)/F(z+ia_n)
\]

extends holomorphically to the entire open upper half-plane. Then **every zero of F is real**.

**Proof.** Suppose F(zeta)=0 for Im zeta=beta>0. Isolatedness of zeros gives delta>0 such that F has no other zeros in 0<|z-zeta|<delta. Choose n so that 0<a_n<min(beta,delta/2). Then z_n=zeta−ia_n is in the upper half-plane. Its denominator is F(zeta)=0 while its numerator is F(zeta−2ia_n)≠0. Thus S_{a_n} has a genuine pole at z_n, a contradiction. Any lower-half-plane zero produces an upper-half-plane conjugate zero because F is real-entire. Hence all zeros are real. QED.

For F(z)=Xi(z)=xi(1/2+iz), all zeros real means RH. Theorem 2 is a **conditional equivalent spectral target**, not an arithmetic proof of its premise. Any independent proof that the Xi ratios are pole-free for a specified null sequence would prove RH.

Caution: for general entire F, holomorphy of each S_a does not alone imply boundedness/contractivity; the theorem only assumes holomorphy. Theorem 1 proves both holomorphy and contractivity for its explicit control.

## Reproducible experiment

Run:

    python experiments/fixed_shift_inner_counterexample.py

Standard-library-only; no zero dataset, no mpmath. Defaults gamma=14, beta=1/8, a=1/4. It checks the exact Blaschke factorization on a grid, boundary modulus one and upper-half-plane contraction, and finds a genuine pole at z=14+0.0625i upon reducing a to beta/2.

Sample outputs: max Blaschke factorization residual 5.56e−16, maximum boundary modulus deviation 1.12e−16, sampled upper-half-plane modulus maximum 0.9997961, smaller-shift pole denominator residual 0. These grid checks illustrate the proof, not replace it.

## Consequences for SPEC / AKG and the s = Delta program

1. Real-axis unitarity of a shifted completed amplitude is automatic from conjugation, hence by itself carries no critical-line information.
2. Even full analytic, contractive, inner scattering at **one or finitely many fixed shifts** misses arbitrarily close off-axis quartets. The finite-family theorem is stronger than a boundary-unitarity objection.
3. Pole-freeness of the scattering ratios for a sequence of shifts tending to zero would eliminate all off-axis zeros; it is RH-hard for Xi. It may be a precise target for a regulator-uniform arithmetic argument, but cannot be assumed in the guise of physicality.
4. In the Lean program, the proved character identity s=Δ₁ plus the proved normalizability selector must not be promoted to XiZeroIsNormalizable1dState through a finite-shift scattering hypothesis. A successful AKG or WeilIsGram map must provide arithmetic-specific positivity or a zero-resolving analytic bridge.
5. Keep F_{gamma,beta} as a no-go regression control for SPEC / scattering-based assertions. Because it has no Euler product, a correct arithmetic proof may reject the control; the hypothesis performing that rejection must be named and proved.

**Status:** Theorem 1 and Theorem 2 proved on paper by direct factorization and isolated-zero argument. Computation reproduced with Python. No Lean build has been run; no claim of an RH proof or of SPEC being discharged.