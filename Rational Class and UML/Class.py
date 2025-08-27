def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    """Least Common Multiple."""
    return abs(a * b) // gcd(a, b)


class Rational:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        common = gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // common
        self.denominator = denominator // common

        # keep denominator positive
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __add__(self, other):
        if isinstance(other, Rational):
            new_num = self.numerator * other.denominator + other.numerator * self.denominator
            new_den = self.denominator * other.denominator
            return Rational(new_num, new_den)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Rational):
            new_num = self.numerator * other.denominator - other.numerator * self.denominator
            new_den = self.denominator * other.denominator
            return Rational(new_num, new_den)
        return NotImplemented

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def gcd_with(self, other):
        """Return GCD of denominators with another Rational."""
        if isinstance(other, Rational):
            return gcd(self.denominator, other.denominator)
        return NotImplemented

    def lcm_with(self, other):
        """Return LCM of denominators with another Rational."""
        if isinstance(other, Rational):
            return lcm(self.denominator, other.denominator)
        return NotImplemented