import numpy as np
import sympy as sp

def compute_svd(A):
    # Convert A to a symbolic matrix
    A = sp.Matrix(A)
    
    # Compute A^T * A
    A_T_A = A.T * A
    
    # Compute eigenvalues and eigenvectors of A^T * A
    eigvals = list(A_T_A.eigenvals().keys())
    eigvecs = [v[2][0] for v in A_T_A.eigenvects()]
    
    # Compute singular values
    sigma = [sp.sqrt(val) for val in eigvals]
    
    # Constructing the Sigma matrix with singular values on the diagonal
    Sigma = sp.zeros(A.shape[0], A.shape[1])
    for i in range(len(sigma)):
        Sigma[i, i] = sigma[i]
    
    # Compute U using A, V and Sigma
    V = sp.Matrix.hstack(*eigvecs)
    U = A * V * Sigma.inv()
       
    return U, Sigma, V.T

# Matrix A
A = [[1, 1, 1], [-1, 0, -2], [1, 2, -1]]

U, Sigma, V_T = compute_svd(A)

print("Matrix V^T:")
print(V_T)
print("\n-----------------------------")
