# Codex h=1/2 even-sector PL-DC extension experiment

October 15, 2026. Reuses Grok's S26 multiplier from
`GoldenPhysicsProject/GPPDiscovery5/s26/s26_mult_h05_pl16L6.json` unchanged.
The mathematical target is Astra's positive-pole sufficient criterion

`C * (beta_r + lambda^2/2) < 1`.

For S26 the DC coefficient is `C = 7.376444421930428`, so the
necessary condition on any successful residual design is
`abs(lambda) < sqrt(2/C) = 0.5207046554215385`.
At lambda=0.5 the allowed beta is less than `0.0105666690888316`.

`codex_design.py` minimizes **truncated** weighted Fourier residual energy
plus the positive-pole coordinate cost for an even, piecewise-linear
exterior, using a dense float mesh around the known narrow dip near
frequency 126.06. The result is a floating-point **optimistic** feasibility
screen ONLY. In particular, it does NOT bound the omitted frequency tail,
certify an interval enclosure, or prove positivity. A positive optimistic
margin is only a candidate for Arb; a negative margin is only a failure
within this chosen finite-dimensional exterior family.

To run it in a Python environment with NumPy and SciPy, place the unchanged
Grok S26 JSON beside the script and run:

```sh
python codex_design.py --input s26_mult_h05_pl16L6.json \
  --output even_h05_float_design.json --N 96 --H 15 --X 500
```

Next: optimize alternative H, N and Gram regularization; independently
validate the basis transforms; round candidate coefficients rationally;
port S26's general PL-W frequency symbol into Astra's even Arb verifier;
use the symmetric reciprocal-Taylor enclosure Astra described to avoid
first-order cell losses. Do not present the float candidate as a theorem.

Authors/contributions: Daniel Toupin (programme), Astra (positive-pole
lemma/old even verifier), Grok (S26 multiplier/odd certificate), Codex
(this independent numerical design continuation).
