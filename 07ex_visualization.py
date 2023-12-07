print("============== 1. Spotting correlations ==============")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
url = 'https://www.dropbox.com/s/aamg1apjhclecka/regression_generated.csv'
df = pd.read_csv("regression_generated.csv")
selected_features = ['features_1', 'features_2', 'features_3']
sns.pairplot(df[selected_features])
plt.suptitle('Scatter Plots for Selected Features')
plt.show()
correlation_matrix = df[selected_features].corr()
print("Correlation Matrix:", correlation_matrix)
# Interpretation of the confusion matrix:
# feature1 X feature2 = -0.00522 this value is very close to 0 which indicates a weak negative correlation between both of them.
# feature1 X feature3 = 0.02369 this value is very close to 0. This indicates a weak negative correlation between both of them.
# feature2 X feature3 = 0.04736 this value is very close to 0. This indicates a weak negative correlation between both of them.

print("============== 2. Color-coded scatter plot ==============")
import numpy as np
def generate_dataset(num_samples, mean1, std_dev1, mean2, std_dev2):
    category1_samples = np.random.normal(mean1, std_dev1, size=(num_samples, 2))
    category2_samples = np.random.normal(mean2, std_dev2, size=(num_samples, 2))
    dataset = np.vstack([category1_samples, category2_samples]) # combining the samples
    labels = np.hstack([np.zeros(num_samples), np.ones(num_samples)]) # Create labels for the categories (0 for category 1, 1 for category 2)
    return dataset, labels

if __name__ == "__main__":

    mean1, std_dev1 = [1, 2], [1, 1]
    mean2, std_dev2 = [4, 5], [1.5, 1]
    dataset, labels = generate_dataset(100, mean1, std_dev1, mean2, std_dev2)
    print(dataset)
    plt.scatter(dataset[:, 0], dataset[:, 1], c=labels, cmap='nipy_spectral',  edgecolors='k', marker='o', alpha=0.5)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Scatter Plot of 2D Dataset with Two Categories')
    plt.show()

print("============== 3. Profile plot ==============")
import pickle
# we read pkl files using the pickle library
with open('residuals_261.pkl', 'rb') as file:
    data3 = pickle.load(file)

print(data3)
df3 = pd.DataFrame(data3, columns=['residuals', 'distances']) #definig the dataframe
cleaned_df = df3[abs(df3[0]) < 2] #filtering the dataframe
joint_plot = sns.jointplot(x='distances', y='residuals', data=cleaned_df, kind='reg', height=7) #visualizing
plt.show()

print("============== 4. Kernel Density Estimate ==============")
x = np.random.normal(0, 1, 100) # the array x is filled with a variable normally distributed
hist, edges = np.histogram(x, bins=10, density=True) # creating the histogram of the data with 10 bins, normalized to form a probability density
fig, ax = plt.subplots() #create the subplots
ax.set_xlabel('value') # setting the labels for the x axis
ax.set_ylabel('frequency') # setting the labels for the y axis
ax.set_yticks(np.arange(0, 0.4, 0.1)) #defining y as an intervals of 0.1 from 0 to 0.4
ax.set_yticklabels(np.arange(0, 40, 10).astype(int)) #defining x as an intervals of 0 from 0 to 40
ax.legend() # we add a legend
standart_deviation= 1.06 * x.std() * 100**(-1/5) # the standard deviation formula

