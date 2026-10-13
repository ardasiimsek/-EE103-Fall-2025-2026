n = int(input("Enter a number: "))
total = 0
expression = ""
for i in range(1, n + 1):
    total += i
    if i < n:
        expression += f"{i}+"
    else:
        expression += f"{i}"

print(f"sum = {expression}={total}")


sum_gauss = n * (n + 1) // 2
print(f"sum_gauss = {sum_gauss}")

if total == sum_gauss:
    print("My running sum code works correctly")
else:
    print("My running sum code failed badly")