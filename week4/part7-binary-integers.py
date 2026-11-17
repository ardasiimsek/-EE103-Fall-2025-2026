# Part 7: Binary conversion (integers)
num = int(input("Enter an integer: "))

if num == 0:
    binary = "0"
else:
    n = abs(num)
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary  # adding to the front reverses the order
        n = n // 2
    if num < 0:
        binary = "-" + binary

print(f"{num} converted to binary is {binary}")
