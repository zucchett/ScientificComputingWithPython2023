#1
import numpy as np
import timeit
import matplotlib.pyplot as plt

m = np.arange(12).reshape((3,4))
mat_mean = m.mean()
mat_mean_rows = m.mean(1)
mat_mean_columns = m.mean(0)

print("#1")
print(f"Total mean is: {mat_mean}")
print(f"Mean is rows are: {mat_mean_rows}")
print(f"Mean is columns are: {mat_mean_columns}")

#2
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

print("\n#2")
print(f"Using outer method:\n {np.outer(u, v)}\n")

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

outer_product_loop = np.array([[i * j for j in v] for i in u])
print(f"Using for loops:\n{outer_product_loop}\n")

outer_product_broadcasting = u[:, np.newaxis] * v
print(f"Using for broadcasting:\n{outer_product_broadcasting}")

#3
print("\n#3")
matrix = np.random.uniform(0.0, 3.0, size=(10, 6))
print("Before Masking:\n", matrix)
mask = (matrix < 0.3)
matrix[mask] = 0
print("\nAfter masking:\n", matrix)

#4
print("\n#4")
a = np.linspace(0, 2*np.pi, 100, endpoint=True)
print(f"Matrix: {a}")
print(f"\nAll tenth elements:\n {a[9::10,]}")
print(f"\nReversed: \n{a[::-1,]}") 

mask = (np.abs(np.sin(a)-np.cos(a)) < 0.1)
close_elements = a[mask]
print(f"\nFiltered:\n {close_elements}")
print()

y_sin = np.sin(a)
y_cos = np.cos(a)

plt.plot(a,y_sin,label='sin')
plt.plot(a,y_cos,label='cos')

plt.scatter(close_elements, np.cos(close_elements), color='red', marker='o', label='Close points')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

#5
print("\n#5")
a = np.linspace(1, 10, num=10)
b = np.linspace(1, 10, num=10)

c = np.array([[i*j for j in b] for i in a])
print(f"10x10 Multiplication Table: \n{c}")

#finding the trace of the matrix
indices = np.arange(0, 10)
trace = sum([c[(i, i)] for i in indices])
print(f"\nTrace: {trace}")

#Extracting the anti-diagonal of the matrix
anti_diagonal = np.array([c[i, -1-i] for i in indices])
print(f"Anti diagonal: {anti_diagonal}")

#Extracting diagonal offset by 1 upwards
diagonal_offset = np.array([c[i, i+1] for i in indices if i != 9])
print(f"Diagonal offset by 1 upwards: {diagonal_offset}\n")

#6
print("\n#6")
positions = np.array((0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448), dtype=int)
distances = np.array([[np.abs(i-j) for j in positions] for i in positions])
print(f"Distances: \n{distances}\n")
print(f"Distances in km: \n{distances * 1.6}")

#7
def generate_primes(N):
    nums = np.arange(0, N+1)
    mask = np.zeros(N+1, dtype=bool)

    multiples = [[i for i in nums[2:] if n%i ==0] for n in nums[2:]]

    for index, array in enumerate(multiples):
        if len(array) == 1:
            mask[2:][index] = 1

    primes = nums[mask]
    return primes

print("\n#7")
print(f"Regular Algorithm (Primes for N = 99): \n{generate_primes(99)}")
Ns = [2, 5, 10, 50, 99, 120]
for N in Ns:
    execution_time = timeit.timeit(lambda: generate_primes(N), number=10000)
    print(f"Execution time for N={N}: {execution_time:.6f} seconds")

#For small values of N, thus, (2, 5, 10), the execution time is relatively low, indicating that the algorithm runs quickly for smaller ranges.
#But as N grows to 50, 99, 120 the execution time increases significantly making the time complexity linear. 
#Therefore this algorithm does not scale well with increasing values of N.

def sieve_of_eratosthenes(n):
    is_prime = np.ones(n+1)
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i**2, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]

n = 99
primes_up_to_n = sieve_of_eratosthenes(n)
print("Sieve of eratosthenes Algorithm")
print(f"Prime numbers up to {n}: {primes_up_to_n}")

#8
print("\n#8")
random_steps = np.random.randint(low=0, high=2, size=(1000, 200)) * 2 - 1

distances = np.cumsum(random_steps, axis=1)

squared_distances = distances**2
mean_squared_distances = np.mean(squared_distances, axis=0)

plt.plot(mean_squared_distances, label='Average Distance')
plt.xlabel('Time Step')
plt.ylabel('Average Distance Squared')
plt.legend()
plt.show()

