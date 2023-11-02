import timeit
from functools import reduce

###################1. Global variables####################
print("###################START 1. Global variables###################")
x = 5
def f(alist):
    alist = list(alist)
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed

###################2. List comprehension####################
print("###################START 2. List comprehension###################")
print_odd_squared = [i**2 for i in range(1,10,2)]
print(print_odd_squared) 

###################3. Filter list####################
print("###################START 3. Filter list###################")
def check_words(word, n):
    return len(word) < n

words = ['Write', 'a', 'Python', 'program', 'that', 'sorts', 'the', 'following', 'list', 'of', 'tuples', 'using', 'a', 'lambda', 'function']
n = 5
filtered_words = list(filter(lambda word: check_words(word, n), words))
print(filtered_words)

###################4. Map dictionary####################
print("###################START 4. Map dictionary###################")
def get_key_size(word):
    return len(word)

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
key_size_lsit = list(map(get_key_size, lang))
print(key_size_lsit)

###################5. Lambda functions####################
print("###################START 5. Lambda functions###################")
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key=lambda x: x[0])
print(language_scores)

###################6. Nested functions####################
print("###################START 6. Nested functions###################")

print("Number chosen: 3")
num = 3
square = lambda x: x**2
cube = lambda x: x**3
print("Number "+str(num)+" to the 6th power is: "+str(cube(square(num))))

###################7. Decorators####################
print("###################START 7. Decorators###################")

def hello(func): 
    def wrapper(arg):
        print("Hello World!")
        return func(arg) 
    return wrapper 

def square(x):
    return x**2

square = hello(square) 
result = square(2)
print(result)

###################8. The Fibonacci sequence (part 2)####################
print("###################START 8. The Fibonacci sequence (part 2)###################")

def fib_recursive(fib_old, fib_new, position, stop):
    if position <= stop:
        print(fib_old+fib_new)
        fib_old, fib_new = fib_new, fib_old+fib_new
        fib_recursive(fib_old, fib_new, position+1, stop)

fib_old = 0
fib_new = 1
position = 3
stop = 20
fib_recursive(fib_old, fib_new, position, stop)

###################9. The Fibonacci sequence (part 3)####################
print("###################START 9. The Fibonacci sequence (part 3)###################")

def fib_loops():
    fib_old = 0
    fib_new = 0
    for i in range(20):
        if i == 0:
            print(0)
        elif i == 1 or i == 2: 
            print(1)
            fib_old = 1
            fib_new = 1
        else:
            print(fib_new+fib_old)
            fib_old, fib_new = fib_new, fib_new+fib_old

timer_recursive = timeit.Timer(lambda: fib_recursive(0, 1, 3, 20))
timer_loop = timeit.Timer(lambda: fib_loops())

execution_time_recursive = timer_recursive.timeit(number=1)
execution_time_loop = timer_loop.timeit(number=1)

print("Recursive fib: "+str(timer_recursive.timeit(number=1)))
print("Loops fib: "+str(timer_loop.timeit(number=1)))
print("The recursive fib is "+str(100*((execution_time_recursive-execution_time_loop)/execution_time_loop))+"% faster")
print("Recursive in general is faster, although, because we are only calculating the 20 first numbers, the difference is not big and can even make fib done by loops the fastest.")

###################10. Class definition####################
print("###################START 10. Class definition###################")

class Polygon:
    def __init__(self, side_length):
        self.side_length = [i for i in side_length]
    
    def getSideLength(self):
        return self.side_length

    def perimeter(self):
        perimiter = 0
        for i in range(len(self.side_length)):
            perimiter += self.side_length[i]
        return perimiter
    
    def getOrderedSides(self, increasing=True):
        if increasing:
            self.side_length.sort()
            return self.side_length
        else:
            self.side_length.sort(reverse=True)
            return self.side_length
        
pentagon = Polygon((3,6,5,3,4))

print("Perimeter:", pentagon.perimeter())

print("Sides Length:", pentagon.getOrderedSides())
        
###################11. Class inheritance####################
print("###################START 11. Class inheritance###################")

class Rectangle(Polygon): # class 'Vector3D' inherits from class 'VectorND'
    
    # The constructor here is optional, and can be inherited from the parent class if omitted
    def __init__(self, side_length):
        if len(side_length) == 4:
            self.side_length = [i for i in side_length]
        else:
            print("Error: number of sides is not 4")
    
    def area(self):
        unique_sides = set(self.side_length)
        return reduce((lambda x, y: x * y), unique_sides)
    
rect = Rectangle((2,4,2,4))

print("Perimeter:", rect.perimeter())
print("Sides Length:", rect.getOrderedSides())
print("Area:", rect.area())