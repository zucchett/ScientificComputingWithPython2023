#SOLUTION NUMBER 1
"""
1.Reductions
Find the total mean, and the mean for each row and column of the following matrix:
m = np.arange(12).reshape((3,4))
"""

import numpy as np

m = np.arange(12).reshape((3, 4))
print("matrics:""\n", m)
print()

print("The Total mean for the above matrics is:", np.mean(m))

row=np.mean(m, axis=1)
print("The mean for each row of the above matrics is:",row,)

column=np.mean(m, axis=0)
print("The mean for each column of the above matrics is:",column

//////////////////////////////////////////END OF SOLUTION 1/////

#SOLUTION NUMBER 2

"""
2. **Outer product**

Find the outer product of the following vectors:

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
```

Use different methods to do this:

   1. Using the function `outer` in numpy
   2. Using a nested `for` loop or a list comprehension
   3. Using numpy broadcasting operations
"""
import numpy as np

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

print("using the function 'outer' in numpy")
print(np.outer(u, v))
print()

print("Using a nested `for` loop or a list comprehension")
print(np.array([i * j for i in v for j in u]).reshape(4, 4).T)
print()
print("using numpy broadcastig operation")
print(np.ones((4, 4)) * v * (np.ones((4, 4)) * u).T)
print()
///////////////////////////END OF SOLUTION 2////////////

#SOLUTION NUMBER 3

"""
3\. **Matrix masking**

Create a 10 by 6 matrix of float random numbers, distributed between 0 and 3 according to a flat distribution.

After creating the matrix, set all entries $< 0.3$ to zero using a mask.
"""
import numpy.random as np

matrix = np.uniform(0, 3, size=(10, 6))
print("Original Matrix:\n", matrix)
print()

mask = matrix < 0.3
matrix[mask] = 0

print("Matrix after setting entries < 0.3 to zero:")
print(matrix)
//////////////////////////////////////END OF SOLUTION 3/////

#SOLUTION NUMBER 4
"""
4\. **Trigonometric functions**

Use `np.linspace` to create an array of 100 numbers between $0$ and $2\pi$ (inclusive).

  * Extract every 10th element using the slice notation
  * Reverse the array using the slice notation
  * Extract elements where the absolute difference between the `sin` and `cos` functions evaluated for that element is $< 0.1$
  * **Optional**: make a plot showing the sin and cos functions and indicate where they are close
"""
import numpy as np
import math

Array_E = np.linspace(0, 2 * np.pi, 100)
print("Array of 100 numbers between 0 to 2pi")
print(Array_E)
print()

tenth = Array_E[0:100:10]
print("Every 10th element from 0 to 100:")
print(tenth)
print()

Reverse = Array_E[::-1]
print("Reversed array:")
print(Reverse)
print()

A_diff = np.array([i for i in a if abs(math.sin(i) - math.cos(i)) < 0.1])
print("elements for the absolute diff between sin and cos functions")
print(A_diff)
///////////////END OF SOLUTION 4//////

SOLUTION NUMBER 5

"""
5. Matrices
Create a matrix that shows the 10 by 10 multiplication table.
Find the trace of the matrix
Extract the anti-diagonal matrix (this should be array([10, 18, 24, 28, 30, 30, 28, 24, 18, 10]))
Extract the diagonal offset by 1 upwards (this should be array([ 2, 6, 12, 20, 30, 42, 56, 72, 90]))
"""

import numpy as np

a = np.ones((10, 10))
b = np.linspace(1, 10, 10)
matrix = np.outer(b, b.T)
print("Matrix")
print(matrix)  # built the matrix

trace = 1
antidiag = np.array([])
offdiag = np.array([])
for i in range(10):
    trace = trace * matrix[i][i]  # find the trace
    antidiag = np.append(antidiag, matrix[i][9 - i])  # find anti-diagonal matrix
    try:
        offdiag = np.append(offdiag, matrix[i + 1][i])  # find offset 1 diagonal
    except:
        print()
print("Trace of the matrix:  ", trace)
print()
print("Anti-diagonal matrix:  ", antidiag)
print()
print("Diagonal offset by 1:  ", offdiag)
////////////////////////END OF SOLUTION 5//////////

#SOLUTION NUMBER 6

"""
6. Broadcasting
Use broadcasting to create a grid of distances.
Route 66 crosses the following cities in the US: Chicago, Springfield, Saint-Louis, Tulsa, Oklahoma City,
Amarillo, Santa Fe, Albuquerque, Flagstaff, Los Angeles.
The corresponding positions in miles are: 0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448
Build a 2D grid of distances among each city along Route 66
Convert the distances in km
"""
import numpy as np
import matplotlib.pyplot as plt

cities = ["Chicago", "Springfield", "Saint-Louis", "Tulsa", "Oklahoma City", "Amarillo", "Santa Fe",
"Albuquerque","Flagstaff", "Los Angeles"]
dist = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
a = np.tile(dist, (10, 1)).T
a = abs(a - dist)  # built the matrix

print("DISTANCES IN MILES\n")
fig, ax = plt.subplots()  # plot the grid
ax.set_axis_off()
table = plt.table(cellText=a, rowLabels=cities, colLabels=cities, loc='center')
table.scale(10, 10)
table.set_fontsize(32)
plt.show()
print()

a = (a * (np.ones((10, 10)) * 1.60934)).round(decimals=0)  # conversion in km
print("DISTANCE IN KM\n")
fig, ax = plt.subplots()  # plot the grid
ax.set_axis_off()
table = plt.table(cellText=a, rowLabels=cities, colLabels=cities, loc='center')
table.scale(10, 10)
table.set_fontsize(32)
plt.show()
//////////////////END OF SOLUTION 6//////////////

#SOLUTION NUMBER 7
"""
7. Prime numbers sieve
Compute the prime numbers in the 0-N (start with N=99) range with a sieve (mask).
Constract a shape (N,) boolean array, which is the mask
Identify the multiples of each number starting from 2 and set accordingly the corresponding mask element
Apply the mask to obtain an array of ordered prime numbers
Check the performances (with timeit); how does it scale with N?
Implement the optimization suggested in the sieve of Eratosthenes
"""
import numpy as np
import timeit
N=100
a = np.arange(1, N)
primes = np.array([])

for i in a:
    mask1 = (a<=i)
    filtered_a = a[mask1]
    mask2 = (i%filtered_a==0)
    dividers = filtered_a[mask2]
    if dividers.size == 2:
        primes = np.append(primes, i)
print("List of prime numbers in range 0 -",N,":  \n\n", primes.astype(int))
////////////////////END OF SOLUTION 7/////

#SOLUTION NUMBER 8
"""
8. Diffusion using random walk**

Consider a simple random walk process: at each step in time, a walker jumps right or left (+1 or -1) with equal probability. The goal is to find the typical distance from the origin of many random walkers after a given amount of time.

Hint*: create a 2D array where each row represents a walker, and each column represents a time step.

   Take 1000 walkers and let them walk for 200 steps
   Use `randint` to create a 2D array of size $walkers \times steps$ with values -1 or 1
   Calculate the walking distances for each walker (e.g. by summing the elements in each row)
   Take the square of the previously-obtained array (element-wise)
   Compute the mean of the squared distances at each step (i.e. the mean along the columns)
   *Optional**: plot the average distances ($\sqrt(distance^2)$) as a function of time (step)
"""
import matplotlib.pyplot as plt
import numpy as np

a = np.random.randint(2, size=(1000, 200))
a[np.where(a == 0)] = -1
print(a)
print()
walking_dist = np.sum(a, axis=1)
print("walking distance of each walker:\n", walking_dist)
print()
sq_a = np.power(walking_dist, 2)
print("element-wise square is:\n", sq_a)
print()

mean = []
for i in range(1, 200):
    b = a[:, i].mean()
    mean.append(b)
print("mean along the columns is:\n", mean)
print()
average_distance = np.sqrt(sq_a)
print("average distances:\n", average_distance)

array = average_distance
time = np.sort(array)
plt.plot(time, array)
plt.xlabel('Time')
plt.ylabel('Average Distances')
///////////////////////////END OF SOLUTION 8//////////

