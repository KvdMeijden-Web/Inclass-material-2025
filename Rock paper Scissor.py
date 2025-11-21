import random
ROCK_PAPER_SCISSOR = ["Rock", "Paper", "Scissor"]

input_user = input("What do you choose? Rock, Paper or Scissor? ").capitalize().strip()
input_computer = random.choice(ROCK_PAPER_SCISSOR)
print("Computer chose: "+ input_computer+"\n")
if input_user==input_computer:
    print("It's a tie!")
elif input_user == "Rock" and input_computer == "Scissor":
    print("You win! Rock beats Scissor")
elif input_user == "Paper" and input_computer == "Rock":
    print("You win! Paper beats Rock")
elif input_user == "Scissor" and input_computer == "Paper":
    print("You win! Scissor beats Paper")




