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


import copy
x = 10

def f(alist):
    new = alist.copy()
    for i in range(x):
        new.append(i)
    return new

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed


# 2\. **List comprehension**
# 
# Write the following expression using a list comprehension:
# 
# `ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))`

# In[6]:


numeri = [x for x in range(10)]
list_com = [x**2 for x in numeri if x % 2 == 1]
print(list_com)


# 3\. **Filter list**
# 
# Using the `filter()` hof, define a function that takes a list of words and an integer `n` as arguments, and returns a list of words that are shorter than `n`.

# In[1]:


words = ["telefono", "bad", "custodia", "occhiali", "jager"]
n = 6

def short(word):
    if len(word) < n:
        return word

short_words = list(filter(short, words))

print(short_words)


# 4\. **Map dictionary**
# 
# 
# Consider the following dictionary:
# 
# `lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}`
# 
# Write a function that takes the above dictionary and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary.

# In[2]:


def len_key(x):
    return len(x)

ang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

keys_L = list(map(len_key, ang.keys()))

print(keys_L)


# 5\. **Lambda functions**
# 
# Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:
# 
# `language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]`
# 
# *Hint*: use the method `sort()` and its argument `key` of the `list` data structure.

# In[8]:


language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

# lambda returns the 1st element of the tuple 
# x is a tuple
language_scores.sort(key=lambda x: x[0])

print(language_scores)


# 6\. **Nested functions**
# 
# Write two functions: one that returns the square of a number, and one that returns its cube.
# 
# Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.

# In[2]:


def square(a):
    return a*a

def cube(a):
    return a*a*a

n = float(input("Insert the number you want to raise to the 6th power: "))
print(cube(square(n)))


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


def hello(func):
    def wrapper(a):
        res = func(a)
        print("Hello World!")
        return res
    return wrapper

@hello
def square(x):
    return x*x

x = 20

print(square(x))


# 8\. **The Fibonacci sequence (part 2)**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using a recursive function.

# In[3]:


def Fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        a = Fibo(x-1)+Fibo(x-2)
        return a
    
n = 20 

for i in range(n+1):
    print(Fibo(i))


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

# In[10]:


import timeit

def recursiveFibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        a = Fibo(x-1) + Fibo(x-2)
        return a
    
execution_time = timeit.timeit("recursiveFibonacci(20)", globals=globals(), number=1)

print(f"Tempo di esecuzione ricorsione: {execution_time} secondi")

def loopFibonacci(n):
    fir = 0
    sec = 1
    for i in range(n+1):
        r = fir + sec
        fir = sec
        sec = r
    return r

execution_time = timeit.timeit("loopFibonacci(20)", globals=globals(), number=1)

print(f"Tempo di esecuzione loop: {execution_time} secondi")


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

# In[3]:


class polygon:
    
    # Definition of the Constructor, a special method that is called every time a new object is created
    # The first argument of the constructor (and also for all other methods in the class) is the instance itself
    def __init__(self, sides):
        self.sides = sides # a list is expected as input
    
    # Definition of the methods
    
    def getSide(self, n):
        return self.sides[n]
    
    def setSide(self, n, value): # n is the side index, and xi is the value
        if n < len(self.sides):
            self.sides[n] = value
        
    def perimeter(self):
        p=0
        for i in range(len(self.sides)):
            p += self.sides[i]
        return p
    
    def getOrderedSides(self, increasing = True):
        sorted_sides = list(self.sides)
        sorted_sides.sort(reverse=not increasing)
        return tuple(sorted_sides)
    
sides = []
n = int(input("How many sides? "))

if n > 3:
    for i in range(n):
        sides.append(float(input("Insert a value: ")))
        
    poly = polygon(tuple(sides))
    print("Perimeter: ", poly.perimeter())
    print("Increasing sides: ", poly.getOrderedSides(True))
    print("Decreasing sides: ", poly.getOrderedSides(False))

else:
    print("Goodbye mf")
    

        
        


# 11\. **Class inheritance**
# 
# Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.
# 
# - Create a method `area()` that returns the area of the rectangle.
# 
# Test the `rectangle` class by creating an instance and passing an appropriate input to the constructor.

# In[9]:


class rectangle(polygon):
    
    def __init__(self, sides):
        if len(sides) == 2:
            self.sides = sides 
        else:
            print("Error: number of sides is not 4")
            
    def area(self):
        a = 0
        a = self.sides[0] * self.sides[1]
        return a

sides = []
for i in range(2):
    sides.append(float(input("Insert a value: ")))
        
rec = rectangle(tuple(sides))
print("Area: ", rec.area())


# In[ ]:




