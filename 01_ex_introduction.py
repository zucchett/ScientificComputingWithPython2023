#1. The HelloWorld replacement
t=tuple()
for i in range (1,101):
    if (i%3==0 and i%5==0): 
        print("HelloWorld")
        t+= ("PythonWorks",)
    elif (i%3 == 0): 
        print("Hello")
        t+=('Python',)
    elif (i%5==0): 
        print("World")
        t+=('Works',)
    else: 
        print (i) 
        t+= (i,)
print(t)
#2. The swap
x= input("Set the value of x: ")
y= input("Set the value of y: ")
x,y=y,x
print ("value of x: ", x)
print ("value of y: ", y)

#3. Computing the distance
import math 
def dist_euc(u,v):
    return math.sqrt((v[0]-u[0])**2 + (v[1]-u[1])**2)
dist_euc((3,0),(0,4))

#4. Counting letters
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

d=dict()
def count_occ(s):
    for c in (s.upper()):
        d[c]=s.count(c)
    return d
print(count_occ(s1))
print(count_occ(s2))

#5. Isolating the unique
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

for i in l:
    if l.count(i) == 1:
        print (i)

#Do the same exploiting only the Python data structures.
dict = {}
s= set()
for i in l:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for k, v in dict.items():
    if v == 1:
        s.add(k)
print(s)
print("number of unique values: ", len(s))

#6. casting
i = input("Set a value of int i: ")
f = input("Set a value of float f: ")
s = input("Set a value of string s: ")

try:
    i = int(i)
    f = float(f)
    #s is already a string
    res1 = i + f
    res2 = s + str(f)  
    res3 = s + str(i)  
    print(res1, res2, res3)

except ValueError:
    print("invalid numbers")

#7. Cubes
#using for loop
la = []
for x in range(11):
    la.append(x ** 3)
print(la)
#using list comprehension 
lb = [x ** 3 for x in range(11)]
print (lb)

#8. List comprehension
a = [(i,j) for i in range(3) for j in range(4)]
print(a)

#9. Nested list comprehension
L = [(a,b,c) for c in range(1,100) for b in range(1,c) for a in range(1,b) if a**2 + b**2 == c**2]
s = set(L) #unique values
Pythagorean_triple = list(s)
print (Pythagorean_triple)

#10. Normalization of a N-dimensional vector
import math
v = (4,6,7)
n=0
normalized_V = tuple()
for x in v:
    n += x ** 2

sq = math.sqrt(n)
for x in v: 
    normalized_V += (x/sq ,)
print(normalized_V)

#11. The Fibonacci sequence
fib= [0,1]
for i in range(2,20):
    fib.append(fib[i-1] + fib[i-2])
print(fib)