#!/usr/bin/env python
# coding: utf-8

# You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a single dedicated `.py` file called `01ex_introduction.py`.
# 
# You can divide the individual exercises in the source code with appropriate comments (`#`).
# 
# The exercises need to run without errors with `python3 01ex_introduction.py`.

# 1\. **The HelloWorld replacement**
# 
# a) Write a program that:
# - prints the numbers from 1 to 100
# - but for multiples of three print "`Hello`" instead of the number and for the multiples of five print "`World`"
# - for numbers which are multiples of both three and five print "`HelloWorld`".
# 
# b) Put the result in a tuple and substitute "`Hello`" with "`Python`" and "`World`" with "`Works`".

#%%

#a)

n=100
case=''



for i in range(n):
    if ((i+1)%3)==0:
        case+="Hello"
    if ((i+1)%5)==0:
        case+="World"
    if ((i+1)%3)!=0 and ((i+1)%5)!=0:
        case=i+1
    print(case)
    case=''


#%%


#b)

def HelloWorld_Replacement(word1, word2):
    n=100
    a=[]
    case=''
    for i in range(n):
        if ((i+1)%3)==0:
            case+=word1
        if ((i+1)%5)==0:
            case+=word2
        if ((i+1)%3)!=0 and ((i+1)%5)!=0:
            case=i+1
        a.append(case)
        case=''
    return tuple(a)
        

print(HelloWorld_Replacement('Python', 'Works'))

#%%

# 2\. **The swap**
# 
# Write a program that swaps the values of two input variables `x` and `y` from command line (whatever the type).
# 
# Try to do that without using a temporary variable, exploiting the Python syntax.

#%%


x=int(input("saisissez un nombre :"))
y=int(input("saisissez un nombre :"))
print("x = ", x, " et y =", y)

x=x+y
y=x-y
x=x-y

print("x = ", x, " et y =", y)

#%%


# 3\. **Computing the distance**
# 
# Write a program that calculates and prints the euclidean distance between two given points $u$ and $v$ in a 2D space, where $u$ and $v$ are both 2-tuples $(x,y)$.
# 
# Example: if $u=(3,0)$ and $v=(0,4)$, the function should return $5$.
# 
# *Hint:* in order to compute the square root, import the `math` library with `import math` and use `math.sqrt()`.

#%%


import math as m

u=(3,0)
v=(0,4)

d=m.sqrt((u[0]-v[0])**2+(u[1]-v[1])**2)
print(" u = ",u,"\n","v = ", v,"\n","d = ", d)

#%%

# 4\. **Counting letters**
# 
# Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.
# 
# The test strings are:

#%%

s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

def Count_Char(S):
    dic={}
    S=list(S.lower())
    Si=set(S)
    for i in Si:
        nb=S.count(i)
        dic[i]=nb
    return dic

dic_s1=Count_Char(s1)
dic_s2=Count_Char(s2)

print(dic_s1)
print(dic_s2)
    
#%%     

# 5\. **Isolating the unique**
# 
# Write a program that determines and counts the unique numbers (numbers with only one occurrence) in the list:

#%%


l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]


l_unique=[]
count_unique=0
l_set=set(l)
for i in l_set:
    if l.count(i)==1:
        l_unique.append(i)
        count_unique+=1
print("There are ", count_unique, " unique number in the list")
print("Wich are : ", l_unique)

#%%
# Do the same exploiting only the Python data structures.

#%%

l_unique=[x for x in sorted(l) if l.count(x)==1]
print(l_unique)
print(len(l_unique))

#%%

# 6\. **Casting**
# 
# Write a program that:
# * reads from command line two variables, that can be either `int`, `float`, or `str`.
# * use the `try`/`except` expressions to perform the addition of these two variables, only if possible
# * print the result without making the code crash for all the `int`/`float`/`str` input combinations.

#%%


a=input("Enter a variable (int, float or str)")
b=input("Enter a second variable (int, float or str)")
print("a = ", a, "; b = ", b)

try:
    a=float(a)
    b=float(b)
    
    if int(a)==a:
        a=int(a)
    
    if int(b)==b:
        b=int(b)
    
except:
    print('')

try:
    c=a+b
    print("a + b = ", c)

except: 
    print("addition of a and b impossible")
    
else:
    print("addition of a (", type(a),") and b (", type(b),") succeed !")

#%%

# 7\. **Cubes**
# 
# Create a list of the cubes of *x* for *x* in *[0, 10]* using:
# 
# a) a for loop
# 
# b) a list comprehension

#%%

#a)

def List_Cubes(n):
    l=[]
    for i in range(n):
        l.append(i**2)
    return l

print (List_Cubes(10))


#%%

#b)

print([x**2 for x in range(10)])

#%%

# 8\. **List comprehension**
# 
# Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

#%%


a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)


#%%


print([(i,j) for i in range(3) for j in range(4)])

#%%

# 9\. **Nested list comprehension**
# 
# > A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is (3, 4, 5).
# 
# Find and put in a tuple all unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$.

#%%


import math

n = 100
pytha = []

for i in range(1,n):
    for j in range(1,n):
        p = math.sqrt(i**2 + j**2)
        if int(p) == p and p < 100:
            pytha.append((min(i,j), max(i,j), int(p)))

pytha=tuple(set(pytha))
print(pytha)                 

#%%

# 10\. **Normalization of a N-dimensional vector**
# 
# Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).

#%%

import math as m

def Vector_Normal(vector):
    norm = m.sqrt(sum(x**2 for x in vector))
    if norm == 0:
        print("Normalization impossible - null vecteur")
    else:
        vector = tuple([round(x/norm,3) for x in vector])
    return vector



#Example:

V1 = (12, 34, 23.344, 0.134, 1.1, 1, 0, 34.145, 3)
V1_normal = Vector_Normal(V1)
V1_Sum = round(m.sqrt(sum(x**2 for x in V1_normal)),3)


print ("V1 = ", V1)
print("V1 normalized = ", V1_normal)
print("Square sum of V1 = ", V1_Sum)

V2 = (0,0,0)
V2_normal = Vector_Normal(V2)

#%%

#     11\. **The Fibonacci sequence**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using only `for` or `while` loops.

#%%


def Fibonacci(n):
    f=[0, 1]    
    while(len(f)<n):
        f.append(f[-1]+f[-2])
    return f


#Example :

Fibo_20 = Fibonacci(20)
print(Fibo_20)

