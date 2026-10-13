given_number = int(input("Enter a number: "))

if given_number < 0:
    print("Square root of negative numbers is not a real number.")
else:
    guess_number = 0
    while guess_number * guess_number < given_number:
        guess_number += 1

    if guess_number * guess_number == given_number:
        print(f"The square root of {given_number} is {guess_number}")
    else:
        print(f"{given_number} is not a perfect square.")