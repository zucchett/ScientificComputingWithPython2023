#QUESTION NUMER 1

#SOLUTION

number = [x for x in range(1, 101)]

for i in range(len(number)):
    if number[i] % 5 == 0 and number[i] % 3 == 0:
        number[i] = "HelloWorld"
    elif number[i] % 5 == 0:
        number[i] = "World"
    elif number[i] % 3 == 0:
        numer[i] = "Hello"
print("Results to point (a)) is: \n", number)
print()
for i in range(len(number)):
    if number[i] == "Hello":
        number[i] = "Python"
    elif numer[i] == "World":
        number[i] = "Works"

tuple_mynumbers = (*number,)
print("result of point (b) is ): \n", tuple_mynumbers)
print()
####################################### END OF QUESTION NUMBER 1

#QUESTION NUMBER 2
#SOLUTION

x = input("Set the value of x: ")  # remember to click Enter after inputting the string
y = input("Set the value of y: ")  # remember to click Enter after inputting the string

x, y = y, x

print("x =", x, ", y =", y)
print()
#####################################END OF QUESTION NUMBER 2

#QUESTION NUMBER 3
#SOLUTION

import math

u_list = []
v_list = []

u_list = [float(item) for item in input("Enter the coordinates of the first point as x,y: ").split(",")]
v_list = [float(item) for item in input("Enter the coordinates of the second point as x,y: ").split(",")]
print()

u = (*u_list,)
v = (*v_list,)

distance = math.sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2)

print("The Euclidean distance between the points is: ", distance)
print()
############################# END OF QUESTION NUMBER 3

#QUESTION NUMBER 4
#SOLUTION

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

list_s1 = list(s1.lower())
list_s2 = list(s2.lower())
list_s3 = list_s1

counter1 = {i: list_s1.count(i) for i in list_s1}
counter2 = {i: list_s2.count(i) for i in list_s2}

for i in range(len(list_s2)):
    list_s3.append(list_s2[i])

counter3 = {i: list_s3.count(i) for i in list_s3}

print("First string characters: \n", counter1)
print()
print("Second string characters: \n", counter2)
print()
print("Number of each character in total: \n", counter3)
print()
##############################END OF QUESTION 4

#QUESTION NUMBER 5
#SOLUTION

#5.Isolating the unique

#Write a program that determines and counts the unique numbers in the list:

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

 #Do the same exploiting only the Python data structures.

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

unique_numbers = []

for i in range(len(l)):
    m = 0
    count = 0
    while m < len(l):
        if l[i] == l[m]:
            count = count + 1
        m = m + 1
    if count == 1:
        unique_numbers.append(l[i])

print("The unique numbers in the list are", len(unique_numbers), "and they are: \n", unique_numbers)
print()

counter_unique = {i: l.count(i) for i in l}
unique_values = [i for i in counter_unique if counter_unique[i] == 1]

print("The unique values found exploiting the python data structures are", len(unique_values), "and they are: \n",
      unique_values)
print()
#########################END OF QUESTION NUMBER 5

#QUESTION NUMBER 6
#SOLUTION

#Write a program that:
# reads from command line two variables, that can be either `int`, `float`, or `str`.
# use the `try`/`except` expressions to perform the addition of these two variables, only if possible
# and print the result without making the code crash for all the `int`/`float`/`str` input combinations.

p = input("Set the first variable: ")
q = input("Set the second variable: ")

try:
    p = int(p)
except:
    try:
        p = float(p)
    except:
        p = str(p)

try:
    q = int(q)
except:
    try:
        q = float(q)
    except:
        q = str(q)

if (type(p) == int or type(p) == float) and (type(q) == int or type(q) == float):
    print("THE SUM OF TWO NUMBERS, the sum is: ", p + q)
elif type(p) == str and type(q) == str:
    print("THE SUM OF TWO NUMBERS, the sum is: ", p + q)
else:
    p = str(p)
    q = str(q)
    print("You are summing one string and one number, the number will be treated as a string. The sum is: ", p + q)
print()
##############################END OF QUESTION NUMBER 6

#QUESTION NUMBER 7
#SOLUTION

#7. Cubes

#Create a list of the cubes of *x* for *x* in *[0, 10]* using:

#a) a for loop

#b) a list comprehension

cube_1 = []

for i in range(11):
    cube_1.append(i ** 3)

print("Cubes obtained with the for loop: \n", cube_1)
print()

cube_2 = [i ** 3 for i in range(11)]

print("Cubes obtained with the list comprehension: \n", cube_2)
print()
#######################END OF QUESTION NUMBER 7

#QUESTION NUMBER 8
#SOLUTION

# 8 **List comprehension**
# Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

# a = []
# for i in range(3):
#   for j in range(4):
#       a.append((i, j))
# print(a)

# [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]

# single line expression
mark = [(i, j) for i in range(3) for j in range(4)]
print(mark)
print()
#########################END OF QUESTION NUMBER 8

#QUESTION NUMBER 9
#SOLUTION

#9. Nested list comprehension

#> A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is
#(3, 4, 5).

#Find and put in a tuple all unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$.

pytha = []
pytha = [(a, b, c) for a in range(1, 101) for b in range(a + 1, 101) for c in range(101) if
              a ** 2 + b ** 2 == c ** 2]
print("The Pythagorean triples are: \n", pytha)
print()
##########################END OF QUESTION NUMBER 9

#QUESTION NUMBER 10
#SOLUTION

#10. Normalization of a N-dimensional vector

import math
vector = []
sum1 = 0
vector = [int(item) for item in input("Enters the vectors components separated only by commas : ").split(",")]
print()

for i in range(len(vector)):
    sum1 = sum1 + vector[i] ** 2

norm = math.sqrt(sum1)

vector_normalized = [vector[i] / norm for i in range(len(vector))]

print("The norm of your vector is: ", norm)
print()
print("The normalized vector is: \n", vector_normalized)
print()

sum2 = 0
for i in range(len(vector_normalized)):
    sum2 = sum2 + vector_normalized[i] ** 2

norm2 = math.sqrt(sum2)
print("The norm of this new vector is: ", norm2)
print()
#########################END OF QUESTION NUMBER 10

#QUESTION NUMBER 11
#SOLUTION

#11. The Fibonacci sequence

fibo = [0]
n1 = 0
n2 = n1 + 1

for i in range(19):
    fib = n1 + n2
    fibo.append(fib)
    n1 = n2
    n2 = fib
print("The first 20 numbers of the Fibonacci sequence: \n", fibo)
########################END OF QUESTION NUMBER 11

