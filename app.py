from Rational_class.Class import Rational
class App:
    def run(self):
        r1 = Rational(1, 2)
        r2 = Rational(3, 4)
        print(r1 + r2)
        print(r1 - r2)
        print("GCD of denominators:", r1.gcd_with(r2))
        print("LCM of denominators:", r1.lcm_with(r2))