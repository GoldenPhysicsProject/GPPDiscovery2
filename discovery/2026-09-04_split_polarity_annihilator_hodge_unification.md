# Split polarity / annihilator / Hodge unification

## Result

A concrete coordinate bridge was derived between Penrose incidence duality and the Grassmannian/Hodge maps.

For a big-cell graph plane

\[
[I\mid A],\qquad A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad D=\det A\neq0,
\]

ordinary annihilator duality in the dual vector space has canonical row basis

\[
[-A^T\mid I].
\]

Row reduction by \((-A^T)^{-1}\) gives

\[
[I\mid -A^{-T}],
\]

so the Euclidean Grassmannian complement is exactly the annihilator map in the same chart:

\[
C(A)=-A^{-T}.
\]

This is now formalized in `AnnihilatorComplementBridge.lean`.

## Split signature

For the split metric

\[
\eta=\operatorname{diag}(+,+,-,-),
\]

the orthogonal complement of the same graph plane has canonical basis

\[
[A^T\mid I].
\]

Indeed a graph-line vector

\[
x=(r,s,ra+sc,rb+sd)
\]

and a split-dual vector

\[
y=(ta+ub,tc+ud,t,u)
\]

satisfy

\[
\langle x,y\rangle_{2,2}=0
\]

identically.  Row reduction gives

\[
[I\mid A^{-T}],
\]

hence

\[
\boxed{C_{\rm split}(A)=A^{-T}}
\]

is literally split metric polarity.

This is formalized in `SplitPolarityComplementBridge.lean`.

## Hodge identification

The existing Plucker calculation proves

\[
\operatorname{Plucker}(C_{\rm split}(A))
\propto
*_{2,2}\operatorname{Plucker}(A).
\]

Therefore on the invertible big cell we now have an exact coordinate identification

\[
\boxed{D_{\rm polarity}=D_{\rm Gr}=D_{\rm Hodge}}
\]

for the split real slice.

This is packaged in `SplitGooglyGeometryCapstone.lean`.

The Euclidean/standard-dual version is packaged in `ConcreteGooglyDualitySpine.lean`.

## Order-two versus order-four clarification

The split polarity/Hodge complement is an involution:

\[
C_{\rm split}^2=1.
\]

The Grassmannian order-four map is instead

\[
\tau=Q\circ C_{\rm split},
\]

where

\[
Q(a,b,c,d)=(c,d,-a,-b),\qquad Q^2=-I.
\]

Since `Q` commutes with `C_split`,

\[
\tau^2=-I,\qquad \tau^4=I.
\]

Thus the order-four lift is not the Hodge/polarity duality itself.  It is polarity followed by a fixed quarter-turn.  This cleanly separates the order-two Fourier/Hodge representation change from the order-four Grassmannian lift.

## Sign interpretation

The sign difference

\[
-A^{-T}\quad\text{vs}\quad +A^{-T}
\]

is now geometrically explained: standard covector annihilation uses the ordinary evaluation pairing, whereas the split real slice uses the metric polarity induced by `diag(+,+,-,-)`.  The sign is therefore a reality/signature choice, not evidence of two incompatible googly maps.

## Remaining theorem

The finite-dimensional geometric part of

\[
D_{\rm Gr}\cong D_{\rm Hodge}
\]

is now concrete on the big cell.  What remains is the field/cohomological statement linking this correspondence to the twistor transform:

\[
P_-\circ D_\varepsilon = R_{\mathfrak o}\circ P_+,
\]

or the equivalent split Fourier/X-ray pull-push identity.  The next task should therefore focus on the induced transform on homogeneous/cohomological data rather than on further chart-level sign manipulations.
