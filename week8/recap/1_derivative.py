# Recap 1: Numerical derivative with the central difference formula
# f'(x) ~ (f(x + h) - f(x - h)) / (2h)


def estimate_derivative(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)


def take_square(x):
    return x ** 2


# take_square passed as a function object -> should give ~2x
for x in [0, 1, 2.5, 10]:
    print(f"x = {x}: derivative ~ {estimate_derivative(take_square, x):.6f}, 2x = {2 * x}")

# Same demonstration with a lambda function
square_lambda = lambda x: x ** 2
for x in [0, 1, 2.5, 10]:
    print(f"(lambda) x = {x}: derivative ~ {estimate_derivative(square_lambda, x):.6f}, 2x = {2 * x}")
