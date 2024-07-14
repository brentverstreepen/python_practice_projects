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
print(card_number)

# Step 2
# Reverse number
card_number = card_number[::-1]
print(card_number)
# Add digits in odd places -> 1, 3, 5...
for x in card_number[::2]:
    sum_odd_digits += int(x)

# Step 3
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# Step 4