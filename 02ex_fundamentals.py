import numpy
import sys
import math
import copy
import timeit

#Global variables
print("*****************************************")
print("Global variables")
print("*****************************************")

x = 5

def f(alist):
    list = copy.copy(alist)
    for i in range(x):
        list.append(i)
    return list

alist = [1, 2, 3]
ans = f(alist)
print("ans: ",ans)
print("alist: ",alist) # alist has NOT been changed
print("\n")

#List comprehension
print("*****************************************")
print("List comprehension")
print("*****************************************")

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)

sol = [x*x for x in range(10) if x % 2 == 1]
print(sol)
print("\n")

#Filter list
print("*****************************************")
print("Filter list")
print("*****************************************")

def is_min(words, n):
    return list(filter(lambda x: len(x) < n, words))

l = ['ciao','ciaoo','ciaoooooooo']
n = 5
print(is_min(l,n))
print("\n")

#Map dictionary
print("*****************************************")
print("Map dictionary")
print("*****************************************")

def s_len(s):
    x = list(map(lambda t: len(t), s.keys()))
    return x

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print("length of the keys of the dictionary ",s_len(lang))
print("\n")

#Lambda functions
print("*****************************************")
print("Lambda functions")
print("*****************************************")


language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda x: x[0])
print(language_scores)
print("\n")

#Nested functions
print("*****************************************")
print("Nested functions")
print("*****************************************")

#First function that returns the square of the number given as parameter
def square(n):
    return n**2

#Second function that returns the cube of the number given as parameter
def cube(n):
    return n**3

a = 2
#test of the two functions
print("Square",square(a))
print("Cube", cube(a))
#nested function using the two previous functions
print("6th power", square(cube(a)))

print("\n")


#Decorators
print("*****************************************")
print("Decorators")
print("*****************************************")

def hello(func):
    def wrapper(x):
        func(x)
        print("Hello World!")
    return wrapper

@hello
def square(x):
    print("Square of the number: ",x**2)
    return x**2

a = 4 #test the implemented function by computing this numer square
square(a) #call the function


print("\n")

#The Fibonacci sequence (part 2)
print("*****************************************")
print("The Fibonacci sequence (part 2)")
print("*****************************************")


def rec_fib(x):
    if(x==0): return 1
    if(x==1): return 1
    return rec_fib(x-1)+rec_fib(x-2)

def recursiveFibonacci(y):
    for i in range(0,y):
        print(rec_fib(i))

recursiveFibonacci(20)
print("\n")

#The Fibonacci sequence (part 3)
print("*****************************************")
print("The Fibonacci sequence (part 3)")
print("*****************************************")

#Fibonacci iterative
def loopFibonacci(x):
    list = []
    x = 0
    y = 1

    for i in range(0,x):
        num = x+y
        list.append(num)
        y = x
        x = num
    return list

#Fibonacci recursive
def rec_fib(x):
    if(x==0): return 0
    if(x==1): return 1
    return rec_fib(x-1)+rec_fib(x-2)

def recursiveFibonacci(y):
    for i in range(0,y):
        rec_fib(i)

def test(n):
    return sum(range(n))

n = 20
loop = 100

result = timeit.timeit('loopFibonacci(20)', globals=globals(), number=loop)
print("time for loopFibonacci (in seconds): ",result/loop)
result = timeit.timeit('recursiveFibonacci(20)', globals=globals(), number=loop)
print("time for recursiveFibonacci (in seconds): ",result/loop)
print("\n")
#the best implementation is the iterative one that consent to achieve the result with way less of time
#compared with the recoursive one

#Class definition
print("*****************************************")
print("Class definition")
print("*****************************************")

class polygon:
    x = []
    def __init__(self, components):
        self.x = components

    def getX(self, n): # n is the component index
        return self.x[n]
    
    # This function allows to set individial elements of the 'x' attribute 
    def setX(self, n, a): # n is the component index, and x is the value
        if n < len(self.x):
            self.x[n] = a
    
    #Function that returns the perimeter of the polygon by computing the sum of the length of each side
    def perimeter(self):
        sum = 0
        for i in range(0,len(self.x)):
            sum = sum + self.x[i]
        return sum

    #Function that returns an ordered tuple containing length of the sides
    def getOrderedSides(self,increasing):
        if(increasing == True):
            (self.x).sort()
        if(increasing == False):
            (self.x).sort()
            (self.x).reverse()
        return self.x

#test of the class and methods
poly = polygon([1,2,3])
per = poly.perimeter()
print("Perimeter: ",per)
print("Length of the sides: ",poly.getOrderedSides(False))

print("\n")


#Class inheritance
print("*****************************************")
print("Class inheritance")
print("*****************************************")

#definition of the class
class rectangle(polygon):
    #Function that returns the rectangle's area
    def area(self):
        a = (self.getX(0)*self.getX(1)) #procuct of the two dimensions
        return a

#test of the class and method
rect = rectangle([2,2])
print(rect.area())
