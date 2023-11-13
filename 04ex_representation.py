#---------------------------------------------------------------------------------------------------------------
# exercise4 part one.Reductions


import numpy as np # import naming convention

m = np.arange(12).reshape((3,4))
print("matrix is :\n" , m)

# Q1.find the total mean
tot_mean = np.mean(m)
print("\nTotal Mean is:", tot_mean)

# Q2.find the mean for each row and column
# Find and print the mean for each row in the matrix
row = np.mean(m, axis=1)
print("\nMean of Each Rows:", row)
# Print each row
print("\nEach Row:")
for row in m:
    print(row)

# Find and print the mean for each column in the matrix
column = np.mean(m, axis=0)
print("\nMean of Each Columns:", column)
# Print each column
print("\nEach Column:")
for j in range(len(m[0])):
    column = m[:, j]
    print(f"Column {j + 1}: {column}")

#---------------------------------------------------------------------------------------------------------------
# exercise4 part two.Outer product


import numpy as np

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

# Q1.Using outer function
print ("Using the outer function:\n", np.outer(u,v))

# Q2.Using a nested for loop
result = []
for i in u:
    row = []
    for j in v:
        row.append(i * j)
    result.append(row)
print ("\nOuter product using nested loop:\n", np.array(result) )

# Q3.Using numpy broadcasting operations
u_broadcasting = u.reshape(-1, 1)
outer_product_broadcasting = u_broadcasting * v
print("\nOuter product using broadcasting:\n", outer_product_broadcasting)

#---------------------------------------------------------------------------------------------------------------
# exercise 4 part three. Matrix masking


import numpy as np

# Create a 10*6 matrix of random numbers between 0 and 3
matrix_size = (10, 6)
lower_case = 0
upper_case = 3

# Create a random matrix name m using a uniform distribution
m = np.random.uniform(lower_case, upper_case, size=matrix_size)

# Set all elements in the matrix m that are less than 0.3 to zero.m[mask] = 0
m[m<0.3]=0

# Display the matrix
print("Random Matrix with Entries < 0.3 Set to Zero:\n", m)

#---------------------------------------------------------------------------------------------------------------
# exercise 4 part four. Trigonometric functions


import numpy as np

# Create an array of 100 numbers
start = 0
stop = 2 * np.pi
num_points = 100  # number of points we want in our array
angles = np.linspace(start, stop, num_points)

# ract every 10th element from the array
alternative = []
for i in range(0, len(angles), 10):
    alternative.append(angles[i])

# Q1.Convert the result back to a NumPy array
convert = np.array(alternative)
print("Every 10th element:\n", convert)

# Q2. Reverse the array using a loop
reversed_angles = []
for j in range(len(angles) - 1, -1, -1):
    reversed_angles.append(angles[j])
print("\nReversed array:\n", reversed_angles)


# Q3.Extract elements where the absolute difference between sin and cos is < 0.1
sin_values = np.sin(angles) # sin value for each angle
cos_values = np.cos(angles) # cos value for each angle

abs_difference = np.abs(sin_values - cos_values) # Calculate the difference between sin and cos
close_points = angles[abs_difference < 0.1] # Select elements where the difference is less than 0.1
print("\nClose points between sin and cos:\n", close_points)

#---------------------------------------------------------------------------------------------------------------
# exercise 4 part five.Matrices


import numpy as np

# Create an empty list to store the rows
table_list = []

# Use nested loops to fill the list.
for i in range(10):
    row = []
    for j in range(10):
        row.append((i + 1) * (j + 1))
    table_list.append(row)

# Convert the list to a NumPy array
multiplication_table = np.array(table_list, dtype=int)

# Display the multiplication table matrix
print("\nMultiplication Table Matrix:")
print(multiplication_table)

# Fill in the matrix with multiplication table values
for i in range(1, 11):
    for j in range(1, 11):
        multiplication_table[i-1, j-1] = i * j

# Display the multiplication table matrix
print("\n\nMultiplication Table Matrix:", multiplication_table)

# Q1.Find the trace of the matrix
trace_value = np.trace(multiplication_table)
print("\n\nTrace of the Matrix:", trace_value)

# Q2.Extract the anti-diagonal matrix
anti_diagonal = np.flipud(multiplication_table)
print("\n\nAnti-Diagonal Matrix:", anti_diagonal)

