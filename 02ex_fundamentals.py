#!/usr/bin/env python
# coding: utf-8

# You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a single dedicated `.py` file called `02ex_fundamentals.py`.
# 
# You can divide the individual exercises in the source code with appropriate comments (`#`).
# 
# The exercises need to run without errors with `python3 02ex_fundamentals.py`.

# 1\. **Global variables**
# 
# Convert the function $f$ into a function that doesn't use global variables and that does not modify the original list

# In[1]:


print("\n--- 1. Global variables ---\n")

import copy

def f(alist, x):
    alist_copy = copy.copy(alist)
    for i in range(x):
        alist_copy.append(i)
    return alist_copy

x = 5
alist = [1, 2, 3]
new_alist = f(alist, x)

print("You can see that the alist list has not changed : alist =", alist)
print("However, the output list of the function is quite different from alist : new_alist =", new_alist)


# 2\. **List comprehension**
# 
# Write the following expression using a list comprehension:
# 
# `ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))`

# In[2]:


print("\n--- # 2. List comprehension ---\n")

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print("With the method: list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))), we obtain the following list:\n =>", ans)

ans2 = [x**2 for x in range(10) if x % 2 == 1] # odd numbers are squared
print("Using a list comprehension such as the following: [x**2 for x in range(10) if x % 2 == 1], we obtain the same results as above:\n =>", ans2)


# 3\. **Filter list**
# 
# Using the `filter()` hof, define a function that takes a list of words and an integer `n` as arguments, and returns a list of words that are shorter than `n`.

# In[3]:


print("\n--- # 3. Filter list ---\n")

def len_words(list_words, n):
    return list(filter(lambda word: len(word) < n, list_words)) # Use the filter function to filter words with a lambda function used to check the length of each word relative to n

list_words = ["Apple", "Dog", "Cat", "Car", "Plane", "Python", "Programmation"]

print("This is the list used for the test :", list_words)
print("\n=> For n = 7 :", len_words(list_words, n = 7))
print("\n=> For n = 5 :", len_words(list_words, n = 5))
print("\n=> For n = 2 :", len_words(list_words, n = 2))


# 4\. **Map dictionary**
# 
# 
# Consider the following dictionary:
# 
# `lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}`
# 
# Write a function that takes the above dictionary and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary.

# In[4]:


print("\n--- 4. Map dictionary ---\n")

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print("This is the dictionary used for the test :", lang)

def Map_dictionnazy(dictionnary):
    return list(map(len,dictionnary.keys())) 
    
print("\n=> We obtain :", Map_dictionnazy(lang))


# 5\. **Lambda functions**
# 
# Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:
# 
# `language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]`
# 
# *Hint*: use the method `sort()` and its argument `key` of the `list` data structure.

# In[5]:


print("\n--- 5. Lambda functions ---\n")

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
print("Here is the list of tuples used for the test :", language_scores)

language_scores.sort(key=lambda x: x[0]) 

print("\n=> After sorting alphabetically on the first element of the tuple, we obtain :", language_scores)


# 6\. **Nested functions**
# 
# Write two functions: one that returns the square of a number, and one that returns its cube.
# 
# Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.

# In[6]:


print("\n--- 6. Nested functions ---\n")

# Defines a function that calculates the square of a number
def square(x):
    return x**2

# Defines a function that calculates the cube of a number
def cube(x):
    return x**3

# Define a function that calculates the power of 6 of a number
# To do this, use the previously defined square and cube functions
def power6(x):
    return square(cube(x))

# --------------------------

import random

print("Here are 3 tests performed with randoms between 1 and 10 :")

for i in range(3): # Perform 3 tests with random numbers between 1 and 10
    random_value = random.randint(1, 10)  # Generates a random number between 1 and 10
    result = power6(random_value) # Calculate the power of 6 of this random number
    print(f"\n => Taking {random_value} as the number, we obtain the following power of 6: {result}")


# 7\. **Decorators**
# 
# Write a decorator named `hello` that makes every wrapped function print “Hello World!” each time the function is called.
# 
# The wrapped function should look like:
# 
# ```python
# @hello
# def square(x):
#     return x*x
# ```

# In[7]:


print("\n--- 7. Decorators ---\n")

# Define a decorator named 'hello'
def hello(func):
    def wrapper(x):
        print("Hello World!") # Display "Hello World!" each time the wrapped function is called
        return func(x) # Call the original function and return its result, otherwise the return function returns None
    return wrapper

# Use the 'hello' decorator to modify the behavior of the 'square' function
@hello
def square(x):
    return x*x


# Examples 
# Call the 'square' function wrapped by the decorator
# This will display "Hello World!" followed by the result of square

