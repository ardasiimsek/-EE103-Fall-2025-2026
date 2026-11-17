# Part 6: Floating point error
x = 0
for i in range(10):
    x = x + 0.1
print(x)  # 0.9999999999999999

# Why?
# Computers store floats in binary. 0.1 in binary is 0.000110011001100...
# (repeats forever), so it can only be stored approximately.
# Each addition carries that tiny error and after 10 additions it adds up,
# so the result is not exactly 1.
print(f"{0.1:.20f}")  # shows the real stored value of 0.1

# So never compare floats with ==, check if they are close enough instead
if abs(x - 1) < 1e-9:
    print("x is close enough to 1")
