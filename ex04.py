# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
## Exercise 1
import numpy as np

m = np.arange(12).reshape((3,4))

# Finding the total mean
total_mean = np.mean(m)
print("The total mean is:", total_mean)

# Finding the mean for each row and column
row_means = np.mean(m, axis=1)
print("The mean for each row is:", row_means)

column_means = np.mean(m, axis=0)
print("The mean for each column is:", column_means)


## Exercise 2
import numpy as np

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

# Using the function outer in numpy
outer_product1 = np.outer(u, v)
print("The outer product using np.outer is:\n", outer_product1)

# Using a nested for loop or a list comprehension
outer_product2 = np.array([u[i] * v[j] for i in range(len(u)) for j in range(len(v))]).reshape(len(u), len(v))
print("The outer product using a nested for loop or list comprehension is:\n", outer_product2)

# Using numpy broadcasting operations
outer_product3 = u[:, np.newaxis] * v
print("The outer product using numpy broadcasting is:\n", outer_product3)


## Exercise 3
import numpy as np

# Creating a 10x6 matrix of float random numbers between 0 and 3
matrix = np.random.uniform(low=0, high=3, size=(10, 6))
print("Here's your matrix of float random numbers:\n", matrix)

# Creating a mask to identify entries less than 0.3
mask = matrix < 0.3

# Setting all entries less than 0.3 to zero using the mask
matrix[mask] = 0

print("After applying the mask, the matrix becomes:\n", matrix)


## Exercise 4
import numpy as np

# Creating an array of 100 numbers between 0 and 2pi (inclusive)
arr = np.linspace(0, 2*np.pi, 100)
print("Here's your array of numbers:\n", arr)

# Extracting every 10th element using slice notation
extracted1 = arr[::10]
print("Here are every 10th elements:\n", extracted1)

# Reversing the array using slice notation
reversed_arr = arr[::-1]
print("Here's the array in reverse order:\n", reversed_arr)

# Extracting elements where the absolute difference between sin and cos is < 0.1
selected_elements = arr[np.abs(np.sin(arr) - np.cos(arr)) < 0.1]
print("Here are the elements where |sin(x) - cos(x)| < 0.1:\n", selected_elements)


## Exercise 5
import numpy as np 

# Creating the 10x10 multiplication table matrix 
matrix = np.arange(1, 11) * np.arange(1, 11)[:, np.newaxis] 

# Printing the matrix 
print(matrix) 

# Finding the trace of the matrix 
trace = np.trace(matrix)
print("The trace of the matrix is:", trace) 

# Extracting the anti-diagonal matrix
anti_diagonal = np.diagonal(np.fliplr(matrix))
print("The anti-diagonal matrix is:", anti_diagonal)


## Exercise 6
import numpy as np

distances_miles = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])

grid_distances = np.abs(distances_miles - distances_miles[:, np.newaxis])
grid_distances_km = np.rint(grid_distances * 1.60934)

print("The grid distances matrix is:\n", grid_distances)
print("The grid distances matrix in km is:\n", grid_distances_km)


## Exercise 7
import numpy as np
import timeit

# Function to compute prime numbers using the sieve of Eratosthenes
def sieve_of_eratosthenes(N):
    mask = np.ones(N, dtype=bool)  # Construct a boolean array of shape (N,)
    mask[:2] = False  # Set the first two elements as False since they are not prime

    for num in range(2, int(np.sqrt(N)) + 1):  # Iterate from 2 to the square root of N
        if mask[num]:  # If the current number is prime
            mask[num**2::num] = False  # Set the multiples of the current number as False

    primes = np.nonzero(mask)[0]  # Apply the mask to obtain an array of ordered prime numbers
    return primes

N = 99
time_taken = timeit.timeit(lambda: sieve_of_eratosthenes(N), number=1000)  # Measure the time taken for N=99
print(f"Time taken for N={N}: {time_taken} seconds")
# Time taken for N=99: 0.006287600001087412 seconds
# Time taken for N=999: 0.013110419000440743 seconds
# Time taken for N=9999: 0.053076579000844504 seconds

## Exercise 8
import numpy as np

# Define the number of walkers and steps
walkers = 1000
steps = 200

# Create a 2D array of size walkers x steps with values -1 or 1
random_walks = np.random.randint(low=-1, high=2, size=(walkers, steps))

# Calculate the walking distances for each walker
distances = np.sum(random_walks, axis=1)

# Square the distances using element-wise multiplication
squared_distances = distances**2

# Compute the mean of the squared distances at each step
mean_squared_distances = np.mean(squared_distances, axis=0)
