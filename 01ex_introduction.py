#!/usr/bin/env python
# coding: utf-8

# In[8]:


# The Hello World replacement

n = 100

# support list
whore_list = []

# It prints and it adds elements to the list
for i in range(1, n+1):
    if ((i%3 == 0) and (i%5 == 0)): 
        print("HelloWorld")
        whore_list.append("HelloWorld")
    elif (i%3 == 0):
        print("Hello")
        whore_list.append("Python")
    elif (i%5 == 0):
        print("World")
        whore_list.append("Works")
    else:
        print(i)
        whore_list.append(i)
    
# It makes the tuple and it prints its elements
cool_tuple = tuple(whore_list)
print(cool_tuple)



# In[13]:


# The swap

x = input("Please enter something for x: ")

# y is only a name and it has the same memory location of x
y = x

x = input("Please enter something for y: ")

print("After the swap:")
print("x = " + x)
print("y = " + y)


# In[23]:


# Computing the distance

import math

u = (3, 0)
v = (0, 4)

x = (v[0] - u[0])
y = (v[1] - u[1])

d = math.sqrt(pow(x,2) + pow(y,2))

print("The euclidean distance between u and v is " + str(d))


# In[6]:


# Counting letters

s = "sono indietro con l'università ma almeno faccio colpo con le tipe"
size = len(s)

# empty dictionary
s_dict = {}

# for every character
for i in range(0, size):
    # search in the dic
    if s[i] in s_dict:
        # if there is add 1 to the counter
        s_dict[s[i]] = s_dict[s[i]] + 1
    # else add to the dic and set the counter to 1
    else:
        s_dict[s[i]] = 1
        
# prints the dictionary
print(s_dict)


# In[14]:


# Isolating the unique 

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

# empty dictionary
s_dict = {}
# size of the list
size = len(l)

# for every number
for i in range(0, size):
    # search in the dic
    if l[i] in s_dict:
        # if there is add 1 to the counter
        s_dict[l[i]] = s_dict[l[i]] + 1
    # else add to the dic and set the counter to 1
    else:
        s_dict[l[i]] = 1
        
# counts the keys that have 1 as value
# counter
c = 0
# every element of the dictionary must correspond to every element of the list
# so if I check the value corresponding to the element of the list I can find 
# the unique numbers
for i in range(0, size):
    if s_dict[l[i]] == 1:
        c = c + 1
        
print("The number of numbers with only one occurrence is ", c)


# In[46]:


# Casting

x = input("Please enter something for x: ")
y = input("Please enter something for y: ")

try:
  s = int(x) + int(y)
  print(s)
except ValueError:
  try:
    s = float(x) + float(y)
    print(s)
  except ValueError:
    print("The sum of x and y can't be performed.")


# In[47]:


cubes = [pow(x,3) for x in range(10)]
print(cubes)


# In[49]:


a = [(i, j) for i in range(3) for j in range(4)]
print(a)


# In[69]:


n = 100

c_sq = [pow(c,2) for c in range(n)]

for i in range(3,n):
    for k in range(4,n):
        for z in range(n):
            if pow(i,2) + pow(k,2) ==  c_sq[z]:
                print(i, k, z)


# In[4]:


# Normalization of a N-dimensional vector

import math
v = [1, 5, 6, 8, 12]

s = 0
for i in range(len(v)):
    s = s + pow(v[i], 2)

leng = math.sqrt(s)

for i in range(len(v)):
    v[i] = round(v[i] / leng, 2)
    
print(v)

# check
check = 0
for i in range(len(v)):
    check = check + pow(v[i], 2)
    
check = round(check, 2)
    
print(check)


# In[18]:


# The Fibonacci sequence

n = 20

fir = 0
sec = 1

for i in range(n+1):
    if i == 0:
        print(i,0)
    elif i == 1:
        print(i,1)
    else:
        r = fir + sec
        print(i,r)
        fir = sec
        sec = r


# In[ ]:




