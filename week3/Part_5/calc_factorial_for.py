x = float(input("Enter a number to calculate its factorial: "))
result = 1
for i in range(1, int(x) + 1):
    result *= i
print(f"The factorial of {int(x)} is {result}.")
