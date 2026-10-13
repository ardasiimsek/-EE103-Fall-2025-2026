from secret_number import secretNum
count = 0
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    count += 1

    if guess == secretNum:
        print("You guessed it!")
        break                      

    elif guess < secretNum:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")

    if count == 5:             
        break                      
if guess != secretNum:
    while True:
        print("Oh! Noooooo…")