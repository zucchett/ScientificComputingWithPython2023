##Global variables
def f(alist):
    x = 5
    a = [1, 2, 3]
    for i in range(x):
        a.append(i)
    return a

alist = [1, 2, 3]
print('List before calling the function: ', alist)
ans = f(alist)
print('Result of the function: ', ans)
print('List after calling the function: ', alist) # alist has not been changed

##List comprehension
print("\n")
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print('Result of the given expression: ', ans)

ans = [x*x for x in range(10) if x%2 == 1] 
print('Result of the list comprehension: ', ans)

##Filter function
print("\n")
string = input('Insert the words: ')
listvec = list(string.split(" "))
n = int(input('Insert the maximum length: '))

def shorter(x, maxlength):
     return len(x) < maxlength

print(f'The words shorter than {n} are', list(filter(lambda x: shorter(x, n), listvec)))



##Map dictionary
print("\n")
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def key_length(x):
    return len(x)

a = list(map(key_length, lang))
print('The keys lengths are ', a)



##Lambda functions
print("\n")
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = lambda pair: pair[0])
print('List of ordered tuples ', language_scores)



##Nested functions
print("\n")
x = float(input('Insert the value of x: '))

def square(x):
    return x*x

def cube(x):
    return x*x*x

def sixth(x):
    return square(cube(x))

print(f'The sixth power of {x} is', sixth(x))



##Decorators
print("\n")
def hello(func):
    def wrapper(x):
        print("Hello World!")
        func(x)
        return func(x)
    return wrapper
    
@hello
def square(x):
    return x*x

print(square(3))


##Fibonacci sequence (Part 2)
print("\n")
def rec_fib(x):
    y = []
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return rec_fib(x-1) + rec_fib(x-2)

print('Fibonacci sequence is', [rec_fib(i) for i in range(20)])

##Fibonacci sequence (Part 3)
print("\n")
import timeit

def recursiveFibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return rec_fib(x-1) + rec_fib(x-2)
  
def loopFibonacci(x):
    F0 = 0
    F1 = 1
    F = []
    F.append(F0)
    F.append(F1)
    for i in range(2,x):
        F.append(F[i-1] + F[i-2])
    return F
    
#%timeit loopFibonacci(20)
#%timeit recursiveFibonacci(20)

#7.74 µs ± 107 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
#6.92 ms ± 589 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)


##Class defintion
print("\n")
class polygon:
    #class attributes
    x = ()
    
    #defintion of the constructor
    def __init__(self, components):
        if len(components) == 3:
            self.x = components
        else:
            print('Error: number of components is not 3')
    
    #method to get the length of each side
    def getLength(self):
        l = []
        l = [self.x[i] for i in range(len(self.x))]
        return l
    
    #method to set the length of each side
    def setLength(self, n, xi):
        xlist = list(self.x)
        if n < len(xlist):
            xlist[n] = xi
        self.x = tuple(xlist)
        
    
    #method that returns the perimeter of the polygon
    def perimeter(self):
        p = 0
        for i in range(len(self.x)):
            p +=  self.x[i]
        return p
        
    #method that returns a tuple containing the length of the sides arranged in increasing or decreasing order
    #depending on the argument of the method
    #def getOrderedSides(self, boolean):
    def getOrderedSides(self, n):
        xlist = list(self.x)
        if n == True:
            xlist = sorted(xlist)
        elif n == False:
            xlist = sorted(xlist, reverse=True)
        self.x = tuple(xlist)
            

#creating an istance
a = polygon((3, 5, 2))

#calling the perimeter() method
print('the perimeter of the polygon is ', a.perimeter())

#calling getOrderedSides(increasing=True) method
a.getOrderedSides(True)
print('The lengths of the sides in increasing order are ', a.getLength())




##Class inheritance
print("\n")
class rectangle(polygon):
    
    def __init__(self, components):
        if len(components) == 4:
            temp = list(components)
            temp.sort()
            
            if ((temp.count(temp[0])) == 2) and ((temp.count(temp[2])) == 2):
                self.x = components
            else:
                print("Error: you should give 4 values (specifically two pairs of values) to define a rectangle")    
        else:
            print("Error: you should give 4 values (specifically two pairs of values) to define a rectangle")
            
    def area(self):
        return self.x[1]*self.x[0]
    

    
rec = rectangle((2,3,3,2))   
