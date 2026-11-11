# Approximation method: square root of secret_number
from secret_data import secret_number

epsilon = 0.01
increment = 0.0001
guess = 0.0
num_guesses = 0

# guess**2 <= secret_number stops the loop if we overshoot
while abs(guess**2 - secret_number) >= epsilon and guess**2 <= secret_number:
    guess += increment
    num_guesses += 1

print(f"Number of guesses = {num_guesses}")
if abs(guess**2 - secret_number) >= epsilon:
    print(f"Failed on square root of {secret_number} (last guess {guess:.4f})")
else:
    print(f"{guess:.4f} is close to the square root of {secret_number}")
