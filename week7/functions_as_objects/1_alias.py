# Functions as objects - Task 1: alias of is_even_or_odd
def is_even_or_odd(number):
    if type(number) is not int:
        return "unknown"
    if number % 2 == 0:
        return "even"
    return "odd"


# A function is an object, so we can bind another name to the same object
is_even_or_odd_alias = is_even_or_odd

print(is_even_or_odd)          # <function is_even_or_odd at 0x...>
print(is_even_or_odd_alias)    # same object, same address
print("Same object?", is_even_or_odd_alias is is_even_or_odd)

for value in [10, 3, 2.5]:
    print(f"{value}: original -> {is_even_or_odd(value)}, "
          f"alias -> {is_even_or_odd_alias(value)}")
