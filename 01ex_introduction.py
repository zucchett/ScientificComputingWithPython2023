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

# In[1]:


print("\n--- # 1. The HelloWorld replacement ---\n")

print("\n--- # a ---\n")

result = [] # We create a list to store
for i in range(1,101) :
    if i%3 == 0 and i%5 == 0:
        result.append("HelloWorld")
    elif i%3 == 0:
        result.append("Hello")
    elif i%5 == 0 :
        result.append("World")
    else :
        result.append(i)
        

for item in result:
    print(item)


# In[2]:


print("\n--- # b ---\n")

for i in range(len(result)) :
    if result[i] == "Hello" :
        result[i] = "Python"
    elif result[i] == "World" :
        result[i] = "Works"

result = tuple(result)

print(result)


# 2\. **The swap**
# 
# Write a program that swaps the values of two input variables `x` and `y` from command line (whatever the type).
# 
# Try to do that without using a temporary variable, exploiting the Python syntax.

# In[3]:


print("\n--- # 2. The swap ---\n")

def swap(x=None, y=None):
    if x is None:
        x = input('Enter x : ')
    if y is None:
        y = input('Enter y : ')
    
    print("We have : x =", x, "and y =", y, ".")
    x, y = y, x
    print("After the swap, we have : x =", x, "and y =", y, ".")
    
    return x, y


# In[4]:


print("Here are some swap tests:\n")
swap(2,4)


# In[5]:


swap("Hello", "World!")


# In[6]:


print("\nTest with input :")
swap()


# 3\. **Computing the distance**
# 
# Write a program that calculates and prints the euclidean distance between two given points $u$ and $v$ in a 2D space, where $u$ and $v$ are both 2-tuples $(x,y)$.
# 
# Example: if $u=(3,0)$ and $v=(0,4)$, the function should return $5$.
# 
# *Hint:* in order to compute the square root, import the `math` library with `import math` and use `math.sqrt()`.

# In[7]:


print("\n--- 3. Computing the distance ---\n")

import math 

def Euclidean_distance(u, v):
    distance_euclidienne = math.sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2)
    print("The Euclidean distance is:", distance_euclidienne)
    return distance_euclidienne


# In[8]:


print("Here is a euclidean distance tests :\n")
print("We take: u = (3,0) and v = (0,4)")
u = (3, 0)
v = (0, 4)
distance = Euclidean_distance(u, v)


# 4\. **Counting letters**
# 
# Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.
# 
# The test strings are:

# In[9]:


s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"


# In[10]:


print("\n--- 4. Counting letters ---\n")

def CountingLetters(string):
    string = string.lower()
    Count = {}
    for i in range(len(string)-1) :      
        if string[i] in Count :
            Count[string[i]] += 1
        else:
            Count.update({string[i] : 1})
    return Count
    
print("For character string s1 :", CountingLetters(s1))
print("For character string s2 :", CountingLetters(s2))


# 5\. **Isolating the unique**
# 
# Write a program that determines and counts the unique numbers (numbers with only one occurrence) in the list:

# In[11]:


l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]


# In[12]:


print("\n--- 5. Isolating the unique ---\n")

print("\n--- # a ---\n")

def CountingNumbers(list_numbers):
    unique = []
    Count = []

    for num in list_numbers:
        if num in Count:
            continue
        if list_numbers.count(num) == 1:
            unique.append(num)
        Count.append(num)

    print("Numbers with only one occurrence :", unique)
    print("Count of umbers with only one occurrence :", len(unique))
    return unique, len(unique)

u1 = sorted(CountingNumbers(l)[0])


# Do the same exploiting only the Python data structures.

# In[13]:


print("\n--- # b ---\n")

def CountingNumbers2(list_numbers):
    Count = {}
    for i in range(len(list_numbers)) :      
        if list_numbers[i] in Count :
            Count[list_numbers[i]] += 1
        else:
            Count.update({list_numbers[i] : 1})
    
    unique = [num for num, count in Count.items() if count == 1]
    
    print("Numbers with only one occurrence (Method 2):", unique)
    print("Count of umbers with only one occurrence (Method 2):", len(unique))
    return unique, len(unique)

