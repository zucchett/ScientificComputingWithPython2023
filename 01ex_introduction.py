# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:21:50 2023

@author: andre
"""
# Exercises week 1
# Scientific computing with python(23/24)
# Written by Andrea Sandbu Numme 


# ex01_1
a = ()
for i in range(1,101):
    if (i % 3 == 0 and i % 5 == 0):
        i = 'HelloWorld'
    elif i % 3 == 0:
        i = 'Hello'
    elif i % 5 == 0:
        i = 'World'
    print(i)
    if i == 'Hello':
        i = 'Python'
    elif i == 'World':
        i = 'Works'
    a = a + (i,)

print(a)


# ex01_2
def swap():
    x = input('Give x value: ')
    y = input('Give y value: ')
    x = x + y
    y = x - y
    x = x - y

    print('x = ', x , 'y = ', y)

swap()    
    
# ex01_3

import math

def eq_distance(u,v):
    dist = math.sqrt(((v[0]-u[0])**2)+((v[1]-u[1])**2))
    print('Distance is: ', dist)
    #alternative solution
    print('Distance is: ', math.dist(u,v))

u = (3,0)
v = (0,4)
eq_distance(u,v)

# ex01_4
def count():
    s = input('Input string: ')
    s2 = list(s.lower())
    
    freq = {}
    
    for i in s2:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    print('Each character and number of representation: ', str(freq))
 
count()       

# ex01_5
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

unique2 = []

for i in l:
    if l.count(i) < 2:
        unique2.append(i)
        
count_unique2 = len(unique2)

print('Number of different: ', count_unique2, ', plus all the different listed: ', unique2)
   

# ex01_6

x = input('Write input (int,float,str): ')
y = input('Write another input (int,float,str): ')

try:
    z = float(x) + float(y)
    print('The two inputs added gives: ', z)        
except:
    print('The two inputs ', x, ' and ', y, ' cannot be added')
  
    
# ex01_7

# for loop
b = []
for i in range(11):
    cube = i**3
    b.append(cube)
    
print('Cubed numbers using for loop', b)

# list comprehension 
cubed_numbers = [i**3 for i in range(11)]
print('Cubed numbers using list comprehension: ', cubed_numbers)


# ex01_8

a = [(i,j) for i in range(3) for j in range(4)]
print('Result of ex01_8 is: ', a)


# ex01_9

triples = []

for a in range(1, 100):
    for b in range(a, 100): #a and b will give two triples, with (a,100) we remove one of them
        c = math.sqrt(a**2 + b**2)
        if c.is_integer() and c < 100:
            triples.append((a, b, int(c)))

print('The triples are: ', triples)


# ex01_10

import math
N = (8,4,3)

norm_vect = [i/math.sqrt(sum(i**2 for i in N)) for i in N]
el_sq = [i**2 for i in norm_vect]
print('Squared sum of normalized vector is: ',round(sum(el_sq)))


# ex01_11

f = [0,1]
for n in range(2,20):
    fib = f[n-1]+f[n-2]
    f.append(fib)
    
print('The first 20 numbers of the Fibonacci sequence is: ', f)





















