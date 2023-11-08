#---------------------------------------------------------------------------------------------------------------
# exercise 1 part one.The HelloWorld replacement


# Creating an empty list to store the results.
output = []

# Set i to start from 1
i = 1

# Continue the loop as long as i is less than or equal to 100
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        output.append("HelloWorld")
    elif i % 3 == 0:
        output.append("Hello")
    elif i % 5 == 0:
        output.append("World")
    else:
        output.append(i)

    i += 1  # Increment i by 1 in each iteration

# Create a new list for the modified elements
new_output = []

# Iterate through the elements in the original list and perform replacements
for value in output:
    if value == "Hello":
        new_output.append("Python")
    elif value == "World":
        new_output.append("Works")
    else:
        new_output.append(value)

# Convert the new list to a tuple
result = tuple(new_output)

# Print the resulting tuple
print(result)

#---------------------------------------------------------------------------------------------------------------
#exercise 1 part two.The swap


# Get input values from the user
x = input("\nEnter x: ")
y = input("Enter y: ")

# Print the values
print("value of x is ->", x)
print("value of y is ->", y)

# Swap the values without a temporary variable
x, y = y, x

# Print the swapped values
print("\nSwapped values:")
print("value of x is ->", x)
print("value of y is ->", y)

#---------------------------------------------------------------------------------------------------------------
# exercise 1 part three.Computing the distance


import math

# Define the points
u = (3, 0)
v = (0, 4)

# Extract the u and v coordinates of both points
u1, v1 = u
u2, v2 = v

# Calculate the distance
du = u1 - u2
dv = v1 - v2
distance = math.sqrt(pow(du, 2) + pow(dv, 2))

# Show the result
print("Distance between point u and v is :", distance)

#---------------------------------------------------------------------------------------------------------------
#exercise 1 part four.Counting letters


# Create dictionaries to store character counts for each string
count_s1 = {}
count_s2 = {}

# Define the test strings
s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

# Convert the strings to lowercase
s1 = s1.lower()
s2 = s2.lower()

# Initialize an index variable to start at the beginning of the string
i = 0

# Create a while loop that continues as long as the index is less than the length of the string (s1)
while i < len(s1):
    # Get the character at the current index
    char = s1[i]
    # Check if the character is an alphabet letter (a-z)
    if char.isalpha():
        # If the character is already in the count_s1 dictionary, increment its count
        if char in count_s1:
            count_s1[char] += 1
        # If the character is not in the count_s1 dictionary, add it with a count of 1
        else:
            count_s1[char] = 1

    # increace the index by 1 to move to the next character in the string
    i += 1

i = 0
while i < len(s2):
    char = s2[i]
    if char.isalpha():
        if char in count_s2:
            count_s2[char] += 1
        else:
            count_s2[char] = 1
    i += 1

# Print character counts for s1
print("Character counts for s1:")

# Initialize an index variable to start at the beginning of s1
i = 0

# Use a while loop to iterate through the characters in s1
while i < len(s1):
    # Get the character with the index
    char = s1[i]
    # Check if the character is an alphabet letter (a-z)
    if char.isalpha():
        # Count the character in s1
        count = s1.count(char)
        # Print the character and its count
        print(f"{char}: {count}")
        # Remove all the character in the string to avoid double-counting
        s1 = s1.replace(char, '')
    # increase the index to move to the next character in the string
    i += 1

# Print character counts for s2
print("\nCharacter counts for s2:")

# Reset the index variable to start at the beginning of s2
i = 0

while i < len(s2):
    char = s2[i]
    if char.isalpha():
        count = s2.count(char)
        print(f"{char}: {count}")
        s2 = s2.replace(char, '')

    i += 1

# ---------------------------------------------------------------------------------------------------------------
# exercise 1 part five.Isolating the unique


# Define the list of L
L = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
           85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
           1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
           45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

# Create an empty dictionary to store counts of each number
L_counts = {}

# set an index variable to start at the beginning of the 'L' list
i = 0

# Create a while loop that continues as long as the index is less than the length of the list
while i < len(L):
    # Get the number at the current index
    num = L[i]
    # Check if the number is already in the 'L_counts' dictionary
    if num in L_counts:
        # If it's already in the dictionary, increase its count
        L_counts[num] += 1
    else:
        # If it's not in the dictionary, add it with a count of 1
        L_counts[num] = 1
    # increase the index to move to the next number in the list
    i += 1

