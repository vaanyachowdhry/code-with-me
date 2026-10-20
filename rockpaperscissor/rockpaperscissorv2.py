import random
import json

try:
   with open("databaserps.json", "r") as f:
    data = json.load(f)
    name = input("Enter your name: ")
    if name in data:
        score = data[name]
        print(f"Welcome back, {name}! Your current score is: {score}")
    else:
        data[name] = {"user": 0, "computer": 0}
        print(f"Welcome, {name}! Your score has been initialized.")
except FileNotFoundError:
    data = {}
    name = input("Enter your name: ")
    data[name] = {"user": 0, "computer": 0}
    print(f"Welcome, {name}! Your score has been initialized.")
    
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
         data[name]["user"] += 1
    elif (COMPUTERCHOICE == "rock" and USERCHOICE == "scissor") or \
         (COMPUTERCHOICE == "paper" and USERCHOICE == "rock") or \
         (COMPUTERCHOICE == "scissor" and USERCHOICE == "paper"):
         print(f"You chose {USERCHOICE}, computer chose {COMPUTERCHOICE}.")
         print("Computer wins!")
         data[name]["computer"] += 1
    else:
         print("Invalid choice, score won't be updated. Please choose rock, paper, or scissor.")

    
    WANTTOPLAY = input("Do you want to play again? (yes/no): ").lower()

print(f"Final Score - User: {data[name]['user']}, Computer: {data[name]['computer']}")
print("Thanks for playing!")

with open("databaserps.json", "w") as f:
    json.dump(data, f, indent=1)