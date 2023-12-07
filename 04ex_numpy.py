#### Q1

import numpy as np
m = np.arange(12).reshape((3,4))
print(m)
total_mean = np.mean(m)
row_means = np.mean(m, axis=1)
column_means = np.mean(m, axis=0)
print("Total Mean:", total_mean)
print("Mean for Each Row:", row_means)
print("Mean for Each Column:", column_means)


##### Q2

import numpy as np
u = np.array([1, 3, 5, 7])  # 1*4
v = np.array([2, 4, 6, 8])  # 1*4
print(u);print(v)
# Using the outer function
outer_product_np = np.outer(u, v)
print("Outer Product using np.outer:")
print(outer_product_np)  # 4*4
# Using a nested for loop
outer_product_loop = np.array([[u_i * v_j for v_j in v] for u_i in u])
# Alternatively, using list comprehension
# outer_product_list_comprehension = np.array([u_i * v for u_i in u])
print("Outer Product using nested for loop:")
print(outer_product_loop)
# Using NumPy broadcasting
outer_product_broadcasting = u[:, np.newaxis] * v
print("Outer Product using broadcasting:")
print(outer_product_broadcasting)


#### Q3

import numpy as np
# Create a 10x6 matrix of float random numbers between 0 and 3
random_matrix = np.random.uniform(0, 3, size=(10, 6))
print("Original Matrix:")
print(random_matrix)
# Create a mask for entries < 0.3
mask = random_matrix < 0.3
# Set entries < 0.3 to zero
random_matrix[mask] = 0
print("After masking")
print(random_matrix)


#### Q4

import numpy as np
import matplotlib.pyplot as plt
# Create an array of 100 numbers between 0 and 2pi
theta = np.linspace(0, 2 * np.pi, 100)
# Extract every 10th element using slice notation
every_10th_element = theta[::10]
# Reverse the array using slice notation
reversed_array = theta[::-1]
# Extract elements where the absolute difference between sin and cos functions is < 0.1
close_elements = theta[np.abs(np.sin(theta) - np.cos(theta)) < 0.1]
plt.plot(theta, np.sin(theta), label='sin(theta)')
plt.plot(theta, np.cos(theta), label='cos(theta)')
# Mark points where sin and cos are close
plt.scatter(close_elements, np.sin(close_elements), color='red', label='Close Points')
plt.xlabel('Theta');plt.ylabel('Function Value');plt.legend();plt.show()



#### Q5

import numpy as np
# Create a 10x10 multiplication table matrix
#multiplication_table = np.arange(1, 11) * np.arange(1, 11)[:, np.newaxis]
m1 = np.arange(1, 11)  # 1*10
m2 = np.arange(1, 11)[:, np.newaxis]  # 10*1
multiplication_table = np.outer(m2,m1)
# Find the trace of the matrix
trace_value = np.trace(multiplication_table)  # sum of elements on the main diagonal of multiplication table
# Extract the anti-diagonal matrix
anti_diagonal = np.diag(np.flipud(multiplication_table))  # diag köşegen bulur, flipud satır bazından tersine çevirir yani en üstteki en altta gelir
# Extract the diagonal offset by 1 upwards
diagonal_offset = np.diag(multiplication_table, k=1)  #1=1  2=2,2   3=3,4,3   4=4,6,6,4  5=5,8,9,8,5
print("Multiplication Table Matrix:")
print(multiplication_table)
print("\nTrace of the Matrix:", trace_value)
print("\nAnti-diagonal Matrix:")
print(anti_diagonal)
print("\nDiagonal Offset by 1 Upwards:")
print(diagonal_offset)



#### Q6

import numpy as np
# Define the cities and corresponding positions in miles
cities = ['Chicago', 'Springfield', 'Saint-Louis', 'Tulsa', 'Oklahoma City', 'Amarillo', 'Santa Fe', 'Albuquerque', 'Flagstaff', 'Los Angeles']
mile_positions = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
# Build a 2D grid of distances among each city along Route 66 using broadcasting
distance_grid_miles = np.abs(mile_positions - mile_positions[:, np.newaxis])
# Convert the distances to kilometers (1 mile = 1.60934 km)
distance_grid_km = distance_grid_miles * 1.60934
print("\nCities along Route 66:")
print(cities)
print("\n2D Grid of Distances among Cities (in miles):")
print(distance_grid_miles)
print("\n2D Grid of Distances among Cities (in kilometers):")
print(distance_grid_km)



#### Q7

import numpy as np
import timeit
def sieve_of_eratosthenes(N):
    # Create a boolean mask array
    is_prime = np.ones(N+1, dtype=bool)
    is_prime[0:2] = False 
    for num in range(2, int(np.sqrt(N))+1):
        if is_prime[num]:
            # Mark multiples of num as non-prime
            is_prime[num*num:N+1:num] = False
    # Extract prime numbers from the mask
    primes = np.nonzero(is_prime)[0]
    return primes
def main():
    N = 99
    time_taken = timeit.timeit(lambda: sieve_of_eratosthenes(N), number=1)
    print(f"Prime numbers up to {N}: {sieve_of_eratosthenes(N)}")
    print(f"Time taken: {time_taken:.6f} seconds")
main()



#### Q8

import numpy as np
import matplotlib.pyplot as plt
def simulate_random_walk(walkers, steps):
    # Create a 2D array of random steps (-1 or 1)
    random_steps = np.random.randint(low=-1, high=2, size=(walkers, steps))  # If we use randint, it will get the values -1,0,1. 
    #random_steps = np.random.choice([-1, 1], size=(walkers, steps))  # If we use choice, it will get the values -1,1.
    # Calculate walking distances for each walker
    distances = np.cumsum(random_steps, axis=1)  
    # Take the square of the distances
    squared_distances = distances**2
    # Compute the mean of the squared distances at each step
    mean_squared_distances = np.mean(squared_distances, axis=0)
    return mean_squared_distances
def main():
    walkers = 1000
    steps = 200   
    # Simulate random walk and compute mean squared distances
    mean_squared_distances = simulate_random_walk(walkers, steps)
    # Plot the average distances as a function of time
    plt.plot(np.sqrt(mean_squared_distances), label='Average Distance')
    plt.xlabel('Time Step');plt.ylabel('Average Distance (sqrt(Distance^2))')
    plt.title('Random Walk Simulation');plt.legend();plt.show()
if __name__ == "__main__":
    main()

