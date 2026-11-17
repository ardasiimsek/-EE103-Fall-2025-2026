x = 1
y = 2
x = y
y = x
print(f"Naive swap: x = {x}, y = {y}")

x = 1
y = 2
temp = x
x = y
y = temp
print(f"Temp swap:  x = {x}, y = {y}")

x = 1
y = 2
(x, y) = (y, x)
print(f"Tuple swap: x = {x}, y = {y}")
