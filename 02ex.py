import sys
import math
import timeit

#exercise 1
print('Exercise 1')

x = 5

def f_modified(alist): 
    new_list = alist.copy()
   
    for i in range(x):
        new_list.append(i) 
    return(new_list)

alist = [1, 2, 3]

print('Modified list:', f_modified(alist))
print('Original list:', alist)

print(' ')

#exercise 2
print('Exercise 2')

#ans_1 = list(map(lambda x: x*x, filter(lambda x: x%2 == 1, range(10))))
ans_2 = [x*x for x in range(10) if x%2==1]

print('Result using list comprehension:', ans_2)
print('')

#exercise 3
print('Exercise 3')

lis = ['ciao', 'come', 'stai', 'buongiorno']
num = 6

list_words = list(filter(lambda word: len(word) < num, lis))
print(list_words)
print(' ')

#exercise 4
print('Exercise 4')

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
list_keys = list(map(lambda x: len(x), lang))
print(list_keys)
print('')

#exercise 5
print('Exercise 5')

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

sorted_by_first = sorted(language_scores, key=lambda tup: tup[0])
print(sorted_by_first)
print('')

#exercise 6
print('Exercise 6')

def square(x):
    return x * x
def cube(x):
    return x * x * x
def power_6th(x):
    return( x*square(x)*cube(x))

print('6th power of 2: ', power_6th(2))
print(' ')

#exercise 7
print('Exercise 7')

def hello(function):
    def wrapper(x):
        print('Hello World!')
        print(function(x))
    return wrapper

@hello
def square(x):
    return x*x

square(4)
print(' ')

#exercise 8
print('Exercise 8')

recFib = lambda n: n if n <= 1 else recFib(n-1) + recFib(n-2)

print('Fibonacci sequence with recursive function:', [recFib(i) for i in range(1,21)])
print(' ')

#exercise 9
print('Exercise 9')

def loopFib(t):
    init = [1, 1]
    for j in range(2, t):
        init.append(init[j-1] + init[j-2])
    return init

time1 = timeit.timeit(lambda: loopFib(20), number=100)
time2 = timeit.timeit(lambda: recFib(20), number=100)

print('Execution time for Fibonacci iterative: ', time1)
print('Execution time for Fibonacci recursive: ', time2)
print("The iterative functione is more efficient:", int(time2/time1), 'faster')
               
print(' ')
        
#exercise 10
print('Exercise 10')

class polygon:
    x = []
    
    def __init__(self, components):
        self.x = components
        if len(self.x) < 3:
            raise Exception("Please enter at least 3 value")
    
    def getX(self, n):
        return self.x[n]
    
    def setX(self, n, xi): 
        if n < len(self.x):
            self.x[n] = xi
            
    def perimeter(self):
        p = sum(self.x)
        return p
    
    def getOrderedSides(self, increasing):
        if increasing == 'true':
            ordered_values = sorted(self.x)
        else:
            ordered_values = sorted(self.x, reverse = True)
        return ordered_values 
    
a = polygon([5, 3, 4])

print('Side length sorted: ',a.getOrderedSides('true'))
print('Side length reverse sorted: ',a.getOrderedSides('false'))
print('The perimeter is: ',a.perimeter())

print(' ')

#exercise 11
print('Exercise 11')

class rectangle(polygon): 
    
    def __init__(self, components):
        if len(components) == 4:
            self.x = components
            if (self.x[0] != self.x[1] or self.x[2] != self.x[3]):
                raise Exception("Error: correct format is (a, a, b, b)")
        else:
            print("Error: number of components is not 4")
        
    def area(self):
        return (self.x[1]*self.x[2])

b = rectangle([4, 4, 6, 6])
print('Area of rectangle is: ',b.area())



