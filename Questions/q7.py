from sympy import Matrix

# Define matrix A
A = Matrix([
    [-2, -8, -9],
    [0, -2, 6],
    [0, 0, -9]
])

# Try to diagonalize A and, if not possible, find the available eigenvectors
try:
    P, D = A.diagonalize()
    print("Matrix A is diagonalizable.")
    print("Matrix P (Eigenvector matrix):")
    print(P)
    print("\nDiagonal Matrix D:")
    print(D)
    print("\nEigenvalues are the diagonal elements of D.")
except Exception as e:
    print("Matrix A is not diagonalizable.")
    
    # If A is not diagonalizable, provide as many linearly independent eigenvectors as possible.
    eigenvects = A.eigenvects()
    eigenvecs = [vect[2][0] for vect in eigenvects for _ in range(vect[1])]
    P_reduced = Matrix.hstack(*eigenvecs)
    print("Linearly Independent Eigenvectors as columns of reduced matrix P:")
    print(P_reduced)
