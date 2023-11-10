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



## Exercise 6



## Exercise 7

