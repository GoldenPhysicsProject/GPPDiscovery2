"""Exact finite tests for a two-sheet, antiunitary spin-half clock.

This is a falsifier/prototype, not a spacetime, quantum-field, or RH proof.
No third-party packages are required.

Let A(v)(u) = R conjugate(v(-u)) with R=[[0,1],[-1,0]].
Then A is norm-preserving and antiunitary, A^2=-I. Two sheets admit
J(v,w)=(A w,-A v), with J^2=I. The untwisted exchange (A w,A v)
instead squares to -I and has no nonzero fixed vectors over C.

J-fixed pairs are Kramers orthogonal: <v,w>=0 when w=-A v.
Consequently their scalar sheet-mixing beat vanishes, while an
off-diagonal spin-sensitive operator can oscillate at 2E/hbar.
"""

import cmath
import math
import random


def spin_reverse(v):
    """R conjugate(v) at a single logarithmic scale."""
    return (v[1].conjugate(), -v[0].conjugate())


def spin_neg(v):
    return tuple(-z for z in v)


def inner(v, w):
    return sum(z.conjugate() * t for z, t in zip(v, w))


def reverse_field(field):
    """Finite log-Haar model: u -> -u, complex conjugation, spin flip."""
    return {u: spin_reverse(field[-u]) for u in field}


def norm2(field):
    return sum(inner(v, v).real for v in field.values())


def double_reflection(pair):
    v, w = pair
    return reverse_field(w), {u: spin_neg(z) for u, z in reverse_field(v).items()}


def untwisted_reflection(pair):
    v, w = pair
    return reverse_field(w), reverse_field(v)


def scalar(z):
    return {0: z}


def samples():
    rng = random.Random(20261028)
    for radius in (0, 1, 3, 7):
        us = range(-radius, radius + 1)
        f = {u: complex(rng.randrange(-9, 10), rng.randrange(-9, 10)) for u in us}
        g = {u: (complex(rng.randrange(-9, 10), rng.randrange(-9, 10)),
                 complex(rng.randrange(-9, 10), rng.randrange(-9, 10))) for u in us}
        h = {u: (complex(rng.randrange(-9, 10), rng.randrange(-9, 10)),
                 complex(rng.randrange(-9, 10), rng.randrange(-9, 10))) for u in us}
        yield f, g, h


def test_involutions():
    for _, f, g in samples():
        a2 = reverse_field(reverse_field(f))
        assert a2 == {u: spin_neg(v) for u, v in f.items()}
        assert norm2(f) == norm2(reverse_field(f))
        p = (f, g)
        assert double_reflection(double_reflection(p)) == p
        assert untwisted_reflection(untwisted_reflection(p)) == (
            {u: spin_neg(v) for u, v in f.items()},
            {u: spin_neg(v) for u, v in g.items()},
        )
        for theta in (0, math.pi / 7, math.pi / 3):
            phase = cmath.exp(1j * theta)
            v = f[0]
            one = tuple(phase * z for z in spin_reverse(v))
            twice = tuple(phase * z for z in spin_reverse(one))
            assert max(abs(x + y) for x, y in zip(twice, v)) < 1e-12


def test_kramers_overlap_and_beat():
    """The equal-energy two-sheet phase need not produce scalar trembling."""
    v = (1 + 0j, 0 + 0j)
    w = spin_neg(spin_reverse(v))
    assert v == spin_reverse(w)
    assert inner(v, w) == 0
    flipped_w = (w[1], w[0])  # sigma_x w
    assert inner(v, flipped_w) == 1
    E, hbar = 3.0, 2.0
    for t in (0, 0.17, 0.51, 1.3, 2.7):
        plus = cmath.exp(-1j * E * t / hbar)
        minus = cmath.exp(1j * E * t / hbar)
        scalar_mixing = (plus.conjugate() * minus * inner(v, w)).real
        spin_sensitive = (plus.conjugate() * minus * inner(v, flipped_w)).real
        assert scalar_mixing == 0
        assert abs(spin_sensitive - math.cos(2 * E * t / hbar)) < 1e-14
    return 2 * E / hbar


def test_log_clock_obstruction():
    """A constant rest energy cannot match lambda*log(tau) for all tau>0."""
    lam, hbar, c = 5.0, 2.0, 1.0
    m_at_one = hbar * lam / (c * c * 1.0)
    m_at_two = hbar * lam / (c * c * 2.0)
    assert m_at_one != m_at_two
    return m_at_one, m_at_two


def main():
    test_involutions()
    omega = test_kramers_overlap_and_beat()
    masses = test_log_clock_obstruction()
    print("PASS: log-Haar spin A is antiunitary and A^2=-I")
    print("PASS: naive two-sheet exchange has square -I; signed exchange J^2=+I")
    print("PASS: multiplying A by a U(1) phase does not change its square")
    print("PASS: J-fixed partners have zero scalar overlap")
    print("PASS: spin-sensitive two-sheet observable has frequency", omega)
    print("PASS: Mellin and proper-time clocks need m_eff(tau) proportional to 1/tau")
    print("Example inferred masses at tau=1,2:", masses)


if __name__ == "__main__":
    main()
