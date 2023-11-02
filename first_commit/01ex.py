##The HelloWorld replacement
list1 = []
for a in range(1,101):
    if (a%3)==0 and (a%5)==0:
        list1.append('HelloWorld')
        print('HelloWorld')
    elif (a%3)==0:
        list1.append('Hello')
        print('Hello')
    elif (a%5)==0:
        list1.append('World')
        print('World')
    else:
        list1.append(a)
        print(a)
        
for i in range(1,len(list1)):
    if list1[i]=='Hello':
        list1[i] = 'Python'
    elif list1[i]=='World':
        list1[i]=='Works'

print(list1)
            
tuple1 = tuple(list1) #check if it is really a tuple


##Swapping
print("\n")
x = input('Value of x: ')
y = input('Value of y: ')

x,y = y,x

print(x)
print(y)



##Eucledin distance
print("\n")
import math

u = (3, 0)
v = (0, 4)

dist = math.sqrt((u[0]+v[0])**2 + (u[1]+v[1])**2)

print(dist)

##Counting letters
print("\n")
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

dictionary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'z', 'j', 'k', 'x', 'w', 'y']
dictionaryCAP = ['A', 'B', 'C', 'D', 'E', 'F','G','H','I','L','M','N','O','P','Q','R','S','T','U','V','Z','J','K','X','W','Y']
counters1 = []
counters2 = []

for i in range(0,len(dictionary)):
    counters1.append(s1.count(dictionary[i])+s1.count(dictionaryCAP[i]))
    
for j in range(0,len(dictionary)):
    print('The occurance of the letter ', dictionary[j], 'in string s1 is ', counters1[j] )
    
for i in range(0,len(dictionary)):
    counters2.append(s2.count(dictionary[i])+s2.count(dictionaryCAP[i]))
    
for j in range(0,len(dictionary)):
    print('The occurance of the letter ', dictionary[j], 'in string s2 is ', counters2[j] )
    

##Isolating the unique
print("\n")
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

uniqueNumberlist = []
for i in range(1, len(l)):
    counter = l.count(l[i])
    if counter == 1:
        uniqueNumberlist.append(l[i])

print('In list l there are ', len(uniqueNumberlist), ' unique numbers.')
#print('The uniqe numbers are: ', [j for j in uniqueNumberlist])



##Casting
print("\n")
x = input('Set the value of x: ')
y = input('Set the value of y: ')

try:
    sum1 = float(x) + float(y)
    print(sum1)
except:
    print('Those two type of variables cannot be summed.')
    
##Cubes
print("\n")
cubes_loop = []
for m in range(0,11):
    cubes_loop.append(m**3)
    
print(cubes_loop)

cubes_list = [l**3 for l in range(0,11)]
print(cubes_list)

##List comprehension
print("\n")
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

b = [(x,y) for x in range(3) for y in range(4)]
print(b)

##Nested list comprehension
print("\n")
import math

pythaTriplets = [(a, b, int(math.sqrt(a**2 + b**2))) for a in range(1,101) for b in range(1, 101) if math.sqrt(a**2 + b**2) < 100 and math.sqrt(a**2 + b**2)%1==0]
print(pythaTriplets)
print(len(pythaTriplets))

##Normalization of a N-dimensional vector
print("\n")
import math
try:
    tvec = []
    while True: 
        tvec.append(float(input('Insert a sequence of numbers, when finished type any string to exit the input phase: ')))
                    
except:
    print('This is the vector that has to be normalized: ', tvec)

norm = math.sqrt(sum(x**2 for x in tvec))
vec = [x/norm for x in tvec]

print('This is the normalized vector: ', vec)


##Fibonacci sequence
print("\n")
F0 = 0
F1 = 1

F = []
F.append(F0)
F.append(F1)

for i in range(2, 20):
    F.append(F[i-1] + F[i-2])

print(F)
