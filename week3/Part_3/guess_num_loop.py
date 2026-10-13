from secret_number import secretNum
guess = 0
while guess != secretNum:
    guess = float(input("Guess a number between 1 and 10: "))
    if guess == secretNum:
        print("You guessed it!")
    elif guess < secretNum:
        print("Your guess is too low!")
    else:
         print("Your guess is too high!")