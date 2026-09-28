# Supercharge causal split is not Hermite-Biehler: zero-independent falsifier

Date: 2026-09-28
Status: numerical falsification of a specific causal/Hermite-Biehler closure candidate using only the explicit positive Riemann kernel; no zero data.

Earlier work defined q(x)>0 on x>=0 by

  q(x)=2 e^(x/2) sum_{n>=1}(2 pi n^2 e^(2x)-1)e^(-pi n^2 e^(2x)),

with A(z)=int_0^infinity q(x)e^(izx)dx and

  E(z)=q(0)+(1/2+iz)A(z),

so that Xi(z)=(E(z)+E#(z))/2.

A tempting direct closure is to prove E or E# Hermite-Biehler. That would force Xi to have only real zeros. This candidate fails.

Using 60-digit quadrature, 25 theta terms, integration to x=8 (the tail is super-exponentially small), the ratio |E#(z)/E(z)| is:

  z=i       : 1.41489167049406167264445773859
  z=10+i    : 1.16218935493110964234489334213
  z=15+4i   : 0.935381385095398012355330022827
  z=20+2i   : 0.998280607933184525982986033869.

Thus E# dominates at some upper-half-plane points but E dominates at others. Neither orientation satisfies the global Hermite-Biehler inequality.

This kills only this PARTICULAR one-sided supercharge split. It does not kill de Branges/Hermite-Biehler as a framework: the correct split, if it exists, must include the global prime/Archimedean dynamical sewing rather than use the bare positive q half-line amplitude.

Methodological consequence: positivity and super-exponential decay of the causal kernel q are not enough. The missing HB phase is genuinely arithmetic/global.