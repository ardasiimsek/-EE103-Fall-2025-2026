x = 0
for i in range(10):
    x = x + 0.1
print(x)

print(f"{0.1:.20f}")

if abs(x - 1) < 1e-9:
    print("x is close enough to 1")
