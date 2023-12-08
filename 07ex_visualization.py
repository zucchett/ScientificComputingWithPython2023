import pandas as pd
import numpy as np
import seaborn as sns
import pickle
import matplotlib.pyplot as plt
import itertools
import scipy

#Load the CSV file into a pandas DataFrame
file_path = './regression_generated.csv'
data = pd.read_csv(file_path)

features = ['features_1', 'features_2', 'features_3']
combinations = list(itertools.combinations(features, 2))

for feature_x, feature_y in combinations:
    plt.figure(figsize=(8, 6))
    plt.scatter(data[feature_x], data[feature_y])
    plt.xlabel(feature_x)
    plt.ylabel(feature_y)
    plt.title(f'Scatter plot: {feature_x} vs {feature_y}')
    plt.show()

correlation_matrix = data[features].corr()

print("Correlation Matrix:\n",correlation_matrix)

print("The values of all correlations between all features are very low and this is a clear indicator of a very weak correlation between them.")

##############################END OF SPOTTING CORRELATIONS.#######################################

def generate_2d_gaussian(mean, cov_matrix, num_samples):
    samples = np.random.multivariate_normal(mean, cov_matrix, size=num_samples)
    return samples

#here we set the mean, covariance matrix and number of samples for category 1
mean_1 = [2, 3]
cov_matrix_1 = [[1, 0.5], [0.5, 1]]
num_samples_category_1 = 100

#here we set the mean, covariance matrix and number of samples for category 2
mean_2 = [4, 5]
cov_matrix_2 = [[1.2, 0.3], [0.3, 1.5]]
num_samples_category_2 = 100

category_1 = np.random.multivariate_normal(mean_1, cov_matrix_1, size=num_samples_category_1)
category_2 = np.random.multivariate_normal(mean_2, cov_matrix_2, size=num_samples_category_2)

plt.figure(figsize=(8, 6))
plt.scatter(category_1[:, 0], category_1[:, 1], color='blue', label='Category 1')
plt.scatter(category_2[:, 0], category_2[:, 1], color='red', label='Category 2')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2D Dataset with Two Categories')
plt.legend()
plt.grid(True)
plt.show()

##############################END OF COLOR-CODED SCATTER PLOT.#######################################

# with open('residuals_261.pkl', 'rb') as f:
#     data = pickle.load(f)

######### I COULD NOT CORRECTLY CONVERT THE 'DATA' VARIABLE INTO pd.DataFrame, AND I COULD NOT FIGURE OUT WHAT WAS CAUSING THE ERROR
# df = pd.DataFrame(data) ############### THIS LINE WAS THE PROBLEM

# cleaned_df = df[abs(df['residuals']) < 2]

##############################END OF PROFILE PLOT.#######################################

#normally distributed data
np.random.seed(8)
N = 100
mean = 5
std = 2
x = np.random.normal(mean, std, N)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
hist, bins, _ = plt.hist(x, bins=10, alpha=0.7, label='Histogram')
errors = np.sqrt(hist)

plt.ylabel('Frequency')
plt.yticks(np.arange(0, max(hist) + 1, 2))

#plot each gaussian function
plt.subplot(1, 2, 2)
x_values = np.linspace(min(x), max(x), 1000)

std_param = 1.06 * np.std(x) * N ** (-1 / 5)
gaussians = []
for value in x:
    gaussian = scipy.stats.norm.pdf(x_values, value, std_param)
    plt.plot(x_values, gaussian, 'r-', alpha=0.1)
    gaussians.append(gaussian)

sum_gaussians = np.sum(gaussians, axis=0)
normalized_sum = sum_gaussians * (np.sum(hist) / scipy.integrate.trapz(sum_gaussians, x=x_values))

plt.subplot(1, 2, 1)
plt.plot(x_values, normalized_sum, 'k-', label='Normalized Sum of Gaussians')
plt.legend()

plt.tight_layout()
plt.show()

##############################END OF KERNEL DENSITY ESTIMATE.#######################################