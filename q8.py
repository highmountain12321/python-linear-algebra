from sympy import Matrix

# Define the matrix representing the given set of polynomials
A = Matrix([
    [0, -1, 0, 2],
    [0, -3, 2, 10],
    [0, 1, 1, 0],
    [0, 3, -1, -8]
])

# Find the Reduced Row Echelon Form of A
rref_matrix, pivot_columns = A.rref()

# Print the RREF of A
print("The Reduced Row Echelon Form (RREF) of A is:")
print(rref_matrix)

# Extract the non-zero rows of the rref_matrix to form the basis of the subspace
basis = [rref_matrix.row(i) for i in range(rref_matrix.rows) if any(rref_matrix.row(i))]

# Print the basis and dimension of the subspace
print("Basis for the Subspace:")
print(basis)
print("Dimension of the Subspace:", len(basis))
