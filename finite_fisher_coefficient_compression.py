from collections import defaultdict

# Exact coefficient compression for the 19-monomial expansion of
# ((a-b)(a-c)(b-c))^2.  After summing against p_i p_j p_k, an exponent triple
# (r,s,t) contributes m_r m_s m_t, so only the sorted exponent multiset matters.

terms = [
    ((4, 2, 0), 1), ((4, 1, 1), -2), ((4, 0, 2), 1),
    ((3, 3, 0), -2), ((3, 2, 1), 2), ((3, 1, 2), 2), ((3, 0, 3), -2),
    ((2, 4, 0), 1), ((2, 3, 1), 2), ((2, 2, 2), -6),
    ((2, 1, 3), 2), ((2, 0, 4), 1),
    ((1, 4, 1), -2), ((1, 3, 2), 2), ((1, 2, 3), 2), ((1, 1, 4), -2),
    ((0, 4, 2), 1), ((0, 3, 3), -2), ((0, 2, 4), 1),
]

compressed = defaultdict(int)
for exponents, coefficient in terms:
    compressed[tuple(sorted(exponents))] += coefficient

expected = {
    (0, 2, 4): 6,
    (1, 1, 4): -6,
    (0, 3, 3): -6,
    (1, 2, 3): 12,
    (2, 2, 2): -6,
}

assert dict(compressed) == expected

# Therefore the ordered Vandermonde energy is exactly
# 6*(m0*m2*m4 + 2*m1*m2*m3 - m2^3 - m0*m3^2 - m1^2*m4).
print(dict(sorted(compressed.items())))
print("compressed identity exact:", dict(compressed) == expected)
