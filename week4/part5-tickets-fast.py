# Part 5: Ben = Alyssa - 20, Cindy = 2 * Alyssa, total = 1000
import time

total = 1000

# Nested loops: try every (alyssa, ben) pair, cindy is whatever is left.
# Three nested loops would be ~10^9 checks and take far too long in Python,
# even two loops already means ~10^6 checks.
start = time.time()
for alyssa in range(total + 1):
    for ben in range(total + 1):
        cindy = total - alyssa - ben
        if ben == alyssa - 20 and cindy == 2 * alyssa:
            print(f"Nested: Alyssa sold {alyssa}, Ben sold {ben}, Cindy sold {cindy}")
nested_time = time.time() - start
print(f"Nested loops took {nested_time:.4f} seconds")

# Single loop: Ben and Cindy are fully determined by Alyssa,
# so we only need to guess Alyssa (~10^3 checks).
start = time.time()
for alyssa in range(total + 1):
    ben = alyssa - 20
    cindy = 2 * alyssa
    if ben >= 0 and alyssa + ben + cindy == total:
        print(f"Single: Alyssa sold {alyssa}, Ben sold {ben}, Cindy sold {cindy}")
single_time = time.time() - start
print(f"Single loop took {single_time:.4f} seconds")
