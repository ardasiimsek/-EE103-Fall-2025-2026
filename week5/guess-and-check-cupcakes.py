# Guess & Check: David, Emma and Frank packing cupcakes
total_cupcakes = 28
found = False

for david in range(total_cupcakes + 1):
    for emma in range(total_cupcakes + 1):
        for frank in range(total_cupcakes + 1):
            if emma == david + 3 and frank == 3 * david and david + emma + frank == total_cupcakes:
                print(f"David packed {david} cupcakes!")
                print(f"Emma packed {emma} cupcakes!")
                print(f"Frank packed {frank} cupcakes!")
                found = True
                break
        if found:
            break
    if found:
        break

if not found:
    print("No solution found.")
