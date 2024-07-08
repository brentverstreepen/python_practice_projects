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

# MINI CHALLENGE #3:
# Given the X and Y values below, obtain the distance between them
# X = [5, 7, 20]
# Y = [9, 15, 4]
print("\nMINI CHALLENGE #3:")
x = np.array([5, 7, 20])
y = np.array([9, 15, 4])

distance = np.sqrt(x**2 + y**2)
print(distance)


# TASK #4: PERFORM ARRAYS SLICING AND INDEXING
print("\n---TASK 4---")
# Access specific index from the numpy array
my_np_array = np.array([3, 5, 6, 2, 8, 10, 20, 50])
print(my_np_array[0], my_np_array[-1])

# Starting from the first index 0 up until and NOT including the last element
print(my_np_array[0:3])
print(my_np_array)

# Broadcasting, altering several values in a numpy array at once
my_np_array[0:4] = 7
print(my_np_array)

# Get a row from a matrix
matrix = np.random.randint(1, 11, (4, 4))
print(matrix[0], matrix[2])

# Get one element from 2D array
print(matrix[0][2])

# MINI CHALLENGE #4:
# In the following matrix, replace the last row with 0
# X = [2 30 20 -2 -4]
#     [3 4  40 -3 -2]
#     [-3 4 -6 90 10]
#     [25 45 34 22 12]
#     [13 24 22 32 37]
print("\nMINI CHALLENGE #4:")
matrix = np.array([[2, 30, 20, -2, -4], [3, 4, 40, -3, -2], [-3, 4, -6, 90, 10], [25, 45, 34, 22, 12], [13, 24, 22, 32, 37]])
matrix[4] = 0
print(matrix)


# TASK #5: PERFORM ELEMENTS SELECTION (CONDITIONAL)
print("\n---TASK 5---")
# Obtain elements from matrix that are greater than a value
matrix = np.random.randint(1, 11, (5,5))
print(matrix)
new_matrix = matrix[matrix > 7]
print(new_matrix)

# Obtain odd and even elements only
new_matrix = matrix[matrix % 2 == 1]
print(new_matrix)
new_matrix = matrix[matrix % 2 == 0]
print(new_matrix)

# MINI CHALLENGE #5:
print("\nMINI CHALLENGE #5:")
# In the following matrix, replace negative elements by 0 and replace odd elements with -2
# X = [2 30 20 -2 -4]
#     [3 4  40 -3 -2]
#     [-3 4 -6 90 10]
#     [25 45 34 22 12]
#     [13 24 22 32 37]
matrix = np.array([[2, 30, 20, -2, -4], [3, 4, 40, -3, -2], [-3, 4, -6, 90, 10], [25, 45, 34, 22, 12], [13, 24, 22, 32, 37]])
matrix[matrix < 0] = 0
matrix[matrix % 2 == 1] = -2
print(matrix)