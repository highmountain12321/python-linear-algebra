import numpy as np

# Given data points
data_points = np.array([[-5, 2], [5, 6], [1, 0], [0, -5]])

# Number of data points
n = len(data_points)

# Calculate the sums needed for the normal equations
sum_x = np.sum(data_points[:, 0])
sum_y = np.sum(data_points[:, 1])
sum_xx = np.sum(data_points[:, 0] ** 2)
sum_xy = np.sum(data_points[:, 0] * data_points[:, 1])

# Solve the normal equations to find a and b
A = np.array([[n, sum_x], [sum_x, sum_xx]])
B = np.array([sum_y, sum_xy])
a, b = np.linalg.solve(A, B)

# Display the results
print(f"The least squares line of best fit is y = {a:.3f} + {b:.3f}x")
