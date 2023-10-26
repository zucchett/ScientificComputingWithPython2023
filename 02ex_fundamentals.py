#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:45:13 2023

@author: annamatzen
"""

## Exercise 1: Global variables

def f(alist):
    x = 5
    alist1 = alist.copy()
    for i in range(x):
        alist1.append(i)
    return alist1

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed


#%%
## Exercise 2: List comprehension
ans_new = [x * x for x in range(10) if x % 2 == 1]
print(ans_new)

#%%
## Exercise 3: Filter list

def filter_list(liste, n):
    mylist = filter(lambda x: len(x) < n, liste)
    return mylist

ll = ["Hello", "me", "foraverylongtime","beawareifyoumakeamistake"]
print(list(filter_list(ll,3)))
print(list(filter_list(ll,10)))
print(list(filter_list(ll,30)))


#%%
## Exercise 4: Map dictionaries
def length_keys(dictionary):
    key_lengths = list(map(len, dictionary.keys()))
    return key_lengths
        

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print("Here is the list containing the lengths of the keys in the dictionary:", length_keys(lang))


#%%
## Exercise 5: Lambda functions
def sort_alphabetic(tuples):
    tuples.sort(key = lambda x: x[0])
    return tuples

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

print("This is the list of tuples sorted alphabetically according to the first element of the tuple")
sort_alphabetic(language_scores)

#%%
## Exercise 6: Nested functions
def squares(x):
    x = x**2
    return x


def cubes(x):
    x = x**3
    return x

def six_times(x):
    x = squares(cubes(x))
    return x

print("Here is the output of the function, created by the square and cube function:", six_times(4))

#%%
## Exercise 7: Decorators
    
def hello(func):
    def wrapper(x):
        print("Hello World!")
        func(x)
        return func(x)
    return wrapper
    
@hello
def square(x):
    return x*x

print("This is the decorated function:", square(4))

#%%
## Exercise 8: Fibonacci sequence (part 2)

def fibo_seq(x):
    if x <= 0:
        return []
    elif x == 1:
        return [0]
    elif x == 2:
        return [0,1]
    else:
        FibSeq= fibo_seq(x-1)
        FibSeq.append(FibSeq[-1] + FibSeq[-2])
    return FibSeq

fibo_seq(20)

#%% 
## Exercise 9: Fibonacci sequence (part 3)

## This is the function from 01ex:
def loop_fibo(n):
    fibonacci_start = [0,1]
    for i in range(2,n):
        fib_next = fibonacci_start[i-1]+fibonacci_start[i-2]
        fibonacci_start.append(fib_next)
    return fibonacci_start

import timeit
print("The time taken for the non-recursive function: ", timeit.timeit(lambda:loop_fibo(20)))
print("The time taken for the recursive function: ", timeit.timeit(lambda:fibo_seq(20)))

## From the results it is clear that the non-recurse function is the fastest.
## The non-recursive function is 3.86 - 2.4 = 1.46 units faster than the recursive function.


#%%
## Exercise 10: Class definition

class polygon:
    x = ()
    
    #The constructor
    def __init__(self, components):
        self.x = components  # takes tuple as input
    
    #Get specific elements from tuple
    def getX(self, n): # n is the component index
        return self.x[n]
    
    #Set specific values in the tuple
    def setX(self, n, xi): # n is the component index, and xi is the value
        if n < len(self.x):
            self.x[n] = xi
           
    #Get the perimeter of the polygon
    def perimeter(self):
        return sum(self.x)
    
    #Get the sides of the polygon in order
    def getOrderedSides(self):
        sorted_ = sorted(self.x)
        return sorted_

# End of class definition
# Creating a class instance
a = polygon((5, 0, 1))

print("This is the perimeter of instance a:", a.perimeter())
print("This is the sides of instance a arranged in increasing order:", a.getOrderedSides())

#%%
## Exercise 11: Class inheritance
class rectangle(polygon):
    
    # Modification of the constructor
    def __init__(self, components):
        if len(components) == 4 and sorted(components)[0] == sorted(components)[1] and sorted(components)[2] == sorted(components)[3]:
            self.x = components # a list is expected as input
        else:
            print("Error: number of components is not 4 or the sides of the rectangle are not correctly typed")
    
    #Getting the area of the rectangle
    def area(self):
        return sorted(self.x)[0]*sorted(self.x)[3]

d = rectangle((4,5,4,5))
print("This is the area of the rectangle created by instance d:", d.area())


