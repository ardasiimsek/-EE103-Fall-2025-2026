# Lambda Functions - Task 3: add/subtract/multiply/divide as lambdas
def calculator(operation, x, y):
    return operation(x, y)


add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b

x, y = 3, 5
print("Named lambdas:")
print("  calculator(add, 3, 5)      =", calculator(add, x, y), "| add(3, 5) =", add(x, y))
print("  calculator(subtract, 3, 5) =", calculator(subtract, x, y), "| subtract(3, 5) =", subtract(x, y))
print("  calculator(multiply, 3, 5) =", calculator(multiply, x, y), "| multiply(3, 5) =", multiply(x, y))
print("  calculator(divide, 3, 5)   =", calculator(divide, x, y), "| divide(3, 5) =", divide(x, y))

# Lambdas passed directly to the calculator, without binding a name
print("Anonymous lambdas passed directly:")
print("  add      :", calculator(lambda a, b: a + b, x, y))
print("  subtract :", calculator(lambda a, b: a - b, x, y))
print("  multiply :", calculator(lambda a, b: a * b, x, y))
print("  divide   :", calculator(lambda a, b: a / b, x, y))
