import numpy as np

# Given matrices A and b
A = np.array([[4, 6], [2, -6], [1, -6]])
b = np.array([[-2], [1], [4]])

# Compute x0 using the least squares method
x0, residuals, rank, singular_values = np.linalg.lstsq(A, b, rcond=None)

# Display the results
print("The vector x0 that best approximates a solution is:")
print(x0)
print(f"The least squares line of best fit is y = {x0[0]:.3f} + {x0[1]:.3f}x")