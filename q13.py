from sympy import Matrix

# Given matrices (λ1I - A) and (λ2I - A)
M1 = Matrix([[-4, 0, -4], [0, -8, 0], [-4, 0, -4]])
M2 = Matrix([[4, 0, -4], [0, 0, 0], [-4, 0, 4]])
# M2 = Matrix([[-1, -2, -1], [-2, -4, -2], [-1, -2, -1]])

# Finding eigenvectors
# For λ1, find the null space of (λ1I - A), which is M1 in this case
eigenvectors_λ1 = M1.nullspace()

# For λ2, find the null space of (λ2I - A), which is M2 in this case
eigenvectors_λ2 = M2.nullspace()

# Assume v1 is the eigenvector corresponding to λ1 and v2 is the eigenvector corresponding to λ2
v1 = eigenvectors_λ1[0].normalized()  # Normalizing v1

# Since λ2 has multiplicity 2, there should be two linearly independent eigenvectors corresponding to λ2
# If the eigenvectors are not already orthogonal, they need to be orthogonalized and then normalized
v2 = eigenvectors_λ2[0].normalized()  # Normalizing v2

# If the nullspace of M2 has only one vector, i.e. is deficient, you can find v3 as orthogonal to both v1 and v2
print('343434343')
print(v2.cross(v1))

if len(eigenvectors_λ2) == 1:
    v3 = v1.cross(v2).normalized()  # Finding orthogonal vector and normalizing
else:
    v3 = eigenvectors_λ2[1].normalized()  # Normalizing the second eigenvector corresponding to λ2

# Create matrix P using the orthogonal normalized eigenvectors
P = Matrix.hstack(v1, v2, v3).T

print(f"Normalized Orthogonal Matrix P:\n{P}")
