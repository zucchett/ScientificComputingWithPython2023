#%% 1. Global variables

import copy

x = 5

def f(alist, x):
    anotherlist = copy.copy(alist)
    for i in range(x):
        anotherlist.append(i)
    return anotherlist

alist = [1, 2, 3]
print(f"alist before: {alist}")
anotherlist = f(alist, x)
print(f"anotherlist: {anotherlist}")
print(f"alist after: {alist}")

#%% 2. List comprehension

ans = [x * x for x in range(10) if x % 2 == 1]
print(ans)

#%% 3. Filter list

def filter_list(words_list, n):
    return list(filter(lambda word: len(word) < n, words_list))

a = ['aaa','bbbb','cc','ddddd','e']
b = 3
print(f"List: {a}")
print(f"n: {b}")
print(f"Final list: {filter_list(a, b)}")

#%% 4. Map dictionary

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def key_lengths(dictionnary):
    return list(map(len, dictionnary.keys()))

print(key_lengths(lang))

#%% 5. Lambda functions

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

sort_tuple = lambda tuple: tuple[0]

language_scores.sort(key=sort_tuple)
print(language_scores)

#%% 6. Nested functions

def square(number):
    return number**2

def cube(number):
    return number**3

def sixth_power(number):
    return cube(square(number))

n = 2
print(f"n = {n}")
print(f"n^6 = {sixth_power(n)}")

#%% 7. Decorators

def hello(func):
    def wrapper(x):
        print("Hello World!")
        return func(x)
    return wrapper

@hello
def square(x):
    return x*x

x = 5
result = square(x)
print(f"{x} * {x} = {result}")

#%% 8. The Fibonacci sequence (part 2)

def recursiveFibonacci(n):  #the first n numbers
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        f_list = recursiveFibonacci(n-1)  # previous elements
        f_list.append(f_list[-1] + f_list[-2])  # sum of the last to elements
        return f_list

print(recursiveFibonacci(20))

#%% 9. The Fibonacci sequence (part 3)

def loopFibonacci(n):
    f_list = []
    for n in range(20):
        if n == 0:
            f_list.append(0)
        elif n == 1:
            f_list.append(1)
        else:
            f_list.append(f_list[n-1]+f_list[n-2])
    return f_list

print(loopFibonacci(20))

import timeit

print(f"Loop Fibonacci: {timeit.timeit(lambda: loopFibonacci(20), number=1000)}")
print(f"Recursive Fibonacci: {timeit.timeit(lambda: recursiveFibonacci(20), number=1000)}")

# Using `for` or `while` loops provides the most efficient implementation.

#%% 10. Class definition

class polygon:

    def __init__(self, sides):
        if len(sides) < 3:
            raise ValueError("The tuple should contain at least 3 items")
        else:
            self.sides = sides
    
    def getSide(self, n):
        return self.sides[n]
    
    def setSide(self, n, new_length):
        if len(self.sides) < n+1:
            raise ValueError(f"The given n is too big")
        else:
            sides_list = list(self.sides)
            sides_list[n] = new_length
            self.sides = tuple(sides_list)

    def perimeter(self):
        return sum(self.sides)
    
    def getOrderedSides(self, increasing = True):
        return tuple(sorted(list(self.sides), reverse = not increasing))

hexagon = polygon((3,6,10,2,5,4))
print(f"Get side 3 : {hexagon.getSide(3)}")
hexagon.setSide(3, 1)
print(f"Get side 3 : {hexagon.getSide(3)}")
print(f"Get perimeter : {hexagon.perimeter()}")
print(f"Get ordered sides (increasing) : {hexagon.getOrderedSides()}")
print(f"Get ordered sides (decreasing) : {hexagon.getOrderedSides(False)}")

#%% 11. Class inheritance

class rectangle (polygon):

    def __init__(self, sides):
        if len(sides) != 4:
            raise ValueError("The tuple should contain exactly 4 items")
        elif (sides[0] != sides[2]) or (sides[1] != sides[3]):
            raise ValueError("The 1st and 3rd items, and the 2nd and 4th items should be equal")
        else:
            self.sides = tuple(sides)
    
    def area(self):
        return self.sides[0] * self.sides[1]
    
figure = rectangle((2,4,2,4))
print(f"Figure side 0: {figure.getSide(0)}")
print(f"Figure perimeter: {figure.perimeter()}")
print(f"Figure area: {figure.area()}")
