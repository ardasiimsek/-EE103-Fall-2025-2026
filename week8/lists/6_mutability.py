my_list = [1, 3, 5]
my_tuple = (1, 3, 5)

my_list[1] = 5
print(my_list)

try:
    my_tuple[1] = 5
except TypeError as e:
    print(f"TypeError: {e}")
my_tuple = my_tuple[:1] + (5,) + my_tuple[2:]
print(my_tuple)
