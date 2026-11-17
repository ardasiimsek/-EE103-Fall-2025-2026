# Part 8: Binary conversion of fractions (0 <= F < 1)
f = float(input("Enter a fraction between 0 and 1 (e.g. 0.375): "))
max_digits = 20  # stop here if the fraction never becomes exactly 0

binary = "0."
count = 0
while f != 0 and count < max_digits:
    f = f * 2
    digit = int(f)
    binary = binary + str(digit)
    f = f - digit
    count += 1

if f != 0:
    print(f"Binary (first {max_digits} digits, not exact): {binary}...")
else:
    print(f"Binary: {binary}")
