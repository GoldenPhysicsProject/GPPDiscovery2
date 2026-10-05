# Euler–Archimedean collision decomposition of the semilocal Weil form

Date: 2026-10-05

Status: exact finite/continuum algebra plus zero-free numerical verification. Not a proof of RH.

This continues RH_ARROW_ROADMAP_EXECUTION_2026-10-05.md. The point is to put the pole, Archimedean, and prime-power pieces into one collision-energy normal form and isolate exactly which term still carries RH-strength information.

## 1. Semilocal source notation

Fix L>0. For 0<=y<=L define

\[
\psi_y(s)=\frac1\pi\sin\!\left(2\pi\left(1-\frac yL\right)s\right).
\]

Its Hermite–Loewner matrix on the integer grid is the CCM kernel

\[
q(y)=L_{\psi_y}.
\]

At y=0,

\[
\psi_0(s)=\frac{\sin(2\pi s)}{\pi}=2h(s),
\]

and since L_h=I,

\[
\boxed{q(0)=2I.}
\]

Define the collision defect

\[
\boxed{D_y:=2I-q(y)=L_{\psi_0-\psi_y}.}
\]

## 2. D_y is an honest positive translation defect

Let

\[
e_n(u)=L^{-1/2}e^{2\pi i n u/L}\mathbf 1_{[0,L]}(u)
\]

as a vector in L^2(R), and let T_y be whole-line translation. Direct overlap calculation gives

\[
q_{nm}(y)=
\langle e_n,T_y e_m\rangle+
\langle T_y e_n,e_m\rangle.
\]

Therefore

\[
\boxed{
(D_y)_{nm}
=
\langle e_n-T_y e_n,\ e_m-T_y e_m\rangle.
}
\]

Consequently

\[
\boxed{D_y\succeq0}
\]

for every 0<=y<=L, and for every finite coefficient vector a,

\[
a^*D_ya=
\left\|\sum_n a_n(e_n-T_ye_n)\right\|_2^2.
\]

This is the exact semilocal matrix version of the whole-line translation-energy identity.

## 3. Pole source in the same y-basis

The healed pole source is

\[
p_L(s)=
\frac{L}{\pi^2}
\int_0^{2\pi}
\cosh\!\left(\frac{L}{4\pi}(2\pi-x)\right)\sin(sx)\,dx.
\]

Put

\[
x=2\pi\left(1-\frac yL\right).
\]

Then dx=-(2\pi/L)dy and

\[
\frac{L}{4\pi}(2\pi-x)=\frac y2.
\]

Hence exactly

\[
\boxed{
p_L(s)=
2\int_0^L\cosh(y/2)\,\psi_y(s)\,dy.
}
\]

Thus

\[
W_{02}=2\int_0^L\cosh(y/2)\,q(y)\,dy.
\]

No zero information enters.

## 4. Archimedean source and the real-place density

Recall

\[
\rho(y)=\frac{e^{y/2}}{e^y-e^{-y}},
\qquad
r(y)=\frac1{e^y-e^{-y}},
\]

\[
\tau_L=\frac12\log\frac{e^L+1}{e^L-1},
\qquad
c_0=\log(4\pi)+\gamma.
\]

The exact regularized Archimedean source is

\[
b_R(s)=
\int_0^L[\rho(y)\psi_y(s)-r(y)\psi_0(s)]\,dy
+\frac{c_0-2\tau_L}{2}\psi_0(s).
\]

Introduce

\[
\boxed{
w_\infty(y)=2\cosh(y/2)-\rho(y).
}
\]

This is the same real-place density already formalized in ArchimedeanLadder.lean, with exact ladder decomposition

\[
w_\infty(y)=e^{y/2}-\sum_{k\ge1}e^{-(2k+1/2)y}.
\]

## 5. Exact prime-power collision normal form

Let

\[
c_n=\frac{\Lambda(n)}{\sqrt n},
\qquad
S_L=\sum_{2\le n\le e^L}c_n.
\]

The prime source is

\[
b_P(s)=\sum_{2\le n\le e^L}c_n\psi_{\log n}(s).
\]

Write

\[
\delta_y(s)=\psi_0(s)-\psi_y(s),
\qquad
L_{\delta_y}=D_y.
\]

Since \psi_y=\psi_0-\delta_y, the full entire source

\[
\widetilde b_W=p_L-b_R-b_P
\]

rearranges exactly as

\[
\boxed{
\widetilde b_W(s)=
M_L\psi_0(s)
+\sum_{2\le n\le e^L}c_n\delta_{\log n}(s)
-\int_0^L w_\infty(y)\delta_y(s)\,dy,
}
\]

where

\[
\boxed{
M_L=
\int_0^L(w_\infty(y)+r(y))\,dy
-\frac{c_0-2\tau_L}{2}
-S_L.
}
\]

