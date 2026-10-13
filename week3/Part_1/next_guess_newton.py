x = float(input("Enter the number for which you want to find the cube root: "))
guess = float(input("Enter your initial guess: "))
next_guess = float(guess - (guess**3 - x) / (3 * guess**2))
print("The next guess for the cube root of", x, "is:", next_guess)