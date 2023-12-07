################################ 04_Numpy ###################################################
print("****************Reductions******************")
import numpy as np
m = np.arange(12).reshape((3,4))
print(m)
print("1-find the total mean of matrix m:")
sum=0
for i in range(3):
    for j in range (4):
        sum+=m[i,j]
print("The total mean of m is = ",sum/12)

print("2-find the mean for each row and column:")
row_means = np.mean(m, axis=1) # this instruction returns a list of float values each one of them is the mean of the corresponding row
print("Mean for each row:", row_means)
column_means = np.mean(m, axis=0) # this instruction returns a list of float values each one of them is the mean of the corresponding column
print("Mean for each column:", column_means)

print("****************Outer product******************")
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
print("1-using numpy:")
outer_uv = np.outer(u, v)
print("Outer product using np.outer:", outer_uv)
print("2-using a nested for loop or list comprehension:")
outer_with_list_comprehension = np.array([i * v for i in u])
print("Outer product using list comprehension:", outer_with_list_comprehension)
print("3-using NumPy Broadcasting Operations:")
outer_broad = u[:, np.newaxis] * v
print("Outer product using NumPy broadcasting:", outer_broad)

print("****************Matrix masking******************")
mat = np.random.uniform(0, 3, size=(10, 6)) # I used the np.random.uniform function for random float values between 0 and 3
print("Matrix = ",mat)
mask = mat < 0.3 # here I created a boolean variable mask for values that are <0.3
mat[mask]=0 # in this instruction I set all values that are less than 0.3 to 0.
print("new mat = ", mat)

print("****************Trigonometric functions******************")
liste = np.linspace(0, 2*np.pi, 100)
print("liste = ", liste)
tenth_element_liste = liste[::10]
print("10th element extraction = ", tenth_element_liste)
reversed_liste= liste[::-1]
print("reversed list", reversed_liste)
mask_4 = np.abs(np.sin(liste) - np.cos(liste)) < 0.1
new_liste = liste[mask_4]
print("new list = ", new_liste)
# Plot the sin and cos functions
import matplotlib.pyplot as plt
plt.plot(liste, np.sin(liste), label='sin(x)')
plt.plot(liste, np.cos(liste), label='cos(x)')
# Mark the points where sin and cos are close
# sins = np.sin(liste)
# plt.scatter(new_liste,sins[mask], color='red', label='Close Points')

print("****************Matrices******************")
vector = np.arange(1, 11)
# Creating a 10x10 multiplication table
multiplication_table = np.outer(vector, vector)
print("multiplication_table=",multiplication_table)
diagonal = multiplication_table[np.arange(10), np.arange(9, -1, -1)]
print("Diagonal=", diagonal)
offset = multiplication_table[np.arange(9), np.arange(1, 10)]
print("Offset = ", offset)

print("****************Broadcasting******************")

miles_l = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
miles_distance = np.abs(miles_l - miles_l[:, np.newaxis])
miles_to_km = 1.60934 # Defining the conversion factor from miles to kilometers
distances_km = miles_distance * miles_to_km
print("Distances in kilometre = ",distances_km)

print("****************Prime numbers sieve******************")
import timeit
N=99
is_prime = np.ones(N, dtype=bool)
is_prime[0:2] = False  # 0 and 1 are not prime

for i in range(2, int(np.sqrt(N)) + 1):
    if is_prime[i]:
        is_prime[i*i:N:i] = False
print(np.nonzero(is_prime)[0])
# Measure the time taken by the sieve_of_eratosthenes function
time_taken = timeit.timeit(lambda: np.nonzero(is_prime)[0], number=1000)
print("Prime numbers up to", N, ":", np.nonzero(is_prime)[0])
print("Time taken for 1000 iterations:", time_taken, "seconds.")

print("****************Diffusion using random walk******************")

num_walkers = 1000
num_steps = 200
# Generate a 2D array of random steps (-1 or 1)
random_steps = np.random.choice([-1, 1], size=(num_walkers, num_steps))
distances = np.cumsum(random_steps, axis=1) # Calculating the walking distances for each walker
squared_distances = distances**2
mean_squared_distances = np.mean(squared_distances, axis=0)
print("The mean squared distances at each step:", mean_squared_distances)
