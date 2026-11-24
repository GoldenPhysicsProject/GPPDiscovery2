"""Finite U(1) charge orthogonality check. Standard library only."""
from cmath import exp
from math import pi
from check import mu


def main():
    cutoff, samples, scale = 60, 127, 12
    counts = [mu(n) for n in range(1, cutoff+1)]
    # Compare Fourier coefficients of the projection/dilation identity exactly.
    for prime in (2, 3, 5, 7):
        for n, coeff_n in enumerate(counts, 1):
            projected = coeff_n if n % prime == 0 else 0
            dilated = -counts[n//prime-1] if n % prime == 0 and n % (prime**2) else 0
            assert projected == dilated
    for coeff in (counts, [abs(x) for x in counts]):
        a = [c*exp(-n/scale).real for n,c in enumerate(coeff,1)]
        traces = [sum(c*exp(2j*pi*n*k/samples) for n,c in enumerate(a,1))
                  for k in range(samples)]
        exact = sum(c*c for c in a)
        observed = sum(abs(z)**2 for z in traces)/samples
        assert abs(observed-exact) < 1e-12
        print('untwisted trace, squared holonomy norm:', traces[0].real, exact)


if __name__ == '__main__':
    main()
