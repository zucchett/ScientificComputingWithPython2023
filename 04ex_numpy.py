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

# In[2]:


import numpy as np

m = np.arange(12).reshape((3,4))
mean = m.mean()
print(f"The matrix: \n\n{m}\n")
print(f"The total mean is: {mean}")

dim = m.shape
print(f"Number of rows: {dim[0]}")
print(f"Number of columns: {dim[1]}")

print("\n")

# mean for each row
# row format = a[i,:] where i is the row and the two points stands for 'everything in there'
for i in range(dim[0]):
    print(f"The mean of the row {i} is {m[i,:].mean()}")
    
print("\n")    

# mean for each column
# column format = a[:,i] where i is the column and the two points stands for 'everything in there'
for i in range(dim[1]):
    print(f"The mean of the column {i} is {m[:,i].mean()}")


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

# In[6]:


import numpy as np

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

outer_product = np.outer(u, v)
print(f"With the function outer in numpy: \n\n {outer_product} \n")

# create the space for the matrix
matr = np.array([[u[i] * v[j] for j in range(len(v))] for i in range(len(u))])

print(f"With a list comprehension: \n\n {matr} \n")

# using numpy broadcasting
matr = u[:, np.newaxis] * v

print(f"With NumPy broadcasting: \n\n {matr} \n")


# 3\. **Matrix masking**
# 
# Create a $10 \times 6$ matrix of float random numbers, distributed between 0 and 3 according to a flat distribution.
# 
# After creating the matrix, set all entries $< 0.3$ to zero using a mask.

# In[7]:


# seed for reproducibility
np.random.seed(2000)

matrix = np.random.uniform(0, 3, size=(10, 6))

mask = matrix < 0.3

# set entries < 0.3 to zero
matrix[mask] = 0

print(matrix)


# 4\. **Trigonometric functions**
# 
# Use `np.linspace` to create an array of 100 numbers between $0$ and $2\pi$ (inclusive).
# 
#   * Extract every 10th element using the slice notation
#   * Reverse the array using the slice notation
#   * Extract elements where the absolute difference between the `sin` and `cos` functions evaluated for that element is $< 0.1$
#   * **Optional**: make a plot showing the `sin` and `cos` functions and indicate graphically (with a line or a marker) where they are close

# In[8]:


import matplotlib.pyplot as plt

array = np.linspace(0, 2 * np.pi, 100)

# extract every 10th element using slice notation
every_10th = array[::10]

# reverse the array using slice notation
reversed_array = array[::-1]

# extract elements where |sin(x) - cos(x)| < 0.1
mask = np.abs(np.sin(array) - np.cos(array)) < 0.1
close_elements = array[mask]

# plot sin and cos functions
plt.plot(array, np.sin(array), label='sin(x)')
plt.plot(array, np.cos(array), label='cos(x)')

# mark points where |sin(x) - cos(x)| < 0.1
plt.scatter(close_elements, np.sin(close_elements), color='red', marker='o', label='Close points')

# Set labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.show()


# 5\. **Matrices**
# 
# Create a matrix that shows the $10 \times 10$ multiplication table.
# 
#  * Find the trace of the matrix
#  * Extract the anti-diagonal matrix (this should be ```array([10, 18, 24, 28, 30, 30, 28, 24, 18, 10])```)
#  * Extract the diagonal offset by 1 upwards (this should be ```array([ 2,  6, 12, 20, 30, 42, 56, 72, 90])```)

# In[9]:


multiplication_table = np.arange(1, 11) * np.arange(1, 11)[:, np.newaxis]

# find the trace of the matrix
trace = np.trace(multiplication_table)

# extract the anti-diagonal matrix
anti_diagonal = np.diag(np.fliplr(multiplication_table))

# extract the diagonal offset by 1 upwards
offset_diagonal = np.diag(multiplication_table, k=1)

# Print the results
print("Multiplication Table Matrix:")
print(multiplication_table)

print("\nTrace of the Matrix:", trace)

print("\nAnti-diagonal Matrix:")
print(anti_diagonal)

print("\nDiagonal Offset by 1 Upwards:")
print(offset_diagonal)


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

# In[11]:


