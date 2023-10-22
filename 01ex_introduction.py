#1\. **The HelloWorld replacement**

#Program to print fro 1 to 100

numbers=[x  for x in range(101)]

for num in numbers:
    print(num)

# but for multiples of three print "`Hello`" instead of the number and for the multiples of five print #"`World`"
#for numbers which are multiples of both three and five print "`HelloWorld`".

replaced = []
for num in range(1, 101):
    if num % 3 == 0 and num % 5 != 0:
        replaced.append("Hello")
    elif num % 3 != 0 and num % 5 == 0:
        replaced.append("World")
    elif num % 3 == 0 and num % 5 == 0:
        replaced.append("Hello World")
    else:
        replaced.append(num)

print(replaced)


#Put the result in a tuple and substitute "`Hello`" with "`Python`" and "`World`" with "`Works`".
modified_replaced = []
for val in replaced:
    if val == "Hello":
        modified_replaced.append("Python")
    elif val == "World":
        modified_replaced.append("Works")
    else:
        modified_replaced.append(val)

result_tuple = tuple(modified_replaced)
print(result_tuple)   


####2\. **The swap**

X=6
print("x before swap",X)
Y=7
print("y before swap",Y)
X,Y=Y,X

print("x after swap",X)
print("y after swap",Y)


#3\. **Computing the distance**

import math

# Define the points u and v as 2-tuples (x, y)
u = (3, 0)
v = (0, 4)

# Calculate the Euclidean distance using the formula
distance = math.sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2)

# Print the result
print(f"The Euclidean distance between {u} and {v} is {distance:.2f}")


##4\. **Counting letters**
input_string=s2.lower()
print("The input string is:", input_string)
mySet = set(input_string)
countOfChars = dict()
for element in mySet:
    countOfChar = 0
    for character in input_string:
        if character == element:
            countOfChar += 1
    countOfChars[element] = countOfChar
print("Count of characters is:")
print(countOfChars)

##5\. **Isolating the unique**
import collections
unique_counts = collections.Counter(e for e in l)

print(len(set(unique_counts)))


#Using python data structure
unique_l= len(set(l))
print(unique_l)
                
##6
value1=int(input("Enter a value"))
value2=str(input("Enter a value"))

try:

    result = value1 + value2

    print(result)
except:
    print("Error: the sum is not possible.")




##7 cubes
##a) a for loop

cubes=[]
for x in range(10):
    cube=x*x*x
    cubes.append(cube)
    
print(cubes)


## list comprehension
cubes=[x*x*x for x in range(10)]

print(cubes)


##8 list comprehension
list_=[(i,j) for i in range(3)  for j in range (4)]
list_

###9 Nested list comprehension
# Define the range of values for a, b, and c
n = 100

# Use list comprehension to generate Pythagorean triples
triples = [(a, b, c) for c in range(1, n) for b in range(1, c) for a in range(1, b) if a**2 + b**2 == c**2]

# Print the generated Pythagorean triples
for triple in triples:
    print(triple)

##10\. **Normalization of a N-dimensional vector**

import math

def normalize_vector(vector):
    # Calculate the Euclidean norm of the vector
    norm = math.sqrt(sum(x**2 for x in vector))
    
    # Normalize the vector by dividing each component by the norm
    normalized_vector = tuple(x / norm for x in vector)
    
    return normalized_vector

# Example usage:
n_dim_vector = (12, 16,20)  # Replace this with your N-dimensional vector
normalized = normalize_vector(n_dim_vector)
print("Original Vector:", n_dim_vector)
print("Normalized Vector:", normalized)


##11 Using for loop

def ForFibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

for num in range (20):
    print ("Fibonnacci for", num, "is",ForFibonacci(num))
    
    
##using while loop
def whileFibonacci(n):
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
    return a
for num in range(20):
    print(whileFibonacci(num))
    
    
#Calculating execution time
import timeit
n=20
for_loop_time = timeit.timeit('ForFibonacci(n)', globals=globals(), number=10000)

While_loop_time = timeit.timeit('whileFibonacci(n)', globals=globals(), number=10000)
print(f"for-based Fibonacci Execution Time: {for_loop_time:.6f} seconds")
print(f"while-based Fibonacci Execution Time: {While_loop_time:.6f} seconds"
    
    
    
    
