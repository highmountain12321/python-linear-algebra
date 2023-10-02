from sympy import Matrix

x1 = Matrix([2, -2, 0, 0])
x2 = Matrix([2, 0, -3, 2])
x3 = Matrix([0, -3, -3, 0])

# Starting with f1 = x1
f1 = x1

# Calculate f2 using Gram-Schmidt
f2 = x2 - (x2.dot(f1) / f1.norm()**2) * f1

# Calculate f3 using Gram-Schmidt
f3 = x3 - (x3.dot(f1) / f1.norm()**2) * f1 - (x3.dot(f2) / f2.norm()**2) * f2

# print the results
print("f1:")
print(f1)
print("\nf2:")
print(f2)
print("\nf3:")
print(f3)
