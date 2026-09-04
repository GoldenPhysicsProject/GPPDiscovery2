#!/usr/bin/env python3
"""Exact Ward audit for the generic nonzero-mu color-ordered Yang-Mills tree.

This validates the Feynman-rule engine used by
``massive_vector_generic_state_sum_symbolic.py`` independently of the later
state-sum simplifications.  The engine is the complete color-ordered four-gluon
tree (two cubic channels plus the quartic contact term), evaluated on 5D-null
kinematics whose four-dimensional projection has mass ``mu = E*rho``.

For every helicity pair of the two ordinary gluons and every physical basis
polarization of the two massive-vector legs, replacing any one external
polarization by its own null momentum must annihilate the tree.  We check all
four external Ward identities exactly in SymPy.

This certifies gauge consistency of the discovery-level tree engine.  It does
not by itself fix coupling/color factors, cut orientation, FDH normalization,
or higher-topology subtraction.
"""
from __future__ import annotations

import sympy as sp
import massive_vector_generic_state_sum_symbolic as g


def main() -> None:
    ks = g.generic_kinematics(5)
    basis = g.massive_basis()

    checks = 0
    for h2 in (-1, +1):
        for h3 in (-1, +1):
            e2 = g.gluon_pol(2, h2, 5)
            e3 = g.gluon_pol(3, h3, 5)

            # Ordinary-gluon Ward identities for every massive-vector basis pair.
            for ea in basis:
                for eb in basis:
                    a2 = sp.simplify(g.base.amplitude(ks, [ea, ks[1], e3, eb]))
                    a3 = sp.simplify(g.base.amplitude(ks, [ea, e2, ks[2], eb]))
                    assert a2 == 0
                    assert a3 == 0
                    checks += 2

            # The two 4D-massive legs are 5D-null gauge bosons, so their parent
            # five-dimensional Ward identities must vanish as well.
            for eb in basis:
                a1 = sp.simplify(g.base.amplitude(ks, [ks[0], e2, e3, eb]))
                assert a1 == 0
                checks += 1
            for ea in basis:
                a4 = sp.simplify(g.base.amplitude(ks, [ea, e2, e3, ks[3]]))
                assert a4 == 0
                checks += 1

    assert checks == 96
    print(f"PASS: {checks} exact generic nonzero-mu external Ward identities")
    print("Tree engine: two cubic channels + quartic color-ordered contact term")
    print("Boundary: coupling/color/cut-orientation/FDH normalization remain separate")


if __name__ == "__main__":
    main()
