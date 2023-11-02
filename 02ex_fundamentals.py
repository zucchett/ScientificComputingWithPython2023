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

# In[ ]:


x = 5

def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed


# 2\. **List comprehension**
# 
# Write the following expression using a list comprehension:
# 
# `ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))`

# In[ ]:


print([i**2 for i in range(10) if i % 2 != 0])


# 3\. **Filter list**
# 
# Using the `filter()` hof, define a function that takes a list of words and an integer `n` as arguments, and returns a list of words that are shorter than `n`.

# In[ ]:


i=0
def func(word):
    global i
    n = 3
    if(i<n):
        i+=1
        return True
    return False    
r = filter(func, ['php', 'javascript', 'java', 'c++', 'c', 'python', 'go', 'rust', 'dart', 'swift'])
print(list(r))


# 4\. **Map dictionary**
# 
# 
# Consider the following dictionary:
# 
# `lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}`
# 
# Write a function that takes the above dictionary and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary.

# In[ ]:


def f(string):
    return len(string)
 
print(list(map(f, {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7})))       


# 5\. **Lambda functions**
# 
# Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:
# 
# `language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]`
# 
# *Hint*: use the method `sort()` and its argument `key` of the `list` data structure.

# In[ ]:


print(sorted([('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)], key = lambda x : x[0],reverse=False))


# 6\. **Nested functions**
# 
# Write two functions: one that returns the square of a number, and one that returns its cube.
# 
# Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.

# In[ ]:


def square(number):
    return number**2

def cube(number):
    return number**3    

def six_power(number):
    return number * square(number) * cube(number)

print(six_power(2))


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

# In[14]:


def hello(func):
    def wrapper(x):
        print('Hello World!')
        func(x)
    return wrapper


@hello 
def square(x):
    print(x*x)

square(5)


# 8\. **The Fibonacci sequence (part 2)**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using a recursive function.

# In[15]:


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 1
while (n <= 20):
    print(fibonacci(n), end=' ')
    n += 1


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

# In[16]:


import timeit

def fibonacci(n):
    fibonacci = [1, 1]
    for i in range(1, n - 1):
        fibonacci.append(fibonacci[i] + fibonacci[i - 1])
    return fibonacci    

def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

start = timeit.default_timer()
fibonacci(40)
print('Time taken for normal fibonacci -> ' + str(timeit.default_timer() - start))

start = timeit.default_timer()
recursive_fibonacci(40)
print('Time taken for recursive fibonacci -> ' + str(timeit.default_timer() - start))


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

# In[21]:


class polygon:
    sides = None
    def __init__(self, sides:tuple) -> None:
        if len(sides) < 3:
            raise Exception('Sides should contain at least 3 items.')
        self.sides = sides

    def get_sides(self) -> tuple:
        return self.sides

    def set_sides(self, sides:tuple) -> None:
            if len(sides) < 3:
                raise Exception('Sides should contain at least 3 items.')
            self.sides = sides     

    def perimeter(self) -> float:
        sum = 0
        for item in self.sides:
            sum += item
        return sum    

    def get_ordered_sides(self, increasing):
        return sorted(self.sides, reverse=not increasing)
        

triangle = polygon((3, 4, 5))
print(triangle.get_sides())
triangle.set_sides((8, 6, 10))
print(triangle.get_sides())
print(triangle.perimeter())
print(triangle.get_ordered_sides(False))


# 11\. **Class inheritance**
# 
# Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.
# 
# - Create a method `area()` that returns the area of the rectangle.
# 
# Test the `rectangle` class by creating an instance and passing an appropriate input to the constructor.

# In[22]:


import math

class polygon:
    sides = None
    def __init__(self, sides:tuple) -> None:
        if len(sides) < 3:
            raise Exception('Sides should contain at least 3 items.')
        self.sides = sides

    def get_sides(self) -> tuple:
        return self.sides

    def set_sides(self, sides:tuple) -> None:
            if len(sides) < 3:
                raise Exception('Sides should contain at least 3 items.')
            self.sides = sides     

    def perimeter(self) -> float:
        sum = 0
        for item in self.sides:
            sum += item
        return sum    

    def get_ordered_sides(self, increasing):
        return sorted(self.sides, reverse=not increasing)

class rectangle(polygon):
    def __init__(self, sides: tuple) -> None:
        super().__init__(sides)

        #if not(self.sides[0] == self.sides[1] and self.sides[3] == self.sides[2]) or not(self.sides[0] == self.sides[2] and self.sides[1] == self.sides[3]) or not(self.sides[0] == self.sides[3] and self.sides[1] == self.sides[2]):
            #raise Exception('These number can not form rectangle')

    def area(self):
        return self.sides[0] + self.sides[1] + self.sides[2] + self.sides[3]


r = rectangle((1, 1, 2, 2))
print(r.area())


# In[ ]:




