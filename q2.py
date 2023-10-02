# from sympy import Matrix

# # Define the matrix M
# M = Matrix([[0, -3, 0, 0], [0, 3, 0, -1], [0, -1, 0, 1], [0, 0, 0, 1]])

# # Find the Reduced Row Echelon Form of M
# rref_matrix, pivot_columns = M.rref()

# # Extract the non-zero rows of the rref_matrix to form the basis of the subspace
# basis = [rref_matrix.row(i) for i in range(rref_matrix.rows)]

# # Print the basis and dimension of the subspace
# print("Basis for the Subspace:")
# print(basis)
# print("Dimension of the Subspace:", len(basis))


from sympy import Matrix, zeros

# Define the matrix M
M = Matrix([[-1, 0, 3, 1], [-3, -6, 6, 3], [3, 5, -6, -3], [0, 0, 0, 3]])

# Find the Reduced Row Echelon Form of M
rref_matrix, pivot_columns = M.rref()

# Extract the non-zero rows of the rref_matrix to form the basis of the subspace
basis = [rref_matrix.row(i) for i in range(rref_matrix.rows) if not rref_matrix.row(i).equals(zeros(1, rref_matrix.cols))]

# Print the basis and dimension of the subspace
print("Basis for the Subspace:")
print(basis)
print("Dimension of the Subspace:", len(basis))
