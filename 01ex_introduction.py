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

# In[ ]:
print("****1.a*************************************************************************")

#a

for i in range(1, 101):
    if i % 15 == 0:
        print("HelloWorld")
    elif i % 3 == 0:
        print("Hello")
    elif i % 5 == 0:
        print("World")
    else:
        print(i)


# In[ ]:

print("****1.b*************************************************************************")
#b
my_list=[]
for i in range(1, 101):
    if i % 15 == 0: #?
        my_list.append("HelloWorld")
    elif i % 3 == 0:
         my_list.append("Python")
    elif i % 5 == 0:
         my_list.append("Works")
    else:
         my_list.append(i)
my_tuple=tuple(my_list)
print(my_tuple)


# 2\. **The swap**
# 
# Write a program that swaps the values of two input variables `x` and `y` from command line (whatever the type).
# 
# Try to do that without using a temporary variable, exploiting the Python syntax.

# In[ ]:

print("****2.*************************************************************************") 
x=input('Please set x value')
y=input('Please set y value')
print("old x :",x)
print("old y :",y)
x, y = y, x
print("new x :",x)
print("new  y :",y)


# 3\. **Computing the distance**
# 
# Write a program that calculates and prints the euclidean distance between two given points $u$ and $v$ in a 2D space, where $u$ and $v$ are both 2-tuples $(x,y)$.
# 
# Example: if $u=(3,0)$ and $v=(0,4)$, the function should return $5$.
# 
# *Hint:* in order to compute the square root, import the `math` library with `import math` and use `math.sqrt()`.

# In[ ]:

print("****3.*************************************************************************")
import math

u=(3,0)
v=(0,4)
distance=((v[0] - u[0])**2 + (v[1] - u[1])**2)**0.5

print(distance)

print("****4.*************************************************************************")
# 4\. **Counting letters**
# 
# Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.
# 
# The test strings are:

# In[ ]:


s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"


# In[ ]:

print("****4.for s1*************************************************************************")
character_count=dict()
for i in s1 :
    i=i.lower()
    if i in character_count:
        character_count.update({i:character_count[i]+1})
    else :
        character_count[i] = 1
for i,j in character_count.items():
    print(i,j)
    


# In[ ]:

print("****4. for s2*************************************************************************")
character_count=dict()
for i in s2 :
    i=i.lower()
    if i in character_count:
        character_count.update({i:character_count[i]+1})
    else :
        character_count[i] = 1
for i,j in character_count.items():
    print(i,j)
    


# 5\. **Isolating the unique**
# 
# Write a program that determines and counts the unique numbers (numbers with only one occurrence) in the list:

# In[ ]:

print("****5.*************************************************************************")
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]


# In[ ]:


l_unique=[]
countcont=[]

for i in l :
    if i not in l_unique :
        l_unique.append(i)
        
num_of_unique=len(l_unique)

print("number of unique numbers : ",num_of_unique)


# Do the same exploiting only the Python data structures.

# 6\. **Casting**
# 
# Write a program that:
# * reads from command line two variables, that can be either `int`, `float`, or `str`.
# * use the `try`/`except` expressions to perform the addition of these two variables, only if possible
# * print the result without making the code crash for all the `int`/`float`/`str` input combinations.

# In[3]:

print("****6.*************************************************************************")
x,y = input("Set the value of x: "),input("Set the value of y: ")
iftype = input("What is the type of inputs? [str or float or int]   ")
try:
    if(iftype == "float"):
        z = float(x) + float(y)
    if(iftype == "int"):
        z = int(x) + int(y)
    if(iftype == "str"):
        z = x+y
    print(z)
except:
    print("These two inputs cannot be added")


# 7\. **Cubes**
# 
# Create a list of the cubes of *x* for *x* in *[0, 10]* using:
# 
# a) a for loop
# 
# b) a list comprehension

# In[ ]:
print("****7.a*************************************************************************")

#a for loop
cubes_for = []
for i in range(1, 11):
    cubes_for.append(i**3)
print (cubes_for)

print("****7.b*************************************************************************")
#b list comprehension
cubes_lco = [i**3 for i in range(1, 11)]
print (cubes_lco)


# 8\. **List comprehension**
# 
# Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

print("****8.*************************************************************************")
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)
# In[ ]:


a=[(i , j) for j in range(0,4) for i in range(0,3)]
print(a)


# 9\. **Nested list comprehension**
# 
# > A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is (3, 4, 5).
# 
# Find and put in a tuple all unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$.

# In[ ]:

print("****9.*************************************************************************")
pythagorean_triples = [(a, b, c) for a in range(1, 100)
                                 for b in range(a, 100)
                                 for c in range(1, 100)
                                 if a**2 + b**2 == c**2]
print (tuple(pythagorean_triples))


# 10\. **Normalization of a N-dimensional vector**
# 
# Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).

# In[ ]:

print("****10.*************************************************************************")
x=[3,4,9]
a=sum(x)

for i in range(len(x)):
    x[i]=(x[i]/a)
    
print(x)  
    


# 11\. **The Fibonacci sequence**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using only `for` or `while` loops.

# In[ ]:

print("****11.*************************************************************************")
firstnum=1
secondnum=1
summ=0
count=1
while (count<=20):
    count+=1
    firstnum=secondnum
    secondnum=summ
    summ=firstnum+secondnum
    print(summ)

