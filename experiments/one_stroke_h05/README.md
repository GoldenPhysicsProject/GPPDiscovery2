# Even Weil h=1/2: one-stroke Legendre numerical candidate

Daniel Toupin / Golden Physics Project / Codex, October 15 2026.
Independent SciPy floating assembly inspired by **Marcus Chuk, arXiv:2608.24827** (Sept 2026). This is an **experimental reproduction**, not an original one-stroke method, not an interval certificate and not a proof of RH/GRH.

Use `python one_stroke_h05.py --h .5 --T 35 --modes 40 --quad 1200`. At h=1/2, n=2 is the only active prime power; n=3 appears only for h>(log 3)/2. The tested lower envelope is `beta = log(T/(2*pi))-2 log(2)/sqrt(2)-1/T`. The even and odd blocks use orthonormal Legendre support basis, spherical-Bessel Fourier transforms, digamma real-place multiplier, and full signed cosh/sinh poles. Complex tests reduce to parity blocks only after establishing the actual continuum quadratic identity and Hermitian form.

Executed local float result at T=35, 40 modes per parity, 1200 Gauss nodes:
- beta=0.708641423040092
- smallest even eigenvalues: 4.77394757e-7, 0.0102761359
- smallest odd eigenvalues: 8.70578646e-5, 0.269457168
- first omitted even spherical-Bessel amplitude upper design estimate: 4.01146e-44
- finite-frequency omitted trace design estimate: 1.793e-86

The results remain positive under float Gauss quadrature grids of 400–1600 points. These are not rigorous interval comparisons and numerical condition numbers for such small eigenvalues matter. **To certify**: reproduce the finite symmetric block entries with Arb-rounded digamma, quadrature and spherical Bessel/Legendre, show exact outward-rounded Cholesky/positive-definiteness; establish the analytic high-frequency multiplier envelope on the full tail; bound all finite-to-infinite cross terms and the omitted pole coefficient as operators; prove the quadratic normalization/smooth-to-L2 extension. A tempting `|Psi-beta| <=100` on [0,35] is not yet certified.

This is most valuable as an independent check of the published h=0.8 finite-window result. The all-h prime–Archimedean signed inequality, and RH/GRH, remain unproved.
