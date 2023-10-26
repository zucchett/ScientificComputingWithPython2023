print("\nExercise 1\n")

'''
1\. **Global variables**

Convert the function $f$ into a function that doesn't use global variables and that does not modify the original list
'''

x = 5

def f(alist):
    alist = [1, 2, 3]
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist)





print("\nExercise 2\n")
'''
2\. **List comprehension**

Write the following expression using a list comprehension:

`ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))`
'''


ans = [x*x for x in range(10) if x % 2 == 1] 
print(ans)

print("\nExercise 3\n")
'''
3. Filter list

Using the filter() hof, define a function that takes a list of words and an integer n as arguments, and returns a list of words that are shorter than n.
'''
from functools import partial

n=4
def is_short_n(words,n):
	
    
	return len(words)<n

words = ["python", "c++", "java", "ruby", "c#" ]
print(list(filter(lambda x: is_short_n(x, n), words)))



print("\nExercise 4\n")
'''
4\. **Map dictionary**


Consider the following dictionary:

`lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}`

Write a function that takes the above dictionary and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary.
'''





lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def length_key(*lang):
	length = []
	
	
	
	for key, value in lang:
		length.append(len(key))
	return length
x = list( map(length_key,lang.items()) ) 
print(x)	

print("\nExercise 5\n")
'''
5. Lambda functions

Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

Hint: use the method sort() and its argument key of the list data structure.

'''
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
addit = lambda x: sorted(x)
print(addit(language_scores))
print("\nExercise 6\n")
'''
6. Nested functions

Write two functions: one that returns the square of a number, and one that returns its cube.

Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.
'''

def square(x):    
    return x * x

def cube(x):    
    return x * x * x

def sixth_pow(a, b, n):	
	print(a(n)*b(n)*n)
n =2
sixth_pow(square,cube,n)

print("\nExercise 7\n")
'''
7. Decorators

Write a decorator named hello that makes every wrapped function print “Hello World!” each time the function is called.

The wrapped function should look like:

@hello
def square(x):
    return x*x

'''
def hello(func):
	def wrapper():
		print("Before")
		func()
		print("After")
	return wrapper


@hello
def say_hello():
	print("Hello World!")
say_hello()
print("\nExercise 8\n")
'''
8. The Fibonacci sequence (part 2)

Calculate the first 20 numbers of the Fibonacci sequence using a recursive function.

'''
lisst = []
def recursiveFibonacci(x):
	

    if x <=1:	
        return 1

		
    return recursiveFibonacci(x - 1)+recursiveFibonacci(x-2)
	

	
fib_num = []
for i in range(0,20):
    fib_num.append(recursiveFibonacci(i))
print(fib_num)

print("\nExercise 9\n")
'''
9. The Fibonacci sequence (part 3)

Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only for and while loops.

Measure the execution code of the two functions with timeit (link to the doc), for example:

%timeit loopFibonacci(20)

%timeit recursiveFibonacci(20)

which one is the most efficient implementation? By how much?

'''
import timeit

def loopFibonacci(n):
    if n <= 1:
        return n
    
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[-1] + fib[-2])
    return fib[n]

starttime = timeit.default_timer()
print("The start time is :",starttime)
loopFibonacci(20)
print("The time difference is :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
print("The start time is :",starttime)
recursiveFibonacci(20)
print("The time difference is :", timeit.default_timer() - starttime)



print("\nExercise 10\n")
'''
10. Class definition

Define a class polygon. The constructor has to take a tuple as input that contains the length of each side. The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.

    Create appropriate methods to get and set the length of each side

    Create a method perimeter() that returns the perimeter of the polygon

    Create a method getOrderedSides(increasing = True) that returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method

Test the class by creating an instance and calling the perimeter() and getOrderedSides(increasing = True) methods.
'''


import math
class polygon:
	def __init__(self, components):
		self.x = components # a list is expected as input


	def getLength(self):
		return len(self.x)
	def setLength(self, n,xi):
		if n< len(self.x):
			self.x[n] = xi
	def perimeter(self):
		

		sum_polygon = sum(self.x)
		print("Perimeter is",sum_polygon)
	def getOrderedSides(self,increasing):
		if increasing==True:
			print("Ascending order:",tuple(sorted(self.x,reverse=False)))
		else:
			print("Descending order:",tuple(sorted(self.x,reverse=True)))

	
length = polygon([1,2,3,6,4])
print("The length of the polygon:",length.getLength())
length.perimeter() 
length.getOrderedSides(True)


print("\nExercise 11\n")

'''
11. Class inheritance

Define a class rectangle that inherits from polygon. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.

    Create a method area() that returns the area of the rectangle.

Test the rectangle class by creating an instance and passing an appropriate input to the constructor.


'''



class rectangle(polygon): # class 'Vector3D' inherits from class 'VectorND'
    
    # The constructor here is optional, and can be inherited from the parent class if omitted
    def __init__(self, components):
        if len(components) == 4 and sorted(components)[0] == sorted(components)[1] and sorted(components)[2] == sorted(components)[3] :
            self.x = components # a list is expected as input
           
        else:
            print("Error: number of components is not 4 or it is not rectanle")
    
    # New methods that only belong to the child class
    def area(self):
        print("Area of rectangle:",sorted(self.x)[0] * sorted(self.x)[-1])


rectangle = rectangle([3,1,1,3])
rectangle.area()
