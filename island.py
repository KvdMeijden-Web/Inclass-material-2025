island = [
    ["O", "O", "O", "O", "O"],
    ["O", "O", "0", "O", "O"],
    ["O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O"]
]   

print(island[1][2])
island[1][2] = "B"
print(island[1][2])
#randomly place a treasure in the island.(replace the value "O" with "X")

#randomly place three bombs in the island.(replace the value "O" with "B")
#make sure the treasure and bombs are not in the same place.
#ask the user to guess where the treasure is.
#If the user guesses the treasure, they win.
#If the user guesses a bomb, they lose.
#If the user guesses an empty spot, they can guess again.
#The game continues until the user finds the treasure or hits a bomb.