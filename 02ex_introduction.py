
#Exercice1
def f(alist,x):
    #We can define x in this scope too instead of putting it in an argument 
    vlist = alist.copy()
    for i in range(x):
        vlist.append(i)
    return vlist

#Exercice2
def Exercice2():
   
    return [x**2 for x in range(0,10,2)]

#Exercice3
def Exercice3(words,n):
    return list(filter(lambda x : len(x)<n,words))
#Exercice4
def Exercice4():
    lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
    return list(map(lambda x : len(x), lang.keys()))
#Exercice5
def Exercice5():
    language_scores = language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
    return sorted(language_scores, key=lambda x : x[0].upper())
#Exercice6
def square(x):
    return x**2
def cube(x):
    return x**3
def Exercice6(x):
    return cube(square(x))
#Exercice7

def hello(sq):
    def wrapper(*args, **kwargs):
        print("Hello World !")
        return sq(*args, **kwargs)
    return wrapper
@hello
def square(x):
    return x*x

#Exercice8
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq
    
#Exercice9
import timeit

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

def Exercice11(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

time_recursive = timeit.timeit("fibonacci(20)", globals=globals(), number=10000)
time_loop = timeit.timeit("Exercice11(20)", globals=globals(), number=10000)

print("Recursive Function Time:", time_recursive)
print("Loop Function Time:", time_loop)
#The Loop function takes less time 

#Exercice10

class Polygon:
    def __init__(self, sides):
        if len(sides) < 3:
            raise ValueError("You must input at least 3 sides")
        self.sides = list(sides)

    def set_sides(self, sides):
        if len(sides) < 3:
            raise ValueError("You must input at least 3 sides")
        self.sides = list(sides)

    def get_sides(self):
        return self.sides

    def perimeter(self):
        return sum(self.sides)

    def get_ordered_sides(self, increasing=True):
        return tuple(sorted(self.sides, reverse=not increasing))




sides = (1, 2, 3, 4, 5)
poly = Polygon(sides)

print("Sides:", poly.get_sides())
print("Perimeter:", poly.perimeter())
print("Ordered Sides (Increasing):", poly.get_ordered_sides(increasing=True))
print("Ordered Sides (Decreasing):", poly.get_ordered_sides(increasing=False))


#Exercice11
class Rectangle(Polygon):
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Both length and width must be greater than zero")
        super().__init__([length, width, length, width])

    def area(self):
        return self.sides[0] * self.sides[1]



length = 8
width = 7
rect = Rectangle(length, width)

print("Sides:", rect.get_sides())
print("Perimeter:", rect.perimeter())
print("Area:", rect.area())