The apparent y=0 singularities cancel in the combination w_\infty+r.

Applying the Hermite–Loewner map and using L_{\psi_0}=2I gives

\[
\boxed{
Q_L=
2M_L I
+\sum_{2\le n\le e^L}\frac{\Lambda(n)}{\sqrt n}D_{\log n}
-\int_0^L w_\infty(y)D_y\,dy.
}
\tag{EC}
\]

This is the Euler-local collision decomposition.

Every prime-power term is manifestly positive because c_n>0 and D_{\log n}\succeq0. The Archimedean/pole completion uses the same collision family D_y, plus one scalar Nyquist mass 2M_L I.

## 6. Closed form of the scalar mass

Put q=e^{-L/2}. An elementary substitution gives

\[
\int_0^L(w_\infty+r)\,dy
=
2(e^{L/2}-e^{-L/2})
+\log(1+q)-\frac12\log(1+q^2)
+\arctan q-\frac12\log2-\frac\pi4.
\]

Adding \tau_L and using

\[
\arctan q=
\frac\pi4-\frac12\arctan(\sinh(L/2))
\]

yields

\[
\boxed{
\begin{aligned}
M_L={}&
2(e^{L/2}-e^{-L/2})-S_L
+\operatorname{artanh}(e^{-L/2})\\
&-\frac12\arctan(\sinh(L/2))
-\frac12\log2
-\frac12(\log(4\pi)+\gamma).
\end{aligned}}
\tag{M}
\]

Thus the dominant 2e^{L/2} continuum term and the all-prime-power sum S_L live in one explicit scalar coefficient. This is an RH-strength discrepancy quantity; no smallness claim is made here.

## 7. Trivial-zero ladder form

Using

\[
w_\infty(y)=
e^{y/2}-\sum_{k\ge1}e^{-(2k+1/2)y},
\]

equation (EC) becomes

\[
\boxed{
Q_L=
2M_LI
+\sum_{n\le e^L}c_nD_{\log n}
+\sum_{k\ge1}\int_0^L e^{-(2k+1/2)y}D_y\,dy
-\int_0^L e^{y/2}D_y\,dy.
}
\tag{Ladder}
\]

After the scalar Nyquist mass is isolated:

- every prime-power channel is positive;
- every trivial-zero ladder channel is positive;
- one growing s=1 pole collision family carries the negative sign.

This exact Hodge-like decomposition does not by itself prove positivity: the final growing collision operator is not rank one.

The sharpened hard question is:

> Can the single growing pole collision family be controlled by the positive Euler + trivial-zero collision family on the physical two-box / odd Paley–Wiener sector with only e^{o(L)} loss?

A polynomial loss would already suffice by the fixed-window/vacuum-instability theorem.

## 8. Relation to the two-arrow factorization

Each q(y) already has the exact two-arrow Krein factorization from the arrow-roadmap execution:

\[
q(y)=C_yT_yC_y-S_yT_yS_y.
\]

Equation (EC) says the same one-parameter collision family D_y=2I-q(y) carries the prime, Archimedean, and pole sectors. There is no need to invent incompatible factorizations for the three places.

The arithmetic sewing problem is a weighted comparison of one common collision family.

The shifted-product falsifier changes the prime weights to

\[
2\cosh(\theta\log n)c_n
\]

but leaves the real-place/pole collision density unchanged. Any successful comparison must therefore be sharp enough to hold at theta=0 and fail for theta nonzero.

## 9. Zero-free numerical verification

The companion script verify_euler_archimedean_collision.py checks:

1. the direct source/matrix expression W02-WR-WP;
2. the collision decomposition (EC);
3. the integral definition and closed form (M) of M_L;
4. finite-section eigenvalues of D_y.

At 50 decimal digits, representative checks give residuals at roughly 1e-49 to 1e-50 when L is supplied as an exact decimal mp.mpf. For L=2,N=2:

\[
S_L=2.92623418217640901526901774394\ldots,
\]

\[
M_L=-0.173039278983764618849789597546\ldots,
\]

and

\[
\max_{m,n}|Q^{direct}_{mn}-Q^{collision}_{mn}|
\approx 10^{-50}.
\]

No zeta zeros are used.

## 10. Next execution step

Do not attempt full Weil positivity first.

Insert the physical two-box vector a_t=f_\ell-T_tf_\ell into (EC). For t>\ell, its autocorrelation h_\ell gives the exact collision profile

\[
\|a_t-T_ya_t\|^2
=
4-4h_\ell(y)+2h_\ell(t-y)
\qquad(y\ge0),
\]

with h_\ell(u)=(1-|u|/\ell)_+.

Thus all t-dependent prime terms are concentrated in the moving Euler window h_\ell(t-\log n). The next task is to carry the pole/Archimedean integral through the same profile, cancel every t-independent piece, and isolate the one moving discrepancy whose subexponential control closes RH.

