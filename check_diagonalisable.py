from sympy import Matrix, symbols

# Define the matrix A
A = Matrix([[-2, 1, -4], [1, -2, -5], [-4, -5, 5]])

# Find the eigenvalues and their algebraic multiplicities
eigenvalues = A.eigenvals()

# Check if the matrix is diagonalizable
algebraic_multiplicity_sum = sum(eigenvalues.values())
is_diagonalizable = algebraic_multiplicity_sum == A.shape[0]

# Output the results
print("Eigenvalues and their multiplicities:", eigenvalues)
print("The matrix is diagonalizable:", is_diagonalizable)
