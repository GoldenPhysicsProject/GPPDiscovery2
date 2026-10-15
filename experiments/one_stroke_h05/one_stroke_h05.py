"""Independent float design: h=1/2 Weil one-stroke Legendre lower envelope.

Golden Physics Project / Daniel Toupin / Codex, October 15 2026.
Method follows Marcus Chuk, arXiv:2608.24827 (Sep 2026), with a
fresh independent SciPy assembly for the one-prime window.

UNTRUSTED FLOAT: no interval certificate and no global RH/GRH proof.
"""
import argparse
import math

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import eigvalsh
from scipy.special import digamma, spherical_in, spherical_jn


def finite_block(h, T, beta, nmodes, nquad, parity):
    nodes, weights = leggauss(nquad)
    freqs = (nodes + 1) * T / 2
    weights = weights * T / 2
    amp = 2 * math.log(2) / math.sqrt(2)
    symbol = (np.real(digamma(.25 + .5j * freqs))
              - math.log(math.pi)
              - amp * np.cos(freqs * math.log(2)))
    quadrature_weight = (weights / math.pi) * (symbol - beta)
    degrees = range(parity, 2 * nmodes, 2)
    f = np.stack([
        (-1) ** (degree // 2) * math.sqrt(2 * h * (2 * degree + 1))
        * spherical_jn(degree, h * freqs)
        for degree in degrees
    ])
    pole = np.asarray([
        math.sqrt(2 * h * (2 * degree + 1))
        * spherical_in(degree, h / 2)
        for degree in degrees
    ])
    matrix = beta * np.eye(nmodes) + (f * quadrature_weight) @ f.T
    matrix += ((-1) ** parity) * 2 * np.outer(pole, pole)
    return eigvalsh(matrix, subset_by_index=[0, 1])


def bessel_tail(h, T, nmodes):
    # |j_n(x)| <= x^n/(2n+1)!! for real x, by Bessel's integral representation.
    # Even parity n=2N is the first omitted degree; an analogous odd bound
    # starts at 2N+1 and is smaller.
    n = 2 * nmodes
    doublefactorial_log = math.lgamma(2 * n + 2) - n * math.log(2) - math.lgamma(n + 1)
    first = math.exp(.5 * math.log(2 * h * (2 * n + 1)) +
                     n * math.log(h * T) - doublefactorial_log)
    geometric_ratio = ((h * T)**2 / ((2*n + 3)*(2*n + 5))
                       * math.sqrt((2*n + 5)/(2*n + 1)))
    # Trace of omitted finite-frequency Fourier projection divided by pi.
    return (T / math.pi) * first**2 / (1 - geometric_ratio**2), first


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--h', type=float, default=.5)
    parser.add_argument('--T', type=float, default=35)
    parser.add_argument('--modes', type=int, default=40)
    parser.add_argument('--quad', type=int, default=1000)
    args = parser.parse_args()
    h, T = args.h, args.T
    if not math.log(2) < 2*h < math.log(3):
        raise ValueError('Only the prime-2-active, prime-3-inactive window is implemented')
    if T < 15/4:
        raise ValueError('The borrowed Archimedean envelope needs T >= 15/4')
    A = 2 * math.log(2) / math.sqrt(2)
    beta = math.log(T/(2*math.pi)) - A - 1/T
    if beta <= 0:
        raise ValueError('Choose T so the borrowed global frequency floor is positive')
    ev = finite_block(h, T, beta, args.modes, args.quad, 0)
    od = finite_block(h, T, beta, args.modes, args.quad, 1)
    tail, first = bessel_tail(h, T, args.modes)
    print('UNTRUSTED FLOAT / NOT A WEIL CERTIFICATE / RH OPEN')
    print(f'h={h} T={T} modes_per_sector={args.modes} gauss_nodes={args.quad}')
    print(f'prime_comb_A={A:.15g} high_frequency_floor_beta={beta:.15g}')
    print(f'even two smallest eigenvalues {ev}')
    print(f'odd  two smallest eigenvalues {od}')
    print(f'first omitted even Bessel-amplitude bound {first:.6g}')
    print(f'Fourier tail trace estimate {tail:.6g}')
    print('Outstanding: rigorous digamma and quadrature intervals, rational Cholesky,')
    print('and complete infinity-tail/operator coupling (including pole) certificate.')

if __name__ == '__main__':
    main()
