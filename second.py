import numpy as np

def qr_algorithm(A, max_iterations=100, tol=1e-10):
    """
    Approximate eigenvalues of matrix A using the QR algorithm.

    Parameters:
        A (numpy.ndarray): The matrix for which to find eigenvalues.
        max_iterations (int): Maximum number of iterations for the QR algorithm.
        tol (float): Convergence tolerance. If changes between iterations are below this threshold, stop.

    Returns:
        numpy.ndarray: Diagonal of the converged matrix, approximating the eigenvalues of A.
    """
    
    for _ in range(max_iterations):
        # Compute the QR factorization
        Q, R = np.linalg.qr(A)
        print("A = Q, R")
        print(A, Q, R)
        
        # Update A
        A_new = R @ Q
        
        # Check for convergence
        if np.linalg.norm(A_new - A) < tol:
            break
        
        A = A_new

    return np.diag(A_new)

# Example usage:
A = np.array([[3, 1], [1, 0]])
eigenvalues_approx = qr_algorithm(A, max_iterations=3)

print("Approximated Eigenvalues:")
print(eigenvalues_approx)
