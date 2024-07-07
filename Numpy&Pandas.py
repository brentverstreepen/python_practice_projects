import numpy as np

# TASK #1: DEFINE SINGLE AND MULTI-DIMENSIONAL NUMPY ARRAYS
print("---TASK 1---")
# Let's define a one-dimensional array
list_01 = [50, 60, 70, 80, 90, 100, 200, 300, 500, 600]
print(list_01)

# Let's create a numpy array from the list
numpy_array = np.array(list_01)
print(numpy_array)
print(type(numpy_array))

# Multi-dimensional (Matrix definition)
my_matrix = np.array([[2, 5, 8], [7, 3, 6]])
print(my_matrix)

# MINI CHALLENGE #1:
#   Write a code that creates the following 2x4 numpy array
#   [[3 7 9 3]
#   [4 3 2 2]]

my_matrix01 = np.array([[3, 7, 9, 3], [4, 3, 2, 2]])
print(f"\nMINI CHALLENGE #1:\n{my_matrix01}")


# TASK #2: LEVERAGE NUMPY BUILT-IN METHODS AND FUNCTIONS
print("\n---TASK 2---")
# "rand()" uniform distribution between 0 and 1 (define random numbers that are uniformly distributed between 0 and 1)
x = np.random.rand(5)
print(x)

# You can create a matrix of random number as well
x = np.random.rand(3, 3)
print(x)

# "randint" is used to generate random integers between upper and lower bounds
x = np.random.randint(1, 50)
print(x)

# "randint" can be used to generate a certain number of random integers as follows
x = np.random.randint(1, 100, 15)
print(x)

# np.arange creates evenly spaced values within a given interval
x = np.arange(1, 21)
print(x)

# Create a diagonal of ones and zeros everywhere else
x = np.eye(5)
print(x)

# Matrix of ones
x = np.ones((3, 3))
print(x)

# Array of zeros
x = np.zeros(3)
print(x)

# MINI CHALLENGE #2:
# Write a code that takes in a positive integer "x" from the user and
# creates a 1x10 array with random numbers ranging from 0 to "x"
"""print("\nMINI CHALLENGE #2:")
userInput = int(input("Enter a number above 0: "))
array = np.random.randint(0, userInput, 10)
print(array)"""


# TASK #3: PERFORM MATHEMATICAL OPERATIONS IN NUMPY
print("\n---TASK 3---")
# Add 2 numpy arrays together
x = np.arange(1, 11)
y = np.arange(1, 11)
print(x + y)

# Power of numpy arrays
squared = x ** 2
print(squared)

# Square root of numpy arrays
sqrt = np.sqrt(squared)
print(sqrt)

