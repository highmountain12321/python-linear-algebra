from sympy import Matrix

# Define the matrices A and B
A = Matrix([
    [3, -7],
    [1, 3]
])

B = Matrix([
    [9, 3],
    [0, -3]
])

# Compute determinant, trace, and eigenvalues for A
det_A = A.det()
trace_A = A.trace()
eigenvalues_A = A.eigenvals(multiple=True)  # multiple=True returns a flat list of eigenvalues

# Compute determinant, trace, and eigenvalues for B
det_B = B.det()
trace_B = B.trace()
eigenvalues_B = B.eigenvals(multiple=True)

# Display the results and comparisons
print(f"Determinant of A: {det_A}, Determinant of B: {det_B}")
print(f"Trace of A: {trace_A}, Trace of B: {trace_B}")
print(f"Eigenvalues of A: {eigenvalues_A}, Eigenvalues of B: {eigenvalues_B}")

# Check if determinant, trace and eigenvalues are the same
if det_A == det_B:
    print("Determinants of A and B are the same.")
else:
    print("Determinants of A and B are different.")

if trace_A == trace_B:
    print("Traces of A and B are the same.")
else:
    print("Traces of A and B are different.")

if sorted(eigenvalues_A) == sorted(eigenvalues_B):  # Sort the eigenvalues before comparing
    print("Eigenvalues of A and B are the same.")
else:
    print("Eigenvalues of A and B are different.")
