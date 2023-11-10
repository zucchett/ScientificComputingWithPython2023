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



## Exercise 5



## Exercise 6



## Exercise 7

