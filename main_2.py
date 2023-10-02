import numpy as np
import scipy
import sklearn
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Generating random data
np.random.seed(12345)
Xp = np.random.randn(10000, 2) * 0.25
t = np.array([3,2])
S = np.diag([2, 0.5])

alpha = np.pi/6
Q = np.array([
  [np.cos(alpha), np.sin(alpha)],
  [-np.sin(alpha), np.cos(alpha)]
])

X = Xp @ S @ Q + t

# Plot your data
plt.figure()
plt.plot(X[:, 0], X[:, 1], "o", alpha=0.1)
plt.show()

# SVD
Xcentered = X - np.mean(X, axis=0)
U, s, V = scipy.linalg.svd(Xcentered, full_matrices=False)
print("Singular values (from SVD) of artificial data:", s)

pca = PCA(n_components=2)
pdata = pca.fit_transform(Xcentered)
principal_components = pca.components_
samples_new_coordinates = pdata

print("Explained variance (PCA) of artificial data:", pca.explained_variance_)
print("Singular values (PCA) of artificial data:", pca.singular_values_)
print("Principal Components:\n", principal_components)
print("\nSample in New Coordinates (first 10 rows):\n", samples_new_coordinates[:10])

plt.figure()
plt.plot(pdata[:,0], pdata[:,1], "o", alpha=0.1)
plt.show()


print("---------- Real Data analysis ----------")
print("---------- Real Data analysis ----------")
print("---------- Real Data analysis ----------")
# Importing real world data
body = np.genfromtxt("https://raw.githubusercontent.com/gagolews/"+"teaching-data/master/marek/nhanes_adult_female_bmx_2020.csv", delimiter=",")[1:,:]
print("First 6 rows of NHANES data:", body[:6, :])

Xcentered = body - np.mean(body, axis=0)
pca = PCA(n_components=3)
pdata = pca.fit_transform(Xcentered)
principal_components = pca.components_
samples_new_coordinates = pdata

print("Explained variance (PCA) of NHANES data:", pca.explained_variance_)
print("Singular values (PCA) of NHANES data:", pca.singular_values_)
print("Principal Components:\n", principal_components)
print("\nSample in New Coordinates (first 10 rows):\n", samples_new_coordinates[:10])

plt.figure()
plt.plot(pdata[:,0], pdata[:,1], "o", alpha=0.1)
plt.show()
