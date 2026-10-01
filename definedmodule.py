# ==========================================
# Python Modules and Functions
# ==========================================

# User-defined module functions
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


# Using user-defined functions
print("=== User-Defined Module ===")
print("Addition:", add(5, 3))
print("Multiplication:", multiply(4, 2))


# ==========================================
# Reduce Function
# ==========================================

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print("\n=== Reduce Function ===")
print("Sum using reduce:", result)


# ==========================================
# Built-in Module: math
# ==========================================

import math

num = 16

print("\n=== Math Module ===")
print("Square root:", math.sqrt(num))
print("Factorial:", math.factorial(5))
print("Power:", math.pow(2, 3))
print("Log:", math.log(10))


# ==========================================
# Built-in Module: statistics
# ==========================================

import statistics

data = [10, 20, 20, 30]

print("\n=== Statistics Module ===")
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))