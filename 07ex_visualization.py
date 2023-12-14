import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pickle
import scipy
from scipy.integrate import trapz

def ex1():
	print("Spotting correalations")
	data = pd.read_csv('regression_generated.csv')

	features = ['features_1', 'features_2', 'features_3']

	# Создание всех возможных комбинаций диаграмм рассеяния
	pd.plotting.scatter_matrix(data[features], figsize=(10, 8))
	plt.suptitle('Scatter Plots for Selected Features')
	plt.show()
	
	correlation_matrix = data[features].corr()
	print(correlation_matrix)
	print("Most correlation coefficients are close to zero. This indicates that there is no strong linear dependence between pairs of features")
	
def ex2():
	samples = 50
	mean1 = (4, 1)
	std1 = (1, 2)
	mean2 = (2, 1)
	std2 = (3, 4) 

	def generate_dataset(samples, mean1, std1, mean2, std2):
		category1 = np.random.normal(mean1, std1, size=(samples, 2)) 
		category2 = np.random.normal(mean2, std2, size=(samples, 2))
		return category1, category2

	def plot_color(category1, category2):
		plt.scatter(category1[:, 0], category1[:, 1], color='blue', label='Category 1')
		plt.scatter(category2[:, 0], category2[:, 1], color='red', label='Category 2')
		plt.xlabel('Feature 1')
		plt.ylabel('Feature 2')
		plt.title('Color-coded scatter plot')
		plt.legend()
		plt.show()
		
	print("Color-coded scatter plot")
	category1, category2 = generate_dataset(samples, mean1, std1, mean2, std2)
	plot_color(category1, category2)

		
def ex3():
	print("3. Profile plot")
	
	file_path = 'residuals_261.pkl'
	with open(file_path, 'rb') as file:
		data = pickle.load(file)

	print(data)
	data = pd.DataFrame.from_dict(data.item())
	df = data[data['residuals'] < 2]
	sns.jointplot(data=df, x='distances', y='residuals', kind="reg")
	plt.show()
	
	h, xedges, patches = plt.hist(df['distances'], bins=30)
	x = (xedges[:-1] + xedges[1:]) / 2
	df['bins'] = pd.cut(df['distances'], bins=xedges, labels=False)
	y = df.groupby('bins')['residuals'].mean().values
	err_y = df.groupby('bins')['residuals'].std().values
	
	plt.scatter(df['distances'], df['residuals'])
	plt.errorbar(x, y, yerr=err_y, fmt='o', c='red', label='Profile Plot')
	plt.xlabel('Distance')
	plt.ylabel('Residuals')
	plt.legend()
	plt.title('Profile Plot of Residuals vs Distance')
	plt.show()
	
def ex4():
	print("4. Kernel Density Estimate")
	x = np.random.normal(0, 1, 100) 
	hist, bin_edges = np.histogram(x, bins=20)
	
	bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
	poisson_errors = np.sqrt(hist)
	plt.bar(bin_centers, hist, width=bin_edges[1] - bin_edges[0], yerr=poisson_errors)
	plt.xlabel('value')
	plt.ylabel('frequency')
	plt.yticks(np.arange(0, max(hist) + 2, 2))
	plt.show()
	
	
	standart_deviation = 1.06 * x.std() * 100**(-1/5)
	grid  = np.linspace(min(x), max(x), 300)
	kernels = []
	for elem in x:
		kernel = scipy.stats.norm(elem, standart_deviation).pdf(grid)
		kernels.append(kernel)
		plt.plot(grid, kernel, lw=1)
	plt.show()
	
	sum_of_gaussians = np.sum(kernels, axis=0)
	integral_hist = trapz(hist, bin_centers)
	integral_gaussians = trapz(sum_of_gaussians, grid)
	normalized_sum = sum_of_gaussians * integral_hist / integral_gaussians

	plt.bar(bin_centers, hist, width=bin_edges[1] - bin_edges[0], yerr=poisson_errors, label='Original Histogram')
	plt.plot(grid, normalized_sum, 'r', label='Normalized Sum of Gaussians')
	plt.xlabel('value')
	plt.ylabel('frequency')
	plt.legend()
	plt.show()
ex1()
ex2()	
ex3()
ex4()