# 02ex_fundamentals.py

# 1. Global variables 
print("1. Global variables \n")

x = 5

def f(alist):
    alist = alist.copy()
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has not been changed

# 2. List comprehension
print("\n 2. List comprehension \n")

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))) 
ans2 = [i**2 for i in range(10) if i % 2 == 1 ]
print(ans == ans2)

# 3. Filter list
print("\n 3. Filter list \n")

my_list = ["This", "is", "the", "best", "function"]

def g(x,n):
    if len(x) < n :
        return x

n=5 #testing

my_shorter_list = list(filter(lambda x: g(x,n), my_list))
print(my_shorter_list)

# 4. Map dictionary
print("\n 4. Map dictionary \n")

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
    
def keys_length(lang):
    return list(map(lambda i : len(i), lang))
    
print(keys_length(lang))

# 5. Lambda functions 
print("\n 5. Lambda functions \n")

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = lambda x: x[0])
print(language_scores)

# 6. Nested functions
print("\n 6. Nested functions \n")

def square(x):
    return x**2

def cube(x):
    return x**3

def f(x):
    return square(x)*cube(x)

print(f(5)) # testing

# 7. Decorators
print("\n 7. Decorators \n")

def hello(func):
    def wrapper(x):
        print("Hello World!")
        return func(x)
    return wrapper
    

@hello
def square(x):
    return x*x

#testing
print(square(5))

# 8. The Fibonacci sequence (part 2)
print("\n 8. The Fibonacci sequence (part 2) \n")

def recursive_fibonacci(num: int):
    if num > 1:
        return recursive_fibonacci(num-1) + recursive_fibonacci(num-2)
    elif num == 1:
        return 1
    elif num == 0:
        return 0
    
for i in range (21): 
    print(recursive_fibonacci(i))

# 9. The Fibonacci sequence (part 3)
print("\n 8. The Fibonacci sequence (part 3) \n")

import timeit

with_recursive_fibonacci = """  
def recursive_fibonacci(num: int):
    if num > 1:
        return recursive_fibonacci(num-1) + recursive_fibonacci(num-2)
    elif num == 1:
        return 1
    elif num == 0:
        return 0

  
for i in range(21): 
    print(recursive_fibonacci(i))
"""

print("time =", timeit.timeit(stmt=with_recursive_fibonacci, number=10)) #time for 10 loops

with_while_loop = """
count=0
n1=0
n2=1

while count<=20 :
    nth = n1 + n2
    print(n1)
    n1 = n2
    n2 = nth
    count+=1
"""

print("time =", timeit.timeit(stmt=with_while_loop, number=10)) #time for 10 loops

if timeit.timeit(stmt=with_recursive_fibonacci, number=1) > timeit.timeit(stmt=with_while_loop, number=1):
    print("The recursive function is faster")
else :
    print("The while loop is faster")


# 10. Class definition
print("\n 10. Class definition \n")

# define a class polygon
class polygon:

    x = []
    def __init__(self, components):
        if len(components) >= 3 :
            self.x = components
        else :
            print("That's not a polygon!")

    def getDimension(self): 
        return len(self.x)
    
    def getX(self, n): # n is the component index
        return self.x[n]
        
    def setX(self, n, xi): # n is the component index, and xi is the value
        if n < len(self.x):
            self.x[n] = xi

    def perimeter(self):
        return sum(self.x)

    def getOrderedSides(self, increasing):
        my_list =[]
        for i in range(len(self.x)):
            my_list.append(self.x[i])
            my_list.sort()
        if increasing == True :
            return tuple(my_list)
        else :
            return tuple(my_list[::-1]) 
            
# testing the class
a = polygon([2,8,4,5,6])

print("dimension", a.getDimension())
print("n-side length =", a.getX(2))
print("perimeter =", a.perimeter())
print("decreasing order sides->", a.getOrderedSides(False))
print("increasing order sides->", a.getOrderedSides(True))

# 11. Class inheritance
print("\n 11. Class inheritance \n")

class rectangle(polygon):

    x = []
    def __init__(self, components):
        if len(components) == 4 and (components[0] == components[2]) and (components[1] == components[3]) and (components[0]**2+components[1]**2 == components[2]**2+components[3]**2):
            self.x = components
        else :
            print("That's not a rectangle!")

    def area(self):
        if len(self.x) == 4 and self.x[0]*self.x[1] == self.x[2]*self.x[3] :
            return self.x[1]*self.x[2]
        else :
            return False


#testing
b = rectangle([2,3,2,3])
print("area =", b.area())

