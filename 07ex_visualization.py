#---------------------------------------------------------------------------------------------------------------
# exercise 7.PART ONE.Spotting correlations


import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt

file_path = '.data/regression_generated.csv'

# Read the CSV file
data = pd.read_csv(file_path, header=None)

# Display the first few rows to check the structure
print("Data Structure:")
print(data.head())

# Create scatter plots for each pair of features
features = data.columns[:-1]  # Exclude the last column if it represents the target variable

# Create subplots for scatter plots
fig, axes = plt.subplots(nrows=len(features), ncols=len(features), figsize=(12, 12))

# Adjust spacing between subplots
fig.tight_layout()

# Create scatter plots for each pair of features
for i, feature1 in enumerate(features):
    for j, feature2 in enumerate(features):
        if i != j:
            axes[i, j].scatter(data[feature1], data[feature2])
            axes[i, j].set_xlabel(feature1)
            axes[i, j].set_ylabel(feature2)
            axes[i, j].set_title(f"Scatter Plot: {feature1} vs {feature2}")

# Show the plots
plt.show()

#---------------------------------------------------------------------------------------------------------------
# exercise 7.PART TWO.Color-coded scatter plot


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# Write a function that generates a 2D dataset consisting of 2 categories.
def generate_2d_gaussian_data(num_points, mean, std_dev):
    np.random.seed(42)
    data = np.random.normal(loc=mean, scale=std_dev, size=(num_points, 2))
    return data

# Display the dataset in a scatter plot marking the two categories with different marker colors.
def plot_2d_gaussian_data(category_1_data, category_2_data):
    plt.scatter(category_1_data[:, 0], category_1_data[:, 1], label='Category 1', color='blue')
    plt.scatter(category_2_data[:, 0], category_2_data[:, 1], label='Category 2', color='orange')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('2D Gaussian Distributed Data')
    plt.legend()
    plt.show()

# Define parameters for the two categories
mean_category_1 = [2, 3]
std_dev_category_1 = [1, 0.5]

mean_category_2 = [6, 5]
std_dev_category_2 = [0.5, 1]

# Generate data for the two categories
category_1_data = generate_2d_gaussian_data(50, mean_category_1, std_dev_category_1)
category_2_data = generate_2d_gaussian_data(50, mean_category_2, std_dev_category_2)

# Create and display the scatter plot
plot_2d_gaussian_data(category_1_data, category_2_data)

#---------------------------------------------------------------------------------------------------------------
# exercise 7.PART THREE.Profile plot


import matplotlib
matplotlib.use('Agg')

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate some random data
np.random.seed(0)
n = 100
distances = np.random.normal(size=n)
residuals = distances + np.random.normal(size=n)

# Create a Pandas DataFrame
dataframe = pd.DataFrame({
    'distances': distances,
    'residuals': residuals
})

# Calculate absolute residuals
absolute_residuals = np.abs(dataframe['residuals'])

# Create a boolean mask based on the condition
mask = absolute_residuals < 2

# Apply the mask to filter the DataFrame
filtered_data = dataframe[mask]

# Plot a Seaborn jointplot of "residuals" versus "distances", and use seaborn to display a linear regression
sns.jointplot(x='distances', y='residuals', data=dataframe, kind='reg')

# Manually create the profile histogram for the "distance" variable
bins = np.linspace(-5, 5, 11)

# Calculate the histogram
hist = np.histogram(dataframe['distances'], bins=bins)

# Unpack the results
hist, bin_edges = hist

# Calculate the left and right bin edges
left_edges = bin_edges[:-1]
right_edges = bin_edges[1:]

# Calculate the bin centers
bin_centers = (left_edges + right_edges) / 2

# Obtain 3 numpy arrays:
x = bin_centers

# Initialize an empty list to store results
y = []

# Iterate over bins
for i in range(len(bins) - 1):
    # Define the current bin range condition
    bin_range_condition = (dataframe['distances'] >= bins[i]) & (dataframe['distances'] < bins[i + 1])

    # Extract data within the current bin
    data_in_bin = dataframe[bin_range_condition]

    # Calculate the mean of 'residuals' in the current bin and append to the list
    y.append(np.mean(data_in_bin['residuals']))

# Initialize an empty list to store results
err_y = []

# Iterate over bins
for i in range(len(bins) - 1):
    # Define the lower and upper bin edges
    lower_edge, upper_edge = bins[i], bins[i + 1]

    # Extract data within the current bin
    data_in_bin = dataframe[(dataframe['distances'] >= lower_edge) & (dataframe['distances'] < upper_edge)]

    # Calculate the standard deviation of 'residuals' in the current bin and append to the list
    err_y.append(np.std(data_in_bin['residuals']))

# Plot the profile plot on top of the scatter plot
plt.figure(figsize=(10, 6))
sns.jointplot(x='distances', y='residuals', data=dataframe, kind='reg')
plt.plot(x, y, 'o', label='Profile mean')
plt.errorbar(x, y, yerr=err_y, fmt='none', ecolor='red', label='Profile std')
plt.xlabel('Distance')
plt.ylabel('Residual')
plt.legend()
plt.savefig('.data/jointplot.png')

#---------------------------------------------------------------------------------------------------------------
# exercise 7.PART FOUR.Kernel Density Estimate


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.integrate import trapz
import matplotlib
matplotlib.use('TkAgg')

# Define the number of data points
N = 100

# Define the mean and standard deviation of the normal distribution
mean = 0
standard = 1

# Generate a normally distributed sample
x = np.random.normal(mean, standard, N)

# Define the number of bins for the histogram
bins_num = 10

# Create the histogram
fig, axis = plt.subplots(figsize=(12, 6))
n, bins, patches = axis.hist(x, bins_num, histtype="step", fill=False)

# Set the y-axis label
axis.set_ylabel("Frequency")

# Set the y-axis major ticks labels
axis.set_yticks(np.arange(min(n), max(n) + 1, 1))

# Set the title of the histogram plot
axis.set_title("Histogram of the normally distributed data")

# Compute the standard deviation using Scott's rule
sigma = 1.06 * x.std() * pow(x.size, -1 / 5)

# Create a list of Gaussian functions
gaussian_functions = []

# Iterate over the data points
for xi in x:
    # Create a Gaussian function with the mean corresponding to the data point value and the standard deviation
    gaussian = stats.norm(xi, sigma)
    gaussian_functions.append(gaussian)

# Create a separate plot for the Gaussian functions
fig, ax2 = plt.subplots(figsize=(12, 6))

# Iterate over the Gaussian functions and plot them
for gaussian in gaussian_functions:
    ax2.plot(bins, gaussian.pdf(bins))

# Set the title of the Gaussian functions plot
ax2.set_title("Gaussian functions")

# Compute the sum of the Gaussian functions
sum_of_gaussians = np.sum([gaussian.pdf(bins) for gaussian in gaussian_functions], axis=0)

# Normalize the sum of the Gaussian functions
normalized_sum_of_gaussians = sum_of_gaussians / trapz(sum_of_gaussians, bins)

# Superimpose the normalized sum of all gaussians to the first histogram
fig, ax3 = plt.subplots(figsize=(12, 6))
ax3.hist(x, bins_num, histtype="step", fill=False)
ax3.plot(bins, normalized_sum_of_gaussians)

# Set the title of the superimposed plot
ax3.set_title("Superimposed histogram and normalized sum of Gaussian functions")
plt.show()

#---------------------------------------------------------------------------------------------------------------