cities = ['Chicago', 'Springfield', 'Saint-Louis', 'Tulsa', 'Oklahoma City', 'Amarillo', 'Santa Fe', 'Albuquerque', 'Flagstaff', 'Los Angeles']

# corresponding positions in miles
mile_positions = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])

# convert miles to kilometers (1 mile is approximately 1.60934 kilometers)
km_positions = mile_positions * 1.60934

# use broadcasting to create a 2D grid of distances
grid_distances = np.abs(np.subtract.outer(mile_positions, mile_positions))

# Convert the grid distances from miles to kilometers
grid_distances_km = grid_distances * 1.60934

print("\n2D Grid of Distances (Miles):")
print(grid_distances)

print("\n2D Grid of Distances (Kilometers):")
print(grid_distances_km)


# 7\. **Prime numbers sieve**
# 
# Compute the prime numbers in the 0-N (start with N=99) range with a sieve (mask).
# 
#   * Construct a shape (N,) boolean array, which is the mask
#   * Identify the multiples of each number starting from 2 and set accordingly the corresponding mask element
#   * Apply the mask to obtain an array of ordered prime numbers
#   * Check the performances (with `timeit`); how does it scale with N?
#   * Implement the optimization suggested in the [sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

# In[18]:


import timeit

def sieve_of_eratosthenes(N):
    # create a boolean mask of shape (N)
    is_prime = np.ones(N, dtype=bool)

    # set 0 and 1 to False, as they are not prime
    is_prime[:2] = False

    # identify multiples and set corresponding mask elements to False
    for i in range(2, int(np.sqrt(N)) + 1):
        if is_prime[i]:
            is_prime[i*i:N:i] = False

    # Return an array of ordered prime numbers
    primes = np.nonzero(is_prime)[0]
    return primes

# test 
N = 99
primes = sieve_of_eratosthenes(N)

# Print the prime numbers
print("Prime Numbers up to", N, ":", primes)

# Check performance with timeit
time_taken = timeit.timeit(lambda: sieve_of_eratosthenes(N), number=1000)
print(f"Time taken for N = {N}: {time_taken:.6f} seconds")
N = 1000
time_taken = timeit.timeit(lambda: sieve_of_eratosthenes(N), number=1000)
print(f"Time taken for N = {N}: {time_taken:.6f} seconds")
N = 1000000
time_taken = timeit.timeit(lambda: sieve_of_eratosthenes(N), number=1000)
print(f"Time taken for N = {N}: {time_taken:.6f} seconds")

def sieve_of_eratosthenes_optimized(N):
    # Create a boolean array of shape (N+1)
    is_prime = np.ones(N+1, dtype=bool)

    # Set 0 and 1 to False, as they are not prime
    is_prime[:2] = False

    # Start marking multiples from p^2
    for p in range(2, int(np.sqrt(N)) + 1):
        if is_prime[p]:
            is_prime[p*p:N+1:p] = False

    # Return an array of prime numbers
    primes = np.nonzero(is_prime)[0]
    return primes

# Test with N = 99
N = 99
primes = sieve_of_eratosthenes_optimized(N)

# Print the prime numbers
print("Prime Numbers up to", N, ":", primes)
time_taken = timeit.timeit(lambda: sieve_of_eratosthenes_optimized(N), number=1000)
print(f"Time taken for N = {N}: {time_taken:.6f} seconds")


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

# In[16]:


# seed for reproducibility
np.random.seed(2211)

# Number of walkers and steps
num_walkers = 1000
num_steps = 200

# Generate a 2D array of random steps (-1 or 1) for each walker
steps = np.random.choice([-1, 1], size=(num_walkers, num_steps))

# Calculate walking distances for each walker
distances = np.cumsum(steps, axis=1)

# Take the square of the distances
squared_distances = np.sqrt(distances**2)

# Compute the mean of squared distances at each step
mean_squared_distances = np.mean(squared_distances, axis=0)

# Optional: Plot the average distances as a function of time
plt.plot(mean_squared_distances)
plt.xlabel('Time Step')
plt.ylabel('Mean Squared Distance')
plt.title('Average Distance of Random Walkers')
plt.show()

