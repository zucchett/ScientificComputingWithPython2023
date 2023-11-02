#EXERCISE 1
print("\n")
def f(alist):
    x = 5
    alist = alist + [i for i in range(x)]
    return alist

alist = [1, 2, 3]
print("List before calling the function: ", alist)
print("Result of calling the function f(alist): ", f(alist))
print("List after calling the function: ", alist)
print("The function doesn't modify the original list")


#EXERCISE 2
print("\n")
ans = [i for i in map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))]
print(ans)

#alternative solution
ans = [x*x  for x in range(10) if x%2 == 1]
print(ans)


#EXERCISE 3
print("\n")
def listFilter(aList,n):
    listF = list(filter(lambda x: len(x) < n, aList))
    return listF

input_string = input("Insert a list of words separated by space: ")
n = int(input("Insert n: "))
myList = input_string.split(" ")
print(f'The elements of the list less than {n} are',listFilter(myList,n))


#EXERCISE 4
print("\n")
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def keyLen(aDict):
    return list( map(lambda x: len(x), lang.keys()) ) 

print("Lengths of the keys: ", keyLen(lang))

#EXERCISE 5
print("\n")
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key = lambda pair: pair[0])
print(language_scores)

#EXERCISE 6
def square(x):
    return x**2

def cube(x):
    return x**3

def power6(x):
    return square(cube(x))
    
n = input("Insert a number to raise to the 6th power: ")
print("The number raised to the 6th power",power6(int(n)))


#EXERCISE 7

def hello(func):
    def wrapper(x):
        func(x)
        print("Hello World!")
        return(func(x))
    return wrapper

@hello
def square(x):
    return x*x

print(square(2))


#EXERCISE 8
print("\n")
def fibRec(n):
    if (n == 0):
        return n
    elif (n == 1):
        return n
    
    else:
        return fibRec(n-1) + fibRec(n-2)

fibRecSeq = [fibRec(i) for i in range(20)]
print("Calculate the first 20 numbers of the Fibonacci sequence using a recursive function",fibRecSeq)


#EXERCISE 9
print("\n")
import timeit

def fibLoop(n):
    fibSeq = [ i for i in range(0,n)]
    for i in range(2,20):
        fibSeq[i] = fibSeq[i-1] + fibSeq[i-2]
    return fibSeq

def fibRec(n):
    if (n == 0):
        return n
    elif (n == 1):
        return n
    
    else:
        return fibRec(n-1) + fibRec(n-2)
        
setupLoop = """def fibLoop(n):
    fibSeq = [ i for i in range(0,n)]
    for i in range(2,20):
        fibSeq[i] = fibSeq[i-1] + fibSeq[i-2]
    return fibSeq
"""
stmtLoop = """fibLoop(20)"""

timeLoop = timeit.timeit(stmt = stmtLoop, setup = setupLoop, number = 1)

setupRec = """def fibRec(n):
    if (n == 0):
        return n
    elif (n == 1):
        return n
    
    else:
        return fibRec(n-1) + fibRec(n-2)
"""

stmtRec = """fibRec(20)"""

timeRec = timeit.timeit(stmt = stmtRec, setup = setupRec, number = 1)

print("The time for the execution of the Fibonacci code sequence using loop is: ",  timeLoop)
print("The time for the execution of the Fibonacci code sequence using rec is: ",  timeRec)

"""
The most efficient implementation is the Fibonacci code sequence with loop. In fact, the time for the execution of the Fibonacci with the loop is in the order of 10^-5, for the one with the recursive algorithm is in the order of 10^-2.
"""

#EXERCISE 10

import math
class polygon:
    '''This is a comment that is supposed to describe the purpose of the class'''

    x = ()

    # Definition of the Constructor
    #def __init__(self, lengths):
     #   self.x = lengths


    def __init__(self, lengths):
        if len(lengths) > 2:
            self.x = lengths
        else:
            print("Not valid argument, you have to put at least 3 sides")

    def getLen(self, n): # n is the component index
        print(self.x[n])

    def setLen(self, n, xi): # n is the component index, and xi is the value
        y = list(self.x)
        if n < len(y):
            y[n] = xi
        self.x = tuple(y)

    def perimeter(self):
        per = 0
        for i in range(len(self.x)):
            per += self.x[i]
        return print(per)

    def getOrderedSides(self,increasing = True):
        y = list(self.x)
        y.sort(reverse = True)

        if increasing == False:
            y.sort(reverse = True)
        
        self.x = tuple(y)
        return self.x

    

#testing the class
a = polygon((3, 19, 8, 3))
print("The perimeter is: ")
a.perimeter()
a.setLen(3,10)
print("The new perimeter is: ")
a.perimeter()
print("Ordered sides: ", a.getOrderedSides(increasing = True))

class rectangle(polygon):
    def __init__(self, lengths):        
        if len(lengths) == 4:
            y = list(lengths) 
            y.sort()

            if(((y.count(y[0])) == 2) and (y.count(y[3])) == 2):
                self.x = tuple(y)
            else:
                print("Error: it's not a rectangle!")
            
        else:
            print("Error: number of components is not 3")

    def area(self):
        return print(self.x[0]*self.x[3] )

#testing the class
print("Insert the rectangle sides")
l1 = int(input("l1= "))
l2 = int(input("l2= "))
l3 = int(input("l3= "))
l4 = int(input("l4= "))

rect = rectangle((l1,l2,l3,l4))
print("The area of the rectangle: ")
rect.area()
print("The area of the rectangle: ")
rect.perimeter()



