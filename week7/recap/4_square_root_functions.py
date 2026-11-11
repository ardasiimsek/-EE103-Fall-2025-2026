# Recap 4: Three square root functions, one for each search method
def sqrt_guess_and_check(x):
    """Guess and Check: tries integers 0, 1, 2, ...
    Returns the exact integer root for perfect squares, otherwise the
    closest integer estimate."""
    guess = 0
    while guess**2 < x:
        guess += 1
    # now guess**2 >= x; pick whichever of guess-1 / guess is closer
    if guess > 0 and abs((guess - 1)**2 - x) < abs(guess**2 - x):
        return guess - 1
    return guess


def sqrt_approximation(x, epsilon=0.01, increment=0.0001):
    """Approximation Method: increase guess by a small step until close enough."""
    guess = 0.0
    while abs(guess**2 - x) >= epsilon and guess**2 <= x:
        guess += increment
    return guess


def sqrt_bisection(x, epsilon=0.01):
    """Bisection Search: halve the interval [low, high] every step."""
    low = 0.0
    high = max(1.0, x)
    guess = (low + high) / 2
    while abs(guess**2 - x) >= epsilon:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    return guess


for number in [25, 2, 0.25, 1000]:
    print(f"x = {number}")
    print("  Guess and Check :", sqrt_guess_and_check(number))
    print("  Approximation   :", round(sqrt_approximation(number), 4))
    print("  Bisection       :", round(sqrt_bisection(number), 4))
    print("  Real value      :", round(number**0.5, 4))
