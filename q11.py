from sympy import Matrix

# Define the vectors as matrices in sympy
x1 = Matrix([0, 2, -3])
x2 = Matrix([3, -1, 0])
x = Matrix([3, 0, -3])

# Stack x1 and x2 as columns to form matrix A
A = x1.row_join(x2)

# Compute the projection matrix P
P = A * (A.T * A).inv() * A.T

# Compute the closest vector u in span {x1, x2} to x
u = P * x

# Compute the vector v orthogonal to span {x1, x2}
v = x - u

# Output the results
print("The closest vector u in U to x is:")
print(u)
print("\nThe vector v which is orthogonal to U is:")
print(v)
