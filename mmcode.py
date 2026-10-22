from colorama import init, Fore, Style

init(autoreset= True)

print(Fore.RED + Style.BRIGHT + "THE LAST BELL - A COLLEGE THEMED MURDER MYSTERY")

#INTRODUCTION STARTS HERE

print(Fore.YELLOW + "CASE NUMBER #234 \n STATUS:UNDER INVESTIGATION")

print(Fore.GREEN + "One murder. \n Five suspects. \n What will you do detective?")

name = input("Please enter your name: ")
print(f"Welcome detective {name}.")

#GAMEPLAY OPTIONS:
print(Fore.GREEN + "===========MAIN PANEL============")

print (Fore.MAGENTA + "[1] Investigate a location")
print (Fore.MAGENTA + "[2] Question a suspect")
print (Fore.MAGENTA + "[3] Review the evidence")
print (Fore.MAGENTA + "[4] Quit the game")

print(Fore.GREEN + "=================================")

while True:

 try:      
  user_input = int(input("Please enter a number: "))

  if user_input ==1:
       print(Fore.BLUE + "Opening location data...")
       print(Fore.BLUE + "Three locations detected on file. Choose one to investigate")
       print(Fore.GREEN + "===========LOCATION PANEL============")
       print(Fore.BLUE + "[1] FESTIVAL GROUNDS")
       print(Fore.BLUE + "[2] COMPUTER LABORATORY")
       print(Fore.BLUE + "[3] VICTIM'S DORMROOM")
       print(Fore.MAGENTA + "[4] Return to Main Menu")
       print(Fore.GREEN + "=====================================")
       while True:
        try:
         user1_input = int(input("Please enter a number: "))
          if user1_input ==1:
              print(Fore.BLUE +"THE FESTIVE GROUNDS")
              print(Fore.MAGENTA + "The torn wristband: \nA festival wristband is found near the side exit. \nIt belongs to the volunteer access category, but the name is missing.")
          elif user1_input ==2:
              print(Fore.BLUE +"COMPUTER LABORATORY")
              print(Fore.MAGENTA + "Late login access: \nAn email ID: angiechauhaan@yahoooo.com was accessed 20 mins before the murder.")
          elif user1_input ==3:
              print(Fore.BLUE +"VICTIM'S DORMROOM")
              print(Fore.MAGENTA + "A note addressed to Kabir: \"you said noone would find out. Meet me near the lab after the fireworks")
          elif user1_input ==4:
              print("Returning to main menu...")
              break
          else:
              print("Invalid value")
         
       except ValueError:
         print("Only numbers please!")

  elif user_input ==2:
       print("Opening suspect files...")
  elif user_input ==3:
       print("Opening evidence files...")
  elif user_input ==4:
       print("Logging out. Goodbye detective...")
       break
  else:
            print("Invalid choice")

 except ValueError:
  print("Please enter numbers, not letters!")

