# Incidence kernel for the diagonal googly transform

Date: 2026-09-03
Status: discovery note, theorem target not yet analytic proof

## Key correction

The ambient four-form/annihilator construction does not canonically define a point map

PT -> PT*.

For a 2-plane W subset V representing a spacetime point, annihilator duality gives the dual 2-plane

W -> W^0 subset V*.

Thus the natural projective object is a dual twistor line P(W^0), not a single dual twistor point.

## Canonical correspondence

If L subset W is a twistor point on P(W), and K subset W^0 is any dual twistor point on P(W^0), then every alpha in K annihilates every Z in L:

alpha(Z)=0.

Therefore the canonical incidence kernel over W is

P(W) x P(W^0),

not the graph of a pointwise map P(W) -> P(W^0).

On the Gr(2,4) big cell this was formalized in

GppVerify/CelestialHolography/IncidenceKernelGoogly.lean

at commit 3c96f48b26732c2556357095ea15c2ac0583904f.

The coordinate theorem proves that a general graph-line vector

Z(r,s)=(r,s,ra+sc,rb+sd)

pairs to zero with a general annihilator-line covector

W(t,u)=(-(ta+ub),-(tc+ud),t,u)

for all r,s,t,u:

<Z(r,s),W(t,u)>=0.

## Interpretation

This is a stronger and cleaner explanation of why the googly operation should be a field-level correspondence/integral transform rather than a pointwise twistor involution. The ambient geometry canonically pairs the whole original twistor line with the whole annihilator dual line.

This fits the current diagonal-lift hypothesis:

- Gr(2,4) complement/annihilator is canonical;
- projective weight duality k -> -k-4 is canonical;
- helicity reversal follows from k=2h-2;
- the missing analytic step is to construct the induced transform on cohomology/field data from this incidence kernel and prove the Penrose commuting square.

The desired theorem remains

P_- o D_epsilon = R_orientation o P_+,

but D_epsilon should now be sought as an integral/correspondence transform over the incidence kernel, not as a map of individual twistor points.

## External consistency check

The classical Penrose transform is itself an integral-geometric transform on the double fibration

PT <- F_{1,2}(V) -> Gr(2,V),

and in split signature becomes the X-ray transform. This is structurally consistent with a correspondence-level googly map. Aryapoor's split Penrose transform and Mason's split-signature discussion are useful external checks, not ingredients to be copied into the GPP construction.

## Falsifier / next target

The proposal fails as a complete googly mechanism if the annihilator incidence kernel does not induce a well-defined map between the relevant opposite-helicity cohomology classes, or if the induced map fails to intertwine the two Penrose transforms with orientation reversal.

Next target: define the dual flag correspondence

(L subset W) -> (W^0 subset L^0)

and derive the induced pull-push transform on homogeneous data. Track the canonical -4 determinant twist explicitly rather than inserting it by hand.
