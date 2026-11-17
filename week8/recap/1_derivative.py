def estimate_derivative(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)


def take_square(x):
    return x ** 2


for x in [0, 1, 2.5, 10]:
    print(f"x = {x}: derivative ~ {estimate_derivative(take_square, x):.6f}, 2x = {2 * x}")

square_lambda = lambda x: x ** 2
for x in [0, 1, 2.5, 10]:
    print(f"(lambda) x = {x}: derivative ~ {estimate_derivative(square_lambda, x):.6f}, 2x = {2 * x}")
