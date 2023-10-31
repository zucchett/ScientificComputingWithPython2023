import math
import sys
from collections import Counter

# 1. THE HELLO WORLD REPLACEMENT
print('1. The HelloWorld replacement')
result = []
# A
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        result.append("HelloWorld")
    elif i % 3 == 0:
        result.append("Hello")
    elif i % 5 == 0:
        result.append("World")
    else:
        result.append(i)

# B
resultOfTuple = tuple(result)
resultOfTuple = tuple(map(lambda x: str(x).replace("Hello", "Python").replace("World", "Works"), resultOfTuple))
print(resultOfTuple)

# 2. THE SWAP
print('2. The swap')

x = input("Enter the x: ")
y = input("Enter the y: ")

print("Before swapping: x = " + x + " y = " + y)

x, y = y, x

print("After swapping:x = " + x + " y = " + y)

# 3. COMPUTING THE DISTANCE
point1 = (1, 2)
point2 = (4, 6)

distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

print("The distance  is" + str(point1) + " and " + str(point2) + " is " + str(distance))


# 4. COUNTING LETTERS

def count_characters(input_string):
    input_string = input_string.lower()
    character_count = Counter(char for char in input_string if char.isalpha())
    return character_count


s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number " \
     "and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

count_s1 = count_characters(s1)
count_s2 = count_characters(s2)

print("Character num in s1:")
print(count_s1)

print("\nCharacter num in s2:")
print(count_s2)

# 5. ISOLATING THE UNIQUE
listOfNumbers = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
                 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
                 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
                 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
unique_numbers = []

for num in listOfNumbers:
    if listOfNumbers.count(num) == 1:
        unique_numbers.append(num)
print("Unique Numbers:", unique_numbers)
print("Total count of unique numbers:", len(unique_numbers))


# 6. CASTING

def add_variables(num1, num2):
    try:
        casting_result = num1 + num2
        return casting_result
    except (TypeError, ValueError) as e:
        return f"Error: {e}"


# Get two variables as input
num1 = input("Enter Num 1: ")
num2 = input("Enter Num 2: ")

try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    pass

CastingResult = add_variables(num1, num2)
print("Casting Result:", CastingResult)

# 7. CUBES
cubes_a = []
# a) Using a for loop:
for x in range(11):
    cubes_a.append(x ** 3)
    print(cubes_a)
# b) Using a list comprehension:
cubes_b = [x ** 3 for x in range(11)]
print(cubes_b)

# 8. LIST COMPREHENSION
a = [(i, j) for i in range(3) for j in range(4)]
print(a)

# 9. NESTED LIST COMPREHENSION
limit = 100

pythagorean_triples = [(a, b, c) for c in range(1, limit)
                       for b in range(1, c)
                       for a in range(1, b)
                       if a ** 2 + b ** 2 == c ** 2]

unique_triples = set()
for triple in pythagorean_triples:
    a, b, c = sorted(triple)
    unique_triples.add((a, b, c))

pythagorean_triples_tuple = tuple(unique_triples)
print(pythagorean_triples_tuple)


# 10. NORMALIZATION OF AN N-DIMENSIONAL VECTOR
def normalize_vector(vector):
    magnitude = math.sqrt(sum(x ** 2 for x in vector))

    if magnitude == 0:
        return vector

    normalizedVector = tuple(x / magnitude for x in vector)

    return normalizedVector


n_dimensional_vector = (3, 4, 0)
normalized_vector = normalize_vector(n_dimensional_vector)
print("Result", normalized_vector)

# 11. THE FIBONACCI SEQUENCE
fibonacci = [0, 1]

for i in range(2, 20):
    next_fib = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_fib)

print(fibonacci)
print('Done Homework 1')
