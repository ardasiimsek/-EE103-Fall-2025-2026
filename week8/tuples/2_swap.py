# Tuples: Swap variables

# 1) x = y then y = x -> does NOT work
x = 1
y = 2
x = y      # x is now 2, the old value 1 is lost
y = x      # y gets 2 as well
print(f"Naive swap: x = {x}, y = {y}")   # x = 2, y = 2

# 2) With a temporary variable -> works
x = 1
y = 2
temp = x
x = y
y = temp
print(f"Temp swap:  x = {x}, y = {y}")   # x = 2, y = 1

# 3) Tuple swap -> works, the right side (y, x) is built first, then unpacked
x = 1
y = 2
(x, y) = (y, x)
print(f"Tuple swap: x = {x}, y = {y}")   # x = 2, y = 1
