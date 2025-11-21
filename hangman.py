# Hangman Game
# Make sure the lives.py file is in the same directory as this script
from lives import stages
import random
words = ["arrow", "banana", "computer", "python", "hangman"]
lives = 5
guessed_letters = []
print("Welcome to Hangman!")
word = random.choice(words)
for letter in word:
    guessed_letters.append("_")
print(guessed_letters)
# print(word)  # Uncomment this line to see the chosen word (for testing purposes)
while lives > 0 and "_" in guessed_letters:
    print(stages[lives])
    # Print the right image from the list in lives.py using the lives variable to index the stages list. (remember that the index starts at 0)
    # Print the lives left.
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            letter = word[i]
            if letter == guess:
                guessed_letters[i] = letter
        print("Correct!")
        print(guessed_letters)
    else:
        lives -= 1
        print("Wrong!")


if lives == 0:
    print("You lose! The word was:", word)
else:
    print("You win! The word was:", word)