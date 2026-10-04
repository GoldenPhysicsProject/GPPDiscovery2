"""Finite-window quadrature for exact totient dilation correlations.

Requires NumPy. No zero data; finite tails are not certified by this script.
The Gauss panels split every threshold for dilation ratios 1, 2, and 3.
"""
import argparse
import json
import numpy as np


def totients(nmax):
    phi = np.arange(nmax + 1, dtype=np.int64)
    for p in range(2, nmax + 1):
        if phi[p] == p:
            phi[p::p] -= phi[p::p] // p
    return phi


def response(x, coeff):
    n = np.arange(1, len(coeff), dtype=np.float64)
    out = np.empty_like(x)
    for first in range(0, len(x), 128):
        last = min(first + 128, len(x))
        y = n[None, :] / x[first:last, None]
        y = np.minimum(y, 1.0)
        g = 4*y*np.arccos(y) - 2*np.sqrt((1-y)*(1+y))
        out[first:last] = np.sum(g*coeff[None, 1:], axis=1)
    return out


def run(cutoff, order):
    nmax = 3*cutoff
    phi = totients(nmax)
    coeff = phi.astype(float)
    coeff[1:] /= np.arange(1, nmax + 1)
    nodes, weights = np.polynomial.legendre.leggauss(order)
    # Six equal panels per integer: split integer, half- and third-integer cusps.
    left = np.arange(6, 6*cutoff, dtype=float)/6
    x = (left[:, None] + (nodes[None, :] + 1)/12).ravel()
    w = np.broadcast_to(weights[None, :]/12, (len(left), order)).ravel()
    k = response(x, coeff)
    rows = []
    for r in [1, 2, 3]:
        kr = k if r == 1 else response(r*x, coeff)
        value = float(np.sum(w*k*kr/x))
        rows.append({'r':r, 'integral_1_to_cutoff':value,
                     'exact_infinite_integral':1/(2*r),
                     'infinite_value_minus_finite':1/(2*r)-value})
    return {'cutoff':cutoff, 'gauss_order':order, 'panels_per_integer':6,
            'arithmetic':'float64', 'rows':rows,
            'status':'finite quadrature only; no certified tail or RH decay estimate'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--cutoff', type=int, default=256)
    parser.add_argument('--order', type=int, default=16)
    args = parser.parse_args()
    print(json.dumps(run(args.cutoff, args.order), indent=2))
