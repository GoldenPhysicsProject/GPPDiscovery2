# Completed-zeta logarithmic derivative on the critical line

Codex/GPT discovery track, 2026-08-25.

Let

\[
\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

be the completed Riemann zeta function away from its poles. It satisfies

\[
\Lambda(s)=\Lambda(1-s)
\]

and the reality symmetry

\[
\Lambda(\bar s)=\overline{\Lambda(s)}.
\]

Differentiating these identities where holomorphic gives

\[
\Lambda'(s)=-\Lambda'(1-s),
\qquad
\Lambda'(\bar s)=\overline{\Lambda'(s)}.
\]

On the critical line `s=1/2+it`,

\[
1-s=\bar s.
\]

Hence

\[
\Lambda'(s)
=-\Lambda'(\bar s)
=-\overline{\Lambda'(s)},
\]

so

\[
\boxed{\Re\Lambda'(1/2+it)=0.}
\]

The same two symmetries give

\[
\Lambda(s)=\Lambda(\bar s)=\overline{\Lambda(s)},
\]

therefore

\[
\boxed{\Im\Lambda(1/2+it)=0.}
\]

At every critical-line point where `Lambda(s) != 0`, division by the real nonzero value gives

\[
\boxed{
\Re\!\left(\frac{\Lambda'(1/2+it)}{\Lambda(1/2+it)}\right)=0.
}
\]

Thus the completed logarithmic response is purely imaginary on the unitary axis between zeros. This is an exact consequence of functional equation plus conjugation symmetry; it is not an RH statement and says nothing about whether all zeros lie on that axis.

Verify2 already contains the completed functional-equation derivative antisymmetry and critical-line reality of `Lambda`. The missing formal interface for direct promotion is the derivative-conjugation identity `Lambda'(conj s)=conj(Lambda'(s))`; it must be proved rather than assumed.
