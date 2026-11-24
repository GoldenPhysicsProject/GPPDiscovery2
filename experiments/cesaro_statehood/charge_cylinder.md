# Möbius heat sums on a compact-boson cylinder

This is a realization of the Statehood observable in a specific standard unitary CFT. It identifies its charge, Hamiltonian, insertion and holonomy, and derives a bound for almost every fixed holonomy. It does not identify the full AFT with the compact boson or prove the untwisted bound.

## Exact charge-channel dictionary

Use the chiral even lattice L=√2 Z at central charge one. Its vacuum module decomposes into oscillator Fock spaces indexed by n∈Z. Normalize Q|n⟩=n|n⟩; on its oscillator descendants L₀=n²+N. Take q=exp(−t), t>0, and let η(q)=q^(1/24)∏_{k≥1}(1−q^k). The insertion M is diagonal, equal to μ(n) on charge n≥1 and zero elsewhere. This is a bounded operator commuting with the current oscillators and Virasoro; no locality, modular transformation law or topological-defect sewing axiom for M is assumed. Let U(α)=exp(2πiαQ). Then

    η(q) Tr( M U(α) q^(L₀−1/24)) = Σ_{n≥1} μ(n) exp(−tn²)e^(2πinα).

This follows by tracing oscillators in each charge sector. Subordinating that stripped heat trace gives the exact observable of the Statehood test:

    A_X(α)=Σ μ(n)exp(−n/X)e^(2πinα)
          = (y/(2√π)) ∫₀∞ t^(−3/2) exp(−y²/(4t)) Σ μ(n)exp(−tn²)e^(2πinα) dt,
    y=1/X.

The scalar subordination formula follows from the Gaussian integral; interchange is absolutely justified by Σ exp(−yn)<∞. The linear energy |Q| in this Poisson kernel is obtained by functional calculus on the charge sector. A_X(0)=S(X), exactly; this construction keeps the integer phases at that angle. M was specified from arithmetic. Realizing it as an insertion does not derive its coefficients from the stress tensor.

## Square-root bound at almost every fixed relative holonomy

The U(1) character orthogonality relation gives

    ∫₀¹ |A_X(α)|² dα = Σ μ(n)² exp(−2n/X) = X/(2ζ(2))+O(√X).

The last equality is partial summation from Σ_{n≤u}μ(n)²=u/ζ(2)+O(√u). To pass from an average to individual angles simultaneously for all large X, take R dyadic, v=log(X/R) in [0,log 2]. By Parseval both ∫ |A_X|² and ∫ |∂_v A_X|² are O(R) uniformly on this interval: the derivative multiplies the nth coefficient by n/X and Σ (n/X)² exp(−2n/X)≪X. Sobolev's inequality on this fixed v interval, followed by integration in α, gives

    ∫₀¹ sup_{R≤X≤2R}|A_X(α)|² dα ≪ R.

Chebyshev bounds the measure where the supremum exceeds R^(1/2+ε) by O(R^(−2ε)). Summing over dyadic R and applying Borel–Cantelli proves that for almost every single fixed α and every ε>0, A_X(α)=O_{α,ε}(X^(1/2+ε)) for every X≥1. Take a countable intersection over positive rational ε. This bound uses only |μ|≤1 and charge orthogonality, apart from the precise mean-square constant. It is consistent with the classical metric theory of orthogonal series.

## Why fixing the holonomy is substantive

Replace M by the positive insertion |M|, with coefficients μ(n)². It has exactly the same holonomy mean-square curve for every X and the same almost-everywhere bound. Yet at α=0 its trace after subordination is X/ζ(2)+O(√X). This is an explicit example, in the same Hilbert space with the same stress tensor, where inferring a bound at trivial holonomy from the mean or from almost-everywhere behavior fails. The self-dual arithmetic point requires cancellation of the actual signs.

Nor does the usual two-character modular transformation of the A₁ lattice CFT automatically supply the missing identity. At α=0, after stripping η, ordinary irreducible characters have numerators Σ q^(n²) and Σ q^((n+1/2)²) with n∈Z. A constant combination equal to Σ_{n≥1} μ(n)q^(n²) would have to have zero second coefficient by its q^(1/4) term and zero first coefficient by its constant term. The target has coefficient 1 at q. Any usable modular relation for M must therefore involve additional amplitudes or additional structure. This argument concerns the ordinary two-character span only.

At α=0 the desired conclusion is precisely S(k²)=O_ε(k^(1+ε)). The Mellin and derivative argument in scalar_bound.md proves that this is equivalent to RH. The almost-everywhere theorem supplies no bound at that specified angle. The CFT calculation gives a concrete benchmark for a proposed AFT Ward or sewing identity: it must constrain the signed trace at zero holonomy and evade the |M| control.

Run charge_cylinder_check.py for a finite character-orthogonality test with the actual signs and the positive control. No zero data are inputs.

## An exact arithmetic identity between holonomies and scales

Write A(y,α)=A_(1/y)(α). Let Π_p average the U(1) insertion over α+j/p for j=0,…,p−1, and T_p f(y,α)=f(py,pα). On charge characters Π_p projects onto charges divisible by p. Squarefreeness and fermion parity then give the exact identity

    Π_p A = −T_p(I−Π_p) A.

Indeed the coefficient at charge pm is −μ(m) when p does not divide m and zero when p divides m. The positive control |M| has the opposite sign in this identity. Within amplitudes of the form Σ a_n exp(−ny)e^(2πinα) on positive charges, these identities for every prime and the charge-one coefficient a₁=1 uniquely specify all the μ(n), by repeated division. Thus the arithmetic sign has an observable signature in the CFT. This uses the dilation relation of the charge sums, without asserting it follows from the Virasoro algebra.

At p=2 write C(y)=A(y,0), D(y)=A(y,1/2). The identity reduces to

    D(y)−D(2y) = −C(y)−C(2y).

For any β>0, C(y)=O(y^(−β)) at zero iff D(y)=O(y^(−β)). To see both directions telescope D(y)−D(2y), or iterate C(y)=−C(2y)−D(y)+D(2y). Terms with 2^j y≤1 are bounded by a geometric series with ratio 2^(−β); the remaining terms decay exponentially as their arguments grow. In particular a square-root-with-epsilon estimate at the fixed half-turn would suffice for Statehood. Almost-everywhere control does not certify that fixed twist either. The identity supplies the sign and moves the missing bound to a second explicit amplitude; bounding either amplitude at that strength remains open.
