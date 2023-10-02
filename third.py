import numpy as np

A1 = np.array([[1, -1], [0, 1], [1, 0]])
U1, S1, VT1 = np.linalg.svd(A1)

print("U1:\n", U1)
print("S1:\n", np.diag(S1))
print("VT1:\n", VT1)

A2 = np.array([[1, 1, 1], [-1, 0, -2], [1, 2, 0]])
U2, S2, VT2 = np.linalg.svd(A2)

print("U2:\n", U2)
print("S2:\n", np.diag(S2))
print("VT2:\n", VT2)


def compute_svd(A):
    # Compute A^T * A
    A_T_A = np.dot(A.T, A)
    
    # Compute eigenvalues and eigenvectors of A^T * A
    eigvals, V = np.linalg.eig(A_T_A)
    
    # Sorting the eigenvectors by decreasing eigenvalues
    idx = eigvals.argsort()[::-1]
    eigvals = eigvals[idx]
    V = V[:,idx]
    
    # Compute singular values
    sigma = np.sqrt(eigvals)
    
    # Constructing the Sigma matrix with singular values on the diagonal
    Sigma = np.zeros(A.shape)
    for i in range(len(sigma)):
        Sigma[i, i] = sigma[i]
    
    # Compute U using A, V and Sigma
    U = np.dot(A, np.dot(V, np.linalg.inv(Sigma)))
    
    return U, Sigma, V.T

# Matrix A
A = np.array([[1, 1, 1], [-1, 0, -2], [1, 2, -1]])

U, Sigma, V_T = compute_svd(A)

print("Matrix U:")
print(U)
print("\nMatrix Sigma:")
print(Sigma)
print("\nMatrix V^T:")
print(V_T)
