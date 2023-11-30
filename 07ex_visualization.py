from IPython.display import Image
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Spotting correlations
filename = 'regression_generated.csv'
data = csv.reader(open(filename, newline=''), delimiter=',')
header = next(data)  # skip first line
dataset = list(data)
x_len = len(dataset[1])
y_len = len(dataset)
print(x_len, y_len)
features1 = list()
features2 = list()
features3 = list()
y = list()
for i in range(1, y_len):
    print(dataset[i][2])
    features1.append(dataset[i][1])
    features2.append(dataset[i][2])
    features3.append(dataset[i][3])
    y.append(i)

plt.scatter(features1, y)
plt.scatter(features2, y)
plt.scatter(features3, y)
plt.show()



# 2. Color-coded scatter plot


Image('images/two_categories_scatter_plot.png')

def cate(meanList, covList, N):
    data_1 = cate_data(meanList[0], covList[0], N)
    data_2 = cate_data(meanList[1], covList[1], N)
    return cate_df(data_1), cate_df(data_2)


def cate_data(mean, cov, N):
    return np.intrandom.multivariate_normal(mean, cov, N)


def cate_df(data):
    return pd.DataFrame(data, columns=["x", "y"])


mean = ([2, 3], [6, 9])
covariance = ([[-5, 0], [0, 5]], [[-3, 0], [0, 2]])
N = 500

df1, df2 = cate(mean, covariance, N)

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111)
ax.set_title("Scatter Plot", fontsize=20)
ax.scatter(x="x", y="y", data=df1, marker="*", c="red", s=100, alpha=0.7)
ax.scatter(x="x", y="y", data=df2, marker="*", c="black", s=100, alpha=0.7)
plt.show()



# 3. Profile plot


data = pd.read_pickle('residuals_261.pkl')
data_dictionary = data[()]

df = pd.DataFrame(data_dictionary)
print(df)

df_clean = df[df['residuals'].abs() < 2]


plot = sns.jointplot(x="distances", y="residuals", data=df_clean, kind="reg", color = "r" ,line_kws = {"color": "w"});
plot.set_axis_labels("Distances", "Residuals")




# 4. Kernel Density Estimate


arr = np.random.normal(scale=10, size=100)
print(arr)

fig, ax = plt.subplots(figsize=(5, 5))
y, bins, patches = plt.hist(arr, bins=25, density=True)

ax.set_title('Kernel Density')
ax.set_xlabel('x')

centers = 0.5 * (bins[:-1] + bins[1:])

fig.tight_layout()
plt.show()


#Superimpose the normalized sum of all gaussians to the first histogram
from scipy.stats import norm

loc = 0
std_dev = 5
size = 50
x = np.random.normal(loc=loc, scale=std_dev, size=size)
mean = x
std_dev = 1.06 * np.std(x) * len(x) ** (-1 / 5)
x_points = np.linspace(np.min(mean) - 3 * std_dev, np.max(mean) + 3 * std_dev, 100)
y_points = np.array([norm.pdf(x_points, mean[i], std_dev) for i in range(len(x))])
for i in y_points: plt.plot(x_points, i)
plt.xlabel('Gaussian Samples')
plt.ylabel('Counts')

plt.show()

