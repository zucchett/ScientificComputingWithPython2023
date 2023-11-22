# 01ex_introduction.py

# 1. The HelloWorld replacement
print("1. The HelloWorld replacement \n")

# a)
for i in range(1,101) : 
    if i % 3 == 0 and not i % 5 == 0 : print("Hello")
    elif i % 5 == 0 and not i %3 == 0 : print("World")
    elif i % 3*5 == 0 : print("HelloWorld")
    else : print(i)

# b)
lista = []
for i in range(1,101) : 
    if i % 3 == 0 and not i % 5 == 0 : lista.append("Python") # the replacement is here because it's impossible to replace any element in a tuple
    elif i % 5 == 0 and not i %3 == 0 : lista.append("Works")
    elif i % 3*5 == 0 : lista.append("Python Works")
    else : lista.append(i)
tupla = tuple(lista)
print(tupla)

# 2. The swap
print("\n 2. The swap \n")

x = input("Set the value of x: ") 
y = input("Set the value of y: ") 
x, y = y, x
print("newx =", x, "; newy =", y)

# 3. Computing the distance 
print("\n 3. Computing the distance \n")

x_u = int(input("Set x value of u:"))
y_u = int(input("Set y value of u:"))
x_v = int(input("Set x value of v:"))
y_v = int(input("Set y value of v:"))
u = (x_u, y_u)
v = (x_v, y_v)

print(u, v)

import math
distance = math.sqrt(abs(x_u - x_v)**2 + abs(y_u - y_v)**2)

print("The euclidean distance between u =", u , "and v =", v, " is =", distance)

# 4. Counting letters
print("\n 4. Counting letters \n")

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

from collections import Counter
print("s1 counter ->", Counter(s1.lower()), "s2 counter->", Counter(s2.lower()), sep='\n' )

# 5. Isolating the unique
print("\n 5. Isolating the unique \n")

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

from collections import Counter
d = []
for k, v in Counter(l).items() :
    if v == 1 :  d.append(k)

print(d)

# using only Python data structures

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

lista = [i for i in l if l.count(i) == 1 ]
print(lista)
print(lista == d) # control check

# 6. Casting 
print("\n 6. Casting \n")

var1 = input("insert first variable:")
var2 = input("insert second variable:")

try : 
    sum = int(var1) + int(var2) 
    print(sum, "first")
except:
    try : 
        sum = float(var1) + float(var2) 
        print(sum, "second")
    except:
        sum = var1 + var2
        print(sum, "str")

# 7. Cubes
print("\n 7. Cubes \n")

# a)
for i in range(0,11) : print(i**3) # for loop
# b)
x_cube = [i**3 for i in range(0,11)] # list comprehension
print(x_cube)
    
# 8. List comprehension
print("\n 8. List comprehension \n")

#a = []
#for i in range(3):
#    for j in range(4):
#        a.append((i, j))
#print(a)

a = [(i,j) for i in range(3) for j in range(4)] 
print(a)

# 9. Nested list comprehension 
print("\n 9. Nested list comprehension \n")

pyth = [(a,b,c) for c in range(101) for b in range(c) for a in range(b) if a**2+b**2==c**2]
my_pythagorean_tuple = tuple(pyth)
print(my_pythagorean_tuple)

# 10. Normalization of a N-dimensional vector 
print("\n 10. Normalization of a N-dimensional vector \n")

N_vector = [1,1,0] #testing
sum_squared = 0
from math import sqrt
for i in N_vector : 
    sum_squared += i**2 
N_vector_normalized = [i/sqrt(sum_squared) for i in N_vector]
print(N_vector_normalized)

# or, more easily with a list comprehension
#N_vector = [1,1,0] 
#import math
#N_vector_normalized = [i/sqrt(sum([j**2 for j in N_vector])) for i in N_vector]
#print(N_vector_normalized)

# 11. The Fibonacci sequence
print("\n 11. The Fibonacci sequence \n")

count=0
n1=0
n2=1
while count<20 :
    nth = n1 + n2
    print(n1)
    n1 = n2
    n2 = nth
    count+=1
