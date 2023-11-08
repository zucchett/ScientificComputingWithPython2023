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

# In[6]:


for i in range (1,101):
    if i%15 == 0:
        print ("Hello World")
    elif i%3==0:
        print ("Hello")
    elif i%5==0:
        print ("World")
    else :
        print (i)


# In[7]:


result = []
for i in range (1,101):
    if i%15 == 0:
        result.append('python works')
    elif i%3==0:
        result.append('python')
    elif i%5==0:
        result.append('works')
    else :
        result.append(i)
print(tuple(result)) 


# 2\. **The swap**
# 
# Write a program that swaps the values of two input variables `x` and `y` from command line (whatever the type).
# 
# Try to do that without using a temporary variable, exploiting the Python syntax.

# In[ ]:


left, right = input().split(' ')
print(left, right, end='=>')
left, right = right, left
print(left, right)


# 3\. **Computing the distance**
# 
# Write a program that calculates and prints the euclidean distance between two given points $u$ and $v$ in a 2D space, where $u$ and $v$ are both 2-tuples $(x,y)$.
# 
# Example: if $u=(3,0)$ and $v=(0,4)$, the function should return $5$.
# 
# *Hint:* in order to compute the square root, import the `math` library with `import math` and use `math.sqrt()`.

# In[ ]:


import math

u=(float(input()),float(input()))
v=(float(input()),float(input()))
d= math.sqrt((u[0]-v[0])**2+(u[1]-v[1])**2)
print(d) 


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


s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s1 , s2 = s1.lower(), s2.lower()

for i in s1:
    print(i , ": ",s1.count(i) + s2.count(i))


# 5\. **Isolating the unique**
# 
# Write a program that determines and counts the unique numbers (numbers with only one occurrence) in the list:

# In[ ]:


l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]


# In[ ]:


l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

result = {}

for i in range(len(l)):
    c = 0
    for j in range(len(l)):
        if l[i] == l[j]:
            c+=1
            result[l[i]] = c
#print(result)
uniques = []
for key, value in result.items():
    if value == 1:
        uniques.append(key)
print(uniques)    


# Do the same exploiting only the Python data structures.

# 6\. **Casting**
# 
# Write a program that:
# * reads from command line two variables, that can be either `int`, `float`, or `str`.
# * use the `try`/`except` expressions to perform the addition of these two variables, only if possible
# * print the result without making the code crash for all the `int`/`float`/`str` input combinations.

# In[ ]:


a = input('enter your value: ')
b = input('enter your value: ')
try:
     if not a.isnumeric() and not b.isnumeric():
          c = a + b
     else:
          c = float(a) + float(b)
except:
     c = 'can not add integer to string!'
print(c)


# In[ ]:


a=input("input 1:")
b=input("input 2:")
try:
    try:
        a,b=float(a),float(b)
        c=a+b
        print(c)
   
    except: 
        try:
            a=int(a)
            print('can not add integer to string!')            
        except:
             b=int(b)
             print('can not add integer to string!')
except: 
    c=a+b 
    print(c)


# 7\. **Cubes**
# 
# Create a list of the cubes of *x* for *x* in *[0, 10]* using:
# 
# a) a for loop
# 
# b) a list comprehension

# In[ ]:


cubes = [i**3 for i in range(0, 11)]
print(cubes)


# 8\. **List comprehension**
# 
# Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

# In[ ]:


a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)


# In[ ]:


print([(i, j) for i in range(3) for j in range(4)])


# 9\. **Nested list comprehension**
# 
# > A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is (3, 4, 5).
# 
# Find and put in a tuple all unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$.

# In[ ]:


result = []
c, m = 0, 2
while c < 100 :
    for n in range(1, m) :
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        if c > 100 :
            break
        result.append((a, b, c))
        m = m + 1
print(tuple(result))        


# 10\. **Normalization of a N-dimensional vector**
# 
# Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).

# In[ ]:


import math

n = int(input('Enter the number of dimensions: '))
vector = []
square_sum = 0
for i in range(n):
    vector.append(int(input()))
    square_sum += vector[i]**2
size = math.sqrt(square_sum)
for i in range(n):
    vector[i] = vector[i] / size
print(vector)    


# 11\. **The Fibonacci sequence**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using only `for` or `while` loops.

# In[ ]:


fibonacci = [1, 1]
for i in range(1, 19):
    fibonacci.append(fibonacci[i] + fibonacci[i - 1])
print(fibonacci)    

