def _gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return abs(a)


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        g = _gcd(numerator, denominator)
        numerator //= g
        denominator //= g

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        self.n = numerator
        self.d = denominator

    def __str__(self) -> str:
        return f"{self.n}/{self.d}"

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(
            self.n * other.d + other.n * self.d,
            self.d * other.d
        )

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(
            self.n * other.d - other.n * self.d,
            self.d * other.d
        )

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(
            self.n * other.n,
            self.d * other.d
        )

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.n == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction")
        return Fraction(
            self.n * other.d,
            self.d * other.n
        )

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        return self.n == other.n and self.d == other.d