# Create a set to store unique numbers
unique_L = set()

# set an index variable to start at the beginning of the 'L_counts' dictionary
i = 0

# Get the keys and values from the 'L_counts' dictionary
L = list(L_counts.keys())
counts = list(L_counts.values())

# this loop continues as long as the index is less than the length of the dictionary
while i < len(L_counts):
    num = L[i]
    count = counts[i]
    # Check if the number appears only once
    if count == 1:
        unique_L.add(num)
    # increase the index to move to the next in the dictionary
    i += 1

# Count how many unique numbers we found
unique_count = len(unique_L)

# Show the unique numbers and their count
print("\nUnique numbers:\n", unique_L)
print("Count of unique numbers:", unique_count)

# ---------------------------------------------------------------------------------------------------------------
# exercise 1 part six.Casting


# Read the two variables from user input
variable1 = input("Enter the first variable: ")
variable2 = input("Enter the second variable: ")

try:
    result = int(variable1) + int(variable2)
    print("Result of addition:", result)

except ValueError:
    try:
        result = float(variable1) + float(variable2)
        print("Result of addition (float):", result)
    except ValueError:
        result = str(variable1) + str(variable2)
        print("Result of concatenation (str):", result)

# ---------------------------------------------------------------------------------------------------------------
#exercise 1 part seven.Cubes


# Create an empty list to store the cubes
cubes = []

# Start with the first number, 0
x = 0

# a) Using a for loop:
for x in range(11):  # Loop in the range [0, 10] (11 to include 10)
    cubes.append(pow(x,3))  # Calculate the cube of each value (x) and add it to the list
print("\nA) the list of cubes calculated with for: ",cubes)

# b) Using a list comprehension:
list_comprehension = []
for x in range(11):
    list_comprehension.append(pow(x, 3))
print("\nB) the list comprehension: ", list_comprehension)

# ---------------------------------------------------------------------------------------------------------------
# exercise 1 part eight.List comprehension


# Create an empty list to store the pairs
a = []

# Initialize 'i' to 0
i = 0

# Write, using the list comprehension, a single-line expression
a = [(i, j) for i in range(3) for j in range(4)]

# Print the list of pairs
print("\nList of pairs: ",a)

# ---------------------------------------------------------------------------------------------------------------
#exercise 1 part nine.Nested list comprehension


# Create an empty list to store the Pythagorean triples
triples = []

# check if 'c' value from 1 to 99
for c in range(1, 100):
    # check 'b' values from 1 to 'c-1'
    for b in range(1, c):
        # check 'a' values from 1 to 'b-1'
        for a in range(1, b):
            # Check if 'a^2 + b^2 = c^2'
            if pow(a,2) + pow(b,2) == pow(c,2):
                # If true, it's a Pythagorean triple, so add it to the list
                triples.append((a, b, c))

# Create a tuple by removing unnecessary triples.
unique_triples = tuple(set(triples))

# Print the unique Pythagorean triples
print("\nUnique Pythagorean triples (a, b, c) where c < 100:")
for triple in unique_triples:
    print(triple)

# ---------------------------------------------------------------------------------------------------------------
# exercise 1 part ten.Normalization of a N-dimensional vector


import math

vector = []

# Input the number of dimensions (N)
N = int(input("Enter the number of dimensions: "))

# Input the values for each dimension as integers
for i in range(N):
    dimension = float(input("Enter dimension value: "))
    vector.append(dimension)

print("You choosed",{N},"dimensions")
print("Entered N-dimensional vector:", vector)

# Calculate the magnitude of the vector
magnitude = math.sqrt(sum(pow(x,2) for x in vector))

# Normalize the vector by dividing each element by the magnitude
normalized_vector = [x / magnitude for x in vector]

# Print the normalized vectors
print("Normalized Vector:", normalized_vector)

# ---------------------------------------------------------------------------------------------------------------
# exercise 1 part eleven.The Fibonacci sequence


# First two Fibonacci numbers
a = 0
b = 1

count = 0

while count < 20:
    print(a)  # Print the current Fibonacci number
    next_number = a + b
    a = b
    b = next_number
    count += 1

# ---------------------------------------------------------------------------------------------------------------
