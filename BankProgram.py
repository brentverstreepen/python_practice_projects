# Banking program

def showBalance(balance):
    print(f"---Your balance is €{balance:.2f}---\n")

def deposit():
    depositAmount = float(input("\nEnter the amount to deposit: "))
    if depositAmount <= 0:
        print("Deposit amount needs to be greater than €0\n")
        # Need to return a value else TypeError
        return 0
    else:
        print(f"€{depositAmount} has been deposited\n")
        return depositAmount

def withdraw(balance):
    withdrawAmount = float(input("Enter amount to withdraw: "))
    if withdrawAmount > balance:
        print(f"Withdraw amount can't be higher than current balance (€{balance})\n")
    elif withdrawAmount <= 0:
        print("Withdraw amount must be greater than €0\n")
        # Need to return a value else TypeError
        return 0
    else:
        print(f"€{withdrawAmount} has been withdrawn\n")
        return withdrawAmount

def main():
    # Create variables
    balance = 0
    is_running = True
    # Create options for user
    while is_running:
        print("*********************")
        print("   Banking Program   ")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")

        # Ask for user input
        choice = input("Enter your choice (1-4): ")

        # Use input to run the chosen choice
        if choice == "1":
            showBalance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Please enter a valid number\n")

    # Print goodbye message if user exits
    print("Goodbye")

# Allow to execute code when file runs as a script
if __name__ == "__main__":
    main()