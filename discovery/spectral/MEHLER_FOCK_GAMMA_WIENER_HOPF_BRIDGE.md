# Mehler-Fock / Gamma / Wiener-Hopf spectral bridge

Codex/GPT discovery track, 2026-08-25.

Define the two exact spectral weights

\[
P(\lambda)=\frac{\pi\lambda}{\sinh(\pi\lambda)},
\qquad
m(\lambda)=\lambda\tanh(\pi\lambda).
\]

The first is the Wiener-Hopf weight already used in the chamber-convolution calculation; the second is the standard Mehler-Fock Plancherel density up to convention-dependent overall normalization.

For real \(\lambda\), the classical Gamma modulus identities are

\[
|\Gamma(1+i\lambda)|^2=\frac{\pi\lambda}{\sinh(\pi\lambda)},
\]

\[
|\Gamma(\tfrac12+i\lambda)|^2=\frac{\pi}{\cosh(\pi\lambda)},
\]

and, from \(\Gamma(1+i\lambda)=i\lambda\Gamma(i\lambda)\),

\[
|\Gamma(i\lambda)|^2=\frac{\pi}{\lambda\sinh(\pi\lambda)}
\quad (\lambda\ne0).
\]

Therefore

\[
\boxed{P(\lambda)=|\Gamma(1+i\lambda)|^2.}
\]

More importantly, the Mehler-Fock density is the exact adjacent-half-shift Gamma ratio

\[
\boxed{
 m(\lambda)
 =\frac{|\Gamma(\tfrac12+i\lambda)|^2}{|\Gamma(i\lambda)|^2}
}
\qquad (\lambda\ne0),
\]

with the continuous value \(m(0)=0\).

Multiplying the two weights gives the particularly simple bridge

\[
\boxed{
P(\lambda)m(\lambda)
=\frac{\pi\lambda^2}{\cosh(\pi\lambda)}
=\lambda^2|\Gamma(\tfrac12+i\lambda)|^2.
}
\]

Thus the Wiener-Hopf weight and Mehler-Fock measure are not unrelated spectral decorations: they are the integer-shift and half-integer-shift Gamma moduli of the same principal-series parameter. Their product removes the \(\sinh\) denominator entirely and leaves the half-shifted Plancherel factor.

This result is harmonic-analysis structure only. It does not by itself identify an amplitude measure, prove an RH statement, or establish a new physical spectrum.
