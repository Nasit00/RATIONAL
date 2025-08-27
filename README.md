Rational Numbers with GCD & LCM
📌 Overview

This project provides a Rational class to represent fractions with automatic simplification. It supports arithmetic operations, string formatting, and utilities for computing GCD and LCM. Helper functions gcd and lcm are implemented separately and used within the class. A UML diagram illustrates the design.

✨ Features

Automatic fraction simplification

Addition and subtraction of rationals

Safe denominator handling (no zero values)

GCD and LCM utilities for denominators

Readable string representation


🚀 Usage
from rational import Rational

r1 = Rational(1, 2)
r2 = Rational(3, 4)

print(r1 + r2)        # 5/4
print(r1 - r2)        # -1/4
print(r1.gcd_with(r2)) # 4
print(r1.lcm_with(r2)) # 4
