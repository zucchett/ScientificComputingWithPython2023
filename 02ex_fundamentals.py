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

#%%


x=5

def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed


#%%

import copy  

x=5

def f(alist):
    alist_copy = copy.copy(alist) #We use a copy to not modify the original list
    for i in range(x):
        alist_copy.append(i)
    return alist_copy

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist doesn't change

#%%

# 2\. **List comprehension**
# 
# Write the following expression using a list comprehension:
# 
# `ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))`

# In[16]:


ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))) #This code compute the square of x for x between 1 and 10 only for even values of x
print(ans)


# In[21]:


ans_comp = [x*x for x in range(10) if x%2 == 1]
print(ans_comp)

#%%

# 3\. **Filter list**
# 
# Using the `filter()` hof, define a function that takes a list of words and an integer `n` as arguments, and returns a list of words that are shorter than `n`.

#%%

def Filter_list(words, n):
    return list(filter(lambda x: len(x)<n, words))

words_1 = ['link', 'keyboard', 'computer', 'cat', 'tomatoes', 'hammer', 'bottle', 'ski']
n = 7

print(Filter_list(words_1, n)) #return only the wordy shorter than 7 letters

#%%

# 4\. **Map dictionary**
# 
# 
# Consider the following dictionary:
# 
# `lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}`
# 
# Write a function that takes the above dictionary and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary.

#%%

def Map_Dict(dico):
    return(list(map(lambda x: len(x), dico)))

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

print(Map_Dict(lang))

#%%

# 5\. **Lambda functions**
# 
# Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:
# 
# `language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]`
# 
# *Hint*: use the method `sort()` and its argument `key` of the `list` data structure.

#%%


language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key = lambda x: x[0])

print(language_scores)

#%%
# 6\. **Nested functions**
# 
# Write two functions: one that returns the square of a number, and one that returns its cube.
# 
# Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.

#%%


def Square(n):
    return n*n

def Cube(n):
    return n*n*n

def Power_6(n):
    return Square(Cube(n))

a = 3
print("a = ", a)
print("a_2 = ", Square(a))
print("a_3 = ", Cube(a))
print("a_6 = ", Power_6(a))

#%%

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

#%%


def hello(func):
    def wrapper(n):
        print("Hello_World")
        func(n)
        return func(n)
    return wrapper

@hello
def square(x):
    return x*x

square(5)
print(square(5))

#%%

# 8\. **The Fibonacci sequence (part 2)**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using a recursive function.

#%%

def Fibonacci(n):
    f=[0, 1]    
    while(len(f)<n):
        f.append(f[-1]+f[-2])
    return f

print(Fibonacci(20))


#%%

def Fibonacci_Rec(n): #With recusrsive method
    if n==1:
        return 1 #Final output Fibonacci(1) = 1
    elif n==0: #Final output Fibonacci(0) = 0
        return 0
    else:
        return Fibonacci_Rec(n-1)+Fibonacci_Rec(n-2) #If n is not 0 or 1, we add the two previews numbers of the sequence and we reuse the function to compute them 

print(list(Fibonacci_Rec(x) for x in range(20)))

#%%

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

#%%


import timeit

starttime = timeit.default_timer()
print(list(Fibonacci_Rec(x) for x in range(21)))
temps_1 = timeit.default_timer() - starttime
print("The running time for the recursive function is :", temps_1)

starttime_2 = timeit.default_timer()
print(Fibonacci(20))
temps_2 = timeit.default_timer() - starttime_2
print("The running time for the while function is :", temps_2)

diff_time = temps_1/temps_2
print("The While function is ",round(diff_time)," times faster to run than the recursive one")

'''
The While function is  375  times faster to run than the recursive one because the recursive function calculate several time the same value of the sequence to compute the result 
'''

#%%

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

#%%


import math

class polygon:  
    x = []
    def __init__(self, side_length):
        if len(side_length)>=3:
            self.x = side_length
        else:
            print("A polygon has at least 3 side")
  
    #def __del__(self):
        #print("Goodbye")
    
    def getDimension(self):
        return len(self.x)
    
    def getX(self, n): 
        return self.x[n]
    
    def setX(self, n, xi):
        if n < len(self.x):
            a=list(self.x)
            a[n] = xi
            self.x=tuple(a)
    
    def perimeter(self):
        return sum(self.x)
    
    def getOrderedSides(self, increasing = True):
        return sorted(self.x, reverse=not(increasing))


#%%

Rectangle_1 = polygon((2.5,4,2.5,4))
Polygon_1 = polygon((2,5,3,7,2.143,4.2))

print("Rectangle 1: ", Rectangle_1.x,"\nPerimeter = ", Rectangle_1.perimeter() ,"\nOrdered sides = ", Rectangle_1.getOrderedSides())
print("\nPolygon 1: ", Polygon_1.x,"\nPerimeter = ", Polygon_1.perimeter() ,"\nOrdered sides = ", Polygon_1.getOrderedSides(False))

NotAPoly = polygon((2,5)) #Error message "A polygon has at least 3 side"

print("\nDimension Polygon 1 = ", Polygon_1.getDimension())
print("5e élément de Polygon 1 = ", Polygon_1.getX(4))
Polygon_1.setX(4,6.43)
print("Le 5e élémet de Polygon 1 est modifié : ", Polygon_1.x)

#%%

# 11\. **Class inheritance**
# 
# Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.
# 
# - Create a method `area()` that returns the area of the rectangle.
# 
# Test the `rectangle` class by creating an instance and passing an appropriate input to the constructor.

#%%

def Valid_Input(variable):
    if isinstance(variable, tuple) and len(variable) != 4:
        return False
    else:
        v=sorted(variable)
        if v[0]==v[1] and v[-1]==v[-2]:
            return True
        else:
            return False



class rectangle(polygon):
    
    def __init__(self, side_length):
        if Valid_Input(side_length):
            self.x = side_length
        else:
            print("A rectangle must have 4 sides equal two by two")
    
    def area(self):
        return min(self.x, default=0)*max(self.x, default=0)




Rec_1 = rectangle((3,7,3,7))
print(f"Rec_1 = {Rec_1.x} - area = {Rec_1.area()}")

Rec_2 = rectangle((1,4,5.3,2))

Rec_3 = rectangle((3,3,3,2))

Rec_4 = rectangle(tuple(4*[2.5]))
print(f"Rec_4 = {Rec_4.x} - area = {Rec_4.area()}")

