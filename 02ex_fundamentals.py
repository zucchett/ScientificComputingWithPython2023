##### EXERCISE 1 #####
print("\n##### 02ex_fundamentals #####")
print("\n##### EXERCISE 1 #####")
import copy

x = 5

def f(alist):
    # copy the input list to another object,
    # in such away to do not modify the 
    # original one
    newlist = copy.copy(alist)
    for i in range(x):
        newlist.append(i)
    return newlist

# input list
alist = [1, 2, 3] 

# computing the function
ans = f(alist)

# print the results
print("Original list:", alist, "with id:", id(alist)) 
print("Modified list:", ans, "with id:", id(ans))


input("\npress enter to go on...")



##### EXERCISE 2 #####
print("\n\n##### EXERCISE 2 #####")

# desired result
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
# computed result
vec = [x**2 for x in range(10) if x % 2 ==1]

# print the result
print("The desired result is:", ans)
print("The computed result is:", vec)


input("\npress enter to go on...")



##### EXERCISE 3 #####
print("\n\n##### EXERCISE 3 #####")

# input list
mylist = []
try:
    n = int(input("You want words shorter than: "))
    num = int(input("Enter number of elements : "))
    for i in range(0, num):
        print("Enter word", i+1,": ", end="")
        element = input()
        mylist.append(element)

    # function definition
    def shortList(mylist, n):
        """returns a list of words that are shorter than n"""
        
        # we should use a lambda function otherwise, we
        # should pass to filter function another function
        # ex:shortLength that accpets as inputs mylist and n,
        # but using filter we can pass only one input
        output = list(filter(lambda x: len(x) < n, mylist))
        return output

    # print the result        
    print("Selected words are:", shortList(mylist, n))
except:
    print("Please, enter consistent inputs")


input("\npress enter to go on...")



##### EXERCISE 4 #####
print("\n\n##### EXERCISE 4 #####")

# input dictionary
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

# function definition
def keyLength(dict):
    output = list(map(lambda x: len(x), dict))
    return output

# print result
print("The dictionary is:", lang)
print("key lengths are:", keyLength(lang))


input("\npress enter to go on...")



##### EXERCISE 5 #####
print("\n\n##### EXERCISE 5 #####")

# input list 
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

# using sorting
result1 = sorted(language_scores)
# sort does not return anything, so I cannot
# assign it to another variable
language_scores.sort(key = lambda x: x[0])

# print the results
print("Using sorted:", result1)
print("Using sort:", language_scores)


input("\npress enter to go on...")



##### EXERCISE 6 #####
print("\n\n##### EXERCISE 6 #####")

# square function
def getSquare(x):
    return x*x

# cube function
def getCube(x):
    return x*x*x

# sixth function 
def getSixth(x):
    return getSquare(getCube(x))

try:
    x = float(input("Enter a number: "))
    # print the results
    print("The square of", x, "is:", getSquare(x))
    print("The cube of", x, "is:", getCube(x))
    print("The sixth of", x, "is:", getSixth(x))
except:
    print("That value is not a number!")


input("\npress enter to go on...")



##### EXERCISE 7 #####
print("\n\n##### EXERCISE 7 #####")

def hello(func):
    # I sholud pass here the input value
    def wrapper(x):
        print("Hello World!")
        # remember to capture the return value
        result = func(x)
        return result
    return wrapper

# square function
@hello
def getSquare(x):
    return x*x

# cube function
@hello
def getCube(x):
    return x*x*x

# sixth function 
@hello
def getSixth(x):
    return getSquare(getCube(x))

# testing
try:
    x = float(input("Insert a value: "))
    # print the results
    print("The square of", x, "is:", getSquare(x))
    print("The cube of", x, "is:", getCube(x))
    print("The sixth of", x, "is:", getSixth(x))
except:
    print("Please, enter a number")


input("\npress enter to go on...")



##### EXERCISE 8 #####
print("\n\n##### EXERCISE 8 #####")

# define Fibonacci function
def fib_rec(x):
    if(x == 0):
        return 0
    elif(x == 1):
        return 1
    else:
        return fib_rec(x-1)+fib_rec(x-2)

# compute the first 20 Fibonacci numbers
mylist = []
for i in range(21):
    mylist.append(fib_rec(i))
    
# print the result
print("First 20 Fibonacci rumbers are:")
print(mylist)


input("\npress enter to go on...")



##### EXERCISE 9 #####
print("\n\n##### EXERCISE 9 #####")

import timeit

