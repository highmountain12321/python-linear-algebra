from sympy import Matrix

# Define the given matrix A
A = Matrix([
    [-1, 1, 1, 0],
    [-2, 2, 3, -2],
    [0, 0, 1, 0],
    [1, -1, -3, 2]
])

# Find the RREF of A
rref_matrix, pivot_columns = A.rref()

# Display the RREF of A
print("The Reduced Row Echelon Form (RREF) of A is:")
print(rref_matrix)

# Find the basis of the null space of A
null_space_basis = A.nullspace()

# Display the basis and dimension of the null space
print("Basis for the Null Space of A:")
for vec in null_space_basis:
    print(vec)
print("Dimension of the Null Space of A:", len(null_space_basis))
