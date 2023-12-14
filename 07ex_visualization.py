#!/usr/bin/env python
# coding: utf-8

# 1\. **Spotting correlations**
# 
# Load the remote file:
# 
# ```bash
# https://www.dropbox.com/s/aamg1apjhclecka/regression_generated.csv
# ```
# 
# with Pandas and create scatter plots with all possible combinations of the following features:
#     
#   + `features_1`
#   + `features_2`
#   + `features_3`
#   
# Are these features correlated? Please add a comment.

# In[ ]:


get_ipython().system('wget https://www.dropbox.com/s/aamg1apjhclecka/regression_generated.csv -P data/')


# In[20]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/regression_generated.csv')

plt.subplot(1,3,1)
plt.scatter(df.loc[:,'features_1'], df.loc[:,'features_2'])
plt.subplot(1,3,2)
plt.scatter(df.loc[:,'features_1'], df.loc[:,'features_3'])
plt.subplot(1,3,3)
plt.scatter(df.loc[:,'features_2'], df.loc[:,'features_3'])



# 2\. **Color-coded scatter plot**
# 
# Produce a scatter plot from a dataset with two categories.
# 
# * Write a function that generates a 2D dataset consisting of 2 categories. Each category should distribute as a 2D gaussian with a given mean and standard deviation. Set different values of the mean and standard deviation between the two samples.
# * Display the dataset in a scatter plot marking the two categories with different marker colors.
# 
# An example is given below:

# In[1]:


from IPython.display import Image
Image('images/two_categories_scatter_plot.png')


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

def generate_2d_gaussian(mean, std_dev, num_samples):
    return np.random.multivariate_normal(mean, std_dev*np.eye(2), num_samples)

def generate_2d_dataset(category1_mean, category1_std_dev, category2_mean, category2_std_dev, num_samples_per_category):
    category1_data = generate_2d_gaussian(category1_mean, category1_std_dev, num_samples_per_category)
    category2_data = generate_2d_gaussian(category2_mean, category2_std_dev, num_samples_per_category)
    
    labels_category1 = np.zeros(num_samples_per_category, dtype=int)
    labels_category2 = np.ones(num_samples_per_category, dtype=int)
    
    dataset = np.concatenate((category1_data, category2_data))
    labels = np.concatenate((labels_category1, labels_category2))
    
    return dataset, labels

def plot_scatter(dataset, labels):
    category1_mask = (labels == 0)
    category2_mask = (labels == 1)
    
    plt.scatter(dataset[category1_mask, 0], dataset[category1_mask, 1], c='blue', label='Category 1')
    plt.scatter(dataset[category2_mask, 0], dataset[category2_mask, 1], c='red', label='Category 2')
    
    plt.title('Scatter Plot of 2D Dataset with Two Categories')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.show()

# Set parameters for the two categories
category1_mean = [1, 1]
category1_std_dev = 0.5

category2_mean = [4, 4]
category2_std_dev = 0.8

num_samples_per_category = 100

# Generate dataset and labels
dataset, labels = generate_2d_dataset(category1_mean, category1_std_dev, category2_mean, category2_std_dev, num_samples_per_category)

# Plot scatter plot
plot_scatter(dataset, labels)


# 3\. **Profile plot**
# 
# Produce a profile plot from a scatter plot.
# * Download the following pickle file:
# ```bash
# wget https://www.dropbox.com/s/3uqleyc3wyz52tr/residuals_261.pkl -P data/
# ```
# * Inspect the dataset, you'll find two variables (features)
# * Convert the content to a Pandas Dataframe
# * Clean the sample by selecting the entries (rows) with the absolute values of the variable "residual" smaller than 2
# * Plot a Seaborn `jointplot` of "residuals" versus "distances", and use seaborn to display a linear regression. 
# 
# Comment on the correlation between these variables.
# 
# * Create manually (without using seaborn) the profile histogram for the "distance" variable; choose an appropriate binning.
# * Obtain 3 numpy arrays:
#   * `x`, the array of bin centers of the profile histogram of the "distance" variable
#   * `y`, the mean values of the "residuals", estimated in slices (bins) of "distance"
#   * `err_y`, the standard deviation of the of the "residuals", estimated in slices (bins) of "distance"
# * Plot the profile plot on top of the scatter plot

# In[ ]:


get_ipython().system('wget https://www.dropbox.com/s/3uqleyc3wyz52tr/residuals_261.pkl -P data/')


# In[19]:


import numpy as np
import pandas as pd
import pickle

# Load the dataset from the pickle file
with open('data/residuals_261.pkl', 'rb') as file:
    data = pickle.load(file)

data = np.array(data)

#data.reshape(2)
# It's 1d and I can't reshape so I can't have the dataframe from the array from the pickle


# 4\. **Kernel Density Estimate**
# 
# Produce a KDE for a given distribution (by hand, not using seaborn):
# 
# * Fill a numpy array `x` of length N (with $N=\mathcal{O}(100)$) with a variable normally distributed, with a given mean and standard deviation
# * Fill an histogram in pyplot taking proper care of the aesthetic:
#    * use a meaningful number of bins
#    * set a proper y axis label
#    * set proper value of y axis major ticks labels (e.g. you want to display only integer labels)
#    * display the histograms as data points with errors (the error being the poisson uncertainty)
# * For every element of `x`, create a gaussian with the mean corresponding to the element value and the standard deviation as a parameter that can be tuned. The standard deviation default value should be:
# $$ 1.06 * x.std() * x.size ^{-\frac{1}{5}} $$
# you can use the scipy function `stats.norm()` for that.
# * In a separate plot (to be placed beside the original histogram), plot all the gaussian functions so obtained
# * Sum (with `np.sum()`) all the gaussian functions and normalize the result such that the integral matches the integral of the original histogram. For that you could use the `scipy.integrate.trapz()` method. Superimpose the normalized sum of all gaussians to the first histogram.
# 

# In[1]:


import numpy as np

mu, sigma = 0, 0.1 # mean and standard deviation
x = np.random.normal(mu, sigma, 100) # this is the normal distribution 

# Display the histogram of the samples, along with the probability density function
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(x, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()

