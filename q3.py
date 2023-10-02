import sympy

# Define variables
a, b, c, d = sympy.symbols('a b c d')

# Given vectors
v1 = (2, 2, -1, -1)
v2 = (1, 1, -1, 5)
v3 = (11, 1, 22, 2)

# Given value for d
d_value = 1  # or any other value of your choice

# Define the equations based on the dot products being 0
equation_1 = sum(v1_i * a_i for v1_i, a_i in zip(v1, (a, b, c, d_value)))
equation_2 = sum(v2_i * a_i for v2_i, a_i in zip(v2, (a, b, c, d_value)))
equation_3 = sum(v3_i * a_i for v3_i, a_i in zip(v3, (a, b, c, d_value)))

# Solve the system of equations for a, b, and c
solutions = sympy.solve((equation_1, equation_2, equation_3), (a, b, c))

# Display the solutions along with the chosen value for d
print("a =", solutions[a])
print("b =", solutions[b])
print("c =", solutions[c])
print("d =", d_value)
