# 1. The HelloWorld replacement
print("\n\n---------- 1. The HelloWorld replacement ----------\n\n")
list = []
for i in range(1,100):
    if (i%3 == 0) and (i%5 == 0):
        print("HelloWorld")
        list.append("PythonWorks")
    elif i%3 == 0:
        print("Hello")
        list.append("Python")
    elif i%5 == 0:
        print ("World")
        list.append("Works")
    else:
        print(i)

final = tuple(list)
print(final)




# 2. The swap
print("\n\n---------- 2. The swap ----------\n\n")
x = input("Insert x value: ")
y = input("Insert y value: ")

print("x value before swap: ",x)
print("y value before swap: ",y)
x,y = y,x
print("x value after swap: ",x)
print("y value after swap: ",y)


# 3. Computing the distance
print("\n\n---------- 3. Computing the distance ----------\n\n")
import math

u = (3,0)
v = (0,4)
print(math.sqrt(math.pow(u[0]-v[0],2)+math.pow(u[1]-v[1],2)))

# 4. Counting letters
print("\n\n---------- 4. Counting letters ----------\n\n")
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

a = {}
s1 = s1.lower()
s2 = s2.lower()
letters = " abcdefghijklmnopqrttuvwxyz"

print("Letters in s1: ")
for i in letters:
    print(i,"occures",s1.count(i),"times")

print("Letters in s2: ")
for i in letters:
    print(i,"occures",s2.count(i),"times")

#from collections import Counter
#lettersS1 = Counter(s1.lower())
#print(lettersS1)
#lettersS2 = Counter(s2.lower())
#print(lettersS2)


# 5. Isolating the unique
print("\n\n---------- 5. Isolating the unique ----------\n\n")
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

d={}
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1

list=[]

for i in d:
    if d[i]==1:
        list.append(i)

print(len(list))

#python data structure
list = [i for i in l if l.count(i)==1]
print(len(list))

# 6. Casting
print("\n\n---------- 6. Casting ----------\n\n")
x = input("Inserisci un valore: ")
y = input("Inserisci un valore: ")
try:
    w = x+y
    print (w)
except:
    print("Problem with summation")

# 7. Cubes
print("\n\n---------- 7. Cubes ----------\n\n")
x = [x for x in range(11)]
cubes=[]
#for loop
for i in x:
    cubes.append(i**3)

print(cubes)

#list
cubes = [x**3 for x in range(11)]

print(cubes)

# 8.  List comprehension
print("\n\n---------- 8.  List comprehension ----------\n\n")
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)


a = [(i,j) for i in range(3) for j in range(4)]
print (a)


# 9. Nested list comprehension
print("\n\n---------- 9. Nested list comprehension ----------\n\n")
pt = []

for a in range(1, 100):
    for b in range(a, 100):
        c_squared = a**2 + b**2
        c = int(c_squared**0.5)

        if c*c == c_squared and c<100:
            pt.append((a, b, c))

print(pt)



# 10. Normalization of a N-dimensional vector
print("\n\n---------- 10. Normalization of a N-dimensional vector ----------\n\n")
import math

input_tuple = (3,1,-4,6)
print("Input tuple: ",input_tuple)

norm_factor = math.sqrt(sum(x**2 for x in input_tuple))
norm_tuple =tuple([x/norm_factor for x in input_tuple])
print(norm_tuple)


# 11. The Fibonacci sequence
print("\n\n---------- 11. The Fibonacci sequence ----------\n\n")
a = 0
b = 1
fib = [0, 1]
for i in range(18):
    fib.append(a + b)
    a, b = b, a + b

print(fib)