import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# 1. Plotting Power Functions
def plot_power_functions():
    x1 = np.linspace(-1, 1, 400)
    x2 = np.linspace(0, 10, 400)
    x3 = np.linspace(-10, 10, 400)
    
    intervals = [x1, x2, x3]
    titles = ["[-1,1]", "[0,10]", "[-10,10]"]
    
    for idx, x in enumerate(intervals):
        plt.figure(figsize=(8,6))
        for i in range(7):  # for k = 0 to 6
            plt.plot(x, x**i, label=f"x^{i}")
        
        plt.title(f"Power Functions on {titles[idx]}")
        plt.legend()
        plt.grid(True)
        plt.show()

plot_power_functions()

# 2. Gram-Schmidt Process
def gram_schmidt(f, inner_product, epsilon=1e-10):
    orthogonal = []
    for fn in f:
        for gn in orthogonal:
            ip = inner_product(gn, gn)
            if abs(ip) > epsilon:
                fn -= inner_product(fn, gn) / ip * gn
        if abs(inner_product(fn, fn)) > epsilon:
            orthogonal.append(fn)
    return orthogonal


# Legendre Inner Product
def legendre_inner_product(f, g):
    return integrate.quad(lambda x: f(x)*g(x), -1, 1)[0]

# Chebyshev Inner Product
def chebyshev_inner_product(f, g):
    return integrate.quad(lambda x: f(x)*g(x)/np.sqrt(1-x**2), -1, 1)[0]

# Laguerre Inner Product
def laguerre_inner_product(f, g):
    return integrate.quad(lambda x: np.exp(-x) * f(x) * g(x), 0, np.inf)[0]

# Define power functions
f = [np.poly1d([0]*i + [1]) for i in range(7)]  # [1, x, x^2, ..., x^6]

legendre_polynomials = gram_schmidt(f, legendre_inner_product)
chebyshev_polynomials = gram_schmidt(f, chebyshev_inner_product)
laguerre_polynomials = gram_schmidt(f, laguerre_inner_product)

print("First 6 Legendre Polynomials:")
for poly in legendre_polynomials:
    print(poly)

print("\nFirst 6 Chebyshev Polynomials:")
for poly in chebyshev_polynomials:
    print(poly)

print("\nFirst 6 Laguerre Polynomials:")
for poly in laguerre_polynomials:
    print(poly)