Mandatory controls:

- Davenport–Heilbronn;
- shifted product F_theta(s)=xi(s-theta)xi(s+theta).

If a proposed bound survives either control without using the zeta degree-one local normalization, it has forgotten the arithmetic input.


## 11. Exact insertion of the fixed-window two-box state

This makes the connection to the current RH spine explicit.

Let

\[
f_\ell=\ell^{-1/2}\mathbf 1_{[0,\ell]},
\qquad
h_\ell=f_\ell*\widetilde f_\ell
=\left(1-\frac{|u|}{\ell}\right)_+,
\]

and for \(t>\ell\),

\[
a_t=f_\ell-T_tf_\ell.
\]

Then \(\|a_t\|_2^2=2\). For \(y\ge0\),

\[
\operatorname{Re}\langle a_t,T_ya_t\rangle
=
2h_\ell(y)-h_\ell(t-y),
\]

because the other cross term \(h_\ell(t+y)\) vanishes. Hence the common collision family has the exact profile

\[
\boxed{
D_y[a_t]
=
\|a_t-T_ya_t\|_2^2
=
4(1-h_\ell(y))+2h_\ell(t-y).
}
\tag{TB1}
\]

This is important: the only \(t\)-dependent part is the moving triangular window \(h_\ell(t-y)\).

Define

\[
P_\ell(t)
=
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,
h_\ell(t-\log n).
\]

For \(L\ge t+\ell\), inserting (TB1) into the prime collision sum shows that its entire moving part is

\[
\boxed{2P_\ell(t).}
\]

For the real-place density, use the ladder

\[
w_\infty(y)
=
e^{y/2}
-\sum_{k\ge1}e^{-(2k+1/2)y}.
\]

The triangular bilateral Laplace transform is

\[
\boxed{
H_\ell(a)
=
\int_{-\ell}^{\ell}h_\ell(v)e^{av}\,dv
=
\frac{2(\cosh(a\ell)-1)}{\ell a^2}
}
\tag{TB2}
\]

for \(a\ne0\), with \(H_\ell(0)=\ell\).

Since \(h_\ell(t-y)\) is supported on \(y\in[t-\ell,t+\ell]\), for \(t>\ell\),

\[
\begin{aligned}
\int_0^L w_\infty(y)h_\ell(t-y)\,dy
&=
H_\ell(1/2)e^{t/2}\\
&\quad-
\sum_{k\ge1}
H_\ell(2k+1/2)e^{-(2k+1/2)t}.
\end{aligned}
\]

Put

\[
A_\ell=H_\ell(1/2)
=
\boxed{\frac{8}{\ell}\bigl(\cosh(\ell/2)-1\bigr)}
\]

and

\[
D_\ell(t)
=
\sum_{k\ge1}
H_\ell(2k+1/2)e^{-(2k+1/2)t}>0.
\]

Then the entire moving contribution of the Euler–Archimedean collision form is

\[
\boxed{
2\left[
P_\ell(t)-A_\ell e^{t/2}+D_\ell(t)
\right].
}
\tag{TB3}
\]

But the fixed-window explicit formula writes, for \(t>\ell\),

\[
C_\ell(t)
=
A_\ell e^{t/2}-P_\ell(t)-D_\ell(t).
\]

Therefore

\[
\boxed{
\text{moving collision contribution}=-2C_\ell(t).
}
\tag{TB4}
\]

The remaining \(t\)-independent regularized piece is \(2C_\ell(0)\), giving exactly

\[
\boxed{
Q[a_t]
=
2(C_\ell(0)-C_\ell(t)).
}
\tag{TB5}
\]

Thus the semilocal collision decomposition and the fixed-window growth criterion are not parallel routes: they are the same arithmetic object in two coordinate systems.

For the dyadic window \(\ell=\log2\),

\[
\boxed{
A_{\log2}
=
\frac{6\sqrt2-8}{\log2}.
}
\]

This recovers the exact coefficient in the dyadic prime-window criterion.

### Consequence for the proof search

The full RH-level burden is now located in a single moving collision balance:

\[
P_\ell(t)
-
A_\ell e^{t/2}
+
D_\ell(t)
\ge -e^{o(t)}
\]

in the one-sided sense needed by the fixed-window theorem.

Everything outside this moving window is a \(t\)-independent renormalization.

This also explains why the degree-one Euler structure is the only plausible place left to gain leverage: the growing continuum collision \(A_\ell e^{t/2}\) must be matched by the moving prime-power window \(P_\ell(t)\), while the trivial-zero ladder \(D_\ell(t)\) is positive and exponentially decaying.

The next attack should therefore be on \(P_\ell(t)\) itself through coherent local Euler factors, not on the full semilocal matrix.
