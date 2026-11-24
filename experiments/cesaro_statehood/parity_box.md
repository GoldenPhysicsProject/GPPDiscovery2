# Dyadic subtraction puts the surviving half-turn on the cofactor

Let M(N)=Σ_{n≤N}μ(n), U=⌊√N⌋, N≥4. Both sides of the following integer identity retain the genuine signs:

    M(N)−2M(⌊N/2⌋) = −2M(U)−Q(N),
    Q(N)=Σ_{d,e≤U} μ(d)μ(e) K_N(d,e),
    K_N(d,e)=⌊N/(de)⌋ mod 2.

This uses a standard truncated Dirichlet hyperbola identity, applied twice. Let a=μ restricted to [1,U], b=μ−a, and let 1 denote the constant arithmetic function. Then b*1*b = μ−2a+a*1*a because μ*1 is the convolution identity. The left side vanishes below (U+1)². Summing through each of N and ⌊N/2⌋ using the same U yields the formula since both cutoffs are at least U. Subtracting twice the smaller floor from the larger floor leaves its parity. Equivalently the kernel is the alternating sum of the phases (−1)^(j+1) for the free cofactor charges j≤N/(de). This half-turn acts on j; the external Möbius charge remains untwisted. The previous cylinder identity transfers a completed untwisted heat bound to the fixed half-turn.

The correction −2M(U) already has size ≤2√N. Thus |Q(N)|≪ε N^(1/2+ε) for all N suffices for the independent proof. Indeed write D(N)=M(N)−2M(⌊N/2⌋). The prime number theorem M(n)=o(n) allows backward recovery M(N)=−Σ_{j≥1}2^(−j)D(2^jN) by telescoping. For 0<ε<1/2 this geometric sum preserves exponent 1/2+ε. Conversely a bound of that order on M gives the same bound for Q. No invocation of RH is used in this equivalence. Partial summation gives the heat-amplitude estimate from M.

## A quantitative check on the proposed sign mechanism

For each p≤U give the prime an independent uniform random sign and extend the signs χ multiplicatively. Insert χ(d)χ(e) into Q. The root mean square of the resulting quadratic form obeys

    (E |Q_χ(N)|²)^(1/2) ≤ U (1+log(U²))².

In fact the bound works for any deterministic matrix with entries of modulus at most one. To prove it group squarefree pairs as d=ga, e=gb with g their gcd. The sign character of the pair is χ(c) with c=ab squarefree. Distinct c give orthogonal characters. For any c the absolute grouped coefficient is at most Σ_{a|c} U/max(a,c/a) ≤ U·τ(c)/√c. Squaring and summing gives ≤U² Σ_{c≤U², squarefree} 4^ω(c)/c. For squarefree c, 4^ω(c) counts ordered factorizations into four positive integers; dropping the product constraint yields at most (1+log(U²))⁴ for the last sum. Orthogonality here is over auxiliary prime signs, not over the distinguished physical charge angle. It does not bound Q at the identity twist, nor assert a hyperbola identity for other twists with this same kernel.

The matrix alone gives insufficient control. On the index block √(N/2)<d,e≤√N every entry is 1, so its operator norm is at least the block size, of order √N. At N=6 its principal block on 1,2 is [[0,1],[1,1]], which is indefinite. A positivity claim for the kernel, or a uniform operator bound ignoring the distinguished vector, cannot supply the missing estimate. In fact an all-positive indicator confined to the large-index block gives a quadratic form of order N. What the arithmetic needs is cancellation on the specific squarefree vector μ. Grouping by c makes its sign (−1)^ω(c) explicit. No independent uniform bound for that signed sum is proved here.

## Reproduction

Run parity_box.py with Python. It checks every N from 4 through 1000 and three larger cutoffs by an independent Möbius sieve. At N=10⁶ it finds U=1000, Q=−228 and D=224. At N=225 the exact prime-sign mean square is 289 by enumeration and independently by grouping. These finite checks illustrate the identities. They do not establish the asymptotic bound for the genuine signs.
