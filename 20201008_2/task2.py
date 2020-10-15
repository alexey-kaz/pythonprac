from fractions import Fraction as F


def is_root_frac(a):
    a = a.split(', ')
    s, w, pA = F(a[0]), F(a[1]), int(a[2])
    pB = int(a[4 + pA])
    cA = [F(c) for c in a[3:4 + pA]]
    cB = [F(c) for c in a[5 + pA:6 + pA + pB]]
    s1 = sum(c * s ** (len(cA) - i - 1) for i, c in enumerate(cA))
    s2 = sum(c * s ** (len(cB) - i - 1) for i, c in enumerate(cB))
    return s2 * w == s1


def is_root_float(a):
    a = a.split(', ')
    s, w, pA = float(F(a[0])), float(F(a[1])), int(a[2])
    pB = int(a[4 + pA])
    cA = [float(F(c)) for c in a[3:4 + pA]]
    cB = [float(F(c)) for c in a[5 + pA:6 + pA + pB]]
    s1 = sum(c * s ** (len(cA) - i - 1) for i, c in enumerate(cA))
    s2 = sum(c * s ** (len(cB) - i - 1) for i, c in enumerate(cB))
    return s2 * w == s1
