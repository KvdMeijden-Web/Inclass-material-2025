import random
island = [
    ["O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O"]
]   
#randomly place a treasure in the island.
treasure_row = random.randint(0, 4)
treasure_col = random.randint(0, 4)
island[treasure_row][treasure_col] = "X"

#randomly place three bombs in the island.
for i in range(3):
    bomb_row = random.randint(0, 4)
    bomb_col = random.randint(0, 4)
#make sure the treasure and bombs are not in the same place.
    while island[bomb_row][bomb_col] == "X" or island[bomb_row][bomb_col] == "B":
        bomb_row = random.randint(0, 4)
        bomb_col = random.randint(0, 4)
    island[bomb_row][bomb_col] = "B"

#ask the user to guess where the treasure is.
while True:
    
    choice_row = int(input("Enter a row (1-5): "))
    choice_col = int(input("Enter a column (1-5): "))
    if island[choice_row-1][choice_col-1] == "X":
        print("You found the treasure! You win!")
        break
    elif island[choice_row-1][choice_col-1] == "B":
        print("You hit a bomb! You lose!")
        break
    else:
        print("No treasure here. Try again.")

#If the user guesses the treasure, they win.
#If the user guesses a bomb, they lose.
#If the user guesses an empty spot, they can guess again.
#The game continues until the user finds the treasure or hits a bomb.