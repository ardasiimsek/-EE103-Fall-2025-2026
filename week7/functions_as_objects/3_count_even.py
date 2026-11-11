# Functions as objects - Task 3: count_even takes a function as input
def is_even_or_odd(number):
    if type(number) is not int:
        return "unknown"
    if number % 2 == 0:
        return "even"
    return "odd"


def count_even(check_function, n):
    count = 0                                # a. start from count = 0
    for i in range(n):                       # b. loop over range(n)
        if check_function(i) == "even":      # c. check if the index is even or odd
            count += 1                       # d. increment if even
    return count                             # e. return the count


print("count_even(is_even_or_odd, 5) =", count_even(is_even_or_odd, 5))    # 3 -> 0, 2, 4
print("count_even(is_even_or_odd, 10) =", count_even(is_even_or_odd, 10))  # 5
