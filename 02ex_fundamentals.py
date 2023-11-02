########## Q1

import copy
x = 10
print(f"Gloabal x {x} before f")
def f(changed_list, x): 
    changed_list2 = copy.deepcopy(changed_list)    
    x = x + 5
    print("Local x : ",x) 
    for i in range(x):
        changed_list2.append(i)
    return changed_list2
original_List = [1, 2, 3]
print(f"Original List : {original_List} before f")  # before using f
changed_List = f(original_List, x)
print(f"Original List : {original_List} after f") # original list has been changed after used f
print("Changed List  : ", changed_List)
print(f"Gloabal x {x} after f")


########## Q2

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)
liste = [x*x for x in range(10) if x%2==1]
print(liste)


########## Q3

words_list = ["banana", "apple", "strawberry", "melon", "Daniel", "Alessandro", "John", "Stephan", "Anna", "Mia", "Valerio"]
number = 6
def fu(words_list,number):
    filtered_list = list(filter(lambda word: len(word) < number, words_list))
    return filtered_list
print(fu(words_list,number))  


########## Q4

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
def fun(lang):
    keys = list(lang.keys())
    print(type(keys))
    print(keys)
    length_keys = [len(keys[i]) for i in range(len(keys))]
    print(length_keys)
    liste = list(map(lambda x, y: (x, y), keys, length_keys))
    return liste

fun(lang)


########## Q5

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda x: x[0])
print(language_scores)
for language, score in language_scores:
    print(f'{language}: {score}')



########## Q6

def sq(x):
    return x**2
def cub(x):
    return x**3
def power_of_six2(x):
    return x**6
def power_of_six3(x):
    return cub(x)**2
def power_of_six4(x):
    return sq(x)**3

def square(x):
    def cube(x):
        sonuc = x**3
        return sonuc
    sonuc = (cube(x))**2
    return sonuc

number = 2
print(sq(number))
print(cub(number))
print(power_of_six2(number))
print(power_of_six3(number))
print(power_of_six4(number))
print(square(number))


########## Q7

def hello(function):
    def wrapper(*args,**kwargs):
        result = function(*args,**kwargs)
        print("Hello World!")
        return result
    return wrapper

@hello
def square(liste):
    result = []
    for i in liste:
        result.append(i**2)
    return result
@hello
def cube(x):
    return x**3
@hello
def summary(x,y):
    return x+y

print(square(range(3,14)))
cube(3)
print(summary(33,44))


########## Q8

def fibbo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibbo(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

n = 20
result = fibbo(n)
print(result)



########## Q9

import timeit

def loopFibonacci(n):
    result = [0, 1]
    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])
    return result

def recursiveFibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = recursiveFibonacci(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

# Measuring time using timeit
n = 20
print("Time taken for calculation using a loop:")
print(timeit.timeit("loopFibonacci(n)", globals=globals(), number=1000))

print("Time taken for calculation using recursion:")
print(timeit.timeit("recursiveFibonacci(n)", globals=globals(), number=1000))



########## Q10


class Polygon:
    def __init__(self, sides):
        if len(sides) < 3:
            raise ValueError("A polygon must have at least 3 sides")
        self.sides = list(sides)

    def get_sides(self):
        return self.sides

    def set_sides(self, sides):
        if len(sides) < 3:
            raise ValueError("A polygon must have at least 3 sides")
        self.sides = list(sides)

    def perimeter(self):
        return sum(self.sides)

    def get_ordered_sides(self, increasing=True):
        sorted_sides = sorted(self.sides) if increasing else sorted(self.sides, reverse=True)
        return tuple(sorted_sides)

# Test the Polygon class
polygon = Polygon((4, 5, 6))
print("Sides:", polygon.get_sides())
print("Perimeter:", polygon.perimeter())
print("Ordered Sides (Increasing):", polygon.get_ordered_sides(increasing=True))
print("Ordered Sides (Decreasing):", polygon.get_ordered_sides(increasing=False))


######### Q11

class Polygon:
    def __init__(self, sides):
        if len(sides) < 3:
            raise ValueError("A polygon must have at least 3 sides")
        self.sides = list(sides)

    def get_sides(self):
        return self.sides

    def set_sides(self, sides):
        if len(sides) < 3:
            raise ValueError("A polygon must have at least 3 sides")
        self.sides = list(sides)

    def perimeter(self):
        return sum(self.sides)

    def get_ordered_sides(self, increasing=True):
        sorted_sides = sorted(self.sides) if increasing else sorted(self.sides, reverse=True)
        return tuple(sorted_sides)

class Rectangle(Polygon):
    def __init__(self, length, width):
        # Ensure that a rectangle has exactly 4 sides
        super().__init__([length, width, length, width])
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Test the Rectangle class
rectangle = Rectangle(5, 8)
print("Sides of Rectangle:", rectangle.get_sides())
print("Perimeter of Rectangle:", rectangle.perimeter())
print("Area of Rectangle:", rectangle.area())



