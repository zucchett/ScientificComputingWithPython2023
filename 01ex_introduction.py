#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:50:49 2023

@author: annamatzen
"""

import math

## Exercise 1: The HelloWorld replacement
# a and b
t = ()

for i in range(0,100):
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        i = "HelloWorld"
    elif i % 3 == 0:
        i = "Hello"
    elif i % 5 == 0:
        i = "World"
    print(i)
    if i == "Hello":
        i = "Python"
    elif i == "World":
        i = "Works" 
    t = t + (i,)

print(t)


###
## Exercise 2: The swap
def swap(x,y):
    print("x =", y)
    print("y =", x)

    
x1 = input("Set the value of x: ")
y1 = input("Set the value of y: ")

swap(x1,y1)

###
## Exercise 3: Computing the distance
u = ()
u1 = float(input("Set the first element of the first point: "))
u2 = float(input("Set the second element of the first point: "))
u = u + (u1,u2)

v = ()
v1 = float(input("Set the first element of the second point: "))
v2 = float(input("Set the second element of the second point: "))
v = v + (v1,v2)

eucldist = math.sqrt((u1-v1)**2+(u2-v2)**2)
print("The euclidean distance for the two points is ",eucldist)


###
## Exercise 4: Counting letters    
def counting_letters(string):
    string = string.lower()
    counts = {}

    for i in string:
        counts[i] = counts.get(i, 0) + 1
    
    for i, j in counts.items():
        print(f"'{i}': {j}")
        

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

print("Test string s1:")
counting_letters(s1)
print()
print("Test string s2:")
counting_letters(s2)

###
## Exercise 5: Isolate the unique

def isolate_unique(l):
    #seen = set()
    l.sort()
    uniques = []
    dupes = []

    for x in l:
        if x in uniques:
            dupes.append(x)
        else:
            uniques.append(x)
    
    for k in uniques:
        if k in dupes:
            uniques.remove(k)
    
    for o in uniques:
        if o in dupes:
            uniques.remove(o)
    print("Unique numbers:", uniques)
    print("Number of uniques:", len(uniques))
    

ll = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

isolate_unique(ll)

###
## Exercise 6: Casting

def casting(var1, var2):
    try:
        result = float(var1) + float(var2)
        print(result)
    except:
        print("You can't add a string with another string or number, try two integers or floats.")

vare1 = input("First variable: ")
vare2 = input("Second variable: ")

casting(vare1,vare2)

###
## Exercise 7: Cubes
# a - Foor loop
cubes1 = []
for i in range(11):
    cubes1.append(i**3)
print(cubes1)


# b - List comprehension
cubes2 = [x**3 for x in range(11)]
print(cubes2)

###
## Exercise 8: List comprehension

b = [(x, y) for x in range(3) for y in range(4)]
print(b)

###
## Exercise 9: Nested list comprehension

pythagorean = tuple((a, b, c) for a in range(1,100) for b in range(a,100) for c in range(1,100) if a**2 + b**2 == c**2)
print(pythagorean)

###
## Exercise 10: Normalization of an N-dimensional vector

def normvector(l):
    sums = sum(i**2 for i in l)
    sqrt_sum = math.sqrt(sums)
    normalized = [i/sqrt_sum for i in l]
    normalized_vector = [i**2 for i in normalized]
    
    print(round(sum(normalized_vector)))

ll = (90,7,32)

normvector(ll)

###
## Exercise 11: Fibonacci sequence
def loop_fibo(n):
    fibonacci_start = [0,1]
    for i in range(2,n):
        fib_next = fibonacci_start[i-1]+fibonacci_start[i-2]
        fibonacci_start.append(fib_next)
    print("The first 20 elements of the Fibonacci sequence are:", fibonacci_start)

loop_fibo(20)
    
        






