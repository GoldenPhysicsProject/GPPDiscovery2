# Exact finite Fejer lift for S27 (Codex)

This script verifies with Python Fraction arithmetic the exact cosine-polynomial
identity that produces Grok S27's prime-separable invisible-harmonic upper
construction. Run `python research/codex/s27_fejer_exact.py`.

For a prime with exactly one visible harmonic B(theta)=c cos(theta),
choose integer M>=2, K=c(M+1)/(2M), and shifted Fejer kernel
F_M(theta-pi)=1+2 sum_{k=1}^M (1-k/(M+1))(-1)^k cos(k theta).

The script checks coefficient by coefficient that h=B-K+K F_M
has neither a constant nor a first harmonic. Therefore h uses only
harmonics k>=2 and B-h=K(1-F_M)<=K, since
F_M=|sum_{j=0}^M(-exp(i theta))^j|^2/(M+1)>=0.

For e^L<=p<e^(2L), k>=2 implies k log p>=2L and is invisible
to any compact-window test f supported in (-L,L).

Together with the dual lower bound K>=c/2 (weight 1+cos(theta))
and unconditional PNT, this gives the exact asymptotic optimal
prime-separable envelope A_L=(2+o(1))e^L. The complete proof and
scope limitations are in private GPP-bridge Codex
`work/codex/2026-10-15_s27_h27_proof_fejér_optimal_separable_asymptotic.md`.

This is a finite rational algebra check, NOT a Lean theorem, RH or GRH proof.
Method origin: Grok S27 invisible lift; one-stroke basis: X. Zhu.

## Independent rational tail audit for L=1

Run `python research/codex/s27_rational_tails_L1.py` for exact Fraction
bounds on the complete even/odd Bessel and modified-Bessel tails at the
reported S27 L=1 run (T=300, K=262 per parity). This removes the script's
floating-point 400-term pole tail cutoff, using the exact decreasing
ratio of successive parity terms. It is a *partial* verifier audit,
not a proof of the finite Cholesky matrix or the whole Weil certificate.
