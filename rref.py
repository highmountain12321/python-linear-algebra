""" Use this python file for finding the Reduced Row Echelon Form(RREF) of a matrix"""

from sympy import Matrix

# Define the augmented matrix
A = Matrix([
    [1, 0, -1, -3, 0],
    [1, 2, -2, 1, 0],
    [5, -1, 2, 1, 0]
])

# Compute the RREF of the matrix
rref_matrix, pivot_columns = A.rref()

# Display the RREF matrix and the pivot columns
print("Row Reduced Echelon Form:")
print(rref_matrix)

print("\nPivot Columns:")
print(pivot_columns)
