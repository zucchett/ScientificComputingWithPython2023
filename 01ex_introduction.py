# Exercise 1 - The HelloWorld replacement
# Part a:
f = []
for i in range(1, 101):
    if (i % 3 == 0):
        if (i % 5 == 0):
            f.append("HelloWorld")
        else:
            f.append("Hello")
    elif (i % 5 == 0):
        f.append("World")
    else:
        f.append(i)

t = tuple(f)
print("First tuple:")
print(t)
j = list(t)

# Part b:
for k in range(len(j)):
    if (j[k] == "Hello"):
        j[k] = "Python"
    if (j[k] == "World"):
        j[k] = "Works"
    if (j[k] == "HelloWorld"):
        j[k] = "PythonWorks"
tup = tuple(j)
print("--------------", "after substitution :",sep="\n")
print(tup)

# Exercise 1 - Swap
x = input ("enter first input: ")
print("x : ", x)
y = input ("enter scond input: ")
print("y : " ,y)
x, y = y, x
print("---------------", "swap results:", sep="\n")
print("x : " ,x)
print("y : " ,y)

#Exercise 1 - computing the distance
import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
p1 = (x1,y1)
print("p1:", p1)
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
p2 = (x2, y2)
print("p2:", p2)

calD =math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
print("distance between the given points is : %.3f" % calD)


#counting letters
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
#s1 analysis
s1 = s1.lower()
for i1,j1 in enumerate(s1):
    if (j1 not in s1[:i1]):
        print(j1,":", s1.count(j1))
#s2 analysis
s2 = s2.lower()
print("second string")
for i2, j2 in enumerate(s2):
    if (j2 not in s2[:i2]):
        print(j2,":", s2.count(j2))

#Isolating the unique
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
counter = 0
for i in l:
    if (l.count(i) == 1):
        counter += 1
print ("uniques total :",counter)

#-------
#casting
x1 = input("enter x1 of type(str, int, or float):")
x2 = input("enter x2 of type(str, int, or float):")
try:
    x1 = float(x1)
    x2 = float(x2)
    sum = x1 + x2
    print("add operation is feasible. sum is:", sum)
    print("first input type is", type(x1), "and second input type is", type(x2))
except (ValueError, TypeError):
    print("add operation is not possible for x1 and x2")
    print("first input type is", type(x1), "and second input type is", type(x2))
#---------
# cubes a
cubes_for = []
for i in range(11):
    cubes_for.append(i ** 3)
# cubes b
cubes_list = [i ** 3 for i in range(11)]
print(cubes_for)
print(cubes_list)

#list comprehension
a = [(i,j) for i in range(3) for j in range(4)]
print(a)

#Nested list comprehension
p =[(a,b,c) for c in range(1,100) for b in range(1,c) for a in range(1,b) if (a*a) + (b*b) == (c*c)]
p = tuple(p)
print(p)

#Normalization of a N-dimensional vector
import math
x = input("enter size of the vector ")
vector = []
for i in range(int(x)):
    k = input("enter elements (numbers are accepted)")
    vector.append(float(k))
print(vector)
r = math.sqrt(sum([x**2 for x in vector]))
norm_vector = []
for k in vector:
    norm_vector.append(k/r)
print("result vector:", norm_vector)

#11:The Fibonacci sequence
fibList = []
for x in range(20):
    if (len(fibList) < 2):
        fibList.append(x)
    else:
        fibList.append(fibList[x-1] + fibList[x-2])
print(fibList)