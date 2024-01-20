#!/usr/bin/env python
# coding: utf-8

# You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a single dedicated `.py` file called `02ex_fundamentals.py`.
# 
# You can divide the individual exercises in the source code with appropriate comments (`#`).
# 
# The exercises need to run without errors with `python3 02ex_fundamentals.py`.

# 1\. **Global variables**
# 
# Convert the function $f$ into a function that doesn't use global variables and that does not modify the original list

# In[ ]:

print("****1.*************************************************************************")
import copy


def f(alist):
    
    copy_alist = copy.deepcopy(alist)
    x = 5
    for i in range(x):
        copy_alist.append(i)
    return copy_alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed


# 2\. **List comprehension**
# 
# Write the following expression using a list comprehension:
# 
# `ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))`

# In[ ]:

print("****2.*************************************************************************")
a=[i*i for i in range(10) if i % 2 == 1]
print(a)


# 3\. **Filter list**
# 
# Using the `filter()` hof, define a function that takes a list of words and an integer `n` as arguments, and returns a list of words that are shorter than `n`.

# In[ ]:

print("****3.*************************************************************************")
word_list=['aysima','merve','coskuner','ali']
k=6

def myFunc(x,n):
    if len(x)<n:
        return x

words=list(filter(lambda x: myFunc(x, k), word_list))

print(words)


# 4\. **Map dictionary**
# 
# 
# Consider the following dictionary:
# 
# `lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}`
# 
# Write a function that takes the above dictionary and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary.

# In[ ]:
print("****4.*************************************************************************")

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
def keylength(x):
    return len(x)

lang_length=list(map(keylength, lang.keys()))

print(lang_length)


# 5\. **Lambda functions**
# 
# Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:
# 
# `language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]`
# 
# *Hint*: use the method `sort()` and its argument `key` of the `list` data structure.

# In[ ]:

print("****5.*************************************************************************")
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda x: x[0]) 
print(language_scores)


# 6\. **Nested functions**
# 
# Write two functions: one that returns the square of a number, and one that returns its cube.
# 
# Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.

# In[ ]:

print("****6.*************************************************************************")
x=int(input("x: "))
def square(x):
    return x**2
def cube(x):
    return x**3
def sixthpower(x):
    return cube(square(x))
print(sixthpower(x))

    


# 7\. **Decorators**
# 
# Write a decorator named `hello` that makes every wrapped function print “Hello World!” each time the function is called.
# 
# The wrapped function should look like:
# 
# ```python
# @hello
# def square(x):
#     return x*x
# ```

# In[10]:

print("****7.*************************************************************************")
def hello(func):
    def wrapper(x):
        print("Hello World!")
        func(x)
        return func(x)
    return wrapper

@hello
def square(x):
    return x*x
print(square(9))


# 8\. **The Fibonacci sequence (part 2)**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using a recursive function.

# In[16]:

print("****8.*************************************************************************")
def nthFibonacci(n):
    if n <= 1:
        return 1
    else:
        return(nthFibonacci(n-1) + nthFibonacci(n-2))
    
def recursiveFibonacci(n):
    for i in range(n):
        print(nthFibonacci(i))
        nthFibonacci(i)

recursiveFibonacci(20)


# 9\. **The Fibonacci sequence (part 3)**
# 
# Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only `for` and `while` loops.
# 
# Measure the execution code of the two functions with `timeit` ([link to the doc](https://docs.python.org/3/library/timeit.html)), for example:
# 
# `%timeit loopFibonacci(20)`
# 
# `%timeit recursiveFibonacci(20)`
# 
# which one is the most efficient implementation? By how much?

# In[17]:
print("****9.*************************************************************************")

def loopFibonacci(n):
    firstnum=1
    secondnum=1
    sum=0
    count=1
    while (count<=n):
        count+=1
        firstnum=secondnum
        secondnum=sum
        sum=firstnum+secondnum 
        #print(sum)
        
loopFibonacci(20)


# In[19]:



print("loopFibonacci(20):943 ns ± 12.5 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)")


# In[20]:


print("recursiveFibonacci(20):2.24 ms ± 70.1 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)")


# In[ ]:


print("loopFibonacci is more efficient than recursiveFibonacci more than 2375 times")


# 10\. **Class definition**
# 
# Define a class `polygon`. The constructor has to take a tuple as input that contains the length of each side. The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.
# 
# - Create appropriate methods to get and set the length of each side
# 
# - Create a method `perimeter()` that returns the perimeter of the polygon
# 
# - Create a method `getOrderedSides(increasing = True)` that returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method
# 
# Test the class by creating an instance and calling the `perimeter()` and `getOrderedSides(increasing = True)` methods.

# In[1]:

print("****10.*************************************************************************")
class polygon:
    
    def __init__(self, sides_tuple): # Constructor
        
        if len(sides_tuple) < 3:
            raise Exception("input tuple should contain at least 3 items")
            
        self.sides_tuple = sides_tuple
        
    def getSide(self, item_order):
        if item_order>=len(self.sides_tuple):
            raise Exception("item order must be smaller than the length of tuple")
        return self.sides_tuple[item_order]
    
    def setSide(self, item_order, new_side):
        if item_order>=len(self.sides_tuple):
            raise Exception("item order must be smaller than the length of tuple")
        sides_list=list(self.sides_tuple)
        sides_list[item_order] = new_side
        self.sides_tuple=tuple(sides_list)
    
    def perimeter(self):
        return sum(self.sides_tuple)
    
    def getOrderedSides(self,increasing = True):
        sides_list=list(self.sides_tuple)
        
        if increasing:                    
            sides_list.sort()
            
        else:
            sides_list.sort(reverse=True)
            
        return tuple(sides_list)
        
        


# In[ ]:


sides= (3,5,4)
a=polygon(sides)


# In[ ]:
b=a.perimeter()
print(f"Perimeter: {b}")


# In[ ]:



c=a.getOrderedSides()


# In[ ]:


print(f"Ordered tuple : {c}")


# 11\. **Class inheritance**
# 
# Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.
# 
# - Create a method `area()` that returns the area of the rectangle.
# 
# Test the `rectangle` class by creating an instance and passing an appropriate input to the constructor.

# In[23]:

print("****11.*************************************************************************")
class rectangle(polygon):
    
        def __init__(self,sides_tuple): # Constructor            
            polygon.__init__(self, sides_tuple)
            
            if len(sides_tuple) != 4 or len(set(sides_tuple))!=2 :
                raise Exception("input tuple must contain 4 elements and they must be the same two by two ")
        def area(self):
            temp=list(set(self.sides_tuple))
            area=temp[0]*temp[1]
            
            return area
            
    


# In[24]:


rect_sides=(4,4,8,8)


# In[25]:


a=rectangle(rect_sides)


# In[26]:


b=a.area()
print(f"Area: {b}")

# In[ ]:




