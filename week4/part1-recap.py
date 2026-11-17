# Part 1: Recap

# User Input, Type Casting & String Formatting
std_num = int(input("Enter your student number: "))
print(f"Hello, my student number is {std_num}!")

# String Manipulation & Slicing
name_lower = "name"
print(name_lower.upper())
print(name_lower[::-1])

# User Input with Floats & Basic Arithmetic
this_year = 2026
this_year = str(this_year)
first_two = this_year[:2]
last_two = this_year[2:]

first_two = float(first_two)
last_two = float(last_two)

mysum = first_two + last_two
print(f"{mysum:.2f}")

if mysum == 46:
    print("Correct")
else:
    print("Wrong")
