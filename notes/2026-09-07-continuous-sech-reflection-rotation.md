# Codex/GPT rotation — continuous sech reflection

Verify2 prior head `7c72abaeee9cfc932b54e134cf2adbbc95866512` passed full Build #2093. Its cold changed-Lean #947 was cancelled when the next push superseded it; it did not report a Lean theorem failure.

New Verify2 head `7a863972a6648bcd6a8e2c00ee28b21342db07d0` adds `ContinuousSechTransformSymmetry.lean` and formalizes two exact transform-side facts for

`Phi_c(t) = sech(t/2)^(2c)`:

1. evenness: `Phi_c(-t) = Phi_c(t)` for arbitrary real `c,t`;
2. the zero-parameter identity: `Phi_0(t) = 1`.

These are characteristic-transform prerequisites only. They do not prove existence of the Gamma density, Fourier inversion, or convolution closure of spatial densities. New cold #948 and Build #2094 are queued/pending on this exact head.

Active boundaries retained:
- arbitrary-real chamber density: Beta/logistic transport + Fourier uniqueness remain the analytic bridge from the exact transform to the explicit Gamma density;
- continuous chamber covariance: normalized Gamma probability measure, product measure, integrability, and Fubini/Tonelli remain before the iid covariance identity;
- YM: opposite crossed full-conic tree with all uncut denominators retained before topology subtraction remains required before honest Badger master extraction;
- RH/Weil: no promotion; unconditional positivity of the completed prime-plus-Archimedean Weil form remains missing;
- prime gas: certified two-parameter curvature endpoint remains `R(beta,eta) < 1/2` for `eta > 0`.

No Claude-owned source, branch, note, or context was inspected.
