#1)HelloWorld Replacement program
print("Program 1 begins")
result_list=[]
for number in range(1,101):
	if number%3==0 and number%5==0:
	  result_list.append("HelloWorld")
	elif number%3==0:
	  result_list.append("Hello")
	elif number%5==0:
	  result_list.append("World")
	else:
	  result_list.append(str(number))

#converting the list to a tuple
result_tuple=tuple(result_list)

#substitute "Hello" with "Python" and "World" with "Works" in the tuple
result_tuple=tuple(item.replace("Hello","Python").replace("World","Works") for item in result_tuple)

#print the final tuple
print(result_tuple)

print("Program 1 ends\n")

#2)The Swap
print("Program 2 begins")
# Input values from the command line
x = input("Enter the value for x: ")
y = input("Enter the value for y: ")

# Print the original values
print(f"Original values: x = {x}, y = {y}")

# Swap the values without a temporary variable
x, y = y, x

# Print the swapped values
print(f"Swapped values: x = {x}, y = {y}")

print("Program 2 ends\n")
#3)Computing the distance
print("Program 3 begins")
#point1 = (2, 3)
#point2 = (4, 5)

# Extract the coordinates from the tuples
#x1, y1 = point1
#x2, y2 = point2
import math  # Import the math library for sqrt function

# Get the coordinates of the first point from the user
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))

# Get the coordinates of the second point from the user
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

# Calculate the Euclidean distance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Print the result
print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")

print("Program 3 ends\n")
#4)Counting letters
print("Program 4 begins")
# Define the input strings
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."

s2 = "The quick brown fox jumps over the lazy dog"

# Create a dictionary to store character counts (case-insensitive)
char_count = {}

# Function to add characters to the dictionary
def add_char_count(char, char_count):
    char_count[char] = char_count.get(char, 0) + 1

# Count characters in s1 (case-insensitive)
for char in s1:
    add_char_count(char.lower(), char_count)

# Count characters in s2 (case-insensitive)
for char in s2:
    add_char_count(char.lower(), char_count)

# Print the character counts
for char, count in char_count.items():
    print(f"'{char}' occurs {count} time(s) in the input strings.")

print("Program 4 ends\n")
#5)Isolating the unique
print("Program 5 begins")
# Define the list
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
     85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
     1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
     45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

# Create a set for unique numbers
unique_numbers = set()

# Create a set for duplicate numbers
duplicate_numbers = set()

# Loop through the list and determine unique and duplicate numbers
for number in l:
    if number in unique_numbers:
        unique_numbers.remove(number)
        duplicate_numbers.add(number)
    elif number not in duplicate_numbers:
        unique_numbers.add(number)

# Count and print the number of unique numbers
count_of_unique_numbers = len(unique_numbers)
print(f"Unique numbers: {count_of_unique_numbers}")
print("Program 5 ends\n")
#6) casting
print("Program 6 begins")
import sys


def add_variables(var1, var2):
    try:
        result = var1 + var2
        return result
    except (TypeError, ValueError):
        return None


if __name__ == "__main__":
    var1 = input("Enter the first variable: ")
    var2 = input("Enter the second variable: ")

    try:
        var1 = float(var1)
    except ValueError:
        pass

    try:
        var2 = float(var2)
    except ValueError:
        pass

    result = add_variables(var1, var2)

    if result is not None:
        print("Result:", result)
    else:
        print("Error: Unable to perform addition with the given input variables.")
print("Program 6 ends\n")
#7)Cubes
print("Program 7 begins")
#a) Using a for loop
cubes = []
for x in range(11):
    cubes.append(x**3)
print("Using a for loop:",cubes)
#b) Using a list comprehension:
cubes = [x**3 for x in range(11)]
print("Using a list comprehension:",cubes)
print("Program 7 ends\n")
#8)List Comprehension
print("Program 8 begins")
a = [(i, j) for i in range(3) for j in range(4)]
print(a)
print("Program 8 ends\n")
#9)Nested list comprehension
print("Program 9 begins")
triples = [(a, b, c) for c in range(1, 101) for b in range(1, c) for a in range(1, b) if a**2 + b**2 == c**2]
unique_triples = list(set(triples))

# Filter out Pythagorean triples with a, b, and c that have a greatest common divisor (gcd) greater than 1
filtered_triples = [(a, b, c) for a, b, c in unique_triples if a % 3 != 0 or b % 4 != 0 or c % 5 != 0]

# Print the unique Pythagorean triples
for triple in filtered_triples:
    print(triple)
print("Program 9 ends\n")
#10)Normalization of a N-dimensional vector
print("Program 10 begins")
import math

def normalize_vector(vector):
    # Calculate the L2 norm (Euclidean norm) of the vector
    norm = math.sqrt(sum(x**2 for x in vector))

    # Check for a zero vector to avoid division by zero
    if norm == 0:
        return tuple(0 for x in vector)

    # Normalize the vector by dividing each component by the norm
    normalized_vector = tuple(x / norm for x in vector)

    return normalized_vector

# Example usage
input_vector = (3, 4)  # A 2-dimensional vector
normalized_vector = normalize_vector(input_vector)
print("Original vector:", input_vector)
print("Normalized vector:", normalized_vector)
print("L2 Norm of the normalized vector:", math.sqrt(sum(x**2 for x in normalized_vector)))
print("Program 10 ends\n")
#11)The Fibonacci sequence
print("Program 11 begins")
# Initialize the first two Fibonacci numbers
fibonacci_sequence = [0, 1]

# Calculate the next 18 Fibonacci numbers using a for loop
for i in range(2, 20):
    next_fibonacci = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
    fibonacci_sequence.append(next_fibonacci)

# Print the first 20 Fibonacci numbers
print(fibonacci_sequence)
print("Program 11 ends\n")






