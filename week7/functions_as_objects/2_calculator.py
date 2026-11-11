# Functions as objects - Task 2: calculator that takes a function as input
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculator(operation, x, y):
    """Calls the given operation (a function object) with x and y."""
    return operation(x, y)


x, y = 3, 5
for op in [add, subtract, multiply, divide]:
    print(f"calculator({op.__name__}, {x}, {y}) = {calculator(op, x, y)}   |   "
          f"{op.__name__}({x}, {y}) = {op(x, y)}   |   "
          f"same: {calculator(op, x, y) == op(x, y)}")
