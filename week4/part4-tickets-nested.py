# Part 4: Guess and Check with nested loops
# Ben = Alyssa - 2, Cindy = 2 * Alyssa, total = 10
total = 10

for alyssa in range(total + 1):
    for ben in range(total + 1):
        for cindy in range(total + 1):
            if ben == alyssa - 2 and cindy == 2 * alyssa and alyssa + ben + cindy == total:
                print(f"Alyssa sold {alyssa}, Ben sold {ben}, Cindy sold {cindy}")
