# Recap 3: Apply a function twice
from math import sqrt


def f_x_twice(x, f_x):
    return f_x(f_x(x))


print(f_x_twice(16, sqrt))              # sqrt(sqrt(16)) = sqrt(4) = 2.0
print(f_x_twice(2, lambda x: x ** 2))   # (2^2)^2 = 4^2 = 16
