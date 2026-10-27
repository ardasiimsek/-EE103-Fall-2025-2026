# Tasks Part 1: Approximation methods - square root problem
x = float(input("Enter a number to find its square root: "))

epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001

# guess**2 <= x stops the loop if we overshoot (avoids an infinite loop)
while abs(guess**2 - x) >= epsilon and guess**2 <= x:
    guess += increment
    num_guesses += 1
    if num_guesses % 1000 == 0:
        print('Current guess =', guess)

print(f"Number of guesses = {num_guesses}")
if abs(guess**2 - x) >= epsilon:
    print(f"Failed on square root of {x}")
else:
    print(f"{guess} is close to the square root of {x}")
