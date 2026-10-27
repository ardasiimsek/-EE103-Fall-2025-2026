# Multiply - all - 1 (for loop)
start = int(input("Enter a start number: "))
end = int(input("Enter an end number: "))

result_for = 1
for i in range(start, end + 1):
    result_for *= i
print(f"Result with for loop: {result_for}")

# Multiply - all - 2 (while loop)
result_while = 1
i = start
while i <= end:
    result_while *= i
    i += 1
print(f"Result with while loop: {result_while}")

# Sanity check
if result_for == result_while:
    print("results are same")
else:
    print("results are different")