print("Using square(5), we obtain :\n")
print(square(5))
print("\n-----\n")
print("Using square(10), we obtain :\n")
print(square(10))


# 8\. **The Fibonacci sequence (part 2)**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using a recursive function.

# In[8]:


print("\n--- 8. The Fibonacci sequence (part 2) ---\n")

# Define a function to recursively calculate the nth term of the Fibonacci sequence
def recursiveFibonacci(n):
    if n == 0 : # F_0: the first term of the Fibonacci sequence is 0
        return 0
    elif n == 1 : # F_1: the first term of the Fibonacci sequence is 0
        return 1
    else : 
        return recursiveFibonacci(n-1)+recursiveFibonacci(n-2) # For any other term, it is the sum of the two preceding terms

List_Fibonacci = []
for i in range(20):
    List_Fibonacci.append(recursiveFibonacci(i))

print("Using a recursive function, we obtain the first 20 numbers of the Fibonacci list :\n\n", List_Fibonacci)


# 9\. **The Fibonacci sequence (part 3)**
# 
# Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only `for` and `while` loops.
# 
# Measure the execution code of the two functions with `timeit` ([link to the doc](https://docs.python.org/3/library/timeit.html)), for example:
# 
# `%timeit loopFibonacci(20)`
# 
# `%timeit recursiveFibonacci(20)`
# 
# which one is the most efficient implementation? By how much?

# In[9]:


print("\n--- 9. The Fibonacci sequence (part 3) ---\n")

def loopFibonacci(nb):
    list_Fibonacci = [0, 1]
    while len(list_Fibonacci) < nb :
        list_Fibonacci.append(list_Fibonacci[-1]+list_Fibonacci[-2])
    return list_Fibonacci

List_loopFibonacci = loopFibonacci(20)
print("Using a loop function, we obtain the first 20 numbers of the Fibonacci list :\n\n", List_loopFibonacci)

print("\n\nDoes a function using a loop or recursion return the same result ? => ", List_loopFibonacci == List_Fibonacci)


# In[10]:


# WARNING: We don't use %timeit, otherwise we'll have a problem when we run the .py code via Python3.
# So, we decided to create our own function to solve this problem

import timeit


# In[20]:


print("\n=> For the Fibonacci function using a loop, we obtain the following execution time :")

# %timeit loopFibonacci(20) # 2.72 µs ± 642 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

loop_time = timeit.timeit(lambda: loopFibonacci(20), number = 1000)
print(loop_time, "ms")


# In[21]:


print("\n=> For the Fibonacci function using recursion, we obtain the following execution time :")

# %timeit recursiveFibonacci(20) # 2.02 ms ± 72.2 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

rec_time = timeit.timeit(lambda: recursiveFibonacci(20), number = 1000)
print(rec_time, "ms")


# In[13]:


print("""\n\n=> Which is more efficient?

The loop version, loopFibonacci, is clearly more efficient than the recursive version, recursiveFibonacci.



=> By how much more efficient?

If we compare the two execution times:
2020 µs (recursiveFibonacci) divided by 2.72 µs (loopFibonacci) gives approximately 742.65.

This means that recursiveFibonacci is around 742 times slower than loopFibonacci in calculating the 20th term of the Fibonacci sequence.

In conclusion, using a loop to generate the Fibonacci sequence is clearly more efficient than the recursive approach, at least for the 20th term. This contrast would become even more marked for higher values of n.""")


# 10\. **Class definition**
# 
# Define a class `polygon`. The constructor has to take a tuple as input that contains the length of each side. The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.
# 
# - Create appropriate methods to get and set the length of each side
# 
# - Create a method `perimeter()` that returns the perimeter of the polygon
# 
# - Create a method `getOrderedSides(increasing = True)` that returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method
# 
# Test the class by creating an instance and calling the `perimeter()` and `getOrderedSides(increasing = True)` methods.

# In[52]:


print("\n--- 10. Class definition ---\n")

