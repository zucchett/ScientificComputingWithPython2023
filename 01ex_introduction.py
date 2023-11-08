import numpy
import sys
import math

#The HelloWorld replacement
print("*****************************************")
print("The HelloWorld replacement")
print("*****************************************")

#create an empty tuple
tupla = ()

#for loop with index 1<= i <= 100
for i in range(1,101):
    #more restrictive condition (find numbers which are multiples of both three and five)
    if(i%3==0 and i%5==0): 
        print("Hello world")
        tupla = tupla + ("PythonWorks",)
    #find numbers which are multiples of three
    elif(i%3==0): 
        print("Hello")
        tupla = tupla + ("Python",)
    #find numbers which are multiples of five
    elif(i%5==0): 
        print("World")
        tupla = tupla + ("Works",)
    #other numbers
    else: 
        print(i)
        tupla = tupla + (i,)

print(tupla,"\n")


#The swap
print("*****************************************")
print("The swap")
print("*****************************************")
try:
    x = sys.argv[1]
    y = sys.argv[2]
    x,y = y,x
    print(x)
    print(y,"\n")
except:
    print("You have to write two numbers in the command line!!\n")

#Computing the distance
print("*****************************************")
print("Computing the distance")
print("*****************************************")
u = (3,0)
v = (0,4)
distance = 0
try:
    distance = math.sqrt(pow(v[0]-u[0],2)+pow(v[1]-u[1],2))
    print(distance,"\n")
except:
    print("Invalid values\n")


#Counting letters
print("*****************************************")
print("Counting letters")
print("*****************************************")
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
#Ignore differences in capitalization in the first string
s1 = s1.lower()
s2 = "The quick brown fox jumps over the lazy dog"
#Ignore differences in capitalization in the second string
s2 = s2.lower()

dic = {}
for i in range (0,len(s2)):
    dic[s2[i]] = 0

for i in dic:
    for j in range (0,len(s2)):
        if(s2[j]==i): dic[s2[j]] = dic[s2[j]] + 1

print(dic,"\n")

#Isolating the unique
print("*****************************************")
print("Isolating the unique")
print("*****************************************")

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

dic = {}
for i in range (0,len(l)):
    dic[l[i]] = 0

#dictionary to memorize the number of occurences for each number
for i in dic:
    for j in range (0,len(l)):
        if(l[j]==i): dic[l[j]] = dic[l[j]] + 1

count = 0
print(dic)
for i in dic:
    if(dic[i]==1):
        count = count + 1
        print(i)

print("Count of the unique numbers: ", count,"\n")

#Casting
print("*****************************************")
print("Casting")
print("*****************************************")

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    sum = x+y
    print(sum,"\n")
except:
    print("Invalid values, you have to re-insert the number in the command line!","\n")

#Cubes
print("*****************************************")
print("Cubes")
print("*****************************************")

list = []
for i in range(0,11):
    list.append(i**3)
print(list)

list = [x**3 for x in range(11)]
print(list,"\n")

#List comprehension
print("*****************************************")
print("List comprehension")
print("*****************************************")
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)


a = [(i,j) for i in range(3) for j in range(4)]
print(a,"\n")

#Nested list comprehension
print("*****************************************")
print("Nested list comprehension")
print("*****************************************")
list = []
a = 3
b = 4
c = 5

for c in range(5,101):
    for b in range(4,101):
        for a in range(3,101):
            if ((a**2+b**2)==c**2): list.append((a,b,c))

print(list,"\n")


#Normalization of a N-dimensional vector
print("*****************************************")
print("Normalization of a N-dimensional vector")
print("*****************************************")

list = [1,2,3,4,5]
sum = 0
for i in range(0,len(list)):
    sum = sum + list[i]

for i in range(0,len(list)):
    list[i] = list[i]/sum
print(list,"\n")

#The Fibonacci sequence
print("*****************************************")
print("The Fibonacci sequence")
print("*****************************************")
list = []
x = 0
y = 1
num = 0
for i in range(0,20):
    num = x+y
    list.append(num)
    y = x
    x = num

print("First 20 numbers of the Fibonacci sequence: ",list)