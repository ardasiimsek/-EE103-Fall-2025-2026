x = int(input("Enter a number to calculate its factorial: "))
result = 1
while x > 0:
    result *= x
    x -= 1
print(f"The factorial is {result}.")