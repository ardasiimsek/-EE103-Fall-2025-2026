# Bisection search: square root of secret_number
from secret_data import secret_number

epsilon = 0.01
low = 0.0
high = max(1.0, secret_number)     # for numbers < 1 the root is bigger than the number
guess = (low + high) / 2
num_guesses = 1

while abs(guess**2 - secret_number) >= epsilon:
    if guess**2 < secret_number:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2
    num_guesses += 1

print(f"Number of guesses = {num_guesses}")
print(f"{guess:.4f} is close to the square root of {secret_number}")
