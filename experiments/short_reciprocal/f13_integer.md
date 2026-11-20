# An integer encoding of the prime term in the F13 bound

Put X=exp(L)>1 and let D(L)=A(L)-S(L) in the Round 23 convention. Grouping the prime powers gives
$
 S(L)=\sum_{p\le X} b_p(X)\log p,\qquad
 b_p(X)=\sum_{p^j\le X,\ j\ge1}p^{-j/2}\log(X/p^j).
$
All these real coefficients are nonnegative. For a positive integer T define the explicit integer
$
 N(X,T)=\prod_{p\le X}p^{\lceil T b_p(X)\rceil}.
$
Counting each prime once in the rounding error yields
$
 0\le T^{-1}\log N(X,T)-S(L)\le T^{-1}\sum_{p\le X}\log p.
$
Choose T=ceil(X log(2X)). Even the elementary estimate sum(log p) <= X log X now bounds the error by 1. No prime number theorem, zero data or floating-point rounding is involved. One may use T=ceil(X) with Chebyshev's estimate if only a uniform constant is needed.

For any epsilon >= 0, an upper bound log N / T <= A(L)+C exp(epsilon L) implies the filed lower bound on D(L). Conversely the filed lower bound gives the upper bound with C+1. These implications also hold restricted to any specified set of L, with the same set on both sides. They do not extend the zero-free implication in F13 to sparse sets.

A concrete sufficient arithmetic statement is to exhibit, independently of the target estimate, a nonzero integer M(X) divisible by N(X,T) and an archimedean estimate log |M(X)| <= T(A(L)+C exp(epsilon L)). Nonvanishing, the prime valuations and the upper bound must hold for the same M. The integer N supplies the required valuations by definition. Taking M=N merely restates the desired estimate. A proposed factorial ratio, determinant or evaluation map can be checked against these three conditions. For an algebraic integer one must use a norm or include all the weighted archimedean places.

In the distinct Riesz kernel discussed by Heart, a prime power n contributes, after multiplying by X^{-1/2}, n^{-1/2} 2 sinh(u/2) with u=log(X/n); the present kernel contributes n^{-1/2}u. The quotient tends to 1 at the cutoff and is unbounded for large u. Comparing unsigned prime terms alone does not compare the centered remainders. The outside window criterion cannot simply be substituted into F13.

This calculation is elementary. Its contribution is to specify the integer and precision a proposed construction can target. The required archimedean estimate remains open.
