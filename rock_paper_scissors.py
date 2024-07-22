import random

# Keep track of the score
userWins = 0
computerWins = 0

# Create list of input choices
choices = ["Rock", "Paper", "Scissors"]

# Create while loop for game
while True:
    # If user wants to quit
    userInput = input("Choose between Rock/Paper/Scissors or Q to quit: ").lower()
    if userInput == "q":
        break

    # If user gives wrong input
    if userInput not in ["rock", "paper", "scissors"]:
        print("Please choose a valid option.\n")
        continue

    # Generate choice for computer
    # Rock = 0, Paper = 1, Scissors = 2
    randomNumber = random.randint(0, 2)
    computerChoice = choices[randomNumber]
    print("The computer picked:", computerChoice, "\n")

    if userInput == "rock" and computerChoice == "Scissors":
        print("Congratulations, you win!")
        userWins += 1
        print("Your score:", userWins, "-", "Computer's score:", computerWins, "\n")

    elif userInput == "paper" and computerChoice == "Rock":
        print("Congratulations, you win!")
        userWins += 1
        print("Your score:", userWins, "-", "Computer's score:", computerWins, "\n")

    elif userInput == "scissors" and computerChoice == "Paper":
        print("Congratulations, you win!")
        userWins += 1
        print("Your score:", userWins, "-", "Computer's score:", computerWins, "\n")

    elif userInput == "rock" and computerChoice == "Rock":
        print("It's a draw!")
        print("Your score:", userWins, "-", "Computer's score:", computerWins, "\n")

    elif userInput == "paper" and computerChoice == "Paper":
        print("It's a draw!")
        print("Your score:", userWins, "-", "Computer's score:", computerWins, "\n")

    elif userInput == "paper" and computerChoice == "Scissors":
        print("It's a draw!")
        print("Your score:", userWins, "-", "Computer's score:", computerWins, "\n")

    else:
        print("You lost, better luck next time.")
        computerWins += 1
        print("Your score:", userWins, "-", "Computer's score:", computerWins, "\n")
        continue


print("Goodbye!")
