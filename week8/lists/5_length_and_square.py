def length_and_square(L):
    """ L is a list of numbers
    Return a tuple where the first value is the length of L and the second
    value is a list of same length of L but the values are the square of the
    values in L; e.g. if L = [1,3,5] then the function should return (3, [1,9,25]) """
    squares = []
    for x in L:
        squares.append(x ** 2)
    return (len(L), squares)


print(length_and_square([1, 3, 5]))
print(length_and_square([]))
