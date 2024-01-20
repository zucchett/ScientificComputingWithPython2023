#!/usr/bin/env python
# coding: utf-8

# 1\. **PCA on 3D dataset**
# 
# * Generate a dataset simulating 3 features, each with N entries (N being ${\cal O}(1000)$). Each feature is made by random numbers generated according the normal distribution $N(\mu,\sigma)$ with mean $\mu_i$ and standard deviation $\sigma_i$, with $i=1, 2, 3$. Generate the 3 variables $x_{i}$ such that:
#     * $x_1$ is distributed as $N(0,1)$
#     * $x_2$ is distributed as $x_1+N(0,3)$
#     * $x_3$ is given by $2x_1+x_2$
# * Find the eigenvectors and eigenvalues using the eigendecomposition of the covariance matrix
# * Find the eigenvectors and eigenvalues using the SVD. Check that the two procedures yield to same result
# * What percent of the total dataset's variability is explained by the principal components? Given how the dataset was constructed, do these make sense? Reduce the dimensionality of the system so that at least 99% of the total variability is retained
# * Redefine the data according to the new basis from the PCA
# * Plot the data, in both the original and the new basis. The figure should have 2 rows (the original and the new basis) and 3 columns (the $[x_0, x_1]$, $[x_0, x_2]$ and $[x_1, x_2]$ projections) of scatter plots.

# In[1]:

print("************************************1.*************************************************************************")
from scipy import linalg as la
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


n = 1000
x1 = np.random.normal(0, 1, n)
x2 = x1 + np.random.normal(0, 3, n)
x3 = 2*x1 + x2

dataset = np.array([x1, x2, x3])


# In[3]:


# 1)
cov = np.cov(dataset)
l, V = la.eig(cov)
l = np.real_if_close(l)

print("Eigenvalues of the covariance matrix:\n", l, '\n')
print("Eigenvectors of the covariance matrix:\n", V, '\n')


# In[4]:


# 2)
U, S, Vt = np.linalg.svd(dataset)
l_svd = S**2/(n-1)
V_svd = U
print("Eigenvalues SVD:\n", l_svd)
print("Eigenvectors SVD:\n", V_svd)


# In[5]:


# 3)
Lambda = np.diag(l)
print("Lambda:\n", Lambda, '\n')
print("Trace(A):\n", cov.trace(), '\n')
print("Trace(Lambda):\n", Lambda.trace(), '\n')


# In[6]:


# 4)
transpose_U = U.T
Xp = np.dot(transpose_U, dataset)


# In[7]:


# 5)
fig = plt.figure(figsize=(15,10))

plt.subplot(2, 3, 1)
plt.title("Original X0 - X1")
plt.scatter(dataset[0,:], dataset[1,:], alpha=0.2)

plt.subplot(2, 3, 2)
plt.title("Original X0 - X2")
plt.scatter(dataset[0,:], dataset[2,:], alpha=0.2)

plt.subplot(2, 3, 3)
plt.title("Original X1 - X2")
plt.scatter(dataset[1,:], dataset[2,:], alpha=0.2)

plt.subplot(2, 3, 4)
plt.title("New basis X0 - X1")
plt.scatter(Xp[0,:], Xp[1,:], alpha=0.3)

plt.subplot(2, 3, 5)
plt.title("New basis X0 - X2")
plt.scatter(Xp[0,:], Xp[2,:], alpha=0.2)

plt.subplot(2, 3, 6)
plt.title("New basis X1 - X2")
plt.scatter(Xp[1,:], Xp[2,:], alpha=0.2)
plt.show()


# In[8]:


print("The percentual of dataset variability :"+ str(np.real(np.sum(l[:2])/np.sum(l))*100))

print("************************************2.*************************************************************************")
# 2\. **PCA on a nD dataset**
# 
# * Start from the dataset you have genereted in the previous exercise and add uncorrelated random noise. Such noise should be represented by other 10 uncorrelated variables normally distributed, with a standard deviation much smaller (e.g. a factor 20) than those used to generate the $x_1$ and $x_2$. Repeat the PCA procedure and compare the results with what you have obtained before.

# In[9]:


noise = []
for i in range(10):
    noise.append(np.random.rand(n)/20)
dataset_nd = np.vstack([dataset, [i for i in noise ]])


# In[10]:


# 1)
cov_nd = np.cov(dataset_nd)
l_nd, V_nd = la.eig(cov_nd)
l_nd = np.real_if_close(l_nd)

print("Eigenvalues of the covariance matrix:\n", l_nd, '\n')
print("Eigenvectors of the covariance matrix:\n", V_nd, '\n')


# In[11]:


# 2)
U_nd, S_nd, Vt_nd = np.linalg.svd(dataset_nd)
l_svd_nd = S_nd**2/(n-1)
V_svd_nd = U_nd
print("Eigenvalues SVD:\n", l_svd_nd)
print("Eigenvectors SVD:\n", V_svd_nd)


# In[12]:


# 3)
Lambda_nd = np.diag(l_nd)
print("Lambda:\n", Lambda_nd, '\n')
print("Trace(A):\n", cov_nd.trace(), '\n')
print("Trace(Lambda):\n", Lambda_nd.trace(), '\n')


# In[13]:


# 4)
transpose_U_nd = U_nd.T
Xp = np.dot(transpose_U_nd, dataset_nd)


# In[14]:


# 5)
fig = plt.figure(figsize=(7,5))
plt.title("Original X0 - X1")
plt.scatter(dataset_nd[0,:], dataset_nd[1,:], alpha=0.4)


# In[15]:


print("The percentual of dataset variability :"+ str(np.real(np.sum(l_nd[:12])/np.sum(l_nd))*100))

print("************************************3.*************************************************************************")
# 3\. **Optional**: **PCA on the MAGIC dataset**
# 
# Perform a PCA on the magic04.data dataset.

# In[16]:


# get the dataset and its description on the proper data directory
get_ipython().system('wget https://archive.ics.uci.edu/ml/machine-learning-databases/magic/magic04.data -P data/')
get_ipython().system('wget https://archive.ics.uci.edu/ml/machine-learning-databases/magic/magic04.names -P data/')


# In[17]:


df = pd.read_csv("data/magic04.data", names = ['fLength','fWidth','fSize','fConc','fConc1','fAsym','fM3Long','fM3Trans','fAlpha','fDist','class'])
df = df.drop(['class'], axis=1).T
df.head(15)


# In[18]:


cov = np.cov(df)
l, V = la.eig(cov)
l = np.real_if_close(l)

print("Eigenvalues of the covariance matrix:\n", l, '\n')
print("Eigenvectors of the covariance matrix:\n", V, '\n')


# In[19]:


for i in range(len(df)):
    print("The percentual of dataset variability using "+str(i)+" components: "+ str(np.real(np.sum(l[:i])/np.sum(l))*100))


# In[20]:


Xp = np.dot(U.T, dataset)

fig = plt.figure(figsize=(7,5))
plt.title("X0 - X1")
plt.scatter(Xp[0,:], Xp[1,:], alpha=0.4)

