# Tasks Part 2: Bisection search - guess the favorite page (1..148)
# Instead of trying pages one by one, always guess the middle of the
# remaining range and throw away the half that cannot contain the page.
low = 1
high = 148
num_guesses = 0

print(f"Think of a page between {low} and {high}.")
while low <= high:
    guess = (low + high) // 2
    num_guesses += 1
    answer = input(f"Is it {guess}? Enter 'h' (higher), 's' (smaller) or 'c' (correct): ")
    if answer == 'c':
        print(f"Found your favorite page {guess} in {num_guesses} guesses!")
        break
    elif answer == 'h':
        low = guess + 1
    elif answer == 's':
        high = guess - 1
    else:
        print("Please enter h, s or c.")
        num_guesses -= 1
else:
    print("Your answers were inconsistent, no page left to guess.")
