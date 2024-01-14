from scipy.stats import poisson
import numpy as np
from scipy import stats, optimize
import matplotlib.pyplot as plt
import pandas as pd
import pickle

historic_average = 6.3
k = 15
probability_less_than_15 = poisson.cdf(k - 1, historic_average)
probability_15_or_more = 1 - probability_less_than_15

print(f"The probability of observing 15 or more hurricanes in a single year is: {probability_15_or_more*100:.2f}%")
print("##############################END OF Hurricanes per Year.#######################################\n")

##############################END OF Hurricanes per Year.#######################################

pre = np.array([120, 132, 120, 110, 115, 128, 120, 112, 110, 100])
post = np.array([140, 156, 145, 130, 117, 148, 137, 119, 127, 135])
differences = post - pre

mean_diff = np.mean(differences)
std_dev_diff = np.std(differences, ddof=1)

n = len(differences)

#calculate the t-statistic and p-value, also set an arbitrary value to check if the change was significant 
t = mean_diff / (std_dev_diff * (2 / np.sqrt(n)))
df = n - 1
p_value = stats.t.sf(np.abs(t), df) * 2 
value = 0.05

print(f"T-statistic: {t:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < value:
    print("The change in blood pressures within the sample is statistically significant.")
else:
    print("There is no statistically significant change in blood pressures within the sample.")

print("##############################END OF Pairwise t-test.#######################################\n")

##############################END OF Pairwise t-test.#######################################
    
months = np.arange(12)
max_temps = np.array([17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18])
min_temps = np.array([-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58])

#1st plot the temperatures
plt.figure(figsize=(8, 6))
plt.scatter(months, max_temps, color='red', label='Max Temperatures')
plt.scatter(months, min_temps, color='blue', label='Min Temperatures')
plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Extremes in Alaska')
plt.legend()
plt.show()

def fit_func(x, a, b, c, d):
    return a * np.sin(b * x + c) + d

popt_max, _ = optimize.curve_fit(fit_func, months, max_temps, bounds=([0, 0.1, -np.pi, -np.inf], np.inf))
popt_min, _ = optimize.curve_fit(fit_func, months, min_temps, bounds=([0, 0, -np.pi, -np.inf], np.inf))

#ploting the temperatures + the fitted curve
plt.figure(figsize=(8, 6))
plt.scatter(months, max_temps, color='red', label='Max Temperatures')
plt.scatter(months, min_temps, color='blue', label='Min Temperatures')
plt.plot(months, fit_func(months, *popt_max), color='orange', label='Fitted Max Temp Curve')
plt.plot(months, fit_func(months, *popt_min), color='green', label='Fitted Min Temp Curve')
plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.title('Fitted Curves for Temperature Extremes in Alaska')
plt.legend()
plt.show()

print(f"Fitted parameters for Max Temp: {popt_max}")
print(f"Fitted parameters for Min Temp: {popt_min}")

print("##############################END OF Curve fitting of temperature in Alaska.#######################################\n")
##############################END OF Curve fitting of temperature in Alaska.#######################################
####I could not load successfully the data
# with open('data/residuals_261.pkl', 'rb') as file:
#     data = pickle.load(file)

# residuals = data['residual']

##############################END OF Fit the residues.#######################################

# Load the data from the file
data = np.loadtxt('data/munich_temperatures_average_with_bad_data.txt')

# Extract time and temperature from the data
time = data[:, 0]
temperature = data[:, 1]

def model_function(t, a, b, c):
    return a * np.cos(2 * np.pi * t + b) + c

plot_start_year = 2008
plot_end_year = 2012
mask = (time >= plot_start_year) & (time <= plot_end_year)

#fit the model to the data
params, covariance = optimize.curve_fit(model_function, time[mask], temperature[mask])

fit_time = np.linspace(plot_start_year, plot_end_year, 1000)
fit_temperature = model_function(fit_time, *params)

#best-fit parameter values and their errors
a_fit, b_fit, c_fit = params
a_uncertainty, b_uncertainty, c_uncertainty = np.sqrt(np.diag(covariance))

average_temperature = np.mean(temperature)
coldest_time = np.argmin(model_function(time, a_fit, b_fit, c_fit))
hottest_time = np.argmax(model_function(time, a_fit, b_fit, c_fit))

coldest_prediction = model_function(time[coldest_time], a_fit, b_fit, c_fit)
hottest_prediction = model_function(time[hottest_time], a_fit, b_fit, c_fit)

#results
print("Best-fit values of the parameters:")
print(f"a: {a_fit} +- {a_uncertainty}")
print(f"b: {b_fit} +- {b_uncertainty}")
print(f"c: {c_fit} +- {c_uncertainty}\n")

print(f"Overall average temperature in Munich: {average_temperature}°C")
print(f"Coldest time of year: {coldest_prediction}°C")
print(f"Hottest time of year: {hottest_prediction}°C")

plt.figure(figsize=(10, 6))
plt.scatter(time, temperature, label='Data')
plt.plot(fit_time, fit_temperature, label='Best-fit Model', color='red')
plt.title('Temperature in Munich (2008-2012)')
plt.xlabel('Time (years)')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()

# The 'b' parameter in the model function represents the phase shift of the cosine model function.
# It determines how the cosine wave is shifted along the time axis. In the context of temperature modeling, can be set
# to represent the time of the year when the temperature reaches its maximum or minimum value.

##############################END OF Temperatures in Munich.#######################################