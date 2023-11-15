import numpy as np
import matplotlib.pyplot as plt
import timeit

###################1. Reductions####################
print("###################START 1. Reductions###################")

m = np.arange(12).reshape((3,4))
print(m)
print("Total Mean:", m.mean())
print("Row Means:", m.mean(axis=1))
print("Col Means:", m.mean(axis=0))

###################2. Outer product####################
print("###################START 2. Outer product###################")

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

outer_product = np.outer(u, v)
print("Outer product 1:\n",outer_product)

outer_product_2 = np.empty((len(u), len(v)))

for i in range(len(u)):
    for j in range(len(v)):
        outer_product_2[i, j] = u[i] * v[j]

print("Outer product 2:\n", outer_product_2)

u_column = u[:, np.newaxis]  
v_row = v[np.newaxis, :]    
outer_product_3 = u_column * v_row

print("Outer product 3:\n",outer_product_3)

###################3. Matrix masking####################
print("###################START 3. Matrix masking###################")

matrix = np.random.uniform(0, 3, size=(10, 6))
mask = (matrix < 0.3)
matrix[mask] = 0
print("Original matrix:\n", matrix)

###################4. Trigonometric functions####################
print("###################START 4. Trigonometric functions###################")

arr = np.linspace(0, np.pi, 100)

every_10th_element = arr[::10]
reversed_arr = arr[::-1]

sin_values = np.sin(arr)
cos_values = np.cos(arr)

close_elements = arr[np.abs(sin_values - cos_values) < 0.1]

plt.figure(figsize=(10, 4))
plt.plot(arr, sin_values, label='sin(x)')
plt.plot(arr, cos_values, label='cos(x)')
plt.scatter(close_elements, np.sin(close_elements), c='red', marker='o', label='Close Points')
plt.xlabel('x')
plt.ylabel('sin(x) and cos(x)')
plt.legend()
plt.grid(True)
plt.show()

print("Every 10th element:", every_10th_element)
print("Reversed array:", reversed_arr)
print("Close elements:", close_elements)

###################5. Matrices####################
print("###################START 5. Matrices###################")

table = np.arange(1, 11)[:, np.newaxis] * np.arange(1, 11)
trace = np.trace(table)
anti_diagonal = np.diagonal(np.flip(table, axis=0))
offset_diagonal = np.diagonal(table, offset=1)

print("Multiplication Table Matrix:")
print(table)
print("Trace of the Matrix:", trace)
print("Anti-Diagonal Matrix:", anti_diagonal)
print("Diagonal Offset by 1 Upwards:", offset_diagonal)

###################6. Broadcasting####################
print("###################START 6. Broadcasting###################")

cities = ["Chicago", "Springfield", "Saint-Louis", "Tulsa", "Oklahoma City", "Amarillo", "Santa Fe", "Albuquerque", "Flagstaff", "Los Angeles"]
mile_positions = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
distances = np.abs(mile_positions[:, np.newaxis] - mile_positions)
km_distances = distances * 1.60934

for i in range(len(cities)):
    for j in range(len(cities)):
        print(f"Distance from "+cities[i]+" to "+cities[j]+": "+str(km_distances[i, j])+" km")

###################7. Prime numbers sieve####################
print("###################START 7. Prime numbers sieve###################")

def find_prime(N):
    is_prime = np.ones(N+1, dtype=bool)
    is_prime[0:2] = False
    
    for p in range(2, int(N**0.5) + 1):
        if is_prime[p]:
            is_prime[p*p::p] = False

    primes = np.nonzero(is_prime)[0]
    return primes

N = 99

time_taken = timeit.timeit(lambda: find_prime(N), number=1)
print(find_prime(N))
print("Time taken:",time_taken,"seconds")

###################8. Diffusion using random walk####################
print("###################START 8. Diffusion using random walk###################")

walkers = 1000
steps = 200

random_jumps = np.random.choice([-1, 1], size=(walkers, steps))
distances = np.cumsum(random_jumps, axis=1)
squared_distances = distances ** 2
mean_squared_distances = np.mean(squared_distances, axis=0)
rms_distances = np.sqrt(mean_squared_distances)

plt.figure(figsize=(10, 6))
plt.plot(range(1, steps + 1), rms_distances)
plt.xlabel("Time Steps")
plt.ylabel("Root Mean Square Distance")
plt.grid(True)
plt.show()

print("Mean squared distances at each step:")
print(mean_squared_distances)
