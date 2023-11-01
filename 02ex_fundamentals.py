#1
print("\n#1", "\n==========")
def f(alist):
    x = 5
    alist_copy = alist.copy()
    for i in range(x):
        alist_copy.append(i)
    return alist_copy

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed

#2
print("\n#2", "\n==========")
ans = [x*x for x in range(10) if x%2 ==1]
print(ans)

#3
print("\n#3", "\n==========")
words = ["word", "is", "also", "a", "word"]
n = 3

def word_len(word, n):
    return len(word) < n
result = list(filter(lambda word: word_len(word, n), words))
print(result)

#4
print("\n#4", "\n==========")
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

lengths1 = map(len, lang.keys())
print(list(lengths1))

#5
print("\n#5", "\n==========")
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key = lambda x: x[0])
print(language_scores)

#6
print("\n#6", "\n==========")
def sqr(n):
    return n*n
def cube(n):
    return n*n*n
def sixth_power(n):
    return sqr(n)*cube(n)*n

print(sixth_power(1))

#7
print("\n#7", "\n==========")
def hello(func):
    def wrapper(x):
        print("hello world")
        return func(x)
    return wrapper
        
@hello
def square(x):
    return x*x

print(square(2))


#8
print("\n#8", "\n==========")
n = 20

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))
for i in range(n):
    print(fibonacci(i))


#9
print("\n#9", "\n==========")
import timeit

#Fibonacci using for loop
def fibonacci_for_loop(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

#Fibonacci using recursive function
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

for_loop_time = timeit.timeit("fibonacci_for_loop(20)", globals=globals(), number=1000)
recursive_time = timeit.timeit("fibonacci_recursive(20)", globals=globals(), number=1000)

print(f"for-loop Fibonacci Time: {for_loop_time:.6f} seconds")
print(f"Recursive Fibonacci Time: {recursive_time:.6f} seconds")


#10
print("\n#10", "\n==========")
class Polygon:
    def __init__(self, sides: tuple):
        if len(sides) < 3:
            print("number of lengths should be 3 or more")
        else:
            self.sides = sides
    def getlengths(self):
        return self.sides
    def setlengths(self, sides):
        self.sides = sides
        return self.sides
    def perimeter(self):
        return sum(self.sides)
    def getOrderedSides(self, increasing= True):
        if increasing:
            return tuple(sorted(self.sides))
        else:
            return tuple(sorted(self.sides, reverse= not increasing))
    
triangle = (4, 6, 3)
pol = Polygon(triangle)
print(pol.perimeter())
print(pol.getOrderedSides(increasing=True))


#11
print("\n#11", "\n==========")
class Rectangle(Polygon):
    def __init__(self, sides):
        super().__init__(sides)
        self.sides = sides
        
    def area(self):
        sides = self.getOrderedSides()
        return sides[0] * sides[2]

rectangle = (2, 3, 3, 2)
rec = Rectangle(rectangle)
print(rec.area())

