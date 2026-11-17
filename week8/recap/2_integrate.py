def integrate(func, steps=1000):
    total_area = 0
    dx = 1 / steps
    for i in range(steps):
        x_i = (i + 0.5) * dx
        total_area += func(x_i) * dx
    return total_area


print(f"integral of x^2 from 0 to 1 ~ {integrate(lambda x: x ** 2):.6f} (exact 1/3)")
print(f"integral of x from 0 to 1   ~ {integrate(lambda x: x):.6f} (exact 0.5)")
print(f"integral of 1 from 0 to 1   ~ {integrate(lambda x: 1):.6f} (exact 1)")
