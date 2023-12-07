#!/usr/bin/env python
# coding: utf-8

# 1\. **Reductions**
# 
# Given the following matrix:
# 
# ```python
# m = np.arange(12).reshape((3,4))
# ```
# 
#    1. find the total mean
#    2. find the mean for each row and column

# In[1]:
print("****************************************1.********************************************************")

import numpy as np
m = np.arange(12).reshape((3,4))
print("mean:",  np.mean(m))
print("sum along the columns:", m.mean(axis=0))
print("sum along the rows:", m.mean(axis=1))


# 2\. **Outer product**
# 
# Find the outer product of the following vectors:
# 
# ```python
# u = np.array([1, 3, 5, 7])
# v = np.array([2, 4, 6, 8])
# ```
# 
# Use different methods to do this:
# 
#    1. Using the function `outer` in numpy
#    2. Using a nested `for` loop or a list comprehension
#    3. Using numpy broadcasting operations

# In[2]:
print("****************************************2.********************************************************")

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])


# In[9]:


from numpy import array, newaxis
first = np.outer(u, v)
second = np.array([i * v for i in u])
third=u[:,newaxis] * v
print("Using the function outer in numpy : ", '\n', first, '\n')
print("Using list comprehension : ", '\n',second, '\n')
print("Using numpy broadcasting operations : ", '\n', third, '\n')


# 3\. **Matrix masking**
# 
# Create a $10 \times 6$ matrix of float random numbers, distributed between 0 and 3 according to a flat distribution.
# 
# After creating the matrix, set all entries $< 0.3$ to zero using a mask.

# In[5]:

print("****************************************3.********************************************************")
x=np.random.uniform(low=0.0, high=3.0, size=(10,6))
print("original array : ", '\n', x , '\n')
mask = (x < 0.3)
print("after the mask:", '\n' , mask, '\n')
x[x < 0.3 ] = 0
print("the modified array:", '\n', x, '\n')



# 4\. **Trigonometric functions**
# 
# Use `np.linspace` to create an array of 100 numbers between $0$ and $2\pi$ (inclusive).
# 
#   * Extract every 10th element using the slice notation
#   * Reverse the array using the slice notation
#   * Extract elements where the absolute difference between the `sin` and `cos` functions evaluated for that element is $< 0.1$
#   * **Optional**: make a plot showing the `sin` and `cos` functions and indicate graphically (with a line or a marker) where they are close

# In[21]:

print("****************************************4.********************************************************")
arr=np.linspace(0, 2*np.pi, num=100)
every_10th_element = arr[10::10]
reversed_arr = arr[::-1]

indices = np.where(np.abs(np.sin(arr) - np.cos(arr)) < 0.1)
selected_elements = arr[indices]
print("Use np.linspace to create an array of 100 numbers between 0 and 2𝜋 (inclusive):\n", '\n',arr, '\n', '\n')
print("Reverse the array using the slice notation:\n", '\n',reversed_arr, '\n', '\n')
print("Extract every 10th element using the slice notation :\n", '\n',every_10th_element, '\n', '\n')
print("Extract elements where the absolute difference between sin and cos is < 0.1 : \n", '\n',selected_elements, '\n', '\n')



# In[28]:
print("****************************************OPTIONALPART********************************************************")

#Optional part
import matplotlib.pyplot as plt

plt.plot(arr, np.sin(arr), label='sin(x)')
plt.plot(arr, np.cos(arr), label='cos(x)')
plt.scatter(selected_elements, np.sin(selected_elements), c='red', marker='o', label='|sin(x) - cos(x)| < 0.1')
plt.legend()


# 5\. **Matrices**
# 
# Create a matrix that shows the $10 \times 10$ multiplication table.
# 
#  * Find the trace of the matrix
#  * Extract the anti-diagonal matrix (this should be ```array([10, 18, 24, 28, 30, 30, 28, 24, 18, 10])```)
#  * Extract the diagonal offset by 1 upwards (this should be ```array([ 2,  6, 12, 20, 30, 42, 56, 72, 90])```)

# In[20]:

print("****************************************5.********************************************************")
multiplication_table = np.outer(np.arange(1, 11), np.arange(1, 11))
trace_mt = np.trace(multiplication_table)
anti_diagonal_mt = np.diag(np.fliplr(multiplication_table))
offset_diagonal_mt = np.diag(multiplication_table, k=1)

