import numpy as np
import scipy
import sklearn
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Next, let us generate some random data in 2 variables, rotated about the origin and shifted, to simulate real world data.
np.random.seed(12345)
Xp = np.random.randn(10000, 2) * 0.25
t = np.array([3,2])
S = np.diag([2, 0.5])

alpha = np.pi/6
Q=np.array([
  [np.cos(alpha), np.sin(alpha)],
  [-np.sin(alpha), np.cos(alpha)]
])

X = Xp @ S @ Q + t

# Plot your data
plt.figure()
print("plt_1 figured")
plt.plot(X[:, 0], X[:, 1], "o", alpha=0.1)
print("plt_1 plotes")
plt.show()
print("plt_1 showed")

# Here we start our SVD
Xcentered = X-np.mean(X,axis=0)
print(Xcentered)
U, s, V = scipy.linalg.svd(Xcentered, full_matrices=False)
s

pca=PCA(n_components=2)
pdata=pca.fit_transform(Xcentered)
pca.explained_variance_
pca.singular_values_

plt.figure()
plt.plot(pdata[:,0], pdata[:,1], "o", alpha=0.1)
plt.show()
print("plt_2 showed")

# Describe what you observe in the plots. What are our singular values. How was the data generated?
# Now import some real world data from National Health and Nutrition Examination Survey(NHANES study)

body=np.genfromtxt("https://raw.githubusercontent.com/gagolews/"+"teaching-data/master/marek/nhanes_adult_female_bmx_2020.csv", delimiter=",")[1:,:] # skip first row (column names)
body[:6, :] # preview: 6 first rows, all columns
body.shape

# That is we have 4221 participants and 7 features. The features are "weight", "height", "arm len.", "leg len", "arm circ.", "hip circ.", "waist circ."

Xcentered=body-np.mean(body, axis=0)
pca=PCA(n_components=3)
pdata=pca.fit_transform(Xcentered)
pca.explained_variance_
pca.singular_values_

# Plot the data in the first two principal variables
plt.figure()
plt.plot(pdata[:,0], pdata[:,1], "o", alpha=0.1)
plt.show()
print("plt_3 showed")

# Describe what you observe in the plots. Include all the plots and outputs of your commands. If the datasets are not loaded automatically, just download them and open a local copy.
# Read documentation of the functions PCA and SVD. What other outputs you can get? Play with other data sets.