import timeit
print("ESERCIZIO 1") #ESERCIZIO 1

def f(alist):
    x = 5
    alist= []
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist)

print("ESERCIZIO 2") #ESERCIZIO 2

ans = [x*x for x in range(10) if x % 2 == 1]
print(ans)

print("ESERCIZIO 3") #ESERCIZIO 3

def function1(world,n):
    world_list = list(filter(lambda w: len(w) < n, world))
    return world_list

parole = ["ciao", "cane", "pos", "tre", "soleggiato"]
print(function1(parole, 4))

print("ESERCIZIO 4") #ESERCIZIO 4

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
x = list( map(lambda l: len(l), lang) )
print(x)

print("ESERCIZIO 5") #ESERCIZIO 5

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda x: x[0])
print(language_scores)

print("ESERCIZIO 6") #ESERCIZIO 6

def square(x):
    return x ** 2
def cube(x):
    return x ** 3
def power_six(x):
    return square(cube(x))
prova = 4
print(power_six(prova))

print("ESERCIZIO 7") #ESERCIZIO 7

def hello(func):
    def wrapper(*args, **kwargs):
        print("Hello World!")
        return func(*args, **kwargs)
    return wrapper

@hello
def square(x):
    return x*x

print(square(3))

print("ESERCIZIO 8") #ESERCIZIO 8

def recursiveFibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = recursiveFibonacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib


fibonacciex02 = recursiveFibonacci(20)
print(fibonacciex02)

print("ESERCIZIO 9") #ESERCIZIO 9

def loopFibonacci(n):
    fibonacciex01 = [0, 1]
    for i in range(2, n):
        next_fibonacci = fibonacciex01[i - 1] + fibonacciex01[i - 2]
        fibonacciex01.append(next_fibonacci)
    return fibonacciex01

recursive_time = timeit.timeit("recursiveFibonacci(20)", globals=globals(), number=1000)
loop_time = timeit.timeit("loopFibonacci(20)", globals=globals(), number=1000)

print("recursive time = ", recursive_time)
print("loop time = ", loop_time)
print("the loop implementation is more efficient, when i tested it running the codes it was more or less 44% faster than \nthe recursive implementation")

print("ESERCIZIO 10") #ESERCIZIO 10

class Polygon:
    def __init__(self, sides):
        if len(sides) < 3:
            raise ValueError("a polygon must have at least 3 sides")
        else:
            self.polygon_sides = list(sides)

    polygon_sides = []

    def set_side_length(self, index, length):
        if len(self.polygon_sides) > index and index >= 0:
            self.polygon_sides[index] = length
        else:
            raise ValueError("the index is wrong")

    def get_side_length(self, index):
        if len(self.polygon_sides) > index and index >= 0:
            return self.polygon_sides[index]
        else:
            raise ValueError("the index is wrong")

    def perimeter(self):
        return sum(self.polygon_sides)

    def get_ordered_sides(self, increasing=True):
        if increasing == True:
            sorted_sides = sorted(self.polygon_sides)
        elif increasing == False:
            sorted_sides = sorted(self.polygon_sides, reverse=True)
        return tuple(sorted_sides)

polygon = Polygon((7, 4, 5))
print("Perimeter:", polygon.perimeter())
print("Ordered Sides (increasing):", polygon.get_ordered_sides())

print("ESERCIZIO 11") #ESERCIZIO 11

class Rectangle(Polygon):
    def __init__(self, length, width):
        if len(length) != 2 or length[0] != length[1] or width[0] != width[1]:
            raise ValueError("Input data is not consistent with the properties of a rectangle")
        else:
            super().__init__(length + width)

    def area(self):
        return self.polygon_sides[0] * self.polygon_sides[2]


rectangle = Rectangle([4, 4], [3, 3])
print("Perimeter:", rectangle.perimeter())
print("Area:", rectangle.area())

