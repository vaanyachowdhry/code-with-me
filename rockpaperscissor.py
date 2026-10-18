import random

SCORE = {"user": 0, "computer": 0}
choices = ["rock", "paper", "scissor"]

WANTTOPLAY = input("Do you want to play? (yes/no): ").lower()

while WANTTOPLAY == "yes":

    USERCHOICE = input("Enter your choice (rock, paper, scissor): ").lower()
    COMPUTERCHOICE = random.choice(choices)

    if USERCHOICE == COMPUTERCHOICE:
        print("It's a tie!")
    elif (USERCHOICE == "rock" and COMPUTERCHOICE == "scissor") or \
         (USERCHOICE == "paper" and COMPUTERCHOICE == "rock") or \
         (USERCHOICE == "scissor" and COMPUTERCHOICE == "paper"):
         print(f"You chose {USERCHOICE}, computer chose {COMPUTERCHOICE}.")
         print("You win!")
         SCORE["user"] += 1
    else:
         print(f"You chose {USERCHOICE}, computer chose {COMPUTERCHOICE}.")
         print("Computer wins!")
         SCORE["computer"] += 1

    
    WANTTOPLAY = input("Do you want to play again? (yes/no): ").lower()

print(f"Final Score - User: {SCORE['user']}, Computer: {SCORE['computer']}")
print("Thanks for playing!")
