# Recap 1 – Search Algorithms

## Guess and Check (Exhaustive Enumeration)
**Idea:** Try every possible candidate one by one and check whether it satisfies the condition.

- **Example task:** Find the integer cube root of 27.
- **Solution approach:** Try `guess = 0, 1, 2, 3, ...`. For each guess check `guess**3 == 27`.
  Stop at `guess = 3`. If `guess**3` passes 27 without a match, the number is not a perfect cube.
- **Pros / cons:** Simple and always correct for a finite/discrete search space, but slow and
  only works when the answer is one of the candidates (e.g. integers).

## Approximation Method
**Idea:** Start from a small guess and increase it by a tiny `increment` until the answer is
"close enough" (`abs(guess**2 - x) < epsilon`).

- **Example task:** Find the square root of 25 with `epsilon = 0.01`.
- **Solution approach:** `guess = 0.0`, `increment = 0.0001`. While `abs(guess**2 - 25) >= epsilon`,
  increase `guess` by `increment`. Stop when close enough (≈ 4.999). Also stop if `guess**2 > x`
  (overshoot), otherwise the loop may never end.
- **Pros / cons:** Works for real (non-integer) answers, but needs very many steps
  (~sqrt(x) / increment) and the accuracy depends on `epsilon` and `increment`.

## Bisection Search
**Idea:** The answer lies in an interval `[low, high]`. Check the middle point and throw away the
half that cannot contain the answer. Repeat until close enough.

- **Example task:** Find the square root of 25 with `epsilon = 0.01`.
- **Solution approach:** `low = 0`, `high = 25`, `guess = (low + high) / 2 = 12.5`.
  `12.5**2 > 25` → the answer is in the lower half, so `high = 12.5`. New guess `6.25` → `high = 6.25`.
  New guess `3.125` → `3.125**2 < 25` → `low = 3.125` ... continue until `abs(guess**2 - 25) < epsilon`.
- **Pros / cons:** Very fast (the search space halves every step → about `log2(range / epsilon)` steps),
  but the problem must be ordered/monotonic (larger guess → larger `guess**2`).
