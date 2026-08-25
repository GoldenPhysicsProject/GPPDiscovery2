# Exact thermodynamic/Fisher identities for the zeta prime gas

For inverse temperature \(\beta>1\), take

\[
Z(\beta)=\zeta(\beta),\qquad
\Psi(\beta)=\log Z(\beta),
\]

with canonical energy

\[
E(\beta)=-\Psi'(\beta)=-\frac{\zeta'(\beta)}{\zeta(\beta)}.
\]

The Fisher information / energy variance is

\[
g(\beta)=\Psi''(\beta)=\operatorname{Var}_\beta(\log n)>0.
\]

Then the canonical entropy

\[
S(\beta)=\Psi(\beta)+\beta E(\beta)
\]

obeys the exact differential law

\[
\boxed{S'(\beta)=-\beta g(\beta)<0.}
\]

Writing physical temperature as \(T=1/\beta\), the heat capacity is

\[
C(T)=\frac{dE}{dT}
=\beta^2g(\beta),
\]

so

\[
\boxed{C=\beta^2 g>0.}
\]

Thus the one-dimensional Fisher metric is exactly heat capacity divided by \(\beta^2\):

\[
\boxed{g=\frac{C}{\beta^2}.}
\]

The Fisher arclength element

\[
d\tau=\sqrt{g(\beta)}\,d\beta
\]

can therefore be written thermodynamically as

\[
\boxed{d\tau=\frac{\sqrt C}{\beta}\,d\beta=-\frac{\sqrt C}{T}\,dT.}
\]

Near the zeta pole \(\beta=1+\varepsilon\),

\[
\Psi(\beta)=-\log\varepsilon+O(\varepsilon),\qquad
E(\beta)=\varepsilon^{-1}+O(1),\qquad
g(\beta)=\varepsilon^{-2}+O(1),
\]

hence

\[
C(\beta)=\frac{\beta^2}{(\beta-1)^2}+O(1),
\qquad
S(\beta)=\frac{\beta}{\beta-1}-\log(\beta-1)+O(1).
\]

In particular, the pole is at infinite Fisher distance and has divergent positive heat capacity. These identities are exact consequences of canonical zeta thermodynamics and require no continuation into the critical strip.
