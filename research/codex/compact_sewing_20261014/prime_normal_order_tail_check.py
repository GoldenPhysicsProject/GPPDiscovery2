#!/usr/bin/env python3
"""Prime-jump non-Levy tail / exact vacuum counterterm probe.

This is NOT a global RH test. It checks finite prime-power sums, using a
compact-support sharp odd autocorrelation whose formula is independently
Lean-verified in OddWindowAutocorrelation. Cutoffs are NOT used to infer RH;
the sign and limiting tail are established analytically in bridge note.
"""
import math

h = 1.0
N = math.sinh(h) - h

def autocorrelation(t):
    t = abs(t)
    if t >= 2 * h:
        return 0.0
    return (math.sinh(h - t/2) - (h - t/2) * math.cosh(t/2)) / N

def prime_powers(limit):
    composite = bytearray(limit + 1)
    entries = []
    for p in range(2, limit+1):
        if composite[p]:
            continue
        for j in range(2*p, limit+1, p):
            composite[j] = 1
        pk = p
        while pk <= limit:
            entries.append((pk, 2*math.log(p)/math.sqrt(pk)))
            if pk > limit // p:
                break
            pk *= p
    return sorted(entries)

def main():
    all_powers = prime_powers(int(math.exp(12)))
    mass, pair, pos = 0.0, 0.0, 0
    for R in (2, 4, 6, 8, 10, 12):
        while pos < len(all_powers) and all_powers[pos][0] <= math.exp(R):
            n, coeff = all_powers[pos]
            mass += coeff
            pair += coeff * autocorrelation(math.log(n))
            pos += 1
        jump_form = mass - pair
        normal_ordered = jump_form - mass
        assert abs(normal_ordered + pair) < 1e-9
        print(f'R={R:2d} primepowers={pos:5d} '
              f'M_prime={mass:13.7f} positive_J={jump_form:13.7f} '
              f'J_minus_counterterm={normal_ordered:13.7f}')
        if R >= 2:
            assert abs(normal_ordered - 1.2877354273457737) < 1e-8
if __name__ == '__main__':
    main()
