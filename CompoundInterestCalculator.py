# Compound Interest Calculator
# Create needed variables
principle = 0
rate = 0
time = 0

# Create loop to ask for user input and place it in variables
while principle <= 0:
    try:
        principle = float(input("Enter the principle amount: "))
        if principle <= 0:
            print("Principle amount can't be less than or equal to zero.")

    except ValueError:
        print("Please enter a number.")

while rate <= 0:
    try:
        rate = float(input("Enter the rate: "))
        if rate <= 0:
            print("Rate can't be less than or equal to zero.")

    except ValueError:
        print("Please enter a number")

while time <= 0:
    try:
        time = float(input("Enter the time in years: "))
        if time <= 0:
            print("Time can't be less than or equal to zero.")
    except ValueError:
        print("Please enter a number")

# Calculate total value with formula
total = principle * pow((1 + rate / 100), time)

# Print total balance rounded to 2 decimals
print(f"\nBalance after {time} year/s: €{total:.2f}")
