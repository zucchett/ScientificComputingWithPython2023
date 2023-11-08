# Esecizio 1
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("HelloWorld")
    elif num % 3 == 0:
        print("Hello")
    elif num % 5 == 0:
        print("World")
    else:
        print(num)

## Exercise 2
import sys

x = sys.argv[1]
y = sys.argv[2]

print("Before swapping: x =", x, "and y =", y)

x, y = y, x

print("After swapping: x =", x, "and y =", y)

## Exercise 3
import math

def calculate_distance(u, v):
    x1, y1 = u
    x2, y2 = v
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

u = (3, 0)
v = (0, 4)

euclidean_distance = calculate_distance(u, v)

print("The Euclidean distance between", u, "and", v, "is:", euclidean_distance)

## Exercise 4
def count_characters(string):
    string = string.lower()
    character_count = {}

    for char in string:
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1

    return character_count

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."

s2 = "The quick brown fox jumps over the lazy dog"

print("Character counts in s1:")
for character, count in count_characters(s1).items():
    print(character, ":", count)

print("Character counts in s2:")
for character, count in count_characters(s2).items():
    print(character, ":", count)

## Exercise 5
from collections import Counter

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
     85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
     1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
     45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

counter = Counter(l)
unique_numbers = [num for num, count in counter.items() if count == 1]

print("Unique numbers in the list:")
for number in unique_numbers:
    print(number)

## Exercise 6
import sys

def perform_addition(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        return None

def parse_input(argument):
    try:
        return int(argument)
    except ValueError:
        try:
            return float(argument)
        except ValueError:
            return argument

a = parse_input(sys.argv[1])
b = parse_input(sys.argv[2])

result = perform_addition(a, b)

if result is not None:
    print("The result of the addition is:", result)
else:
    print("Oops! Addition is not possible with the given input types.")

## Exercise 7 for loop
for x in range(11):
    cube = x ** 3
    cubes.append(cube)

print("List of cubes from 0 to 10:")
print(cubes)

## Exercise 7 list comprehension
cubes = [x ** 3 for x in range(11)]

print("List of cubes from 0 to 10:")
print(cubes)

## Exercise 8
a = [(i, j) for i in range(3) for j in range(4)]
print(a) 

## Exercise 9
triples = [(a, b, c) for a in range(1, 100) for b in range(a, 100) for c in range(b, 100) if (a ** 2 + b ** 2) == c ** 2]
print(triples)

## Exercise 10
def normalize_vector(vector):
    squared_sum = sum(x ** 2 for x in vector)
    normalized = tuple(x / squared_sum ** 0.5 for x in vector)
    return normalized

my_vector = (3, 4, 5)
normalized_vector = normalize_vector(my_vector)
print(normalized_vector)

## Exercise 11
# Initializing variables
num1 = 0
num2 = 1
count = 0

# Printing the first two numbers
print(num1)
print(num2)

# Calculating the rest of the sequence
while count < 18:
    fib = num1 + num2
    print(fib)
    num1 = num2
    num2 = fib
    count += 1
