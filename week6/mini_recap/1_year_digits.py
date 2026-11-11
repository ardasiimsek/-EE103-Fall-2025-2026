# Mini Recap - Basics syntaxing
# 1) Ask the user for a year and cast it to an integer
year = int(input("What year is this? "))

# 2) Extract each digit, cast it to int and sum them with a for loop
digit_sum = 0
for digit in str(year):
    digit_sum += int(digit)
print(f"Sum of the digits of {year} = {digit_sum}")

# 3) Divide the sum by the number of digits
num_digits = len(str(year))
average = digit_sum / num_digits
print(f"Sum / number of digits = {digit_sum} / {num_digits} = {average}")
