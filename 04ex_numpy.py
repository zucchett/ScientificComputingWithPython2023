##exe4
#q1
import numpy as np
m = np.arange(12).reshape((3,4))
print(m)

total_mean =np.mean(m)

rows_mean=np.mean(m, axis=1)
cols_mean=np.mean(m, axis=0)


print(f'The total mean is :  {total_mean}')
print(f'The rows mean is :  {rows_mean}')
print(f'The column mean is :  {cols_mean}')

#q2
import numpy as np
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

outer_=np.outer(u,v)

print(outer_)

#using list comprehension
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
outer=[[i*j for j in v] for i in u]

print (outer)

##broadcasting
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
import numpy as np
outer__=u*v
print(outer__)

#q3
import numpy as np
# initializing 10x6 matrix of random numbers between 0 and 3
mat = np.random.uniform(low=0.0, high=3.0, size=(10, 6))
# Create a mask for values less than 0.3
mask = mat < 0.3
# Apply the mask to set values less than 0.3 to zero
mat[mask] = 0
print(mat)

###q4

import numpy as np
arr = np.linspace(0, 2 * np.pi, 100)
Tenth = arr[::10]
reversed_arr = arr[::-1]
sin_values = np.sin(arr)
cos_values = np.cos(arr)
# Extract elements where the absolute difference between sin and cos is < 0.1
close_values_indices = np.where(np.abs(sin_values - cos_values) < 0.1)
close_values = arr[close_values_indices]

print(sin_values)


#q5
import numpy as np

# Create 10x10 multiplication table
matrix = np.arange(1, 11)[:, None] * np.arange(1, 11)
# Find the trace of the matrix
tr = np.trace(matrix)
#Anti-diagonal matrix
anti_diagonal = np.diagonal(np.flip(matrix, axis=1))
#Diagonal offset by 1 upwards
offset_diagonal = np.diagonal(matrix, offset=1)
print("Matrix:")
print(matrix)
print("\nTrace of the matrix:", tr)
print("\nAnti-diagonal matrix:", anti_diagonal)
print("\nDiagonal offset by 1 upwards:", offset_diagonal)

#q6
import numpy as np
# Positions of cities along Route 66 in miles
location_miles = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
# Calculate the differences to get the distances between cities
distances_miles = np.abs(location_miles[:, np.newaxis] - location_miles)
# 1 mile = 1.60934 kilometers
conversion_factor = 1.60934  
# Convert distances from miles to kilometers using broadcasting
distances_km = distances_miles * conversion_factor

# Display the 2D grid of distances in kilometers
print("2D grid of distances in kilometers:")
print(distances_km)

##q7
import numpy as np
import timeit

def sieve_of_eratosthenes_basic(N):
    # Create a boolean mask of shape (N,)
    mask = np.ones(N, dtype=bool)
    mask[:2] = False

    for i in range(2, int(np.sqrt(N)) + 1):
        if mask[i]:
            mask[i * i:N:i] = False  

    # Generate array of ordered prime numbers
    primes = np.nonzero(mask)[0]
    return primes

# Define N value
N = 100000

# Measure the time taken to compute primes using the basic sieve
time_basic = timeit.timeit(lambda: sieve_of_eratosthenes_basic(N), number=1)

print(f"Prime numbers using basic sieve for N = {N}:")
print(sieve_of_eratosthenes_basic(N))
print(f"\nTime taken for basic sieve with N = {N}: {time_basic} seconds")


##for large value of N the perfomance degrades 
#q8
import numpy as np
import matplotlib.pyplot as plt
# Number of walkers and steps
walkers = 1000
steps = 200
# Generate a 2D array representing the random walk for each walker
random_walks = np.random.choice([-1, 1], size=(walkers, steps))
# Calculate the walking distances for each walker
distances = np.cumsum(random_walks, axis=1)
squared_distances = distances ** 2
# Compute the mean of squared distances at each step
mean_distances = np.mean(squared_distances, axis=0)
# Calculating the square root of mean squared distances to get the typical distance
typical_distances = np.sqrt(mean_distances)
