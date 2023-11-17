# 1. The HelloWorld replacement
list1 = []
for i in range(0, 100):
    i += 1
    if i % 3 == 0 & i % 5 == 0:
        list1.append("HelloWorld")
    elif i % 3 == 0:
        list1.append("Hello")
    elif i % 5 == 0:
        list1.append("World")
    else:
        list1.append(i)
print(list1)
print(type(list1))
# b
for index in range(len(list1)):
    if list1[index] == "Hello":
        list1[index] = "Python"
    elif list1[index] == "World":
        list1[index] = "Works"
    elif list1[index] == "HelloWorld":
        list1[index] = "PythonWorks"
tup = tuple(list1)
print(tup)
print(type(tup))


# 2. The swap
def switch(x, y):
    x, y = y, x
    return print("x =", x, "y=", y)


print(switch(9.2, 2))


#  3\. **Computing the distance**
import math
def distance(u , v):
    dis = math.sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2)
    return dis
u = (3, 0)
v = (0, 4)


print(distance(u, v))


# 4. Counting letters
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
from collections import Counter
def count_words(str):
    low_str = str.lower()
    c = Counter(low_str)
    print(c)
    return
count_words(s2)
count_words(s1)


#5. Isolating the unique
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

l2 = [2, 3, 2, 4, 5, 7]
def uni_num(list):
    newL = []
    for i in list:
        x = list.count(i)
        if x == 1:
            newL.append(i)
    print(newL)
uni_num(l2)


# 6. Casting
def count_num(a, b):
    try:
        x = a + b
        print(x)
    except:
        print(a, b)
    return

count_num(3, "yyy")



# 7. Cubes
# a) a for loop
cubes = []
for i in range(0, 11):
    cubes.append(i**3)
print("cubes", cubes)

# b) a list comprehension
cubes2 = [i**3 for i in range(0, 11)]
print("cubes2", cubes2)


#8. List comprehension
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)
# List comprehension
newA = [(i, j) for i in range(3) for j in range(4)]
print(newA)



#9. Nested list comprehension
from math import sqrt

pyth = []
for a in range(1, 100):
    for b in range(1, 100):
        c = int(sqrt(a * a + b * b))
        if c * c == a * a + b * b and a < b and a + b > c and b + c > a and a + c > b and c < 100:
            pyth.append((a, b, c))
tup = tuple(pyth)
print(pyth)
print(tup)


#10. Normalization of a N-dimensional vector
def normalizes(var):
    squ = [i / sum(var) for i in var]
    print(squ)
    return squ
demo_tuple = (2, 4.5, 5, 7)
normalizes(demo_tuple)

#11. The Fibonacci sequence
def fib2(n=20):
    i = 0
    a, b = 0, 1
    finona = []
    while i < n:
        i += 1
        finona.append(b)
        a, b = b, a + b
    return finona
print(fib2(20))