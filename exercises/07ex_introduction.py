import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Spotting correlations
print('1. Spotting correlations')

csv_file_path = 'data/regression_generated.csv'
df = pd.read_csv(csv_file_path)
features_to_plot = ['features_1', 'features_2', 'features_3']

sns.set(style="ticks")
sns.pairplot(df[features_to_plot])
plt.show()

# 2. Color-coded scatter plot
print('Color-coded scatter plot')


def generate_2d_dataset(mean1, std1, mean2, std2, size_per_category):
    category1 = np.random.normal(loc=mean1, scale=std1, size=(size_per_category, 2))
    category2 = np.random.normal(loc=mean2, scale=std2, size=(size_per_category, 2))
    labels = np.concatenate([np.zeros(size_per_category), np.ones(size_per_category)])
    dataset = np.vstack([category1, category2])

    return dataset, labels


def plot_color_coded_scatter(dataset, labels):
    plt.scatter(dataset[:, 0], dataset[:, 1], c=labels, cmap='viridis', marker='o', edgecolors='k')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Color-Coded Scatter Plot')
    plt.show()


mean1 = [2, 3]
std1 = [1, 1]
mean2 = [8, 7]
std2 = [1.5, 1.5]
size_per_category = 50

dataset, labels = generate_2d_dataset(mean1, std1, mean2, std2, size_per_category)
plot_color_coded_scatter(dataset, labels)
