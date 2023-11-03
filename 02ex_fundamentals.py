import timeit

# Task 1. Global variables
def f(alist, x):
    new_list = alist[:]
    for i in range(x):
        new_list.append(i)
    return new_list

alist = [1, 2, 3]
ans = f(alist, 5)
print('Task 1')
print(ans)
print(alist)

# Task 2. List comprehension
ans = [x**2 for x in range(10) if x % 2 == 1]
print('Task 2')
print(ans)

# Task 3. Filter list
def filter_list(list_of_words, n):
    return list(filter(lambda word: len(word) < n, list_of_words))

words = ["frknfj", "nd", "dmewjkdiej", "akk", "akrabaka"]
result = filter_list(words, 7)
print('Task 3')
print(result)  

# Task 4. Map dictionary
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
def map_dictionary(dictionary):
    return list(map(lambda key: len(key), dictionary.keys()))
print('Task 4')
print(map_dictionary(lang))

# Task 5. Lambda functions
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda x: x[0])
print('Task 5')
print(language_scores)

# Task 6. Nested functions
def square(num):
    return num**2
def cube(num):
    return num**3
def power_of_6(num):
    return square(cube(num))
print('Task 6')
print(power_of_6(3))

# Task 7. Decorators
def hello(func):
    def wrapper(*args, **kwargs):
        print("Hello World!")
        return func(*args, **kwargs)
    return wrapper

@hello
def square(x):
    return x*x
print('Task 7')
square(4)

# Task 8. The Fibonacci sequence, part 2
def fibonacci(index):
    if index <= 1:
        return index
    else:
        return fibonacci(index-1) + fibonacci(index-2)

print('Task 8')
fibonacci_sequence = [fibonacci(i) for i in range(1,21)]
print(fibonacci_sequence)


# Task 9. The Fibonacci sequence, part 3
def Fibonacci_sequence_ex01():
    Fibonacci_sequence = []
    while len(Fibonacci_sequence) < 20:
        if(len(Fibonacci_sequence) < 2):
            Fibonacci_sequence.append(1)
        else:
            Fibonacci_sequence.append(sum(Fibonacci_sequence[len(Fibonacci_sequence)-2:]))


print('Task 9')
time_1 = timeit.timeit(lambda : Fibonacci_sequence_ex01(), number=1)
print('With loop: ' + str(time_1))
time_2 = timeit.timeit(lambda : [fibonacci(i) for i in range(1,21)], number=1)
print('With recursive: ' + str(time_2))

# Task 10. Class definition
class Polygon:
    def __init__(self, sides):
        if len(sides) < 3:
            raise ValueError("A polygon must have at least 3 sides")
        self._sides = list(sides)

    def getSide(self, index):
        return self._sides[index]

    def setSide(self, index, value):
        self._sides[index] = value

    def perimeter(self):
        return sum(self._sides)

    def getOrderedSides(self, increasing=True):
        return tuple(sorted(self._sides, reverse=not increasing))

print('Task 10')
poly = Polygon((4, 2, 3, 5, 6))
print("Perimeter:", poly.perimeter())
print("Ordered sides (increasing):", poly.getOrderedSides(increasing=True))
print("Ordered sides (decreasing):", poly.getOrderedSides(increasing=False))

# Task 11. Class inheritance
class Rectangle(Polygon):
    def __init__(self, length, breadth):
        super().__init__((length, breadth, length, breadth))
        
    def area(self):
        return self._sides[0] * self._sides[1]
 
print('Task 11')
r = Rectangle(4, 5)
print("Perimeter:", r.perimeter())
print("Area:", r.area()) 
print("Ordered Sides:", r.getOrderedSides(increasing=True))

