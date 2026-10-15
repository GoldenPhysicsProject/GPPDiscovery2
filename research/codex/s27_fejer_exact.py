from fractions import Fraction

def fejer_lift(M, c):
    """Exact cosine coefficients for a nonnegative shifted Fejer upper bound."""
    assert M >= 2 and c > 0
    c = Fraction(c)
    K = c * Fraction(M+1, 2*M)
    F = [Fraction(1)] + [
        Fraction(2 * (M+1-k) * (-1)**k, M+1)
        for k in range(1, M+1)
    ]
    h = [Fraction(0), c + K*F[1]] + [K*F[k] for k in range(2,M+1)]
    assert h[1] == 0
    B = [Fraction(0), c] + [Fraction(0)]*(M-1)
    assert all(B[k]-h[k] == K*(int(k==0)-F[k]) for k in range(M+1))
    return K,h

for M in (2,3,5,10,50):
    k,h=fejer_lift(M,Fraction(14,5))
    print(M, k, h[1])
