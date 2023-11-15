#***************************Ex 1.1*******************************
# Initialize a variable x
x = 5

# Define a function that appends integers from 0 to x-1 to a list
def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

# Initialize a list called alist
alist = [1, 2, 3]

# Call the function f and store the result in ans
ans = f(alist)

# Print the result of the function
print("Result of f(alist):", ans)

# Print the modified alist (alist has been changed by the function)
print("Modified alist:", alist)

#***************************Ex 1.2*******************************
import copy

# Define a function that appends n numbers to a copy of the original list
def new_f(alist, n):
    print("Before the function: ", alist)
    
    # Create a copy of the original list
    temp_list = copy.copy(alist)
    
    # Append n numbers to the copy
    for i in range(n):
        temp_list.append(i)
    
    # Return the modified copy
    return temp_list

# Initialize a list called alist
alist = [1, 2, 3]

# Call the function new_f and store the result in ans
ans = new_f(alist, 5)

# Print the result of the function
print("Result of new_f(alist, 5):", ans)

# Print the original alist (original list remains unchanged)
print("Original alist:", alist)

#***************************Ex 2*******************************
# Create a list using a list comprehension
# It contains the squares of odd numbers from 0 to 9
ans = [x**2 for x in range(10) if x % 2 == 1]

# Print the result
print(ans)

#***************************Ex 3*******************************
# Define a function that checks if the length of a word is less than n
def shorter_words(word):
    return len(word) < n

# Input words as a string and the value of n
words = "lorem ipsum docet dolorem luna sole ape"
n = 5

# Use filter to create a list of words shorter than n
ans = list(filter(shorter_words, words.split()))

# Print the result
print(ans)

#***************************Ex 4*******************************
# Define a function that returns the length of the key
def key_length(element):
    key, value = element
    return len(key)

# Define the dictionary
lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}

# Use map to create a list of key lengths
ans = list(map(key_length, lang.items()))

# Print the result
print(ans)

#***************************Ex 5*******************************
# Define the list of tuples
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

# Print the original list
print("Original list:", language_scores)

# Sort the list alphabetically by the first element of each tuple using a lambda function as the key
language_scores.sort(key=lambda element: element[0])

# Print the sorted list
print("Sorted list:", language_scores)

#***************************Ex 6*******************************
# Define a function that calculates the square of a number
def square(x):
    return x**2

# Define a function that calculates the cube of a number
def cube(x):
    return x**3

# Define a function that calculates the sixth power of a number
# It does this by first squaring the input and then cubing the result
def sixth_power(x):
    return square(cube(x))

# Call the sixth_power function with an input of 3
result = sixth_power(3)

# Print the result
print("The sixth power of 3 is:", result)

#***************************Ex 7*******************************
# Define a decorator function that adds "Hello world!" messages before and after the original function
def hello_world_decorator(func):
    def wrapper(x):
        print("Hello world!")  # Message before
        print(func(x))         # Call the original function
        print("Hello world!")  # Message after
    return wrapper

# Decorate the square function with the hello_world_decorator
@hello_world_decorator
def square(x):
    return x * x

# Call the decorated square function
square(8)

#***************************Ex 8*******************************
# Define a recursive function to calculate the Fibonacci sequence
def recursive_fibonacci(prev=0, curr=1, iteration=20):
    # Base case: return curr if iteration is 0
    if iteration == 1:
        return curr

    # Calculate the next Fibonacci number
    next_fibonacci = prev + curr

    # Recursively call the function with updated values and decremented iteration
    return recursive_fibonacci(curr, next_fibonacci, iteration - 1)

# Call the function with default values
result = recursive_fibonacci(iteration = 20)
print("The 20th Fibonacci number is:", result)

#***************************Ex 9*******************************
import timeit
def fibonacci_loop(x):
    # Initialize variables for the Fibonacci sequence
    current_number = 0
    prev_number = 0

    # Create a list to store the Fibonacci sequence, starting with 0
    fibonacci = [current_number]

    # Generate the Fibonacci sequence for the first 20 numbers
    for i in range(x):
        # Calculate the next number in the sequence
        next_number = int(prev_number) + int(current_number)

        # Update the variables for the next iteration
        prev_number = current_number
        current_number = next_number

        # Ensure that prev_number is not 0 for the next iteration
        if (prev_number == 0):
            prev_number = 1

        # Add the next_number to the Fibonacci sequence
        fibonacci.append(next_number)
    return fibonacci

