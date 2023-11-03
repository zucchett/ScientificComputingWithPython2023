#***************************Ex 1.1.1*******************************

# Use range to generate numbers from 1 to 100
hundreds = [x for x in range (1, 101)]
print(hundreds)

#***************************Ex 1.1.2*******************************
# Define the word to replace multiples of 3
replacement_word = "Hello"

# Use a list comprehension to generate numbers from 1 to 100
# Replace multiples of 3 with the replacement word
hundreds = [replacement_word if x % 3 == 0 else x for x in range(1, 101)]

# Print the resulting list
print(hundreds)

#***************************Ex 1.1.3*******************************
#Now I have to replace every three multiple with 'Hello'
#And every five multiple with "World"

# Define the replacement words
words = ["Hello", "World"] 

# Use a list comprehension to generate numbers from 1 to 100
# Replace multiples of 3 and 5 with the corresponding word
hundreds = [words[0] if x % 3 == 0 
            else words[1] if x % 5 == 0
            else x for x in range (1, 101)]

# Print the resulting list
print(hundreds)

#***************************Ex 1.1.4*******************************
#Now I have to replace every three multiple with 'Hello'
#And every five multiple with "World"
#And every three AND five multiple with "Hello World"

hundreds = [words[0] + words[1] if x % 3 == 0 and x % 5 == 0
            else words[0] if x % 3 == 0 
            else words[1] if x % 5 == 0
            else x for x in range (1, 101)]
print(hundreds)

#***************************Ex 1.2*******************************
#Create the tuple
result = tuple(hundreds)

#Considering that a tuple is unchengable

#Replace the two words
result = tuple(str(word).replace("Hello", "Python").replace("World", "Works") for word in hundreds)

#Print the tuple
print(result)

#***************************Ex 2*******************************
# Ask the user to input the values for x and y
x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

# Original values
print("Original values:", x, y)

# Swap the values of x and y
x, y = y, x

# Swapped values
print("Swapped values:", x, y)

#***************************Ex 3*******************************
# Import the math library to use math.sqrt()
import math

# Create the coordinates of two points as tuples
u = tuple([3, 0])
v = tuple([0, 4])

# Calculate the distances on the x and y axes
distance_x = v[0] - u[0]  # Calculate the horizontal distance
distance_y = v[1] - u[1]  # Calculate the vertical distance

# Calculate the distance between the two points using the Pythagorean theorem
distance = math.sqrt(distance_x**2 + distance_y**2)

# Print the result
print("Distance between the two points:", distance)

#***************************Ex 4*******************************
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

#Define a function which counts the occurrences of every char
def count_char_occurrences(input_string, excludes, dict):
    #Iter the string
    for char in input_string:
        #If the char is an actual char 
        if char not in excludes:
            #I don't wanna count separately capital chars from lower chars
            char = char.lower()
            #If the current char is already counted
            if char in dict:
                #Increment the occurrences counter
                dict[char] += 1
            else:
                #Instance a first value
                dict[char] = 1
    #Return the dictionary updated
    return dict

#We have to use a Dictionary{"char", "occurrence"}
char_with_occurrences = {}

#List of the non-char symbols
excludes = [str(0), str(1), " ", "."]

#Call a function which counts the times every char appear
char_occurrences = count_char_occurrences(s1, excludes, char_with_occurrences)
char_occurrences = count_char_occurrences(s2, excludes, char_with_occurrences)

#Print the dictionary
for key, value in char_with_occurrences.items():
    print(f"Chiave: {key}, Valore: {value}")

#***************************Ex 5*******************************
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

# Using a for loop to create a list with unique values
unique_list_for = []
for i in l:
    if i not in unique_list_for:
        unique_list_for.append(i)

# Using a set to create a list with unique values
unique_list_set = list(set(l))

# Print the unique lists and their lengths
print("Using a for loop:", unique_list_for)
print("Using a Set:", unique_list_set)
print("Number of unique values using a for loop: ", len(unique_list_for))
print("Number of unique values using a Set: ", len(unique_list_set))

#***************************Ex 6*******************************
x = input("Inserisci il valore di x (accettati int, float o stringhe): ")
y = input("Inserisci il valore di y (accettati int, float o stringhe): ")

print(x)
print(y)

try:
    # Prova a convertire x e y in int
    print(int(x) + int(y))
except ValueError:
    try:
        print(float(x) + float(y))
    except ValueError:
        if isinstance(x, str) and isinstance(y, str):
            print(x + y)
        else: print("Incompatible types")

#***************************Ex 7*******************************
# Declare a list and fill it using a for loop
list_loop = []
for x in range(10):
    # Add the cube of x to the list
    list_loop.append(x**3)

# Print the list filled with the for loop
print("Using a for loop:", list_loop)

# Declare and define a list comprehension
list_comprehension = [x**3 for x in range(10)]

# Print the list filled with a list comprehension
print("Using a list comprehension:", list_comprehension)

#***************************Ex 8*******************************
import random

result = 101

# Keep generating random values for a and b until c^2 is less than 100
while result >= 100:
    a = random.randint(0, 10)
    b = random.randint(1, 10)
    result = a**2 + b**2

# Print the values of a^2, b^2, and c^2
print("a^2 = ", a, "\nb^2 = ", b, "\nc^2 = ", result)

#***************************Ex 9*******************************
# Imports
import math
import random

# Generate a random length for the vector (1 to 10)
length = random.randint(1, 10)

# Define the N-vector with random integers
vector = tuple([random.randint(0, 100) for x in range(length)])

# Print the generated vector
print("Original vector:", vector)

# Calculate the sum of squares of vector elements
sum_of_squares = 0
for x in range(length):
    sum_of_squares += (vector[x]**2)

# Calculate the norm of the vector
norm = math.sqrt(sum_of_squares)

# Normalize the vector
normalized_vector = tuple(x / norm for x in vector)

# Print the normalized vector
print("Normalized vector:", normalized_vector)

#***************************Ex 10*******************************

# Initialize variables for the Fibonacci sequence
current_number = 0
prev_number = 0

# Create a list to store the Fibonacci sequence, starting with 0
fibonacci = [current_number]

# Generate the Fibonacci sequence for the first 20 numbers
for i in range(20):
    # Calculate the next number in the sequence
    next_number = int(prev_number) + int(current_number)

    # Update the variables for the next iteration
    prev_number = current_number
    current_number = next_number

    # Ensure that prev_number is not 0 for the next iteration
    if (prev_number == 0):
        prev_number = 1

    # Add the next_number to the Fibonacci sequence
    fibonacci.append(next_number)

# Print the generated Fibonacci sequence
print("Fibonacci sequence:", fibonacci)