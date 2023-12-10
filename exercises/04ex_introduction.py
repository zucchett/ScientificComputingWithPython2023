import numpy as np
import matplotlib.pyplot as plt
import timeit

# 1. REDUCTIONS
print('1. REDUCTIONS')
m = np.arange(12).reshape((3, 4))
total_mean = np.mean(m)
row_means = np.mean(m, axis=1)
column_means = np.mean(m, axis=0)

print("Total Mean:", total_mean)
print("Mean for each row:", row_means)
print("Mean for each column:", column_means)

# 2. OUTER PRODUCT
print('2. Outer product')

# Method 1: Using np.outer()
print('Method 1: Using np.outer()')

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
outer_product_np = np.outer(u, v)
print(outer_product_np)

# Method 2: Using a Nested For Loop or List Comprehension
print("Using nested for loop:")
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
outer_product_loop = np.array([[u_i * v_j for v_j in v] for u_i in u])
outer_product_list_comp = np.array([u_i * v for u_i in u])

print(outer_product_loop)
print("Using list comprehension:")
print(outer_product_list_comp)

# Method 3: Using Numpy Broadcasting
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
outer_product_broadcast = u[:, np.newaxis] * v

print("Using numpy broadcasting:")
print(outer_product_broadcast)

# 3. MATRIX MASKING
matrix = np.random.uniform(0, 3, size=(10, 6))
mask = matrix < 0.3
matrix[mask] = 0
print("Original Matrix:")
print(matrix)

# 4.TRIGONOMETRIC FUNCTIONS
arr = np.linspace(0, 2 * np.pi, 100)
every_10th_element = arr[::10]
reversed_arr = arr[::-1]
indices = np.where(np.abs(np.sin(arr) - np.cos(arr)) < 0.1)
selected_elements = arr[indices]
plt.plot(arr, np.sin(arr), label='sin(x)')
plt.plot(arr, np.cos(arr), label='cos(x)')

plt.scatter(selected_elements, np.sin(selected_elements), color='red', marker='o', label='Close Points')
plt.xlabel('x')
plt.ylabel('Function Value')
plt.legend()

# Show the plot
plt.show()

# Print the results
print("Every 10th element:", every_10th_element)
print("\nReversed array:", reversed_arr)
print("\nSelected elements with |sin(x) - cos(x)| < 0.1:", selected_elements)

# 5. MATRICES
multiplication_table = np.arange(1, 11) * np.arange(1, 11)[:, np.newaxis]
trace_value = np.trace(multiplication_table)
anti_diagonal = np.diag(np.flip(multiplication_table, axis=1))
diagonal_offset = np.diag(multiplication_table, k=1)

# Print the results
print("Multiplication Table Matrix:")
print(multiplication_table)
print("\nTrace of the Matrix:", trace_value)
print("\nAnti-diagonal Matrix:", anti_diagonal)
print("\nDiagonal Offset by 1 Upwards:", diagonal_offset)

# 6. BROADCASTING

cities = ["Chicago", "Springfield", "Saint-Louis", "Tulsa", "Oklahoma City", "Amarillo", "Santa Fe", "Albuquerque",
          "Flagstaff", "Los Angeles"]

positions_miles = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
distances_miles = np.abs(positions_miles - positions_miles[:, np.newaxis])
miles_to_km = 1.60934
distances_km = distances_miles * miles_to_km

print("Cities:", cities)
print("\nPositions in Miles:", positions_miles)
print("\nGrid of Distances (in Kilometers):")
print(distances_km)


# 7. Prime numbers sieve

def sieve_of_eratosthenes(N):
    is_prime = np.ones(N + 1, dtype=bool)
    is_prime[0:2] = False

    for i in range(2, int(np.sqrt(N)) + 1):
        if is_prime[i]:
            is_prime[i * i: N + 1: i] = False

    primes = np.nonzero(is_prime)[0]
    return primes

N = 99
primes = sieve_of_eratosthenes(N)
time_taken = timeit.timeit(lambda: sieve_of_eratosthenes(N), number=1000)

print(f"Prime numbers up to {N}:")
print(primes)
print("\nTime taken:", time_taken, "seconds")
N_values = [10 ** 3, 10 ** 4, 10 ** 5]

for N in N_values:
    time_taken = timeit.timeit(lambda: sieve_of_eratosthenes(N), number=10)
    print(f"\nTime taken for N={N}:", time_taken, "seconds")


# 8. Diffusion using random walk
walkers = 1000
steps = 200
random_walks = np.random.choice([-1, 1], size=(walkers, steps))
distances = np.cumsum(random_walks, axis=1)
distances_squared = distances ** 2
mean_distances_squared = np.mean(distances_squared, axis=0)
time_steps = np.arange(1, steps + 1)
plt.plot(time_steps, np.sqrt(mean_distances_squared), label='Average Distance')
plt.xlabel('Time Step')
plt.ylabel('Average Distance')
plt.legend()
plt.show()
