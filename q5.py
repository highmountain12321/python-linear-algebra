from sympy import Matrix, symbols, solve

# Define the matrix A
A = Matrix([
    [-6, 0, 7],
    [0, -4, 0],
    [-4, 0, 5]
])

# Calculate Eigenvalues and Eigenvectors
eigenvalues = A.eigenvals(multiple=True)  # Returns a list of eigenvalues
eigenvectors = A.eigenvects()  # Returns a list of tuples, each containing the eigenvalue, algebraic multiplicity, and eigenvectors

# Form the Matrix P (Eigenvector Matrix) and Diagonal Matrix D (Eigenvalue Matrix)
P = Matrix.hstack(*[eigenvector[2][0] for eigenvector in eigenvectors])  # Concatenates eigenvectors horizontally to form P
D = Matrix.diag(*eigenvalues)  # Creates a diagonal matrix D with eigenvalues on the diagonal

# Calculate P^-1 * A * P to confirm the result
P_inv = P.inv()
result = P_inv * A * P

# print the Results
print("Matrix A:")
print(A)
print("\nEigenvalues (Diagonal matrix D):")
print(D)
print("\nEigenvectors (Matrix P):")
print(P)
print("\nInverted Matrix P (P^-1):")
print(P_inv)
print("\nCheck P^-1 * A * P:")
print(result)
