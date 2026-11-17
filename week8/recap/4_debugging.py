# Recap 4: Using the 3 debugging tools on the functions above
#   1) print debugging   -> set DEBUG = True to see intermediate values
#   2) pdb               -> uncomment the pdb line, then use n, s, p <var>, c, q
#   3) VSCode debugger   -> click left of a line number to add a red breakpoint,
#                           press F5 and watch variables in the Variables panel

DEBUG = False


def estimate_derivative(func, x, h=1e-5):
    forward = func(x + h)
    backward = func(x - h)
    if DEBUG:
        print(f"[debug] f(x+h) = {forward}, f(x-h) = {backward}")
    return (forward - backward) / (2 * h)


def integrate(func, steps=1000):
    total_area = 0
    dx = 1 / steps
    for i in range(steps):
        x_i = (i + 0.5) * dx
        # import pdb; pdb.set_trace()   # tool 2: stops here every iteration
        total_area += func(x_i) * dx
        if DEBUG and i < 3:
            print(f"[debug] i = {i}, x_i = {x_i}, total_area = {total_area}")
    return total_area


def f_x_twice(x, f_x):
    once = f_x(x)          # tool 3: put a VSCode breakpoint here
    return f_x(once)


print(estimate_derivative(lambda x: x ** 2, 3))
print(integrate(lambda x: x ** 2))
print(f_x_twice(2, lambda x: x ** 2))
