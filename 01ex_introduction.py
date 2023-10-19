#1)HelloWorld Replacement program

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

#2)The Swap

# Input values from the command line
x = input("Enter the value for x: ")
y = input("Enter the value for y: ")

# Print the original values
print(f"Original values: x = {x}, y = {y}")

# Swap the values without a temporary variable
x, y = y, x

# Print the swapped values
print(f"Swapped values: x = {x}, y = {y}")

#3)Computing the distance

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


#4)Counting letters

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


#5)Isolating the unique
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

#6)
import sys

def add_variables(var1, var2):
    try:
        result = var1 + var2
        print(f"Result: {result}")
    except TypeError:
        print("Cannot perform addition. Make sure the inputs are int or float.")

if len(sys.argv) != 3:
    print("Usage: python program.py <var1> <var2>")
    sys.exit(1)

var1 = sys.argv[1]
var2 = sys.argv[2]

try:
    var1 = int(var1) if var1.isdigit() else float(var1)
    var2 = int(var2) if var2.isdigit() else float(var2)
except ValueError:
    pass

add_variables(var1, var2)
