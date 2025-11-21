import random
print("Welcome to the Guess the Number Game!")
computer_number = random.randint(1, 100)
user_input = 0
while user_input != computer_number:
    user_input = int(input("Guess a number between 1 and 100:\n"))
    if user_input < computer_number:
        print("Too low. Try again.")
    elif user_input > computer_number:
        print("Too high. Try again.")
   
print("Congratulations! You've guessed the number:", computer_number)
