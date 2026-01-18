from math_toolkit.fraction import Fraction

def test_simplify():
    assert Fraction(4, 8) == Fraction(1, 2)

def test_negative_denominator():
    assert Fraction(1, -2) == Fraction(-1, 2)

def test_addition():
    assert Fraction(1, 3) + Fraction(1, 2) == Fraction(5, 6)

def test_divide_by_zero():
    try:
        Fraction(1, 2) / Fraction(0, 1)
        assert False
    except ZeroDivisionError:
        assert True