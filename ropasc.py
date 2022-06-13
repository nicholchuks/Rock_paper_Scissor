import random

computer = 0
player = 0

def Choose_Option():
    user_choice = input("Choose Rock, Paper, or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"

    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"

    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"

    else:
        print("I dont understand, try again")
        Choose_Option()
    return user_choice

def Computer_Option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice

while True:
    print("")
    user_choice = Choose_Option()
    comp_choice = Computer_Option()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print ("You chose rock and computer chose rock. It's a Tie")
        elif comp_choice == "p":
            print("Computer chose paper. Computer Wins.")
            computer += 1
        elif comp_choice == "s":
            print("computer chose scissors. You win.")
            player += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print ("Computer chose rock. You win.")
            player += 1
        elif comp_choice == "p": 
            print("You chose paper and computer chose paper. It's a Tie.")
        elif comp_choice == "s":
            print("Computer chose scissors. Computer wins.")
            computer += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print ("Computer chose rock. Computer win.")
            computer += 1
        elif comp_choice == "p":
            print("Computer chose paper. You wins")
            player += 1
        elif comp_choice == "s":
            print("You chose scissors and computer chose scissors. It's a Tie.")

    print("")
    print("Player wins: " + str(player))
    print("Computer wins: " + str(computer))
    print("")

    user_choice = input("Do you want to play again? (y/n) ")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass 
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break