u2 = sorted(CountingNumbers2(l)[0])


# In[14]:


print("The same results are obtained by both methods u1 == u2 :", u1 == u2)


# 6\. **Casting**
# 
# Write a program that:
# * reads from command line two variables, that can be either `int`, `float`, or `str`.
# * use the `try`/`except` expressions to perform the addition of these two variables, only if possible
# * print the result without making the code crash for all the `int`/`float`/`str` input combinations.

# In[26]:


print("\n--- # 6. Casting ---\n")

def add_variables(var1, var2):
    print("Variable 1 =", var1, "(type of var1 :", type(var1),")")
    print("Variable 2 =", var2, "(type of var2 :", type(var2),")")
    try:
        result = var1 + var2
        print("The result is :", result)
        return result
    except TypeError as e:
        print("TypeError :", e)
        return e
    
print("Test 1 =>", add_variables(10, 7), "\n")
print("Test 2 =>",add_variables(10.1, 7), "\n")
print("Test 3 =>", add_variables(10.1, 7.7), "\n")
print("Test 4 =>", add_variables(10.1, "Hello"), "\n")
print("Test 5 =>",add_variables(10, "Hello"), "\n")


# 7\. **Cubes**
# 
# Create a list of the cubes of *x* for *x* in *[0, 10]* using:
# 
# a) a for loop
# 
# b) a list comprehension

# In[16]:


print("\n--- # 7. Cubes ---\n")

print("\n--- # a ---\n")

list1 = []
for x in range(11) :
    list1.append(x**3)
    
print("With for loop :", list1)


# In[17]:


print("\n--- # b ---\n")

list2 = [x**3 for x in range(11)]

print("With list comprehension :", list2)


# 8\. **List comprehension**
# 
# Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

# In[18]:


print("\n--- 8. List comprehension ---\n")


# In[19]:


a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))


# In[20]:


a_new = [(i,j) for i in range(3) for j in range(4)]

print("By making a comprehension list, we have :", a_new, ".\nThe result is the same as before (Verification with a == a_new) :", a == a_new, ".")


# 9\. **Nested list comprehension**
# 
# > A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is (3, 4, 5).
# 
# Find and put in a tuple all unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$.

# In[37]:


print("\n--- 9. Nested list comprehension ---\n")

def Pythagorean(limit_c) :
    Pythagorean = []
    c = 0
    while c < limit_c :
        for a in range(1, c):
            for b in range(a, c): # If you want to display the tuples (a,b,c) and in addition the tuples (b,a,c) or a =>b and b => a then you need to set: for b in range(1, c):
                if a**2 + b**2 == c**2:
                    Pythagorean.append((a, b, c))
        c+=1
        
    return tuple(Pythagorean) 

print(f"All unique Pythagorean triples with c < 100 : {Pythagorean(100)}")


# 10\. **Normalization of a N-dimensional vector**
# 
# Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).

# In[39]:


print("\n--- 10. Normalization of a N-dimensional vector ---\n")

import math

def normalization(vector):
    norm = math.sqrt(sum(x**2 for x in vector))

    if norm == 0:
        return "Error"

    normalized_vector = tuple(x/norm for x in vector)

    return normalized_vector

v1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("For the vector :", v1, "\n==> Normalized Vector:", normalization(v1), "\n")
v2 = (1, 2)
print("For the vector :", v2, "\n==> Normalized Vector:", normalization(v2), "\n")
v3 = (10.7, 2.5, 8.4)
print("For the vector :", v3, "\n==> Normalized Vector:", normalization(v3), "\n")


# 11\. **The Fibonacci sequence**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using only `for` or `while` loops.

# In[23]:


print("\n--- 11. The Fibonacci sequence ---\n")

def Fibonacci(nb):
    list_Fibonacci = [0, 1]
    while len(list_Fibonacci) < nb :
        list_Fibonacci.append(list_Fibonacci[-1]+list_Fibonacci[-2])
        
    return list_Fibonacci
   
print("Here is a list of the first 20 numbers in the Fibonacci sequence :", Fibonacci(20))

