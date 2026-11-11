# Newton-Raphson: square root of secret_number
# Root of p(x) = x**2 - secret_number is sqrt(secret_number), p'(x) = 2x
# Better guess: g - p(g) / p'(g)
from secret_data import secret_number

epsilon = 0.01
guess = secret_number / 2
num_guesses = 0

while abs(guess * guess - secret_number) >= epsilon:
    guess = guess - (guess**2 - secret_number) / (2 * guess)
    num_guesses += 1

print(f"Number of guesses = {num_guesses}")
print(f"Square root of {secret_number} is about {guess:.4f}")
