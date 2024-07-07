import numpy as np

# Task #1: Define single and multidimensional NumPy arrays

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
