# Brainstorm & Comparison

## Brainstorm
**Feedback is only "correct / not correct":** Bisection search can **not** be used.
A wrong guess tells us nothing about which half the secret year is in, so we cannot
throw away half of the range. The only option is guess-and-check (try every year).

**Feedback is "higher / lower":** Bisection search **can** be used. After each guess we know
whether the secret is above or below it, so half of the remaining range is discarded each time.
For 2027 possible years this needs at most ⌈log2(2027)⌉ = 11 guesses.

## Secret year = 2020
| Method | Number of guesses |
|---|---|
| Guess and Check (`find_secret_guess_and_check.py`) | 2021 |
| Bisection Search (`find_secret_bisection_search.py`) | 11 |

Bisection search is far more efficient.

## Square root of secret_number = 54321 (epsilon = 0.01)
| Method | Number of guesses | Result |
|---|---|---|
| Approximation (`sqrt_approximation.py`, increment 0.0001) | 2 330 687 | **Failed** (stepped over the answer) |
| Bisection Search (`sqrt_bisection_search.py`) | 31 | 233.0687 |
| Newton-Raphson (`newton-raphson.py`) | 10 | 233.0687 |

The approximation method is extremely slow, and here it even fails: near 233 one step of
0.0001 changes `guess**2` by about 0.047, which is larger than the 2 * epsilon window, so the
loop jumps over the answer. Bisection is much more efficient, and Newton-Raphson is the fastest.
