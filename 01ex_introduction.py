#1. The HelloWorld replacement
output = []  # Create an empty list to store the output

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        output.append("helloworld")
    elif x % 3 == 0:
        output.append("hello")
    elif x % 5 == 0:
        output.append("world")
    else:
        output.append(x)
# Convert the list to a tuple
output_tuple = tuple(output)

# Perform the substitutions in the tuple
output_tuple = tuple(["Python" if x == "hello" else "Works" if x == "world" else x for x in output_tuple])

# Print the modified tuple
for output in output_tuple:
    print(output, end=', ')


#2. Write a program that swaps the values of two input variables
x = input("enter the value of x: ")
y = input ("enter the value of y: ")
#swapp the values
x, y = y, x
# Print the swapped values
print("Swapped values: x =", x, "y =", y)


#3. Write a program that calculates and prints the euclidean distance
import math

# u coordinates x1 and y1
x1 = float (input ("Enter the value of x1: "))
y1 = float (input("Enter the value of y1: "))
# v coordinates x2 and y2
x2 = float(input("Enter the value of x2: "))
y2 = float (input("Enter the value of y2: "))


# Calculate the squared differences in coordinates
dx = x2 - x1
dy = y2 - y1

# Calculate the squared Euclidean distance
squared_distance = dx ** 2 + dy ** 2

# Calculate the Euclidean distance by taking the square root
distance = math.sqrt(squared_distance)

# Print the result
print("The Euclidean distance between" , distance)

#4. Write a program that calculates the number of times each character occurs in a given string.
#Ignore differences in capitalization

input_string = "But for multiples of three print Hello instead of the number and for the multiples of five print World"

# Convert the string to lowercase to ignore case differences
input_string = input_string.lower()

# Create an empty dictionary to store character counts
char_count = {}


for char in input_string:
    # Check if the character is a letter
    if char.isalpha():
        # If the character is in the dictionary, increment its count, otherwise initialize it with 1
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

# Print the character counts
for char, count in char_count.items():
    print(f"'{char}': {count} times

#5. Write a program that determines and counts the unique numbers (numbers with only one occurrence) in the list:
i_list =[36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
#create empty dictionary for storing count values
unique_numbers = {}
for number in i_list:
    unique_numbers[number] = unique_numbers.get(number, 0) + 1

for number, count in unique_numbers.items():
    if count == 1:
        print(number, end=', ')

#6. Write a program that reads from command line two variables, that can be either int, float, or str

var1 = input("Enter the first variable: ")
var2 = input("Enter the second variable: ")

try:
    var1 = int(var1)
except ValueError:
    try:
        var1 = float(var1)
    except ValueError:
        # If it's not a float, it must be a string
        var1 = var1

try:
    var2 = int(var2)
except ValueError:
    try:
        var2 = float(var2)
    except ValueError:
        # If it's not a float, it must be a string
        var2 = var2

addition = var2 + var1
print("Addition:", addition)

#7. Create a list of the cubes of x for x in [0, 10] using
cubes_numbers = [x**3 for x in range(11)]
print(cubes_numbers)

#8. Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.
a = [(i, j) for i in range(3) for j in range(4)]
print(a)

# 9.Using a list comprehension to generate unique Pythagorean triples
pythagorean_triples = [(a, b, int((a**2 + b**2)**0.5)) 
                       for a in range(1, 100)
                       for b in range(a, 100) 
                
                       if ((a**2 + b**2)**0.5).is_integer() and (a**2 + b**2)**0.5 < 100]

# Sort the list for readability
pythagorean_triples.sort()

# Convert to a tuple
unique_triples_tuple = tuple(pythagorean_triples)

# Print the unique Pythagorean triples
for triple in unique_triples_tuple:
    print(triple)
#10. Write a program that takes an N-dimensional vector,e.g. a variable-length tuple of numbers, 
#and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1)

import math

# Input: N-dimensional vector as a variable-length tuple
input_vector = (3, 4, 5)

# Calculate the squared sum of entries
squared_sum = sum(x ** 2 for x in input_vector)

# Check if the squared sum is already 0
if squared_sum == 0:
    normalized_vector = input_vector  # Already normalized or all entries are 0
else:
    # Calculate the magnitude
    magnitude = math.sqrt(squared_sum)

    # Normalize the vector by dividing each component by the magnitude
    normalized_vector = tuple(x / magnitude for x in input_vector)

# Print the input vector and the normalized vector
print("Input Vector:", input_vector)
print("Normalized Vector:", normalized_vector)

#11. Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops
fib_sequence = [0, 1]
for x in range(2, 20):
    next_number = fib_sequence[x - 1] + fib_sequence[x - 2]
    fib_sequence.append(next_number)

# Print the result
print(fib_sequence)
