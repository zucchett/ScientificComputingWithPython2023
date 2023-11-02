## Q1

result = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        result.append("HelloWorld")
    elif i % 3 == 0:
        result.append("Hello")
    elif i % 5 == 0:
        result.append("World")
    else:
        result.append(str(i))

result = tuple(result)
result = tuple(map(lambda x: x.replace("Hello", "Python").replace("World", "Works"), result))
print(result)

#########

## Q2

x = input("Enter the value of x: ")
y = input("Enter the value of y: ")
print("Original values: x =", x, "y =", y)
x, y = y, x
print("Swapped values: x =", x, "y =", y)

##########

## Q3

import math
def euclidean_distance(u, v):
    # Unpack the coordinates of u and v
    x1, y1 = u
    x2, y2 = v
    x_diff = (x1 - x2) ** 2
    y_diff = (y1 - y2) ** 2
    distance = math.sqrt(x_diff + y_diff)
    return distance
u = (3, 0)
v = (0, 4)
distance = euclidean_distance(u, v)
print(f"The Euclidean distance between {u} and {v} is {distance}")

#########

## Q4

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
alphabet = "abcdefghijklmnopqrstuvwxyz"
#letter_count = {letter: 0 for letter in alphabet}
letter_count = dict.fromkeys(list(alphabet),0)
for i in s1:
        for j in alphabet:
            if j == i.lower():
                letter_count[j]+=1         
print(letter_count)
for i in s2:
        for j in alphabet:
            if j == i.lower():
                letter_count[j]+=1           
print(letter_count)


##########

## Q5

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
l.sort()
print(l)
unique_numbers = [x for x in l if l.count(x) == 1]
unique_count = len(unique_numbers)
print("Unique (occurring only once) numbers : ", unique_numbers)
print("Total number of unique numbers : ", unique_count)
repeated_count = len(set(l)) - unique_count
print(f"Total of {repeated_count} numbers are repeated multiple times in the list.")



#######

## Q6

input1 = input("Enter the first variable: ")
input2 = input("Enter the second variable: ")
try:
    result = float(input1) + float(input2)
    if int(result) == result:
        print("Result (integer):", int(result))
    else:
        print("Result (float):", result)
except (ValueError, TypeError):
    print("Unable to calculate the sum of the variables.")


#########

## Q7

cubes_for_loop = []
for x in range(11):
    cube = x ** 3
    cubes_for_loop.append(cube)
print(cubes_for_loop)
cubes_list_comprehension = [x ** 3 for x in range(11)]
print(cubes_list_comprehension)

########

## Q8

a = [(i,j) for i in range(3) for j in range(4)]
print(a)

########

## Q9

triples = [(a, b, c) for c in range(1, 100) for b in range(1, c) for a in range(1, b) if a**2 + b**2 == c**2]
triples.sort()
print(len(triples))
print(triples)


###########

## Q10

import math
def normalize_vector(vector):
    vector_len = math.sqrt(sum(x**2 for x in vector))
    normalized_vector = tuple(x / vector_len for x in vector)   
    return normalized_vector

vector = (5, 4, 3, 2)
vector_len = math.sqrt(sum(x**2 for x in vector))
normalized_vector = normalize_vector(vector)
normalized_vector_len = math.sqrt(sum(x**2 for x in normalized_vector))
print(f"Original vector is {vector} and length equals to {vector_len:.2f}.")
print(f"Normalized vector is {normalized_vector} and length equals to {normalized_vector_len:.2f}.")


#############

## Q11

result = [0,1]
for i in range(2,20):
    result.append(result[i-1]+result[i-2])   
print(result)

