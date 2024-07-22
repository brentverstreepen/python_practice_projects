largest = None
smallest = None

# Create loop that repeatedly prompts user for int numbers
while True:
    number = input("Enter a number: ").lower()

    # Break out of loop if user enters 'done'
    if number == "done":
        break

    # Print error if user doesn't enter int
    try:
        number = int(number)
    except ValueError:
        print("Please enter a number.\n")
        continue

    if largest is None or number > largest:
        largest = number

    if smallest is None or number < smallest:
        smallest = number

# Print largest and smallest number
print("\nLargest number:", largest)
print("Smallest number:", smallest)

