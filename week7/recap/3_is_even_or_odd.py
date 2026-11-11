# Recap 3: is_even_or_odd function
def is_even_or_odd(number):
    """Returns 'even' or 'odd' for an integer input, 'unknown' for any other type."""
    # type(...) is int -> floats, strings, bools etc. are rejected
    if type(number) is not int:
        return "unknown"
    if number % 2 == 0:
        return "even"
    return "odd"


print(is_even_or_odd(4))      # even
print(is_even_or_odd(7))      # odd
print(is_even_or_odd(-3))     # odd
print(is_even_or_odd(4.0))    # unknown
print(is_even_or_odd("12"))   # unknown
