#LAB 2
#ex1:
print("1 ------ Global variables ")

def f(blist,x):
    res = blist.copy()
    for i in range(x):
        res.append(i)
    return res

alist = [1, 2, 3]
ans = f(alist,5)
print(ans)
print(alist) # alist has been changed

#ex2:
print("2 ------  List comprehension")

ans2 = [x * x for x in range(10) if x % 2 == 1]
print(ans2)

#ex3:
print("3 ------  Filter list")

def shorter_than_n (lis,n):
    res = list(filter(lambda word: len(word) < n, lis))
    
    return res

print(shorter_than_n (["an","elephant","is","there"],5))

#ex4:
print("4 ------ Map dictionary")

def get_key_lengths(dictionary):
    key_lengths = list(map(len, dictionary.keys()))
    return key_lengths

lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}
print(get_key_lengths(lang))


#ex5:
print("5 ------ Lambda functions")

def sort_list_tuples(lis):
    res = lis
    res.sort()
    return res
    
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
print(language_scores)
print(sort_list_tuples(language_scores))


#ex6:
print("6 ------ Nested functions")

def square(x):
    return x*x
def triple(x):
    return x**3
def sixth (x):
    return square(triple(x))

print(square(2))
print(triple(2))
print(sixth(2))

#ex7:
print("7 ------ Decorators")

def hello(func):
    def wrapper(*args, **kwargs):
        print("Hello World!")
        result = func(*args, **kwargs)
        return result
    return wrapper

@hello
def square(x):
    return x * x
print(square(5))

#ex8:
print("8 ------The Fibonacci sequence (part 2)")

def fibonacci_rec(n):
    if n <= 1:
        return n
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

def fibonacci_list(n, i=0, fibo_list=[]):
    if i < n:
        fibo_list.append(fibonacci_rec(i))
        fibonacci_list(n, i + 1, fibo_list)
    return fibo_list

print(fibonacci_list(20))



#ex9:
import timeit
print("9 ------ The Fibonacci sequence (part 3)")

def fibo_ex1(n):
    fibonacci_list = [0,1]

    for i in range(n-2):
        fibonacci_list.append(fibonacci_list[i]+fibonacci_list[i+1])

recursive_time = timeit.timeit('fibonacci_rec(20)', globals=globals(), number=10000)
list_time = timeit.timeit('fibonacci_list(20)', globals=globals(), number=10000)

print(f"Recursive Fibonacci Time: {recursive_time:.6f} seconds")
print(f"Fibonacci List Time: {list_time:.6f} seconds") #takes a longer time because it recalculate every time things that already have been calculated
#ex10:
print("10 ------ Class definition")

class Polygon:
    def __init__(self, sides):
        if len(sides) < 3:
            raise ValueError("Minimum 3 sides")
        self.sides = list(sides)

    def get_sides(self):
        return self.sides

    def set_sides(self, sides):
        if len(sides) < 3:
            raise ValueError("Minimum 3 sides")
        self.sides = list(sides)

    def perimeter(self):
        return sum(self.sides)

    def getOrderedSides(self, increasing=True):
        ordered_sides = sorted(self.sides) if increasing else sorted(self.sides, reverse=True)
        return tuple(ordered_sides)

#poly_1 = Polygon((1,2))
poly_2 = Polygon((3,4,6,5))
print("Sides:", poly_2.get_sides())
print("Perimeter:", poly_2.perimeter())
print("Ordered Sides (increasing):", poly_2.getOrderedSides(increasing=True))
print("Ordered Sides (decreasing):", poly_2.getOrderedSides(increasing=False))


#ex11:
print("11 ------ Class inheritance")

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])
        if length <= 0 or width <= 0:
            raise ValueError("Positive values needed")

    def area(self):
        return self.sides[0] * self.sides[1]
        
rectangle = Rectangle(4, 5)
print("Sides:", rectangle.get_sides())
print("Perimeter:", rectangle.perimeter())
print("Area of Rectangle:", rectangle.area())
