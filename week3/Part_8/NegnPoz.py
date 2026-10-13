given_number = int(input("Enter an integer: "))

abs_number = abs(given_number)

guess_number = 0
while guess_number ** 3 < abs_number:
    guess_number += 1

if guess_number ** 3 == abs_number:
    if given_number < 0:
        guess_number = -guess_number
    print(f"The cube root of {given_number} is {guess_number}")
else:
    print(f"{given_number} is not a perfect cube.")