# Q3.Extract the diagonal offset by 1 upwards
diagonal_offset = np.diagonal(multiplication_table, offset=1)
print("\n\nDiagonal Offset by 1 Upwards:" , diagonal_offset)

#---------------------------------------------------------------------------------------------------------------
#exercise4 part six.Broadcasting


import numpy as np

# Cities along Route 66
cities = ["Chicago", "Springfield", "Saint-Louis", "Tulsa", "Oklahoma City", "Amarillo", "Santa Fe", "Albuquerque", "Flagstaff", "Los Angeles"]

# Corresponding positions in miles
position_miles = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])

# Q1. Build a 2D grid of distances among each city along Route 66
num_cities = len(cities)
distances_alternative = np.zeros((num_cities, num_cities))  # creating arrays of zeros

for i in range(num_cities):
    for j in range(num_cities):
        distances_alternative[i, j] = position_miles[j] - position_miles[i]

# Take the absolute values of the differences
distances_alternative = np.abs(distances_alternative)

# Display the 2D grid of distances in miles
print("2D Grid of Distances (in miles):")
print(distances_alternative)

# Q2. Convert the distances to km
convert_factor = 1.60934

# Convert distances from miles to kilometers
position_km = position_miles * convert_factor

# Create an empty 2D array for distances in kilometers
distances_km = np.zeros((len(position_km), len(position_km)))

# Calculate the absolute differences between each pair of distances and fill the 2D array
for i in range(len(position_km)):
    for j in range(len(position_km)):
        distances_km[i, j] = np.abs(position_km[j] - position_km[i])

# Display the 2D grid of distances in kilometers
print("\n2D Grid of Distances (in kilometers):", distances_km)

#---------------------------------------------------------------------------------------------------------------
# exercise4 part seven.Prime numbers sieve


import numpy as np
import timeit

# Q1. Construct a shape (N,) boolean array
def  prime_numbers_sieve(n):
    is_prime = [True] * (n + 1)     # Creating a list to keep numbers

    is_prime[0] = is_prime[1] = False

# Q2.Identify the multiples of each number
    for i in range(2, int(np.sqrt(n)) + 1):      # find prime numbers with sieve algorythm
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    # Create an empty list to store prime numbers
    primes = []

# Q3.Apply the mask to obtain an array
    # Add prime numbers to the list
    for i in range(n + 1):
        if is_prime[i]:
            primes.append(i)

    # Convert the list to a NumPy array
    primes = np.array(primes)
    return primes

# Set the range upper limit (N)
N = 99

# Use the sieve to find prime numbers
primes =  prime_numbers_sieve(N)

# Display the prime numbers
print("Prime Numbers up to", N, ":", primes)

# Q4.Check the performances (with timeit)
# Check the performance using timeit
lambda_function = lambda: prime_numbers_sieve(N)
time_taken = timeit.timeit(lambda_function, number=10000) # Measure the time taken using timeit with 10000 iterations
print("Time taken for N =", N, ":", time_taken, "seconds")

#---------------------------------------------------------------------------------------------------------------
# exercise 4 part eight.Diffusion using random walk


import numpy as np
from numpy.random import randint

# Q1. Set the number of walkers and steps
walkers = 1000
steps = 200

# Q2. Create a 2D array for random walk steps
random_steps = randint(low=-1, high=2, size=(walkers, steps))

# Q3. Calculate walking distances for each walker
distances = []      # set a list to store

for current_step in range(1, steps + 1):
    # indexing for rows and columns
    rows = np.arange(walkers)
    columns = np.arange(current_step)

    # Create an empty list to store rows with selected columns
    selected_rows = []

    # Loop through each row in random_steps
    for row in random_steps:
        # Select the desired columns for the current row
        selected_row = row[columns]

        # Append the selected row to the list
        selected_rows.append(selected_row)

    # Convert the list of rows into a NumPy array
    selected_steps = np.array(selected_rows)

    # Sum the steps for each walker
    total_distance = np.sum(selected_steps, axis=1)

    # Store the total distance for each walker at the current step
    distances.append(total_distance)

# Q4.Convert the list of distances into a NumPy array
distances = np.array(distances).T

# Calculate the squared distances
squared_distances = pow(distances, 2)

# Q5.Calculate the average squared distance at each time step
mean_distances = np.mean(squared_distances, axis=0)

# Print the results
print("Average squared distance at each time step:")
print(mean_distances)

#---------------------------------------------------------------------------------------------------------------
