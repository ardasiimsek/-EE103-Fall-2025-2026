# Debugging - Part 1: debugging with print statements
def count_evens(input_n):
    count = 0
    for num in range(input_n):
        # DEBUG PRINT: Watch the current number and running count
        print(f"[DEBUG] Checking num = {num}, Current count = {count}")
        if num % 2 == 0:
            count += 1
            print(f"[DEBUG] -> {num} is EVEN! Updated count = {count}")
    return count


print("Total evens:", count_evens(5))