# Measure the execution time of the Fibonacci loop function
time_fibonacci_loop = timeit.timeit("fibonacci_loop(20)", globals=globals(), number=10000)

# Measure the execution time of the recursive Fibonacci function
time_recursive_fibonacci = timeit.timeit("recursive_fibonacci(iteration = 20)", globals=globals(), number=10000)

# Print the execution times for comparison
print("Execution time for the Fibonacci loop:", time_fibonacci_loop)
print("Execution time for the recursive Fibonacci:", time_recursive_fibonacci)

# Compare the execution times and print the result
if (time_fibonacci_loop > time_recursive_fibonacci):
    print("The recursive Fibonacci is faster by", time_fibonacci_loop - time_recursive_fibonacci, "milliseconds")
else: 
    print("The Fibonacci loop is faster by", time_recursive_fibonacci - time_fibonacci_loop, "milliseconds")

#***************************Ex 10*******************************
class Polygon:
    def __init__(self, components):
        self.dimensions = components

    def getDimension(self, n):
        # Return the nth component of the polygon
        return self.dimensions[n]

    def getDimensions(self):
        # Return a list of all components of the polygon
        return self.dimensions

    def setDimension(self, n, new_dimension):
        # Update the nth component of the polygon with a new value
        if n < len(self.dimensions):
            self.dimensions[n] = new_dimension

    def getPerimeter(self):
        # Calculate and return the perimeter of the polygon (sum of all components)
        return sum(self.dimensions)

    def getOrderedSize(self, increasing=True):
        # Return a sorted list of components, either in increasing or decreasing order
        sorted_dimensions = sorted(self.dimensions)
        if not increasing:
            sorted_dimensions.reverse()
        return sorted_dimensions
    
# Create a Polygon with 4 components (quadrilateral)
quad = Polygon([3, 3, 3, 3])

# Create another Polygon with 3 components (triangle)
tri = Polygon([6, 4, 5])

# Calculate and print the perimeter of the triangle
tri_perimeter = tri.getPerimeter()
print("Perimeter of the triangle:", tri_perimeter)

# Calculate and print the perimeter of the quadrilateral
quad_perimeter = quad.getPerimeter()
print("Perimeter of the quadrilateral:", quad_perimeter)

# Get and print the dimensions of the triangle
tri_dimensions = tri.getDimensions()
print("Dimensions of the triangle:", tri_dimensions)

# Get and print a sorted list of components of the triangle in increasing order
sorted_tri_increasing = tri.getOrderedSize(True)
print("Sorted dimensions of the triangle (increasing):", sorted_tri_increasing)

# Get and print a sorted list of components of the triangle in decreasing order
sorted_tri_decreasing = tri.getOrderedSize(False)
print("Sorted dimensions of the triangle (decreasing):", sorted_tri_decreasing)

#***************************Ex 11*******************************
class Rectangle(Polygon):
    def __init__(self, components):
        # Check if the given components form a valid rectangle
        if len(components) == 4 and (components[0] == components[2] or components[1] == components[3]):
            super().__init__(components)  # Call the constructor of the base class (Polygon)
            print("Rectangle created succesfully")
        else:
            print("Error: This is not a valid rectangle")

    def area(self):
        # Calculate and return the area of the rectangle
        return self.getDimension(0) * self.getDimension(1)
    
# Create a valid rectangle with length 3 and width 4
rec1 = Rectangle([3, 4, 3, 4])

# Attempt to create a rectangle with an invalid number of components
rec2 = Rectangle([1, 2, 1, 2, 3])

# Create a valid rectangle with length 5 and width 4
rec = Rectangle([5, 4, 5, 4])

# Calculate and print the area of the valid rectangle
area = rec.area()
print("Area of the rectangle:", area)