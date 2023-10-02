from sympy import Matrix

# Define matrix A
A = Matrix([[7, -5, -5], [-5, 3, -1], [-5, -1, 3]])

# Given Eigenvalues
eigenvalues = [12, 4, -3]

# Initialize an empty matrix P
P = Matrix([])

# Find the eigenvectors corresponding to each eigenvalue and form the matrix P
for eigenvalue in eigenvalues:
    # Find eigenvector corresponding to eigenvalue
    (eigenvector, ) = (A - eigenvalue * Matrix.eye(3)).nullspace()
    
    # Normalize the eigenvector
    eigenvector_normalized = eigenvector / eigenvector.norm()
    
    # Append the normalized eigenvector as a column to the matrix P
    P = P.row_join(eigenvector_normalized) if P.cols != 0 else eigenvector_normalized
    
# Output the matrix P
print("The orthogonal matrix P is:")
print(P)
