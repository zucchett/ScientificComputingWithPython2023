# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:40:08 2023

@author: andre
"""


# Exercises week 2
# Scientific computing with python(23/24)
# Written by Andrea Sandbu Numme 

# 01 Global Variables 

def f(alist):
    x = 5 #changed to a local variable
    alist = alist.copy() #doesn't change the input variable 
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print('The output from the called function: ',ans)
print('The original input, after the function is called: ',alist) # alist has been changed
    

#02 
ans2 = [i*i for i in range(10) if i % 2 == 1]

print('Output from task 2: ', ans2)

# 03
def ex3(lis, n): 
    lis2 = []
    for i in filter(lambda x: len(x) < n, lis): 
        lis2.append(i)
    print('Words shorter than length:', n, ' is: ', lis2)
    return(lis2)


lis = ["abc", "defgh", "ijklmno", "pqr", "stuvwxyz"]
n = 6
ex3(lis, n)

# 04
def key_length(lang):
    keys = list(map(len, lang.keys()))
    print('The length of the keys are: ', keys)


lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
key_length(lang)



# 05

def alph_sort(language_scores):
    language_scores.sort(key = lambda x: x[0])
    print('Sorted list: ', language_scores)

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
alph_sort(language_scores)

# 06

def square(x):
    return x * x

def cube(x):
    return x * x * x 

def sixth(x):
    return cube(x) * cube(x)

x = 3
print('Input value:', x)
print('Squared input value:', square(x))
print('Cubed input value:', cube(x))
print('Input value to the 6th power:', sixth(x))


# 07

def hello(func):
    def wrapper(x):
        print("Hello World!")
        func(x)
        print("Hello World")
    return wrapper

@hello
def square(x):
    print(x*x)

x = 5
square(x)


#  08

def fib2(x):
    def fib_rec(y):
        if y <= 1:
            return y
        else:
            return fib_rec(y-1) + fib_rec(y-2)       
    
    f2 = []
    
    for i in range(x):
        f2.append(fib_rec(i))
    return f2 

seq = fib2(20)
print('First 20 of the Fibonacci sequence:', seq)


# 09
#code from 01ex_introduction.py
def fib1(x):
    f = [0,1]
    for n in range(2,x):
        fib = f[n-1]+f[n-2]
        f.append(fib)
    return f

print('Fibonacci sequence (first 20 numbers)', fib1(20))


#Import timeit function
import timeit

#time recursive function
timed_rec = timeit.timeit("fib2(20)", globals=globals(), number=1000)
print('Time for recursive function in exercise 2:', timed_rec, 's')

#time function from ex01 
timed_for = timeit.timeit("fib1(20)", globals=globals(), number=1000)
print('Time for function in exercise 1:', timed_for,'s')

"""
The recursive function for calculating the fibonacci sequencce, 
takes approximately 7s longer to run. 
"""

# 10

class Poly():
    
    def __init__(self,sides):
        if len(sides) < 3:
            raise ValueError("It's less than three sides")
        self.sides = list(sides)
        
    def getlength(self, i):
        return self.sides[i]
    
    def setlength(self, i, length):
        self.sides[i] = length
        
    def perimeter(self):
        return sum(self.sides)

    def GetOrderedSides(self, increasing=True):
        sorted_sides = sorted(self.sides) if increasing else sorted(self.sides, reverse=True )
        return tuple(sorted_sides)
    
polygon = Poly((5,2,7,8))
print('Perimeter', Poly.perimeter(polygon))
print('Increasing', polygon.GetOrderedSides(increasing=True))
print('Decreasing', polygon.GetOrderedSides(increasing=False))


# 11

class rect(Poly):
    def __init__(self,sides):
        super().__init__(sides) #super calls for the Poly class
        new_sides = sorted(self.sides)
        if len(sides) != 4:
            raise ValueError("A rectangle has 4 sides")
        elif new_sides[0] != new_sides[1] or new_sides[2] != new_sides[3]:
            raise ValueError("Two and two sides should be equal")
        self.sides = list(sides)   
    
    def area(self):
        sorted_sides = sorted(self.sides)
        area_rect = sorted_sides[0]*sorted_sides[2]
        return area_rect
            
rectangle = rect((3, 5, 3, 5))
print('Area of rectangle', rectangle.area())
          
       
            