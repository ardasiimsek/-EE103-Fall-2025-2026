total = 0
dummy_range = range(10)

dummy_list_1 = list(dummy_range)

dummy_list_2 = []
for i in range(10):
    dummy_list_2.append(i)

print(dummy_list_1)
print(dummy_list_2)
print(f"Equal: {dummy_list_1 == dummy_list_2}")

for value in dummy_list_1:
    total += value
print(f"Sum = {total}")
