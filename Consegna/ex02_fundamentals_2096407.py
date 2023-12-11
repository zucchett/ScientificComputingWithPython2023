# Riccardo Principe 2096407 Homework2
# EXERCISE 1A
print('\n' + 'Exercise 1A' + '\n')
x = 5

def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed
#print(id(alist),id(ans))

# EXERCISE 1B
print('\n' + 'Exercise 1B' + '\n')
def f(alist):
    x = 5
    alist = alist + [i for i in range(x)]
    return alist

alist = [1, 2, 3]
print("List before function: ", alist)
print("List after function: ", f(alist))

print('-------------------------------' + '\n')

# EXERCISE 2
print('\n' + 'Exercise 2' + '\n')
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)
l = [x**2 for x in range(10) if x % 2 == 1]
print(l)

print('-------------------------------' + '\n')

# EXERCISE 3
print('\n' + 'Exercise 3' + '\n')
def shorter_than(l, n):
    filtered_words = list(filter(lambda word: len(word) < n, l))
    return filtered_words


l = ["apple", "banana", "cherry", "date", "elderberry"]
n = 6
result = shorter_than(l, n)
print(result)

print('-------------------------------' + '\n')

# EXERCISE 4
print('\n' + 'Exercise 4' + '\n')
def map_dictionary(dict):
    return len(dict)
    
    
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
x = list(map(map_dictionary,lang))
print(x)

print('-------------------------------' + '\n')


# EXERCISE 5
print('\n' + 'Exercise 5' + '\n')
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
x = []
for i in language_scores:
    x.append(i[0])

ordering = lambda k : sorted(k)
x = ordering(x)
print(x)

print('-------------------------------' + '\n')

# EXERCISE 6
print('\n' + 'Exercise 6' + '\n')
def give_square(x):
    return x**2

def give_cube(x):
    return x**3

def give_six(x):
    return give_square(give_cube(x))

n = 2
print(give_six(n))

print('-------------------------------' + '\n')

# EXERCISE 7
print('\n' + 'Exercise 7' + '\n')
# Define the decorator
def hello(func):
    def wrapper(*args, **kwargs):
        print("Hello World!")
        return func(*args, **kwargs)
    return wrapper

# Use the decorator
@hello
def square(x):
    return x * x

# Test the decorated function
result = square(5)  # This will print "Hello World!" and calculate the square
print("Result:", result)

print('-------------------------------' + '\n')

# EXERCISE 8
print('\n' + 'Exercise 8' + '\n')
def fibonacci_rec(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return fibonacci_rec(x-1)+fibonacci_rec(x-2)

for i in range(0,21,1):
    print(fibonacci_rec(i))
    
print('-------------------------------' + '\n')
    
# EXERCISE 9
print('\n' + 'Exercise 9' + '\n')
import timeit

def recursiveFibonacci(n):
    if n <= 1:
        return n
    return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)


def loopFibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Measure the execution time of the recursive Fibonacci function for n=20
recursive_time = timeit.timeit("recursiveFibonacci(20)", globals=globals(), number=1000)

# Measure the execution time of the iterative Fibonacci function for n=20
iterative_time = timeit.timeit("loopFibonacci(20)", globals=globals(), number=1000)

print("Execution time for recursiveFibonacci(20):", recursive_time)
print("Execution time for loopFibonacci(20):", iterative_time)

print('-------------------------------' + '\n')

# EXERCISE 10
print('\n' + 'Exercise 10' + '\n')
import math

class Polygon:
    x = []
    
    def __init__(self, components):
        for i in range(len(components)):
            self.x.append(components[i])
    
    def setLength(self,n,xi):
        if n < len(self.x):
            self.x[n] = xi
            
    def getLength(self,n):
        return self.x[n]
    
    def perimeter(self):
        return sum(self.x)
    
    def getOrderedSides(self,increasing = True):
        self.x.sort(reverse=not(increasing))
        return tuple(self.x)
# END OF THE CLASS
p = Polygon((3,4,5,1))
print(p.perimeter())
print(p.getOrderedSides(False))

print('-------------------------------' + '\n')

# EXERCISE 11
print('\n' + 'Exercise 11' + '\n')
class Rectangle(Polygon):
    def __init__(self, components):
        if len(components) == 2:
            for i in range(len(components)):
                self.x.append(components[i])
                self.x.append(components[i])
        else:
            print('Error: number of components is not 2')
    
    def area(self):
        return self.x[0]*self.x[2]

r = Rectangle((3,4))
print(r.area())
print(r.perimeter())