# Completed-response confluent controls

Contributed by Daniel Toupin (Golden Physics Project), with Codex assistance.

Python 3 and mpmath==1.3.0. Run `python confluent_control.py` for two-precision Cauchy coefficient sampling, and `python confluent_witness.py` for independent real-axis Taylor differentiation and fixed rational witnesses. Results are written beside the scripts. The second calculation can take several minutes.

These test the full completed zeta logarithmic derivative and shifted F_theta controls, without a prime cutoff or zero table. At u=1, the fourth-dimensional matrix detects theta=1/4 and the fifth detects theta=1/10. Indices start at zero; highest derivatives used are 7 and 9. Conditioning by diag(16^i) is a sign-preserving congruence. All special-function signs are numerical, not interval-certified or Lean-certified. Passing tests for zeta does not prove RH.