class Polygon: # Polygon class definition
    
    # Initialize a constructor that accepts a tuple containing the length of each side
    def __init__(self, sides):
        if len(sides) < 3: # If the polygon has at least 3 sides
            raise ValueError("Error : A polygon has at least 3 sides. Added values.") # If the polygon has less than 3 sides, raise an error
        elif not all(side > 0 for side in sides): # If one of the lengths is negative
            raise ValueError("Error : One of the Polygon sizes is negative. Use positive values.") # If the polygon has a negative length, raise an error
        else :
            self.sides = tuple(sides) 

    # Method for obtaining the length of each side
    def getAllSides(self):
        return self.sides

    # Method for defining the length of each side
    def setAllSides(self, sides):
        if len(sides) < 3: # If the polygon has at least 3 sides
            raise ValueError("Error : A polygon has at least 3 sides. Added values.") # If the polygon has less than 3 sides, raise an error
        elif not all(side > 0 for side in sides): # If one of the lengths is negative or not of type int or float
            raise ValueError("Error : One of the polygon sizes is negative or not of type int or float. Change the values.") # If the polygon has a negative length or not of type int or float , raise an error
        else :
            self.sides = tuple(sides) 
            return self.sides
    
    # Method for obtaining the length of each side
    def getOneSide(self, n):
        self.sides = list(self.sides)
        return self.sides[n]

    # Method for defining the length of each side
    def setOneSide(self, n, new_side):
        if len(self.sides) < n+1 :
            raise ValueError("Error : The given n value does not match the initial polygon size.") # If the polygon has a negative length, raise an error
        elif new_side < 0 :
            raise ValueError("Error : The desired polygon size is negative or not of type int or float. Change the value.") # If the polygon has a negative length or not of type int or float, raise an error
        else :
            self.sides = list(self.sides) 
            self.sides[n] = new_side
            self.sides = tuple(self.sides)
            return self.sides 
    

    # Method for calculating and returning the polygon perimeter
    def perimeter(self):
        return sum(self.sides) # Add the length of all sides to obtain the perimeter

    # Method to obtain sides ordered in ascending or descending order
    def getOrderedSides(self, increasing = True):
        # Sort sides in ascending or descending order according to the 'increasing' argument
        return tuple(sorted(self.sides, reverse= not increasing))


# In[61]:


print("A polygon is created which depends on the Polygon class created : polygon = Polygon((1, 4, 3, 9))")
polygon = Polygon((1, 4, 3, 9))
print("\n=> Polygon description using getAllSides :", polygon.getAllSides())
print("\n=>We can obtain the description of the nth value of the polygon using getOneSide. For example, the 1st value (in Python language, with 0 here) of this polygon is : ", polygon.getOneSide(0))
print("\n=> We can also change the nth value of the polygon by using setOneSide, and supplying the new length. For example, the 1st value (in Python language, i.e. 0 here) of this polygon is replaced by 2 : ", polygon.setOneSide(0,2))
print("The first value is now 2 : ", polygon.getAllSides())
print("\n=> We can also replace all the values contained in this polygon using setAllSides. We now transform this polygon to contain (5,2,4,3,8,9).", polygon.setAllSides((5,2,4,3,8,9)))
print("\nPolygon description using getAllSides :", polygon.getAllSides())
print("\n\n\nWe'll now illustrate the various perimeter() and getOrderedSides(increasing) functions.")
print("\n=> Perimeter of the polygon :", polygon.perimeter())
print("\n=> Sides in increasing order :", polygon.getOrderedSides(increasing=True))
print("\n=> Sides in decreasing order :", polygon.getOrderedSides(increasing=False))


# 11\. **Class inheritance**
# 
# Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.
# 
# - Create a method `area()` that returns the area of the rectangle.
# 
# Test the `rectangle` class by creating an instance and passing an appropriate input to the constructor.

# In[16]:


print("\n--- 11. Class inheritance ---\n")

class Rectangle(Polygon): # Rectangle class definition
    
    # We adapt the Polygon constructor to suit Rectangle
    def __init__(self, sides):
        if not all(side > 0 for side in sides): 
            raise ValueError("Error : One of the Polygon sizes is negative. Use positive values.")
        elif len(sides) != 4: # We verify that we have 4 lengths
            raise ValueError("Error : A rectangle has exactly 4 sides.")
        elif sides[0] != sides[2] or sides[1] != sides[3]: # Check that both lengths and widths measure the same distance
            raise ValueError("Error : A rectangle should have two equal-length sides and two equal-width sides.")
        else:
            self.sides = tuple(sides)

    # Method for calculating and returning the rectangle area
    def area(self):
        return self.sides[0]*self.sides[1]   


# In[17]:


print("A rectangle is created which depends on the Rectangle class created : rectangle = Rectangle((7, 10, 7 ,10))")
rectangle = Rectangle((7, 10, 7 ,10))
print("\n=> Rectangle area :", rectangle.area())
print("\n=> Rectangle perimeter :", rectangle.perimeter())
print("\n=> Rectangle description using getAllSides :", rectangle.getAllSides())
print("\n=> We can obtain the description of the nth value of the rectangle using getOneSide. For example, the 1st value (in Python language, with 0 here) of this polygon is : ", rectangle.getOneSide(0))

