# Guess and Check: find the secret year (between 0 and 2026)
from secret_data import secret_year

num_guesses = 0
for guess in range(0, 2027):
    num_guesses += 1
    if guess == secret_year:
        print(f"Found the secret year: {guess}")
        break

print(f"Number of guesses = {num_guesses}")
