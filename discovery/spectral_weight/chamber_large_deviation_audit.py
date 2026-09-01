#!/usr/bin/env python3
"""Numerical audit for the exact Gamma/Mehler-Fock chamber MGF and rate law."""
import mpmath as mp

mp.mp.dps = 60


def rho0(x):
    if abs(x) < mp.mpf("1e-40"):
        return 2 / mp.pi
    return 2 * x / mp.sinh(mp.pi * x)


def mgf_numeric(theta):
    return mp.quad(lambda x: mp.e ** (theta * x) * rho0(x), [-mp.inf, 0, mp.inf])


def mgf_exact(theta):
    return 1 / mp.cos(theta / 2) ** 2


def rate(x):
    return 2 * x * mp.atan(x) - mp.log(1 + x * x)


def rate_prime(x):
    return 2 * mp.atan(x)


def rate_second(x):
    return 2 / (1 + x * x)


if __name__ == "__main__":
    print("MGF checks for rho_0")
    for theta in [mp.mpf("0"), mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("3")]:
        num = mgf_numeric(theta)
        exact = mgf_exact(theta)
        print(theta, mp.nstr(num, 40), mp.nstr(exact, 40), mp.nstr(abs(num-exact), 6))

    print("\nRate function checks")
    for x in [mp.mpf("0"), mp.mpf("0.25"), mp.mpf("1"), mp.mpf("3")]:
        h = mp.mpf("1e-8")
        d1_num = (rate(x+h)-rate(x-h))/(2*h)
        d2_num = (rate(x+h)-2*rate(x)+rate(x-h))/(h*h)
        print(x, mp.nstr(rate(x), 30), mp.nstr(d1_num-rate_prime(x), 6), mp.nstr(d2_num-rate_second(x), 6))
