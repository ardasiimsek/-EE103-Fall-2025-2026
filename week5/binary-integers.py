# Part 2: Binary conversion (integers)
num = int(input("Enter an integer to find its binary representation: "))

if num == 0:
    binary = "0"
else:
    is_negative = num < 0
    n = abs(num)
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    if is_negative:
        binary = "-" + binary

print(f"Binary representation of {num} is {binary}")
