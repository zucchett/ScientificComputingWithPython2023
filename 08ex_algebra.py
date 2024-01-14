import numpy as np
import matplotlib.pyplot as plt

#find the eigenvectors and eigenvalues using the eigendecomposition of the covariance matrix
N = 1000
x1 = np.random.normal(0, 1, N)
x2 = x1 + np.random.normal(0, 3, N)
x3 = 2 * x1 + x2
data = np.column_stack((x1, x2, x3))
cov_matrix = np.cov(data, rowvar=False)
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

#find the eigenvectors and eigenvalues using the SVD. Check that the two procedures yield to same result
U, s, Vt = np.linalg.svd(data, full_matrices=False)
eigenvalues_svd = s ** 2 / (N - 1)
for i in range(eigenvectors.shape[1]):
    if np.dot(eigenvectors[:, i], Vt[i]) < 0:
        eigenvectors[:, i] *= -1

eigenvectors_close = np.allclose(eigenvectors, Vt.T, rtol=1e-3, atol=1e-3)
print("The procedures lead to a close result?", eigenvectors_close)

#reduce the dimensionality of the system so that at least 99% of the total variability is retained
explained_variance_ratio = eigenvalues / np.sum(eigenvalues)
total_variability_explained = np.sum(explained_variance_ratio)
cumulative_variance_ratio = np.cumsum(explained_variance_ratio)
num_components_99_percent = np.argmax(cumulative_variance_ratio >= 0.99) + 1
print("What percent of the total dataset's variability is explained by the principal components?", total_variability_explained)
print("Given how the dataset was constructed, do these make sense? Yes, this indicates that the dataset can be well defined in a lower dimension space.")

#redefine the data according to the new basis from the PCA
new_basis = eigenvectors[:, :num_components_99_percent]
reduced_data = np.dot(data, new_basis)

#plot the data, in both the original and the new basis.
fig, axs = plt.subplots(2, 3, figsize=(15, 10))
axs[0, 0].scatter(data[:, 0], data[:, 1], alpha=0.5)
axs[0, 0].set_xlabel('x_1')
axs[0, 0].set_ylabel('x_2')
axs[0, 1].scatter(data[:, 0], data[:, 2], alpha=0.5)
axs[0, 1].set_xlabel('x_1')
axs[0, 1].set_ylabel('x_3')
axs[0, 2].scatter(data[:, 1], data[:, 2], alpha=0.5)
axs[0, 2].set_xlabel('x_2')
axs[0, 2].set_ylabel('x_3')
axs[1, 0].scatter(reduced_data[:, 0], reduced_data[:, 1], alpha=0.5)
axs[1, 0].set_xlabel('PC_1')
axs[1, 0].set_ylabel('PC_2')
plt.tight_layout()
plt.show()

##############################END OF PCA ON 3D DATASET.#######################################

#find the eigenvectors and eigenvalues using the eigendecomposition of the covariance matrix + adding some noise
N = 1000
x1 = np.random.normal(0, 1, N)
x2 = x1 + np.random.normal(0, 3, N)
x3 = 2 * x1 + x2
data = np.array([x1, x2, x3]).T
mean = np.mean(data, axis=0)
centered_data = data - mean
num_noise_variables = 10
std_dev_noise = 0.05
noise = np.random.normal(0, std_dev_noise, size=(N, num_noise_variables))
extended_data = np.hstack((centered_data, noise))
cov_matrix_extended = np.cov(extended_data, rowvar=False)
eigenvalues_extended, eigenvectors_extended = np.linalg.eig(cov_matrix_extended)
sorted_indices_extended = np.argsort(eigenvalues_extended)[::-1]
eigenvalues_extended = eigenvalues_extended[sorted_indices_extended]
eigenvectors_extended = eigenvectors_extended[:, sorted_indices_extended]

#find the eigenvectors and eigenvalues using the SVD. Check that the two procedures yield to same result
U_extended, s_extended, Vt_extended = np.linalg.svd(extended_data)
eigenvectors_close_extended = np.allclose(eigenvectors_extended, Vt_extended.T, rtol=1e-3, atol=1e-3)
print("The procedures lead to a close result?", eigenvectors_close)

#calculate explained variance ratio for the extended dataset
explained_var_ratio_extended = eigenvalues_extended / np.sum(eigenvalues_extended)
print("\nExplained Variance Ratio (Extended):", explained_var_ratio_extended)

#calculate cumulative explained variance for the extended dataset
cumulative_var_ratio_extended = np.cumsum(explained_var_ratio_extended)
print("\nCumulative Explained Variance Ratio (Extended):", cumulative_var_ratio_extended)

#find the number of components required to retain 99% of the variability for the extended dataset
num_components_extended = np.argmax(cumulative_var_ratio_extended >= 0.99) + 1
print("\nNumber of components to retain 99% variability (Extended):", num_components_extended)

#compare with the number of components from the previous exercise
print("\nNumber of components to retain 99% variability (Original):", num_components_99_percent)
##############################END OF PCA ON A nD DATASET.#######################################