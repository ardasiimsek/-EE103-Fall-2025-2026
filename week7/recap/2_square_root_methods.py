# Recap 2: Square root of an input number with the three search methods
x = float(input("Enter a non-negative number to find its square root: "))
epsilon = 0.01

# ---------- 1) Guess and Check (integers only) ----------
guess = 0
while guess**2 < x:
    guess += 1
if guess**2 == x:
    print(f"[Guess and Check] {x} is a perfect square, square root = {guess}")
else:
    print(f"[Guess and Check] {x} is not a perfect square (no integer root found)")

# ---------- 2) Approximation Method ----------
guess = 0.0
increment = 0.0001
num_guesses = 0
# guess**2 <= x stops the loop if we overshoot (avoids an infinite loop)
while abs(guess**2 - x) >= epsilon and guess**2 <= x:
    guess += increment
    num_guesses += 1
if abs(guess**2 - x) >= epsilon:
    print(f"[Approximation] Failed on square root of {x}")
else:
    print(f"[Approximation] {guess:.4f} is close to the square root of {x} "
          f"({num_guesses} guesses)")

# ---------- 3) Bisection Search ----------
low = 0.0
high = max(1.0, x)          # for 0 < x < 1 the root is bigger than x
guess = (low + high) / 2
num_guesses = 0
while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2
    num_guesses += 1
print(f"[Bisection] {guess:.4f} is close to the square root of {x} "
      f"({num_guesses} guesses)")
