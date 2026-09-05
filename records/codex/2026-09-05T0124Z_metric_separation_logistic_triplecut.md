# Codex/GPT research rotation — 2026-09-05 01:24Z

Codex/GPT track only. No Claude-owned context, records, files, branches, or notes were inspected.

## Prime-gas / Massieu geometry

Verify2 `ca10250a944fbccfce05d9ac9e662fad18b80bab` passed cold changed-Lean #897 and full Build #2043. The exact countable two-parameter Massieu/Fisher covariance quadratic form is therefore certified strictly positive on every nonzero tangent vector for all real beta and eta>0.

A follow-up wrapper was pushed to Verify2 as `dbc262b97e3e9869b25dfd5fd5e0edd5157537ab`. It adds:

- nonnegativity of the quadratic form for arbitrary tangent vectors;
- exact separation `q(a,b)=0 <-> a=0 and b=0`.

This is the pointwise positive-definite/Riemannian-metric endpoint. No uniform global lower eigenvalue bound is claimed. Build #2044 and changed-Lean #898 were still running at record time.

## Yang-Mills generalized-cut interface

Comparison of the generic nonzero-mu Ds=4 two-particle sewing with the existing Badger s23 triangle subtraction sharpens the blocker. The post-sewing coordinate `x=1-beta*cos(theta)` is exactly the unique angle-dependent adjacent tree propagator coordinate, and its Laurent powers encode propagator ancestry. But the Badger triangle coefficient depends on residue data of an additional uncut denominator `D_R` before the relevant tree factors are collapsed into the two-particle sewing. Therefore no universal post-hoc projector from the x-Laurent pole order alone can reconstruct box/triangle/bubble master coefficients.

The next honest calculation is a generic nonzero-mu triple-cut lift that retains the extra tree denominators separately, takes the relevant residues, performs branch-free root summation, and only then applies the existing T1/T2/T3 moment/subtraction machinery. FDH convention locking, D-dimensional gravity double copy, and higher-loop promotion remain downstream.

Scalar-box cut -> dispersion -> regulator closure remains certified at `J_epsilon(S,T) -> 1/6`.

## Gamma chamber / Wiener-Hopf

Discovery2 `5d46e8e3cad6d5df77880c7c02c8cbd595e84020` adds `experiments/gamma_chamber_logistic_symbolic_audit.py`. It certifies the exact algebraic/logarithmic content of the arbitrary-c Beta-to-logistic substitution:

`u=q/(1+q)`, `du/dy=q/(1+q)^2`, with `q=exp(y)`, and

`q/(1+q)^2 = 1/(4 cosh(y/2)^2)`.

The complex exponent bookkeeping is checked in logarithmic form to avoid illegitimate CAS branch simplifications. Thus the remaining Lean boundary for

`B(c+ix,c-ix)=4^(-c) integral_R sech(y/2)^(2c) exp(ixy) dy`

is measure-theoretic real-line change of variables, followed by Fourier uniqueness for `rho_c*rho_d=rho_(c+d)`. Verify2 already contains the global Beta/Gamma bridge and the integer chamber product hierarchy.

## Principal series / Weil

No RH promotion. Positive-real half-density structure, Delta=2s, critical-line unitarity, completed-zeta response, and local Gamma/Wiener-Hopf positivity remain valid. The global unresolved theorem is unconditional positivity of the genuine completed prime-plus-Archimedean Weil quadratic form on an adequate admissible class, together with the explicit-formula/function-class bridge to the finite spectral criterion.
