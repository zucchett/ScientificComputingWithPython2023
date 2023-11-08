#%% 1. The HelloWorld replacement

results = []

for n in range(1, 101):
    # a)
    if n%3 == 0 and n%5 == 0:
        result = "HelloWorld"
    elif n%5 == 0:
        result = "World"
    elif n%3 == 0:
        result = "Hello"
    else:
        result = n
    print(result)
    
    # b)
    if result == "Hello":
        result = "Python"
    elif result == "World":
        result = "Works"
    results.append(result)
results = tuple(results)

print(results)

#%% 2. The swap

x = input("Enter x value: ")
y = input("Enter y value: ")
print(f"Before: x = {x}, y = {y}")
x, y = y, x
print(f"After: x = {x}, y = {y}")

#%% 3. Computing the distance

from math import *

def euclidean_distance(u, v):
    return sqrt((u[0]-v[0])**2 + (u[1]-v[1])**2)

print(f"Euclidean distance: {euclidean_distance((3,0), (0,4))}")

#%% 4. Counting letters

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

def count_letters(s):
    letters_set = set(s.lower())
    letters_dict = {}
    for letter in letters_set: 
        letters_dict[letter] = s.count(letter)
    return letters_dict

print(f"Letters and their number of occurrences in s1: {count_letters(s1)}")
print(f"Letters and their number of occurrences in s2: {count_letters(s2)}")

#%% 5. Isolating the unique

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

def unique_numbers_1(l):
    unique_numbers_set = set()
    for number in set(l):
        if l.count(number) == 1:
            unique_numbers_set.add(number)
    return unique_numbers_set, len(unique_numbers_set)

print(unique_numbers_1(l))

def unique_numbers_2(l):
    unique_numbers_dict = {}
    for number in l:
        if number not in unique_numbers_dict:
            unique_numbers_dict[number] = 1
        else:
            unique_numbers_dict[number] += 1
    unique_numbers_set = set(num for num in l if l.count(num) == 1)
    return unique_numbers_set, len(unique_numbers_set)

print(unique_numbers_2(l))

#%% 6. Casting

def addition(a, b):
    print(f"Addiction of {a} and {b}: ", end='')
    try:
        print(f"{a} + {b} = {a+b}")
    except TypeError as exp:
        print(f"TypeError: {exp}")

a = 1
b = 1.0
c = "Python"

addition(a, b)
addition(b, c)
addition(c, a)

#%% 7. Cubes

# a)
cube_for = []
for x in range(11):
    cube_for.append(x**3)
print(cube_for)

# b)
cube_list = [x**3 for x in range(11)]
print(cube_list)

#%% 8. List comprehension

a = [(i, j) for i in range(3) for j in range(4)]
print(a)

#%% 9. Nested list comprehension

pythagorean_triples = []

for a in range(1, 100):
    for b in range(a, 100):
        c_squared = a**2 + b**2
        c = int(sqrt(c_squared))
        
        if c_squared == c**2 and c < 100:
            pythagorean_triples.append((a, b, c))

print(pythagorean_triples)

#%% 10. Normalization of a N-dimensional vector

vector = (10, 9, 12)
N = len(vector)

squared_sum = sum(x**2 for x in vector)

if squared_sum == 0:
    print(f"Normalized vector: {tuple(N * [0])}")
else:
    print(f"Normalized vector: {tuple(x/sqrt(squared_sum) for x in vector)}")

#%% 11. The Fibonacci sequence

f_list = []

for n in range(20):
    if n == 0:
        f_list.append(0)
    elif n == 1:
        f_list.append(1)
    else:
        f_list.append(f_list[n-1]+f_list[n-2])

print(f_list)
