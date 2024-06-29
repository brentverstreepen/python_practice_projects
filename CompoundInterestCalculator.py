# Compound Interest Calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    try:
        principle = float(input("Enter the principle amount: "))
    except:
        print("Please enter a number.")
    if principle <= 0:
        print("Principle amount can't be less than or equal to zero.")

while rate <= 0:
    try:
        rate = float(input("Enter the rate: "))
    except:
        print("Please enter a number")
    if rate <= 0:
        print("Rate can't be less than or equal to zero.")

while time <= 0:
    try:
        time = float(input("Enter the time in years: "))
    except:
        print("Please enter a number.")
    if time <= 0:
        print("Time can't be less than or equal to zero.")

print(principle)
print(rate)
print(time)