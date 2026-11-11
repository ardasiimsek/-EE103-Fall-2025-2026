def binary_convertor(number):
    """Returns the binary representation of a non-negative integer as a string."""
    if number == 0:
        return "0"
    binary = ""
    while number > 0:
        remainder = number % 2          # save the remainder
        binary = str(remainder) + binary
        number = number // 2            # divide by 2
    return binary


if __name__ == "__main__":
    for value in [13, 0, 1, 8, 255]:
        print(f"{value} -> {binary_convertor(value)}   (check: {bin(value)[2:]})")