# ITERATIVE FIBONACCI
codes1 = """\
def fibonacci_iter(x):
    mylist = []
    for i in range(x+1):
        if i == 0:
            mylist.append(0)
        elif i == 1:
            mylist.append(1)
        else:
            mylist.append(mylist[i-1] + mylist[i-2])
    return mylist
fibonacci_iter(20)
"""""

# RECURSIVE FIBONACCI
codes2 = """\
def fib_rec(x):
    if(x == 0):
        return 0
    elif(x == 1):
        return 1
    else:
        return fib_rec(x-1) + fib_rec(x-2)
def recursiveFibonacci(x):
    mylist = []
    for i in range(x+1):
        mylist.append(fib_rec(i))
    return mylist  
recursiveFibonacci(20)
"""
    
# Measuering the executions
time1 = timeit.timeit(codes1, number = 100)
print("100 iterations using the iterative approch needs:", time1, "[sec]")
time2 = timeit.timeit(codes2, number = 100)
print("100 iterations using the recursive approch needs:", time2, "[sec]")

# print the results
if time1 > time2:
    print("The best approch is the recursive one, it needs", time1 - time2, "[sec] less for 100 iterations")
elif time1 < time2:
    print("The best approch is the iterative one, it needs", time2 - time1, "[sec] less for 100 iterations")
else:
    print("The two approch are equal, since they need the same amount of time ")


input("\npress enter to go on...")



##### EXERCISE 10 #####
print("\n\n##### EXERCISE 10 #####")

# class definition 
class polygon:
    
    """ class polygon """
    
    x = []
    
    # constructor: check if the input data are given
    # by a tuple and that it has at least three sides
    # at the end it creates the object
    def __init__(self, sides):
        if len(sides) < 3:
            print("A poligon has at least three sides!")
        elif type(sides) != tuple:
            print("Please, give me the sides using a tuple")
        else:
            self.x = list(sides)
     
    # return the side saved at position "index"
    def getSide(self, index):
        if index < 0 or index >= len(self.x):
            print("Index not valid!")
        else:
            return self.x[index]
    
    # set a side to a desidered value, using
    # its corresponding index, if valid
    def setSide(self, index, value):
        if index < 0 or index >= len(self.x):
            print("Index not valid!")
        else:
            self.x[index] = value
        
    # returns the number of sides of your polygon,
    # or 0 in the case it was not correctly defined
    def getSideNum(self):
        return len(self.x)
    
    # returns a list with all the sides 
    def returnSides(self):
        a = []
        for i in self.x:
            a.append(i)
        return a
    
    # returns the perimeter of the polygon 
    def perimeter(self):
        per = 0
        for i in self.x:
            per += i
        return per
    
    # returns a tuple containing the length 
    # of the sides arranged in increasing or 
    # decreasing order, depending on the 
    # argument
    def getOrderedSides(self, increasing = True):
        if increasing:
            a = sorted(self.x)
            return tuple(a)
        else:
            a = sorted(self.x, reverse = True)
            return tuple(a)
    
# testing
mylist = []

try:
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        print("Enter element", i+1,": ", end="")
        element = float(input())
        mylist.append(element) 
    mytuple = tuple(mylist)
    rect = polygon((mytuple))

    # print the results
    print("Origianl order of sides:", rect.returnSides())
    print("The perimeter is:", rect.perimeter())
    print("Ordered sides:", rect.getOrderedSides(increasing = True))
except:
    print("Please, enter consistent values")


input("\npress enter to go on...")



##### EXERCISE 11 #####
print("\n\n##### EXERCISE 11 #####")

# class 'rectangle' inherits from class 'polygon'
class rectangle(polygon): 
    
    # check that the given sides are exactly four
    # and that they are eqaul by couples
    def __init__(self, sides):
        # perfome a sort in order to check that
        # sides are eqaul by couples
        a = sorted(list(sides))
        if len(sides) != 4:
            print("Error: a rectangle has four sides")
        elif a[0] != a[1] or a[2] != a[3]:
            print("Error: a rectangle has couples of equal sides")
        else:
            self.x = list(sides)
            
    # returns the area of the rectangle        
    def area(self):
        a = sorted(self.x)
        return a[0]*a[3]
            
# testing
mylist = []
try:
    for i in range(0, 4):
        print("Enter side", i+1,": ", end="")
        element = float(input())
        mylist.append(element) 
    mytuple = tuple(mylist)
    rect = rectangle(mytuple)
    print("The area is", rect.area())
except:
    print("Something goes wrong...")
