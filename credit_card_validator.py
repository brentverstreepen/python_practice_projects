# Credit card validator

# Exercise:
# 1. Remove any '-' or ' ' after user input
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left. (If result is a two-digit number,
# add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid
sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1
card_number = input("Enter you card number: ")
# Remove "-" and " "
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")

# Step 2
# Reverse number
card_number = card_number[::-1]
# Sum of digits in odd places -> 1, 3, 5...
for x in card_number[::2]:
    sum_odd_digits += int(x)

# Step 3
# Start with 2nd number, step of 2
for x in card_number[1::2]:
    # Double it
    x = int(x) * 2
    # add numbers together if double-digit
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# Step 4
total = sum_odd_digits + sum_even_digits

# Step 5
# If divisible by 10
if total % 10 == 0:
    print(f"Valid Credit Card")
else:
    print(f"Invalid Credit Card")
