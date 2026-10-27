# Part 3: Demonstrate floating error
x = 0
for i in range(10):
    x += 0.1

print(f"x = {x}")
if x == 1.0:
    print("x is equal to 1.0")
else:
    print("x is NOT equal to 1.0")
