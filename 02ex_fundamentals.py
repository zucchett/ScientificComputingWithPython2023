#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
def f(alist):
    x = 5 #jak nie globalnie to musi byc w funkcji lokalnie
    new_list = list(alist)
    for i in range(x):
        new_list.append(i)
    return new_list

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist)


# In[2]:


#2 ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))

ans = [x*x for x in range(10) if x%2==1]
print(ans)


# In[2]:


#3 Using the filter() hof, define a function that takes a list of words and an integer n as arguments, and returns a list of words that are shorter than n.

def fun(words, n):
    return list(filter(lambda word: len(word)<n, words))

w=['pudelko', 'kwncwioe', 'qoj']
x = fun(w,4)
print(x)


# In[6]:


#4 Consider the following dictionary: lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}Write a function that takes the above dictionary and uses the map() higher order function to return a list that contains the length of the keys of the dictionary.

def fun(dic):
    return list(map(lambda x: len(x[0]), dic.items()))

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print(fun(lang))


# In[7]:


#5 language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda x: x[0])
print(language_scores)


# In[8]:


#6
def squared(x):
    return x*x

def cubed(x):
    return x*x*x

def fun(x):
    return cubed(squared(x))
print(fun(2))


# In[9]:


#7

def hello(func):
    def inner(x):
        print("Hello World!")
        return func(x)
    return inner

@hello
def square(x):
    return x * x
    
print(square(4))


# In[2]:


#8
def fibonacci(x):
    if x<=1:
        return x
    else:
        return fibonacci(x-1)+fibonacci(x-2)
    
for i in range(20):
    print(fibonacci(i))


# In[7]:


import timeit

def recursive(n):
    if n <= 1:
        return n
    else:
        return recursive(n-1) + recursive(n-2)

def loop(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Measure the execution time for recursive Fibonacci
recursive_time = timeit.timeit("recursive(20)", globals=globals(), number=1000)

# Measure the execution time for loop Fibonacci
loop_time = timeit.timeit("loop(20)", globals=globals(), number=1000)

print(f"Recursive Fibonacci time: {recursive_time}")
print(f"Loop Fibonacci time: {loop_time}")

#When we're dealing with Fibonacci numbers, the recursive approach involves calling the function over and over again, and sometimes it ends up doing the same calculations multiple times. 
#The loop approach calculates each Fibonacci number one after the other, without going back and redoing things.
#Recursive Fibonacci time: 1.7372213000198826
#Loop Fibonacci time: 0.0021362000261433423


# In[8]:


#10
class Polygon:
    def __init__(self, side_lengths):
        if len(side_lengths) < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        
        self.sides = list(side_lengths)

    def get_sides(self):
        return self.sides

    def set_side(self, index, length):
        if 0 <= index < len(self.sides):
            self.sides[index] = length
        else:
            raise IndexError("Index out of range.")

    def perimeter(self):
        return sum(self.sides)

    def get_ordered_sides(self, increasing=True):
        return tuple(sorted(self.sides) if increasing else sorted(self.sides, reverse=True))

polygon = Polygon((10, 3, 1, 4))
print("Perimeter:", polygon.perimeter())
print("Ordered Sides (Increasing):", polygon.get_ordered_sides())
print("Ordered Sides (Decreasing):", polygon.get_ordered_sides(increasing=False))


# In[9]:


class Polygon:
    def __init__(self, side_lengths):
        if len(side_lengths) < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        
        self.sides = list(side_lengths)

    def get_sides(self):
        return self.sides

    def set_side(self, index, length):
        if 0 <= index < len(self.sides):
            self.sides[index] = length
        else:
            raise IndexError("Index out of range.")

    def perimeter(self):
        return sum(self.sides)

    def get_ordered_sides(self, increasing=True):
        return tuple(sorted(self.sides) if increasing else sorted(self.sides, reverse=True))


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])  # Assuming the order is top, right, bottom, left

    def area(self):
        return self.sides[0] * self.sides[1]


rectangle = Rectangle(5, 9)
print("Perimeter:", rectangle.perimeter())
print("Area:", rectangle.area())


# In[ ]:




