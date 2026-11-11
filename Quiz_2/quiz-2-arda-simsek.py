cube = int(input("Enter a positive integer: "))

for guess in range(cube + 1):
    if guess ** 3 == cube:
        print(f"Cube root of {cube} is {guess}")
        break
else:
    print(f"{cube} is not a perfect cube")