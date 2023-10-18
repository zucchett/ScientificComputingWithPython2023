import math
import string

print("ESERCIZIO 1")#ESERCIZIO 1

tuple = ()
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("hello world")
        tuple = tuple + ("python works",)
    elif i % 3 == 0:
        print("hello")
        tuple = tuple + ("python",)
    elif i % 5 == 0:
        print("world")
        tuple = tuple + ("works",)
    else:
        print(i)
        tuple = tuple + (i,)
print (tuple)

print("ESERCIZIO 2")# ESERCIZIO 2

x = input("Set the value of x: ")
y = input("Set the value of y: ")
x , y = y , x
print("x = ", x)
print("y = ", y)

print("ESERCIZIO 3")# ESERCIZIO 3

u = (3, 0)
v = (0, 4)
z = math.sqrt((u[0]-v[0])** 2 + (u[1]-v[1])** 2)
print("euclidean distance between u and v is ", z)

print("ESERCIZIO 4")# ESERCIZIO 4

s1 = "Write a program that prints the numbers from 1 to 100.\
But for multiples of three print Hello instead of the number and for the multiples of five print World.\
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
s1.lower()
s2.lower()
letters = list(string.ascii_lowercase)
for i in letters:
    counts1 = 0
    for j in s1:
        if i == j:
            counts1 = counts1+1
    print(i," in s1 = ",counts1)

print("\n")
for i in letters:
    counts2 = 0
    for j in s2:
        if i == j:
            counts2 = counts2+1
    print(i," in s2 = ",counts2)

print("ESERCIZIO 5")# ESERCIZIO 5

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
countunique = 0
for i in l:
    count = 0
    for j in l:
        if i == j:
            count = count + 1
    if count == 1:
        print(i, " is unique")
        countunique = countunique + 1
print("unique numbers are ",countunique)
print("\n alternative method: \n")
new_list = []
for i in l:
    if l.count(i) == 1:
        print(i, " is unique")
        new_list.append(i)
print("number of unique elements: ", len(new_list))

print("ESERCIZIO 6")# ESERCIZIO 6

a = input("insert the first value  ")
b = input("insert the second value  ")
try:
    c = float(a) + float(b)
    print(c)
except:
    print( "one of the input is not valid")

print("ESERCIZIO 7")# ESERCIZIO 7

cubes_list = []
for i in range(11):
    cubes_list.append(i**3)
print(cubes_list)
print("\n second method:")
cubes = [x**3 for x in range(11)]
print(cubes)

print("ESERCIZIO 8")# ESERCIZIO 8

a = [(i, j) for i in range(3) for j in range(4)]
print(a)

print("ESERCIZIO 9")# ESERCIZIO 9

triples = []
for a in range(1, 100):
    for b in range(a, 100):
        c = (a**2 + b**2)**0.5
        if c.is_integer() and c < 100:
            triples.append((a, b, int(c)))

print(triples)

print("ESERCIZIO 10")# ESERCIZIO 10

def normalization(vector):

    squared_sum = sum(x**2 for x in vector)

    if squared_sum == 0:
    
        return [0 for x in vector]

    
    
    normalization_factor = 1.0 / math.sqrt(squared_sum)

    normalized_vector = [x * normalization_factor for x in vector]

    return normalized_vector

vector = [5, 4, 7]
normalized_vector = normalization(vector)
print("the normalized vector of ", vector, " is:")
print(normalized_vector)

print("ESERCIZIO 11")# ESERCIZIO 11

fibonacci = [0, 1]

for i in range(2, 20):
    next_fibonacci = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_fibonacci)

print(fibonacci)

