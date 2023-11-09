##01ex_introduction

#Question 1
result_list = []
print("\n1a\n=============")
for i in range(1,101):
    if (i%3 == 0) and (i%5 == 0):
        print("hello world")
        result_list.append("hello world")
    elif i%3 == 0:
        print("Hello", i)
        result_list.append("Hello")
    elif i%5 == 0:
        print("world", i)
        result_list.append("world")

for i, j in enumerate(result_list):
    if j == "Hello":
        result_list[i] = "Python"
    elif j == "world":
        result_list[i] = "Works"
result_tuple = tuple(result_list)

print("\n\n1b\n============")
print(result_tuple)

#Question 2
#import sys

#if len(sys.argv) != 3:
#    print("Please provide two values to swap.")
#else:
print("\n2\n============")
#x, y = sys.argv[1], sys.argv[2]
x, y = 10, 35
print(f"Before swapping: x = {x}, y = {y}")
    
# Swapping the values without a temporary variable
x, y = y, x
print(f"After swapping: x = {x}, y = {y}")

#Question 3
import math
print("\n3\n============")
point1 = (3, 0)  
point2 = (0, 4)  
total = 0

for i, j in zip(point1, point2):
    total += (i-j)**2
distance = math.sqrt(total)

print(f"The Euclidean distance between {point1} and {point2} is {distance:.2f}")

#Question 4
print("\n4\n============")
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
sentences = (s1, s2)

characters = {}
for sentence in sentences:
    for i in sentence:
        if i not in characters.keys():
            characters[i] = 1
        else:
            characters[i] += 1
    print(f"\nThe number of times each character appears in:\n'{sentence}' is: \n")
    
    for i in characters:
        print(i, characters[i])
    print("\n====================================\n")

#Question 5
print("\n5\n============")
sequence = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

numbers = {}
for i in sequence:
    if i not in numbers.keys():
        numbers[i] = 1
    else:
        numbers[i] += 1

unique_numbers = []
for i in numbers:
    if numbers[i] == 1:
        unique_numbers.append(i)

print(f"The unique numbers are: {unique_numbers}")

#Question 6
#import sys
print("\n6\n============")
#if len(sys.argv) != 3:
#    print("Please provide two variables to add.")
#else:
x = 23
y = 56.43

try:
    try:
        var1 = float(x)
    except:
        var1 = sys.argv[1]
    try:
        var2 = float(y)
    except:
        var2 = sys.argv[2]
                  
    result = var1 + var2
    print(f"Result: {result}")
       
except:
    print(f"Can't add {type(var1)} and {type(var2)}")

#Question 7
##creating cubes using for loop
print("\n7\n============")
x = list(range(0,11))
print("x:", x)
cubes1 = []
for i in x:
    cubes1.append(i**3)
print("Cubes with for loop: ", cubes1)

##using list comprehensions
cubes2 = [i**3 for i in range(0,11)]
print("Cubes with list comprehensions: ", cubes2)

#Question 8
print("\n8\n============")
a = [(i, j) for i in range(3) for j in range(4)]
print(a)

#Question 9
print("\n9\n============")
triplets = set([tuple(sorted((x,y,z))) for z in range(1, 100) for y in range(1, 100) for x in range(1,100) if x**2+y**2==z**2])
triplets = tuple(triplets)
print("The Pythagorean triplets are:")
for i, j in enumerate(triplets):
    print(i+1, j)

#Question 10
import math
print("\n10\n============")

vector = (3, 7, 5) #test vector
squared_sum = sum(x ** 2 for x in vector)

normalization_factor = 1.0 / math.sqrt(squared_sum)
normalized_vector = tuple(x * normalization_factor for x in vector)

print("Original Vector:", vector)
print("Normalized Vector:", normalized_vector)
print("The sum of elements of normalized vector is:", sum(x**2 for x in normalized_vector))

#Question 11
print("\n11\n============")
a, b = 0, 1
print("fibonacci sequence:")
print(a, b, sep='\n')
for i in range(18):
    a, b = b, a+b 
    print(b)
