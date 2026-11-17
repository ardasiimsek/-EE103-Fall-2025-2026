# Mutability: Lists vs. Tuples
my_list = [1, 3, 5]
my_tuple = (1, 3, 5)

my_list[1] = 5
print(my_list)   # [1, 5, 5] -> lists are mutable, they can be changed in place

try:
    my_tuple[1] = 5
except TypeError as e:
    print(f"TypeError: {e}")
# 'tuple' object does not support item assignment
# Tuples are immutable: once created, their elements cannot be changed.
# To "change" one you have to build a new tuple:
my_tuple = my_tuple[:1] + (5,) + my_tuple[2:]
print(my_tuple)  # (1, 5, 5) -> this is a NEW tuple object
