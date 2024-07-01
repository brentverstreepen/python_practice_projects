# Bank program

def showBalance():
    pass

def deposit():
    pass

def withdraw():
    pass

balance = 0
is_running = True

# Create options for user
while is_running:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # Ask for user input
    choice = input("Enter your choice (1-4): ")

    # Use input to run the chosen choice
    if choice == "1":
        showBalance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Please enter a valid number\n")

# Print goodbye message if user exits
print("Goodbye")

def main():
    pass