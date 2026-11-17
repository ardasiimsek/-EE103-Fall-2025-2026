product = 1
for i in range(7, 19):
    product *= i
print(f"Product of integers from 7 to 18: {product}")

s = "abcabc"
seen = ""
for ch in s:
    if ch not in seen:
        seen = seen + ch

print(len(seen))
