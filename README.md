# RATIONAL
Rational Numbers with GCD & LCM
Overview

This project implements a simple Rational Number class in Python, along with helper functions for GCD (Greatest Common Divisor) and LCM (Least Common Multiple). The class ensures fractions are always stored in reduced form and supports arithmetic operations.

Features

✅ Compute GCD using recursion

✅ Compute LCM from GCD

✅ Represent fractions as Rational(numerator, denominator)

✅ Automatic fraction simplification

✅ Addition and subtraction of rational numbers

✅ String representation ("numerator/denominator")

Example Usage
from rational import Rational

# Create rationals
r1 = Rational(1, 2)   # 1/2
r2 = Rational(3, 4)   # 3/4

# Arithmetic
print(r1 + r2)   # 5/4
print(r1 - r2)   # -1/4

# GCD & LCM with denominators
print(r1.gcd_with(r2))  # 4
print(r1.lcm_with(r2))  # 4


✅ Utilities to compute GCD/LCM of denominators
