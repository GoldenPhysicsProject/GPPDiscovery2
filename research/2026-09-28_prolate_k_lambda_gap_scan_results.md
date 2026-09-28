# Literal CCM prolate k_lambda vacuum-gap scan

Implements the Connes--Consani--Moscovici educated guess k_lambda=E(h_lambda) using a Legendre-Galerkin prolate solver. No zeta-zero data used.

| c | overlap | 1-overlap^2 | eps/gap | residual/dist2 | k odd fraction | lam1 | even gap |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 1.0000e+00 | 3.1952e-07 | 1.8969e-06 | 4.9955e-02 | 4.7200e-09 | 5.0235e-08 | 1.3678e-03 |
| 5 | 1.0000e+00 | 8.5129e-08 | 2.7582e-07 | 2.5487e+02 | 1.4304e-18 | 9.0681e-18 | 5.2974e-12 |
| 7 | 1.0000e+00 | 1.7920e-08 | 1.3961e-07 | 2.1475e+06 | 4.8226e-29 | 9.7904e-28 | 2.4617e-21 |
| 11 | 9.9998e-01 | 3.5469e-05 | 1.3529e+00 | 6.1507e+17 | 5.0243e-54 | 2.2356e-42 | 5.9504e-36 |
| 13 | 9.9994e-01 | 1.2695e-04 | 1.2771e+06 | 2.1824e+16 | 5.2434e-65 | 7.6821e-47 | 1.8031e-40 |
| 17 | 9.9974e-01 | 5.2976e-04 | 7.8633e+13 | 6.7918e+15 | 2.5692e-68 | 7.8057e-53 | 1.9779e-46 |

Interpretation: compare directly against the naive truncated-Phi control. The relevant quantity for vacuum rigidity is eps/gap, not overlap alone.
