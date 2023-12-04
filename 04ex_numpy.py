#Ex1
import numpy as np

m = np.arange(12).reshape((3,4))
print (m)
print("Total mean:" , np.mean(m))
print("Mean for each row:" , np.mean(m, axis=1))
print("Mean for each column:" , np.mean(m, axis=0))
#---------------------------------------------------
#Ex2
import numpy as np

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
print("Using the function `outer` in numpy:",np.outer(u, v))
print("Using a list comprehension:",np.array([[ui * vj for vj in v] for ui in u]))
uT = u.reshape(-1, 1)
print("Using numpy broadcasting operations:", uT*v )
#---------------------------------------------------
#Ex3
import numpy as np
import numpy.random as npr

matrix = npr.uniform(0, 3, size=(10,6))
print("Original Matrix:")
print(matrix)
mask = matrix < 0.30
matrix[mask] = 0
print("Modified Matrix:")
print(matrix)

#---------------------------------------------------
#Ex4
import numpy as np
import matplotlib.pyplot as plt

alpha = np.linspace(0, 2*np.pi, 100)
slice = alpha[::10]
reversed_alpha = alpha[::-1]
mask = np.abs(np.sin(alpha) - np.cos(alpha)) < 0.1
modified_alpha = alpha[mask]

plt.plot(alpha, np.sin(alpha), label='sin (alpha)')
plt.plot(alpha, np.cos(alpha), label='cos (alpha)')

plt.scatter(modified_alpha, np.sin(modified_alpha), color='red', label='sin (alpha) ~ cos (alpha)')
plt.scatter(modified_alpha, np.cos(modified_alpha), color='blue', label='cos (alpha) ~ sin (alpha)')

plt.legend()
plt.title('sin & cos and sin (close to sin) & cos (close to sin)')
plt.xlabel('alpha')
plt.show()

#---------------------------------------------------
#Ex5

import numpy as np

multiplication_table = np.arange(1, 11) * np.arange(1, 11).reshape(-1, 1)
print("Multiplication Table:")
print(multiplication_table)

trace = np.trace(multiplication_table)
print("\nTrace of the Matrix:", trace)

anti_diagonal = np.flipud(multiplication_table)
print("\nAnti-diagonal Matrix:")
print(anti_diagonal)

diagonal_offset = np.diagonal(multiplication_table, offset=1)
print("\nDiagonal Offset by 1 Upwards:")
print(diagonal_offset)

#---------------------------------------------------
#Ex6

import numpy as np

positions = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])

distances_miles = np.abs(positions - positions[:, np.newaxis])
print("2D Grid of Distances (Miles):")
print(distances_miles)

distances_km = distances_miles * 1.60934
print("\n2D Grid of Distances (Km):")
print(distances_km)
#---------------------------------------------------
#Ex7

import numpy as np
import timeit

def sieve(N):
    is_prime = np.ones(N, dtype=bool)
    is_prime[0:2] = False

    for i in range(2, int(np.sqrt(N)) + 1):
        if is_prime[i]:
            is_prime[i*i:N:i] = False

    primes = np.nonzero(is_prime)[0]

    return primes

def sieve_eratosthenes(N):
    is_prime = np.ones(N, dtype=bool)
    is_prime[0:2] = False

    for i in range(2, int(np.sqrt(N)) + 1):
        if is_prime[i]:
            is_prime[i*i:N:i] = False

    primes = np.nonzero(is_prime)[0]

    return primes

N = 99
print('sieve',sieve(N))
time_basic = timeit.timeit(lambda: sieve(N), number=1000)
print(f"Sieve: {time_basic:.6f} seconds for N={N}")
print('Sieve of Eratosthenes', sieve_eratosthenes(N))
time_eratosthenes = timeit.timeit(lambda: sieve_eratosthenes(N), number=1000)
print(f"Sieve of Eratosthenes: {time_eratosthenes:.6f} seconds for N={N}")


#---------------------------------------------------
#Ex8

import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

walkers = 1000
steps = 200
random_steps = npr.choice([-1, 1], size=(walkers, steps))

distances = np.zeros((walkers, steps), dtype=int)
for i in range(steps):
    distances[:, i] = np.sum(random_steps[:, :i+1], axis=1)

distances_squared = distances**2
mean_squared_distances = np.mean(distances_squared, axis=0)

plt.plot(mean_squared_distances, label='Average Squared Distance')
plt.xlabel('Time Step')
plt.ylabel('Mean Squared Distance')
plt.legend()
plt.show()