#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Task1
result_tuple = []

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        result_tuple.append("HelloWorld")
    elif i % 3 == 0:
        result_tuple.append("Hello")
    elif i % 5 == 0:
        result_tuple.append("World")
    else:
        result_tuple.append(str(i))
result_tuple = tuple([str(x).replace("Hello", "Python").replace("World", "Works") for x in result_tuple])
print(result_tuple)


# In[10]:


#Task2
x=input("Enter value for x: ")
y=input("Enter value for y: ")

x,y=y,x

print("After swapping: ")
print("x=", x)
print("y=", y)


# In[11]:


#Task3
import math

def distanceoftwopoints(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

pointa = (9, 6)
pointb = (4, 2)

distance= distanceoftwopoints(pointa, pointb)
print(f"distance between {pointa} and {pointb} is {distance}")


# In[12]:


#Task4


def countcharacters(input_string):
    input_string=input_string.lower()
    char_count={}
    for char in input_string:
        if char.isalpha():
            char_count[char] = char_count.get(char,0)+1
    return char_count

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

results1 = countcharacters(s1)
results2 = countcharacters(s2)

print("Character counts for s1:")
print(results1)

print("\nCharacter counts for s2:")
print(results2)


# In[13]:


#Task5
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
     85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
     1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
     45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

number_counts = {}
unique_numbers = set()

for number in l:
    number_counts[number] = number_counts.get(number, 0) + 1
    if number_counts[number] == 1:
        unique_numbers.add(number)

number_of_unique = len(unique_numbers)



# In[2]:


#Task6
x = input("first variable: ")
y = input("second variable: ")

try:
    z = x + y
    print(z)
except:
    print("you can not do it")


# In[14]:


#Task7
# a
loop=[]
for x in range(11):
   loop.append(x**3)
print(loop)

# b

listcomprehension=[x**3 for x in range(11)]
print(listcomprehension)


# In[3]:


#Task8
a=[(i,j) for i in range(3) for j in range (4)]
print(a)


# In[5]:


#Task9
pythagorean_triples = [(a, b, c) for a in range(1, 100) for b in range(a, 100) for c in range(b, 100) if a**2 + b**2 == c**2]


# In[15]:


#Task10
import math

def normalize(vector):
    squared_sum=sum(x**2 for x in vector)
    normalization_factor = math.sqrt(squared_sum)

    normalized_vector = tuple(x / normalization_factor for x in vector)

    return normalized_vector


# In[3]:


#Task11
#loop
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

result = fibonacci(20)
print(result)
#while
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

result = fibonacci(20)
print(result)


# In[ ]:





# In[ ]:




