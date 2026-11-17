target = 0.1
epsilon = 0.00001

f = target
binary = "0."
result = 0
place = 0.5

while abs(result - target) >= epsilon:
    f = f * 2
    digit = int(f)
    binary = binary + str(digit)
    result = result + digit * place
    f = f - digit
    place = place / 2

print(f"{target} in binary is about {binary}")
print(f"which equals {result}, error = {abs(result - target)}")
