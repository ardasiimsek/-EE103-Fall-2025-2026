import time

total = 1000

start = time.time()
for alyssa in range(total + 1):
    for ben in range(total + 1):
        cindy = total - alyssa - ben
        if ben == alyssa - 20 and cindy == 2 * alyssa:
            print(f"Nested: Alyssa sold {alyssa}, Ben sold {ben}, Cindy sold {cindy}")
nested_time = time.time() - start
print(f"Nested loops took {nested_time:.4f} seconds")

start = time.time()
for alyssa in range(total + 1):
    ben = alyssa - 20
    cindy = 2 * alyssa
    if ben >= 0 and alyssa + ben + cindy == total:
        print(f"Single: Alyssa sold {alyssa}, Ben sold {ben}, Cindy sold {cindy}")
single_time = time.time() - start
print(f"Single loop took {single_time:.4f} seconds")
