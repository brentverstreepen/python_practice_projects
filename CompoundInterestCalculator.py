# Compound Interest Calculator
# Create needed variables
principle = 0
rate = 0
time = 0

# Create loop to ask for user input and place it in variables
while principle <= 0:
    try:
        # Convert input to float
        principle = float(input("Enter the principle amount: "))
        # Print error message if value is <= 0
        if principle <= 0:
            print("Principle amount can't be less than or equal to zero")
    # Print error message if user gives wrong input
    except ValueError:
        print("Please enter a number")

while rate <= 0:
    try:
        # Convert input to float
        rate = float(input("Enter the rate: "))
        # Print error message if value is <= 0
        if rate <= 0:
            print("Rate can't be less than or equal to zero")
    # Print error message if user gives wrong input
    except ValueError:
        print("Please enter a number")

while time <= 0:
    try:
        # Convert input to float
        time = float(input("Enter the time in years: "))
        # Print error message if value is <= 0
        if time <= 0:
            print("Time can't be less than or equal to zero")
    # Print error message if user gives wrong input
    except ValueError:
        print("Please enter a number")

# Calculate total value with formula
total = principle * pow((1 + rate / 100), time)

# Print total balance rounded to 2 decimals
print(f"\nBalance after {time} year/s: €{total:.2f}")