print("Multiplication Table:\n", multiplication_table)
print("\nTrace of the matrix:", trace_mt)
print("\nAnti-diagonal matrix:\n", anti_diagonal_mt)
print("\nDiagonal offset by 1 upwards:\n", offset_diagonal_mt)


# 6\. **Broadcasting**
# 
# Use broadcasting to create a grid of distances.
# 
# Route 66 crosses the following cities in the US: Chicago, Springfield, Saint-Louis, Tulsa, Oklahoma City, Amarillo, Santa Fe, Albuquerque, Flagstaff, Los Angeles.
# 
# The corresponding positions in miles are: `0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448`
# 
#   * Build a 2D grid of distances among each city along Route 66
#   * Convert the distances in km

# In[22]:
print("****************************************6.********************************************************")

cities = ["Chicago", "Springfield", "Saint-Louis", "Tulsa", "Oklahoma City", "Amarillo", "Santa Fe", "Albuquerque", "Flagstaff", "Los Angeles"]

# Corresponding positions in miles
mile_positions = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])

# Build a 2D grid of distances among each city along Route 66 using broadcasting
distance_matrix_miles = np.abs(mile_positions - mile_positions[:, np.newaxis])

# Conversion factor from miles to kilometers
miles_to_km = 1.60934

# Convert the distances to kilometers
distance_matrix_km = distance_matrix_miles * miles_to_km

# Print the results
print("Cities:", cities)
print("\nDistance Matrix (Miles):\n", distance_matrix_miles)
print("\nDistance Matrix (Kilometers):\n", distance_matrix_km)


# 7\. **Prime numbers sieve**
# 
# Compute the prime numbers in the 0-N (start with N=99) range with a sieve (mask).
# 
#   * Construct a shape (N,) boolean array, which is the mask
#   * Identify the multiples of each number starting from 2 and set accordingly the corresponding mask element
#   * Apply the mask to obtain an array of ordered prime numbers
#   * Check the performances (with `timeit`); how does it scale with N?
#   * Implement the optimization suggested in the [sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

# In[29]:
print("****************************************7.********************************************************")

import timeit

def sieve_of_eratosthenes(N):
    is_prime = np.ones(N + 1, dtype=bool)
    is_prime[0:2] = False  # 0 and 1 are not primes

    for i in range(2, int(np.sqrt(N)) + 1):
        if is_prime[i]:
            is_prime[i*i : N+1 : i] = False

    primes = np.nonzero(is_prime)[0]
    return primes

# Set N to 99
N = 99

# Measure the time it takes to compute prime numbers using the sieve
time_taken = timeit.timeit(lambda: sieve_of_eratosthenes(N), number=1000)

print(f"Prime numbers up to {N}:", sieve_of_eratosthenes(N))
print(f"Time taken for N={N}: {time_taken:.6f} seconds")


# 8\. **Diffusion using random walk**
# 
# Consider a simple random walk process: at each step in time, a walker jumps right or left (+1 or -1) with equal probability. The goal is to find the typical distance from the origin of many random walkers after a given amount of time.
# 
# *Hint*: create a 2D array where each row represents a walker, and each column represents a time step.
# 
#   * Take 1000 walkers and let them walk for 200 steps
#   * Use `randint` to create a 2D array of size $walkers \times steps$ with values -1 or 1
#   * Calculate the walking distances for each walker (e.g. by summing the elements in each row)
#   * Take the square of the previously-obtained array (element-wise)
#   * Compute the mean of the squared distances at each step (i.e. the mean along the columns)
#   * **Optional**: plot the average distances ($\sqrt(distance^2)$) as a function of time (step)

# In[34]:

print("****************************************8.********************************************************")
num_walkers = 1000
num_steps = 200

# Create a 2D array representing the random walk steps
walkers = np.random.choice([-1, 1], size=(num_walkers, num_steps))

# Calculate the walking distances for each walker
distances = np.cumsum(walkers, axis=1)

# Take the square of the distances
squared_distances = distances**2

# Compute the mean of the squared distances at each step
mean_squared_distances = np.mean(squared_distances, axis=0)

# Calculate the square root of the mean squared distances to get the average distance
average_distances = np.sqrt(mean_squared_distances)
print("****************************************OPTIONALPART********************************************************")
# Optional part: Plot the average distances as a function of time
plt.plot(average_distances)
plt.xlabel('Time Step')
plt.ylabel('Average Distance')
plt.title('Average Distance of Random Walkers over Time')
plt.show()


# In[ ]:




