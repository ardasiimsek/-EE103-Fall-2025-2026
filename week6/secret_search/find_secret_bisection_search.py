# Bisection Search: find the secret year (between 0 and 2026)
from secret_data import secret_year       # a. import the secret year

num_guesses = 1                           # b. the first guess counts too
low = 0
high = 2026
guess = (low + high) // 2

while guess != secret_year:               # c.
    if guess < secret_year:               # i. answer is in the upper half
        low = guess + 1
    else:                                 #    answer is in the lower half
        high = guess - 1
    guess = (low + high) // 2             # ii. integer mean of the bounds
    num_guesses += 1                      # iii.

print(f"Found the secret year: {guess}")  # d.
print(f"Number of guesses = {num_guesses}")
