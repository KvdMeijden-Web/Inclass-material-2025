import random


guess_computer = random.randint(1, 100)
game_on = True
counter = 0

while game_on:
    guess_user= int(input("Guess a number between 1 and 100: "))
    counter = counter + 1
    if guess_user < guess_computer:
        print("Too low, try again.")
    elif guess_user > guess_computer:
        print("Too high, try again.")
    else:
        print("Congratulations! You've guessed the number:", guess_computer, ",\n it took you ", counter," tries")
        game_on = False