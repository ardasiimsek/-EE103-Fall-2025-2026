# Part 4: Binary conversion (fractions)
num = float(input("Enter a number to find its binary representation (e.g. 13.375): "))

int_part = int(num)
frac_part = num - int_part

# Integer part: divide by 2 and save the remainder
if int_part == 0:
    int_binary = "0"
else:
    int_binary = ""
    n = int_part
    while n > 0:
        int_binary = str(n % 2) + int_binary
        n = n // 2

# Fraction part: multiply by 2 and save the integer part
frac_binary = ""
max_digits = 32  # stop if the fraction never becomes 0 (e.g. 0.1)
while frac_part > 0 and len(frac_binary) < max_digits:
    frac_part *= 2
    bit = int(frac_part)
    frac_binary += str(bit)
    frac_part -= bit

if frac_binary == "":
    print(f"Binary representation of {num} is {int_binary}")
else:
    print(f"Binary representation of {num} is {int_binary}.{frac_binary}")
