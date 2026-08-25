#!/usr/bin/env python3
"""High-precision audit of the Gamma Wiener--Hopf Hardy obstruction.

For B(z) = [Gamma(1/2-i z/(2pi))/Gamma(1/2+i z/(2pi))]^2,
Stirling predicts at fixed y>0

    |B(x+i y)| ~ |x/(2pi)|^(2y/pi).

The script prints the quotient of the exact modulus by the asymptotic power.
"""

import mpmath as mp

mp.mp.dps = 80


def B(z):
    return (
        mp.gamma(mp.mpf("0.5") - 1j * z / (2 * mp.pi))
        / mp.gamma(mp.mpf("0.5") + 1j * z / (2 * mp.pi))
    ) ** 2


def main():
    for y in [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2")]:
        print(f"y={y}")
        previous = None
        for x in [mp.mpf("30"), mp.mpf("100"), mp.mpf("300"), mp.mpf("1000")]:
            exact = abs(B(x + 1j * y))
            leading = (x / (2 * mp.pi)) ** (2 * y / mp.pi)
            ratio = exact / leading
            print(
                "  x=", mp.nstr(x, 8),
                " |B|=", mp.nstr(exact, 24),
                " ratio=", mp.nstr(ratio, 24),
            )
            if previous is not None:
                assert abs(ratio - 1) < abs(previous - 1)
            previous = ratio
        assert abs(previous - 1) < mp.mpf("0.01")
    print("Stirling power-growth audit passed.")


if __name__ == "__main__":
    main()
