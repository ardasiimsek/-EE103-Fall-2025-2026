# Part 5: Binary conversion of 0.1 (stop when the error is acceptable)
num = 0.1
epsilon = 0.00001

frac_part = num
frac_binary = ""
result = 0          # decimal value of the binary digits found so far
place_value = 0.5   # 2^-1, 2^-2, ...

while abs(result - num) >= epsilon:
    frac_part *= 2
    bit = int(frac_part)
    frac_binary += str(bit)
    frac_part -= bit
    result += bit * place_value
    place_value /= 2

print(f"Binary representation of {num} is approximately 0.{frac_binary}")
print(f"This binary value equals {result} in decimal")
print(f"Error = {abs(result - num)}")
