#part 2
"""product = 1
for i in range(7, 19):
    product *= i
print(product)  """
#part 3
s = "abadmanajnamdsde"
seen =0          
for ch in s:              
    if ch not in seen:        
        seen =seen +ch     

print(len(seen))