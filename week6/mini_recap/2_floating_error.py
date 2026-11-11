# Mini Recap - Demonstrate floating point error
x = 0.1                                         # 1)
y = 0.2
result = x + y                                  # 2)

print("result =", result)                       # 0.30000000000000004
print("result == 0.3 ?", result == 0.3)         # 3) False -> floating error

close_enough = 0.3 - 1e-4 <= result <= 0.3 + 1e-4
print("Close enough to 0.3 ?", close_enough)    # 4) True
