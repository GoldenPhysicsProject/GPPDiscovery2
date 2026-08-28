from fractions import Fraction

# Exact executable audit of the scalar moment bridge and pointwise
# squared-Vandermonde expansion used by the finite-support Fisher theorem.

def fisher_det(m1, m2, m3, m4):
    return (m2 - m1*m1)*(m4 - m2*m2) - (m3 - m1*m2)**2


def moment_discriminant(m0, m1, m2, m3, m4):
    return 6*(m0*m2*m4 + 2*m1*m2*m3 - m2**3 - m0*m3**2 - m1*m1*m4)


def vandermonde_sq(a, b, c):
    return ((a-b)*(a-c)*(b-c))**2


def vandermonde_expanded(a, b, c):
    return (
        a**4*b**2 - 2*a**4*b*c + a**4*c**2
        - 2*a**3*b**3 + 2*a**3*b**2*c + 2*a**3*b*c**2 - 2*a**3*c**3
        + a**2*b**4 + 2*a**2*b**3*c - 6*a**2*b**2*c**2
        + 2*a**2*b*c**3 + a**2*c**4
        - 2*a*b**4*c + 2*a*b**3*c**2 + 2*a*b**2*c**3 - 2*a*b*c**4
        + b**4*c**2 - 2*b**3*c**3 + b**2*c**4
    )

# Rational data ensure exact arithmetic.
p = [Fraction(1, 15), Fraction(2, 15), Fraction(3, 15), Fraction(4, 15), Fraction(5, 15)]
x = [Fraction(-2), Fraction(-1), Fraction(0), Fraction(2), Fraction(5)]

m = [sum(pi * xi**r for pi, xi in zip(p, x)) for r in range(5)]
assert m[0] == 1
assert moment_discriminant(*m) == 6*fisher_det(m[1], m[2], m[3], m[4])

for a in x:
    for b in x:
        for c in x:
            assert vandermonde_sq(a,b,c) == vandermonde_expanded(a,b,c)

ordered = sum(
    p[i]*p[j]*p[k]*vandermonde_sq(x[i],x[j],x[k])
    for i in range(len(x))
    for j in range(len(x))
    for k in range(len(x))
)
assert ordered == moment_discriminant(*m)
assert ordered == 6*fisher_det(m[1], m[2], m[3], m[4])

print('m0..m4 =', m)
print('ordered energy =', ordered)
print('Fisher determinant =', fisher_det(m[1],m[2],m[3],m[4]))
print('identity exact:', ordered == 6*fisher_det(m[1],m[2],m[3],m[4]))
